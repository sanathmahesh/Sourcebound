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
