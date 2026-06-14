---
type: podcast-script
date: 2026-06-08
based_on: 2026-06-08-measurement-moats.md
estimated_duration: 23 minutes
word_count: 3,220
---

# Episode: The Measurement Moat

## COLD OPEN

Atlassian's revenue grew 21% last quarter. [pause] But for the first time in company history, the number of people paying for Jira and Confluence went down. [pause] Revenue up. Customer count down. The link between "people using software" and "software value delivered" just snapped. [pause] Meanwhile, Eli Lilly beat a competitor with a five-year head start and a 70% price cut. And a chip company called Rambus tripled their operating income in two years, but analysts are giving them 15 months before it all evaporates. [pause] Today we're going to talk about why some competitive advantages last three to seven years and others die in 18 months.

---

## INTRODUCTION

I'm Prashant. This is Thinking in Strategies. Every week I take one business or strategy story and try to actually explain what's going on beneath the surface.

This week's question: if every competitive advantage is temporary, how long does yours actually last? Because they don't all break at the same speed. And if you're building a company or investing in one, knowing the difference between a moat that lasts 18 months and one that lasts seven years is the entire game.

---

## ACT 1 — CONTEXT

So here's where we are. For the last twenty years, software companies have charged per seat. You want Slack for 100 employees? That's 100 seats times $15 a month. More people equals more revenue. Growth meant adding seats. The math was simple.

That model just broke.

Atlassian's Q1 2026 numbers tell the story. Revenue climbed 21% year over year. But for the first time ever, seat count declined. Fewer people were paying for Jira and Confluence, yet the company was making more money.

What changed? Automation. AI tools eliminated the need for some team members while making the remaining users dramatically more productive. A team that used to need 10 people to manage a project now needs 6. But those 6 are shipping more work than the original 10 ever did.

The software is delivering more value. Projects completed, bugs resolved, features shipped. All up. But the old metric, seats purchased, no longer captures that value.

And this creates a problem. Companies that stick to per seat pricing are either leaving money on the table or pricing themselves out of markets where automation is shrinking headcount.

Slack raised their price from $20 to $45 per user this year. A 125% increase. They're calling it the "AI tax." They're trying to capture more revenue from each seat because they know seat counts are going to compress.

But here's the problem. Slack can't actually measure whether teams using their product are more productive. Team collaboration and communication quality are fundamentally unmeasurable. You can count messages sent or meetings scheduled, but you can't prove Slack made your team 20% more productive. Without measurement, there's no defensible premium.

Contrast that with Zendesk. At their conference this year, they announced outcome based pricing. Customers pay per verified resolution. That's a customer support ticket that's confirmed resolved 72 hours later. Not per seat. Not per ticket opened. Per actual problem solved.

That's measurable. Zendesk can prove they resolved your customer's issue. They can benchmark their resolution rate against competitors. If they're better at solving problems, they can charge more and defend that premium with data.

So here's the setup. The old model, per seat pricing, is dying. The new model is outcome based pricing. But that only works if you can measure the outcome. And that creates a divide. Companies in categories where results are measurable versus companies in categories where they're not.

---

## ACT 2 — THE ARGUMENT

This week I tracked five different competitive moats across SaaS, infrastructure, pharmaceuticals, and fintech. All of them are temporary. But they expire on wildly different schedules. And the pattern is surprisingly consistent.

Infrastructure moats last 12 to 18 months.

Let me give you an example. Rambus makes memory interface controllers. These are the chips that connect high bandwidth memory to processors in AI servers. They had a near monopoly. Operating income tripled in two years. $91.5 million in 2023 to $260.2 million in 2025. Gross margins hit 80%.

The moat was simple. AI chips needed faster memory. High bandwidth memory, called HBM, was in short supply. And Rambus owned the interface design most chip makers used. You literally couldn't build an AI chip without licensing their technology.

But moats built on scarcity evaporate when supply normalizes. HBM production is ramping up. Supply should normalize by end of 2026, not 2028 like earlier forecasts predicted. And Marvell just shipped an alternative interface design that's 70% more power efficient. Broadcom, Google, and Amazon are already using it in their custom chip designs.

[pause]

Rambus's moat window: 15 months from peak margins to competitive parity.

Infrastructure advantages compress fast because once a better design exists, hyperscalers with the resources to switch will switch. There's no lock in beyond the time it takes to redesign your chip. And these companies redesign chips every 12 to 18 months anyway.

So that's what's happening in infrastructure. Here's why it matters for everything else.

Measurement moats last three to seven years. And this is the part that I think most people miss.

Eli Lilly launched tirzepatide in 2022. It's sold as Mounjaro for diabetes, Zepbound for weight loss. They launched five years after Novo Nordisk's semaglutide, which is Ozempic and Wegovy. Novo had every advantage. Five year head start. Brand recognition. Established supply chains. And they dropped prices 70% to defend market share.

Lilly captured 51% of the combined GLP-1 market by April 2026.

[pause]

How? Measurement. Lilly's drug causes 22.5% average weight loss in clinical trials. Novo's causes 15 to 17%. Lilly didn't beat them on price, brand, or distribution. They beat them on outcomes. And they could prove it with data.

This is a measurement moat. When your product delivers measurably better results, you can charge a premium and customers will pay it because you have proof. Novo dropped prices 70% and still lost market share because efficacy matters more than cost when the difference is 22.5% versus 15% weight loss.

But measurement moats expire too. Lilly's advantage holds until one of three things happens. A competitor publishes equivalent or better weight loss data. Generic versions of tirzepatide get regulatory approval, likely 2028 to 2030. Or regulation forces Lilly to license manufacturing or share data to improve access.

Lilly's patents technically run until 2035, 2036. But regulatory approval pathways for biosimilars and international pricing pressure compress the real moat to three to five years of peak margins. After that, they'll still sell the drug. Just at lower prices and smaller market share.

Three to seven years is dramatically longer than 12 to 18 months. That's the difference between infrastructure moats and measurement moats. Infrastructure advantages break when someone builds a better design. Measurement advantages break when someone proves equivalent outcomes. Which requires years of clinical data, regulatory approval, and real world validation.

Now here's where it gets genuinely interesting.

Distribution advantages last indefinitely. But only with measurement parity.

OpenAI shipped Codex in April 2026. It's a native GPT coding agent that competes directly with Cognition's Devin. Codex hit 3 million weekly active users within two months. Devin has 80,000.

OpenAI's distribution advantage is 40x. They should have crushed Cognition. They didn't. Devin's user count stayed flat. 80,000 to 90,000 from April to June. Developers who had already adopted Devin didn't switch to Codex, even though it was free for OpenAI subscribers and integrated directly into ChatGPT.

Why? Switching costs. Once a team embeds Devin into their development workflow, connects it to their CI/CD pipeline, trains it on their codebase, builds measurement baselines for code quality and review time, switching to a new tool means redoing all of that work. Even if Codex is marginally better, the switching cost exceeds the benefit.

This looks like a process lock in moat. But it's not. It's a measurement moat.

[slower] Developers stick with Devin because they have data showing it works for their specific use case. They've measured how long code reviews take before and after Devin. They know their bug rates. They've quantified the productivity gain. Switching to Codex means losing that measurement baseline and starting over.

But here's the problem. OpenAI's 3 million users are accumulating measurement data 40 times faster than Cognition's 80,000 users. After 18 to 24 months, OpenAI will have statistical power, enough real world data, to prove Codex delivers equivalent or better outcomes than Devin across a wide range of use cases. At that point, the measurement moat collapses. New customers will choose Codex because it has better distribution, integrated into ChatGPT, and equivalent proven outcomes.

Cognition's moat compresses from three to seven years defensible to 18 to 24 months before OpenAI catches up.

This is the pattern. Distribution lasts indefinitely, but you need measurement parity to convert distribution into market share. OpenAI has distribution now. They'll have measurement parity in 18 to 24 months. After that, Cognition's only defense is locking in customers with long term contracts or moving to a new moat before OpenAI's measurement catches up.

And this brings us to the implication. The SaaS market is splitting into two groups. Companies in categories where outcomes are measurable, and companies in categories where outcomes are not.

Measurable categories survive three to seven years. Customer support. Zendesk can measure resolution rates, time to resolution, customer satisfaction scores. They can prove their AI agents resolve tickets better or faster than competitors. That's defensible until competitors measure equally well, which takes three to five years of data accumulation and product iteration.

Credit underwriting. Cashfree in India hit 1,000 crore rupees in revenue and EBITDA profitability in March 2026. That's about $120 million in revenue. They can prove their underwriting models have lower default rates than competitors. That measurement moat lasts until competitors collect equivalent loan performance data and tune their models to match.

Code quality and review time. Cognition's Devin survives against OpenAI's Codex because existing users have measurement baselines proving it works. That lasts 18 to 24 months until OpenAI's larger user base generates equivalent data.

Unmeasurable categories commoditize in 18 to 24 months. Team collaboration. Slack. Productivity, communication quality, team cohesion. Fundamentally unmeasurable. You can count messages sent or meetings scheduled, but you can't prove Slack made your team 20% more productive. Without measurement, there's no defensible premium. Slack's 125% price increase is unsupported by data. Customers will switch to cheaper alternatives like Teams, which is bundled free with Office 365, unless Slack has lock in from integrations or workflows.

Project management. Atlassian's Jira. Project velocity, team efficiency, planning accuracy. Hard to measure in isolation. Jira can show you how many tickets closed, but it can't prove your team shipped projects faster because of Jira versus because they hired better engineers or simplified the product roadmap. Without clear attribution, Atlassian's pricing power depends on switching costs, recreating workflows, retraining teams, not proven outcomes.

[pause]

This is the bifurcation. Measurable category SaaS companies can charge premium pricing and defend it with data for three to seven years. Unmeasurable category SaaS companies either commoditize, race to the bottom on price, or survive on lock in, switching costs exceed the benefit of moving to a cheaper alternative.

---

## ACT 3 — COUNTERARGUMENT

Now, the pushback I'd expect here is this. You're saying measurement moats last three to seven years, but what about brands? Apple charges a premium not because they can prove iPhones make you more productive. They charge a premium because people trust the brand. Same with Nike, same with luxury goods. Measurement doesn't explain everything.

And honestly, it's a fair point. Brand moats exist. They can last decades. But here's why I still think the measurement framework holds for most B2B software and enterprise markets.

Brand works when the buyer is also the user and the decision is emotional or identity driven. You buy an iPhone because it signals something about you. You buy Nike because you identify with what the brand represents.

But in B2B software, the buyer is almost never the user. A CTO buying Zendesk for customer support isn't using Zendesk themselves. They're buying it for their support team. And when you're not the user, emotional attachment to the brand doesn't work the same way. What works is proof. Data showing the product delivers ROI. Measurement.

Brand still matters in B2B, but it's a trust accelerator, not a moat. It helps you close the first deal faster. But it doesn't let you charge 2x more than a competitor unless you also have data proving better outcomes.

So yes, brand moats exist. But in the markets I'm tracking, SaaS, enterprise software, fintech, the defensible moats are measurement based, not brand based.

---

## TAKEAWAY

If you take three things from today:

One. Every competitive advantage is temporary, but they break on different schedules. Infrastructure moats last 12 to 18 months. Measurement moats last three to seven years. Distribution advantages last indefinitely, but only if you also build measurement parity.

Two. The SaaS market is bifurcating. Companies in categories where outcomes are measurable, customer support, credit underwriting, code quality, can charge premium pricing and defend it with data for three to seven years. Companies in unmeasurable categories, team collaboration, project management, will commoditize or survive only on switching costs.

Three. The next evolution might be outcome guarantees. Vendors taking contractual liability if customers don't hit promised results. ServiceNow is testing this now. If it works, it's a five to ten year moat. If it doesn't, it proves outcome guarantees collapse under real world complexity. We'll know in the next 18 to 24 months.

---

## CLOSE

That's it for this week. If you want to go deeper, the full written piece is at prashant-chandel.org/blog. There's an infographic there that maps out the whole hierarchy of moat durability visually.

If this was useful, share it with one person who'd appreciate it. That's the best way to help the show grow.

See you next Sunday.
