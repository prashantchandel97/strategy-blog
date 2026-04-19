---
title: "I built a platform that makes AI research actually readable. Here's a full demo."
type: twitter-long-form
date: 2026-04-11
status: draft
---

# Twitter/X Long-Form Article

---

Six months ago I was three newsletters, two YouTube videos, and one arXiv abstract behind on AI research  and still didn't understand what I was building on.

I'm a PM. I needed to understand *why* agents work, not just that they do.

So I built a platform that turns AI research papers into interactive experiences. Let me walk you through it using one paper: **Toolformer** — the 2023 Meta paper that is the direct ancestor of every AI agent calling tools today.

---

![[Pasted image 20260411165304.png]]

This is the **AI Research Evolution Map**. 80+ papers from 2017 to today. Each dot is a paper. Each line is a conceptual dependency.

The slider at the top controls density. "Core" shows only the most foundational connections. "All" shows every relationship in the dataset.

---

![[Pasted image 20260411165443.png]]

Type any paper name and the map focuses. Everything else fades.

Toolformer sits near the center - heavily connected, mid-era, feeding into almost everything that came after it in the agent/tool-use cluster.

This is what "the field evolved" actually looks like as a picture.

---

Click the node and you're on the paper page.

![[Pasted image 20260411165519.png]]


Five tabs. Each one is a different mode of understanding the same paper.

The Core Insight on the Overview tab is always one sentence. For Toolformer:

> *A language model can teach itself when to use external tools - no human labeling required - by generating its own training examples and keeping only the ones that reduce its uncertainty.*

That sentence took me three arXiv reads to arrive at on my own.

---
![[Pasted image 20260411165644.png]]

The **Idea Graph** is the piece I'm most proud of.

Every paper becomes an Obsidian-style concept map. Color coded by role:
- Red = problems the paper is solving
- Purple = key insights
- Blue = mechanisms
- Green = results / what was demonstrated

Click a node → description panel opens + corresponding section in the long-form text below lights up. The paper and the graph are two views of the same structure.

The problem with AI research isn't that it's too hard to understand.

It's that it's presented in a format optimized for peer reviewers, not for the people building on top of it.

Papers like Toolformer contain real insight that should be shaping product decisions. Most of that insight never makes it to the builders because the bridge doesn't exist.

This platform is the bridge.

---

If you want to understand where AI agents actually came from:

→ [AI Papers for PMs — Toolformer](https://prashant-chandel.org/papers/cmmtza2pc000c12zvpro7amiu)

The idea graph alone is worth 20 minutes.

---

*Built with Next.js, D3-force, and too much time spent staring at arXiv.*
