#!/usr/bin/env python3
"""
Strategy Blog Trend Scout

Runs Sunday night before the week starts. Pulls trending topics from:
  1. Hacker News (free Firebase API — shows what smart tech/biz people care about)
  2. Brave Search (strategy/AI/fintech news from the past week)

Writes: trends/week-YYYY-MM-DD.md (next Monday's date)

The researcher reads this file Monday morning before picking a topic.
No Claude API needed — pure data collection.
"""

import os
import sys
import json
import requests
from datetime import date, timedelta
from pathlib import Path

BASE_DIR  = Path(__file__).parent
TRENDS_DIR = BASE_DIR / "trends"
BRAVE_KEY  = os.environ.get("BRAVE_API_KEY", "")

# ── Date helpers ───────────────────────────────────────────────────────────────

def next_monday() -> str:
    """When run on Sunday, this is tomorrow = Monday."""
    today = date.today()
    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    return (today + timedelta(days=days_until_monday)).isoformat()


# ── Hacker News ────────────────────────────────────────────────────────────────

# Topics that fit the blog's strategy focus — filter out pure code/hobby stories
STRATEGY_KEYWORDS = [
    "ai", "startup", "venture", "funding", "series", "ipo", "acquisition",
    "revenue", "profit", "margin", "market", "platform", "enterprise",
    "saas", "cloud", "model", "regulation", "antitrust", "policy",
    "india", "fintech", "payments", "open", "microsoft", "google", "apple",
    "meta", "amazon", "nvidia", "openai", "anthropic", "strategy",
    "billion", "million", "growth", "layoff", "hire", "launch", "raises",
]

def is_strategy_relevant(title: str) -> bool:
    title_lower = title.lower()
    return any(kw in title_lower for kw in STRATEGY_KEYWORDS)


def fetch_hn_stories(n_ids: int = 100, min_score: int = 50) -> list[dict]:
    """Fetch top HN stories, filter for strategy relevance."""
    try:
        ids = requests.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json",
            timeout=10,
        ).json()[:n_ids]
    except Exception as e:
        print(f"  [HN] Failed to fetch IDs: {e}")
        return []

    stories = []
    for sid in ids:
        try:
            s = requests.get(
                f"https://hacker-news.firebaseio.com/v0/item/{sid}.json",
                timeout=5,
            ).json()
            if not s or not s.get("title"):
                continue
            score = s.get("score", 0)
            if score < min_score:
                continue
            if not is_strategy_relevant(s["title"]):
                continue
            stories.append({
                "title":    s["title"],
                "url":      s.get("url", f"https://news.ycombinator.com/item?id={sid}"),
                "score":    score,
                "comments": s.get("descendants", 0),
            })
        except Exception:
            continue

    return sorted(stories, key=lambda x: x["score"], reverse=True)[:20]


# ── Brave Search ───────────────────────────────────────────────────────────────

# Queries tuned to the blog's topic interests (config.yaml)
BRAVE_QUERIES = [
    "AI startup strategy funding news this week",
    "big tech platform antitrust regulation 2026",
    "enterprise software SaaS business model shift this week",
    "India tech startup fintech growth news this week",
    "AI infrastructure chips cloud margin business model 2026",
]


def brave_search(query: str, count: int = 5) -> list[dict]:
    if not BRAVE_KEY:
        return []
    try:
        resp = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers={
                "Accept":               "application/json",
                "Accept-Encoding":      "gzip",
                "X-Subscription-Token": BRAVE_KEY,
            },
            params={
                "q":         query,
                "count":     count,
                "freshness": "pw",   # past week
            },
            timeout=12,
        )
        resp.raise_for_status()
        results = resp.json().get("web", {}).get("results", [])
        return [
            {
                "title":   r.get("title", ""),
                "url":     r.get("url", ""),
                "snippet": r.get("description", "")[:200],
            }
            for r in results
        ]
    except Exception as e:
        print(f"  [Brave] '{query[:40]}' failed: {e}")
        return []


# ── Writer ─────────────────────────────────────────────────────────────────────

def write_trends_file(
    hn_stories: list[dict],
    brave_results: list[tuple[str, list[dict]]],
    week_monday: str,
) -> Path:
    TRENDS_DIR.mkdir(exist_ok=True)
    out = TRENDS_DIR / f"week-{week_monday}.md"

    lines = [
        f"# Trending Topics — Week of {week_monday}",
        f"_Auto-scouted on {date.today().isoformat()} (Sunday night). Do not edit — regenerated weekly._",
        "",
        "---",
        "",
        "## Hacker News — High-Signal Strategy & Tech Stories",
        "_Score = how many upvotes from HN's tech/business audience. Higher = more people found it worth sharing._",
        "",
    ]

    if hn_stories:
        for s in hn_stories:
            lines.append(f"- **{s['title']}**  ↑{s['score']} | 💬{s['comments']}")
            lines.append(f"  {s['url']}")
            lines.append("")
    else:
        lines.append("_No HN stories fetched this week._")
        lines.append("")

    lines += [
        "---",
        "",
        "## Brave Search — Strategy News This Week",
        "",
    ]

    for query, results in brave_results:
        lines.append(f"### `{query}`")
        lines.append("")
        if results:
            for r in results:
                lines.append(f"- **{r['title']}**")
                if r["snippet"]:
                    lines.append(f"  _{r['snippet']}_")
                lines.append(f"  {r['url']}")
                lines.append("")
        else:
            lines.append("_No results._")
            lines.append("")

    lines += [
        "---",
        "",
        "## How to Use This File (Researcher Instructions)",
        "",
        "1. Scan the HN stories and Brave results above.",
        "2. Identify 2-3 themes appearing in multiple places — that repetition signals real momentum.",
        "3. Do NOT just report what's trending. Find the **strategy story inside the trend**:",
        "   - What does this reveal about power shifting between companies?",
        "   - What does this mean for business models, pricing, or competitive moats?",
        "   - Why does a smart 25-year-old who doesn't work in tech actually care?",
        "4. Cross-check against `topics.md` backlog — trending + on the backlog = ideal pick.",
        "5. If nothing in this file fits the blog's interests, ignore it and use the backlog.",
        "",
        "_The goal: timely + strategic, not just reactive._",
    ]

    out.write_text("\n".join(lines), encoding="utf-8")
    return out


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    week_monday = next_monday()
    print(f"\n=== Trend Scout — Week of {week_monday} ===")

    print("\n[1/2] Fetching Hacker News top stories...")
    hn = fetch_hn_stories()
    print(f"      {len(hn)} strategy-relevant stories found")

    print("\n[2/2] Running Brave searches...")
    brave = []
    for q in BRAVE_QUERIES:
        print(f"      Searching: {q[:55]}...")
        results = brave_search(q)
        brave.append((q, results))
        print(f"      → {len(results)} results")

    print("\nWriting trends file...")
    out = write_trends_file(hn, brave, week_monday)
    print(f"Done → {out.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
