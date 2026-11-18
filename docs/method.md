# Method

Every figure is computed by code from the company's XBRL data in its 10-K and 10-Q filings, using the
most recently filed value for each period. LTM (last twelve months) adds the latest year-to-date flows to
the last fiscal year and subtracts the prior year's year-to-date flows. A figure that cannot be found is
shown as "not available"; it is never estimated.

## Ratios

| Ratio | Definition |
|---|---|
| EBITDA | `operating_income + d_and_a` |
| Debt / EBITDA | `total_debt / EBITDA` |
| Net leverage | `(total_debt - cash - short_term_investments) / EBITDA` |
| EBITDA / interest | `EBITDA / interest_expense` |
| FCF / debt | `(cfo - capex) / total_debt` |
| Liquidity coverage | `(cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)` |
| Near-term maturity cover | `(short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)` |

## The SB scorecard (grid-v1)

SB grades are a student's stylized scorecard, not credit ratings. Each factor is placed in a band from 1
(strongest) to 6 (weakest); the grade comes from the weighted average band. A value exactly on a threshold gets the weaker band (tie rule "worse").

| Factor | Weight | Band 1 | Band 2 | Band 3 | Band 4 | Band 5 | Band 6 |
|---|---|---|---|---|---|---|---|
| Debt / EBITDA | 20% | under 1x | 1x to under 2x | 2x to under 3x | 3x to under 4.5x | 4.5x to under 6.5x | 6.5x or more |
| Net debt / EBITDA | 10% | under 0.5x | 0.5x to under 1.5x | 1.5x to under 2.5x | 2.5x to under 4x | 4x to under 6x | 6x or more |
| EBITDA / interest | 25% | over 15x | over 10x to 15x | over 6x to 10x | over 3.5x to 6x | over 2x to 3.5x | 2x or less |
| FCF / debt | 20% | over 40% | over 25% to 40% | over 15% to 25% | over 8% to 15% | over 0% to 8% | 0% or less |
| Liquidity sources / uses | 15% | over 2.5x | over 2x to 2.5x | over 1.5x to 2x | over 1.2x to 1.5x | over 1x to 1.2x | 1x or less |
| Debt due in 24 months / (cash + undrawn revolver) | 10% | under 0.25x | 0.25x to under 0.5x | 0.5x to under 0.75x | 0.75x to under 1x | 1x to under 1.5x | 1.5x or more |

Special cases: net cash scores band 1; a company with no debt scores band 1 on the debt factors; a ratio that cannot be computed meaningfully scores a fixed band when the reason is EBITDA at or below zero (band 6); no debt (band 1); no uses of cash (band 1); no cash or undrawn revolver (band 6). Any other unscorable factor is left out.

| Weighted score | Grade |
|---|---|
| up to 1.5 | SB-1 |
| over 1.5 to 2.5 | SB-2 |
| over 2.5 to 3.5 | SB-3 |
| over 3.5 to 4.5 | SB-4 |
| over 4.5 to 5.5 | SB-5 |
| over 5.5 | SB-6 |

A weighted score of 3.5 or less counts as "IG-like" (investment-grade-like) in the comparison with agency ratings. When a factor cannot be scored, the remaining weights are scaled up and the grade is marked provisional.
