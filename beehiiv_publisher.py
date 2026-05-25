#!/usr/bin/env python3
"""
Beehiiv Newsletter Publisher

Converts the latest blog post to HTML and creates a draft in Beehiiv.
The draft must be manually reviewed and sent from the Beehiiv dashboard.

Usage:
    python3 beehiiv_publisher.py
    python3 beehiiv_publisher.py --dry-run

Requires env vars:
    BEEHIIV_API_KEY          — from beehiiv.com/settings/integrations
    BEEHIIV_PUBLICATION_ID   — from your publication URL (pub_xxxxxxx)

Setup:
    1. Create account at beehiiv.com
    2. Create a publication
    3. Go to Settings > Integrations > API to get your API key
    4. Your publication ID is in the URL: app.beehiiv.com/publications/pub_xxxxx
    5. Add both as GitHub secrets: BEEHIIV_API_KEY, BEEHIIV_PUBLICATION_ID
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import requests
import yaml
from dotenv import load_dotenv

BASE_DIR    = Path(__file__).parent
BLOGS_DIR   = BASE_DIR / "blogs"
PUBLISH_LOG = BASE_DIR / "publish-log.json"
AUDIO_CACHE = BASE_DIR / "audio-cache.json"

load_dotenv(BASE_DIR / ".env")

BEEHIIV_API_BASE = "https://api.beehiiv.com/v2"


# ── File discovery ────────────────────────────────────────────────────────────

def find_latest_blog() -> Path | None:
    date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
    candidates = [
        f for f in BLOGS_DIR.glob("*.md")
        if date_pattern.match(f.name)
        and "tweet-thread" not in f.name
        and "contrarian" not in f.name
        and "infographic" not in f.name
        and f.stat().st_size > 0
    ]
    if not candidates:
        return None
    return max(candidates, key=lambda f: f.name)


def already_published(blog_path: Path) -> bool:
    if not PUBLISH_LOG.exists():
        return False
    try:
        log = json.loads(PUBLISH_LOG.read_text())
        for entry in log:
            if entry.get("blog_file") == blog_path.name and entry.get("beehiiv_post_id"):
                print(f"[Skip] Already published to Beehiiv: {entry['beehiiv_post_id']}")
                return True
    except Exception:
        pass
    return False


def get_audio_url() -> str | None:
    if not AUDIO_CACHE.exists():
        return None
    try:
        return json.loads(AUDIO_CACHE.read_text()).get("audio_url")
    except Exception:
        return None


# ── Parsing ───────────────────────────────────────────────────────────────────

def parse_blog(path: Path) -> tuple[dict, str]:
    """Return (frontmatter dict, markdown body)."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        raise ValueError(f"No frontmatter in {path.name}")
    fm = yaml.safe_load(match.group(1))
    body = match.group(2).strip()
    return fm, body


def markdown_to_html(markdown_body: str, cover_png_url: str | None, audio_url: str | None) -> str:
    """Convert markdown to newsletter-ready HTML."""
    try:
        import markdown as md_lib
        body_html = md_lib.markdown(
            markdown_body,
            extensions=["extra", "nl2br"],
        )
    except ImportError:
        # Fallback: basic conversion
        body_html = "<p>" + markdown_body.replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>"

    # Remove SVG blocks (email clients can't render them)
    body_html = re.sub(r'<div[^>]*>.*?<svg[\s\S]*?</svg>.*?</div>', '', body_html, flags=re.IGNORECASE)
    body_html = re.sub(r'<svg[\s\S]*?</svg>', '', body_html, flags=re.IGNORECASE)

    # Build the full email HTML
    cover_section = ""
    if cover_png_url:
        cover_section = f"""
        <div style="margin-bottom: 32px;">
          <img src="{cover_png_url}" alt="Article cover"
               style="width: 100%; border-radius: 8px; display: block;" />
        </div>"""

    audio_section = ""
    if audio_url:
        audio_section = f"""
        <div style="background: #F0F4FF; border-left: 4px solid #2563EB; border-radius: 6px;
                    padding: 16px 20px; margin: 24px 0; font-family: system-ui, sans-serif;">
          <p style="margin: 0; font-size: 14px; color: #1E3A5F; font-weight: 600;">
            🎧 Prefer to listen?
          </p>
          <p style="margin: 8px 0 0; font-size: 14px; color: #475569;">
            <a href="{audio_url}" style="color: #2563EB;">Download the audio version</a>
            of this article (AI-narrated, ~12 min).
          </p>
        </div>"""

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body style="font-family: Georgia, 'Times New Roman', serif; color: #1a1a1a; max-width: 680px;
             margin: 0 auto; padding: 24px 16px; background: #ffffff; line-height: 1.7;">

  {cover_section}
  {audio_section}

  <div style="font-family: system-ui, -apple-system, sans-serif;">
    {body_html}
  </div>

  <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 40px 0;">
  <p style="font-size: 13px; color: #9ca3af; font-family: system-ui, sans-serif; text-align: center;">
    Read more at
    <a href="https://prashant-chandel.org/blog" style="color: #2563EB;">prashant-chandel.org/blog</a>
  </p>

</body>
</html>"""

    return html


# ── Beehiiv API ───────────────────────────────────────────────────────────────

def create_beehiiv_draft(title: str, subtitle: str, html: str, dry_run: bool = False) -> str | None:
    """Create a draft post in Beehiiv. Returns the post ID."""
    api_key = os.environ.get("BEEHIIV_API_KEY", "")
    pub_id  = os.environ.get("BEEHIIV_PUBLICATION_ID", "")

    if not api_key or not pub_id:
        print("[Error] BEEHIIV_API_KEY or BEEHIIV_PUBLICATION_ID not set", file=sys.stderr)
        return None

    if dry_run:
        print(f"\n=== DRY RUN — Beehiiv draft ===")
        print(f"  Title: {title}")
        print(f"  Subtitle: {subtitle}")
        print(f"  HTML length: {len(html):,} chars")
        print("=== END DRY RUN ===")
        return "dry-run-id"

    payload = {
        "status":           "draft",
        "send_newsletter":  False,      # user sends manually from Beehiiv dashboard
        "subject":          title,
        "subtitle":         subtitle,
        "content": {
            "free": {
                "type": "html",
                "html": html,
            }
        },
        "displayed_date": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    resp = requests.post(
        f"{BEEHIIV_API_BASE}/publications/{pub_id}/posts",
        json=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type":  "application/json",
        },
        timeout=30,
    )

    if not resp.ok:
        print(f"[Error] Beehiiv API: {resp.status_code} — {resp.text[:300]}", file=sys.stderr)
        return None

    post_id = resp.json().get("data", {}).get("id", "unknown")
    print(f"  Beehiiv draft created: {post_id}")
    return post_id


def update_publish_log(blog_path: Path, beehiiv_post_id: str) -> None:
    log = []
    if PUBLISH_LOG.exists():
        try:
            log = json.loads(PUBLISH_LOG.read_text())
        except json.JSONDecodeError:
            log = []

    # Find existing entry for this blog and add beehiiv_post_id
    for entry in log:
        if entry.get("blog_file") == blog_path.name:
            entry["beehiiv_post_id"] = beehiiv_post_id
            PUBLISH_LOG.write_text(json.dumps(log, indent=2))
            print(f"[Log] Updated publish-log.json with Beehiiv post ID")
            return

    # No existing entry — append a new one
    log.append({
        "timestamp":       datetime.now().isoformat(),
        "blog_file":       blog_path.name,
        "beehiiv_post_id": beehiiv_post_id,
    })
    PUBLISH_LOG.write_text(json.dumps(log, indent=2))
    print(f"[Log] Appended Beehiiv entry to publish-log.json")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Publish blog to Beehiiv as newsletter draft")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.dry_run:
        print("=== DRY RUN MODE ===")

    blog_path = find_latest_blog()
    if not blog_path:
        print("[Skip] No blog file found.")
        sys.exit(0)

    print(f"Blog: {blog_path.name}")

    if already_published(blog_path):
        sys.exit(0)

    fm, body = parse_blog(blog_path)
    title    = fm.get("title", blog_path.stem)
    subtitle = fm.get("summary", "")

    # Find cover PNG URL (committed to GitHub by publisher.py)
    date_prefix   = blog_path.stem[:10]
    cover_png_url = None
    cover_png     = BLOGS_DIR / f"{date_prefix}-cover.png"
    if cover_png.exists():
        # Build raw GitHub URL
        try:
            import subprocess
            remote = subprocess.run(["git", "remote", "get-url", "origin"],
                                    capture_output=True, text=True).stdout.strip()
            repo = remote.replace("https://github.com/", "").replace(".git", "")
            cover_png_url = f"https://raw.githubusercontent.com/{repo}/main/blogs/{cover_png.name}"
        except Exception:
            pass

    audio_url = get_audio_url()

    print(f"\n[HTML] Converting markdown to email HTML...")
    html = markdown_to_html(body, cover_png_url=cover_png_url, audio_url=audio_url)
    print(f"  HTML: {len(html):,} chars")

    print(f"\n[Beehiiv] Creating draft...")
    post_id = create_beehiiv_draft(title, subtitle, html, dry_run=args.dry_run)

    if post_id and not args.dry_run:
        update_publish_log(blog_path, post_id)
        print(f"\n[Done] Draft ready in Beehiiv. Review and send from your dashboard.")
        print(f"       app.beehiiv.com → Posts → Drafts")
    elif args.dry_run:
        print("\n[Done] Dry run complete.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
