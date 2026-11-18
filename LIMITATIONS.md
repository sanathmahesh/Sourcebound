# Known risks and limitations

Seeded from PLAN.md section 4.15; later items were added while building, with the phase that added them.

## Seeded from the plan

- XBRL tagging varies by company and over time; extension tags are invisible to the API; LongTermDebt is
  ambiguous; restatements change history; mergers break trends. Handling is in PLAN.md 4.5.
- No business-risk factors (scale, diversification, cyclicality) in the scorecard, so it will misjudge
  some companies against agencies.
- Section parsing of filing HTML can fail; tables are flattened to text.
- Keyword retrieval misses paraphrases.
- A quoted figure can match a number in the passage that refers to something else; the judge is the only
  check on that.
- The judge can be wrong, and when the judge and writer are the same model it may be lenient. Human labels
  on the golden set are the reference.
- Model outputs vary between runs; Sail may retire a model.
- The scheduled job may be disabled by GitHub after long inactivity; deploys from bot commits are
  unverified.
- The rate limit is per IP only; the spend backstop is a small prepaid Sail balance with auto-recharge off.
- Agency ratings carry redistribution terms. By default the site shows only aggregate agreement; ask
  before showing per-company ratings.

## Added in phase 1

- Chain revision 1 (decision D18) resolved the phase-1 chain issues. Remaining risks:
  - Rank 1 total debt adds finance-lease liabilities from their own tags. If a company's
    LongTermDebtNoncurrent line already includes finance leases and it also tags FinanceLeaseLiability in
    its lease note, leases are counted twice. The reconciliation check catches this only when another
    candidate is reported for the same date.
  - Rank 2 pairs a combined debt-and-lease tag with short-term debt. If short-term debt comes from
    LongTermDebtCurrent alone, the current portion of finance leases may be missing (usually small).
  - At 30 September 2026 Verizon tags its whole "debt maturing within one year" line as LongTermDebtCurrent,
    so its short-term borrowings are logged as "assumed zero" although they sit inside that figure; the
    total is right.
  - DebtLongtermAndShorttermCombinedAmount (now rank 5) varies in scope by company. Walmart's
    reconciliation warns against it in every period; that is expected and stays visible.
- The derived operating income (pre-tax income plus interest expense) includes non-operating items such as
  other income and expense, so it differs from a true operating line.
- InterestExpense and InterestExpenseNonoperating are assumed to include finance-lease interest; this is
  not checked company by company.
- Exact date matching means a fact with irregular dates is reported as not available rather than matched.
- Test fixtures are trimmed (chain tags only, periods from 2021) to keep the repository small; the full
  responses are re-creatable from EDGAR.

## Added in phase 2

- Undrawn revolver capacity is tagged only by Verizon among the 15. For the others it counts as zero
  (logged), which understates liquidity coverage and overstates near-term maturity cover, pushing those two
  factors towards weaker bands (e.g. Walmart).
- Maturity tables use company extension tags for some buckets, invisible to the API: Kohl's (all buckets),
  HCA, Goodyear, Procter & Gamble and ExxonMobil ("after year 5"). Their ladder totals and the ladder
  reconciliation are not available; Kohl's near-term maturity cover is not scored, so its grade is
  provisional.
- Caesars tags about $13.1bn of lease obligations as non-current finance-lease liabilities without a
  current-portion tag. Since chain revision 3 (D27) they count as debt; what they are (the counterparties)
  is to be confirmed in its 10-K.
- Net interest understates gross interest expense where interest income is material.
- ExxonMobil's latest figures (31 March 2026) are about six months older than most companies'.
- The scorecard is ratio-only: no business-risk factors and no operating-lease adjustment, so companies with
  large operating leases (such as retailers) can look stronger than under methods that adjust for leases.
  This is by design, and the comparison with agency ratings will measure its effect.
- Several reconciliation warnings (total debt against alternative candidates, ladder against total debt)
  remain open for a reviewer to resolve; none changes a value.

## Added in phase 3

- Section detection gaps (reports/section-coverage.md): ExxonMobil's 10-K uses a cross-reference format
  (Item 7 and Item 8 point to a later "Financial Section"), so its MD&A is not labelled; HCA's and Oracle's
  Item 8 is a one-line pointer and their statements sit at the end of the document, after the last Item, so
  they are labelled "other_item" (their debt notes are still found); some
  10-Qs have no separate debt note (Procter & Gamble, Oracle, ExxonMobil) and P&G's 10-Q has no liquidity
  heading in the list.
- Tables are flattened to text; in some filings each table cell becomes its own line, which makes passages
  of bare numbers.
- 10-Qs repeat much of the previous quarter's text, so near-identical passages appear from several
  filings; de-duplication happens when passages are merged for the memo (phase 4).
- Keyword search misses paraphrases; recall is measured in phase 5.
- Facts that appear only in text (e.g. Walmart's $15.0bn of undrawn committed credit lines) are not used by
  the ratio engine, which reads XBRL only.

## Added in phase 4

- A quoted figure passes the number check if the same number appears anywhere in the cited passage, even
  with a different meaning; the judge is the only check on that (as the plan anticipated).
- GLM-5.3 is both the default writer and the provisional judge, so the judge may be lenient on its own
  writing; phase 5 calibrates the judge against human labels.
- Model outputs vary between runs and cannot be pinned (no seed); phase 5 measures the spread.
- GLM-5.3 and DeepSeek-V4-Pro invent values when tools and a response schema share a request (probe); the
  design avoids that pattern.

## Added in phase 6

- Liquidity and near-term-maturity flags are noisy: 14 of 15 companies do not tag undrawn revolver capacity,
  which counts as zero, so most companies carry one of these flags (e.g. Walmart, with $15bn of undrawn lines
  in its 10-Q text).
- Vercel Hobby deploys only commits authored by the account owner (Vercel docs, last updated March and
  October 2026), so the watchlist's bot commits rely on a deploy hook; not verified until a repository and
  Vercel project exist.
- ExxonMobil is refreshed on every run (its newest 10-Q's facts sit under its new registrant); this costs one
  extra EDGAR request a day and changes no file.
- The scheduled run is off until the author approves it (phase 10).

## Added in phase 7

- `/api/ask` has no login. Since phase 10 a Vercel Firewall rule limits it per IP address (see phase 10 below).
- When an answer passes the 60-second limit the caller gets a 503, but model requests already started run on
  (up to 45 seconds each) and are billed.
- The follow-up judge is the provisional judge (GLM-5.3), the same model as the provisional writer.
- The maturity ladder is as of the last 10-K. Its first bucket keeps the XBRL tag's wording, "debt maturing in
  the next twelve months", meaning the twelve months after that fiscal year-end; an answer can read it as twelve
  months from today, and the judge accepted that reading in the smoke test (Walmart, maturity_year_1:FY0).
- Checked on the live deploy (18 November 2026): Vercel installs "required dependencies from uv.lock" (its
  build log does not mention the dev group); the rewrite keeps the /api/... path; the search index is bundled
  (a live question searched the filings).
- The results screen reads evals.json's untyped `results` defensively. (Phase 7's plain styling and the missing
  watchlist change column were resolved in phase 9.)
- Checklist sign-off lives in one browser's localStorage: it is not an audit trail.

## Added in phase 8

- The opportunity map's ratings are the author's judgment (drafted for review), not measurements.
- The effort comparison is pending until the author records timings; when recorded, it describes one analyst
  with small samples.
- The model recommendation is provisional until the claim labels and judge calibration exist.
- The decision log is written by hand and records settings and dated one-off observations; unlike artifacts
  1 to 5 it is not generated from results files, so the automatic number check does not cover it. The author
  accepted this on 18 November 2026.

## Added in phase 9

- Fonts load from Google Fonts, so a viewer's browser contacts Google; if that is blocked the page falls back to
  Georgia and system fonts.
- Fiscal years are labelled FY-2, FY-1, FY0 and LTM rather than FY2024 and so on: memo.json carries no mapping
  from period label to fiscal year (metrics.json does, but it can be newer than the memo).
- The fallback log shows the tag used and the engine's message; the fallback rank is inside the message, not a
  column of its own.
- Checklist "Go to" links exist only for items that point at a claim, the scorecard, the maturity ladder or the
  stale banner; items about a concept (fallback tags, blanks taken as zero) have no single place in the memo.
- The visual check is screenshots read by eye, not an automated pixel comparison. The prototype's own runtime
  drew its header and filters but not its tables in headless Chrome, so tables were checked against the handoff
  README and source rather than side by side.
- watchlist.json gained its change field by an offline rebuild from the published state and metrics, with
  checked_at unchanged and no EDGAR request; the next daily run writes it the normal way.

## Added in phase 10

- The site is at sourcebound-app.vercel.app (sourcebound.vercel.app belongs to someone else's site). Vercel makes
  a project's first deployment production, so the planned preview check happened on production instead.
- Preview deployments are behind Vercel Authentication; only the production addresses are public.
- The rate limit counts per IP address: people sharing one address (an office, a campus) share its ten questions
  per ten minutes, and someone rotating addresses can exceed it. The small prepaid Sail balance remains the
  backstop.
- The frontend's build and test tools (vite, vitest, json-schema-to-typescript) use picomatch 4.0.7, which has a
  high-severity advisory (GHSA-fc5q-39xc-vjpf, slow matching on crafted glob patterns) and no fixed version as of
  18 November 2026. Nothing shipped to the browser uses it (`npm audit --omit=dev` finds none), and the tools
  match only this project's own patterns.
- The Vercel project is not linked to the GitHub repository (D61): a push to main does not deploy by itself.
  Code changes are deployed with the CLI; the daily job deploys new data with a Vercel token.
- The daily job's Vercel token expires after a year unless renewed, and while valid it can deploy any project
  in the author's Vercel team; it lives only in GitHub's encrypted secrets.
- The daily job runs at 11:17 UTC and deploys only when data changed (or on a forced manual run). A day on
  which GitHub delays or skips the schedule leaves the site a day behind.
- The public commit history was rewritten before the first push to use GitHub's noreply address; commit IDs in
  stop reports written before that no longer exist.
