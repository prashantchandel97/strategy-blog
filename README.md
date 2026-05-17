# Strategy Blog

A fully automated system that researches, writes, and publishes a weekly strategy and business analysis blog at [prashant-chandel.org/blog](https://prashant-chandel.org/blog) — with a Twitter/X thread posted every Sunday.

No manual writing. No manual posting. It runs itself.

---

## What It Does

Every week, the system:

1. **Researches** business and tech strategy topics Monday through Saturday, pulling from live news, earnings calls, filings, and primary sources
2. **Analyzes** the research daily, stress-testing ideas, building frameworks, and finding the sharpest angles
3. **Compresses** the week's work into a tight summary each evening so nothing is lost
4. **Writes a long-form blog post** on Sunday morning, 2,500-3,500 words in plain English
5. **Generates a tweet thread** (2-7 tweets) distilling the core argument with a hook
6. **Publishes everything** automatically: blog to the website, thread to Twitter/X with an infographic attached

The writing style is Acquired-meets-Stratechery: deep on the business logic, plain on the language. Every claim is explained. No jargon left undefined. No filler.

---

## Output

- Weekly blog posts covering: AI infrastructure, platform shifts, market structure, startup strategy, fintech, media, and more
- Each post includes an infographic summarizing the key data
- A matching tweet thread goes out every Sunday with the infographic attached to the first tweet

---

## Stack

- **GitHub Actions** runs the full pipeline on a cron schedule, no server needed
- **Anthropic Claude** handles research synthesis, analysis, writing, and tweet composition
- **Brave Search** feeds current news and trends into the research pipeline
- **Tweepy** posts the thread to Twitter/X via the v2 API
- **A custom website API** receives the finished blog post

---

## Schedule

| Day | What runs |
|-----|-----------|
| Mon - Sat | Morning: research pass. Evening: analyst pass. Night: rolling summary update |
| Sunday | Morning: blog compiled. Mid-morning: tweet thread written. Noon: everything published |

---

## Topics Covered

Business strategy and technology, focused on understanding why things actually work the way they do:

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
