#!/usr/bin/env python3
"""
Strategy Blog Orchestrator

Manages weekly research files and provides prompts for the scheduled agents.
Each agent (researcher, analyst, compiler) calls this to get their prompt
and to determine which file to work on.

Usage:
    python orchestrator.py init-week        # Create this week's research file
    python orchestrator.py current-file     # Print path to current week's file
    python orchestrator.py researcher-prompt # Print the researcher's full prompt
    python orchestrator.py analyst-prompt    # Print the analyst's full prompt
    python orchestrator.py compiler-prompt   # Print the Sunday compiler's prompt
"""

import sys
import yaml
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path(__file__).parent
RESEARCH_DIR = BASE_DIR / "research"
BLOGS_DIR = BASE_DIR / "blogs"
CONFIG_PATH = BASE_DIR / "config.yaml"
TOPICS_PATH = BASE_DIR / "topics.md"

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_week_monday(dt=None):
    """Get the Monday of the current week."""
    dt = dt or datetime.now()
    monday = dt - timedelta(days=dt.weekday())
    return monday.strftime("%Y-%m-%d")


def get_research_file_path(dt=None):
    """Get the path to this week's research file."""
    monday = get_week_monday(dt)
    return RESEARCH_DIR / f"week-{monday}.md"


def load_config():
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def get_today_name():
    return DAYS[datetime.now().weekday()]


def init_week():
    """Create a new weekly research file if one doesn't exist."""
    path = get_research_file_path()
    if path.exists():
        print(f"Already exists: {path}")
        return path

    monday = get_week_monday()
    config = load_config()
    topics = TOPICS_PATH.read_text() if TOPICS_PATH.exists() else ""

    content = f"""# Strategy Research — Week of {monday}

## Strongest Threads This Week
<!-- Agents: update this section as compelling threads emerge -->
_No threads yet — the week is just starting._

---

"""
    path.write_text(content)
    print(f"Created: {path}")
    return path


def researcher_prompt():
    config = load_config()
    research_file = get_research_file_path()
    today = get_today_name()
    topics = TOPICS_PATH.read_text() if TOPICS_PATH.exists() else "No topic backlog found."

    # Check if it's early in the week (need to pick topics) or mid-week (build on existing)
    file_exists = research_file.exists()
    existing_content = research_file.read_text() if file_exists else ""

    prompt = f"""{config['researcher_personality']}

TODAY IS: {today}, {datetime.now().strftime('%Y-%m-%d')}
WORKING DIRECTORY: {BASE_DIR}

## Your task

You are the Researcher agent for the Strategy Blog project.

### Step 1: Read the current state
- Read `{research_file}` (create it via `python orchestrator.py init-week` if it doesn't exist)
- Read `config.yaml` for your personality and topic preferences
- Read `topics.md` for the topic backlog

### Step 2: Do real research
- Use web search to find 2-3 current, interesting strategy stories from this week
- Focus on topics from config.yaml's `topics_of_interest`
- Look for: earnings reports, acquisitions, product launches, regulatory moves, market shifts
- Find PRIMARY sources — not just news summaries. Dig into the actual data.
- {"Since it's early in the week, PICK the main topic thread(s) for this week. Choose something with enough depth for a full blog post." if today in ("Monday", "Tuesday") else "Build on the existing threads in the research file. Go deeper on what's already there."}

### Step 3: Write your entry
Append your entry to the research file `{research_file}` using this format:

```
## {today} — R (Researcher) — [Your Topic Title]

[Your research entry — 300-800 words]

**Sources:** [list real URLs you found]
**Open questions [?]:** [questions for the Analyst to dig into]
```

### Step 4: Update the "Strongest Threads" section
If a compelling narrative is emerging, update the "Strongest Threads" section at the top.

## Rules
- ALWAYS use web search to find real, current information
- Never fabricate facts, quotes, or data points
- Reference and respond to previous entries in the file (if any)
- Be specific: name companies, cite numbers, reference dates
- Find the non-obvious angle — what is everyone missing?

## Topic backlog for reference:
{topics}
"""
    return prompt


def analyst_prompt():
    config = load_config()
    research_file = get_research_file_path()
    today = get_today_name()

    prompt = f"""{config['analyst_personality']}

TODAY IS: {today}, {datetime.now().strftime('%Y-%m-%d')}
WORKING DIRECTORY: {BASE_DIR}

## Your task

You are the Analyst agent for the Strategy Blog project.

### Step 1: Read the current state
- Read `{research_file}` — understand everything the Researcher has posted
- Read `config.yaml` for your personality and style preferences

### Step 2: Do your own research
- Use web search to verify claims the Researcher made
- Find counter-examples or data that challenges the narrative
- Look for adjacent stories or historical parallels that add depth
- Find framework-level insights: what strategy pattern is at play here?

### Step 3: Write your entry
Append your entry to `{research_file}` using this format:

```
## {today} — A (Analyst) — [Your Response/Topic Title]

[Your analysis — 300-800 words]

**Key framework:** [name the strategy concept at play]
**Counter-argument:** [the strongest case against the main thesis]
**Sources:** [list real URLs]
**Open questions [?]:** [questions for tomorrow's Researcher entry]
```

### Step 4: Update the "Strongest Threads" section
Refine the top-of-file summary. Which threads are blog-worthy? Which should be dropped?

### Step 5: Rate the week's progress
If it's Thursday or later, add a brief assessment:
- Is there enough material for a strong blog post?
- What's the single strongest narrative arc?
- What gap needs filling before Sunday?

## Rules
- ALWAYS read the full research file before writing
- ALWAYS use web search to verify and add to the research
- Challenge weak claims — but build on strong ones
- Apply named strategy frameworks (Porter, Christensen, Aggregation Theory, etc.) where relevant
- Push toward a clear, opinionated conclusion
"""
    return prompt


def compiler_prompt():
    config = load_config()
    research_file = get_research_file_path()
    today_str = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""{config['blog_style']}

TODAY IS: Sunday, {today_str}
WORKING DIRECTORY: {BASE_DIR}

## Your task

You are the Blog Compiler. Take the week's research discussion and produce a polished strategy blog post.

### Step 1: Read everything
- Read `{research_file}` — the full week of Researcher + Analyst discussion
- Read `config.yaml` for style preferences

### Step 2: Identify the narrative
- What's the single strongest thread from this week?
- What's the narrative arc? (setup → tension → insight → implication)
- What's the opinionated takeaway?

### Step 3: Write the blog
Create a new file in `blogs/` named `{today_str}-[slug].md` where [slug] is a URL-friendly title.

The blog should:
- Be 2000-4000 words
- Open with a compelling hook (not "This week we looked at...")
- Build narrative tension — present the puzzle before the answer
- Weave in the best insights from BOTH agents' contributions
- Include an "Aside" box (using a blockquote) for one fascinating tangent
- Use interesting subheadings (not "Introduction", "Analysis", "Conclusion")
- End with a clear, bold, opinionated takeaway
- Include a "Sources & Further Reading" section at the end

Format:
```markdown
---
title: "[Compelling Title]"
date: {today_str}
topic: "[Primary topic area]"
summary: "[1-2 sentence hook for social media]"
---

[Blog content here]
```

### Step 4: Update topics.md
- Move covered topics to the "Explored" section
- Add any new topic ideas that emerged during the week

### Step 5: Archive note
Add a final entry to the research file:

```
---
## Sunday — Blog Compiled
Blog published: blogs/{today_str}-[slug].md
Main topic: [topic]
Word count: [approximate]
```

## Rules
- The blog should stand alone — a reader shouldn't need the research file
- Attribute insights naturally ("The deeper question is..." not "Agent A said...")
- Every claim should be traceable to a source in the research file
- Be opinionated — the best strategy writing takes a clear stance
"""
    return prompt


def tweet_thread_prompt():
    config = load_config()
    today_str = datetime.now().strftime("%Y-%m-%d")
    blogs_dir = BASE_DIR / "blogs"

    # Find the most recent blog file
    blog_files = sorted(blogs_dir.glob("*.md"), reverse=True)
    latest_blog = blog_files[0] if blog_files else None

    prompt = f"""You are a Twitter/X thread writer for a strategy blog.

TODAY IS: {today_str}
WORKING DIRECTORY: {BASE_DIR}

## Your task

Take the latest blog post and distill it into a compelling Twitter/X thread.

### Step 1: Read the blog
- Read the latest blog: `{latest_blog}`
- Read `config.yaml` for tone preferences

### Step 2: Write the thread
Create a file `blogs/{today_str}-tweet-thread.md` with the thread.

Format:
```markdown
---
type: tweet-thread
date: {today_str}
based_on: "{latest_blog.name if latest_blog else 'latest blog'}"
---

# Tweet Thread: [Topic]

🧵 1/ [Hook tweet — this is the most important one. Must stop the scroll.
Make a bold claim or ask a provocative question. Max 280 chars.]

2/ [Context — set up the story. What happened? Why should anyone care?]

3/ [The non-obvious insight — this is your "aha" moment]

4/ [Supporting evidence / data point]

5/ [The counter-argument or tension]

6/ [Resolution / framework for thinking about it]

7/ [The implication — what does this mean going forward?]

8/ [Bold takeaway / opinion]

9/ [Call to action — "Follow for more strategy deep dives" + link to blog]
```

## Rules
- 8-12 tweets in the thread
- Each tweet MUST be under 280 characters
- Tweet 1 is the hook — it must be scroll-stopping
- Use short, punchy sentences — not blog prose
- Include 1-2 relevant data points from the blog
- Add 2-3 relevant hashtags only on the last tweet
- No emojis except the thread emoji (🧵) on tweet 1
- Write like a smart analyst, not a hype account
- The thread should make people want to read the full blog
"""
    return prompt


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python orchestrator.py [init-week|current-file|researcher-prompt|analyst-prompt|compiler-prompt|tweet-thread-prompt]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init-week":
        init_week()
    elif cmd == "current-file":
        print(get_research_file_path())
    elif cmd == "researcher-prompt":
        print(researcher_prompt())
    elif cmd == "analyst-prompt":
        print(analyst_prompt())
    elif cmd == "compiler-prompt":
        print(compiler_prompt())
    elif cmd == "tweet-thread-prompt":
        print(tweet_thread_prompt())
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
