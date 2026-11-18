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

- With the starting chains (pending decisions, see the phase-1 stop report):
  - Walmart's rank-1 total debt (DebtLongtermAndShorttermCombinedAmount) excludes its short-term
    borrowings; the balance-sheet component sum is 2.2% (FY-2) to 26.2% (LTM) higher. Flagged by the
    reconciliation check above 5%; not corrected.
  - Verizon's LTM total debt is not available: no candidate pairs LongTermDebtAndCapitalLeaseObligations
    with the current portion.
  - Verizon's capital expenditure, and so its FCF / debt, is not available in any period: it uses
    PaymentsToAcquireOtherProductiveAssets, which is not in the chain.
  - Finance-lease liabilities are treated inconsistently: inside Verizon's rank-1 total and Goodyear's
    rank-4 alternative, outside Walmart's rank-2 components and Goodyear's rank-3 total.
- The derived operating income (pre-tax income plus interest expense) includes non-operating items such as
  other income and expense, so it differs from a true operating line.
- Interest-expense tags differ in scope: InterestExpenseDebt (Walmart) excludes finance-lease interest.
- Exact date matching means a fact with irregular dates is reported as not available rather than matched.
- Test fixtures are trimmed (chain tags only, periods from 2021) to keep the repository small; the full
  responses are re-creatable from EDGAR.
