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
