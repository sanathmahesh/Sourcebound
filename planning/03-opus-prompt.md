You are building a project called Sourcebound with me, over several sessions. This message is the
complete brief. You have no earlier context. The repository contains only a planning/ folder, which holds
this brief, a plan overview and a design brief; leave that folder in place and build around it.

=====================================================================
1. WHO I AM AND WHY THIS EXISTS
=====================================================================
I am a master's student and a strong AI engineer (agents, RAG, tool calling, eval harnesses). I have no
finance background. I am applying for a graduate role on a bank's Asset-Side AI Strategy team, which
applies AI to the bank's bond portfolio and lending. Sourcebound goes on my resume as a live link, and I
must be able to explain every part of it in an interview.

That purpose should shape your choices:
- Prefer simple, readable code I can walk an interviewer through over clever code.
- Explain every finance concept in plain English the first time it appears.
- Every number the site shows must be traceable to its source, and every result I quote must be measured.
- The role is AI strategy, so the project must also show judgment about where and how AI is used.

Sourcebound is a credit-analysis tool. It drafts a credit memo on a public company from its SEC filings and
proves every figure against source data. It answers: can this company repay its debt, and can we show
where every number came from?

=====================================================================
2. GROUND RULES  (save this section as CLAUDE.md)
=====================================================================
1. Build phase by phase, in the order in the plan. Within a phase, write the tests first, then the code.
   Commit when the phase's tests pass. Do not write code for a later phase early.
2. Stop after each phase and wait for my go-ahead. Your stop report must contain:
   (a) what you built; (b) the exact commands to run it; (c) what I should check by hand;
   (d) the real test output, including any failures; (e) assumptions and limitations added, and every
   fallback used; (f) what to read in NOTES.md; (g) questions and any scope changes you propose.
3. Never invent or silently substitute data.
   - If EDGAR, Sail, Vercel or any other source is unavailable or returns something unexpected, stop and
     ask me.
   - A missing XBRL fact is reported as "not available". It is never estimated, interpolated or copied
     from another period.
   - Financial values may be hardcoded only in test fixtures captured from real EDGAR responses, with the
     accession number recorded beside them.
   - Never fill in anything I am meant to supply: golden-set values, claim labels, agency ratings, timings.
4. Do not change the scope without asking. Put proposals in the stop report.
5. The language model never does arithmetic. Every figure comes from deterministic, tested code.
6. Keep ASSUMPTIONS.md, LIMITATIONS.md, NOTES.md and docs/strategy/06-decision-log.md current, updated in
   the same commit as the change that prompts them.
7. NOTES.md is my study guide. For each part of the system it holds: each finance or regulatory concept in
   plain English; why the part is built the way it is; and the interview questions I should be able to
   answer about it, each with a short model answer.
8. Secrets live only in .env (gitignored) and in server environment variables. Never commit, print or log
   them, and never let them reach the frontend. If I paste a key into chat, tell me to rotate it.
9. Follow SEC EDGAR fair-access rules: a declared User-Agent, a request rate well under the limit, and a
   cache for everything.
10. Outward-facing actions need my explicit go-ahead each time: creating or pushing to a remote, deploying,
    changing GitHub or Vercel settings.
11. The external facts in the plan were checked on 17 November 2026. Before you rely on one (Sail API
    behaviour and prices, Vercel limits, SEC endpoints, supervisory guidance), re-read the source and tell
    me if it has changed.
12. RESULTS.md and the strategy artifacts contain only measured numbers. Each number carries its sample
    size, date, model ID and the command that reproduces it. Estimates are labelled as estimates and kept
    out of RESULTS.md.
13. Write plainly: small functions, type hints, docstrings that say what and why. No abstractions without
    a second use.
14. This repo is standalone and shares nothing with any other project.

=====================================================================
3. FIRST ACTIONS
=====================================================================
1. Save section 4 as PLAN.md and section 2 as CLAUDE.md, both at the repository root. Run git init.
2. Create NOTES.md, ASSUMPTIONS.md (seeded from 4.14), LIMITATIONS.md (seeded from 4.15) and
   docs/strategy/06-decision-log.md (seeded from 4.2).
3. Ask me to create .env with SAIL_API_KEY and EDGAR_USER_AGENT (my name and contact email, which you must
   not hardcode anywhere). Provide .env.example.
4. Confirm you have read the plan, list anything unclear, then start phase 1.

=====================================================================
4. THE PLAN  (save this section as PLAN.md)
=====================================================================

4.1 WHAT IT MUST DO
1. Data: SEC EDGAR. Structured financials from the XBRL company facts API. Narrative from 10-K and 10-Q
   text: business description, management discussion, liquidity, debt footnotes, risk factors.
2. Ratio engine, deterministic and tested: debt to EBITDA, net leverage, EBITDA to interest, free cash flow
   to debt, liquidity sources against 12-month uses, a debt maturity ladder, and 3-year trends. A
   documented fallback chain per concept, with every fallback logged.
3. Scorecard: map the ratios to an internal rating grid, documented as my own stylized method.
4. Memo: retrieve relevant filing passages, then have the model draft a structured memo with six sections:
   business profile, financial risk, liquidity, maturity wall, key risks, rating rationale. Numbers come
   only from the ratio engine. Every qualitative claim cites a filing passage.
5. Verification in three layers: (a) each number traced to XBRL facts with tag, period and accession
   number; (b) each qualitative claim checked against its cited passage by a judge model; (c) anything
   unsupported goes into a reviewer checklist at the end of the memo for a human analyst to sign off.
6. Monitoring: a watchlist that re-runs when a company files a new 10-Q or 10-K and flags deterioration.
7. Evals: 15 companies; a golden set I hand-verify for 5; numeric accuracy, citation precision and
   unsupported-claim rate per model; scorecard rank order against agency ratings I enter by hand.
8. Interface: pick a company, read the memo, click any number to see its source, view the verification
   report and the watchlist, ask follow-up questions.
9. Strategy artifacts (4.16), shown on an About page and kept in the repo.

4.2 FIXED DECISIONS, WITH THE REASON FOR EACH  (seed the decision log; record rejected alternatives)
- Backend: Python 3.12, FastAPI, pandas, pytest. Frontend: React, Vite, TypeScript.
- Inference: Sail Research, not the Claude API, behind one interface configured by environment variables.
- Writer models to evaluate: zai-org/GLM-5.3, deepseek-ai/DeepSeek-V4-Pro-0813,
  deepseek-ai/DeepSeek-V4.1-Flash-1017. Two mid-priced models from different labs and one very cheap one,
  so the recommendation can show a cost against accuracy trade-off.
- Numbers by placeholder. The model writes tokens such as {{m:net_leverage:LTM}} and code substitutes the
  value. Rejected: letting the model copy numbers from a table, because copying errors are silent.
- The memo is a fixed pipeline, not an agent: the same retrieval steps every time, so it is auditable and
  repeatable. Only the live follow-up endpoint uses a bounded tool loop, because questions are open-ended.
- Retrieval: BM25 keyword search plus routing by filing section, with the index shipped as JSON files.
  Sail serves no embedding model. Rejected for now: local embeddings (large serverless bundle, slow cold
  starts) and a second embedding vendor (a second key and provider). Retrieval recall is measured in the
  evals; propose embeddings only if measured recall is poor.
- Hosting: Vercel Hobby, its own project, static frontend plus FastAPI as a Python function. Nothing is
  held in memory between requests. Memos, verification reports and the watchlist are generated ahead of
  time and shipped as static JSON with filing dates shown.
- Watchlist refresh: a daily GitHub Actions job that detects new filings and recomputes ratios and flags
  with no model call, then commits the JSON so Vercel redeploys. The affected memo is marked stale until I
  regenerate it locally and review it. Reason: the Sail key stays only in Vercel and on my laptop, and no
  memo is published without human review, which matches the project's own control story. Rejected:
  Vercel Cron (functions cannot write files) and automatic memo regeneration (publishes unreviewed
  output).
- Rate limiting: Vercel Firewall rate-limit rule keyed by IP on /api/ask. No database needed.
- I will design the interface separately in Claude Design. Build the data contract first, then a plain
  placeholder interface, then a later phase that implements the handed-off design.

4.3 EXTERNAL FACTS, CHECKED 17 NOVEMBER 2026  (re-check before relying on them)

SEC EDGAR
- Company facts: https://data.sec.gov/api/xbrl/companyfacts/CIK{10-digit CIK}.json
- Filing list: https://data.sec.gov/submissions/CIK{10-digit CIK}.json
- Filing documents: https://www.sec.gov/Archives/edgar/data/{cik}/{accession without dashes}/{document}
- Ticker to CIK: https://www.sec.gov/files/company_tickers.json  (look CIKs up here; do not use memory)
- Fair access: at most 10 requests per second and a User-Agent naming the requester with contact details.
  Throttle to 5 per second or lower, one request at a time. Read the User-Agent from EDGAR_USER_AGENT and
  refuse to run if it is unset.
- Company facts contains only standard-taxonomy facts without dimensions. Company-specific extension tags
  and segment breakdowns are absent. The fy and fp fields describe the filing a fact appeared in, not the
  fact's own period, so period logic must use the start and end dates.

Sail Research (https://docs.sailresearch.com: models, pricing, support, migrate, service-tiers,
rate-limits, retries pages)
- OpenAI-compatible. Base URL https://api.sailresearch.com/v1, header Authorization: Bearer <key>. Use the
  OpenAI Python SDK with base_url and api_key set from the environment.
- Chat Completions is stable and supports function tools (with strict), tool_choice, and response_format
  of type json_schema. The support matrix is per API, not per model, so per-model support must be
  confirmed by the capability probe in phase 4.
- Unsupported on Chat Completions: seed, stop, logprobs, top_logprobs, frequency and presence penalties,
  logit_bias, n other than 1. max_tokens is rejected; check the support page for the accepted output-limit
  parameter. There is no way to pin determinism, so the evals measure run-to-run spread.
- GLM-5.3 returns HTTP 400 for reasoning effort "none"; its lowest tier is "low".
- Service tiers: asap (default, no queue, for interactive use), balanced (may queue up to 5 minutes),
  flex (background Responses API or Batch only). Use asap everywhere so latency figures mean something.
- Prices per million tokens on asap, input / cached input / output: GLM-5.3 0.98 / 0.18 / 3.08;
  DeepSeek-V4-Pro-0813 0.92 / 0.04 / 2.77; DeepSeek-V4.1-Flash-1017 0.09 / 0.006 / 0.30. Store prices in
  config/prices.yaml with the date read, and re-read the pricing page before the evals.
- Errors: 429 and 503 carry Retry-After. Retry with backoff of about 1, 2, 4 seconds plus jitter, with a
  cap on attempts.
- No embedding or reranking endpoint. Context windows and output limits are not in the docs pages read;
  get them from GET /v1/models.
- Sail retires models on short notice. Pin model IDs in config, check GET /v1/models at the start of each
  pipeline run, and record the model ID and date in every generated file.
- Zero data retention by default; by default data may be processed outside the United States.
- My account has a key and paid credit.

Vercel Hobby
- Functions: 300 second maximum duration, 2 GB memory, 500 MB uncompressed bundle for Python, 4.5 MB
  request and response body, read-only filesystem with a writable /tmp that does not persist.
- Python 3.12 by default. FastAPI is detected from an app object in a standard entry file.
- Vercel's FastAPI page now recommends a "Services" feature for a backend and frontend in one project. Its
  availability on Hobby was not confirmed. Default to api/index.py exposing the FastAPI app, with
  vercel.json rewrites sending /api/* to it and the Vite build as static output. Read the current docs
  before phase 7 and tell me if a different layout is needed.
- Cron jobs run at most once a day on Hobby. Not used.
- Firewall: one rate-limit rule per project on Hobby, keyed by IP, fixed window of 10 seconds to 10
  minutes, action 429.
- Not confirmed: whether Hobby deploys commits pushed by a GitHub Actions bot. Verify in phase 6. The
  fallback is a Vercel deploy hook.

US supervisory guidance on model risk management
- SR 11-7 (2011) is superseded. On 17 April 2026 the Federal Reserve, OCC and FDIC issued revised
  "Supervisory Guidance on Model Risk Management": Fed SR 26-2, OCC Bulletin 2026-13, FDIC FIL-15-2026.
  Read the guidance itself before writing the control table.
- Its vocabulary, which the control table must use: model risk; inherent risk; model exposure; model
  purpose; model materiality; aggregate risk; effective challenge; model development (statement of
  purpose, model testing); model use (intended purpose, limitations); model validation (conceptual
  soundness, outcomes analysis); ongoing model monitoring; governance and controls (roles and
  responsibilities, model inventory, documentation); vendor and other third-party products.
- Scope, which matters for honesty:
  (1) "model" means a complex quantitative method applying statistical, economic or financial theories to
      produce quantitative estimates, and excludes simple arithmetic and deterministic rule-based
      processes. The ratio engine is therefore not a model under this definition.
  (2) Footnote 3 states that generative AI and agentic AI models are not within the scope of the guidance,
      and that a banking organization's own risk management and governance practices should determine
      controls for tools not covered.
  (3) The guidance is expected to be most relevant to banks with over $30 billion in assets and says it
      sets no enforceable standards.
- So the control table must say plainly that it borrows the guidance's vocabulary by choice, and must not
  claim the guidance applies to the generative parts or that the project "complies".
- The agencies said a request for information on AI in model risk management would follow. None was found
  as of 17 November 2026. Check again.
- Also read before citing: OCC Bulletin 2026-54 (4 November 2026, an examiner framework on AI that
  reportedly sets no expectations for banks; I have only seen a summary), and the interagency third-party
  risk management guidance (2023, with a replacement proposed in September 2026), since Sail is a vendor.
- In NOTES.md, explain all of this in plain English, including what SR 11-7 was, because interviewers may
  still use the old name.

4.4 ARCHITECTURE AND REPO LAYOUT
Flow: EDGAR -> disk cache -> (a) ratio engine -> metrics with lineage -> scorecard; (b) filing text ->
sections -> chunks -> BM25 index. Writer model receives the metric table and retrieved passages and returns
claims. Verification runs. Everything is exported as static JSON, served from the Vercel CDN and read by
the React app. The one live function answers follow-up questions with the same retrieval and checks.

PLAN.md CLAUDE.md NOTES.md ASSUMPTIONS.md LIMITATIONS.md MODEL_CARD.md RESULTS.md README.md
pyproject.toml  vercel.json  .env.example
planning/               the original brief, plan overview and design brief (do not modify)
api/index.py            Vercel entry point; imports the FastAPI app
sourcebound/
  edgar/                client (User-Agent, throttle, retries, cache), facts, filings, sections
  engine/               concepts and fallback chains, periods, ratios, ladder, lineage
  scorecard/            grid loaded from config, scoring
  retrieval/            chunking, BM25 (our own small implementation), index build and load
  llm/                  provider interface, schemas, prompts
  memo/                 section specs, drafting, placeholder rendering
  verify/               number trace, quote check, judge, checklist
  watchlist/            new-filing detection, flags
  pipeline/             command-line entry points, export of static JSON
  api/                  FastAPI app: /api/ask, /api/health
  contracts.py          Pydantic models: the single source of the data contract
config/                 companies.yaml, concepts.yaml, grid.yaml, prices.yaml, overrides.yaml
evals/                  golden/, labels/, agency_ratings.csv, timings.csv, results/, run scripts
data/raw/               EDGAR cache (gitignored)
data/published/         static JSON shipped to the site (committed)
docs/strategy/          the six strategy artifacts as Markdown
web/                    React + Vite + TypeScript
tests/                  includes fixtures captured from real EDGAR responses
.github/workflows/      ci.yml, watchlist.yml

Environment variables: SAIL_BASE_URL, SAIL_API_KEY, SAIL_MODEL_WRITER, SAIL_MODEL_JUDGE,
SAIL_SERVICE_TIER, EDGAR_USER_AGENT. The live function must import neither pandas nor the EDGAR client.

4.5 RATIO ENGINE
Periods: the last three completed fiscal years (FY-2, FY-1, FY0) and LTM (last twelve months) as of the
latest 10-Q when one is newer than the latest 10-K. For flow items, LTM = FY0 + current year-to-date -
prior-year year-to-date; check that the three windows line up before computing. Balance-sheet items use
the latest period end. Identify periods from start and end dates, allowing for 52/53-week years. When a
period's fact appears in several filings, use the most recently filed value and record its accession
number; log when it differs from the original.

Concepts and starting fallback chains (us-gaap tags, in rank order). These are starting points. In phase 1
produce a tag-discovery report showing which candidate tags each company actually reports, and propose
changes to me. Chains live in config/concepts.yaml.
- revenue: RevenueFromContractWithCustomerExcludingAssessedTax; Revenues;
  RevenueFromContractWithCustomerIncludingAssessedTax; SalesRevenueNet
- operating_income: OperatingIncomeLoss; else derived as pre-tax income from continuing operations plus
  interest expense, flagged as derived
- d_and_a: DepreciationDepletionAndAmortization; DepreciationAndAmortization;
  DepreciationAmortizationAndAccretionNet; Depreciation + AmortizationOfIntangibleAssets
- interest_expense: InterestExpense; InterestExpenseNonoperating; InterestExpenseDebt;
  InterestAndDebtExpense; InterestPaidNet (cash paid, flagged as a proxy)
- short_term_debt: DebtCurrent; else LongTermDebtCurrent + ShortTermBorrowings (+ CommercialPaper)
- total_debt: DebtLongtermAndShorttermCombinedAmount; LongTermDebtNoncurrent + short_term_debt;
  LongTermDebt + ShortTermBorrowings; LongTermDebtAndCapitalLeaseObligations + its current counterpart +
  ShortTermBorrowings. LongTermDebt sometimes includes the current portion and sometimes does not:
  when the component tags exist, reconcile and log.
- cash: CashAndCashEquivalentsAtCarryingValue; CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents
  (flagged: includes restricted cash). Add ShortTermInvestments, MarketableSecuritiesCurrent or
  AvailableForSaleSecuritiesDebtSecuritiesCurrent if reported.
- cfo: NetCashProvidedByUsedInOperatingActivities; ...ContinuingOperations
- capex: PaymentsToAcquirePropertyPlantAndEquipment; PaymentsToAcquireProductiveAssets;
  PaymentsForCapitalImprovements
- dividends: PaymentsOfDividends; PaymentsOfDividendsCommonStock; PaymentsOfOrdinaryDividends
- undrawn_revolver: LineOfCreditFacilityRemainingBorrowingCapacity
- maturities: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths, ...InYearTwo, ...InYearThree,
  ...InYearFour, ...InYearFive, ...AfterYearFive, from the latest 10-K

Rules
- A required concept with no fact is "not available"; ratios depending on it are "not available".
- An optional component with no fact (short-term investments, short-term borrowings, dividends) is treated
  as zero, and each such case is logged as "assumed zero: not reported" and placed on the checklist.
- Every resolved value carries lineage: concept, tag used, fallback rank, value, unit, period, form,
  accession number, filing date, EDGAR URL. Every ratio carries its formula and its inputs' lineage.
- Per-company overrides are allowed only in config/overrides.yaml, each with a written reason and my
  approval, and each appears on that company's checklist.

Ratios
- EBITDA = operating_income + d_and_a (unadjusted)
- Debt / EBITDA = total_debt / EBITDA
- Net leverage = (total_debt - cash) / EBITDA; show "net cash" when negative
- Interest coverage = EBITDA / interest_expense
- FCF / debt = (cfo - capex) / total_debt
- Liquidity coverage = sources / uses, where sources = cash + undrawn_revolver (if tagged) + LTM cfo
  (floored at zero) and uses = debt due within 12 months + LTM capex + LTM dividends
- Maturity ladder: years 1 to 5 and later; share due within 24 months; near-term maturity cover =
  debt due within 24 months / (cash + undrawn_revolver)
- Trends: each ratio for FY-2, FY-1, FY0 and LTM, with direction
- EBITDA at or below zero: leverage and coverage are "not meaningful". Zero debt: leverage is 0 and
  FCF / debt is "not meaningful: no debt".
- Checks that raise warnings: ladder sum against total debt (over 5% apart); revenue change above 40%
  year on year ("possible structural change").

4.6 SCORECARD  (my own stylized method; thresholds in config/grid.yaml; documented in docs/strategy)
Each factor scores 1 (strongest) to 6 (weakest):
- Debt / EBITDA, weight 20%: <1.0 | 1.0-2.0 | 2.0-3.0 | 3.0-4.5 | 4.5-6.5 | >6.5 or EBITDA <= 0
- Net debt / EBITDA, 10%: <0.5 or net cash | 0.5-1.5 | 1.5-2.5 | 2.5-4.0 | 4.0-6.0 | >6.0 or EBITDA <= 0
- EBITDA / interest, 25%: >15 | 10-15 | 6-10 | 3.5-6 | 2-3.5 | <2
- FCF / debt, 20%: >40% | 25-40% | 15-25% | 8-15% | 0-8% | negative
- Liquidity coverage, 15%: >2.5 | 2.0-2.5 | 1.5-2.0 | 1.2-1.5 | 1.0-1.2 | <1.0
- Near-term maturity cover, 10%: <0.25 | 0.25-0.5 | 0.5-0.75 | 0.75-1.0 | 1.0-1.5 | >1.5
Weighted score maps to SB-1 (<=1.5), SB-2 (<=2.5), SB-3 (<=3.5), SB-4 (<=4.5), SB-5 (<=5.5), SB-6 (>5.5).
A score of 3.5 or below is "IG-like". If a factor is not available, renormalise the remaining weights,
mark the grade provisional, and add a checklist item. Zero debt scores 1 on debt-related factors.
The grid is frozen at the end of phase 2 (tag the commit grid-v1) before any comparison with agency
ratings. Any later change is logged and reported as tuning. SB grades are not credit ratings and must
never be presented as such.

4.7 FILING TEXT AND RETRIEVAL
- Corpus per company: the latest 10-K and every 10-Q filed after it.
- Parse the primary HTML document to text. Detect 10-K Items 1, 1A, 7, 7A and 8, and within Item 8 the
  debt note; in 10-Qs detect management discussion, liquidity and risk-factor updates. Filing HTML is
  inconsistent: produce a section-coverage report for all 15, fall back to unlabelled chunks when
  detection fails, and never guess a section label.
- Chunk by paragraph to roughly 900-1,500 characters. Each chunk stores id, accession, form, filing date,
  section, character offsets and the document URL, and its text must equal the source text at those
  offsets.
- BM25: our own implementation (lowercase alphanumeric tokens, a short stopword list, k1 = 1.5, b = 0.75),
  small enough to explain line by line. One JSON index file per company.
- Each memo section has fixed query templates and a section filter. Merge and de-duplicate to about eight
  passages per section.

4.8 MEMO DRAFTING
- One model call per section, with structured output validated by Pydantic.
- Inputs per section: the company's metric table with metric IDs, the retrieved passages with chunk IDs,
  and the section's instructions. Rating rationale receives the scorecard and the verified claims from
  earlier sections, and no new passages.
- Output: a list of claims, one sentence each: kind (quantitative or qualitative), text, citations (chunk
  IDs), and for each citation a short word-for-word quote from the passage.
- Number rule: engine figures appear only as placeholders {{m:<metric_id>:<period>}}. A figure from the
  filing narrative (for example the size of a credit facility) is allowed only if it appears word for word
  in a cited passage; it is rendered as a "quoted figure" and traced to the passage, not to XBRL.
- On validation failure, allow one repair attempt, then keep the claim, mark it, and put it on the
  checklist.

4.9 VERIFICATION
(a) Numbers. Every placeholder resolves to an engine value with full lineage. A deterministic validator
    scans every claim: any digit that is neither a rendered placeholder nor present in a cited passage
    fails. For LTM values the lineage shows all three component facts.
(b) Claims. First deterministic checks: the cited chunk exists, and the quote appears in it after
    whitespace and case normalisation. If not, the verdict is "unsupported: quote not found" with no model
    call. Otherwise the judge model receives the rendered claim and the cited passages and returns a
    verdict (supported, partially supported, unsupported), a one-line reason and the evidence quote.
(c) Reviewer checklist, appended to the memo: unsupported and partially supported claims; figures not
    available; fallbacks beyond rank 1; assumed-zero components; overrides; reconciliation warnings;
    provisional grade; stale data. Unsupported claims stay visible in the memo, clearly marked.
The unsupported-claim rate is measured before any filtering.

4.10 WATCHLIST
- Daily GitHub Actions job: read each company's submissions file (15 requests), compare the latest 10-Q
  and 10-K accession numbers with data/published/state.json. For a new filing, refresh company facts,
  recompute ratios and scorecard, compute flags, write watchlist.json, and mark the memo stale. No model
  call. Commit only when something changed, plus one weekly heartbeat commit that updates the "last
  checked" date. EDGAR_USER_AGENT is a GitHub Actions secret.
- A memo is a dated snapshot and embeds its own metric values and lineage. After a refresh, the latest
  metrics file is newer than the memo, and the interface says so.
- Flags, comparing the latest LTM with the prior fiscal year-end:
  leverage_up: Debt / EBITDA up by 0.5x or more, or a worse band
  coverage_down: EBITDA / interest down by 20% or more, or a worse band
  liquidity_shortfall: liquidity coverage below 1.2 (warning) or below 1.0 (alert)
  near_term_maturities: debt due within 12 months above 50% of cash + undrawn revolver (warning) or above
  100% (alert)
  grade_change: a worse SB grade
- Regenerating a memo is a local command that I run, followed by my review.

4.11 EVALS
Companies: the 15 in 4.12. Golden set: WMT, VZ, HCA, GT, CCL, hand-verified by me with the template in 4.17.
Agency ratings: entered by me in evals/agency_ratings.csv with agency, rating, date and source. Scorecard
code must never read this file; add a test that enforces it.

Procedure
1. Generate golden-set memos with each of the three writer models.
2. Export a blind labelling sheet: 12 claims per memo, 2 per section, shuffled, model identity hidden
   (about 180 rows). I label each claim supported / partially supported / unsupported and each citation
   correct or not.
3. Judge calibration: run GLM-5.3 and DeepSeek-V4-Pro as judge candidates over the labelled rows. Report
   agreement with my labels and the false-pass rate (judge says supported, I say unsupported). I choose the
   judge; it is then fixed for all writers.
4. Seeded-error test: corrupt known-good claims (change a number, negate the claim, swap the citation) and
   report the share caught by each layer.
5. Generate and verify memos for all 15 companies with each writer. Repeat the golden-set memos three
   times per writer to report run-to-run spread.

Metrics, each reported with its sample size
- Engine numeric accuracy: of hand-verified values where the engine produced a value, the share that
  match (inputs after rounding to the filing's unit; ratios within 0.05x or 1 percentage point). Report
  coverage separately: the share of hand-verified items for which the engine produced a value.
- Memo numeric accuracy, per model: of the figures printed in that model's golden-set memos, the share
  that equal the hand-verified value (engine figures) or appear word for word in the cited passage
  (quoted figures). Also report how many raw-number attempts the validator rejected.
- Citation precision, per model: of labelled claim-citation pairs, the share where the passage supports
  the claim, by my labels.
- Unsupported-claim rate, per model: by my labels on the sample, and separately by the judge on all 15
  companies, labelled as judge-estimated.
- Retrieval recall: for the five fact questions per golden company, whether the passage I located appears
  in the top eight results.
- Cost per memo, per model: token counts from the API's usage field multiplied by Sail's list price,
  drafting and verification shown separately and summed. Time per memo, per model.
- Scorecard against agency ratings: Spearman rank correlation and IG/HY agreement, n = 15, with a plain
  statement that the sample is small.
Save every raw output so that results can be recomputed without new model calls.

4.12 COMPANIES  (US non-financial filers; approved by me)
Golden set: Walmart WMT, Verizon VZ, Goodyear GT, HCA Healthcare HCA, Carnival CCL.
Others: Microsoft MSFT, Procter & Gamble PG, ExxonMobil XOM, Union Pacific UNP, Oracle ORCL, Kohl's KSS,
American Airlines AAL, Cleveland-Cliffs CLF, Caesars Entertainment CZR, Community Health Systems CYH.
Phase 1 uses WMT, VZ and GT. If a company's data proves unusable, stop and ask; do not swap it yourself.

4.13 PUBLISHED DATA CONTRACT AND LIVE API
Static JSON under /data, defined by Pydantic models in contracts.py, exported as JSON Schema, with
TypeScript types generated from the schemas. Every published file is validated in tests.
- /data/index.json: generated_at; per company: ticker, name, sector, grade, score, provisional, headline
  ratios with status, latest_filing {form, period_end, filed}, memo_status (current | stale), verification
  counts, open_flags.
- /data/companies/{ticker}/memo.json: ticker, memo_date, model, grade, sources [{form, accession,
  period_end, filed, url}], sections [{id, title, claims [{id, kind, verdict, judge_reason, segments
  [{t: text | metric | quoted, v, metric_id?, chunk_id?}], citations [{chunk_id, quote}]}]}], metrics
  {metric_id: {label, value, unit, status (ok | not_available | not_meaningful | net_cash), formula,
  inputs [{label, tag, fallback_rank, value, unit, period, form, accession, filed, url}]}}, passages
  {chunk_id: {text, section, form, filed, url}}, trends, maturity_ladder, scorecard {factors [{id, value,
  band, weight}], weighted_score, grade}, checklist [{id, category, severity, message, ref}].
- /data/companies/{ticker}/metrics.json: the latest metrics, same shapes, possibly newer than the memo.
- /data/companies/{ticker}/verification.json: summary counts, numbers, claims, fallback_log, warnings.
- /data/watchlist.json: checked_at; items [{ticker, latest_filing, memo_status, flags [{type, severity,
  rule, metric_id, from, to}]}].
- /data/evals.json: per-model metrics with sample sizes, judge calibration, scorecard against agency.
- /data/about.json: the strategy documents as Markdown.
Live endpoints
- POST /api/ask {ticker, question}. The model may call two read-only tools, get_metric and search_filing,
  for at most three rounds, then must return claims in the same shape as the memo. The same number
  validator, quote check and judge run on every claim. Claims that fail are removed from the answer and
  returned in a "removed" list with the reason. Response: status (ok | out_of_scope), claims, removed,
  metrics, passages, trace of tool calls, model, seconds. Limits: question at most 500 characters, capped
  output tokens, 60-second overall timeout. Errors: 400, 429, 503 with plain messages. Tools can read only
  the requested company's published data.
- GET /api/health.
Every page shows the data date and: "Educational project. Not investment advice. SB grades are a
student's stylized scorecard, not credit ratings."

4.14 SIMPLIFYING ASSUMPTIONS  (seed ASSUMPTIONS.md; add to it as you work)
1. US non-financial 10-K filers only; no banks, insurers or companies with large captive finance arms.
2. EBITDA is unadjusted: operating income plus depreciation and amortisation.
3. Debt is reported borrowings; operating leases, pensions and guarantees are excluded.
4. Each period uses the most recently filed value.
5. LTM is derived from year-to-date figures.
6. Liquidity uses trailing cash flow as a stand-in for the next 12 months; undrawn revolver capacity
   counts only if tagged.
7. The maturity ladder comes from the annual 10-K.
8. Optional components that are not reported are treated as zero, logged, and shown to the reviewer.
9. The narrative corpus is the latest 10-K and later 10-Qs only.
10. The scorecard is financial-ratio-only, stylized, and frozen before comparison with agency ratings.
11. The judge is a language model; its verdicts are estimates calibrated against a human-labelled sample.
12. Reviewer sign-off in the interface is a demonstration stored in the browser.
13. Memos are dated snapshots; refreshed ratios may be newer than the memo.
14. Timings are self-recorded by a non-expert on a few companies.

4.15 KNOWN RISKS AND LIMITATIONS  (seed LIMITATIONS.md)
- XBRL tagging varies by company and over time; extension tags are invisible to the API; LongTermDebt is
  ambiguous; restatements change history; mergers break trends. Handling is in 4.5.
- No business-risk factors (scale, diversification, cyclicality) in the scorecard, so it will misjudge
  some companies against agencies.
- Section parsing of filing HTML can fail; tables are flattened to text.
- Keyword retrieval misses paraphrases.
- A quoted figure can match a number in the passage that refers to something else; the judge is the only
  check on that.
- The judge can be wrong, and when the judge and writer are the same model it may be lenient. Human labels
  on the golden set are the reference.
- Model outputs vary between runs; Sail may retire a model.
- The scheduled job may be disabled by GitHub after long inactivity; deploys from bot commits are unverified.
- The rate limit is per IP only; the spend backstop is a small prepaid Sail balance with auto-recharge off.
- Agency ratings carry redistribution terms. By default the site shows only aggregate agreement; ask me
  before showing per-company ratings.

4.16 STRATEGY ARTIFACTS  (plain English; in docs/strategy and on the About page)
1. Opportunity map: 8 to 10 workflows of a bank's investment and lending teams (for example credit memo
   drafting, covenant extraction and monitoring, financial spreading, portfolio surveillance of filings,
   new-issue document summaries, committee reporting), each scored on value, feasibility and risk with a
   one-line reason, and an explanation of why this use case was chosen. Scores are my judgment and are
   labelled as such. No invented market statistics. Draft it for my review and expect me to change it.
2. Manual against tool-assisted effort, using only timings I record in evals/timings.csv. Provide the
   protocol and the log template; never fill in a timing.
3. Model recommendation memo from the eval results: accuracy, latency and cost per task for each model.
4. Risk and control table: each failure mode, the control that catches it, the evidence it works (a named
   test or eval metric), and the matching term from the 2026 guidance, with the scope statement from 4.3.
5. Rollout plan: pilot group, human review step, what gets logged, what would trigger a rollback.
6. Decision log: main design choices with the alternatives rejected.
Explain the reasoning behind every artifact in NOTES.md so I can defend it.

4.17 TEMPLATES TO GENERATE FOR ME
- Golden-set sheet per company (evals/golden/{ticker}.md), for the latest 10-K. Rows: revenue; operating
  income; depreciation and amortisation; interest expense; cash and equivalents; short-term investments;
  short-term borrowings plus current portion of long-term debt; long-term debt excluding current portion;
  cash from operations; capital expenditure; dividends paid; undrawn revolver capacity; debt due in years
  1, 2, 3, 4, 5 and later. Columns: where to look, value in filing, page or note. Then derived rows I
  compute by calculator: EBITDA, total debt, debt / EBITDA, net debt / EBITDA, EBITDA / interest,
  FCF / debt, liquidity coverage. Then five fact questions with answer and exact location: revolver size
  and expiry; covenants and stated compliance; largest maturity in the next three years; management's
  stated liquidity sources; the risk factor most relevant to repaying debt. I fill in my values before
  seeing the tool's; a script adds the tool's values and the match column afterwards.
- Claim-labelling sheet (CSV): id, claim, cited passage, my verdict, citation correct, notes.
- Timing log (CSV): date, company, condition (manual | tool-assisted), task, start, end, minutes, errors
  found later, notes.

4.18 PHASES
Each phase ends with passing tests, a commit, a stop report, and my go-ahead.

Phase 1. Foundations, and ratios for three companies.
Build: project scaffold, config, the EDGAR client, ticker-to-CIK lookup, the company-facts normaliser,
period logic, the concept resolver with fallback log, the four core ratios (debt / EBITDA, net leverage,
interest coverage, FCF / debt) for FY-2, FY-1, FY0 and LTM, and the tag-discovery report.
Ends with: one command that, for WMT, VZ and GT, prints every ratio with its formula and, directly beneath
it, the raw XBRL facts it used (tag, fallback rank, value, period, form, accession number, filing date,
EDGAR link), and writes the same to a Markdown file per company. I check these by hand against the 10-Ks
before anything else is built.
Tests: fiscal-year identification across different year-ends; LTM arithmetic and window checks;
restatement de-duplication; the fallback resolver and its log; ratio maths including zero and negative
EBITDA and missing inputs; the EDGAR client sends the User-Agent, refuses to run without it, respects the
throttle, retries on 429, and serves repeats from cache (mocked transport, no network in unit tests);
fixture tests on captured facts for the three companies.

Phase 2. All 15 companies, remaining metrics, scorecard.
Build: liquidity coverage, maturity ladder, trends, warnings, the scorecard, metrics export, a coverage
report (company by metric: fallback rank used, assumed zero, or not available).
Ends with: a scorecard table for 15 companies and the coverage report. I fill in the golden sheets for HCA
and CCL and enter agency ratings. Freeze the grid.
Tests: every band boundary; weights sum to 1; a property test that a worse ratio never earns a better
score; renormalisation and the provisional flag; ladder reconciliation; exported files validate against
the contract; scorecard code does not read the agency file.

Phase 3. Filing text and retrieval.
Build: filing download, section parser, chunker, BM25, index files, a search command, the section-coverage
report.
Ends with: searching a company's filings from the command line and seeing ranked passages with section,
filing and link.
Tests: BM25 scores equal a hand-computed toy example; tokeniser; chunk offsets reproduce the source text;
section parser on three saved filings; index build is deterministic.

Phase 4. Model client, memo drafting, verification.
Build first: the provider interface and a capability probe that, for each of the three models, tests
structured output with a JSON schema, a strict tool call, and both in one request, and records model
limits from GET /v1/models. Write the results to docs/sail-capability-probe.md. If a model fails, stop and
ask. Then: section specs and prompts, drafting, placeholder rendering, the number validator, quote check,
judge (GLM-5.3 provisionally), checklist.
Ends with: memos with verdicts and checklists for WMT, VZ and GT that I can read, with every number
traceable.
Tests: the interface against a fake client; rendering; the validator rejects raw digits and accepts quoted
figures present in the passage; quote normalisation; judge output parsing; checklist assembly; corrupted
claims are caught by the deterministic layers; live smoke tests marked so they run only on request.

Phase 5. Evals and model choice.
Build: the procedure in 4.11, the labelling sheet, metric functions, a results report.
Ends with: a per-model results table. I label, choose the judge, then choose the writer.
Tests: each metric function on hand-built cases; the labelling sheet hides model identity; results
recompute from saved outputs without model calls.

Phase 6. Watchlist and publishing pipeline.
Build: new-filing detection, flags, stale marking, a build-all command that generates all 15 memos with
the chosen models and exports the static JSON, and the GitHub Actions workflow file. Verify how Vercel
handles bot commits and tell me.
Ends with: a simulated new filing (state rolled back for one company) producing flags and a stale memo,
and a second run with nothing new producing no changes.
Tests: each flag threshold; detection against mocked submissions; idempotency; heartbeat logic.

Phase 7. Live API, placeholder interface, preview deploy.
Build: /api/ask and /api/health; JSON Schema and TypeScript type generation; a plain React interface with
every screen working: portfolio, memo with source drawer and checklist, verification report, watchlist,
results, about, and the follow-up panel. Then, with my go-ahead, a Vercel preview deploy to surface
platform problems early.
Tests: request validation; tool-loop bounds; failed claims are removed; error mapping; contract validation
of every published file; frontend type-check and a few component tests.

Phase 8. Strategy artifacts and About page.
Build: the six artifacts from 4.16, using only eval results and my recorded timings; render them in the app.
Tests: a check that every number in an artifact matches a results file or the timing log.

Phase 9. Implement the handed-off design.
I will give you the Claude Design handoff. Implement it over the same data contract without changing the
contract. If the design needs data the contract lacks, stop and ask.
Tests: contract tests unchanged; a visual check against the handoff on desktop and phone widths.

Phase 10. Production deploy and final documents.
With my go-ahead: deploy to Vercel; set server environment variables; give me the steps to add the
firewall rate-limit rule on /api/ask (about 10 requests per 10 minutes per IP) and verify that the
excess request receives 429; enable the scheduled workflow. Check that the built frontend contains no
secrets.
Write MODEL_CARD.md: intended use, out-of-scope use, assumptions, limitations, and the human review
procedure. Write RESULTS.md containing only measured numbers I can quote on my resume: numeric accuracy,
citation precision, unsupported-claim rate and cost per memo, per model, each with sample size, date,
model ID and the reproducing command. Finish the README with the live link and how to run everything.

4.19 WHAT ONLY I PROVIDE
SAIL_API_KEY and EDGAR_USER_AGENT; approval of chain changes and overrides; golden-set values; claim
labels; agency ratings; timings; the choice of judge and writer; the GitHub repository and Vercel project;
the design handoff. If you need one of these, ask and wait.
