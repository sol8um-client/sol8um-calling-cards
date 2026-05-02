# Bespoke Workflows for SciSpace

## Role's daily reality (one sentence)

The Product Owner at SciSpace runs the quality and roadmap loop for the AI Research Agent used by 1M+ researchers — maintaining LLM eval baselines so Agent responses don't silently regress, synthesizing a high-volume feedback stream from PhD candidates and lab PIs into ranked roadmap moves, and preparing evidence-backed sprint inputs before each engineering cycle, all while tracking OpenAI Research Mode for moves that could redefine the category overnight.

---

## Four workflow specs

### Workflow 01 — Researcher Feedback Synthesizer

- **When it fires:** Continuous ingestion (live); daily digest published at 08:30 IST
- **Inputs:** Intercom support tickets + G2 / Capterra / Chrome Web Store reviews (300K user base) + Mixpanel in-app feedback events + App Store mobile reviews + any direct email threads forwarded to a monitored inbox
- **Processing:** NLP clustering groups all incoming signal into themes (citation accuracy, Agent credit confusion, UI friction, missing tool X, model quality complaints). Each theme is scored by frequency x recency x ICP segment (PhD candidate vs. postdoc vs. lab PI vs. industry researcher). Delta vs. prior 7 days is flagged. Top 3 new or rising themes are surfaced with 2-3 verbatim evidence quotes per theme. A "rising fast" alert fires if a new theme crosses a volume threshold mid-day. Weekly rollup writes candidate issues into Linear, tagged by theme and ICP segment.
- **Outputs:** Daily Slack digest in a dedicated #agent-feedback channel: 3 ranked themes with evidence, 1 "rising fast" alert (if triggered), links to raw clusters in Notion. Weekly: Linear tickets pre-populated with theme summary + representative quotes, ready for sprint prioritization.
- **Replaces:** 2-3 hours/day manually reading Intercom tickets and app store reviews; the failure mode of roadmap decisions made without real user signal from the actual ICP (not just the loudest users in the support queue)
- **Anchor metric:** Median time from feedback event to Linear ticket — target: same-day (was: 5+ days untracked)
- **Archetype:** continuous (with daily digest output)

---

### Workflow 02 — Agent Eval Regression Pulse

- **When it fires:** Daily at 09:00 IST, immediately after nightly eval suite completes
- **Inputs:** Nightly automated eval test suite output (citation accuracy, hallucination rate, synthesis coherence scores — run via n8n or LangSmith eval harness against a frozen benchmark set of 200+ researcher queries) + 7-day rolling baseline per eval dimension + yesterday's live Agent session logs (sampled) + model version / prompt version changelog
- **Processing:** Compares last night's eval scores against the 7-day rolling baseline per dimension. Flags any regression above 5% threshold. Clusters failing cases by query type (literature review vs. manuscript draft vs. grant workflow vs. citation generation) and by researcher segment. If a model version or prompt version changed in the last 24 hours, labels regression as "likely model-caused" vs. "likely prompt-caused" vs. "unexplained." Generates a 3-case failure sample for any regressed dimension with actual response vs. expected response diff.
- **Outputs:** Slack alert to PM + engineering channel: color-coded status card (green / amber / red) per eval dimension, 3 failing case examples with diffs, recommended triage owner (prompt engineer vs. backend vs. model config team). If all green, sends a single confirmation message. Persists to a Notion eval log for trend tracking.
- **Replaces:** Manual spot-checking of Agent outputs (sporadic, incomplete, dependent on individual PM attention); the failure mode of shipping a citation accuracy regression to 1M researchers before any internal signal fires
- **Anchor metric:** Mean time to detect a regression from deployment — target: under 12 hours
- **Archetype:** daily-cron

---

### Workflow 03 — Sprint Readiness Dossier

- **When it fires:** T-60 minutes before each sprint planning session (calendar event trigger — detects any event titled containing "sprint planning" or "sprint kickoff")
- **Inputs:** Last sprint's eval regression log (final status per dimension) + Researcher Feedback Synthesizer's top themes from the last 14 days + Linear backlog (open bugs + feature requests sorted by vote count + severity label) + competitor release notes (Elicit changelog, Consensus blog, OpenAI research announcements, Paperpal release notes — monitored via RSS) + Agent credits consumption data by tool category (which of the 150+ tools consumed most credits in the prior sprint period)
- **Processing:** Synthesizes eval trend direction (improving / degrading / stable) per dimension. Maps the top 3 feedback themes to existing open Linear tickets (or flags as untracked). Surfaces any competitor move in the last 14 days that touches Agent functionality. Scores open Linear items by impact estimate (feedback volume x eval severity x credits consumption signal) and generates a ranked "top 5 sprint candidates" list with one-line rationale per item. Drafts 3 open questions for the engineering discussion where data is ambiguous.
- **Outputs:** Notion page auto-created and linked in the calendar invite 60 minutes before the meeting: eval trend summary, feedback-to-ticket map, competitor alert section (populated or "no material moves"), 5 ranked sprint candidates with rationale, 3 open questions. Persists as a sprint artifact for future retrospectives.
- **Replaces:** 45-60 minutes of pre-sprint manual synthesis; the failure mode of arriving at sprint planning without a shared evidence base, causing priority decisions to default to whoever argues most forcefully rather than what the data shows
- **Anchor metric:** Percentage of sprint decisions traceable to a cited data source in the dossier — target: above 80%
- **Archetype:** event-triggered

---

### Workflow 04 — Agent Cohort Activation Gap

- **When it fires:** Weekly, Friday at 17:00 IST
- **Inputs:** Mixpanel cohort data (Premium subscribers segmented by researcher type: PhD candidate, postdoc, lab PI, industry researcher, journalist/policy researcher) + Agent credits consumption logs (who purchased credits, which tools they ran, depth of usage — single task vs. full pipeline) + conversion events (free-to-Premium, Premium-to-credits purchase) + silent churn events (credits purchased, never consumed within 7 days) + post-session micro-survey responses (NPS / "did the Agent answer your question?" binary prompt)
- **Processing:** Segments all Premium users by Agent activation stage: never launched Agent / launched but no credits / purchased credits once / regular credits user / power pipeline user. Calculates activation rate per cohort and week-on-week delta per segment. Identifies the highest drop-off cohort (largest volume at a given stage who did not advance). Compares tool usage patterns and query types of activated vs. non-activated users within the same segment. Surfaces 1 "bright spot" cohort (activation improving fastest, with usage pattern evidence) and 1 "at-risk" cohort (credits purchased but not consumed, with proposed intervention hypothesis). Generates 2 experiment hypotheses targeting the gap.
- **Outputs:** Friday Slack post in #agent-metrics + a Notion weekly report with the activation funnel by segment (visual), the bright spot cohort story, the at-risk cohort story, 2 experiment hypotheses with proposed success metrics for next week.
- **Replaces:** 1.5 hours of manual Mixpanel cohort queries each Friday; the failure mode of optimizing for total Agent usage volume while missing the specific segment that purchases credits, fails to activate on a real workflow, and silently churns — the exact churn pattern that compounds quietly before showing up in revenue
- **Anchor metric:** Agent activation rate among Premium subscribers — baseline to target: lift to above 25% weekly active on Agent by Q2 (from current unmeasured baseline)
- **Archetype:** weekly-reflective

---

## Day-arc layout (for the SVG)

```
Workflow 01 (Researcher Feedback Synthesizer):
  - Trigger: continuous + 08:30 digest
  - Color: #4A90D9 (medium blue — steady, always-on)
  - Label: "Feedback Pulse"
  - Position: spans full day bar, digest dot at 08:30

Workflow 02 (Agent Eval Regression Pulse):
  - Trigger: 09:00 daily
  - Color: #E84C4C (alert red — regression detection)
  - Label: "Eval Check"
  - Position: point event at 09:00, immediately post-standup

Workflow 03 (Sprint Readiness Dossier):
  - Trigger: T-60 before sprint planning (typically Mon or Wed 10:00 or 11:00)
  - Color: #7B61FF (purple — planning/strategy)
  - Label: "Sprint Brief"
  - Position: event dot at sprint planning T-60 (varies by sprint cadence)

Workflow 04 (Agent Cohort Activation Gap):
  - Trigger: Friday 17:00
  - Color: #2ECC71 (green — growth/activation)
  - Label: "Cohort Gap"
  - Position: point event at Fri 17:00, end-of-week anchor
```

---

## Why these four (one paragraph)

The Product Owner role at SciSpace is defined by three compounding risks that a solo PM for a new product must hold simultaneously: silent quality degradation (an AI agent that gives wrong citations destroys researcher trust faster than any competitor can), roadmap noise (1M users generate a constant feedback stream that without synthesis becomes paralyzing), and activation plateau (the credits-based Agent layer sits on top of Premium, meaning the expansion revenue loop only works if researchers actually activate on Agent workflows, not just pay for them). The four workflows address exactly these risks in their actual daily shape. The Researcher Feedback Synthesizer (continuous) prevents the PM from drowning in raw signal or ignoring it entirely. The Agent Eval Regression Pulse (daily-cron) makes quality regression detectable in hours, not weeks. The Sprint Readiness Dossier (event-triggered) ensures every sprint planning conversation starts from shared evidence rather than intuition. The Agent Cohort Activation Gap (weekly-reflective) closes the loop between what researchers do after purchasing Agent access and what the roadmap should fix to improve that number. Together, they cover the quality loop, the user intelligence loop, the planning loop, and the growth loop — the four levers a first PM on an AI product must own to compound trust and revenue at the same time.

---

## What I considered and dropped (3 alternatives)

- **LLM Model Upgrade Impact Watcher (event-triggered):** Fires when a new foundation model version ships and auto-triggers a regression suite against the new model. Strong concept, but functionally a variant of the Agent Eval Regression Pulse — the eval harness in Workflow 02 already captures model-version-caused regressions by comparing the version changelog against failing cases. Adding a separate workflow creates redundancy. If the eval suite matures, this becomes a natural extension of Workflow 02 rather than a standalone demo.

- **Competitor Move Radar (weekly):** Continuously monitors Elicit, Consensus, OpenAI research blog, and Paperpal for feature releases and surfaces implications for the Agent roadmap. The concept is real and the cognitive load is medium-high. Dropped because (a) competitor monitoring is already embedded as an input into the Sprint Readiness Dossier, where it has the highest-leverage placement — immediately before a decision meeting; and (b) as a standalone weekly workflow it lacks the "system absorbs 80% of the work" quality since interpreting competitor moves still requires substantial PM judgment that doesn't reduce well to automation.

- **Free-to-Paid Activation Monitor (daily-cron):** Tracks which users hit the 5-paper free plan wall, how many dismissed the upgrade modal, and which segments churned vs. converted. Important funnel metric with high revenue impact. Dropped because the Product Owner role is scoped to the Agent product specifically, not the free-to-Premium funnel — that funnel sits closer to a growth PM or marketing function. Including it would misrepresent the role's scope. The Agent Cohort Activation Gap (Workflow 04) covers the equivalent question for the Agent credits layer, which is the correct scope boundary.

---

## Contamination check (state explicitly)

- **Cielo workflow name overlap:** No direct match. "Sprint Readiness Dossier" shares the structural prefix "Pre-" conceptually with "Pre-Meeting Brief" but the name was deliberately changed from "Pre-Sprint Evidence Brief" to eliminate even superficial similarity. All four final names are distinct concepts that would be meaningless in a brand-agency EA context.
- **Generic-name risk:** Low. "Researcher Feedback Synthesizer" could theoretically fit any consumer SaaS PM, but the inputs (academic paper query behavior, Intercom + Chrome Web Store + App Store, ICP segments PhD/postdoc/lab PI) and outputs (Linear tickets tagged by researcher type) make it role-specific. "Agent Eval Regression Pulse" is specific to AI/LLM product ownership. "Sprint Readiness Dossier" and "Agent Cohort Activation Gap" are specific to this product's engineering cadence and credits-based activation model.
- **Input-source overlap with Cielo:** None. Cielo uses Gmail + Calendar + Notion + GoHighLevel. These workflows use Intercom, Mixpanel, G2/Capterra, Linear, LangSmith/n8n eval harness, Chrome Web Store reviews, and Agent credits consumption logs. No shared input sources.
- **Firing-time overlap with Cielo:** None material. Cielo fires at 06:30 / continuous / T-30 / Sun 19:00. These workflows fire at 08:30 digest + continuous / 09:00 / T-60 event / Fri 17:00. The continuous archetype is shared (allowed per anti-overlap rules — archetype shape can repeat, names cannot). No identical firing times.
- **Final verdict:** PASS
