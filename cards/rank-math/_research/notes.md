# Rank Math — Calling Card Dossier
*Built: 2026-05-06 | Card slug: rank-math | Card type: Job-application (audit + 4 workflows)*

---

## 1. The role

**Title:** Product Manager
**Company:** Rank Math (part of group.one)
**Compensation:** ₹26.95L – ₹37.73L
**Location:** Remote India ✓
**Required exp:** 5 years (Nihal at ~4y, gap to address honestly)
**Skills called out:** SEO, PM, SaaS, WordPress
**Source:** Wellfound

### Critical strategic angle
The JD says: *"AI isn't just a buzzword at Rank Math, it's core to our product strategy."* But the homepage says *"SEO for WordPress Made Easy"* with no AI in hero copy. The mismatch between hiring narrative and marketing narrative IS the audit's loudest finding and the natural place for an AI-PM to start.

---

## 2. Company snapshot

| Field | Detail |
|---|---|
| Domain | rankmath.com |
| Parent | group.one (€350M, 1,500+ employees, 55+ acquisitions) |
| Founded | 2020 |
| Active installs | "4 Million+" (homepage badge) |
| Headcount | 11-50 (Rank Math standalone) |
| Co-founders | Suraj Vibhute (CTO), Bhanu Ahluwalia, Nimit Kashyap |
| Hiring contact | Nabyasha Singh (HR Manager, Bengaluru) |
| Hero | "SEO for WordPress Made Easy" |
| Sub | "Rank Math is the most powerful way to get BEST SEO tools for WordPress added to your website." |
| Primary CTA | "DOWNLOAD FOR FREE" / "Try Demo Here" |
| Top nav | SEO Plugin / Content AI / Pricing / Tools / About / My Brands / My Account |

### Pricing (annual, auto-renew)
- PRO: $7.99/mo (renews $8.99 — bump pricing)
- BUSINESS: $24.99/mo (renews $27.99) — "Most Popular"
- AGENCY: $54.99/mo (renews $64.99)
- Content AI sold separately: Starter $5.99 / Creator $10.99 / Expert $16.99

### Product reality
- Billed like SaaS (subs, auto-renew, multi-site account at rankmath.com)
- Shipped like plugin (WordPress install, no standalone web-app)
- "Connect multiple websites" is a real differentiator but buried

### AI features (live)
- Content AI page exists at `/content-ai/` — "Write SEO articles in 1-click"
- 40+ AI tools (RankBot, llms.txt generator, AI search traffic tracker, image alt-text, bulk meta, etc.)
- AI is a secondary nav link — not surfaced in hero

### Competitive landscape
- Yoast SEO ~13M installs (legacy giant, ~61% market share)
- Rank Math 4M+ installs (per their badge), +300% growth since 2022
- Yoast bundles AI under "Generate / Optimize / Summarize" — clearer narrative
- Rank Math has the better AI product breadth, weaker AI marketing story

---

## 3. The 3 things already working

1. **4M+ active installs** is a real moat. Yoast is bigger but Rank Math is the credible #2 with the steepest growth trajectory in the space.
2. **Content AI breadth is genuinely impressive.** 40+ tools, llms.txt support, AI search traffic tracker. Most competitors don't have this depth. The product is ahead of the marketing.
3. **Billing infrastructure for the SaaS transition is already in place.** Annual subs, auto-renew, multi-site connection at rankmath.com. The pivot the JD describes is half-shipped.

---

## 4. The 10 audit findings (4-theme spine bespoke to a WordPress SEO plugin transitioning to SaaS)

### Theme A: The AI-promise gap (the loudest)

**Finding 01 — Hero promises "SEO Made Easy." JD promises AI is core. The two narratives don't meet on the homepage.**
- Hero verbatim: "SEO for WordPress Made Easy"
- AI doesn't appear above the fold on the homepage
- A buyer arriving at rankmath.com would not know AI exists unless they click the secondary "Content AI" nav link
- For an AI-PM hire reporting to the CTO, this is the highest-leverage thing to fix in week one
- Severity: Critical · 1 hr (hero copy + sub-headline rework)
- Shot: rank-math-home.png with hero highlighted

**Finding 02 — Content AI is a secondary nav link, not a hero pillar. 40+ AI tools live behind a click.**
- Top nav placement: SEO Plugin / **Content AI** / Pricing / Tools / About / My Brands / My Account
- Content AI's own page exists with strong hero: "Write SEO articles in 1-click"
- The product depth is real (40+ tools, llms.txt, AI search traffic tracker)
- But homepage real estate weights "SEO Plugin" over "Content AI" — backwards for 2026
- Severity: Critical · 4 hr (homepage feature surfacing + Content AI hero block)
- Shot: rank-math-home.png nav + rank-math-content-ai.png

**Finding 03 — No `/for-ai-search` landing page despite shipping llms.txt + AI search traffic tracker**
- The most defensible 2026 SEO positioning is "we make you findable in AI search (ChatGPT / Perplexity / Claude)"
- Rank Math actually ships the features (llms.txt generator, AI search traffic tracker)
- But there's no landing page for "AI search SEO"
- Yoast has this as a content angle. Rank Math has the product but not the page.
- Severity: High · 1 day (build the landing page, surface the features that already exist)
- Shot: compare-cell visual (existing /content-ai vs missing /ai-search)

### Theme B: Plugin-vs-SaaS identity confusion

**Finding 04 — Billed like SaaS, shipped like plugin. The marketing surface tells two different stories.**
- Pricing page: annual subs, auto-renew, multi-website plans
- Homepage: "DOWNLOAD FOR FREE" → WordPress plugin install
- No web-app dashboard screenshots, no multi-tenant browser shell
- The transition the JD describes is real (PM hire is to lead it) but invisible to a homepage visitor
- Severity: High · 1-2 weeks (web-app shell screenshots, "Manage all your sites at rankmath.com" hero block)
- Shot: rank-math-pricing.png (showing SaaS billing) + rank-math-home.png (showing WordPress plugin dashboard) compare

**Finding 05 — Product screenshot on homepage is a WordPress admin panel, not a SaaS web-app**
- Below-fold visual on the homepage is the in-WordPress dashboard interface
- Reads as "WordPress plugin first, web-app maybe later"
- For a buyer evaluating SaaS-shaped tools, this signals the wrong era
- Severity: High · 4 hr (replace with rankmath.com dashboard screenshot)
- Shot: rank-math-home.png with plugin-screenshot area highlighted

**Finding 06 — "Connect multiple websites" / centralized account is the real SaaS differentiator. Buried.**
- This is the actual reason a customer pays for Pro / Business / Agency tiers (not just for the plugin features but for the multi-site centralization)
- It's not surfaced on the homepage
- Should be a hero pillar
- Severity: High · 30 min (add the line + visual)
- Shot: compare-cell (current pricing language vs SaaS-forward framing)

### Theme C: Pricing friction

**Finding 07 — Renewal-bump pricing reads dark-pattern-adjacent**
- PRO: $7.99/mo first year, $8.99/mo on renewal (12.5% bump, mostly invisible until charged)
- Business: $24.99 → $27.99 (12% bump)
- Agency: $54.99 → $64.99 (18% bump)
- Either kill the bumps and price flat, or surface them transparently with rationale ("most users renew at year-2 price; here's why we're upfront")
- Severity: Medium · 30 min (transparency block) or Strategic · 4 hr (re-architect)
- Shot: rank-math-pricing.png with bump pricing highlighted

### Theme D: Founder voice + AI-PM thought leadership

**Finding 08 — Suraj Vibhute (CTO/co-founder) doesn't appear on the homepage**
- For a 4M+ user product, the founder is a real distribution asset
- Suraj has a LinkedIn profile but no homepage presence
- Founder-led marketing pulls AI-tooling buyers harder than logo-led marketing in 2026
- Severity: High · 30 min (founder block on homepage)
- Shot: rank-math-home.png with negative-space marked where founder block should sit

**Finding 09 — No public AI-PM thought leadership from the founder team. Yoast publishes this. Rank Math doesn't.**
- Yoast's CEO publishes regular AI-thinking content (LinkedIn, X, blog)
- Rank Math has the better AI product but a quieter founder voice
- For a category where the buyer is searching for "who's thinking ahead on SEO/GEO," silence loses
- Severity: Strategic · ongoing (founder content cadence)
- Shot: compare-cell (Yoast's CEO content frequency vs Rank Math's)

**Finding 10 — group.one parent listing dilutes Rank Math's standalone narrative**
- Top nav says "My Brands" — dropdown reveals group.one portfolio
- Either lean into the parent ("backed by group.one's €350M digital infrastructure, 1,500+ employees")
- Or hide it entirely and let Rank Math be its own story
- Half-on, where it appears in nav but isn't explained, is signal-noise
- Severity: Strategic · 1 hr
- Shot: rank-math-home.png with "My Brands" nav item highlighted

---

## 5. The 4 BESPOKE workflows (mapped to JD specifics)

### Workflow 01: GEO Trend Pulse
- **What it is:** daily monitor of Generative Engine Optimization trends. The JD literally says "SEO/GEO trends" — that pairing is unusual and signals they care about AI search SEO.
- Tracks: llms.txt adoption rate across the top 10K sites, ChatGPT/Perplexity/Claude search behaviors, citation share by domain, AI overview triggers in Google
- Output: Monday morning Slack digest for the PM. "Last week, llms.txt adoption hit 18% in tech-blog category. Citation share in Perplexity for 'best WordPress SEO' shifted: Yoast -3%, Rank Math +5%, Ahrefs +2%."
- Anchor metric: time from "AI search behavior shifts" to "Rank Math product response" — target same week, was 1-2 quarters
- **Stack:** SerpAPI + Perplexity API + custom llms.txt crawler → n8n → Postgres → Slack digest

### Workflow 02: Content AI Eval Loop
- **What it is:** evaluation framework for Content AI's output. Does the AI-generated article rank? Match brand voice across 4M+ users' range? Pass Google's helpful-content guidelines? Catch regressions before WP forum complaints.
- Per-launch: golden-set of 200+ test prompts → Claude scoring against rubric → ranking simulation against a corpus of 1M+ Rank Math user pages
- Output: weekly eval card showing pass/fail by dimension (helpfulness, factual accuracy, brand-voice match, ranking-likelihood). Catches drift the moment it starts.
- Anchor metric: time from "Content AI quality drift" to "PM visibility" — target same-day, was 2-4 weeks (until WP forum complaints surface)
- **Stack:** Claude/OpenAI eval suite → n8n → Linear ticket auto-generation → CI alert on regression

### Workflow 03: Plugin-to-SaaS Onboarding Instrumentation
- **What it is:** the JD specifically calls out "leading customer onboarding and experience improvements during our SaaS transition."
- Instruments the funnel: WordPress plugin install → first-time login at rankmath.com → connecting their first site → AI feature activation → first paid conversion
- Each transition moment gets A/B tested: which copy, which CTA placement, which feature surfacing converts best
- Output: a dashboard the PM looks at daily showing where users drop off in the plugin-to-SaaS handoff
- Anchor metric: % of plugin users who activate the rankmath.com dashboard within 7 days (target 30%, current likely <10%)
- **Stack:** Mixpanel / PostHog + n8n + Retool dashboard

### Workflow 04: WP Community Feedback Synthesizer
- **What it is:** Rank Math has WP.org reviews (~6,000), a support forum, in-product feedback, X mentions, Reddit /r/WordPress threads. This clusters all of that into a ranked monthly roadmap input.
- Tags by: theme (AI vs core SEO vs plugin reliability vs onboarding), user segment (free vs Pro vs Business vs Agency), AI-feature-vs-classic-SEO
- Output: a Notion page the PM opens before sprint planning. Top 3 themes per segment + the verbatim quotes that drove them
- Anchor metric: % of sprint roadmap that's grounded in clustered feedback vs founder intuition (target 60%+)
- **Stack:** WP.org scraper + Reddit API + Twitter / X search + Intercom → n8n + Claude clustering → Notion

---

## 6. Why Me

### Pillar 1: AI-native operator (the closest match to the JD's "AI is core" line)
- Sol8um.tech (Sept 2025–present, full-time AI-native founder) — paying clients in B2B SaaS automation. Currently building AI video tooling with a Bengaluru media client.
- Daily stack: Claude Code, Cursor, n8n, OpenAI, Whisper, LangChain, Apollo, Supabase, Vercel
- Gamezop (~1.5y PM): 72% qualified inbound lift, 250+ partner integrations automated through n8n flows I wrote, 50% workforce automation

### Pillar 2: PM credibility despite the year-of-experience gap
- Honest acknowledgment: 4+ years PM, JD says 5
- What I bring underneath the gap: AI-tooling depth that most 5-year PMs don't have, ship velocity (this card built in 6 hours), and operator experience as a founder (sol8um.tech has paying clients)
- Frame: "the missing year of title is a poor proxy for the AI-PM bench you're actually trying to fill"

### Industry overlap (4 cells, mapped to Rank Math's domain)
1. **Sol8um.tech** — current AI-tooling work, exact stack match for Content AI Eval, GEO Trend Pulse
2. **Gamezop** — 250+ partner integrations automated, 72% lead lift. Same demand-engine instrumentation muscle the SaaS transition needs.
3. **Kredily** — 800K users, 127% revenue growth, free-to-paid PLG. Direct overlap with Rank Math's plugin-to-SaaS conversion funnel.
4. **The Smart Traveller** — bootstrapped founder velocity. Matches Rank Math's "small, passionate, fully remote team."

---

## 7. Validation rules specific to this card

- No em dashes
- No feelback.fun anywhere
- SCIVO mentioned exactly once, low-key, in why-me Pillar 1
- No comparison framing (no Runway / HeyGen / Higgsfield / Flow Labs)
- No mention of Cielo / SciSpace / Ventracle / Social Capital / REWORK / Klarité / Kiana / Saikiran / Vedika / Anslem
- No Cielo workflow names (Morning Brief / Email Triage / Pre-Meeting / Reflection)
- Phone +91 9468688354 (calling-card phone)
- Card lives at `https://sol8um-calling-cards.vercel.app/rank-math/`
- Audit MUST have real `.shot-frame` blocks on findings 01, 02, 04, 05, 07, 08, 10 (the ones where homepage / content-ai / pricing screenshots support the evidence)
- Findings 03, 06, 09 use compare-cell visual evidence (no screenshot fits the conceptual gap they describe)
- Day-arc / timing visualization uses the Gantt pattern, not a single-axis SVG
