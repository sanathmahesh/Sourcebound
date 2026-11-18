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
