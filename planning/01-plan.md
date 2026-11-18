# Sourcebound: the plan

Written 17 November 2026. This is the plan for you to read and approve. The design brief is in `02-design-brief.md` and the build prompt for Opus is in `03-opus-prompt.md`.

Decisions already made: Sail key with paid credit; three writer models (GLM-5.3, DeepSeek V4 Pro, DeepSeek V4.1 Flash); keyword retrieval; a daily GitHub Actions refresh that recomputes numbers only.

## What Sourcebound is

Sourcebound reads a public company's SEC filings and produces a credit memo: the written case an analyst makes about whether a borrower can repay its debt. Tested code computes every figure, a language model writes the prose around those figures, and three checks prove where each number and claim came from. Anything unproven lands on a checklist for a human reviewer.

## Terms you will meet

| Term | Plain English |
|---|---|
| 10-K / 10-Q | The annual and quarterly reports US-listed companies file with the SEC. EDGAR is the SEC's filing database. |
| XBRL | Machine-readable tags attached to each number in a filing, such as `us-gaap:LongTermDebt`. |
| Accession number | The unique ID of one filing. |
| EBITDA | Earnings before interest, tax, depreciation and amortisation: a rough measure of the cash a business generates before paying lenders and tax. |
| Debt / EBITDA (leverage) | How many years of EBITDA it would take to repay all debt. Higher is riskier. |
| Net leverage | The same, after subtracting the company's cash from its debt. |
| EBITDA / interest (coverage) | How many times over earnings cover the yearly interest bill. |
| Free cash flow (FCF) | Cash from operations minus capital expenditure (spending on plant and equipment). FCF / debt is the share of debt a year's spare cash could repay. |
| Liquidity sources vs uses | Cash available over the next 12 months against cash needed. Below 1.0 is a shortfall. |
| Revolver | A revolving credit facility: a bank credit line the company can draw and repay. |
| Maturity ladder / wall | How much debt falls due each year. A "wall" is a large amount due in one year. |
| Investment grade (IG) / high yield (HY) | The rating agencies' split between lower-risk borrowers (BBB- and above) and riskier ones. |
| LTM | Last twelve months. |
| Scorecard | A table that maps each ratio to a score band and weights the scores into one internal grade. |

## What I verified, and what it changes

**Sail Research** (docs read 17 Nov 2026)
- OpenAI-compatible at `https://api.sailresearch.com/v1`, so the provider interface is the OpenAI Python SDK with three environment variables.
- Chat Completions supports function tools with `strict` and `response_format: json_schema`.
- The support matrix is per API, not per model. Phase 4 therefore opens with a probe that sends a structured-output request and a tool-call request to each of your three models and records the result.
- No embedding or reranking endpoint exists.
- `seed`, `stop`, `logprobs` and `max_tokens` are unsupported on Chat Completions. With no seed, runs cannot be pinned, so the evals repeat the golden-set memos three times and report the spread.
- Prices per million tokens (input / output, default tier):

| Model | Price |
|---|---|
| GLM-5.3 | $0.98 / $3.08 |
| DeepSeek V4 Pro 0813 | $0.92 / $2.77 |
| DeepSeek V4.1 Flash 1017 | $0.09 / $0.30 |

- Sail retires models (one retires on 19 Nov 2026), so every output records the model ID and date.
- Context windows and output limits are not in the pages I read; the probe fetches them from `GET /v1/models`.

**Vercel Hobby**
- Functions: up to 300 seconds, 500 MB Python bundle, read-only filesystem.
- Cron runs once a day at most.
- The firewall allows one per-IP rate-limit rule per project, which is your rate limit with no database.
- Vercel's FastAPI page now points to a "Services" feature for backend plus frontend in one project. I could not confirm it works on Hobby, so the plan uses the long-standing layout (`api/index.py` plus rewrites) and deploys a preview early to find out.

**Model risk guidance**
- SR 11-7 is no longer current. On 17 April 2026 the Fed, OCC and FDIC replaced it with revised guidance: SR 26-2, OCC Bulletin 2026-13, FDIC FIL-15-2026. I read the full text.
- Its sections are: model development and model use; model validation and monitoring (conceptual soundness, outcomes analysis, ongoing model monitoring); governance and controls (roles and responsibilities, model inventory, documentation); vendor and other third-party products. It keeps "effective challenge" and adds "model materiality" (exposure plus purpose).
- **Generative AI is out of scope.** Footnote 3 says generative and agentic AI models "are not within the scope of this guidance", and that a bank's own risk management and governance practices should set the controls for them.
- **Deterministic software is not a "model".** The definition excludes "deterministic rule-based processes", which describes your ratio engine.
- Your control table should therefore say it borrows the guidance's vocabulary by choice and does not claim the guidance applies. That is a stronger interview answer than citing SR 11-7.
- The agencies said a request for information on AI would follow. I found none issued as of 17 Nov 2026, but could not check the OCC's index.
- An OCC examiner framework on AI (Bulletin 2026-54, 4 Nov 2026) reportedly sets no expectations for banks. I saw only a summary of it, so Opus must read it before citing it.

## How the pieces fit

```
EDGAR (XBRL facts + filing text) ──> disk cache
   ├─> ratio engine (deterministic) ──> metrics with lineage ──> scorecard grade
   └─> sections ──> chunks ──> BM25 index (a JSON file per company)
                                   │
writer model (Sail) <── metric table + retrieved passages
   └─> claims: text with metric placeholders + passage citations
          └─> verification: (a) number trace  (b) quote check + judge model  (c) reviewer checklist
                 └─> static JSON ──> Vercel CDN ──> React interface

Live:   POST /api/ask ──> same retrieval, same checks, per-IP limit
Daily:  GitHub Action ──> new filing? ──> ratios + flags (no model) ──> commit ──> redeploy
```

Two design choices carry most of the weight:

- **Numbers by placeholder.** The model writes `{{m:net_leverage:LTM}}`, never a digit. Code substitutes the value. A validator rejects any digit in the prose that is neither a placeholder nor present word-for-word in the cited passage.
- **Fixed pipeline for the memo, bounded tool loop for questions.** The memo runs the same retrieval steps every time, which makes it auditable. Only the open-ended follow-up endpoint lets the model choose its lookups, through two read-only tools and at most three rounds.

## Phases

Each phase ends with a commit and a stop for your go-ahead.

| # | Phase | You run and check | Tests that prove it |
|---|---|---|---|
| 1 | Foundations; ratios for Walmart, Verizon, Goodyear | One command prints each ratio with its formula and, beneath it, the raw XBRL facts (tag, value, period, form, accession number, filing date, EDGAR link). You check them against the 10-Ks. | Fiscal-year and LTM logic; restatement de-duplication; fallback resolver and its log; ratio maths including zero and negative EBITDA; EDGAR client sends the User-Agent, stays under the rate limit, and serves repeats from cache. |
| 2 | All 15 companies; liquidity, maturity ladder, trends, scorecard | Scorecard table for 15; a coverage report showing, per company and metric, which fallback was used or "not available". | Band boundaries; weights sum to 1; a worse ratio never earns a better score; ladder reconciles to total debt; the scorecard code never reads the agency-ratings file. |
| 3 | Filing text and retrieval | Search a company's filings from the command line and see ranked passages with section and link. | BM25 scores match a hand-computed toy example; chunk offsets reproduce the source text; section parser on saved filings; index build is deterministic. |
| 4 | Model client, memo, three-layer verification | Capability probe results for three models; a memo with verdicts and checklist for three companies. | Fake-client tests of the interface; placeholder rendering; the digit validator; quote check; checklist assembly; deliberately corrupted claims are caught. |
| 5 | Evals and model choice | A results table per model; you label a blind sample of claims and choose the writer. | Metric functions on hand-built cases; label sheet hides model identity; results reproduce from saved outputs. |
| 6 | Watchlist and publishing pipeline | A simulated new filing produces flags and marks the memo stale; a rerun with nothing new changes nothing. | Flag thresholds; new-filing detection against mocked EDGAR responses; idempotency. |
| 7 | Live API, placeholder interface, preview deploy | The full click-through locally and on a Vercel preview URL. | Endpoint validation; failed claims are removed from answers; every published JSON file validates against its schema; frontend type-check. |
| 8 | Strategy artifacts and About page | Six artifacts readable in the app. | Every number in an artifact traces to a results file or to a timing you recorded. |
| 9 | Implement your Claude Design handoff | The designed interface on the same data. | Same contract tests; visual check against the handoff. |
| 10 | Production deploy, MODEL_CARD.md, RESULTS.md | The live link; the 11th rapid request to the AI endpoint gets a 429. | Smoke test against production; the built frontend contains no secrets. |

**Cut line if time runs short:** phase 9 can be dropped and the placeholder interface shipped. Phases 1 to 5 are the substance.

## Repo layout

```
PLAN.md  CLAUDE.md  NOTES.md  ASSUMPTIONS.md  LIMITATIONS.md  MODEL_CARD.md  RESULTS.md
pyproject.toml  vercel.json  .env.example
planning/                 this plan, the design brief, the Opus prompt
api/index.py              Vercel entry point (FastAPI: /api/ask, /api/health)
sourcebound/
  edgar/                  client (User-Agent, throttle, cache), facts, filings, sections
  engine/                 concepts + fallback chains, periods, ratios, ladder, lineage
  scorecard/              grid (thresholds as data), scoring
  retrieval/              chunking, BM25, index build and load
  llm/                    provider interface, schemas, prompts
  memo/                   section specs, drafting, placeholder rendering
  verify/                 number trace, quote check, judge, checklist
  watchlist/              new-filing detection, flags
  pipeline/               command-line entry points, export of static JSON
  contracts.py            Pydantic models: the single source of the data contract
config/                   companies.yaml, concepts.yaml, grid.yaml, prices.yaml
evals/                    golden/, labels/, agency_ratings.csv, timings.csv, results/
data/raw/ (ignored)       EDGAR cache
data/published/           static JSON shipped to the site
docs/strategy/            the six artifacts
web/                      React + Vite + TypeScript
tests/  .github/workflows/
```

## Data sources

| Source | Used for |
|---|---|
| `data.sec.gov/api/xbrl/companyfacts/CIK##########.json` | Every financial figure |
| `data.sec.gov/submissions/CIK##########.json` | Filing list, accession numbers, new-filing detection |
| `www.sec.gov/Archives/edgar/data/...` | 10-K and 10-Q text |
| `www.sec.gov/files/company_tickers.json` | Ticker to CIK lookup |
| Agency ratings | Entered by you, by hand, with source and date |

EDGAR allows 10 requests per second with a declared User-Agent. The client throttles to 5 and reads the User-Agent from an environment variable, so your contact details never enter the repo.

## The scorecard (approved 17 November 2026)

This is a stylised method of your own. It uses financial ratios only, and it is frozen at the end of phase 2, before any comparison with agency ratings. With 15 companies you cannot both tune and test.

| Factor | Weight | Score 1 | 2 | 3 | 4 | 5 | Score 6 |
|---|---|---|---|---|---|---|---|
| Debt / EBITDA | 20% | under 1.0x | 1.0–2.0 | 2.0–3.0 | 3.0–4.5 | 4.5–6.5 | over 6.5x, or EBITDA ≤ 0 |
| Net debt / EBITDA | 10% | under 0.5x or net cash | 0.5–1.5 | 1.5–2.5 | 2.5–4.0 | 4.0–6.0 | over 6.0x, or EBITDA ≤ 0 |
| EBITDA / interest | 25% | over 15x | 10–15 | 6–10 | 3.5–6 | 2–3.5 | under 2x |
| FCF / debt | 20% | over 40% | 25–40 | 15–25 | 8–15 | 0–8 | negative |
| Liquidity sources / uses | 15% | over 2.5x | 2.0–2.5 | 1.5–2.0 | 1.2–1.5 | 1.0–1.2 | under 1.0x |
| Debt due in 24 months ÷ (cash + undrawn revolver) | 10% | under 0.25 | 0.25–0.5 | 0.5–0.75 | 0.75–1.0 | 1.0–1.5 | over 1.5 |

The weighted score maps to grades SB-1 (1.5 or below) through SB-6 (above 5.5), in steps of 1.0. A score of 3.5 or below counts as "IG-like" for the agency comparison. The grades deliberately avoid agency letter symbols.

## Companies (approved 17 November 2026)

All are US non-financial filers. Banks, insurers and companies with large captive finance arms are excluded, because debt / EBITDA is meaningless for them. The rating buckets are my recollection, not data: you look up and enter the real ratings.

| # | Company | Ticker | Sector | Expected bucket | Why it is here |
|---|---|---|---|---|---|
| 1 | Walmart | WMT | Retail | IG | January fiscal year-end; **golden set; phase 1** |
| 2 | Verizon | VZ | Telecom | IG | Large debt load, detailed maturity table; **golden set; phase 1** |
| 3 | Goodyear | GT | Autos | HY | **Golden set; phase 1** |
| 4 | HCA Healthcare | HCA | Healthcare | IG, low end | Leveraged; **golden set** |
| 5 | Carnival | CCL | Leisure | HY or crossover | November year-end; **golden set** |
| 6 | Microsoft | MSFT | Technology | IG, top | Net cash case |
| 7 | Procter & Gamble | PG | Consumer | IG | June year-end |
| 8 | ExxonMobil | XOM | Energy | IG | Cyclical earnings |
| 9 | Union Pacific | UNP | Transport | IG | Stable, capital-heavy |
| 10 | Oracle | ORCL | Technology | IG, low end | May year-end, heavy borrowing |
| 11 | Kohl's | KSS | Retail | HY | Pairs with Walmart |
| 12 | American Airlines | AAL | Transport | HY | Pairs with Union Pacific |
| 13 | Cleveland-Cliffs | CLF | Materials | HY | Recent losses test the "not meaningful" path |
| 14 | Caesars Entertainment | CZR | Gaming | HY | High leverage |
| 15 | Community Health Systems | CYH | Healthcare | HY, low end | Pairs with HCA |

Alternates: Boeing, Macy's, Occidental, Charter. Sirius XM and Paramount are avoided because recent mergers created new registrants with short filing histories.

## Simplifying assumptions

1. **EBITDA** is operating income plus depreciation and amortisation, with no adjustments. Companies' own "adjusted EBITDA" is not in XBRL.
2. **Debt** is reported borrowings. Operating leases, pensions and guarantees are excluded; agencies adjust for these, which is one reason your grades will differ from theirs.
3. Each period uses the **most recently filed value**, so restatements overwrite originals. The accession number records which filing supplied it.
4. **LTM** is the latest fiscal year, plus the current year-to-date, minus the prior-year year-to-date.
5. **Liquidity** uses trailing cash flow as a stand-in for the next 12 months. Undrawn revolver capacity counts only if the company tagged it.
6. The **maturity ladder** comes from the annual 10-K. Between 10-Ks only the current portion updates.
7. An optional component with no reported fact (short-term investments, dividends) is treated as zero, and every such case is logged and shown to the reviewer.
8. The narrative corpus is the latest 10-K plus later 10-Qs. No 8-Ks, earnings calls or news.
9. The judge is a language model. Its verdicts are estimates, calibrated against your labels.
10. Reviewer sign-off in the interface is a demonstration, stored in the browser only.
11. A memo is a dated snapshot. After a new filing the watchlist shows fresh ratios and the memo is marked stale until you regenerate and review it.
12. Public data only, no user accounts, not investment advice.

## Risks and handling

| Risk | Handling |
|---|---|
| Companies tag the same concept differently | Ranked fallback chain per concept; every fallback logged; a tag-discovery report in phase 1 shows which candidate tags each company uses. |
| A figure sits under a company-specific tag, which the API omits | Reported as "not available". Never estimated. Goes on the reviewer checklist. |
| `LongTermDebt` sometimes includes the current portion, sometimes not | Reconciliation checks (non-current + current against the total; ladder sum against total debt). Mismatches over 5% are flagged. |
| The API's fiscal-year fields describe the filing, not the fact | Period logic uses start and end dates only. |
| Cash-flow figures in 10-Qs are year-to-date | The LTM formula checks that the three windows line up before computing. |
| Negative or zero EBITDA | Ratio shown as "not meaningful" and scored in the worst band. |
| Mergers break trends | Revenue change above 40% year on year raises a "possible structural change" note. |
| Per-company fixes creep in silently | Overrides live in one file, each with a written reason, and each appears on the checklist. |
| Filing HTML is inconsistent; section detection can fail | Section-coverage report for all 15; fallback to unlabelled chunks; parser tests on saved filings. |
| Model writes a wrong figure | Placeholders plus the digit validator. |
| Citation does not support the claim | Exact-quote check, then the judge. |
| The judge is wrong | Agreement and false-pass rate measured against your labels; seeded corrupted claims must be caught. |
| Sail outage or model retirement | Retries with backoff; model IDs pinned and recorded; static content is unaffected by an outage. |
| Scheduled GitHub jobs can be disabled after 60 days of repo inactivity | A weekly heartbeat commit updates the "last checked" date. I am not certain bot commits count as activity, so re-enabling is one click if not. |
| Vercel Hobby may refuse deploys triggered by bot commits | Opus verifies in phase 6; fallback is a Vercel deploy hook. |
| Public abuse of the AI endpoint | Firewall rule, input and output caps, and a small prepaid Sail balance with auto-recharge off. |
| Redistribution terms on agency ratings | By default the site shows only aggregate agreement. You decide whether to show per-company ratings. |

## Golden-set template

Fill in the "Value in filing" column from the 10-K **before** looking at the tool's output. A script adds the tool's columns afterwards.

```
Company: ________  Ticker: ____  Form 10-K, fiscal year ended: ________
Accession no.: ____________________  Filed: ________  Units in filing: ________
Verified by: ________  Date: ________

 #  Item                                   Where to look                         Value in filing   Page/note
 1  Revenue                                Income statement, top line
 2  Operating income                       Income statement
 3  Depreciation and amortisation          Cash flow statement, operating
 4  Interest expense                       Income statement or interest note
 5  Cash and cash equivalents              Balance sheet
 6  Short-term investments (0 if none)     Balance sheet
 7  Short-term borrowings + current        Balance sheet, current liabilities
    portion of long-term debt
 8  Long-term debt excl. current portion   Balance sheet
 9  Cash from operations                   Cash flow statement
10  Capital expenditure                    Cash flow statement, investing
11  Dividends paid (0 if none)             Cash flow statement, financing
12  Undrawn revolver capacity              Liquidity section or debt note
13-18  Debt due in year 1, 2, 3, 4, 5, later   Debt note, maturity table

By calculator, from your own values:
D1  EBITDA = 2 + 3                  D5  EBITDA / interest = D1 / 4
D2  Total debt = 7 + 8              D6  FCF / debt = (9 - 10) / D2
D3  Debt / EBITDA = D2 / D1         D7  Sources / uses = (5 + 6 + 12 + 9) / (13 + 10 + 11)
D4  Net debt / EBITDA = (D2 - 5 - 6) / D1

Pass rule: inputs match after rounding to the filing's unit; ratios within 0.05x or 1 percentage point.

Fact questions (answer + exact section and page):
Q1  Size and expiry of the main revolving credit facility
Q2  Financial covenants, and whether the company states it complies
Q3  Largest single debt maturity in the next three years
Q4  Management's stated sources of liquidity
Q5  The risk factor most relevant to repaying debt
```

Phase 5 adds two more sheets. The first is a blind claim-labelling sheet: about 180 rows, each with a claim, its cited passage and your verdict. The second is a timing log for the manual-versus-tool comparison.

## What only you can do

- Put `SAIL_API_KEY` and `EDGAR_USER_AGENT` in `.env`. Never paste either into chat.
- Hand-verify five companies and label the claim sample.
- Enter agency ratings and record your own timings.
- Create the GitHub repo and the Vercel project.
- Produce the design in Claude Design.

## Sources

- [Fed SR 26-2: Revised Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), and its [attachment](https://www.federalreserve.gov/supervisionreg/srletters/SR2602a1.pdf), read in full
- [OCC Bulletin 2026-13](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html)
- [FDIC FIL-15-2026](https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance)
- [OCC Bulletin 2026-54](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-54.html) (summary only)
- [Sail Research docs](https://docs.sailresearch.com): models, pricing, support, migrate, service-tiers, rate-limits, retries, security
- Vercel docs: [limits](https://vercel.com/docs/limits), [Python runtime](https://vercel.com/docs/functions/runtimes/python), [FastAPI](https://vercel.com/docs/frameworks/backend/fastapi), [cron pricing](https://vercel.com/docs/cron-jobs/usage-and-pricing), [WAF rate limiting](https://vercel.com/docs/vercel-firewall/vercel-waf/rate-limiting)
