"""
Strategy Blog Pipeline Dashboard
Run: streamlit run dashboard.py
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import streamlit as st
import yaml

# ─────────────────────────────────────────────
# Constants
# ─────────────────────────────────────────────

BASE_DIR   = Path(__file__).parent
RESEARCH_DIR = BASE_DIR / "research"
BLOGS_DIR  = BASE_DIR / "blogs"
PUBLISH_LOG = BASE_DIR / "publish-log.json"

DAYS_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
DAY_TO_INT = {d: i for i, d in enumerate(DAYS_ORDER)}

AGENTS = {
    "Researcher (R)": {"cron_hour": 9,  "cron_days": "1-6", "label": "R"},
    "Analyst (A)":    {"cron_hour": 17, "cron_days": "1-6", "label": "A"},
    "Blog Compiler":  {"cron_hour": 10, "cron_days": "0",   "label": "📝"},
    "Tweet Writer":   {"cron_hour": 11, "cron_days": "0",   "label": "🐦"},
    "Publisher":      {"cron_hour": 12, "cron_days": "0",   "label": "🚀"},
}

# ─────────────────────────────────────────────
# Utility
# ─────────────────────────────────────────────

def get_week_monday(dt=None) -> datetime:
    dt = dt or datetime.now()
    return dt - timedelta(days=dt.weekday())


def fmt_delta(dt: datetime) -> str:
    now = datetime.now()
    delta = dt - now
    if delta.total_seconds() < 0:
        return "overdue"
    h, rem = divmod(int(delta.total_seconds()), 3600)
    m = rem // 60
    if h >= 24:
        return f"in {h // 24}d {h % 24}h"
    return f"in {h}h {m}m"


def compute_next_run(cron_hour: int, cron_days: str) -> datetime:
    """Compute next fire time for simple hour-based cron."""
    now = datetime.now()
    candidate = now.replace(hour=cron_hour, minute=5, second=0, microsecond=0)

    is_weekend_only = cron_days == "0"    # Sunday only
    is_weekday      = cron_days == "1-6"  # Mon-Sat

    for offset in range(8):
        t = candidate + timedelta(days=offset)
        wd = t.weekday()  # 0=Mon … 6=Sun
        if is_weekend_only and wd == 6 and t > now:
            return t
        if is_weekday and wd < 6 and t > now:
            return t
    return candidate + timedelta(days=8)  # fallback


# ─────────────────────────────────────────────
# Parsing
# ─────────────────────────────────────────────

@st.cache_data(ttl=300)
def parse_research_file(path_str: str) -> dict:
    path = Path(path_str)
    if not path.exists():
        return {"week_of": None, "entries": [], "strongest_threads": None, "ready": False}

    text = path.read_text()

    # Week date from filename
    m = re.search(r"week-(\d{4}-\d{2}-\d{2})", path.stem)
    week_of = m.group(1) if m else None

    # Two patterns: new (pipes) and legacy (em dashes) — both parsed for history
    pipe_re   = re.compile(r"^##\s+([\w][\w –-]*?)\s*\|\s*(R|A)\s*\|\s*(.+)$", re.MULTILINE)
    legacy_re = re.compile(r"^##\s+([\w][\w –-]*?)\s*[—]+\s*(R|A)\s+\([^)]+\)\s*[—]+\s*(.+)$", re.MULTILINE)

    entries = []
    for day_raw, agent, title in pipe_re.findall(text) + legacy_re.findall(text):
        # Normalise day (handle catch-up ranges like "Monday–Wednesday")
        first_day = re.split(r"[–-]", day_raw)[0].strip()
        canonical = next((d for d in DAYS_ORDER if d.startswith(first_day[:3])), first_day)
        entries.append({"day": canonical, "agent": agent, "title": title.strip()})

    # Strongest Threads block (between heading and first ---)
    threads_match = re.search(
        r"## Strongest Threads This Week\n(.*?)(?=\n---)", text, re.DOTALL
    )
    threads_raw = threads_match.group(1).strip() if threads_match else None
    # Strip HTML comment placeholder
    if threads_raw and threads_raw.startswith("<!--"):
        threads_raw = None

    ready = bool(re.search(r"STATUS:\s*READY FOR COMPILATION", text))

    return {
        "week_of":          week_of,
        "entries":          entries,
        "strongest_threads": threads_raw,
        "ready":            ready,
    }


@st.cache_data(ttl=300)
def parse_blog_file(path_str: str) -> dict:
    path = Path(path_str)
    text = path.read_text()
    parts = re.split(r"^---\s*$", text, maxsplit=2, flags=re.MULTILINE)
    if len(parts) < 3:
        return {}
    fm = yaml.safe_load(parts[1]) or {}
    date_val = fm.get("date", "")
    if isinstance(date_val, datetime):
        date_str = date_val.strftime("%Y-%m-%d")
    else:
        date_str = str(date_val)
    return {
        "title":   fm.get("title", path.stem),
        "date":    date_str,
        "topic":   fm.get("topic", ""),
        "summary": fm.get("summary", ""),
        "slug":    path.stem,
        "type":    fm.get("type", "article"),
    }


@st.cache_data(ttl=300)
def load_publish_log() -> list:
    if not PUBLISH_LOG.exists():
        return []
    try:
        return json.loads(PUBLISH_LOG.read_text())
    except Exception:
        return []


@st.cache_data(ttl=300)
def load_all_weeks() -> list:
    files = sorted(RESEARCH_DIR.glob("week-*.md"), reverse=True)
    return [parse_research_file(str(f)) for f in files]


@st.cache_data(ttl=300)
def load_all_blogs() -> list:
    files = sorted(
        [f for f in BLOGS_DIR.glob("*.md") if "tweet-thread" not in f.name],
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )
    results = []
    for f in files:
        data = parse_blog_file(str(f))
        if data:
            data["has_tweet_thread"] = (
                BLOGS_DIR / f"{f.stem[:10]}-tweet-thread.md"
            ).exists()
            results.append(data)
    return results


def get_sunday_status(week_monday_str: str, publish_log: list) -> dict:
    """Check if blog/tweet/published exist for this week."""
    if not week_monday_str:
        return {"blog": False, "tweet_thread": False, "published": False, "pub_status": None}

    monday = datetime.strptime(week_monday_str, "%Y-%m-%d")
    sunday = monday + timedelta(days=6)

    blog_found = thread_found = False
    for f in BLOGS_DIR.glob("*.md"):
        if "tweet-thread" in f.name:
            continue
        data = parse_blog_file(str(f))
        if not data.get("date"):
            continue
        try:
            d = datetime.strptime(data["date"][:10], "%Y-%m-%d")
        except ValueError:
            continue
        if monday <= d <= sunday:
            blog_found = True
            thread_found = (BLOGS_DIR / f"{f.stem[:10]}-tweet-thread.md").exists()
            break

    pub_entry = next(
        (e for e in reversed(publish_log)
         if e.get("blog_status") not in ("dry_run", None)
         and week_monday_str[:7] in (e.get("blog_slug") or "")),
        None,
    )
    published = pub_entry is not None
    pub_status = pub_entry.get("blog_status") if pub_entry else None

    return {
        "blog": blog_found,
        "tweet_thread": thread_found,
        "published": published,
        "pub_status": pub_status,
    }


# ─────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Strategy Blog Monitor",
    page_icon="📊",
    layout="wide",
)

# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────

with st.sidebar:
    st.title("📊 Strategy Blog")
    st.caption(f"Updated: {datetime.now().strftime('%a %b %d, %H:%M')}")
    if st.button("🔄 Refresh data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    st.divider()
    st.markdown("**Pipeline schedule**")
    for name, cfg in AGENTS.items():
        nxt = compute_next_run(cfg["cron_hour"], cfg["cron_days"])
        days_label = "Sun" if cfg["cron_days"] == "0" else "Mon–Sat"
        st.markdown(
            f"`{cfg['label']}` **{name}**  \n"
            f"{days_label} {cfg['cron_hour']:02d}:00 · {fmt_delta(nxt)}"
        )

# ─────────────────────────────────────────────
# Load data
# ─────────────────────────────────────────────

publish_log  = load_publish_log()
all_weeks    = load_all_weeks()
all_blogs    = load_all_blogs()

monday_dt    = get_week_monday()
monday_str   = monday_dt.strftime("%Y-%m-%d")
current_week = next((w for w in all_weeks if w["week_of"] == monday_str), None)

today_name   = datetime.now().strftime("%A")
today_idx    = datetime.now().weekday()  # 0=Mon … 6=Sun

# ─────────────────────────────────────────────
# Zone 1 — Header metrics
# ─────────────────────────────────────────────

st.title("Strategy Blog Pipeline")
st.caption(f"Week of {monday_str}  ·  Today is {today_name}")
st.divider()

entries      = current_week["entries"] if current_week else []
r_entries    = [e for e in entries if e["agent"] == "R"]
a_entries    = [e for e in entries if e["agent"] == "A"]

# Days elapsed this week (Mon=0 … Sat=5), capped at 6
days_elapsed = min(today_idx, 5) + 1 if today_idx < 6 else 6
expected_r   = days_elapsed  # one per day
expected_a   = days_elapsed

last_r_day   = r_entries[-1]["day"] if r_entries else "—"
last_a_day   = a_entries[-1]["day"] if a_entries else "—"

sunday_status = get_sunday_status(monday_str, publish_log)

m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("Researcher entries",  f"{len(r_entries)} / {expected_r}",
          delta="on track" if len(r_entries) >= expected_r else f"behind by {expected_r - len(r_entries)}",
          delta_color="normal" if len(r_entries) >= expected_r else "inverse")
m2.metric("Analyst entries",     f"{len(a_entries)} / {expected_a}",
          delta="on track" if len(a_entries) >= expected_a else f"behind by {expected_a - len(a_entries)}",
          delta_color="normal" if len(a_entries) >= expected_a else "inverse")
m3.metric("Blog compiled",       "✅ Yes" if sunday_status["blog"] else "⏳ Pending")
m4.metric("Tweet thread",        "✅ Yes" if sunday_status["tweet_thread"] else "⏳ Pending")
m5.metric("Published",           "✅ Yes" if sunday_status["published"] else "⏳ Pending")
m6.metric("Total blogs",         str(len(all_blogs)))

st.divider()

# ─────────────────────────────────────────────
# Zone 2 — This week
# ─────────────────────────────────────────────

col_left, col_right = st.columns([3, 2])

with col_left:
    st.subheader("This week's coverage")

    if current_week and current_week["ready"]:
        st.success("READY FOR COMPILATION — agents marked this week complete")

    # Build coverage grid
    coverage = {(e["day"], e["agent"]): e["title"] for e in entries}
    grid_data = {}
    for day in DAYS_ORDER:
        past = DAY_TO_INT.get(day, 0) <= min(today_idx, 5)
        r_title = coverage.get((day, "R"))
        a_title = coverage.get((day, "A"))
        grid_data[day] = {
            "R — Researcher": (r_title[:55] + "…") if r_title and len(r_title) > 55 else (r_title or ("" if not past else "—")),
            "A — Analyst":    (a_title[:55] + "…") if a_title and len(a_title) > 55 else (a_title or ("" if not past else "—")),
        }

    df = pd.DataFrame(grid_data).T
    df.index.name = "Day"

    def colour_cell(val):
        if val and val != "—":
            return "background-color: #d1fae5; color: #065f46"   # green — done
        if val == "—":
            return "background-color: #fee2e2; color: #991b1b"   # red — missed
        return "background-color: #f3f4f6; color: #6b7280"       # grey — future

    styled = df.style.applymap(colour_cell)
    st.dataframe(styled, use_container_width=True, height=265)

    # Anchor topic
    anchor = r_entries[0]["title"] if r_entries else None
    if anchor:
        st.markdown(f"**This week's topic:** {anchor}")
    else:
        st.caption("No research entries yet this week.")

with col_right:
    st.subheader("Strongest threads")
    if current_week and current_week["strongest_threads"]:
        threads_text = current_week["strongest_threads"]
        # Trim placeholder text
        if "_No threads yet" in threads_text:
            st.caption("No threads identified yet — check back after the first few entries.")
        else:
            st.markdown(threads_text)
    else:
        st.caption("No threads identified yet.")

st.divider()

# ─────────────────────────────────────────────
# Zone 3 — Sunday pipeline status
# ─────────────────────────────────────────────

st.subheader("Sunday pipeline")

days_until_sunday = (6 - today_idx) % 7 or 7
next_sunday = datetime.now() + timedelta(days=days_until_sunday)
next_sunday_str = next_sunday.strftime("%a %b %d")

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("**📝 Blog Compiler** · Sun 10:00 AM")
    if sunday_status["blog"]:
        blog = next((b for b in all_blogs
                     if b["date"][:7] == monday_str[:7]), None)
        if blog:
            st.success(f"Done — *{blog['title'][:50]}*")
        else:
            st.success("Blog file found")
    else:
        st.info(f"Runs {next_sunday_str} at 10:00 AM")

with p2:
    st.markdown("**🐦 Tweet Writer** · Sun 11:00 AM")
    if sunday_status["tweet_thread"]:
        st.success("Done — thread written")
    elif sunday_status["blog"]:
        st.warning("Blog done, tweet thread pending")
    else:
        st.info(f"Runs {next_sunday_str} at 11:00 AM")

with p3:
    st.markdown("**🚀 Publisher** · Sun 12:00 PM")
    if sunday_status["published"]:
        st.success(f"Published · status: {sunday_status['pub_status']}")
    elif sunday_status["tweet_thread"]:
        st.warning("Ready to publish — runs at noon")
    else:
        st.info(f"Runs {next_sunday_str} at 12:00 PM")

st.divider()

# ─────────────────────────────────────────────
# Zone 4 — Published blogs
# ─────────────────────────────────────────────

st.subheader("Published blogs")

if all_blogs:
    pub_slugs = {e.get("blog_slug"): e for e in publish_log}

    for blog in all_blogs:
        log_entry = pub_slugs.get(blog["slug"])
        status = log_entry.get("blog_status") if log_entry else "not published"
        tweets = log_entry.get("tweet_count", 0) if log_entry else 0
        first_tweet = log_entry.get("first_tweet_id") if log_entry else None
        published_at = log_entry.get("timestamp", "")[:10] if log_entry else ""

        status_badge = {
            "published": "🟢 Published",
            "dry_run":   "🟡 Dry run",
            "skipped":   "⚪ Skipped",
        }.get(status, f"⚫ {status}")

        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"#### {blog['title']}")
                st.caption(f"{blog['date']}  ·  {blog['topic']}")
                if blog["summary"]:
                    st.markdown(f"_{blog['summary'][:200]}_")
            with c2:
                st.markdown(status_badge)
                if published_at:
                    st.caption(f"Published {published_at}")
                if blog["has_tweet_thread"]:
                    if first_tweet:
                        st.markdown(f"🐦 {tweets} tweets · ID `{first_tweet}`")
                    else:
                        st.markdown(f"🐦 Thread written ({tweets} tweets)")
                else:
                    st.caption("No tweet thread")
else:
    st.caption("No blogs published yet.")

st.divider()

# ─────────────────────────────────────────────
# Zone 5 — Historical archive
# ─────────────────────────────────────────────

with st.expander("Historical archive — all weeks", expanded=False):
    rows = []
    for week in all_weeks:
        w_entries = week["entries"]
        w_r = [e for e in w_entries if e["agent"] == "R"]
        w_a = [e for e in w_entries if e["agent"] == "A"]
        topic = w_r[0]["title"][:60] if w_r else "—"
        week_status = get_sunday_status(week["week_of"], publish_log)
        rows.append({
            "Week of":        week["week_of"] or "—",
            "R entries":      len(w_r),
            "A entries":      len(w_a),
            "Topic":          topic,
            "Blog":           "✅" if week_status["blog"] else "—",
            "Tweet thread":   "✅" if week_status["tweet_thread"] else "—",
            "Published":      "✅" if week_status["published"] else ("🟡 dry run" if any(
                e.get("blog_status") == "dry_run" and (week["week_of"] or "")[:7] in (e.get("blog_slug") or "")
                for e in publish_log) else "—"),
            "Ready":          "✅" if week.get("ready") else "—",
        })

    if rows:
        hist_df = pd.DataFrame(rows)
        st.dataframe(hist_df, use_container_width=True, hide_index=True)
    else:
        st.caption("No historical data yet.")
