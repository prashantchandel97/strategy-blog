#!/usr/bin/env python3
"""
Audio Generator

Converts the latest blog post to MP3 using ElevenLabs, uploads to GitHub Releases,
and writes the URL to audio-cache.json for publish.py to include in the blog API call.

Usage:
    python3 audio_generator.py
    python3 audio_generator.py --dry-run

Requires env vars:
    ELEVENLABS_API_KEY
    GITHUB_TOKEN  (automatically available in GitHub Actions)

Optional env vars:
    ELEVENLABS_VOICE_ID  (defaults to Rachel: 21m00Tcm4TlvDq8ikWAM)
    ELEVENLABS_MODEL_ID  (defaults to eleven_multilingual_v2)

Note on costs: a 2500-word blog is ~15,000 characters.
  - Starter plan ($5/mo): 30,000 chars/mo = ~2 posts/mo
  - Creator plan ($22/mo): 100,000 chars/mo = ~6 posts/mo
  - Pro plan ($99/mo): 500,000 chars/mo = unlimited weekly posts
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE_DIR    = Path(__file__).parent
BLOGS_DIR   = BASE_DIR / "blogs"
AUDIO_CACHE = BASE_DIR / "audio-cache.json"

load_dotenv(BASE_DIR / ".env")

DEFAULT_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"   # Rachel — clear, professional
DEFAULT_MODEL_ID = "eleven_multilingual_v2"
MAX_CHARS_PER_CHUNK = 4500


# ── Blog discovery ────────────────────────────────────────────────────────────

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


def already_generated(blog_path: Path) -> str | None:
    """Return cached audio URL if already generated for this blog."""
    if not AUDIO_CACHE.exists():
        return None
    try:
        data = json.loads(AUDIO_CACHE.read_text())
        if data.get("blog_file") == blog_path.name:
            url = data.get("audio_url")
            print(f"[Cache] Already generated audio for {blog_path.name}: {url}")
            return url
    except Exception:
        pass
    return None


# ── Text extraction ───────────────────────────────────────────────────────────

def extract_readable_text(blog_path: Path) -> str:
    """Strip markdown syntax and return clean prose suitable for TTS."""
    text = blog_path.read_text(encoding="utf-8")

    # Remove YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)

    # Remove SVG and HTML blocks entirely
    text = re.sub(r"<svg[\s\S]*?</svg>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<div[\s\S]*?</div>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)

    # Remove markdown headings — keep the text, lose the #
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

    # Remove bold/italic markers
    text = re.sub(r"\*{1,3}([^*\n]+)\*{1,3}", r"\1", text)
    text = re.sub(r"_{1,2}([^_\n]+)_{1,2}", r"\1", text)

    # Convert links [text](url) → text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)

    # Remove blockquote markers
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)

    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)

    # Remove bullet markers — keep the text
    text = re.sub(r"^[\*\-\+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)

    # Remove horizontal rules
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # Remove "In this piece:" label (the bullets will read naturally)
    text = re.sub(r"\*\*In this piece:\*\*", "Here is what this piece covers.", text)

    # Collapse excess whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.strip()

    return text


def chunk_text(text: str, max_chars: int = MAX_CHARS_PER_CHUNK) -> list[str]:
    """Split text at paragraph boundaries to stay under ElevenLabs chunk limit."""
    paragraphs = text.split("\n\n")
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) + 2 > max_chars and current:
            chunks.append(current.strip())
            current = para
        else:
            current = (current + "\n\n" + para).strip() if current else para
    if current:
        chunks.append(current.strip())
    return chunks


# ── ElevenLabs TTS ────────────────────────────────────────────────────────────

def text_to_speech(text: str, dry_run: bool = False) -> bytes | None:
    """Convert text to MP3 bytes using ElevenLabs API."""
    api_key  = os.environ.get("ELEVENLABS_API_KEY", "")
    voice_id = os.environ.get("ELEVENLABS_VOICE_ID", DEFAULT_VOICE_ID)
    model_id = os.environ.get("ELEVENLABS_MODEL_ID", DEFAULT_MODEL_ID)

    if not api_key:
        print("[Error] ELEVENLABS_API_KEY not set", file=sys.stderr)
        return None

    chunks = chunk_text(text)
    total_chars = sum(len(c) for c in chunks)
    print(f"  Text: {total_chars:,} chars across {len(chunks)} chunk(s)")

    if dry_run:
        print(f"  [DRY RUN] Would send {total_chars:,} chars to ElevenLabs")
        return b""

    audio_parts = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  Generating chunk {i}/{len(chunks)} ({len(chunk):,} chars)...")
        resp = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
            headers={
                "xi-api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
            json={
                "text": chunk,
                "model_id": model_id,
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
            },
            timeout=120,
        )
        if not resp.ok:
            print(f"  [Error] ElevenLabs chunk {i}: {resp.status_code} — {resp.text[:200]}", file=sys.stderr)
            return None
        audio_parts.append(resp.content)

    return b"".join(audio_parts)


# ── GitHub Releases upload ────────────────────────────────────────────────────

def get_repo_slug() -> str | None:
    """Get owner/repo from git remote."""
    try:
        remote = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        return remote.replace("https://github.com/", "").replace(".git", "")
    except Exception as e:
        print(f"[Error] Cannot determine repo slug: {e}", file=sys.stderr)
        return None


def upload_to_github_releases(mp3_bytes: bytes, blog_path: Path, dry_run: bool = False) -> str | None:
    """Upload MP3 to GitHub Releases and return the download URL."""
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("[Error] GITHUB_TOKEN not set", file=sys.stderr)
        return None

    repo = get_repo_slug()
    if not repo:
        return None

    date_prefix = blog_path.stem[:10]
    tag_name    = f"audio-{date_prefix}"
    mp3_name    = f"{blog_path.stem}.mp3"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if dry_run:
        print(f"  [DRY RUN] Would upload {mp3_name} to GitHub Releases tag {tag_name}")
        return f"https://github.com/{repo}/releases/download/{tag_name}/{mp3_name}"

    # Try to find existing release with this tag
    release_id = None
    list_resp = requests.get(f"https://api.github.com/repos/{repo}/releases", headers=headers)
    for rel in list_resp.json() if list_resp.ok else []:
        if rel.get("tag_name") == tag_name:
            release_id = rel["id"]
            print(f"  Found existing release: {tag_name} (id: {release_id})")
            break

    # Create release if not found
    if not release_id:
        create_resp = requests.post(
            f"https://api.github.com/repos/{repo}/releases",
            json={"tag_name": tag_name, "name": f"Audio: {blog_path.stem}", "body": "Auto-generated audio narration.", "draft": False},
            headers=headers,
        )
        if not create_resp.ok:
            print(f"[Error] Create release: {create_resp.status_code} — {create_resp.text[:200]}", file=sys.stderr)
            return None
        release_id = create_resp.json()["id"]
        print(f"  Created release: {tag_name} (id: {release_id})")

    # Upload MP3 asset
    upload_resp = requests.post(
        f"https://uploads.github.com/repos/{repo}/releases/{release_id}/assets?name={mp3_name}",
        data=mp3_bytes,
        headers={**headers, "Content-Type": "audio/mpeg"},
        timeout=120,
    )
    if not upload_resp.ok:
        print(f"[Error] Upload asset: {upload_resp.status_code} — {upload_resp.text[:200]}", file=sys.stderr)
        return None

    url = upload_resp.json().get("browser_download_url")
    print(f"  Uploaded: {url}")
    return url


# ── Cache ─────────────────────────────────────────────────────────────────────

def write_cache(blog_path: Path, audio_url: str) -> None:
    AUDIO_CACHE.write_text(json.dumps({
        "timestamp":  datetime.now().isoformat(),
        "blog_file":  blog_path.name,
        "audio_url":  audio_url,
    }, indent=2))
    print(f"[Cache] Saved to audio-cache.json")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate audio for latest blog post")
    parser.add_argument("--dry-run", action="store_true", help="Preview without calling APIs")
    args = parser.parse_args()

    blog_path = find_latest_blog()
    if not blog_path:
        print("[Skip] No blog file found.")
        sys.exit(0)

    print(f"Blog: {blog_path.name}")

    cached = already_generated(blog_path)
    if cached:
        sys.exit(0)

    print(f"\n[Text] Extracting readable prose...")
    text = extract_readable_text(blog_path)
    print(f"  Extracted {len(text):,} chars ({len(text.split()):,} words)")

    print(f"\n[ElevenLabs] Converting to audio...")
    mp3_bytes = text_to_speech(text, dry_run=args.dry_run)
    if mp3_bytes is None:
        print("[Error] Audio generation failed.", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        print("\n[Done] Dry run complete — no files written.")
        return

    print(f"\n[GitHub] Uploading {len(mp3_bytes):,} bytes to GitHub Releases...")
    audio_url = upload_to_github_releases(mp3_bytes, blog_path)
    if not audio_url:
        print("[Error] Upload failed.", file=sys.stderr)
        sys.exit(1)

    write_cache(blog_path, audio_url)
    print(f"\n[Done] Audio URL: {audio_url}")


if __name__ == "__main__":
    main()
