#!/usr/bin/env python3
"""
Daily Tweet Publisher

Reads the latest daily tweet file from tweets/ and posts it to Twitter/X.
Runs after the daily-poster agent writes tweets/daily-YYYY-MM-DD.md.

Usage:
    python3 daily_publisher.py
    python3 daily_publisher.py --dry-run

Requires env vars:
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import date
from pathlib import Path

import tweepy
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
TWEETS_DIR = BASE_DIR / "tweets"
PUBLISH_LOG = BASE_DIR / "publish-log.json"

load_dotenv(BASE_DIR / ".env")


def find_todays_tweet() -> Path | None:
    """Find today's daily tweet file."""
    today = date.today().isoformat()
    candidate = TWEETS_DIR / f"daily-{today}.md"
    if candidate.exists() and candidate.stat().st_size > 0:
        return candidate
    return None


def already_posted(tweet_file: Path) -> bool:
    """Check if this daily tweet was already posted."""
    if not PUBLISH_LOG.exists():
        return False
    try:
        log = json.loads(PUBLISH_LOG.read_text())
        for entry in log:
            if entry.get("daily_file") == tweet_file.name and entry.get("tweet_count", 0) > 0:
                print(f"[Twitter] Already posted {tweet_file.name}. Skipping.")
                return True
    except Exception:
        pass
    return False


def parse_daily_tweet(path: Path) -> tuple[dict, list[str]]:
    """Parse frontmatter and tweet text(s) from a daily tweet file."""
    text = path.read_text()

    # Strip YAML frontmatter
    import yaml
    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter found in {path.name}")

    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2).strip()

    # Check if it's a mini-thread (has 1/ 2/ markers) or a single tweet
    thread_pattern = re.compile(r"\d+/\s*(.*?)(?=\n\n\d+/|\Z)", re.DOTALL)
    matches = thread_pattern.findall(body)

    if matches:
        tweets = [m.strip() for m in matches if m.strip()]
    else:
        # Single tweet — whole body is the tweet
        tweets = [body.strip()]

    # Validate length
    for i, tweet in enumerate(tweets, 1):
        if len(tweet) > 280:
            print(f"  WARNING: Tweet {i} is {len(tweet)} chars (over 280)", file=sys.stderr)

    return frontmatter, tweets


def post_tweets(tweets: list[str], dry_run: bool = False) -> list[str]:
    """Post tweet(s) to Twitter/X."""
    try:
        import tweepy
    except ImportError:
        print("  [ERROR] tweepy not installed. Run: pip3 install tweepy", file=sys.stderr)
        sys.exit(1)

    print(f"\n[Twitter] Posting {len(tweets)} tweet(s)")

    if dry_run:
        for i, tweet in enumerate(tweets, 1):
            print(f"  Tweet {i} ({len(tweet)} chars): {tweet[:100]}...")
        print("  [DRY RUN] No tweets posted.")
        return []

    client = tweepy.Client(
        consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
        consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
        access_token=os.environ["TWITTER_ACCESS_TOKEN"],
        access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
    )

    posted_ids = []
    previous_id = None

    for i, tweet_text in enumerate(tweets, 1):
        try:
            kwargs = {"text": tweet_text}
            if previous_id:
                kwargs["in_reply_to_tweet_id"] = previous_id

            response = client.create_tweet(**kwargs)
            tweet_id = response.data["id"]
            posted_ids.append(tweet_id)
            previous_id = tweet_id

            print(f"  Posted tweet {i}/{len(tweets)} (id: {tweet_id})")
            if i < len(tweets):
                time.sleep(2)

        except tweepy.TweepyException as e:
            print(f"  [ERROR] Failed on tweet {i}: {e}", file=sys.stderr)
            break

    return posted_ids


def write_log(tweet_file: Path, frontmatter: dict, tweet_ids: list[str]) -> None:
    """Append daily tweet record to publish-log.json."""
    log = []
    if PUBLISH_LOG.exists():
        try:
            log = json.loads(PUBLISH_LOG.read_text())
        except json.JSONDecodeError:
            log = []

    log.append({
        "timestamp":      __import__("datetime").datetime.now().isoformat(),
        "type":           "daily-tweet",
        "daily_file":     tweet_file.name,
        "day_format":     frontmatter.get("day_format", "unknown"),
        "tweet_count":    len(tweet_ids),
        "first_tweet_id": tweet_ids[0] if tweet_ids else None,
        "tweet_ids":      tweet_ids,
    })

    PUBLISH_LOG.write_text(json.dumps(log, indent=2))
    print(f"\n[Log] Saved to {PUBLISH_LOG.name}")


def main():
    parser = argparse.ArgumentParser(description="Post daily strategy tweet")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN MODE ===")

    tweet_file = find_todays_tweet()
    if not tweet_file:
        print(f"No daily tweet file found for today ({date.today().isoformat()}). Nothing to do.")
        sys.exit(0)

    print(f"Tweet file: {tweet_file.name}")

    if already_posted(tweet_file):
        sys.exit(0)

    frontmatter, tweets = parse_daily_tweet(tweet_file)
    print(f"Format: {frontmatter.get('day_format', 'unknown')}")
    print(f"Tweets: {len(tweets)}")

    tweet_ids = post_tweets(tweets, dry_run=args.dry_run)

    write_log(tweet_file, frontmatter, tweet_ids)
    print("\nDone.")


if __name__ == "__main__":
    main()
