# Strategy Blog

A fully automated system that researches, writes, and publishes a weekly strategy and business analysis blog at [prashant-chandel.org/blog](https://prashant-chandel.org/blog), with a Twitter/X thread posted every Sunday.

No manual writing. No manual posting. It runs itself. And it gets better every week.

---

## What It Does

Every week, the system:

1. **Researches** business and tech strategy topics Monday through Saturday, pulling from live news, earnings calls, filings, and primary sources
2. **Analyzes** the research daily, stress-testing ideas, building frameworks, and finding the sharpest angles
3. **Compresses** the week's work into a rolling summary each evening so nothing is lost
4. **Scouts trends** on Sunday night, feeding the next week's research with signals from Hacker News and fresh search results
5. **Writes a long-form blog post** on Sunday morning, 2,500-3,500 words in plain English
6. **Generates a tweet thread** (2-7 tweets) distilling the core argument with a hook
7. **Publishes everything** automatically: blog to the website, thread to Twitter/X with an infographic attached

The writing style is Acquired-meets-Stratechery: deep on the business logic, plain on the language. Every claim is explained. No jargon left undefined. No filler.

---

## How It Gets Better Over Time

The system has two feedback loops that compound week after week.

**Content quality loop:** Every Monday morning, the system measures how each tweet in the thread performed: impressions, likes, retweets, bookmarks, and how many people read through to the end. That data gets compressed into a performance memory file. The researcher uses it to prioritise topics the audience responds to. The tweet writer uses it to sharpen hooks and pick the right thread length.

**Editorial memory loop:** After every post, the compiler records what was argued, what frameworks were introduced, what questions were left open, and what positions were taken. This editorial memory persists across weeks. Future posts can build on established concepts instead of re-explaining them, continue narrative threads across multiple posts, and stay consistent in the arguments they make. Every month, both memory files get compressed so they stay compact.

The result: the blog develops a coherent body of work rather than a series of disconnected weekly takes.

---

## Output

- Weekly long-form blog posts covering strategy, AI, markets, and business models
- Each post includes an infographic summarizing the key data
- A matching tweet thread every Sunday with the infographic attached to the first tweet

---

## Stack

- **GitHub Actions** runs the full pipeline on a cron schedule, no server needed
- **Anthropic Claude** handles research synthesis, analysis, writing, tweet composition, and memory compression
- **Brave Search** feeds current news and trends into the research pipeline
- **Tweepy** posts the thread to Twitter/X via the v2 API
- **A custom website API** receives the finished blog post

---

## Schedule

| When | What runs |
|------|-----------|
| Mon - Sat, 9am | Research pass |
| Mon - Sat, 5pm | Analyst pass |
| Mon - Sat, 6pm | Rolling summary update |
| Sunday 10am | Blog compiled |
| Sunday 11am | Tweet thread written |
| Sunday 12pm | Everything published |
| Monday 2pm | Engagement metrics fetched from Twitter API |
| First Monday of month | Memory compression pass |

---

## Topics Covered

Business strategy and technology, focused on understanding why things work the way they do:

- AI and infrastructure shifts
- Platform dynamics and competitive moats
- Market structure and regulation
- Startup growth patterns
- Fintech and payments
- Enterprise software
- India tech ecosystem
- Media and distribution

---

## Philosophy

Most strategy writing tells you what happened. This tries to explain why it happened and why it matters to someone who was not already following it.

Every post is written as if explaining to a smart friend over coffee, not a consultant writing a memo. If a concept is used, it is defined. If a number is cited, the implication is spelled out. The goal is that a reader finishes each piece genuinely understanding something new.

---

## Blog

[prashant-chandel.org/blog](https://prashant-chandel.org/blog)
