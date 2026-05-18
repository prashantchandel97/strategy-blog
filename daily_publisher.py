#!/usr/bin/env python3
"""
Daily Tweet Publisher

Reads today's daily tweet file from tweets/ and posts it to Twitter/X
after passing a quality gate. Runs after the daily-poster agent.

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
from datetime import date, datetime
from pathlib import Path

import yaml
import tweepy
from dotenv import load_dotenv

BASE_DIR   = Path(__file__).parent
TWEETS_DIR = BASE_DIR / "tweets"
PUBLISH_LOG = BASE_DIR / "publish-log.json"

load_dotenv(BASE_DIR / ".env")

# Characters that must never appear in a posted tweet
BANNED_CHARS = [
    "—",  # em dash —
    "–",  # en dash –
    "‒",  # figure dash
    "―",  # horizontal bar
    "---",     # triple hyphen
]


# ── File discovery ────────────────────────────────────────────────────────────

def find_todays_tweet() -> Path | None:
    today = date.today().isoformat()
    candidate = TWEETS_DIR / f"daily-{today}.md"
    if not candidate.exists() or candidate.stat().st_size == 0:
        return None
    # Agent writes "SKIP" when no good insight exists today
    if candidate.read_text().strip() == "SKIP":
        print(f"[Skip] Agent found no good insight today. Skipping cleanly.")
        return None
    return candidate


def already_posted(tweet_file: Path) -> bool:
    """Two-layer check: publish-log.json AND whether tweets were actually sent."""
    if not PUBLISH_LOG.exists():
        return False
    try:
        log = json.loads(PUBLISH_LOG.read_text())
        for entry in log:
            if (
                entry.get("daily_file") == tweet_file.name
                and entry.get("tweet_count", 0) > 0
                and entry.get("first_tweet_id")  # real tweet ID, not dry-run
            ):
                print(f"[Skip] Already posted {tweet_file.name} "
                      f"(id: {entry['first_tweet_id']})")
                return True
    except Exception:
        pass
    return False


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_daily_tweet(path: Path) -> tuple[dict, list[str]]:
    """Return (frontmatter dict, list of tweet strings)."""
    text = path.read_text()

    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter found in {path.name}")

    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2).strip()

    # Mini-thread: lines like "1/ ...", "2/ ..."
    thread_pattern = re.compile(r"\d+/\s*(.*?)(?=\n\n\d+/|\Z)", re.DOTALL)
    matches = thread_pattern.findall(body)

    if matches:
        tweets = [m.strip() for m in matches if m.strip()]
    else:
        tweets = [body.strip()]

    return frontmatter, tweets


# ── Quality gate ─────────────────────────────────────────────────────────────

def quality_check(tweets: list[str]) -> list[str]:
    """
    Run pre-flight checks. Returns list of failure messages.
    An empty list means the tweet passes and can be posted.
    """
    failures = []

    for i, tweet in enumerate(tweets, 1):
        label = f"Tweet {i}"

        # Length
        if len(tweet) > 280:
            failures.append(f"{label}: {len(tweet)} chars — over 280 limit")

        # Banned characters
        for char in BANNED_CHARS:
            if char in tweet:
                name = {
                    "—": "em dash (—)",
                    "–": "en dash (–)",
                    "‒": "figure dash",
                    "―": "horizontal bar",
                    "---":    "triple hyphen",
                }.get(char, repr(char))
                failures.append(f"{label}: contains banned character: {name}")

        # Empty tweet
        if not tweet.strip():
            failures.append(f"{label}: empty")

        # Hashtags (should only be in Sunday thread)
        if "#" in tweet:
            failures.append(f"{label}: contains hashtag — daily posts should not have hashtags")

    # Thread length
    if len(tweets) > 3:
        failures.append(f"Thread has {len(tweets)} tweets — daily posts max 3")

    return failures


# ── Posting ───────────────────────────────────────────────────────────────────

def post_tweets(tweets: list[str], dry_run: bool = False) -> list[str]:
    print(f"\n[Twitter] Posting {len(tweets)} tweet(s)")

    if dry_run:
        for i, tweet in enumerate(tweets, 1):
            print(f"  [{len(tweet)} chars] {tweet}")
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
            print(f"  Posted {i}/{len(tweets)} (id: {tweet_id})")
            if i < len(tweets):
                time.sleep(2)

        except tweepy.TweepyException as e:
            print(f"  [ERROR] Failed on tweet {i}: {e}", file=sys.stderr)
            break

    return posted_ids


# ── Logging ───────────────────────────────────────────────────────────────────

def write_log(tweet_file: Path, frontmatter: dict, tweet_ids: list[str],
              quality_failures: list[str] = None) -> None:
    log = []
    if PUBLISH_LOG.exists():
        try:
            log = json.loads(PUBLISH_LOG.read_text())
        except json.JSONDecodeError:
            log = []

    entry = {
        "timestamp":      datetime.now().isoformat(),
        "type":           "daily-tweet",
        "daily_file":     tweet_file.name,
        "day_format":     frontmatter.get("day_format", "unknown"),
        "domain":         frontmatter.get("domain", "unknown"),
        "tweet_count":    len(tweet_ids),
        "first_tweet_id": tweet_ids[0] if tweet_ids else None,
        "tweet_ids":      tweet_ids,
    }
    if quality_failures:
        entry["quality_blocked"] = True
        entry["quality_failures"] = quality_failures

    log.append(entry)
    PUBLISH_LOG.write_text(json.dumps(log, indent=2))
    print(f"[Log] Saved to {PUBLISH_LOG.name}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Post daily strategy tweet")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN MODE ===")

    # Find tweet file
    tweet_file = find_todays_tweet()
    if not tweet_file:
        print(f"[Skip] No tweet file for today ({date.today().isoformat()}). "
              f"Agent may not have found a good insight — skipping cleanly.")
        sys.exit(0)

    print(f"Tweet file: {tweet_file.name}")

    # Deduplication
    if already_posted(tweet_file):
        sys.exit(0)

    # Parse
    frontmatter, tweets = parse_daily_tweet(tweet_file)
    print(f"Format: {frontmatter.get('day_format', 'unknown')}")
    print(f"Domain: {frontmatter.get('domain', 'unknown')}")
    print(f"Tweets: {len(tweets)}")
    for i, t in enumerate(tweets, 1):
        print(f"  [{len(t)} chars] {t[:120]}{'...' if len(t) > 120 else ''}")

    # Quality gate
    failures = quality_check(tweets)
    if failures:
        print(f"\n[BLOCKED] Quality gate failed — tweet will not be posted:")
        for f in failures:
            print(f"  - {f}")
        write_log(tweet_file, frontmatter, [], quality_failures=failures)
        print("\nFix the tweet file and re-run, or it will be skipped today.")
        sys.exit(1)

    print("\n[OK] Quality gate passed.")

    # Post
    tweet_ids = post_tweets(tweets, dry_run=args.dry_run)
    write_log(tweet_file, frontmatter, tweet_ids)
    print("\nDone.")


if __name__ == "__main__":
    main()
