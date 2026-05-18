#!/usr/bin/env python3
"""
Engagement Tracker

Runs Monday morning after each weekend's thread is posted.
Tracks follower count week-over-week (free Twitter API tier).

Tweet-level metrics (impressions, likes, retweets) require Twitter API Basic
tier ($100/month) and are not tracked here. Check analytics.twitter.com manually
and paste numbers into the generated JSON if you want them recorded.

Usage:
    python3 engagement_tracker.py

Requires env vars (or .env):
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
"""

import json
import os
from datetime import date
from pathlib import Path

import tweepy
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
ANALYTICS_DIR = BASE_DIR / "analytics" / "weekly"
PUBLISH_LOG = BASE_DIR / "publish-log.json"

load_dotenv(BASE_DIR / ".env")


def get_client() -> tweepy.Client:
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
        if not entry.get("tweet_ids"):
            continue
        blog_date = entry.get("blog_file", "")[:10]
        if not blog_date:
            continue
        if not (ANALYTICS_DIR / f"week-{blog_date}.json").exists():
            return entry
    return None


def fetch_follower_count(client: tweepy.Client) -> int:
    try:
        response = client.get_me(user_fields=["public_metrics"])
        count = response.data.public_metrics.get("followers_count", 0)
        print(f"  Follower count: {count:,}")
        return count
    except Exception as e:
        print(f"  [WARNING] Could not fetch follower count: {e}")
        return 0


def previous_follower_count() -> int:
    """Read last week's follower count from the most recent analytics file."""
    files = sorted(ANALYTICS_DIR.glob("week-*.json"))
    for f in reversed(files):
        try:
            data = json.loads(f.read_text())
            fc = data.get("follower_count", 0)
            if fc:
                return fc
        except Exception:
            continue
    return 0


def write_analytics(entry: dict, follower_count: int, prev_followers: int) -> None:
    ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)
    blog_date = entry.get("blog_file", "")[:10]

    data = {
        "blog_file":       entry["blog_file"],
        "blog_date":       blog_date,
        "tracked_on":      date.today().isoformat(),
        "follower_count":  follower_count,
        "follower_delta":  follower_count - prev_followers if prev_followers else None,
        "note":            "Tweet metrics (impressions, likes, retweets) require Twitter API Basic tier. Check analytics.twitter.com and paste manually if needed.",
        "tweet_metrics": {
            "impressions":      None,
            "likes":            None,
            "retweets":         None,
            "replies":          None,
            "bookmarks":        None,
            "completion_rate":  None,
            "engagement_score": None,
        },
    }

    out = ANALYTICS_DIR / f"week-{blog_date}.json"
    out.write_text(json.dumps(data, indent=2))
    print(f"  Written: {out.name}")

    if data["follower_delta"] is not None:
        sign = "+" if data["follower_delta"] >= 0 else ""
        print(f"  Follower delta: {sign}{data['follower_delta']} (from {prev_followers:,} to {follower_count:,})")


def main():
    print("\n=== Engagement Tracker ===")

    entry = get_latest_untracked_entry()
    if not entry:
        print("No untracked entries. Nothing to do.")
        return

    print(f"Tracking: {entry['blog_file']}")

    client = get_client()
    prev = previous_follower_count()
    followers = fetch_follower_count(client)
    write_analytics(entry, followers, prev)

    print("\nDone. For tweet metrics, visit: https://analytics.twitter.com")


if __name__ == "__main__":
    main()
