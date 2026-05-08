# WOWCube — Calling Card Dossier
*Built: 2026-05-09 | Card slug: wowcube | Card type: Job-application (audit + 4 workflows)*

---

## 1. The role

**Title:** Product Manager: E-Commerce & CRO
**Company:** Cubios Inc. / WOWCUBE™
**Comp:** $50-60K USD, contract, no equity
**Remote:** Everywhere ✓
**Required exp:** 2 years (Nihal at 4+, exceeds)
**Timezone:** CET 09:00-18:00 = 12:30pm-9:30pm IST (comfortable overlap)
**Reports to:** CMO
**Hiring contact:** Alina Shyriaieva (HR, Kyiv)
**Source:** Wellfound

**Key tools called out:** Shopify, Convert.com, Smartlook, A/B testing
**Key responsibilities:** website + e-commerce as a product, CJM, CRO, experimentation, roadmap

---

## 2. Company snapshot

| Field | Detail |
|---|---|
| Marketing domain | wowcube.com (Shopify-hosted) |
| Checkout domain | shop.wowcube.com (split funnel — CRO finding) |
| HQ | Sarasota / Novato |
| Founded | 2017 (per Crunchbase) |
| Funded | $6.4M raised, Series A $4.5M Aug 2021 |
| Headcount | 51-200 |
| Founders | Max Filin (CEO, Florida), Semyon Orlov (Chief Engineer), Ilya Osipov (CTO, San Francisco) |
| Hero | "The World's First Gaming Console in a Cube" |
| Sub | "Play with your hands. Grow your mind." |
| Primary CTAs | "Get WOWCube" / "See how it works" |
| Above-fold price | NONE. "From $399" only in footer CTA. |

### Product
- Modular cube, 24 screens, motion sensors
- Hardware + embedded software + own OS + system apps
- Flagship SKU: Rubik's® WOWCube® (Spin Master partnership relaunch July 2025)
- PDP price: **$499** standalone, Bundle $598 → $439, Ultimate Bundle $648 → $499

### Press logos (decorative on homepage)
Forbes, BBC, Yahoo, ABC News, NEW ATLAS, CNET, GIZMODO

### Public sentiment (CRITICAL for audit framing)
- **Hardware praised:** CES 2021, Edison, Red Dot, Time
- **Software/QC/support criticized:** Reddit r/Cubers calls out "SUPER glitchy, hard to turn, hard to charge," "Worst customer service ever"
- CGMag review: "Hardware gets a 10, but the software needs work"
- The #1 buyer objection in the wild = software stability fear
- Site addresses this objection ZERO times

**Implication for audit:** lead with trust-repair + proof-of-quality, NOT generic copy fixes. A buyer arrives with software-stability concerns from the category's discourse. The audit should help WOWCube defuse that objection on-site, not pretend it doesn't exist.

---

## 3. The 3 things already working

1. **Hardware reputation is genuinely strong.** Press loves it. The product itself is real and well-engineered.
2. **The Spin Master / Rubik's partnership (July 2025 relaunch)** is real category leverage. Few hardware startups land an IP this iconic.
3. **The category claim** ("World's First Gaming Console in a Cube") is unique and defensible. Not Steam Deck, not Playdate, not Nintendo. New category, owned.

---

## 4. The 10 audit findings (4-theme spine bespoke to a $499 hardware SKU with mixed software sentiment)

### Theme A: Trust repair and proof-of-quality (the loudest gap)

**Finding 01 — No reviews widget on the PDP. $499 hardware, zero star count, zero verified-purchase snippets.**
- shop.wowcube.com/products/wowcube-rubiks shows: title, price, "Add to cart," "Buy it now," "Reliable shipping," "Flexible returns." That's it.
- For a $499 SKU with mixed public sentiment, the absence of reviews is the single highest-leverage conversion gap.
- Severity: Critical · 1 day to integrate Yotpo/Judge.me/Stamped
- Shot: wowcube-pdp.png with PDP highlighted, callout where reviews should sit

**Finding 02 — No software-stability or firmware-update transparency anywhere on the buy flow.**
- The #1 buyer objection from Reddit/CGMag is software glitches.
- Site addresses it zero times. No firmware-update cadence shown, no roadmap, no warranty terms surfaced on PDP.
- A "your cube gets better every month with firmware updates" badge directly defuses the buyer's pre-existing objection.
- Severity: Critical · 4 hr to draft + add badge + link to changelog
- Shot: wowcube-pdp.png showing clean PDP without quality-trust elements

**Finding 03 — No third-party trust signal anywhere.**
- No Trustpilot embed, no Google Reviews score, no BBB, no return-rate stat.
- Press logos exist (Forbes, BBC, Yahoo, etc.) but are decorative, not clickable to the actual coverage.
- Severity: High · 2 hr to make press logos clickable + add Trustpilot widget if score warrants
- Shot: wowcube-home.png with press logo strip highlighted

### Theme B: Funnel hygiene (the subdomain hop is the loudest single conversion leak)

**Finding 04 — Subdomain hop mid-funnel: wowcube.com → shop.wowcube.com.**
- Marketing site is wowcube.com. Buy CTAs route to shop.wowcube.com/products/wowcube-rubiks. That's a different subdomain.
- Cart cookie scope, Convert.com test scope, GA stitching, and Smartlook session continuity all break across subdomains unless explicitly configured (and most Shopify defaults don't).
- The PM hired into this role would need to verify cross-domain tracking is intact OR consolidate to a single domain.
- Severity: Critical · 1 day to audit cross-domain config; up to 2 weeks to consolidate
- Shot: visual flow diagram showing the hop (compare-cell)

**Finding 05 — Generic shipping/returns language on PDP: "Reliable shipping" / "Flexible returns".**
- No ship time. No return window. No policy details. The PDP says nothing concrete.
- Specifics like "Ships in 3-5 days, 30-day returns, free return shipping" measurably lift conversion.
- Severity: High · 30 min to update the PDP copy
- Shot: wowcube-pdp.png with the generic policy lines highlighted

**Finding 06 — International duties hidden until checkout.**
- Return policy buried: "Duties, taxes, brokerage, and other import fees are the responsibility of the customer."
- For a global D2C product priced at $499, international buyers find this out at the worst possible moment (checkout).
- Pre-cart disclosure is a known abandonment fix. DDP-style "all-in pricing" is the gold standard.
- Severity: Strategic · 1 day to surface; 1-2 weeks to integrate DDP
- Shot: compare-cell showing current hidden vs proposed surfaced

### Theme C: Pricing presentation and financing (the $499 friction)

**Finding 07 — No financing on a $499 SKU. Affirm / Klarna / Shop Pay Installments missing.**
- 1-line Shopify integrations. Standard for hardware in this price band.
- Playdate ($200), Steam Deck ($400+), Quest ($500+) all offer financing at checkout. WOWCube doesn't.
- Severity: High · 1 day to enable on Shopify
- Shot: wowcube-pdp.png with checkout area highlighted, "no financing options visible" callout

**Finding 08 — Bundle merchandising broken: standalone $499 vs Ultimate Bundle $499 (was $648).**
- Same price, drastically different value, no visual comparison logic on PDP.
- Buyer who notices feels rewarded; buyer who doesn't picks the worse-value option.
- Severity: Critical · 4 hr to add bundle comparison block on PDP
- Shot: compare-cell showing current confusing pricing vs proposed merchandising

**Finding 09 — No price above the fold on homepage.**
- Hero says "Get WOWCube." Price ($399 floor, $499 flagship) appears only in footer CTA.
- For a hardware product at this price band, hiding the price drives bounces from price-sensitive buyers and surprise-bounces from buyers who arrive expecting a $99 toy.
- Severity: Strategic · 30 min (or A/B test the placement)
- Shot: wowcube-home.png with hero highlighted, "no price" callout

### Theme D: Capture infrastructure (visitors who don't buy on visit 1 are gone)

**Finding 10 — No exit-intent recovery, no cart-abandonment email capture, no first-order discount hook.**
- Newsletter capture is footer-only ("Get exclusive deals and early access").
- For a $499 considered-purchase SKU, most buyers don't convert on visit 1. Without email capture, they're gone unless they remember the brand.
- Klaviyo + Shopify is the standard stack here. 30-min setup; immediate revenue lift.
- Severity: Compounding · 1 day
- Shot: wowcube-home.png footer area + compare-cell of suggested pop-up

---

## 5. The 4 BESPOKE workflows (mapped 1:1 to JD responsibilities)

### Workflow 01: CRO Experiment Engine
- Convert.com + Shopify + Smartlook orchestration
- Each experiment lifecycle: hypothesis from Smartlook session-recording analysis → variant build → split-test config → significance gating → ship-or-kill decision → learnings log
- The PM opens the engine on Monday, sees what's running, what's reached significance, what shipped last week
- Anchor metric: experiments shipped per quarter (target 10-15) + win rate (target 25%+)
- Maps to JD: "Experiments, A/B Testing, and Iteration"

### Workflow 02: Customer Journey Instrumentation (cross-domain)
- Solves Finding 04 directly
- Cross-domain analytics + Smartlook + Shopify event mapping → funnel-as-live-data dashboard
- Tracked transitions: wowcube.com landing → /buy click → shop.wowcube.com PDP → cart → checkout → purchase
- Each transition has a measured rate, an A/B slot, an alert on regression
- Anchor metric: % of marketing-site visitors who land at the PDP (current likely 30-40%, target 60%+)
- Maps to JD: "Customer Journey and Conversion Logic"

### Workflow 03: Proof-of-Quality Surfacing System
- For Theme A (the trust repair theme)
- Reviews aggregator (Yotpo + YouTube comments + Reddit mentions) → tagged by hardware/software/support → surfaced on PDP with verified-purchase filter
- Software-update timeline / firmware changelog block on PDP, auto-pulled from internal release notes
- Returns transparency: live "X days average ship time, Y% return rate, Z-day refund processing" stat block
- Anchor metric: Theme A finding closure (4 of 4 concrete proof artifacts surfaced on PDP within 30 days)
- Maps to JD: e-commerce product ownership + "Make decisions based on data, not opinions"

### Workflow 04: Bundle and Upsell Intelligence
- Solves Finding 08 directly
- Smart bundle comparison on PDP (visual: standalone vs bundle, savings highlighted, "most picked" badge)
- Cart-time upsell of the Extra Dock ($29) — known high-attach-rate accessory
- Post-purchase 7-day cross-sell email of game packs / firmware-paid upgrades / accessories
- Anchor metric: AOV lift (target +15-25%) + bundle attach rate
- Maps to JD: "pricing presentation, bundles, promos, and upsell logic"

These four are NOT Cielo's, SciSpace's, Ventracle's, Social Capital's, REWORK's, or Rank Math's. Reasoned from a Shopify-hosted $499 hardware SKU with a CRO-focused PM hire.

---

## 6. Why Me

### Pillar 1: AI-native operator with e-commerce funnel chops
- Sol8um.tech (Sept 2025–present, full-time AI-native founder) — paying clients in B2B SaaS automation. Currently building AI video tooling with a Bengaluru media client.
- Daily stack overlaps with the role: Claude, n8n, Shopify (for sol8um clients), GA4, Mixpanel, OpenAI
- Kredily APM (~7mo): 54% sign-up funnel recovery, 127% revenue growth on PLG. Same conversion mechanics that lift WOWCube's PDP-to-paid funnel.
- Gamezop PM (~1.5y): demand-side automation, n8n flows, 72% qualified inbound lift, 250+ integrations automated. Shows the experimentation + system-thinking muscle the JD asks for.

### Pillar 2: The card itself is velocity proof
- Built in 6 hours. Solo. End-to-end. Custom domain. Deployable.
- Same Shopify + Convert.com + Smartlook stack the role lives on, demonstrated through the audit's depth.
- Most CRO PM applicants send a resume PDF. This applicant sent a working CRO audit on the actual site.

### Industry overlap (4 cells, mapped to WOWCube's domain)
1. **Sol8um.tech** — current AI-tooling work for clients including content automation (Matrix Academy: 55K → 75K IG followers via reel-package automation, Dec '25-Jan '26)
2. **Kredily** — 800K users, 127% revenue growth, free-to-paid PLG funnel surgery. Same conversion-flow muscle.
3. **The Smart Traveller** (co-founded) — bootstrapped D2C, ₹11L GMV in 4 months, 20K+ travelers. Direct B2C ownership experience.
4. **Gamezop** — n8n / experimentation / instrumented funnel at scale. The "system thinking" the JD calls out.

---

## 7. Validation rules specific to this card

- No em dashes
- No feelback.fun anywhere
- SCIVO mentioned exactly once, low-key, in why-me Pillar 1
- No comparison framing (no Runway / HeyGen / etc.)
- No mention of Cielo / SciSpace / Ventracle / Social Capital / REWORK / Rank Math / Klarité / Kiana / Saikiran / Vedika / Anslem / Suraj
- No Cielo workflow names (Morning Brief / Email Triage / Pre-Meeting / Reflection)
- Phone +91 9468688354 (calling-card phone)
- Card lives at `https://sol8um-calling-cards.vercel.app/wowcube/`
- Audit MUST have real `.shot-frame` blocks on findings 01, 02, 03, 05, 07, 09, 10 (the visual-evidence ones); findings 04, 06, 08 use compare-cell visual evidence
- Don't quote Reddit reviewers in the audit. Frame Theme A as "buyer arrives with software-stability concerns from the category" — implicit not explicit
- Trust-repair-not-copy-tweak is the audit's thesis
