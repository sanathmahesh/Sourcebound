# Study notes

My study guide to Sourcebound. For each part of the system: the finance or regulatory concepts in plain
English, why the part is built the way it is, and the interview questions I should be able to answer, each
with a short model answer. Sections are added as each phase is built.

## 0. The project in one paragraph

A **credit memo** is the written case a bank analyst makes about whether a borrower can repay its debt.
Sourcebound drafts one for a US public company from its SEC filings. Deterministic, tested code computes
every figure; a language model writes the prose around those figures; three checks prove where each number
and claim came from; anything unproven goes on a checklist for a human reviewer.

Phase 1 built the foundation: getting the numbers out of SEC filings correctly, and computing four core
credit ratios with a full trail back to the filing each number came from.

---

## 1. SEC EDGAR and XBRL (sourcebound/edgar/)

### Concepts in plain English

- **SEC**: the US Securities and Exchange Commission. Companies whose shares trade publicly in the US must
  file reports with it.
- **EDGAR**: the SEC's public database of those filings. Free, and has JSON APIs.
- **10-K**: the annual report. Audited financial statements, business description, risk factors,
  management's discussion and analysis (MD&A), and notes such as the debt footnote.
- **10-Q**: the quarterly report, filed for the first three quarters of the fiscal year (the fourth is
  covered by the 10-K). Unaudited. Income and cash-flow figures are often **year-to-date**.
- **Amendment (10-K/A, 10-Q/A)**: a correction or addition to an earlier filing.
- **Accession number**: the unique ID of one filing, e.g. `0000732712-26-000007`. It is the anchor of
  every lineage record in this project: given it, anyone can open the exact filing.
- **CIK** (Central Index Key): the SEC's ID for a filer. Walmart's is 104169. URLs need it padded to ten
  digits (`CIK0000104169`). We look CIKs up in SEC's `company_tickers.json`, never from memory.
- **XBRL**: machine-readable tags attached to each number in a filing. The tag says what the number is
  (`us-gaap:LongTermDebtNoncurrent`), the context says which period, and the unit says the currency.
- **us-gaap taxonomy**: the standard dictionary of tags for US GAAP accounts. Companies may also invent
  **extension tags** (e.g. a Verizon-only tag) when no standard tag fits.
- **Dimensions**: XBRL can break a number down by segment, product line and so on.
- **Company facts API** (`data.sec.gov/api/xbrl/companyfacts/CIK##########.json`): every standard-tag,
  non-dimensional fact a company has ever filed, with value, period dates, accession, form and filing date.
  It does *not* contain extension tags or segment breakdowns. Its `fy`/`fp` fields describe the *filing*
  a fact appeared in, not the fact's own period: a 10-K for 2025 reports 2023's revenue again as a
  comparative, and that 2023 fact carries `fy=2025`.
- **Submissions API** (`data.sec.gov/submissions/CIK##########.json`): the company's filing list, with
  form type, accession, filing date and **report date** (the period end the filing covers).
- **Fair access**: SEC asks automated users to stay at or under 10 requests per second and to send a
  User-Agent header naming who they are and how to contact them. Re-checked on 17 November 2026; the page
  has moved to https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data.

### Why it is built this way

- **One small client** (`edgar/client.py`) does the four polite things: refuses to run without a
  User-Agent containing an email; one request at a time with at least 0.2 s between request starts
  (5 per second, half the limit); retries 429 and 5xx with `Retry-After` or 1, 2, 4 s plus jitter, up to
  4 attempts; caches every response on disk at a path mirroring the URL, with a sidecar file recording
  when it was fetched. The fetch time becomes the "data date" in reports.
- **The User-Agent lives only in `.env`** and is read at run time. It is never logged or cached; a test
  checks the cache contains no email address.
- **Tests never touch the network**: `httpx.MockTransport` stands in for EDGAR, and a fake clock and fake
  sleep make throttle and backoff tests instant and exact.
- **Facts are flattened** into one `Fact` dataclass (tag, unit, value, start, end, accession, form,
  filed). `fy`/`fp` are deliberately dropped so nothing can use them by mistake.
- **Only 10-K, 10-Q and amendments** are used as sources. The company-facts API also includes facts from
  8-Ks and registration statements; a credit memo should rest on the periodic reports.

### Interview questions

**Q: Where does every number come from, and how would I find it myself?**
A: From the SEC's XBRL company-facts API. Each value records its tag, period dates, form, accession number
and filing date, plus a link to the filing's index page on EDGAR. Open the link, open the 10-K or 10-Q,
and find the line item for that period.

**Q: Why not scrape numbers from the HTML of the 10-K?**
A: XBRL is the company's own machine-readable tagging of the same statements, so it avoids table-parsing
errors. The trade-off is that the API omits extension tags and segment data, so some items are "not
available" and must be read from the text, which phase 3 handles for the narrative.

**Q: How do you avoid getting blocked by the SEC?**
A: A declared User-Agent, a throttle at half the published limit, sequential requests, backoff on 429,
and a cache so a rerun makes no requests at all. Three requests per company cover phase 1.

**Q: What is the trap in the company-facts API?**
A: `fy` and `fp` describe the filing, not the fact. A 10-K for fiscal 2025 also reports fiscal 2023 as a
comparative, tagged fy=2025. Period logic must use the start and end dates.

---

## 2. Fiscal periods and LTM (sourcebound/engine/periods.py)

### Concepts in plain English

- **Fiscal year**: a company's accounting year. It need not match the calendar: Walmart's ends on
  31 January, Procter & Gamble's on 30 June.
- **52/53-week year**: many retailers end their year on the same weekday each year (say, the last
  Saturday of September). Most years are 52 weeks (364 days); every five or six years one is 53 weeks.
  So "annual" cannot mean "exactly 365 days".
- **Duration vs instant**: income-statement and cash-flow items are measured *over* a period (a
  duration with start and end). Balance-sheet items are measured *at* a date (an instant).
- **Year-to-date (YTD)**: a 10-Q's cash-flow statement covers the year so far (e.g. nine months), not
  just the quarter.
- **LTM** (last twelve months, also TTM): the most recent twelve months, built from filings:
  `LTM = last full fiscal year + current YTD - same YTD a year earlier`.
  Example from the phase-1 report: Walmart's cash from operations for the twelve months to 31 July 2026
  is 41,565 (FY to Jan 2026, 10-K `0000104169-26-000055`) + 19,710 (Feb–Jul 2026) − 18,352 (Feb–Jul 2025,
  both from 10-Q `0000104169-26-000154`) = $42,923m.
- **FY0, FY-1, FY-2**: the latest completed fiscal year and the two before it. Three years is enough to
  see a trend.

### Why it is built this way

- **FY0 comes from the latest 10-K's report date** (submissions API). Its window is the annual window
  ending on that date that most facts use. FY-1 and FY-2 are the annual windows ending the day before the
  later year starts. "Annual" means 360–372 days between start and end, which admits 52-week (363),
  calendar (364/365) and 53-week (370) years.
- **LTM windows are discovered from the latest 10-Q's own facts**: the longest non-annual window ending on
  the 10-Q's date is the current YTD; the longest ending about a year earlier is the prior YTD. Then
  `check_ltm_windows` checks they line up: current YTD starts the day after FY0 ends, prior YTD starts
  when FY0 starts, and the two YTDs are within a week of the same length. If not, LTM is *not available*
  and the reason is reported. It is never patched.
- **No newer 10-Q** (the latest filing is the 10-K): LTM equals FY0, and the report says so.
- **Exact date matching**: a fact belongs to a period only if its dates equal the window exactly. A
  fact with odd dates is missed and reported as not available rather than guessed into a period.

### Interview questions

**Q: How do you compute LTM, and what can go wrong?**
A: Full year plus current year-to-date minus prior year-to-date. It goes wrong if the windows don't line
up: a 53-week year, a changed fiscal year-end, or a 10-Q that only tags the quarter. So the code checks
start dates and lengths first and refuses to compute LTM if they disagree.

**Q: Why not use the API's fiscal-year fields?**
A: They describe the filing, so a comparative figure for 2023 inside the 2025 10-K is labelled 2025. Only
the start and end dates identify the period the number measures.

**Q: Walmart's year ends in January. Does that break anything?**
A: No. Periods are anchored on the 10-K's report date and found by dates, so January, June, November or
52/53-week year-ends all work. A test covers each case.

---

## 3. Concepts, fallback chains and lineage (sourcebound/engine/concepts.py, resolver.py)

### Concepts in plain English (the items the ratios need)

- **Revenue**: sales for the period, the top line. (Not used by the four phase-1 ratios.)
- **Operating income**: revenue minus operating costs, before interest and tax. What the business earns
  from operations.
- **Depreciation and amortisation (D&A)**: the accounting charge that spreads the cost of equipment
  (depreciation) and intangible assets (amortisation) over their lives. It is a non-cash cost, which is
  why it is added back to get EBITDA.
- **Interest expense**: the cost of borrowing for the period.
- **Short-term debt**: borrowings due within a year: short-term borrowings (e.g. commercial paper, bank
  lines) plus the **current portion of long-term debt** (bonds and loans maturing in the next 12 months).
- **Total debt**: short-term debt plus long-term debt. Here it means reported borrowings; operating
  leases, pensions and guarantees are excluded (assumption 3).
- **Commercial paper**: short-term unsecured IOUs large companies sell to investors, usually for under
  270 days.
- **Finance lease**: a lease that is economically a purchase financed by debt, like leasing a car you
  will end up owning. Companies present finance-lease liabilities either inside their debt lines (Verizon,
  Goodyear) or on separate lines (Walmart, $6,761m at 31 January 2026). Sourcebound counts them as debt for
  every company (decision D18), as credit analysts normally do. Operating leases (ordinary rentals) are not
  counted.
- **Cash and cash equivalents**: cash and very short-term, very safe investments. Restricted cash
  (set aside for a purpose) is different and is flagged when included.
- **Short-term investments**: liquid securities held for less than a year; counted with cash for net
  leverage.
- **Cash from operations (CFO)**: cash generated by the business in the period, from the cash-flow
  statement.
- **Capital expenditure (capex)**: cash spent on property, plant and equipment.
- **Restatement**: a company reporting a different figure for a past period than it originally did
  (a correction, an accounting change, or discontinued operations). Goodyear's 2024 pre-tax income was
  155 in the 2024 10-K and 130 in the 2025 10-K.

### How resolution works

- Each concept has a **ranked chain** of candidates in `config/concepts.yaml`. A candidate is one tag,
  or a sum of tags and other concepts. The resolver uses the first candidate the company reports for the
  period, and **logs every fallback beyond rank 1** with the reason each higher rank failed.
- **Required vs optional**: a required concept with no fact is "not available", and every ratio using it
  is "not available". An optional item (short-term investments, short-term borrowings inside a sum,
  dividends) with no fact counts as zero, logged as "assumed zero: not reported" for the reviewer.
- **Most recently filed wins**: the same period appears in several filings (comparatives). The resolver
  takes the latest-filed value, records its accession, and logs a restatement if an earlier filing said
  something different.
- **LTM uses one tag for all three windows**, so a single LTM value never mixes tags.
- **Lineage**: each value carries a list of `SourceFact` records: concept, tag, fallback rank, value,
  unit, dates, form, accession, filing date, EDGAR link, and for LTM its role and sign.

### Why it is built this way

- Companies tag the same item differently and change tags over time (Verizon moved from
  `InterestExpense` to `InterestExpenseNonoperating` in its 2024 10-K; Goodyear during 2025). A chain makes the choice explicit,
  ordered and reviewable, and the log makes every deviation visible.
- Chains are **data, not code**, so changing one needs no code change, and every change is a diff the
  author approves.
- **Never estimate**: a missing fact stays missing. That is a ground rule, and it is also the right credit
  behaviour: a reviewer would rather see "not available" than a plausible wrong number.

### Interview questions

**Q: A company doesn't tag `OperatingIncomeLoss`. What do you do?**
A: Goodyear is an example: its income statement has no operating-income line. The chain falls back to
pre-tax income from continuing operations plus interest expense, flags the value "derived", and logs the
fallback. The derived figure includes other non-operating items, which the reviewer sees.

**Q: How do you handle restatements?**
A: Use the most recently filed value for each period and record which filing it came from. If any earlier
filing reported a different number, log both with their accession numbers.

**Q: What is the risk of summing tags?**
A: Double counting when one tag already includes another (commercial paper is often inside short-term
borrowings; available-for-sale securities are often inside short-term investments). That is why
short-term investments is a chain (first reported) rather than a sum.

**Q: Why is the chain in YAML and not in code?**
A: It is a judgement about accounting data, not logic. Keeping it as data makes it reviewable and
changeable with an audit trail, and per-company exceptions go in a separate overrides file.

---

## 4. The four core ratios (sourcebound/engine/ratios.py)

### Concepts in plain English

- **EBITDA** = operating income + D&A. Earnings before interest, tax, depreciation and amortisation: a
  rough proxy for the cash the business throws off before paying lenders, the tax authority and for
  reinvestment. Here it is **unadjusted**: companies' own "adjusted EBITDA" adds back other items and is
  not in XBRL.
- **Debt / EBITDA** (gross leverage): how many years of EBITDA it would take to repay all debt. The most
  common single measure of credit risk. Higher is riskier. The plan's stylized scorecard bands run from
  under 1.0x (strongest) to over 6.5x (weakest).
- **Net leverage** = (debt − cash − short-term investments) / EBITDA. Credits the company for cash it
  could use to repay debt. When cash exceeds debt the company is in **net cash**.
- **EBITDA / interest** (interest coverage): how many times over earnings cover the interest bill.
  Lower is riskier; below about 2x the scorecard puts it in its weakest band.
- **FCF / debt**: free cash flow (CFO − capex) as a percentage of debt: the share of debt one year's spare
  cash could repay. Can be negative when a company spends more than it generates.

### Edge cases, in order of precedence

1. Any input not available → the ratio is not available, with the missing input named.
2. Zero debt → debt / EBITDA is 0; net leverage is net cash (or 0); FCF / debt is "not meaningful: no
   debt". This wins over rule 3, because a company with no debt has no leverage whatever its EBITDA.
3. EBITDA at or below zero → leverage and coverage are "not meaningful" (dividing by a negative number
   gives a meaningless negative multiple; the scorecard puts these in the worst band).
4. Interest expense at or below zero → coverage is not meaningful.

### Why it is built this way

- Pure functions (`debt_to_ebitda(total_debt, ebitda)` and so on) hold the arithmetic, so each rule is
  tested in isolation. `compute_ratios` wraps them and attaches the formula and the resolved inputs.
- The language model never does arithmetic (ground rule 5); these functions are the only source of
  computed figures.

### Interview questions

**Q: Why EBITDA and not net income?**
A: Lenders care about cash available to service debt before financing and tax decisions. EBITDA strips
out interest (the thing being tested), tax, and non-cash D&A. Its weakness is that it ignores capex and
working capital, which is why FCF / debt sits beside it.

**Q: What does "not meaningful" mean, and why not show the number?**
A: If EBITDA is negative, debt / EBITDA comes out negative, which would read as better than zero leverage.
That's wrong, so the ratio is marked not meaningful and scored in the worst band.

**Q: Goodyear's FCF / debt is negative. Is that a bug?**
A: No. Its capex exceeded its cash from operations in those years, so free cash flow was negative. The
sign is information.

---

## 5. Checks (sourcebound/engine/checks.py)

- **Debt reconciliation**: total debt uses one candidate, but every other candidate the company reports
  for that date is computed too. If any differs by more than 5%, a warning is raised. No value changes.
  On real data this caught a real problem: for Walmart, the plan's starting rank-1 tag
  `DebtLongtermAndShorttermCombinedAmount` ($38,166m at 31 Jan 2026) turned out to be long-term debt
  only, *without* $6,596m of short-term borrowings. After the approved chain revision (D18) Walmart's
  debt comes from its balance-sheet lines plus finance leases ($51,523m), and the check still shows the
  gap to the narrow tag, now ranked last.

**Q: Tell me about a time your validation caught a data problem.**
A: The first run's reconciliation flagged Walmart's debt: the top-ranked XBRL tag was 15–30% below the sum
of the balance-sheet lines because it left out short-term borrowings. I didn't patch it silently; I
reported it with the evidence, proposed a chain change, and changed it only after approval, with the
tests updated to pin the new behaviour.
- **LongTermDebt scope**: `LongTermDebt` should include the current portion but companies differ. When all
  three tags exist for a date, the report records which reading the numbers support (Walmart's includes
  it: 38,166 = 34,624 + 3,542).
- **Mixed ranks**: a concept resolved through different tags in different periods is noted, because a
  trend across tags may not be like for like.

**Q: How do you know your debt number is right?**
A: Three ways: the lineage shows exactly which facts were added; the reconciliation compares every
candidate the company reports and warns on gaps over 5%; and I hand-check the golden-set companies
against the 10-K balance sheet and debt note.

---

## 6. Reports (sourcebound/pipeline/)

- `ratio_report`: per company, the periods and their windows, a summary table, the warnings, then every
  ratio for every period with its formula, its input values, and directly beneath, one table row per XBRL
  fact (tag, rank, value, period and role, form, accession, filing date, EDGAR link). Then the
  total-debt candidate table and the full log. Written to `reports/ratios/<TICKER>.md`.
- `tag_discovery`: per company, which candidate each concept resolves to in each period, a coverage
  matrix of every candidate tag, and related tags reported for FY0 that sit in no chain. This is the
  evidence for proposed chain changes.

---

## 7. Testing approach

- **Tests first** within each part of the phase.
- **Synthetic data** for logic (period identification, resolver rules, ratio maths): small round numbers
  and the fictional accession prefix `0000000000`, clearly not any company's data.
- **Captured fixtures** for real behaviour: trimmed copies of real EDGAR responses for WMT, VZ and GT in
  `tests/fixtures/edgar/`, made by `capture_fixtures.py` (kept tags in the chains, periods from 2021).
  Every expected value in those tests was read directly from the JSON, not from the engine, and carries
  its accession number in a comment.
- **No network in tests**: the EDGAR client is tested through a mock transport; live checks are marked
  `live` and skipped by default.

**Q: How do you test code whose correct answer depends on messy real data?**
A: Two layers. Synthetic cases pin each rule (restatements, LTM, zero EBITDA). Then fixture tests on
captured real responses pin the behaviour on known companies, with every expected figure traceable to an
accession number. Known weaknesses of the starting chains are pinned too and labelled, so changing a
chain is a deliberate, visible test change.

---

## Still to write

- US supervisory guidance on model risk (SR 11-7, its 2026 replacement SR 26-2 / OCC 2026-13 / FDIC
  FIL-15-2026, scope footnote 3) — written when the guidance is read in full, before the control table
  (phase 8).
