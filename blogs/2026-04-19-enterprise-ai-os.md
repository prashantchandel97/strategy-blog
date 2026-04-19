---
title: "The Database Always Wins: Why SAP and Oracle Are the Most Underappreciated Players in the Enterprise AI War"
date: 2026-04-19
topic: "Enterprise software strategy"
summary: "Everyone is watching Salesforce vs. ServiceNow fight to become the enterprise AI operating system. They're both playing the wrong game — and the ERP incumbents have been quietly winning it the whole time."
---

On March 24, 2026, Oracle did something that received almost no coverage in the enterprise software press: it launched 22 Fusion Agentic Applications, embedded natively inside Oracle Fusion Cloud, spanning finance, HR, supply chain, and customer experience. Not a beta. Not a preview. Generally available, in production, for Oracle's installed base.

Three weeks later, the coverage cycle is entirely absorbed by Salesforce versus ServiceNow — two CRM and ITSM vendors running at each other for the title of "enterprise AI operating system." Oracle's 22-application launch barely registered.

That asymmetry is the story.

---

## The Premise Everyone Has Agreed On (And Why It's Incomplete)

The enterprise AI narrative of early 2026 has a clean, satisfying shape: incumbent SaaS giants are racing to add an orchestration layer above their existing applications, turning themselves from application vendors into platforms. Salesforce built Agentforce and the Atlas Reasoning Engine. ServiceNow positioned itself as the "AI Control Tower." Both companies adopted consumption-based pricing — Salesforce's Flex Credits ($500 per 100,000 credits, roughly $0.10 per AI action) and ServiceNow's Assist Packs — as the commercial model for a post-seat-license world.

The conventional take: one of these two companies will own the enterprise AI OS, the way AWS owns cloud infrastructure or Apple owns mobile. The market is pricing this like a winner-take-most outcome. The strategic conversation has organized itself around which company has the better orchestration platform, the more defensible data moat, and the right commercial structure.

It's a compelling frame. It's also a category error.

The better analogy is not operating systems. It's the enterprise middleware wars of the 2000s — and if you know how those ended, the current landscape looks very different.

---

## The Middleware Wars, Briefly

Between roughly 2000 and 2008, an entire generation of middleware companies competed to become the Enterprise Service Bus: the integration layer that routed data between applications, governed cross-system workflows, and collected a toll on every enterprise transaction. TIBCO, WebMethods, BEA, Vitria — all of them pitched the same story. Whoever routes the data between applications captures the value. Sound familiar?

The outcome was fragmentation, not consolidation. No single vendor captured the orchestration layer outright. The market split into domain oligopolies: TIBCO owned financial services real-time data; MuleSoft owned API-led integrations in Salesforce shops; IBM owned the mainframe-adjacent middleware. And then, in 2018, Salesforce paid $6.5 billion to acquire MuleSoft — not because MuleSoft was winning the middleware war, but because Salesforce needed the integration layer to make its own platform stickier.

That acquisition was an admission. You cannot win the orchestration layer from the application layer alone. Salesforce learned this lesson in 2018 and then immediately set about repeating the underlying mistake with Agentforce.

ServiceNow, to its credit, has a more coherent structural position. The company has spent the last decade becoming the connective tissue of the Fortune 500 — managing IT workflows, HR processes, and increasingly supply chain. Most large enterprises already have a ServiceNow contract. Bill McDermott's "AI Control Tower" positioning is not just a product rebrand; it's a claim that ServiceNow already sits in the cross-system governance layer that every middleware aspirant spent the 2000s fighting to occupy.

But there's a complication. ServiceNow's moat comes from being the system that manages workflows *about* work. The approvals, the tickets, the escalations. When AI agents start automating that work directly — when the AI cancels the order rather than creating a ticket to cancel the order — ServiceNow's workflow volume could shrink even as each unit becomes more valuable. Goldman Sachs and Stifel are bullish on the AI transition. UBS downgraded the stock in April, calling AI a structural headwind rather than tailwind for ServiceNow's core model. Both camps have a point, which is the problem.

---

## The Wildcard With the Wrong Frame

On April 16, OpenAI shipped a Codex desktop update that received the most coverage of any enterprise AI move this week — which is itself a tell about where the attention economy in tech is focused right now.

The capabilities are real and significant. Full computer use: Codex can now operate any Mac application, clicking, typing, taking screenshots, running multiple parallel agents without interfering with the user's active work. A 90+ plugin marketplace combining app integrations and MCP servers. Persistent memory and automation: agents that schedule their own future work and resume tasks across days or weeks.

The strategic framing was "this threatens Salesforce and ServiceNow from below." The bottoms-up distribution playbook — reach individual users directly, before IT governance can intercept, the same way Salesforce bypassed Siebel by going through SMBs before enterprise IT teams knew what was happening.

Here's what makes this genuinely threatening: OpenAI doesn't need to win the enterprise governance layer to win. It just needs to lock in the end-user habit layer before IT departments mandate a governed alternative. If your sales rep is already using Codex to draft proposals, pull CRM data, and schedule follow-ups — through a Mac app, without an IT ticket — the enterprise contract for Agentforce becomes a harder sell.

But here's what limits the threat: the governance gap is temporary, and the regulated enterprises that Salesforce and ServiceNow serve are not going to tolerate unaudited desktop agents for long. A Help Net Security analysis the day after the Codex launch asked the central question directly: "Codex can now operate between apps. Where are the boundaries?" That question has a boring, correct answer: the boundaries are wherever enterprise IT draws them, and they will draw them. The governance gap creates a window for OpenAI, not a moat.

> **Aside:** The Siebel parallel cuts both ways. Salesforce won against Siebel by being simpler, cheaper, and accessible without IT approval — the bottoms-up distribution playbook. OpenAI's Codex is now running the exact same play against Salesforce. But Siebel's real failure wasn't that it lost distribution. It was that Salesforce's data model was fundamentally more accessible — the *product* was easier to use, not just cheaper. Whether Codex is genuinely easier to use than Agentforce for enterprise tasks, or just faster to download, is the empirical question that will determine whether this parallel holds.

---

## The Companies Nobody Is Watching (Who Are Actually Winning)

Let's return to Oracle's 22 Fusion Agentic Applications, which launched on March 24 and were largely ignored.

Oracle's explicit framing for these applications is that being "native to the transactional system" is the decisive differentiator over orchestration layers that sit above the data. Finance agents that live inside your financial data, not above it. HR agents that read your HRIS directly, not through an API call to a middleware layer. Supply chain agents that have authoritative write-back access to the system that actually governs your inventory.

This is not a product pitch. It is a strategic argument — and it is the most coherent strategic argument in this entire competitive landscape.

SAP made the same move more quietly. SAP Joule Studio went generally available in Q1 2026. SAP's Cash Management Agent is in production across a subset of customers, reducing time spent on manual cash positioning by up to 80% through autonomous bank statement analysis. The full Joule platform now spans 40+ agents and 2,400 skills — which is more agent surface area than either Salesforce or ServiceNow has shipped.

The Researcher's take this week called this "strategic silence." The Analyst's pushback was sharper and correct: this is not silence. It is the most coherent strategic argument in the room, and it is coming from the two companies that nobody in the CRM/ITSM world is taking seriously enough.

Here is the argument, stated plainly:

Every AI agent that operates in the enterprise ultimately needs to do one of two things: read from a system of record, or write back to one. The agent that researches a customer's history reads from CRM. The agent that approves a purchase order writes back to ERP. The agent that reconciles supplier invoices writes to the financial system of record. If you own the system of record, you control the last mile of every enterprise AI workflow — the moment of truth where the agent's output becomes an authoritative business transaction.

Salesforce owns the CRM system of record for roughly 150,000 enterprise customers. This is a real and substantial moat. But it's a moat for front-office workflows: customer relationships, sales pipelines, service tickets. The moment an agent needs to cross the perimeter — to update an order in ERP, modify a headcount in HRIS, settle a transaction in the financial system — Salesforce is no longer the system of record. It is a participant.

Oracle and SAP own the systems of record for the workflows that actually run enterprises: financial consolidation, supply chain execution, procurement, workforce management. These are not adjacent to the action layer. They *are* the action layer, for everything that matters to a CFO or a COO.

---

## Why Distribution Speed Might Still Beat Data Depth

The counter-argument deserves a serious treatment, because it is genuinely strong.

SAP Joule has 3% production adoption among SAP's own customer base, despite 40+ agents and 2,400 skills. Let that land. The company with arguably the deepest enterprise data moat, and the most native access to that data, has gotten 3 out of every 100 customers to actually use its AI product in production.

Separately, Gartner estimates that through 2026, enterprises will abandon 60% of AI projects due to insufficient data quality. The implication: the orchestration platform might not matter yet, because the underlying data isn't clean enough for agents to do anything useful with it. If enterprises are hitting a data readiness wall before they can deploy agents at scale, the "platform war" frame is premature by 12 to 18 months. We are in the infrastructure build-out phase, not the winner-takes-distribution phase.

This is the strongest argument against the ERP incumbents winning: their data may be the richest, but their product velocity is poor, and they may be fighting a war that hasn't actually started yet. Meanwhile, Salesforce and ServiceNow are shipping consumption-based commercial models, building agent marketplaces, and training enterprise sales teams on AI-first pitches.

The consumption model itself is worth dwelling on. Salesforce Flex Credits and ServiceNow's Assist Packs are both convergent on the same logic: price AI by the action, not the seat. ServiceNow reported a 55x increase in AI Agent Assist consumption over five months in Q3 2025, with 4x quarter-over-quarter growth in control tower traffic. The company has set a $1 billion AI-specific ACV target by end of 2026, against a total subscription revenue forecast of $15.53–$15.57 billion. These are not hypothetical numbers. The commercial model is working, at scale, right now.

SAP and Oracle do not have equivalent public consumption metrics. The 3% adoption figure is the number that matters, and it is damning.

---

## The Framework That Resolves the Tension

Here is how to hold both sides of this simultaneously without going crazy.

The enterprise AI orchestration battle is playing out on two timescales.

In the near term — the next 12 to 24 months — Salesforce and ServiceNow win on distribution. They have the enterprise relationships, the trained sales forces, the consumption-based commercial models, and the developer ecosystems to get agents into production faster than SAP and Oracle can ship a compelling UX. ServiceNow's cross-system governance position is particularly strong: it is already the system that large enterprises use to manage change across applications, which makes it the natural candidate for governing AI agents that operate across applications.

But in the medium term — beyond 24 months — the system of record thesis reasserts itself. Every enterprise workflow that agents automate has a moment of truth: the write-back. The agent doesn't just draft the supplier payment recommendation; it executes the supplier payment. The agent doesn't just analyze the inventory shortfall; it places the purchase order. Those write-back actions happen in ERP, not in CRM or ITSM. The company whose system accepts the authoritative write-back owns the durable moat.

The critical variable is whether SAP or Oracle can ship agent-native UX fast enough to matter before Salesforce or ServiceNow builds a credible ERP perimeter story. ServiceNow has explicitly said it wants to challenge SAP and Oracle in ERP. If "AI Control Tower" becomes the system running supply chain, finance, and HR in addition to governing the agents that touch those systems, ServiceNow stops being a SaaS company and becomes an enterprise OS. That is the bull case. It requires ServiceNow to win a fight it has never won against competitors it has never beaten in their home domain.

The more likely outcome is the middleware wars outcome: fragmentation into domain oligopolies, with a new interoperability layer — probably provided by a startup or an unexpected incumbent — capturing rent in the middle. The orchestration tax will be collected. The question is whether it goes to Salesforce, ServiceNow, Oracle, SAP, or a company that doesn't have a significant line in this piece.

---

## The Most Important Question Nobody Is Asking

One open question from this week's research deserves to be elevated: what happens to the majority of enterprises that run SAP for finance and Salesforce for CRM simultaneously?

This is not a niche scenario. It is the default architecture of most large enterprises. Your financial system of record is SAP. Your customer system of record is Salesforce. Your IT workflow system is ServiceNow. Your HR system is Workday. You have four "systems of record" that are authoritative for different domains, none of which talk to each other natively.

When an agent needs to process a customer return — which requires reading CRM data, updating inventory in ERP, triggering an IT workflow for exception handling, and logging a finance entry — which system is the agent's home? Whose orchestration layer governs the cross-system write-backs? This is the actual enterprise AI OS question, and it is not answered by any of the companies currently competing for the title.

ServiceNow has the most plausible answer: it's already the company that sits above all these systems for governance and workflow management. But ServiceNow has never had authoritative write-back access to SAP or Oracle. It manages *about* those systems. The moment of truth for the "AI Control Tower" thesis is whether ServiceNow can get ERP-level write-back access — or whether SAP and Oracle will foreclose that path to protect their own agent strategies.

This is a classic platform perimeter battle, and it will be decided not by product features but by enterprise contracts and API access terms. The company that controls the APIs to the systems of record controls the orchestration layer. That is not a technology question. It is a business development and legal question, which means it will take longer to resolve and create more durable outcomes when it does.

---

## So What — For the Three People This Actually Affects

**If you are an enterprise buyer** deciding between Agentforce, ServiceNow AI Control Tower, and rolling your own agent stack: the near-term decision is probably right to focus on Salesforce and ServiceNow, because they will ship faster, have more enterprise-grade governance, and carry less implementation risk than betting on SAP Joule or Oracle Fusion Agentic today. But you should be asking every vendor the same question: when my agent needs to write back to my ERP, what does that look like? Any vendor that can't give you a clear, technically specific answer to that question is selling you a demo, not an enterprise deployment.

**If you are a SaaS investor** with exposure to ServiceNow or Salesforce: the UBS downgrade thesis (AI as structural headwind to seat-based models) and the Goldman bull thesis (AI as consumption-model upside) are both correct, simultaneously, depending on your time horizon. The near-term setup favors Salesforce and ServiceNow capturing consumption revenue from AI. The medium-term risk is that they hit the ERP perimeter and can't cross it. The stock question is whether their multiples price in the near-term opportunity but not the medium-term perimeter risk — which, given where both stocks are trading, is probably the right framing.

**If you are building an agent product** for the enterprise: the system of record insight is the most actionable piece of analysis from this week. Do not build an orchestration layer. Build an application that has authoritative read/write access to the system of record your target customer cares most about, and let the orchestration question be someone else's problem. The middleware companies of the 2000s tried to own the orchestration layer and got commoditized. MuleSoft got acquired for $6.5 billion precisely because it had made itself necessary to the *application* layer (Salesforce) rather than trying to own the orchestration layer independently. That is the playbook.

---

The enterprise AI orchestration war is real. The stakes are real. Salesforce and ServiceNow are genuine contenders with genuine momentum. OpenAI's Codex distribution threat is genuinely novel. But the companies that hold the deepest cards are the ones who launched with the least fanfare. Oracle shipped 22 production agents in March. SAP's Cash Management Agent is reducing manual cash positioning by 80% in live deployments. Neither made the front page.

History has a consistent opinion about enterprise software wars: the database always wins. Not always immediately. Not always cleanly. But the company that owns where the authoritative data lives ends up owning the strategic position. The enterprise AI orchestration battle is a fight about where agents write back to — and the companies who already own those write-back positions are playing a very different game than the one being covered.

---

## Sources & Further Reading

- [The Great Agent War: Salesforce and ServiceNow Clash Over the Future of the Enterprise AI Operating System](https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-the-great-agent-war-salesforce-and-servicenow-clash-over-the-future-of-the-enterprise-ai-operating-system)
- [The Platform of Platforms at a Crossroads: A 2026 Deep Dive into ServiceNow (NOW)](https://markets.financialcontent.com/stocks/article/finterra-2026-4-14-the-platform-of-platforms-at-a-crossroads-a-2026-deep-dive-into-servicenow-now)
- [The AI Control Tower: A Deep Dive into ServiceNow's GenAI Evolution and 2026 Outlook](https://markets.financialcontent.com/stocks/article/finterra-2026-3-31-the-ai-control-tower-a-deep-dive-into-servicenows-now-genai-evolution-and-2026-outlook)
- [Is ServiceNow's AI 'Control Tower' Strategy Deepening Its Cross-Industry Moat?](https://simplywall.st/stocks/us/software/nyse-now/servicenow/news/is-servicenows-now-ai-control-tower-strategy-deepening-its-c)
- [AI governance fuels ServiceNow enterprise momentum](https://www.ciodive.com/news/servicenow-earnings-ai-governance-control-tower/804438/)
- [OpenAI Codex Update Adds Computer Use, Image Generation, and Memory on Mac (April 16, 2026)](https://www.macrumors.com/2026/04/16/openai-codex-mac-update/)
- [OpenAI Expands Codex Desktop App With 90+ Plugins and Full Computer Control](https://creati.ai/ai-news/2026-04-17/openai-expands-codex-desktop-app-plugins-computer-control/)
- [Codex can now operate between apps. Where are the boundaries?](https://www.helpnetsecurity.com/2026/04/17/openai-codex-desktop-update-macos/)
- [How the Atlas Reasoning Engine Powers Agentforce](https://www.salesforce.com/agentforce/what-is-a-reasoning-engine/atlas/)
- [Enterprise Agentic AI Landscape 2026: Trust, Flexibility, and Vendor Lock-in](https://www.kai-waehner.de/blog/2026/04/06/enterprise-agentic-ai-landscape-2026-trust-flexibility-and-vendor-lock-in/)
- [Nvidia launches enterprise AI agent platform with Adobe, Salesforce, SAP among 17 adopters at GTC 2026](https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among)
- [Salesforce Agentforce Flex Credits Pricing — official](https://www.salesforce.com/agentforce/pricing/)
- [Salesforce Introduces Flexible Agentforce Pricing, May 2025](https://www.salesforce.com/news/press-releases/2025/05/15/agentforce-flexible-pricing-news/)
- [ServiceNow Q2 Earnings: Inside the AI Push Toward $1 Billion ACV](https://io-fund.com/ai-stocks/servicenow-q2-ai-push-1b-acv-target-2026)
- [ServiceNow Just Made AI Free and the Pricing War Is Live](https://saasintelligence.substack.com/p/servicenow-just-made-ai-free-and)
- [Oracle Launches Fusion Agentic Applications, March 24, 2026](https://www.oracle.com/news/announcement/oracle-introduces-fusion-agentic-applications-2026-03-24/)
- [Oracle's Fusion Agentic Apps: Can Platform-First AI Finally Deliver Enterprise ROI? — Futurum Group](https://futurumgroup.com/insights/agentic-ai-11/)
- [SAP Joule Agentic AI 2026: Autonomous ERP](https://prolifics.com/usa/resource-center/blog/sap-joule-agentic-ai)
- [SAP Joule 2026: Agentic Enterprise AI — Promise vs. Reality](https://www.innobu.com/en/articles/sap-joule-2026-agentic-enterprise-ai.html)
- [The 3 forces quietly dismantling enterprise software profitability — Fortune, April 17, 2026](https://fortune.com/2026/04/17/ai-saas-enterprise-software-moats-margins-saaspocalypse/)
- [How Salesforce Took Down Siebel — And Could Face the Same Fate](https://medium.com/@ianhayes2121/how-salesforce-took-down-siebel-and-could-face-the-same-fate-aef7d2d4ed3e)
- [OpenAI Codex Now Controls Your Mac — Desktop Agents Go Live](https://aiautomationglobal.com/blog/openai-codex-computer-use-desktop-automation-april-2026)
