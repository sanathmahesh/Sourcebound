# Decision log

Each entry: the decision, why, and the alternatives rejected. Entries D1–D10 are seeded from PLAN.md
section 4.2 (fixed before building started, 17 November 2026). Later entries were made while building and
say which phase made them. Where the plan named no rejected alternative, the entry says so rather than
inventing one.

## Fixed in the plan (PLAN.md 4.2)

### D1. Backend Python 3.12, FastAPI, pandas, pytest; frontend React, Vite, TypeScript
- **Why:** mainstream, readable stacks that the author can explain; Python is the natural home for
  financial data handling and evaluation code; FastAPI runs as a Vercel Python function.
- **Rejected:** none recorded in the plan.

### D2. Inference through Sail Research, behind one interface configured by environment variables
- **Why:** an OpenAI-compatible API giving access to several open-weight models from different labs at
  low list prices, with paid credit already in place. One interface means the model is a config value.
- **Rejected:** the Claude API (the plan fixes Sail as the provider).

### D3. Three writer models: zai-org/GLM-5.3, deepseek-ai/DeepSeek-V4-Pro-0813, deepseek-ai/DeepSeek-V4.1-Flash-1017
- **Why:** two mid-priced models from different labs and one very cheap one, so the recommendation can
  show a cost-against-accuracy trade-off.
- **Rejected:** none recorded in the plan.

### D4. Numbers by placeholder
- **Decision:** the model writes tokens such as `{{m:net_leverage:LTM}}` and code substitutes the value.
- **Why:** a figure the model never types cannot be mistyped; every printed number traces to the engine.
- **Rejected:** letting the model copy numbers from a table, because copying errors are silent.

### D5. The memo is a fixed pipeline, not an agent
- **Why:** the same retrieval steps every time make the memo auditable and repeatable. Only the live
  follow-up endpoint uses a bounded tool loop (two read-only tools, at most three rounds), because
  questions are open-ended.
- **Rejected:** an agentic memo writer that chooses its own lookups (not auditable or repeatable).

### D6. Retrieval: our own BM25 plus routing by filing section; index shipped as JSON files
- **Why:** Sail serves no embedding model; BM25 is small enough to explain line by line and needs no
  second vendor. Retrieval recall is measured in the evals; embeddings are proposed only if measured
  recall is poor.
- **Rejected for now:** local embeddings (large serverless bundle, slow cold starts); a second embedding
  vendor (a second key and provider).

### D7. Hosting: Vercel Hobby, own project, static frontend plus FastAPI as a Python function
- **Why:** free tier, CDN for static JSON, one Python function for the live endpoint. Nothing is held in
  memory between requests; memos, verification reports and the watchlist are generated ahead of time and
  shipped as static JSON with filing dates shown.
- **Rejected:** none recorded in the plan.

### D8. Watchlist refresh: a daily GitHub Actions job with no model call; memo marked stale until regenerated locally and reviewed
- **Why:** the Sail key stays only in Vercel and on the author's laptop, and no memo is published without
  human review, which matches the project's own control story.
- **Rejected:** Vercel Cron (functions cannot write files); automatic memo regeneration (publishes
  unreviewed output).

### D9. Rate limiting: a Vercel Firewall rate-limit rule keyed by IP on /api/ask
- **Why:** no database needed.
- **Rejected:** none recorded in the plan.

### D10. Interface designed separately in Claude Design
- **Decision:** build the data contract first, then a plain placeholder interface, then implement the
  handed-off design in a later phase.
- **Why:** the contract is the stable part; the design can change without touching the engine.
- **Rejected:** none recorded in the plan.

## Made while building

### D11. EDGAR client on httpx with a disk cache that mirrors the URL (phase 1)
- **Why:** httpx has a built-in mock transport, so throttle, retry and cache behaviour is tested with no
  network. Mirroring the URL makes the cache inspectable by hand; a sidecar file records the fetch time,
  which becomes the data date in reports.
- **Rejected:** `requests` (needs an extra mocking library); the standard-library `urllib` (no bundled
  certificates on this machine's Python, and harder to mock).

### D12. Plain dataclasses in the engine instead of pandas for phase 1
- **Why:** a company has a few thousand facts; explicit loops over small dataclasses are easier to walk an
  interviewer through than DataFrame operations. pandas stays in the stack for tabular work where it earns
  its place (coverage reports, evals).
- **Rejected:** loading company facts into a DataFrame.

### D13. Periods anchored on the 10-K's report date and identified by fact dates
- **Why:** the submissions API states the period each filing covers; fact start and end dates are the
  only reliable description of a fact's period.
- **Rejected:** the API's fy/fp fields (they describe the filing, not the fact); the frames API
  (calendar-aligned to within 30 days, which blurs non-calendar fiscal years).

### D14. One tag per LTM value
- **Why:** mixing tags across FY0, current YTD and prior YTD could add numbers with different scopes.
- **Rejected:** falling back window by window.

### D15. Debt reconciliation compares every total-debt candidate, warning above 5%
- **Why:** a tag can cover less than its name suggests. On real data this caught Walmart's rank-1 tag
  omitting short-term borrowings. The check changes no value; it puts the gap in front of the reviewer.
- **Rejected:** trusting rank 1 silently; auto-switching to the larger candidate (that would be a silent
  substitution).

### D16. Phase-1 reports written to reports/ and committed
- **Why:** the hand check needs files that can be diffed across runs. reports/ is not in the plan's
  layout; it holds human-readable check reports, separate from data/published/ (the site's JSON).

### D17. Test fixtures are trimmed captures plus the script that made them
- **Why:** the full responses for three companies are about 13 MB. The capture keeps every chain tag from
  2021 on, unmodified, with the source URL and fetch time; the script makes the trimming reproducible.
- **Rejected:** committing full responses; hand-written fixtures of real companies (not traceable).

### D18. Chain revision 1: finance leases count as debt; components before combined tags (approved 17 November 2026)
- **Decision:** (1) total debt prefers balance-sheet components, adds a candidate pairing
  LongTermDebtAndCapitalLeaseObligations with short-term debt, and moves DebtLongtermAndShorttermCombinedAmount
  to last; (2) finance-lease liabilities count as debt for every company, and finance-lease interest is
  added when only InterestExpenseDebt is reported; (3) capex adds PaymentsToAcquireOtherProductiveAssets
  (Verizon); (4) revenue ranks Revenues (total revenue) first.
- **Why:** the phase-1 tag-discovery and reconciliation reports showed the starting chains understated
  Walmart's debt (the combined tag omits its $6,596m of short-term borrowings at FY0), could not produce
  Verizon's LTM debt or any Verizon capex, and treated finance leases differently by company (inside
  Verizon's and Goodyear's debt lines, separate for Walmart at $6,761m). Finance leases are economically
  borrowings, and credit analysts normally count them as debt.
- **Effect at FY0:** Walmart total debt $38,166m -> $51,523m; Goodyear $5,937m -> $6,198m (its balance-sheet
  total); Verizon unchanged at $158,150m. Verizon's LTM debt ($166,233m) and capex ($17,011m in FY0) became
  available.
- **Consequence for phase 2:** the golden-set template needs a finance-lease row, so a hand-computed total
  debt follows the same definition.
- **Rejected:** debt exactly as each balance sheet presents it (inconsistent across companies); excluding
  finance leases everywhere (needs subtraction from combined tags, and understates debt-like obligations).

### D19. Chain revision 2 (approved 17 November 2026, phase 2)
- **Decision:** net-interest tags (InterestIncomeExpenseNonoperatingNet, InterestIncomeExpenseNet), sign
  flipped and flagged, rank above the cash-interest-paid proxy; amortisation is optional beside
  Depreciation; short-term debt adds LongTermDebtAndCapitalLeaseObligationsCurrent and NotesPayableCurrent,
  and counts as zero when nothing is reported; total debt adds LongTermNotesAndLoans + short-term debt +
  finance leases; the year-1 maturity falls back to the balance-sheet current portion of long-term debt.
- **Why:** the tag-discovery run over all 15 companies showed these were the tags actually used by Union
  Pacific (depreciation only), Kohl's, Cleveland-Cliffs, Community Health and Caesars (net interest), Oracle
  (notes payable), Union Pacific and Community Health (current debt), and HCA (no year-1 maturity tag).
  Afterwards every core ratio is available for every company.
- **Rejected:** keeping the cash-interest-paid proxy (cash paid can differ from expense by timing); leaving
  short-term debt "not available" when untagged (companies usually omit a nil line; the checklist shows each
  assumed zero, so a wrong zero is caught).

### D20. ExxonMobil uses its predecessor registrant (override, approved 17 November 2026)
- **Decision:** config/overrides.yaml maps XOM to Exxon Mobil Corp (CIK 34088) instead of the new holding
  company ExxonMobil Holdings Corp (CIK 2115436), with the written reason; the override is on XOM's checklist.
- **Why:** the new registrant (from 1 July 2026, Form 8-K12B) has no 10-K yet; the predecessor has every
  annual report. Its XBRL data runs to the 10-Q for 31 March 2026 (the June 10-Q's facts sit under the new
  CIK), so XOM's latest figures are about six months older than most companies'.
- **Rejected:** swapping in Occidental; dropping to 14 companies; merging two registrants' facts (more code,
  harder to explain; revisit when the new registrant files its first 10-K).

### D21. One definition of "debt due within 12 months"; ladder metrics as of FY0
- **Decision:** debt due within 12 months is the balance sheet's short-term debt (short-term borrowings plus
  the current portion of long-term debt), used in liquidity coverage and in debt due within 24 months
  (= short-term debt + ladder year 2). Near-term maturity cover divides that by cash + short-term investments
  + undrawn revolver. The ladder metrics are as of FY0, from the 10-K's maturity table.
- **Why:** the balance sheet updates every quarter and includes commercial paper, which the maturity table
  leaves out; one definition everywhere keeps the golden-set formulas and the engine identical.
- **Rejected:** the maturity table's year 1 (omits short-term borrowings; annual only).

### D22. Scorecard rules beyond the plan's grid
- **Decision:** a value exactly on a threshold takes the worse band (approved 17 November 2026). Statuses
  without a value map to fixed bands: EBITDA <= 0 -> 6 on leverage, net leverage and coverage; net cash -> 1;
  no uses of cash -> 1 on liquidity; debt due with no cash or revolver -> 6; zero debt -> 1 on every
  debt-related factor. Interest <= 0 with debt outstanding is not scored. The "latest" grade uses LTM
  ratios and the FY0 near-term maturity cover; an FY0 grade is computed too (for the phase-6 grade-change flag).
- **Why:** the plan's grid notation ("<1.0", "1.0-2.0", ">6.5") leaves exact boundaries ambiguous; a single
  conservative rule is easy to state and test. Fixed bands for special statuses follow the plan's own
  "EBITDA <= 0" and "net cash" entries.
- **Rejected:** "better band" on ties; scoring "not meaningful" as not available (would hide distress).

### D23. Trend direction rule
- **Decision:** direction from FY-2 to LTM; "stable" within 10% of the FY-2 value (and at least 0.1x) for
  multiples, within 2 percentage points for percentages.
- **Why:** a simple, explainable rule that ignores noise. Not tuned on any result.

### D24. Use the newest filing that has facts; flag skipped ones
- **Decision:** the latest 10-K and 10-Q are the newest that have facts in the company's XBRL data; a newer
  filing without facts is skipped and logged as stale data (on the checklist).
- **Why:** facts can lag a new filing, or sit under another registrant (ExxonMobil). Without this, LTM failed
  and XOM's "latest" grade rested on one factor of six.

### D25. Published metrics contract
- **Decision:** contracts.py (Pydantic) defines metrics.json. Metrics are keyed "<metric_id>:<period>" to
  match memo placeholders; every metric carries its XBRL inputs; an assumed-zero value is exported as status
  ok with a note; the checklist groups repeated log entries into one item naming the periods.
- **Why:** one source of truth for the site and the memo; every number traceable from the JSON alone.

### D26. Golden-set sheets
- **Decision:** generated blank from the latest 10-K, never overwritten once they exist; a finance-lease row
  (D18) and derived formulas identical to the engine's definitions.
- **Why:** the author's values must be independent of the tool's, and both must measure the same thing.

### D27. Chain revision 3: finance-lease current portion optional (approved 17 November 2026)
- **Decision:** in the finance-lease sum, FinanceLeaseLiabilityCurrent is optional (assumed zero, logged).
- **Why:** Caesars tags about $13.1bn of non-current finance-lease liabilities with no current-portion tag,
  so they were left out of its debt while their interest was in its interest expense. Tested on all 15
  companies before approval: only Caesars changes (LTM debt $11,558m -> $24,746m; debt / EBITDA 3.6x ->
  7.7x; SB-4 -> SB-5). Chain changes do not touch the frozen grid (grid-v1).

### D28. Text extraction with the standard-library HTML parser (phase 3)
- **Why:** about 60 readable lines, no dependency, 0.1 s per filing; handles inline XBRL by skipping the
  hidden header and display:none elements.
- **Rejected:** BeautifulSoup/lxml (more dependencies for no gain here); an LLM (cost, variance, untestable).

### D29. Rule-based section detection, every rule tied to a real filing
- **Decision:** headings only; titled beats bare; most text before a different item; 10-Q part from title;
  debt note by numbered heading with a debt title, ending at the next note number, searched across the
  document outside narrative sections; joint filers' statement items labelled from their titles.
- **Why:** deterministic and testable; the section-coverage report over all 15 companies drove each rule.
  Where rules fail, text stays unlabelled rather than guessed.

### D30. BM25 index as one JSON file per company in data/index/, committed
- **Decision:** passages, statistics and inverted index in one file (about 21 MB for 15 companies);
  deterministic bytes; the loader imports neither the EDGAR client nor pandas.
- **Why:** the live API (phase 7) needs the index at run time with no network and no state between
  requests. data/index/ is not in the plan's layout; it is separate from data/published/ because the site's
  pages never load it.
- **Rejected:** building the index at request time (slow, needs EDGAR); a database (none needed).

### D31. Saved filing texts as test fixtures
- **Decision:** three extracted texts (WMT 10-K, GT 10-K, VZ 10-Q), gzipped, with their source URLs.
- **Why:** section tests run against real filings without network access; gzip keeps them to 280 KB.

### D32. Chat Completions API, although Sail now labels its Responses API "recommended" (phase 4)
- **Why:** the plan fixed Chat Completions; Sail still lists it as stable, and it supports everything
  needed (json_schema structured output, strict function tools, service tier, reasoning effort). Re-read
  17 November 2026: `max_completion_tokens` is the output limit (`max_tokens` is rejected); `seed`, `stop`
  and `logprobs` are unsupported, so run-to-run spread is measured instead.
- **Rejected for now:** switching to the Responses API (no capability the project needs; one more change).

### D33. Idempotent retries; the OpenAI SDK's own retries switched off
- **Why:** Sail's retry guidance (re-read 17 November 2026) says only 429s and capacity 503s are refused
  before work starts; other errors may have started a generation, so a blind retry can pay twice. Every
  call sends an Idempotency-Key and reuses it on each retry (backoff: Retry-After, else 1, 2, 4 s + jitter;
  at most 4 attempts).

### D34. Tools and the answer format go in separate requests (approved 17 November 2026)
- **Decision:** the follow-up endpoint (phase 7) runs its lookup turns with tools only, then asks for the
  structured answer in a separate request with the response schema and no tools.
- **Why:** the capability probe (docs/sail-capability-probe.md, run twice) found GLM-5.3 and
  DeepSeek-V4-Pro skip the tool and invent a number when tools and a response schema share a request;
  DeepSeek-V4.1-Flash does not. The separated pattern passed for all three. Memo drafting and judging use
  structured output only, which all three pass.
- **Rejected:** dropping the two models (loses the cost-against-accuracy comparison); trusting combined
  requests (they produced fabricated numbers).

### D35. One reasoning-effort setting per role, the same for every model
- **Decision:** writer "medium", judge "low" (config/models.yaml); GLM-5.3 rejects "none".
- **Why:** comparable settings make the model comparison fair; the judge's task is narrow.

### D36. The judge also sees the engine values behind a claim's placeholders
- **Why:** a claim such as "leverage rose to {{m:...}}" has no passage to cite; giving the judge the
  values lets it catch a wrong direction or comparison. Passages are still the evidence for everything else.

### D37. A memo embeds only what it uses
- **Decision:** memo.json holds the metrics its claims, ladder and scorecard reference, and the passages its
  claims cite, so it is a self-contained dated snapshot; the full metric set stays in metrics.json.

### D38. Every model request and response is saved (data/runs/<TICKER>/<run>.jsonl)
- **Why:** results can be recomputed and audited without new model calls (PLAN.md 4.11); the API key is
  never in the request body, and a test checks the saved file does not contain it.

### D39. Judge evidence carries period dates; rating-rationale claims are judged against the scorecard
- **Why:** the first Walmart memo (run WMT-20261118, GLM-5.3) had true claims marked "partially supported"
  only because the judge saw "Revenue, FY-2" without the date it stands for, and a false rationale claim
  (that the grade was provisional) passed as "partially supported" because the judge never saw the
  scorecard. The writer is now told explicitly whether the grade is provisional.
- **Effect:** the first run's outputs are kept in data/runs/ for comparison; memos are regenerated.

### D40. Evaluation runs are resumable and recomputable (phase 5)
- **Decision:** eval memos go to evals/results/memos/<writer>/run<n>/ and are skipped if present; the report
  reads only saved files; judge candidates and seeded errors replay the saved drafts.
- **Why:** an interrupted run never pays twice, and every number can be recomputed without new model calls.

### D41. Golden sheets get a quote column for the fact questions (phase 5)
- **Why:** retrieval recall needs to know which passage the author located; a page number cannot be matched
  to a passage, a short copied quote can. The sheets were regenerated before the author had edited them.

### D42. Agency ratings: one rank per company, averaged across the agencies entered
- **Why:** the author may enter one, two or three agencies; averaging their positions on one scale (AAA/Aaa
  = 1 ... D/C = 22) keeps every company in the comparison. IG = BBB-/Baa3 or better.

### D43. Writer output limit raised from 8,000 to 16,000 tokens (approved 18 November 2026)
- **Why:** in the first golden runs DeepSeek-V4-Pro's reasoning (medium effort) used the whole 8,000-token
  limit in 11 draft calls (finish_reason "length", empty or cut-off answers), forcing repairs and leaving one
  memo section without a draft; GLM-5.3 and DeepSeek-V4.1-Flash never reached it. The limit was measuring my
  setting, not the model. The same limit applies to every writer.
- **Effect:** DeepSeek-V4-Pro's five golden run-1 memos were regenerated; the capped versions are kept in
  evals/results/superseded/ with their raw outputs in data/runs/. GLM-5.3 and Flash memos are unaffected.

### D44. The watchlist job triggers a Vercel deploy hook after committing (phase 6)
- **Why:** Vercel's docs (troubleshoot-project-collaboration, last updated 13 March 2026; KB guide, 16 October
  2026) say a Hobby team deploys only commits whose author is the team owner, so the job's bot commits would not
  deploy. A deploy hook (a secret URL, stored as a GitHub secret; Hobby allows 5 per project, 60 calls an hour)
  starts the deploy instead. To be confirmed once the repository and project exist.
- **Rejected:** authoring bot commits as the owner (blurs who changed what); Vercel Cron (cannot write files).

### D45. Staleness is an event, not a comparison
- **Decision:** the job marks a memo stale when it sees a new filing; regenerating the memo marks it current.
- **Why:** simple to explain and to test, and it matches the review step: a stale memo stays stale until a
  human has regenerated and reviewed it.

### D46. Published memos come from the GLM-5.3 evaluation run until the models are chosen
- **Why:** they are already verified, so publishing them costs nothing; once the author chooses the writer and
  judge, build-all regenerates (or copies the chosen writer's run and re-judges it) in one command.

### D47. Deploy layout: one Python function for /api, the Vite build as static files (phase 7)
- **Decision:** `api/index.py` exposes the FastAPI app; `vercel.json` rewrites `/api/*` to it, builds `web/`
  and serves `web/dist` (with the published JSON copied to `dist/data`). The function may run 75 seconds, so the
  app's own 60-second limit answers first with a plain 503.
- **Why:** Vercel's docs, re-read 18 November 2026, still detect FastAPI from an `app` object in a standard
  entry file (app.py, index.py, server.py, main.py at the root, in src/ or app/, or `tool.vercel.entrypoint`)
  and recommend a newer "Services" setup for a frontend plus backend, without saying whether Hobby has it. The
  plan's default layout uses only long-standing features. Unverified until a preview deploy (needs approval).
- **Rejected:** Services (Hobby availability unknown); a FastAPI app at the root (Vercel would treat the whole
  project as a Python app).

### D48. A live answer keeps only claims the judge marks supported
- **Decision:** `/api/ask` runs the memo's checks on every claim and keeps only "supported"; partly supported
  and unsupported claims go to the "removed" list with the reason.
- **Why:** a memo is reviewed by a person before publication and its partly supported claims are marked and
  listed; a live answer is read straight away with no reviewer, so the bar is higher.

### D49. Follow-up limits sized for 60 seconds
- **Decision:** at most 3 lookup rounds, 3 lookups per round, 5 passages per search, 5 claims; writer reasoning
  effort low with a 4,000-token cap; judges run in parallel; each model request times out at 45 seconds with
  one retry. The final answer always comes from a schema-only request, even when the model stops looking
  things up early (D34 applied strictly).
- **Evidence:** a two-round Walmart question took 18.3 s and an out-of-scope one 2.5 s (GLM-5.3, 18 November
  2026, one run each, so indicative only).

### D50. The data contract is exported as one JSON Schema; TypeScript types are generated from it
- **Decision:** `pipeline/export_schema.py` writes `web/src/contracts/schema.json` from the Pydantic models
  (published files in serialization mode, with defaulted fields marked required because they are always
  written; the request body in validation mode); `json-schema-to-typescript` generates `types.ts`. Tests fail if
  either is out of date, and every published file is validated against its model.
- **Why:** contracts.py stays the single source of the shapes, and a contract change cannot silently break the
  interface.

### D51. The interface formats numbers exactly as the Python engine does
- **Decision:** `web/src/format.ts` mirrors `format_metric`, rounding like Python (the double's exact value,
  ties to even); a test compares it with every metric chip in the 15 published memos.
- **Why:** the first version used JavaScript's `toFixed`, and the test caught HCA's FY0 debt ($47.25 billion)
  reading "$47.3 billion" in a table and "$47.2 billion" in the memo.
- **Rejected:** publishing a display string for every value (a contract change; can be proposed for phase 9).

### D52. Plain React with hash routing; the npm lockfile is generated with npm 12.2.1
- **Decision:** no router or component library (phase 9 replaces the look); routes are URL hashes, so the static
  host needs no rewrite rules. Exact versions, each at least two weeks old on 18 November 2026. The lockfile was
  generated with npm 12.2.1 via npx because the installed npm 10.9.3 crashes on this dependency set (an internal
  error in its peer-dependency resolver); installs use `npm ci`, which reads the lockfile and works on npm 10.

### D53. Strategy artifacts are rendered from templates, like the memos (phase 8)
- **Decision:** artifacts 1 to 5 are templates in docs/strategy/templates/ whose figures are placeholders filled
  from evals/results/results.json and evals/timings.csv; a test fails if any other digit appears (identifiers
  and list numbering aside). The decision log stays hand-written. The method page is generated from
  config/grid.yaml and the engine's formula strings. All of it is published as about.json.
- **Why:** the plan requires that every number in an artifact matches a results file or the timing log; making
  it impossible to type one is stronger than checking afterwards, and a re-run of the evaluation updates the
  documents with one command.
- **Rejected:** hand-written artifacts checked by a search for matching numbers (a typed number that happens to
  match a result would pass).

### D54. Opportunity-map ratings are words, and the model choice waits for the labels
- **Decision:** the map rates value, feasibility and risk as High, Medium or Low, labelled as the author's
  judgment for review. The model memo states a rule for choosing, written before the labels exist, instead of
  a choice.
- **Why:** numeric scores would look like measurements; and choosing a model before the human labels exist
  would rest on the provisional judge grading its own writing.

### D55. The control table cites the 2026 guidance only for vocabulary
- **Decision:** the risk and control table states the guidance's scope (its definition of a model, footnote 3,
  the $30 billion relevance line, no enforceable standards) before the table, and maps each control to a
  borrowed term; it claims no compliance.
- **Why:** read from the primary documents on 18 November 2026. The ratio engine is outside the definition and
  the generative parts are outside the scope, so a compliance claim would be false; the vocabulary is still how a
  bank's model-risk team would assess the tool.

### D56. The watchlist carries each headline ratio's change since the prior year-end (phase 9)
- **Decision:** a contract change, approved by the author on 18 November 2026 when the design handoff needed
  it: each watchlist item gains `changes`, Debt / EBITDA and EBITDA / interest at FY0 and LTM, their difference,
  how it reads ("+2.88x", "not meaningful") and whether a flag fired on that ratio. Computed in
  sourcebound/watchlist/flags.py next to the flag rules. The published watchlist.json was rebuilt offline from
  the published state and metrics, keeping checked_at; index.json was checked to be unchanged.
- **Why:** every figure comes from tested Python code; highlighting by the flags that fired avoids a second copy
  of the rule in the browser.
- **Rejected:** dropping the columns (loses the design's main signal), and computing them in the browser from 15
  metrics files (duplicated logic, more requests).

### D57. Where the interface departs from the handoff, and why
- **Decision:** the screens follow the handoff's tokens, type, layout, copy and interactions, except where the
  real data or the project's rules require otherwise:
  - The footer's "All companies and figures are fictional" is dropped (the data is real); the project's
    disclaimer appears on every page.
  - Every claim carries its verdict label, not only qualitative ones, because every claim was judged.
  - The citation drawer lists every passage a claim cites, each with whether its quote was found.
  - Multiples show two decimals, the engine's format, so a figure reads the same everywhere. Ratio tiles are
    20 pixels wider to fit those labels.
  - The chip key uses the word "figure" as its sample rather than invented numbers.
  - Routes stay hash-based with the handoff's path names (`#/memo/WMT`), so the static host needs no rewrites.
  - The Results screen keeps the measures the evaluation actually produces, in the handoff's table layout,
    each with its sample size and a "how measured" note.
  - The drawer gained focus trapping and Escape to close, which the handoff asked for.
  - On a phone the header's navigation sits on its own row under the wordmark, at the author's request (the
    prototype stacks the links in a column beside it).
- **Why:** the plan says to implement the design over the data contract without changing it, and never to show
  invented or false content.

### D58. Deployed to Vercel from the CLI, with the rate limit at the edge (phase 10)
- **Decision:** a Vercel project `sourcebound` on the author's Hobby plan, deployed with Vercel CLI 65.11.0
  (the newest release at least two weeks old on 18 November 2026). Five server settings (SAIL_*), the API key
  stored as a secret. A firewall rule on `/api/ask`: 10 requests per 600-second fixed window per IP address,
  then HTTP 429; the author approved publishing it. Address: sourcebound-app.vercel.app, the author's choice
  because sourcebound.vercel.app is taken.
- **Why:** the plan's phase 10; the CLI could do every step (environment variables, firewall, domains) and its
  facts were re-read on 18 November 2026: Hobby allows one rate-limit rule per project and functions up to
  300 seconds.
- **Checked live:** pages and data load; `/api/health` reports the settings present; bad requests get 400; a
  question was answered in about 15 seconds with every kept claim supported; an out-of-scope question was refused;
  the 11th request in a window got 429.
- **Rejected:** a rate limit inside the function (it would still run, and bill, for each request).

### D59. The public history uses GitHub's noreply address
- **Decision:** before the first push to the public repository, the author chose to replace the personal email
  on all commits and on the `grid-v1` tag with GitHub's noreply address; future commits in this repository use it
  too. File contents are unchanged (the final tree is identical).
- **Why:** a public commit history would otherwise publish the author's personal email.

### D60. RESULTS.md is generated, like the strategy artifacts; the model card joins the About page
- **Decision:** RESULTS.md is rendered from docs/templates/RESULTS.md with figures from results.json, and the
  build fails on any typed figure. It holds the plan's four measures per model (three pending the author's labels
  and hand-checked values) plus two code checks and the model time. MODEL_CARD.md is published on the About page
  with the limitations, as the design brief lists.
- **Why:** the plan allows RESULTS.md only measured numbers with sample size, date, model ID and command; filling
  them by code makes a mistyped figure impossible.

### D61. The daily job deploys with a Vercel token, not through a Git link
- **Decision:** the Vercel project is not linked to the repository. After committing new data, the watchlist
  workflow deploys a copy of the checkout (without .git) with Vercel CLI 65.11.0 and a token kept in GitHub's
  secrets (VERCEL_TOKEN, with VERCEL_ORG_ID and VERCEL_PROJECT_ID). A manual run can force a deploy. The author
  chose this on 18 November 2026.
- **Why:** the author's Vercel account is connected to a different GitHub user, which has no access to this
  repository, so Vercel refused the link. Deploying a copy without .git avoids Hobby's check on who authored a
  commit, since the data commits are made by a bot.
- **Rejected:** reconnecting the Vercel account's GitHub login (the author preferred not to change it); leaving
  new data undeployed until a manual deploy.
- **Note:** Vercel does not let a CLI login create tokens (HTTP 403), so the author creates the token in the
  dashboard.
- **Checked:** on 18 November 2026 a manual run with a forced deploy checked all 15 companies, found no new
  filings, and deployed to production from GitHub; the site, API and data then served from that deployment.

