#!/usr/bin/env python3
"""
Engagement Tracker

Runs Monday morning after each weekend's thread is posted.
Reads tweet IDs from publish-log.json, fetches metrics from Twitter API v2,
and writes analytics/weekly/week-YYYY-MM-DD.json.

Usage:
    python3 engagement_tracker.py

Requires .env with:
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
"""

import json
import os
import sys
from pathlib import Path

import tweepy
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
ANALYTICS_DIR = BASE_DIR / "analytics" / "weekly"
PUBLISH_LOG = BASE_DIR / "publish-log.json"

load_dotenv(BASE_DIR / ".env")


def get_client():
    return tweepy.Client(
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )


def get_latest_untracked_entry() -> dict | None:
    """Find the most recent publish-log entry with tweets that has no analytics file yet."""
    if not PUBLISH_LOG.exists():
        print("No publish-log.json found.")
        return None

    log = json.loads(PUBLISH_LOG.read_text())

    for entry in reversed(log):
        tweet_ids = entry.get("tweet_ids", [])
        if not tweet_ids:
            continue
        blog_date = entry.get("blog_file", "")[:10]
        if not blog_date:
            continue
        analytics_file = ANALYTICS_DIR / f"week-{blog_date}.json"
        if not analytics_file.exists():
            return entry

    return None


def fetch_tweet_metrics(client: tweepy.Client, tweet_ids: list[str]) -> list[dict]:
    """Fetch public metrics for each tweet in the thread."""
    if not tweet_ids:
        return []

    try:
        response = client.get_tweets(
            ids=tweet_ids,
            tweet_fields=["public_metrics", "text", "created_at"],
        )
    except tweepy.Unauthorized:
        print("  [ERROR] Twitter API returned 401 Unauthorized.")
        print("  Check that your Twitter app has Read permissions enabled at developer.twitter.com")
        print("  App settings -> User authentication settings -> Permissions -> Read")
        print("  After changing permissions, regenerate your access tokens and update GitHub Secrets.")
        return []
    except tweepy.TweepyException as e:
        print(f"  [ERROR] Twitter API error: {e}")
        return []

    if not response.data:
        print("  [WARNING] No tweet data returned from API.")
        return []

    # Re-order results to match original thread order
    by_id = {str(t.id): t for t in response.data}
    metrics = []
    for tid in tweet_ids:
        tweet = by_id.get(str(tid))
        if not tweet:
            continue
        m = tweet.public_metrics or {}
        metrics.append({
            "id": str(tweet.id),
            "text_preview": tweet.text[:120],
            "impressions":  m.get("impression_count", 0),
            "likes":        m.get("like_count", 0),
            "retweets":     m.get("retweet_count", 0),
            "replies":      m.get("reply_count", 0),
            "quotes":       m.get("quote_count", 0),
            "bookmarks":    m.get("bookmark_count", 0),
        })

    return metrics


def fetch_follower_count(client: tweepy.Client) -> int:
    try:
        response = client.get_me(user_fields=["public_metrics"])
        return response.data.public_metrics.get("followers_count", 0)
    except Exception as e:
        print(f"  [WARNING] Could not fetch follower count: {e}")
        return 0


def engagement_score(metrics: list[dict]) -> float:
    """Weighted engagement rate: (likes + 3x RTs + 2x replies + 4x quotes + 2x bookmarks) / impressions."""
    total_impressions = sum(m["impressions"] for m in metrics)
    if total_impressions == 0:
        return 0.0
    weighted = sum(
        m["likes"] * 1 +
        m["retweets"] * 3 +
        m["replies"] * 2 +
        m["quotes"] * 4 +
        m["bookmarks"] * 2
        for m in metrics
    )
    return round(weighted / total_impressions * 100, 3)


def write_analytics(entry: dict, tweet_metrics: list[dict], follower_count: int) -> dict:
    ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)

    blog_date = entry.get("blog_file", "")[:10]
    analytics_file = ANALYTICS_DIR / f"week-{blog_date}.json"

    hook = tweet_metrics[0] if tweet_metrics else {}
    total_impressions = sum(m["impressions"] for m in tweet_metrics)

    # Completion rate: did people make it to tweet 5+?
    completion_rate = None
    if len(tweet_metrics) >= 5 and hook.get("impressions", 0) > 0:
        completion_rate = round(
            tweet_metrics[4]["impressions"] / hook["impressions"] * 100, 1
        )

    data = {
        "blog_file":           entry["blog_file"],
        "blog_date":           blog_date,
        "posted_at":           entry.get("timestamp"),
        "follower_count":      follower_count,
        "tweet_count":         len(tweet_metrics),
        "total_impressions":   total_impressions,
        "hook_impressions":    hook.get("impressions", 0),
        "completion_rate_pct": completion_rate,
        "totals": {
            "likes":     sum(m["likes"]     for m in tweet_metrics),
            "retweets":  sum(m["retweets"]  for m in tweet_metrics),
            "replies":   sum(m["replies"]   for m in tweet_metrics),
            "quotes":    sum(m["quotes"]    for m in tweet_metrics),
            "bookmarks": sum(m["bookmarks"] for m in tweet_metrics),
        },
        "engagement_score": engagement_score(tweet_metrics),
        "tweets": tweet_metrics,
    }

    analytics_file.write_text(json.dumps(data, indent=2))
    print(f"  Written: {analytics_file.name}")
    return data


def main():
    print("\n=== Engagement Tracker ===")

    entry = get_latest_untracked_entry()
    if not entry:
        print("No untracked entries with tweet IDs. Nothing to do.")
        return

    print(f"Tracking: {entry['blog_file']}")
    tweet_ids = entry.get("tweet_ids", [])

    client = get_client()

    print(f"  Fetching metrics for {len(tweet_ids)} tweets...")
    tweet_metrics = fetch_tweet_metrics(client, tweet_ids)

    print("  Fetching follower count...")
    follower_count = fetch_follower_count(client)

    data = write_analytics(entry, tweet_metrics, follower_count)

    print(f"\n  Hook impressions:    {data['hook_impressions']:,}")
    print(f"  Total impressions:   {data['total_impressions']:,}")
    print(f"  Likes:               {data['totals']['likes']:,}")
    print(f"  Retweets:            {data['totals']['retweets']:,}")
    print(f"  Replies:             {data['totals']['replies']:,}")
    print(f"  Bookmarks:           {data['totals']['bookmarks']:,}")
    if data["completion_rate_pct"] is not None:
        print(f"  Completion rate:     {data['completion_rate_pct']}%")
    print(f"  Engagement score:    {data['engagement_score']}")
    print(f"  Follower count:      {follower_count:,}")
    print("\nDone.")


if __name__ == "__main__":
    main()
