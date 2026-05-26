#!/usr/bin/env python3
"""
Strategy Blog Agent Runner
Uses the Anthropic Python SDK directly — no Claude Code CLI required.

Usage:
    python3 .github/scripts/run_agent.py researcher
    python3 .github/scripts/run_agent.py analyst
    python3 .github/scripts/run_agent.py compiler
    python3 .github/scripts/run_agent.py tweet-thread

Requires:
    ANTHROPIC_API_KEY env var
    BRAVE_API_KEY env var  (optional — enables web search)
"""

import json
import os
import re
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import anthropic
import requests

# ── Config ────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).parent.parent.parent   # repo root
# Haiku for daily research/analyst/summarizer runs (cheap, does the legwork)
# Sonnet for compiler + tweet thread + memory compressor (does the actual thinking and writing)
MODEL_DEFAULT   = "claude-haiku-4-5"
MODEL_COMPILER  = "claude-sonnet-4-5"
MODEL_SUMMARIZER = "claude-haiku-4-5"
MODEL_COMPRESSOR = "claude-sonnet-4-5"
MAX_TOKENS = 8192  # hard ceiling for claude-sonnet/haiku
MAX_TURNS  = 60   # safety ceiling

# ── Date helpers ──────────────────────────────────────────────────────────────

def today_str() -> str:
    return date.today().isoformat()

def monday_str() -> str:
    """ISO date of the Monday of the current week."""
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return monday.isoformat()

# ── Tool implementations ───────────────────────────────────────────────────────

def tool_read_file(path: str) -> str:
    p = BASE_DIR / path
    if not p.exists():
        return f"ERROR: File not found: {path}"
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:
        return f"ERROR reading {path}: {e}"


def tool_write_file(path: str, content: str) -> str:
    p = BASE_DIR / path
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        p.write_text(content, encoding="utf-8")
        return f"OK: wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"ERROR writing {path}: {e}"


def tool_append_to_file(path: str, content: str) -> str:
    p = BASE_DIR / path
    if not p.exists():
        return f"ERROR: File not found: {path}. Use write_file to create it first."
    try:
        existing = p.read_text(encoding="utf-8")
        p.write_text(existing + content, encoding="utf-8")
        return f"OK: appended {len(content)} chars to {path}"
    except Exception as e:
        return f"ERROR appending to {path}: {e}"


def tool_replace_in_file(path: str, old_string: str, new_string: str) -> str:
    p = BASE_DIR / path
    if not p.exists():
        return f"ERROR: File not found: {path}"
    try:
        text = p.read_text(encoding="utf-8")
        if old_string not in text:
            return f"ERROR: old_string not found in {path}"
        count = text.count(old_string)
        if count > 1:
            return f"ERROR: old_string appears {count} times in {path} — make it more specific"
        new_text = text.replace(old_string, new_string, 1)
        p.write_text(new_text, encoding="utf-8")
        return f"OK: replaced 1 occurrence in {path}"
    except Exception as e:
        return f"ERROR replacing in {path}: {e}"


def tool_list_directory(path: str) -> str:
    p = BASE_DIR / path
    if not p.exists():
        return f"ERROR: Directory not found: {path}"
    try:
        # Sort alphabetically by name — YYYY-MM-DD filenames sort chronologically.
        # Do NOT sort by mtime: in GitHub Actions all files share the same checkout
        # timestamp, making mtime-based ordering unreliable.
        entries = sorted(p.iterdir(), key=lambda x: x.name)
        lines = []
        for e in entries:
            kind = "dir" if e.is_dir() else "file"
            lines.append(f"{kind}  {e.name}")
        return "\n".join(lines) if lines else "(empty directory)"
    except Exception as e:
        return f"ERROR listing {path}: {e}"


def tool_web_search(query: str) -> str:
    """Search the web via Brave Search API."""
    api_key = os.environ.get("BRAVE_API_KEY", "")
    if not api_key:
        return "ERROR: BRAVE_API_KEY not set. Web search unavailable."
    try:
        resp = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers={
                "Accept": "application/json",
                "Accept-Encoding": "gzip",
                "X-Subscription-Token": api_key,
            },
            params={"q": query, "count": 5, "text_decorations": False},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
        results = data.get("web", {}).get("results", [])
        if not results:
            return "No results found."
        lines = []
        for r in results:
            lines.append(f"Title: {r.get('title','')}")
            lines.append(f"URL: {r.get('url','')}")
            lines.append(f"Snippet: {r.get('description','')}")
            lines.append("")
        return "\n".join(lines)
    except Exception as e:
        return f"ERROR searching web: {e}"


def tool_fetch_url(url: str) -> str:
    """Fetch the text content of a URL (simple HTTP GET, no JS)."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; StrategyBotResearcher/1.0)"}
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        # Strip HTML tags crudely
        text = re.sub(r"<[^>]+>", " ", resp.text)
        text = re.sub(r"\s{3,}", "\n\n", text)
        return text[:8000]  # cap at 8k chars
    except Exception as e:
        return f"ERROR fetching {url}: {e}"


# ── Tool registry ─────────────────────────────────────────────────────────────

TOOLS = [
    {
        "name": "read_file",
        "description": "Read the full content of a file in the repository. Path is relative to repo root.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative path from repo root, e.g. 'research/week-2026-04-14.md'"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "write_file",
        "description": "Write (create or overwrite) a file with the given content. Path is relative to repo root.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string", "description": "Full file content to write"}
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "append_to_file",
        "description": "Append text to the end of an existing file. Use this to add research/analyst entries.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string", "description": "Text to append"}
            },
            "required": ["path", "content"]
        }
    },
    {
        "name": "replace_in_file",
        "description": "Replace a unique string in a file with new text. old_string must appear exactly once.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "old_string": {"type": "string"},
                "new_string": {"type": "string"}
            },
            "required": ["path", "old_string", "new_string"]
        }
    },
    {
        "name": "list_directory",
        "description": "List files in a directory, sorted by modification time (newest first).",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative path from repo root, e.g. 'research' or 'blogs'"}
            },
            "required": ["path"]
        }
    },
    {
        "name": "web_search",
        "description": "Search the web for current news, facts, and data. Always use this for research — never fabricate facts.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "fetch_url",
        "description": "Fetch and read the text content of a specific URL. Use after web_search to get article details.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Full URL to fetch"}
            },
            "required": ["url"]
        }
    },
]


def dispatch_tool(name: str, inputs: dict) -> str:
    if name == "read_file":
        return tool_read_file(inputs["path"])
    elif name == "write_file":
        return tool_write_file(inputs["path"], inputs["content"])
    elif name == "append_to_file":
        return tool_append_to_file(inputs["path"], inputs["content"])
    elif name == "replace_in_file":
        return tool_replace_in_file(inputs["path"], inputs["old_string"], inputs["new_string"])
    elif name == "list_directory":
        return tool_list_directory(inputs["path"])
    elif name == "web_search":
        return tool_web_search(inputs["query"])
    elif name == "fetch_url":
        return tool_fetch_url(inputs["url"])
    else:
        return f"ERROR: Unknown tool '{name}'"


# ── Agentic loop ──────────────────────────────────────────────────────────────

def run_agent(agent_type: str) -> None:
    prompt_path = BASE_DIR / ".github" / "prompts" / f"{agent_type}.md"
    if not prompt_path.exists():
        print(f"ERROR: Prompt file not found: {prompt_path}", file=sys.stderr)
        sys.exit(1)

    system_prompt = prompt_path.read_text(encoding="utf-8")

    # Inject live date context
    date_context = (
        f"\n\n---\n"
        f"**Context injected at runtime:**\n"
        f"- Today's date: {today_str()}\n"
        f"- Day of week: {date.today().strftime('%A')}\n"
        f"- Monday of this week: {monday_str()}\n"
        f"- This week's research file: research/week-{monday_str()}.md\n"
    )

    # For tweet-thread: inject the exact blog file to process.
    # list_directory mtime ordering is unreliable in CI (all files share checkout
    # timestamp), so we resolve the latest dated blog in Python and tell the agent.
    if agent_type == "tweet-thread":
        import re as _re
        date_pat = _re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
        blogs_dir = BASE_DIR / "blogs"
        candidates = [
            f for f in blogs_dir.glob("*.md")
            if date_pat.match(f.name)
            and "tweet-thread" not in f.name
            and "infographic" not in f.name
            and f.stat().st_size > 0
        ]
        if candidates:
            latest_blog = max(candidates, key=lambda f: f.name)
            blog_slug   = latest_blog.stem   # e.g. 2026-05-11-vertical-integration-not-silicon
            blog_date   = latest_blog.name[:10]  # e.g. 2026-05-11
            date_context += (
                f"- **Blog to thread**: blogs/{latest_blog.name}\n"
                f"- **Blog slug**: {blog_slug}\n"
                f"- **Blog date**: {blog_date}\n"
                f"- **Tweet thread file to write**: blogs/{blog_date}-tweet-thread.md\n"
                f"- **Blog URL for CTA**: https://prashant-chandel.org/blog/{blog_slug}\n"
            )

    # For daily-poster: inject today's exact output file path
    if agent_type == "daily-poster":
        date_context += (
            f"- **Daily tweet file to write**: tweets/daily-{today_str()}.md\n"
            f"- **Today's format slot**: {date.today().strftime('%A')} — see format table in your instructions\n"
        )

    # For brief-generator: inject today's brief output path and day context
    if agent_type == "brief-generator":
        date_context += (
            f"- **Brief file to write**: briefs/brief-{today_str()}.md\n"
            f"- **Today's day**: {date.today().strftime('%A')}\n"
        )

    # For podcast-script: inject the blog file to convert (same logic as tweet-thread)
    if agent_type == "podcast-script":
        import re as _re
        date_pat = _re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")
        blogs_dir = BASE_DIR / "blogs"
        candidates = [
            f for f in blogs_dir.glob("*.md")
            if date_pat.match(f.name)
            and "tweet-thread" not in f.name
            and "contrarian" not in f.name
            and "infographic" not in f.name
            and "podcast-script" not in f.name
            and f.stat().st_size > 0
        ]
        if candidates:
            latest_blog = max(candidates, key=lambda f: f.name)
            blog_date   = latest_blog.name[:10]
            date_context += (
                f"- **Blog to convert**: blogs/{latest_blog.name}\n"
                f"- **Podcast script file to write**: blogs/{blog_date}-podcast-script.md\n"
            )

    system_prompt = system_prompt + date_context

    if agent_type in ("compiler", "tweet-thread", "memory-compressor", "daily-poster", "brief-generator", "podcast-script"):
        model = MODEL_COMPILER   # Sonnet — quality matters for public-facing drafts
    elif agent_type == "summarizer":
        model = MODEL_SUMMARIZER
    else:
        model = MODEL_DEFAULT

    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        max_retries=6,   # SDK handles exponential backoff on 429 automatically
    )

    messages = [
        {"role": "user", "content": "Execute your task now. Follow your instructions step by step."}
    ]

    print(f"\n=== Strategy Blog Agent: {agent_type} ===")
    print(f"Today: {today_str()}  |  Week Monday: {monday_str()}")
    print(f"Model: {model}")
    print("=" * 50)

    # Compiler/tweet-thread read large files — need longer pauses to stay
    # under the 30k input-tokens-per-minute rate limit.
    # Summarizer reads the full research file too so gets the same treatment.
    inter_turn_sleep = 65 if agent_type in ("compiler", "tweet-thread", "summarizer", "memory-compressor", "daily-poster", "brief-generator", "podcast-script") else 8

    for turn in range(MAX_TURNS):
        print(f"\n[Turn {turn + 1}] Calling Claude API...")

        # Explicit 429 retry loop — SDK backoff isn't long enough for TPM limits
        for attempt in range(8):
            try:
                response = client.messages.create(
                    model=model,
                    max_tokens=MAX_TOKENS,
                    system=system_prompt,
                    tools=TOOLS,
                    messages=messages,
                )
                break  # success
            except anthropic.RateLimitError as e:
                wait = 65 * (attempt + 1)
                print(f"  [429] Rate limited. Waiting {wait}s before retry {attempt + 1}/8...")
                time.sleep(wait)
                if attempt == 7:
                    raise  # give up after 8 attempts
        else:
            break

        print(f"  stop_reason: {response.stop_reason}")

        # Collect all content from this response
        assistant_content = response.content

        # Print text blocks for visibility
        for block in assistant_content:
            if hasattr(block, "text"):
                preview = block.text[:200].replace("\n", " ")
                print(f"  Text: {preview}...")

        # Append assistant message
        messages.append({"role": "assistant", "content": assistant_content})

        # If done, exit
        if response.stop_reason == "end_turn":
            print("\n[Done] Agent finished successfully.")
            break

        # Process tool calls
        if response.stop_reason == "tool_use":
            tool_results = []
            for block in assistant_content:
                if block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    print(f"  Tool: {tool_name}({list(tool_input.keys())})")

                    result = dispatch_tool(tool_name, tool_input)
                    result_preview = result[:150].replace("\n", " ")
                    print(f"  Result: {result_preview}")

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            messages.append({"role": "user", "content": tool_results})

            # Pace calls to stay under 30k tokens/minute rate limit.
            # Compiler handles large files so needs a full 65s window reset.
            print(f"  Sleeping {inter_turn_sleep}s...")
            time.sleep(inter_turn_sleep)

        else:
            # Unexpected stop reason
            print(f"[WARN] Unexpected stop_reason: {response.stop_reason}. Stopping.")
            break

    else:
        print(f"\n[WARN] Reached max turns ({MAX_TURNS}). Agent may not have finished.")


# ── Entry point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_agent.py <agent-type>")
        print("  agent-type: researcher | analyst | compiler | tweet-thread")
        sys.exit(1)

    agent_type = sys.argv[1]
    valid = {"researcher", "analyst", "compiler", "tweet-thread", "summarizer", "memory-compressor", "daily-poster", "brief-generator", "podcast-script"}
    if agent_type not in valid:
        print(f"ERROR: Unknown agent type '{agent_type}'. Must be one of: {valid}", file=sys.stderr)
        sys.exit(1)

    run_agent(agent_type)
