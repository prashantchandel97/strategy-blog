---
title: "When Regulatory Moats Become Liabilities"
date: 2026-06-29
topic: "Business Strategy & Regulation"
summary: "Salesforce and Razorpay solved 2026 FTC enforcement. But antitrust enforcement in 2027-2028 turns today's regulatory moat into tomorrow's structural liability. Accenture lost $240M betting on the wrong regulatory cycle."
---

On June 18, Accenture told investors it was cutting growth guidance from 5% to 3-4%. That 1-2 point drop doesn't sound dramatic until you realize it represents over $240 million in cancelled contracts. The reason? Not competition from OpenAI or Anthropic. Not client budget cuts. Regulatory risk. Specifically, the risk that outcome-based pricing (where you charge based on "time saved" or "revenue generated" instead of hours worked) falls under FTC algorithmic pricing enforcement. Clients walked away because they couldn't defend the causality required to prove results, and neither could Accenture.

Meanwhile, Salesforce breezed through the same regulatory environment with zero contract cancellations. Their solution: Flex Credits, where you pay $0.10 per measurable action (like an automated email or a case resolution). Same AI, same automation, completely different regulatory exposure. And Razorpay, processing 30-40% of India's digital payments, spent two years and complied with regulatory capital requirements that keep out every competitor except those willing to lock up ₹25 crore ($3 million) in net worth. They just raised money at a premium valuation, regulatory moat intact.

Here's the tension: Accenture, Salesforce, and Razorpay were all solving the same problem (how to prove value without triggering regulatory liability), but they made different bets on which regulatory cycle would matter. Accenture bet on measurement sophistication. Salesforce bet on transparency. Razorpay bet on compliance barriers. Two worked, one didn't. The question is whether the two winners stay winners, or whether the next enforcement cycle (already visible in Google's Chrome divestiture order from June 2026, and Meta and Uber antitrust verdicts the same month) turns regulatory defensibility into regulatory liability.

> **TL;DR** — The market just went through three years of regulatory enforcement targeting deceptive pricing and measurement opacity. Companies that built moats by solving transparency (Salesforce's Flex Credits) or regulatory licensing (Razorpay's Payment Aggregator license) won. But 2027-2028 antitrust enforcement shifts the target from deception to market concentration and exclusionary conduct. Razorpay's 30-40% payment market share becomes monopoly risk. Salesforce's CRM dominance bundled with AI becomes market leverage risk. Regulatory moats last 5-10 years, then enforcement priorities shift. The companies preparing for Cycle 2 (antitrust) while executing Cycle 1 (deception enforcement) survive. Everyone else faces structural remedies.

**In this piece:**
- Accenture lost $240 million in contracts because outcome-based pricing requires proving causality that no vendor can defend under FTC scrutiny, while Salesforce's consumption model (Flex Credits) survived because auditable actions pass regulatory tests that outcome metrics fail.
- Regulatory moats like Razorpay's Payment Aggregator license create real defensibility for 5-10 years by locking out competitors who can't meet capital requirements, but they're legal defenses that expire when enforcement priorities shift or scaled competitors (PhonePe, Paytm) acquire their own licenses.
- The enforcement cycle is moving from Cycle 1 (2024-2026 deception and algorithmic pricing) to Cycle 2 (2027-2028 market concentration and exclusionary conduct), visible in Google's Chrome divestiture, Meta jury verdicts, and Uber antitrust losses all happening in June 2026.
- Razorpay's 30-40% payment market share and Salesforce's CRM bundling with Agentforce both become antitrust targets under Cycle 2 enforcement, turning today's regulatory moat into tomorrow's structural liability unless companies prepare for unbundling or forced licensing remedies now.
- Companies hit by two shifts simultaneously (regulatory + architectural, like Turtlemint facing embedded insurance and PhonePe distribution, or INFLUISH facing regulatory capital requirements) fail even with strong underlying metrics because moats don't travel across enforcement contexts.

<div style="margin: 2rem 0;">
<svg viewBox="0 0 800 480" xmlns="http://www.w3.org/2000/svg" style="font-family: Inter, system-ui, -apple-system, sans-serif; width:100%; height:auto; display:block;">
  <!-- Background -->
  <rect x="0" y="0" width="800" height="480" fill="#F8FAFC"/>
  
  <!-- Header -->
  <rect x="0" y="0" width="800" height="3" fill="#2563EB"/>
  <rect x="0" y="3" width="800" height="49" fill="#0F172A"/>
  <text x="400" y="34" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">
    Regulatory Moats: 5-10 Year Windows, Not Permanent Defenses
  </text>
  
  <!-- Timeline spine -->
  <line x1="80" y1="140" x2="720" y2="140" stroke="#E2E8F0" stroke-width="3"/>
  
  <!-- Cycle 1: 2024-2026 -->
  <circle cx="200" cy="140" r="10" fill="#2563EB" stroke="#FFFFFF" stroke-width="2"/>
  <text x="200" y="120" text-anchor="middle" font-size="13" font-weight="600" fill="#0F172A">2024-2026</text>
  <text x="200" y="170" text-anchor="middle" font-size="12" font-weight="600" fill="#1E3A5F">Cycle 1: Deception</text>
  <text x="200" y="188" text-anchor="middle" font-size="11" fill="#475569">FTC algorithmic pricing</text>
  <text x="200" y="204" text-anchor="middle" font-size="11" fill="#475569">Transparency enforcement</text>
  
  <!-- Transition: June 2026 -->
  <circle cx="400" cy="140" r="10" fill="#F59E0B" stroke="#FFFFFF" stroke-width="2"/>
  <text x="400" y="120" text-anchor="middle" font-size="13" font-weight="600" fill="#0F172A">June 2026</text>
  <text x="400" y="170" text-anchor="middle" font-size="12" font-weight="600" fill="#F59E0B">Enforcement Shift</text>
  <text x="400" y="188" text-anchor="middle" font-size="11" fill="#475569">Google Chrome order</text>
  <text x="400" y="204" text-anchor="middle" font-size="11" fill="#475569">Meta/Uber verdicts</text>
  
  <!-- Cycle 2: 2027-2028 -->
  <circle cx="600" cy="140" r="10" fill="#DC2626" stroke="#FFFFFF" stroke-width="2"/>
  <text x="600" y="120" text-anchor="middle" font-size="13" font-weight="600" fill="#0F172A">2027-2028</text>
  <text x="600" y="170" text-anchor="middle" font-size="12" font-weight="600" fill="#DC2626">Cycle 2: Antitrust</text>
  <text x="600" y="188" text-anchor="middle" font-size="11" fill="#475569">Market concentration</text>
  <text x="600" y="204" text-anchor="middle" font-size="11" fill="#475569">Bundling enforcement</text>
  
  <!-- Arrow indicating direction -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#94A3B8"/>
    </marker>
  </defs>
  <line x1="210" y1="140" x2="390" y2="140" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  <line x1="410" y1="140" x2="590" y2="140" stroke="#94A3B8" stroke-width="1.5" marker-end="url(#arrowhead)"/>
  
  <!-- Company outcome cards -->
  <!-- Card shadows (subtle) -->
  <rect x="43" y="253" width="230" height="200" rx="8" fill="#0000000D"/>
  <rect x="288" y="253" width="230" height="200" rx="8" fill="#0000000D"/>
  <rect x="533" y="253" width="230" height="200" rx="8" fill="#0000000D"/>
  
  <!-- Card backgrounds -->
  <rect x="40" y="250" width="230" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
  <rect x="285" y="250" width="230" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
  <rect x="530" y="250" width="230" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
  
  <!-- Card header bars -->
  <rect x="40" y="250" width="230" height="3" rx="8" fill="#DC2626"/>
  <rect x="285" y="250" width="230" height="3" rx="8" fill="#059669"/>
  <rect x="530" y="250" width="230" height="3" rx="8" fill="#059669"/>
  
  <!-- Card 1: Accenture (Failed) -->
  <text x="155" y="276" text-anchor="middle" font-size="13" font-weight="600" fill="#1E3A5F">Accenture</text>
  <text x="155" y="292" text-anchor="middle" font-size="11" fill="#94A3B8">Failed Cycle 1</text>
  
  <text x="155" y="320" text-anchor="middle" font-size="30" font-weight="700" fill="#DC2626">$240M</text>
  <text x="155" y="338" text-anchor="middle" font-size="11" fill="#94A3B8">contracts cancelled</text>
  
  <text x="56" y="365" font-size="12" fill="#475569">▸ Outcome pricing undefendable</text>
  <text x="56" y="384" font-size="12" fill="#475569">▸ No counterfactual audit trail</text>
  <text x="56" y="403" font-size="12" fill="#475569">▸ Hit by regulatory + AI shifts</text>
  <text x="56" y="422" font-size="12" fill="#475569">▸ Guidance cut 5% → 3-4%</text>
  
  <!-- Card 2: Salesforce (Survived, at risk) -->
  <text x="400" y="276" text-anchor="middle" font-size="13" font-weight="600" fill="#1E3A5F">Salesforce</text>
  <text x="400" y="292" text-anchor="middle" font-size="11" fill="#94A3B8">Survived Cycle 1, Cycle 2 risk</text>
  
  <text x="400" y="320" text-anchor="middle" font-size="30" font-weight="700" fill="#059669">Zero</text>
  <text x="400" y="338" text-anchor="middle" font-size="11" fill="#94A3B8">cancellations</text>
  
  <text x="301" y="365" font-size="12" fill="#475569">▸ Flex Credits auditable ($0.10/action)</text>
  <text x="301" y="384" font-size="12" fill="#475569">▸ CRM lock-in = product moat</text>
  <text x="301" y="403" font-size="12" fill="#475569">▸ But: 23% market share</text>
  <text x="301" y="422" font-size="12" fill="#475569">▸ Agentforce bundling = antitrust risk</text>
  
  <!-- Card 3: Razorpay (Survived, at risk) -->
  <text x="645" y="276" text-anchor="middle" font-size="13" font-weight="600" fill="#1E3A5F">Razorpay</text>
  <text x="645" y="292" text-anchor="middle" font-size="11" fill="#94A3B8">Survived Cycle 1, Cycle 2 risk</text>
  
  <text x="645" y="320" text-anchor="middle" font-size="30" font-weight="700" fill="#059669">30-40%</text>
  <text x="645" y="338" text-anchor="middle" font-size="11" fill="#94A3B8">payment market share</text>
  
  <text x="546" y="365" font-size="12" fill="#475569">▸ PA license = ₹25cr barrier</text>
  <text x="546" y="384" font-size="12" fill="#475569">▸ Blocks startups, not giants</text>
  <text x="546" y="403" font-size="12" fill="#475569">▸ Market concentration risk</text>
  <text x="546" y="422" font-size="12" fill="#475569">▸ Moat duration: 5-10 years</text>
  
  <!-- Source -->
  <text x="790" y="472" text-anchor="end" font-size="10" fill="#94A3B8">prashant-chandel.org/blog</text>
</svg>
</div>

## Why Outcome Pricing Hit a Ceiling

Let me break down what happened to Accenture, because it explains a much bigger pattern about regulatory moats.

For years, enterprise software moved toward "outcome-based pricing." Instead of charging per user or per hour, you charge based on results: time saved, revenue generated, customer satisfaction improvement. The logic was simple. CFOs want to pay for results, not activity. If your AI agent saves the sales team 20 hours per week, charge based on the hours saved, not the number of agents deployed.

By Q1 2026, roughly 21.7% of enterprise software contracts were outcome-based (this is from a Futurum survey of 838 decision-makers). Another 60% were hybrid models, mixing seat licenses with outcome payments. Pure consumption models (pay per API call, per token, per action) sat at 43% preference. The trend seemed unstoppable.

Then the FTC made algorithmic pricing enforcement a 2026 priority. Algorithmic pricing means using software to set prices dynamically based on user behavior, market conditions, or other inputs the customer can't see or audit. The FTC's concern: companies hide margin extraction behind complexity. You can't tell if you're getting a fair price when the algorithm adjusts based on your desperation or willingness to pay.

Here's where outcome-based pricing ran into a wall. To charge based on "time saved," you need to prove causality. You need to show that your software caused the time savings, not something else (the employee got better at their job, the process changed, the workload decreased). That requires a counterfactual: what would have happened without your software? And counterfactuals are, by definition, unmeasurable. You can estimate them, but you can't audit them.

The FTC and EU regulators (the EU AI Act went into effect August 2, 2026) both require explainability for high-risk automated systems. Outcome pricing is a high-risk system because it directly affects what customers pay. If you can't explain how you calculated the outcome, you can't defend the price. And if you can't defend the price, you have regulatory liability.

Salesforce solved this by moving to Flex Credits. Instead of charging based on "deals closed faster" or "time saved," they charge $0.10 per action: an automated email sent, a case resolved, a data enrichment performed. These are all auditable events. You can count them. You can verify them. There's no counterfactual required. The FTC can look at your bill, see 10,000 actions at $0.10 each, and confirm the math. No algorithmic pricing risk.

Accenture didn't have that option. Consulting work is inherently outcome-based. You're hired to solve a problem (improve margins, launch a product, restructure operations), and the value is in the result. You can't break it down into countable micro-actions the way Salesforce can. So when clients realized they'd have to defend outcome-based contracts to regulators who now view outcome measurement as algorithmic pricing, they cancelled. Not because the work wasn't valuable. Because the regulatory risk was uninsurable.

The result: outcome-based pricing hit a ceiling at 20-30% adoption. It works in narrow cases where outcomes are directly measurable without counterfactuals (e.g., Zendesk charging per verified customer support resolution, where "verified" means the customer confirmed the issue was fixed). It fails everywhere else.

This is the first lesson: **regulatory moats require you to solve the regulator's problem, not just the customer's problem.** Salesforce built a moat not by measuring outcomes better than competitors, but by choosing a measurement method that passes regulatory scrutiny. Accenture optimized for client ROI and lost to regulatory design.

## When Regulatory Barriers Become Moats

Now let's look at Razorpay. They process 30-40% of India's digital payments through their Payment Aggregator (PA) platform. A payment aggregator sits between merchants and banks, handling the complexity of connecting to multiple payment methods (credit cards, UPI, wallets, net banking) so the merchant only integrates once.

In September 2025, the Reserve Bank of India (RBI) published final Payment Aggregator directions. The big requirement: ₹25 crore ($3 million) in net worth. That's not revenue. That's capital you have to have sitting in the company, unencumbered, to prove you can survive operational shocks and settlement failures.

For Razorpay, already at scale, this was annoying but manageable. They raised capital, met the requirement, and got their PA license. For startups trying to enter the market, it's a wall. You need to raise $3 million just to get the license, before you process a single transaction. And because payment aggregation is a volume business with thin margins (you earn 1-2% per transaction), you need massive scale to justify that upfront capital.

The result: Razorpay has a regulatory moat. Not because they have better technology or distribution (though they do). Because they met a compliance requirement that prevents new competitors from entering the market unless they have venture backing or deep-pocketed parents.

This is what happened to INFLUISH. They built a creator payment settlement layer with 500,000 creators and 50% month-over-month growth. The moat was real: once creators earned money across multiple platforms through INFLUISH's settlement layer, switching costs were high. You'd have to reconfigure payouts for every brand deal, every platform, every contract.

But INFLUISH didn't have ₹25 crore. And they couldn't raise it fast enough. So they got acquihired. The settlement layer became a feature inside someone else's product, not a standalone moat. The regulatory requirement killed the company even though the product worked and customers wanted it.

> **Aside:** This dynamic, where regulatory capital requirements become the primary filter for market entry, is accelerating across fintech. India's NBFC (non-banking financial company) license requires ₹200 crore ($24 million) in net worth. Lending licenses, payment licenses, insurance distribution licenses all have similar floors. The result is that fintech in India is bifurcating into two groups: companies with licenses (who can build moats) and companies without (who become features or get acquihired). The middle ground is disappearing.

Razorpay's moat is durable for 5-10 years. That's how long it takes for scaled competitors (PhonePe, Paytm, Google Pay) to decide the payment aggregation market is worth entering, apply for their own PA licenses, and spend the 18-24 months navigating RBI approval. Once they enter, Razorpay's moat erodes to competition on fees, integration quality, and customer service. The regulatory barrier kept out startups, not giants.

This is the second lesson: **regulatory moats are time-limited defenses, not permanent business moats.** They give you a window (5-10 years) to build something else (distribution, brand, switching costs) that survives after the regulatory barrier falls or competitors clear it.

## Why Moats Fail Against Architectural Shifts

Turtlemint is a useful contrast. They built a large insurance distribution network in India: thousands of agents selling policies through Turtlemint's platform. By FY25, they'd improved service EBITDA margin from -12% (FY23) to +11.89%. Profitability, growing revenue, real business.

Their IPO in late June 2026 priced at an 11% discount to the initial range. Not because of the numbers. Because the market looked at PhonePe and Paytm (who don't have agent networks) earning 35-45% margins on embedded insurance versus Turtlemint's 11-12%, and realized the agent network wasn't a moat. It was a cost structure.

Here's what happened. Insurance used to require agents because buying a policy was complicated: comparing plans, understanding exclusions, filling out applications. Agents simplified the process and provided trust (you're trusting them with your financial security, so personal relationships mattered).

Then UPI (India's instant payment network) embedded insurance distribution directly into payment flows. You're paying your phone bill on PhonePe, it offers you device insurance right there, you click yes, the premium gets added to your transaction, done. No agent. No comparison shopping. The distribution happens inside a flow you were already completing.

The result: PhonePe and Paytm earn 35-45% on insurance because they have zero agent costs. Turtlemint earns 11-12% because they pay agents. The moat (agent relationships, agent training, agent software) didn't just get competed away. It became a liability. The architecture changed, and the old moat became drag.

This is why architectural shifts are more dangerous than competition. When PhonePe competes with Turtlemint by building a better agent platform, Turtlemint can respond (improve their software, offer better commissions, invest in agent training). When PhonePe competes by eliminating agents entirely, Turtlemint's entire cost structure is wrong for the new game. You can't optimize your way out. You'd have to rebuild from scratch, and by then, PhonePe and Paytm have the embedded distribution advantage.

This is the third lesson: **moats don't travel across architectural shifts.** You can't defend an agent network moat in an embedded distribution world. You can't defend an outcome-pricing moat in a consumption-based pricing world. You can't defend a regulatory moat in a new enforcement cycle. The moat has to match the structure of the game being played.

## The Cycle Is Shifting

Here's why this all matters right now. June 2026 saw three major antitrust events:

1. **Google's Chrome and Android divestiture order** was enforced (this came out of the 2023 DOJ antitrust case). Google has to spin out Chrome and license Android on fair terms to competitors. The remedy is structural: break up the company's control over distribution.

2. **Meta lost a jury verdict** in an antitrust case over Instagram's acquisition of a competitor. The finding: Meta used its dominance to prevent competitive threats.

3. **Uber lost an antitrust case** over driver classification and market power in the gig economy.

These aren't regulatory enforcement like the FTC algorithmic pricing crackdown. These are antitrust cases targeting market concentration and exclusionary conduct (when a dominant company uses its position to block competitors or lock in customers unfairly).

The shift is from **Cycle 1** (2024-2026: deception, transparency, algorithmic pricing) to **Cycle 2** (2027-2028: market concentration, bundling, exclusionary conduct).

In Cycle 1, Salesforce won by being transparent. Flex Credits pass FTC scrutiny because you can audit every charge. Razorpay won by meeting licensing requirements. The PA license proves they can handle settlement risk.

In Cycle 2, Salesforce's dominance becomes the risk. They own roughly 23% of the global CRM market (per Gartner, which tracks this). Now they're bundling Agentforce (their AI agent platform) into CRM subscriptions at $125-650 per user per month. If you're a CRM customer, you get Agentforce whether you want it or not (in most packaging tiers). That's bundling. And bundling by a dominant player to extend market power into a new category (AI agents) is exactly what antitrust enforcers target.

The precedent is Microsoft bundling Internet Explorer into Windows in the 1990s. Microsoft wasn't punished for having a dominant OS. They were punished for using OS dominance to kill competition in browsers by making IE the default and free. Salesforce bundling Agentforce into CRM is the same structure: using CRM dominance (where they have lock-in through data and workflows) to win in AI agents (where they don't yet have dominance).

Razorpay faces similar risk. Processing 30-40% of India's digital payments creates market concentration. If the Competition Commission of India (CCI) investigates and finds exclusionary conduct (e.g., favorable terms to merchants who use only Razorpay, or blocking access to certain payment rails for competitors), that 30-40% share becomes liability. The regulatory moat (PA license) that kept out startups becomes evidence of dominance in an antitrust case.

This is the fourth lesson, and the hardest one: **regulatory moats built in one enforcement cycle become liabilities in the next cycle.** What protected you from Cycle 1 enforcement (transparency, licensing) exposes you to Cycle 2 enforcement (dominance, bundling).

## What Separates Survivors from Failures

So why did Accenture, Turtlemint, and INFLUISH fail, while Salesforce and Razorpay (so far) succeeded?

The pattern is being hit by **two shifts simultaneously.** Accenture got hit by regulatory shift (FTC enforcement) and architectural shift (AI agents replacing consulting headcount). Turtlemint got hit by regulatory shift (embedded insurance regulation favoring platforms) and architectural shift (UPI distribution eliminating agents). INFLUISH got hit by regulatory shift (₹25 crore PA requirement) and market timing (couldn't raise before the requirement took effect).

Salesforce and Razorpay each solved one shift. Salesforce solved the regulatory shift (moved to Flex Credits) but has existing CRM lock-in protecting them from architectural shifts in their core business. Razorpay solved the regulatory shift (got PA license) but has existing payment distribution protecting them from new entrants.

The key is **layering defenses.** Regulatory moats alone don't work because enforcement priorities shift every 3-5 years. Architectural moats alone don't work because someone always rebuilds the architecture (see: Turtlemint losing to embedded distribution). You need both. You solve the current regulatory cycle (Cycle 1: transparency and licensing) while preparing for the next regulatory cycle (Cycle 2: antitrust and unbundling) **and** you build product lock-in that survives architectural changes (Salesforce's CRM data moat, Razorpay's merchant integration moat).

Companies that only solve one layer get disrupted by the other. Accenture had client relationships but no regulatory defense and no product lock-in (clients can switch consultants). INFLUISH had product engagement but no regulatory defense (couldn't meet capital requirements). Turtlemint had agent relationships but no architectural defense (embedded distribution bypassed agents).

The companies surviving both cycles right now are doing three things:

1. **Solving the current enforcement priority** (transparency, explainability, licensing)
2. **Preparing for the next enforcement priority** (antitrust remedies: can you unbundle without destroying the business? can you license your platform on fair terms? can you prove you're not engaging in exclusionary conduct?)
3. **Building non-regulatory moats that survive both cycles** (switching costs, data moats, distribution advantages that work regardless of which regulations apply)

Salesforce has CRM data and workflow lock-in (non-regulatory moat) + Flex Credits compliance (Cycle 1 defense) but faces Agentforce bundling risk (Cycle 2 exposure). Razorpay has merchant integration and settlement trust (non-regulatory moat) + PA license (Cycle 1 defense) but faces market share concentration risk (Cycle 2 exposure).

The question for both is whether they're preparing for Cycle 2 now, or whether they'll be caught flat-footed the way Accenture was caught by Cycle 1.

## What This Means for Investors and Builders

If you're evaluating a company with a "regulatory moat," here's the framework:

**Ask: Which enforcement cycle does this moat solve?**
- Cycle 1 (transparency, licensing, capital requirements): Protects against deception enforcement and keeps out under-capitalized competitors
- Cycle 2 (unbundling, market share limits, non-exclusionary conduct): Protects against antitrust enforcement targeting dominance

Most companies only solve Cycle 1. That gives you 5-10 years of defensibility, then exposes you to Cycle 2 risk.

**Ask: What non-regulatory moat exists underneath?**
- Data lock-in (Salesforce CRM workflows)
- Switching costs (Razorpay settlement integration)
- Distribution advantages (PhonePe embedded insurance)
- Network effects (INFLUISH creator settlement layer, before regulatory barrier killed it)

If the only moat is regulatory, the durability is 5-10 years maximum. If there's a product moat layered underneath, the regulatory moat buys time to deepen the product moat.

**Ask: Is the company preparing for the next cycle?**
- Can they unbundle without losing revenue? (Salesforce test: can Agentforce be sold standalone, or does it only work bundled?)
- Can they operate at lower market share without losing economics? (Razorpay test: if CCI forces fair access to UPI rails for competitors, does Razorpay's margin hold?)
- Can they prove non-exclusionary conduct? (Both test: are contract terms the same for all merchant/customer sizes, or do they favor scale in ways that block competitors?)

If the answer is "we'll deal with that when it happens," you're holding a 5-10 year moat, not a durable one.

And if you're building a company, the lesson is this: **solve the current regulatory cycle, prepare for the next one, and build product lock-in that survives both.** Regulatory moats are real, but they're time-limited defenses, not permanent competitive advantages. The companies that survive are the ones treating regulatory defensibility as necessary but not sufficient, and layering it on top of product moats that last regardless of which enforcement priorities dominate.

Accenture learned this the expensive way. Salesforce and Razorpay have a few years to figure it out before Cycle 2 enforcement catches up to them.



## Sources & Further Reading

**Regulatory Framework & Enforcement:**
- FTC, "Rule on Unfair or Deceptive Fees," 16 CFR Part 464, effective May 12, 2025
- Freshfields, "2026 Enforcement Priority: Algorithmic Pricing," June 2026
- Paul Weiss, "Surveillance Pricing and Algorithmic Pricing — U.S. Regulatory Developments and Enforcement Actions," May 2026
- Holland & Knight, "Surveillance Pricing, AI Pricing Tools and the Push for Price Transparency," April 2026
- EU AI Act Official Text, 2024 (compliance timeline: August 2, 2026)
- Reserve Bank of India, "Payment Aggregators Directions, 2025-26" (RBI/DPSS/2025-26/141, September 15, 2025)

**Company Financials & Earnings:**
- Accenture Q3 FY2026 Earnings Release, June 18, 2026
- F1GMAT Premium, "Q1 2026 Consulting Trends: Outcome-Based Pricing & AI Agents"
- Salesforce Agentforce Pricing Documentation, 2026
- Turtlemint IPO DRHP, June 2026
- Economic Times, "Razorpay, Stripe, Pine Labs granted in-principle RBI approvals," July 2025

**Market Research & Analysis:**
- Futurum Group, "AI Platforms Decision Maker Survey Q1 2026" (n=838)
- Bessemer Venture Partners, "AI Pricing Playbook 2026"
- Parloa / Forbes, "Outcome-Based Pricing: The Most Expensive Myth In Enterprise AI," January 2026
- Zywave, "Four Forces Reshaping Insurance Distribution in 2026"
- FortuneIndia, "PhonePe vs Paytm: Decoding Profits and Valuation Supremacy," June 2026

**Antitrust & Legal Context:**
- Eastern Virginia U.S. District Court, "United States v. Google," Judge Leonie Brinkema ruling April 2025, enforcement order June 2026
- Bloomberg Law, "Major Tech Verdicts Serve to Check Industry as Regulation Stalls," June 2026
- New York State Department of State, "New York Algorithmic Pricing Disclosure Law," January 2026
- Maryland House Bill 618, "Protection from Predatory Pricing Act," 2026
- Competition Commission of India enforcement guidelines, Section 4 (Abuse of Dominance)

