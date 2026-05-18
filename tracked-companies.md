# Earnings Watch — Tracked Companies

The brief-generator agent checks this list against today's research and recent news.
When a tracked company reports earnings in the next 48 hours, the brief will flag it
with key metrics to watch.

---

## Big Tech / AI Infrastructure

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Microsoft | MSFT | Azure + OpenAI partnership, Copilot monetization | Azure growth rate, AI revenue breakout, capex |
| Alphabet / Google | GOOGL | Search + AI, cloud (GCP), DeepMind | Search revenue, GCP growth, YouTube ads |
| Amazon | AMZN | AWS + AI inference, e-commerce margin | AWS growth rate, operating margin, ad revenue |
| Meta | META | Ad platform, Llama / AI infra spend | Ad revenue per user, AI infra capex, Reality Labs loss |
| Apple | AAPL | Services margin, iPhone cycle, India manufacturing | Services revenue, gross margin |
| Nvidia | NVDA | GPU demand signal for entire AI buildout | Data center revenue, gross margin guidance |
| OpenAI | — | Private — track via news, funding rounds, Microsoft filings | ARR milestones, compute spend disclosures |

---

## Enterprise SaaS

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Salesforce | CRM | AI agent monetization, enterprise AI adoption | Revenue growth, operating margin, remaining performance obligations |
| Snowflake | SNOW | Data cloud, AI workload migration | Product revenue growth, net revenue retention |
| ServiceNow | NOW | Enterprise AI workflows | Subscription revenue, cRPO |
| Palantir | PLTR | AI + defense, commercial AI platform | US commercial revenue, government contracts |

---

## Fintech and Payments

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Visa | V | Card network health, cross-border volume | Payment volume, cross-border transactions |
| Stripe | — | Private — track via funding, blog posts, Collison interviews | Valuation, product announcements |
| Block | SQ | Cash App unit economics, Bitcoin strategy | Gross profit per active, Bitcoin holdings |
| PayPal | PYPL | BNPL, checkout button wars | Active accounts, take rate |

---

## Retail and Consumer

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Costco | COST | Membership model, private label | Membership fee revenue, same-store sales, traffic |
| Walmart | WMT | Flywheel: advertising + fulfillment + financial services | Advertising revenue, operating income |
| Shein | — | Private — track via regulatory filings, news | Market share, IPO news |

---

## India Tech Ecosystem

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Zomato / Eternal | ZOMATO.NS | Hyperpure B2B, quick commerce Blinkit | Blinkit GOV, adjusted EBITDA |
| Paytm / One97 | PAYTM.NS | Payments recovery, lending re-entry | GMV, loan disbursements |
| Jio Financial | JIOFIN.NS | Insurance, asset management, lending | AUM, revenue |

---

## Media and Distribution

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Netflix | NFLX | Ad tier economics, content spend ROI | Ad revenue, membership, ARM |
| Spotify | SPOT | Creator monetization, gross margin trajectory | Gross margin, MAU, premium subscribers |

---

## Industrials and Defense

| Company | Ticker | Why We Track | Key Metrics |
|---------|--------|--------------|-------------|
| Boeing | BA | Supply chain recovery, defense backlog | Deliveries, free cash flow |
| Anduril | — | Private defense tech — track via contracts, news | Contract wins, valuation rounds |

---

## How the Agent Uses This

When the brief-generator runs, it checks today's research for mentions of companies
on this list. If any company is reporting earnings within 48 hours (per search results
or research notes), it adds an EARNINGS WATCH section to the brief with:
- What the market is focused on
- The key number to watch
- Why it matters for the broader thesis

Add or remove companies by editing this file.
