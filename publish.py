#!/usr/bin/env python3
"""
Strategy Blog Publisher

Reads the latest blog and tweet thread from blogs/, publishes to:
  1. prashant-chandel.org via /api/n8n/posts
  2. Twitter/X as a threaded reply chain

Usage:
    python3 publish.py                  # publish latest blog + tweet thread
    python3 publish.py --blog-only      # skip Twitter
    python3 publish.py --twitter-only   # skip blog
    python3 publish.py --dry-run        # print what would be posted, don't post

Requires .env with:
    N8N_API_KEY, BLOG_API_URL,
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests
import yaml
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
BLOGS_DIR = BASE_DIR / "blogs"

load_dotenv(BASE_DIR / ".env")

# ──────────────────────────────────────────────
# File discovery
# ──────────────────────────────────────────────

def find_latest_blog() -> Path:
    """Return the most recently dated blog post (YYYY-MM-DD-*.md, not a tweet-thread)."""
    import re as _re
    date_pattern = _re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    candidates = [
        f for f in BLOGS_DIR.glob("*.md")
        if date_pattern.match(f.name)
        and "tweet-thread" not in f.name
        and "infographic" not in f.name
        and f.stat().st_size > 0
    ]
    if not candidates:
        raise FileNotFoundError(f"No dated blog files found in {BLOGS_DIR}")
    # Sort by filename (date prefix) — most reliable, not mtime
    return max(candidates, key=lambda f: f.name)


def find_tweet_thread_for(blog_path: Path) -> Path:
    """Return the tweet thread file that corresponds to the given blog."""
    date_prefix = blog_path.stem[:10]  # YYYY-MM-DD
    thread_path = BLOGS_DIR / f"{date_prefix}-tweet-thread.md"
    if not thread_path.exists():
        candidates = list(BLOGS_DIR.glob(f"{date_prefix}*tweet-thread*.md"))
        if not candidates:
            raise FileNotFoundError(f"No tweet thread found for {blog_path.name}")
        return candidates[0]
    return thread_path


def find_infographic_for(blog_path: Path) -> Path | None:
    """Return the SVG infographic file for the given blog, or None if not found."""
    date_prefix = blog_path.stem[:10]
    svg_path = BLOGS_DIR / f"{date_prefix}-infographic.svg"
    return svg_path if svg_path.exists() else None


def svg_to_png(svg_path: Path) -> Path | None:
    """Convert SVG to PNG using cairosvg. Returns PNG path or None on failure."""
    try:
        import cairosvg
    except ImportError:
        print("  [INFO] cairosvg not installed — skipping infographic image. Run: pip3 install cairosvg", file=sys.stderr)
        return None

    png_path = svg_path.with_suffix(".png")
    try:
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=800,
        )
        print(f"  Converted infographic: {png_path.name}")
        return png_path
    except Exception as e:
        print(f"  [WARNING] SVG→PNG conversion failed: {e}", file=sys.stderr)
        return None


# ──────────────────────────────────────────────
# Parsing
# ──────────────────────────────────────────────

def parse_blog(path: Path) -> dict:
    """Extract YAML frontmatter and markdown body from a blog file."""
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter found in {path.name}")

    frontmatter = yaml.safe_load(match.group(1))
    content = match.group(2).strip()

    date_raw = frontmatter.get("date", datetime.now().isoformat())
    if isinstance(date_raw, datetime):
        date_str = date_raw.isoformat()
    else:
        date_str = str(date_raw)

    slug = path.stem  # e.g. 2026-04-04-ai-margin-is-the-moat

    return {
        "title":   frontmatter.get("title", path.stem),
        "slug":    slug,
        "date":    date_str,
        "type":    frontmatter.get("type", "article"),
        "tags":    frontmatter.get("tags", ["Strategy", "AI", "Business"]),
        "summary": frontmatter.get("summary", ""),
        "content": content,
        "status":  frontmatter.get("status", "published"),
    }


def parse_tweet_thread(path: Path) -> list[str]:
    """
    Extract individual tweets from the thread file.
    Handles formats:
      🧵 1/ text
      2/ text
    """
    text = path.read_text()

    # Strip YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)

    # Strip the heading line (# Tweet Thread: ...)
    text = re.sub(r"^#.*\n", "", text, flags=re.MULTILINE).strip()

    # Match numbered tweets: optional emoji + number + slash
    pattern = re.compile(r"(?:🧵\s*)?\d+/\s*(.*?)(?=\n\n(?:🧵\s*)?\d+/|\Z)", re.DOTALL)
    matches = pattern.findall(text)

    tweets = [m.strip() for m in matches if m.strip()]

    if not tweets:
        raise ValueError(f"Could not parse any tweets from {path.name}")

    # Validate 280-char limit, warn but don't fail
    for i, tweet in enumerate(tweets, 1):
        if len(tweet) > 280:
            print(f"  WARNING: Tweet {i} is {len(tweet)} chars (over 280)", file=sys.stderr)

    return tweets


# ──────────────────────────────────────────────
# Blog publishing
# ──────────────────────────────────────────────

def publish_blog(blog_data: dict, dry_run: bool = False) -> dict:
    """POST the blog to the website API."""
    api_url = os.environ.get("BLOG_API_URL", "https://www.prashant-chandel.org/api/n8n/posts")

    print(f"\n[Blog] Publishing: {blog_data['title']}")
    print(f"       Slug:   {blog_data['slug']}")
    print(f"       Date:   {blog_data['date']}")
    print(f"       Status: {blog_data['status']}")

    if dry_run:
        print("  [DRY RUN] Would POST to", api_url)
        return {"dry_run": True, "slug": blog_data["slug"]}

    api_key = os.environ["N8N_API_KEY"]

    resp = requests.post(
        api_url,
        json=blog_data,
        headers={
            "x-api-key": api_key,
            "Content-Type": "application/json",
        },
        timeout=30,
    )

    if resp.status_code == 409:
        print(f"  Blog already exists (slug conflict). Skipping.")
        return {"skipped": True, "reason": "slug_conflict"}

    resp.raise_for_status()
    result = resp.json()
    print(f"  Published. Post ID: {result.get('post', {}).get('id', 'unknown')}")
    return result


# ──────────────────────────────────────────────
# Twitter publishing
# ──────────────────────────────────────────────

def publish_tweet_thread(tweets: list[str], png_path: Path | None = None, dry_run: bool = False) -> list[str]:
    """Post a tweet thread. Attaches infographic PNG to tweet 1 if provided."""
    try:
        import tweepy
    except ImportError:
        print("  [ERROR] tweepy not installed. Run: pip3 install tweepy", file=sys.stderr)
        sys.exit(1)

    consumer_key        = os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret     = os.environ["TWITTER_CONSUMER_SECRET"]
    access_token        = os.environ["TWITTER_ACCESS_TOKEN"]
    access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    print(f"\n[Twitter] Posting {len(tweets)}-tweet thread" +
          (" + infographic image" if png_path else ""))

    if dry_run:
        for i, tweet in enumerate(tweets, 1):
            suffix = " [+ image]" if i == 1 and png_path else ""
            print(f"  Tweet {i} ({len(tweet)} chars){suffix}: {tweet[:80]}...")
        print("  [DRY RUN] No tweets posted.")
        return []

    # v1.1 API needed for media upload
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api_v1 = tweepy.API(auth)

    # v2 client for creating tweets
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    # Upload infographic if available
    media_id = None
    if png_path and png_path.exists():
        try:
            media = api_v1.media_upload(filename=str(png_path))
            media_id = media.media_id
            print(f"  Uploaded infographic (media_id: {media_id})")
        except Exception as e:
            print(f"  [WARNING] Image upload failed: {e} — posting without image", file=sys.stderr)

    posted_ids = []
    previous_id = None

    for i, tweet_text in enumerate(tweets, 1):
        try:
            kwargs = {"text": tweet_text}
            if previous_id:
                kwargs["in_reply_to_tweet_id"] = previous_id
            # Attach image to tweet 1 only
            if i == 1 and media_id:
                kwargs["media_ids"] = [media_id]

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

    print(f"  Thread posted. First tweet ID: {posted_ids[0] if posted_ids else 'none'}")
    return posted_ids


# ──────────────────────────────────────────────
# Result logging
# ──────────────────────────────────────────────

def write_publish_log(blog_path: Path, blog_result: dict, tweet_ids: list[str]):
    """Append a publish record to publish-log.json."""
    log_path = BASE_DIR / "publish-log.json"
    log = []
    if log_path.exists():
        try:
            log = json.loads(log_path.read_text())
        except json.JSONDecodeError:
            log = []

    log.append({
        "timestamp":     datetime.now().isoformat(),
        "blog_file":     blog_path.name,
        "blog_slug":     blog_result.get("post", {}).get("slug") or blog_result.get("slug"),
        "blog_status":   "skipped" if blog_result.get("skipped") else ("dry_run" if blog_result.get("dry_run") else "published"),
        "tweet_count":   len(tweet_ids),
        "first_tweet_id": tweet_ids[0] if tweet_ids else None,
    })

    log_path.write_text(json.dumps(log, indent=2))
    print(f"\n[Log] Saved to {log_path.name}")


# ──────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Publish strategy blog and tweet thread")
    parser.add_argument("--blog-only",    action="store_true", help="Skip Twitter posting")
    parser.add_argument("--twitter-only", action="store_true", help="Skip blog publishing")
    parser.add_argument("--dry-run",      action="store_true", help="Preview without posting")
    parser.add_argument("--blog-file",    type=str, default=None, help="Specific blog file to publish")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN MODE ===")

    # Find files
    blog_path = Path(args.blog_file) if args.blog_file else find_latest_blog()
    print(f"Blog file:   {blog_path.name}")

    tweet_path = find_tweet_thread_for(blog_path)
    print(f"Tweet file:  {tweet_path.name}")

    blog_result = {}
    tweet_ids = []

    # Find infographic SVG and convert to PNG
    svg_path = find_infographic_for(blog_path)
    png_path = svg_to_png(svg_path) if svg_path else None
    if svg_path and not png_path:
        print(f"  [INFO] No infographic PNG — tweets will post without image")

    # Publish blog
    if not args.twitter_only:
        blog_data = parse_blog(blog_path)
        blog_result = publish_blog(blog_data, dry_run=args.dry_run)

    # Publish tweet thread
    if not args.blog_only:
        required = ["TWITTER_CONSUMER_KEY", "TWITTER_CONSUMER_SECRET",
                    "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_TOKEN_SECRET"]
        missing = [k for k in required if not os.environ.get(k)]
        if missing:
            print(f"\n[Twitter] Skipping — missing env vars: {', '.join(missing)}")
        else:
            tweets = parse_tweet_thread(tweet_path)
            tweet_ids = publish_tweet_thread(tweets, png_path=png_path, dry_run=args.dry_run)

    # Log result
    write_publish_log(blog_path, blog_result, tweet_ids)
    print("\nDone.")


if __name__ == "__main__":
    main()
