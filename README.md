# Strategy Blog

A multi-agent system that researches, writes, and publishes a weekly strategy and business analysis blog at [prashant-chandel.org/blog](https://prashant-chandel.org/blog), with a Twitter/X thread posted every Sunday.

The research and writing is fully automated. The posting is human-in-the-loop: every weekday morning the system compiles the best tweetable insight from that day's research and delivers 3-5 ready-to-post options by Telegram. The author picks the best one. No copy-pasting. No scrolling through research notes. Just a tap.

---

## What It Does

**Every weekday (Mon-Fri):**

1. **Researches** a business and tech strategy topic, pulling from live news, earnings calls, filings, and primary sources (9am)
2. **Analyzes** the research, stress-testing ideas, building frameworks, finding the sharpest angles (5pm)
3. **Compresses** the day's work into a rolling weekly summary (6pm)
4. **Drafts a Daily Intelligence Brief** with 3-5 tweetable options from that day's research, sent to the author's phone by Telegram (11am)

**Every Sunday:**

5. **Scouts trends** on Sunday night, feeding the next week's research with signals from fresh search results
6. **Writes a long-form blog post** (2,500-3,500 words, plain English, Acquired-style depth)
7. **Generates a tweet thread** (2-7 tweets) distilling the core argument with a hook
8. **Publishes everything** automatically: blog to the website, thread to Twitter/X

**The author's only job on weekdays:** open Telegram, read 3-5 tweet options, pick one, paste and post.

The writing style is Acquired-meets-Stratechery: deep on the business logic, plain on the language. Every claim is explained. No jargon left undefined. No filler.

---

## Daily Intelligence Brief

Every weekday at 11am, the system sends a brief like this to Telegram:

```
STRATEGY BRIEF | Monday, May 18

Today's research: Microsoft compute spend reveals the AI buildout scale
Domain: AI and infrastructure

TWEET OPTIONS

[A] The Number

$47B: Microsoft's disclosed AI compute spend across 2022-2025. More than
Netflix spent on content in the same 3 years, for a product with zero
subscriptions attached yet.
(178 chars)

[B] Historical Parallel

The AI compute buildout maps onto 1990s telecom: massive capex, optimistic
demand forecasts, and consolidation within 5 years. The question is not if.
It is who survives.
(169 chars)

[C] Counter-Narrative

Everyone assumes AI capex is destroying margins. Microsoft's operating margin
hit 45% last quarter while tripling AI spend. The unit economics are working.
The market is mispricing this.
(189 chars)

EARNINGS WATCH
Amazon reports Wednesday. Watch: AWS growth rate (last Q: 17%). Why it
matters: first real signal on whether AI inference is accelerating cloud spend.

Source: Microsoft Q3 2025 earnings filing + Azure investor day transcript
```

The author picks an option and posts it. No rewriting. No looking up sources. Done in 30 seconds.

---

## How It Gets Better Over Time

The system has two feedback loops that compound week after week.

**Editorial memory loop:** After every blog post, the system records what was argued, what frameworks were introduced, what positions were taken, and what questions were left open. This memory persists across weeks. Future posts build on established concepts instead of re-explaining them, continue narrative threads, and stay consistent. Every month the memory files get compressed so they stay compact.

**Topic signal loop:** The researcher reads an insights file that tracks which topic categories have historically resonated with the audience. It uses this to break ties between equally interesting stories. Over time the system leans toward what works.

The result: the blog develops a coherent body of work rather than a series of disconnected weekly takes.

---

## Output

- Weekly long-form blog posts covering strategy, AI, markets, and business models
- Each post includes an infographic summarizing the key data
- A matching tweet thread every Sunday with the infographic attached to the first tweet
- A weekday Telegram brief with 3-5 ready-to-post tweet options (human picks and posts)

---

## Stack

- **GitHub Actions** runs the full pipeline on a cron schedule, no server needed
- **Anthropic Claude** handles research synthesis, analysis, writing, tweet drafting, and memory compression
- **Brave Search** feeds current news and trends into the research pipeline
- **Tweepy** posts the Sunday thread to Twitter/X via the v2 API
- **Telegram Bot API** delivers the weekday brief to the author's phone
- **A custom website API** receives the finished blog post

---

## Schedule

| When | What runs |
|------|-----------|
| Mon - Sat, 9am CDT | Research pass |
| Mon - Sat, 5pm CDT | Analyst pass |
| Mon - Sat, 6pm CDT | Rolling summary update |
| Mon - Fri, 11am CDT | Daily Intelligence Brief compiled and sent to Telegram |
| Sunday 10am CDT | Blog compiled |
| Sunday 11am CDT | Tweet thread written |
| Sunday 12pm CDT | Everything published |
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

## Setup

To run your own version:

1. Add GitHub secrets: `ANTHROPIC_API_KEY`, `BRAVE_API_KEY`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
2. For Sunday publishing: add `TWITTER_CONSUMER_KEY`, `TWITTER_CONSUMER_SECRET`, `TWITTER_ACCESS_TOKEN`, `TWITTER_ACCESS_TOKEN_SECRET`, and your website `N8N_API_KEY`
3. Edit `config.yaml` with your topics and style preferences
4. Edit `tracked-companies.md` with the companies you want earnings alerts for
5. Push to GitHub. The workflows start on schedule automatically.

To get your Telegram `CHAT_ID`: message your bot once, then call `https://api.telegram.org/bot{TOKEN}/getUpdates` and look for `"chat":{"id":...}`.

---

## Philosophy

Most strategy writing tells you what happened. This tries to explain why it happened and why it matters to someone who was not already following it.

Every post is written as if explaining to a smart friend over coffee, not a consultant writing a memo. If a concept is used, it is defined. If a number is cited, the implication is spelled out. The goal is that a reader finishes each piece genuinely understanding something new.

---

## Blog

[prashant-chandel.org/blog](https://prashant-chandel.org/blog)
