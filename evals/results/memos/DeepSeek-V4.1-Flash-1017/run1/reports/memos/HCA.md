# Credit memo: HCA Healthcare, Inc. (HCA)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4.1-Flash-1017`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-4**.
Sources: [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm); [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526191444/hca-20260331.htm); [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm)

Claims: 35 — 31 supported, 3 partially supported, 1 unsupported. Raw numbers rejected in first drafts: 1; repairs: 1.

## Business profile

1. HCA Healthcare is a large acute-care provider, with revenue of **$78.7 billion** [F1] and EBITDA of **$15.9 billion** [F2] in the twelve months to 30 September 2026.  
   ◐ partially supported (judge): The revenue ($78.7B) and EBITDA ($15.9B) figures are supported by the metric values, but the characterization as a 'large acute-care provider' is not backed by any evidence passage.
2. Revenue rose from **$65.0 billion** [F3] in the fiscal year ended 31 December 2023 to **$78.7 billion** [F1] in the twelve months to 30 September 2026, with EBITDA of **$15.6 billion** [F4] in the fiscal year ended 31 December 2025.  
   ✅ supported (judge): All three figures match the XBRL-computed metric values exactly.
3. The company operates a hospital network that is mostly general acute care, with smaller behavioral and rehabilitation components.  
   ✅ supported (judge): Evidence states 190 hospitals, of which 179 are general acute care, with smaller behavioral (7) and rehabilitation (4) components.
   - cites `HCA-000119312526044769-0004` ✓: “we operated 190 hospitals, comprised of 179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals”
4. Its operations also include freestanding outpatient surgery and endoscopy centers, and its facilities are concentrated in the United States with one additional market abroad.  
   ✅ supported (judge): The passage confirms freestanding outpatient surgery and endoscopy centers and facilities concentrated in the U.S. with England as the one market abroad.
   - cites `HCA-000119312526044769-0004` ✓: “we operated 121 freestanding ambulatory surgery centers (“ASCs”) and 31 freestanding endoscopy centers. Our facilities are located in 19 states and England”
5. Patient volumes and reimbursement are exposed to payer utilization controls and a shift toward outpatient care, which pressures admissions and lengths of stay.  
   ✅ supported (judge): The passage explicitly states admissions, lengths of stay and reimbursement are negatively affected by payer pre-authorization, utilization review, and pressure toward outpatient care.
   - cites `HCA-000119312526044769-0079` ✓: “Admissions, average lengths of stay and reimbursement amounts continue to be negatively affected by third-party payer pre-admission authorization requirements, utilization review and pressure to maximize outpatient”
6. Competitive position depends heavily on attracting and retaining physicians, which supports patient flows but is not contractually assured.  
   ✅ supported (judge): The passage states physician number and quality are two of the most significant competitive factors, that physicians may terminate relationships at any time (no contractual assurance), and that physicians refer patients based on hospital quality factors.
   - cites `HCA-000119312526044769-0075` ✓: “Two of the most significant factors that impact the competitive position of a hospital are the number and quality of physicians affiliated with or employed by the hospital”

## Financial risk

1. Debt / EBITDA was **3.17x** [F5] at the fiscal year ended 31 December 2023, **3.03x** [F6] at the fiscal year ended 31 December 2025 and **3.17x** [F7] at the twelve months to 30 September 2026, a stable trend across the period.  
   ✅ supported (judge): All three ratio values match the scorecard exactly, and the small variation (3.17x, 3.03x, 3.17x) supports the characterization of a stable trend.
2. Net leverage was **3.09x** [F8] at the fiscal year ended 31 December 2023, **2.96x** [F9] at the fiscal year ended 31 December 2025 and **3.11x** [F10] at the twelve months to 30 September 2026, also stable.  
   ✅ supported (judge): The metric values from XBRL data exactly match the three net leverage figures (3.09x, 2.96x, 3.11x), and the small range (2.96–3.11x) reasonably supports describing the level as stable.
3. EBITDA / interest was **6.56x** [F11] at the fiscal year ended 31 December 2023, **6.94x** [F12] at the fiscal year ended 31 December 2025 and **6.74x** [F13] at the twelve months to 30 September 2026, a stable trend.  
   ✅ supported (judge): All three reported ratios (6.56x, 6.94x, 6.74x) exactly match the XBRL-computed metric values, and the small variation supports the 'stable trend' characterization.
4. FCF / debt was **11.6%** [F14] at the fiscal year ended 31 December 2023, **16.3%** [F15] at the fiscal year ended 31 December 2025 and **11.8%** [F16] at the twelve months to 30 September 2026, stable overall.  
   ✅ supported (judge): All three FCF/debt values match the scorecard exactly (11.6%, 16.3%, 11.8%) and the ratio remains in a similar range across periods, consistent with 'stable overall'.
5. Debt rose over the period as the company issued long-term debt and increased short-term borrowings and revolving credit facility draws, so leverage ratios stayed broadly flat only because EBITDA also grew.  
   ◐ partially supported (judge): Debt issuance and increased short-term borrowings/revolver draws are supported, but the evidence says nothing about leverage ratios staying flat or EBITDA growth offsetting them.
   - cites `HCA-000119312526321077-0007` ✓: “Net change in short-term borrowings and revolving credit facility”
   - cites `HCA-000119312526044769-0298` ✓: “including $2.207 billion of outstanding commercial paper notes (short-term borrowings)”
6. Interest expense increased mainly on a higher average debt balance at a steady average effective rate, while operating cash flow declined in the first half of **2026** [quoted: HCA-000119312526044769-0295] on unfavorable working capital and higher income taxes paid.  
   ✅ supported (judge): Interest expense increase attributed to higher average debt balance with 5.0% rate in both years, and operating cash flow decline driven by unfavorable working capital and higher income taxes paid, matching the evidence.
   - cites `HCA-000119312526044769-0295` ✓: “The $187 million increase in interest expense was primarily due to an increase in the average debt balance.”
   - cites `HCA-000119312526321077-0038` ✓: “The decline in cash provided by operating activities was primarily related to unfavorable working capital changes of $1.413 billion”

## Liquidity

1. Liquidity coverage was **1.30x** [F17] in the fiscal year ended 31 December 2025 and **0.86x** [F18] for the twelve months to 30 September 2026, so measured sources covered less than the uses captured by the metric over the twelve-month period.  
   ✅ supported (judge): The metric values match the claimed 1.30x (FY2025) and 0.86x (LTM to Sep-2026) coverage figures, and a coverage ratio below 1.0x directly implies sources covered less than uses over that period.
2. Cash from operations of **$11.2 billion** [F19] exceeded capital expenditure of **$5.2 billion** [F20] and dividends of **$681 million** [F21] in the twelve months to 30 September 2026, but did not cover the **$8.1 billion** [F22] of short-term debt alongside them.  
   ✅ supported (judge): All figures match the metrics; CFO of $11.2B covers capex ($5.2B) and dividends ($681M) totaling ~$5.9B, but not the additional $8.1B short-term debt (~$14.0B combined).
3. The coverage metric assumes **$0** [F23] of undrawn revolving capacity, whereas the company reports remaining availability under its senior unsecured credit facility during the twelve months to 30 September 2026.  
   ✅ supported (judge): The metric was assumed to be $0 because undrawn revolver capacity was not reported, while the company discloses billions available under its senior unsecured credit facility.
   - cites `HCA-000119312526321077-0068` ✓: “amounts available under our senior unsecured credit facility ($3.086 billion and $3.816 billion available as of June 30, 2026”
4. The principal committed backstop is a senior unsecured revolving facility, which the company sized at $**8.000** [quoted: HCA-000119312526044769-0304] billion of commitments.  
   ◐ partially supported (judge): The $8.000 billion senior unsecured revolving credit commitments are supported, but the evidence does not describe the facility as a 'backstop' or as the company's principal committed backstop.
   - cites `HCA-000119312526044769-0304` ✓: “$8.000 billion of senior unsecured revolving credit commitments with a term of five years”
5. Capital spending is expected to remain substantial, and the company states it will fund it from internal generation and borrowing.  
   ✅ supported (judge): The passage states planned capex of $5.0–5.5 billion plus $8.6 billion in construction commitments, to be funded by internally generated and borrowed funds.
   - cites `HCA-000119312526321077-0066` ✓: “Planned capital expenditures are expected to be approximately between $5.0 billion and $5.5 billion in 2026, excluding acquisitions.”
6. Debt service requirements are described as significant, with total debt of $**48.023** [quoted: HCA-000119312526191444-0055] billion reported at the end of the first quarter of **2026** [quoted: HCA-000119312526191444-0055].  
   ✅ supported (judge): The passage explicitly states significant debt service requirements and debt of $48.023 billion at March 31, 2026, matching the claim.
   - cites `HCA-000119312526191444-0055` ✓: “We have significant debt service requirements. Our debt totaled $48.023 billion at March 31, 2026.”

## Maturity wall

1. Debt scheduled to mature within the next two years totals **$7.4 billion** [F24], or **15.7%** [F25] of total debt of **$47.2 billion** [F26].  
   ✅ supported (judge): All figures in the claim match the computed XBRL metrics: debt due within 24 months of $7.4B, share of 15.7%, and total debt of $47.2B.
2. Scheduled maturities rise from **$2.5 billion** [F27] in year two to **$3.6 billion** [F28] in year three, **$3.6 billion** [F29] in year four and **$4.0 billion** [F30] in year five.  
   ✅ supported (judge): The passage's maturities ($2.547B, $3.645B, $3.577B, $4.021B) round to the claimed $2.5B, $3.6B, $3.6B, and $4.0B.
   - cites `HCA-000119312526044769-0418` ✓: “Maturities of long-term debt in years 2027 through 2030 are $2.547 billion, $3.645 billion, $3.577 billion and $4.021 billion, respectively.”
3. Near-term maturity cover is **7.15x** [F31], calculated with undrawn revolver capacity and short-term investments treated as zero.  
   ✅ supported (judge): The scorecard shows near-term maturity cover of exactly 7.15x with short-term investments and undrawn revolver assumed zero, matching the claim.
   - cites `HCA-000119312526044769-0306` ✓: “there were no borrowings outstanding under our senior unsecured credit facility”
4. Commercial paper, which forms part of short-term debt of **$4.9 billion** [F32], matures within **397** [quoted: HCA-000119312526044769-0418] days of issue and therefore falls inside the near-term maturity window.  
   ✅ supported (judge): Evidence states commercial paper maturities will not exceed 397 days from issue, and short-term debt is $4.9 billion per XBRL metric.
   - cites `HCA-000119312526044769-0418` ✓: “The maturities of the commercial paper notes borrowings may vary, but will not exceed 397 days from the date of issue”
5. Refinancing activity has run alongside the near-term maturities, with a **2026** [quoted: HCA-000119312526437871-0023] note issuance whose proceeds went to commercial paper repayment and with **2026** [quoted: HCA-000119312526437871-0023] notes subsequently redeemed in full.  
   ✅ supported (judge): The passage confirms April 2026 note issuance proceeds repaid commercial paper and May 2026 full redemption of 2026 notes, alongside $8,093 million due within one year showing near-term maturities.
   - cites `HCA-000119312526437871-0023` ✓: “We used the net proceeds to repay borrowings under our commercial paper program”
   - cites `HCA-000119312526437871-0023` ✓: “During May 2026, we redeemed all $1.500 billion aggregate principal amount of 5.250% senior notes due 2026 and all $1.000 billion aggregate principal amount of 5.375% senior notes due 2026.”
6. Cash and cash equivalents of **$1.0 billion** [F33] are well below the **$4.9 billion** [F32] of short-term debt due within one year, so repayment of the nearest maturities depends on refinancing or operating cash flow rather than balance-sheet liquidity alone.  
   ✅ supported (judge): The two metric values ($1.0B cash vs. $4.9B short-term debt) directly establish the gap, and the conclusion about reliance on refinancing or operating cash flow follows directly since cash covers only ~20% of near-term maturities.

## Key risks

1. Significant indebtedness could limit the company's ability to raise additional capital, react to changes in the economy or industry, and meet its obligations.  
   ✅ supported (judge): The risk factor passage directly states each part of the claim about significant indebtedness's effects.
   - cites `HCA-000119312526044769-0144` ✓: “Our indebtedness could adversely affect our ability to raise additional capital to fund our operations, limit our ability to react to changes in the economy or our industry”
   - cites `HCA-000119312526044769-0144` ✓: “expose us to interest rate risk to the extent of our variable rate debt and prevent us from meeting our obligations”
2. A portion of cash flows from operations must be dedicated to principal and interest payments, reducing funds available for operations, capital expenditures, and future opportunities.  
   ✅ supported (judge): The passage states that debt service requires a portion of operating cash flows, reducing funds for operations, capital expenditures, and future business opportunities.
   - cites `HCA-000119312526044769-0145` ✓: “requiring a portion of cash flows from operations to be dedicated to the payment of principal and interest on our indebtedness”
3. Refinancing debt on favorable terms, or at all, is directly affected by global economic and financial conditions and may also be hurt by credit rating downgrades.  
   ✅ supported (judge): The passage states both that refinancing on favorable terms, or at all, is directly affected by global economic and financial conditions, and that credit rating downgrades may negatively affect debt financing availability and rates.
   - cites `HCA-000119312526044769-0147` ✓: “Our ability to refinance our indebtedness on favorable terms, or at all, is directly affected by the then current global economic and financial conditions”
   - cites `HCA-000119312526044769-0147` ✓: “Downgrades in our credit ratings may also negatively affect availability of debt financing and the rates at which such financing is available”
4. A breach of covenant under the senior unsecured credit facility could result in a default and acceleration of amounts outstanding, with cross-default risk across other debt.  
   ✅ supported (judge): The passage states a covenant breach under the senior unsecured credit facility could trigger default, acceleration of amounts outstanding, and an event of default under a significant portion of other debt (cross-default).
   - cites `HCA-000119312526044769-0149` ✓: “A breach of this or any other covenant could result in a default under our senior unsecured credit facility”
   - cites `HCA-000119312526044769-0149` ✓: “upon which the lenders thereunder could elect to declare all amounts outstanding to be immediately due and payable”
   - cites `HCA-000119312526044769-0149` ✓: “which would also result in an event of default under a significant portion of our other outstanding”
5. Debt to EBITDA was **3.17x** [F7] at the twelve months to 30 September 2026.  
   ✅ supported (judge): The claim exactly matches the computed metric value for Debt/EBITDA LTM to 30 September 2026.

## Rating rationale

1. The company's scorecard outcome is **SB-4** [F34], a stylized internal scorecard grade and not a credit rating, corresponding to a weighted score of **4.25** [F35]; the grade is not provisional, because all six factors were assigned a band.  
   ✅ supported (judge): All claim parts match the computed scorecard: SB-4 grade, 4.25 weighted score, and all six factors banded so the grade is not provisional.
2. The strongest-scoring factor is interest coverage, at **6.74x** [F13] with band **3** [F36] and a **25.0%** [F37] weight, making it the main support for the grade.  
   ✅ supported (judge): Interest coverage has the best band (3 vs 4/4/4/6/6 for the other factors) and the highest weight (25%), with a value of 6.74x, so it is the strongest-scoring factor and main support for the grade.
3. The weakest-scoring factors are liquidity coverage, at **0.86x** [F18] with band **6** [F38] and a **15.0%** [F39] weight, and near-term maturity cover, at **7.15x** [F31] with band **6** [F40] and a **10.0%** [F41] weight.  
   ✅ supported (judge): Metric values match the claim exactly: liquidity coverage 0.86x with band 6 and 15.0% weight; near-term maturity cover 7.15x with band 6 and 10.0% weight, and these are the weakest (band 6) factors.
4. The middle bands come from debt / EBITDA of **3.17x** [F7] and net leverage of **3.11x** [F10], each scoring band **4** [F42] and **4** [F43] at weights of **20.0%** [F44] and **10.0%** [F45], alongside FCF / debt of **11.8%** [F16] at band **4** [F46] and a **20.0%** [F47] weight.  
   ✅ supported (judge): All cited values (3.17x debt/EBITDA, 3.11x net leverage, 11.8% FCF/debt, each band 4, weights 20%/10%/20%) match the computed scorecard metrics.
5. The weak liquidity and maturity bands rest on a metric that treats undrawn revolver capacity as zero, whereas the company does report borrowing capacity under its senior unsecured credit facility, so those two bands may understate measured liquidity.  
   ❌ unsupported (judge): The scorecard metrics explicitly include undrawn revolver capacity in their denominators (e.g., 'Debt due in 24 months / (cash + undrawn revolver)'), so the premise that the metric treats undrawn revolver as zero is contradicted by the evidence.
   - cites `HCA-000119312526321077-0068` ✓: “available sources of capital include amounts available under our senior unsecured credit facility”
6. The scorecard result is tempered by a stated reliance on borrowing alongside internal cash generation to fund substantial planned capital spending.  
   ✅ supported (judge): The filing explicitly states reliance on borrowed funds alongside internal cash generation to fund substantial planned capital expenditures ($5.0–5.5 billion in 2026 plus $8.6 billion of construction projects).
   - cites `HCA-000119312526321077-0066` ✓: “We expect to finance capital expenditures with internally generated and borrowed funds.”

## Reviewer checklist

- [ ] **not available** (warning): Debt maturing in the next twelve months not available in FY0: no candidate tag is reported (see the log).
- [ ] **not available** (warning): Debt maturing after year five not available in FY0: no candidate tag is reported (see the log).
- [ ] **fallback** (info): Operating income: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper in FY-2.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): ShortTermBorrowings assumed zero (not reported) in FY-2.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): CommercialPaper assumed zero (not reported) in FY-2.
- [ ] **assumed zero** (info): Short-term investments assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Finance-lease liabilities (current plus non-current) assumed zero (not reported) in LTM.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **reconciliation** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $50,493m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $44,766m (-11.3%). Check which matches the balance sheet.
- [ ] **partially supported claim** (warning): Business profile: partially supported (The revenue ($78.7B) and EBITDA ($15.9B) figures are supported by the metric values, but the characterization as a 'large acute-care provider' is not backed by any evidence passage.): “HCA Healthcare is a large acute-care provider, with revenue of $78.7 billion and EBITDA of $15.9 billion in the twelve months to 30 September 2026.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (Debt issuance and increased short-term borrowings/revolver draws are supported, but the evidence says nothing about leverage ratios staying flat or EBITDA growth offsetting them.): “Debt rose over the period as the company issued long-term debt and increased short-term borrowings and revolving credit facility draws, so leverage ratios stayed broadly flat only because EBITDA also grew.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The $8.000 billion senior unsecured revolving credit commitments are supported, but the evidence does not describe the facility as a 'backstop' or as the company's principal committed backstop.): “The principal committed backstop is a senior unsecured revolving facility, which the company sized at $8.000 billion of commitments.”
- [ ] **unsupported claim** (warning): Rating rationale: unsupported (The scorecard metrics explicitly include undrawn revolver capacity in their denominators (e.g., 'Debt due in 24 months / (cash + undrawn revolver)'), so the premise that the metric treats undrawn revolver as zero is contradicted by the evidence.): “The weak liquidity and maturity bands rest on a metric that treats undrawn revolver capacity as zero, whereas the company does report borrowing capacity under its senior unsecured credit facility, so those two bands may understate measured liquidity.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:LTM) | $78.7 billion | rank 1: Revenues | Revenues 75,600,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>Revenues 59,188,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>Revenues 56,087,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F2 | EBITDA (ebitda:LTM) | $15.9 billion | operating_income + d_and_a | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 1,676,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 2,828,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F3 | Revenue (revenue:FY-2) | $65.0 billion | rank 1: Revenues | Revenues 64,968,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F4 | EBITDA (ebitda:FY0) | $15.6 billion | operating_income + d_and_a | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F5 | Debt / EBITDA (debt_to_ebitda:FY-2) | 3.17x | total_debt / EBITDA | LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,706,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,077,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F6 | Debt / EBITDA (debt_to_ebitda:FY0) | 3.03x | total_debt / EBITDA | LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:LTM) | 3.17x | total_debt / EBITDA | LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 1,676,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F8 | Net leverage (net_leverage:FY-2) | 3.09x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 935,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,706,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,077,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F9 | Net leverage (net_leverage:FY0) | 2.96x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F10 | Net leverage (net_leverage:LTM) | 3.11x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F11 | EBITDA / interest (interest_coverage:FY-2) | 6.56x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,706,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,077,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F12 | EBITDA / interest (interest_coverage:FY0) | 6.94x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F13 | EBITDA / interest (interest_coverage:LTM) | 6.74x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 1,676,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 2,828,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F14 | FCF / debt (fcf_to_debt:FY-2) | 11.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 9,431,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,744,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| F15 | FCF / debt (fcf_to_debt:FY0) | 16.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F16 | FCF / debt (fcf_to_debt:LTM) | 11.8% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F17 | Liquidity coverage (liquidity_coverage:FY0) | 1.30x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsOfDividends 679,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F18 | Liquidity coverage (liquidity_coverage:LTM) | 0.86x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F19 | Cash from operations (cfo:LTM) | $11.2 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F20 | Capital expenditure (capex:LTM) | $5.2 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F21 | Dividends paid (dividends:LTM) | $681 million | rank 1: PaymentsOfDividends | PaymentsOfDividends 679,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsOfDividends 519,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsOfDividends 517,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F22 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $8.1 billion | rank 1: DebtCurrent | DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F23 | Undrawn revolving credit capacity (undrawn_revolver:LTM) | $0 |  | — |
| F24 | Debt due within 24 months (debt_due_24m:FY0) | $7.4 billion | short_term_debt + maturity_year_2 | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F25 | Share of debt due within 24 months (share_due_24m:FY0) | 15.7% | (short_term_debt + maturity_year_2) / total_debt | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F26 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $47.2 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F27 | Debt maturing in year two (maturity_year_2:FY0) | $2.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F28 | Debt maturing in year three (maturity_year_3:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 3,645,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F29 | Debt maturing in year four (maturity_year_4:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 3,577,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F30 | Debt maturing in year five (maturity_year_5:FY0) | $4.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 4,021,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F31 | Near-term maturity cover (near_term_maturity_cover:FY0) | 7.15x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F32 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $4.9 billion | rank 1: DebtCurrent | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F33 | Cash and cash equivalents (cash:FY0) | $1.0 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F34 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 4.25 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F35 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 4.25 | sum of weight x band over the factors scored, divided by their weights | — |
| F36 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 3 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F37 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F38 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F39 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F40 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 6 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F41 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F42 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 4 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F43 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 4 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F44 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F45 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F46 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 4 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F47 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### HCA-000119312526044769-0004

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 5633–6593

> Item 1. Business
> General
> HCA Healthcare, Inc. is one of the leading health care services companies in the United States. At December 31, 2025, we operated 190 hospitals, comprised of 179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals. In addition, we operated 121 freestanding ambulatory surgery centers (“ASCs”) and 31 freestanding endoscopy centers. Our facilities are located in 19 states and England.
> The terms “Company,” “HCA,” “HCA Healthcare,” “we,” “our” or “us,” as used herein and unless otherwise stated or indicated by context, refer to HCA Healthcare, Inc. and its affiliates. The term “affiliates” means direct and indirect subsidiaries of HCA Healthcare, Inc. and partnerships and joint ventures in which such subsidiaries are partners. The terms “facilities” or “hospitals” refer to entities owned and operated by affiliates of HCA, and the term “employees” refers to employees of affiliates of HCA.

### HCA-000119312526044769-0075

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 88058–89358

> Two of the most significant factors that impact the competitive position of a hospital are the number and quality of physicians affiliated with or employed by the hospital. Although physicians may at any time terminate their relationship with a hospital we operate, our hospitals seek to retain physicians with varied specialties on the hospitals’ medical staffs and to attract other qualified physicians. We believe physicians refer patients to a hospital based on the quality and scope of services the hospital renders to patients and physicians, the quality of physicians on the medical staff, the location of the hospital and the quality of the hospital’s facilities, technology, equipment and employees. Accordingly, we strive to maintain and provide quality facilities, technology, equipment, employees and services for physicians and patients. As part of these efforts, we are implementing a new EHR platform across our facilities that is designed to help improve care coordination, enhance data integrity and interoperability, and drive operating efficiencies and cost savings. Our hospitals face competitors that are implementing physician alignment strategies, such as employing physicians, acquiring physician practice groups and participating in ACOs or other clinical integration models.

### HCA-000119312526044769-0079

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 93332–94732

> In addition, changes in licensure or other laws or regulations and recognition of new provider types or payment models could impact our competitive position. See Item 1, “Business — Regulation and Other Factors.”
> We and the health care industry as a whole face the challenge of continuing to provide quality patient care while dealing with rising costs and strong competition for patients. Changes in medical technology, existing and future legislation, regulations and interpretations and contracting for provider services by third-party payers remain ongoing challenges.
> Admissions, average lengths of stay and reimbursement amounts continue to be negatively affected by third-party payer pre-admission authorization requirements, utilization review and pressure to maximize outpatient and alternative health care delivery services for less acutely ill patients. Increased competition, admission constraints and third-party payer pressures are expected to continue. To meet these challenges, we intend to expand and update our facilities or acquire or construct new facilities where appropriate, enhance the provision of a comprehensive array of outpatient services, offer market competitive pricing to group purchasers of health care services, upgrade facilities and equipment and offer new or expanded programs and services.
> Regulation and Other Factors
> Licensure, Certification and Accreditation

### HCA-000119312526044769-0144

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 164898–166383

> Item 1A. Risk Factors
> If any of the events discussed in the following risk factors were to occur, our business, financial position, results of operations, cash flows or prospects could be materially, adversely affected. Additional risks and uncertainties not presently known to us or that we currently deem immaterial may also affect us. Our business is subject to the following material risks and uncertainties.
> Risks related to our indebtedness:
> We have significant indebtedness and may incur further indebtedness in the future. Our indebtedness could adversely affect our ability to raise additional capital to fund our operations, limit our ability to react to changes in the economy or our industry, expose us to interest rate risk to the extent of our variable rate debt and prevent us from meeting our obligations.
> As of December 31, 2025, our total indebtedness was $46.492 billion. As of December 31, 2025, we had availability of $5.779 billion under our senior unsecured credit facility (after giving effect to all issued and outstanding letters of credit and our intention to maintain a minimum available borrowing capacity equal to the aggregate amount outstanding under the commercial paper program ($2.207 billion as of December 31, 2025)). Our indebtedness could have important consequences, including:
> •
> increasing our vulnerability to downturns or adverse changes in general economic, industry or competitive conditions and adverse changes in government regulations;
> •

### HCA-000119312526044769-0145

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 166384–167684

> requiring a portion of cash flows from operations to be dedicated to the payment of principal and interest on our indebtedness, therefore reducing our ability to use our cash flows to fund our operations, capital expenditures and future business opportunities;
> •
> exposing us to the risk of increased interest rates on our existing borrowings that are at variable rates of interest or refinancing our debt in a rising or high rate environment;
> •
> limiting our ability to make strategic acquisitions or causing us to make nonstrategic divestitures;
> 33
> •
> limiting our ability to obtain additional financing for working capital, capital expenditures, share repurchases, dividends, product or service line development, debt service requirements, acquisitions and general corporate or other purposes; and
> •
> limiting our ability to adjust to changing market conditions and placing us at a competitive disadvantage compared to our competitors who have less debt.
> We and our subsidiaries have the ability to incur additional indebtedness in the future, subject to the restrictions contained in our senior unsecured credit facility and the indentures governing our outstanding notes. If new indebtedness is added to our current debt levels, interest rates and the related risks that we now face could intensify.

### HCA-000119312526044769-0147

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 169033–169809

> We may find it necessary or prudent to refinance our outstanding indebtedness, the terms of which refinancing may not be favorable to us. Our ability to refinance our indebtedness on favorable terms, or at all, is directly affected by the then current global economic and financial conditions which affect the availability of debt financing and the rates at which such financing is available. In addition, our ability to incur secured indebtedness depends in part on the value of our assets, which depends, in turn, on the strength of our cash flows and results of operations, and on economic and market conditions and other factors. Downgrades in our credit ratings may also negatively affect availability of debt financing and the rates at which such financing is available.

### HCA-000119312526044769-0149

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 171241–172368

> Under our senior unsecured credit facility, we are required to satisfy and maintain a specified financial ratio. Our ability to maintain this financial ratio may be affected by global economic and financial conditions or other events beyond our control, and there can be no assurance we will continue to maintain this ratio. A breach of this or any other covenant could result in a default under our senior unsecured credit facility, upon which the lenders thereunder could elect to declare all amounts outstanding to be immediately due and payable and terminate all commitments to extend further credit, which would also result in an event of default under a significant portion of our other outstanding
> 34
> indebtedness. In a scenario where the repayment of borrowings is accelerated, there can be no assurance there will be sufficient assets to repay our senior unsecured credit facility and our other indebtedness.
> Risks related to human capital:
> Our results of operations may be adversely affected by competition for staffing, the shortage of experienced nurses and other health care professionals and labor union activity.

### HCA-000119312526044769-0295

mdna, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 336972–338435

> Other operating expenses, as a percentage of revenues, were 21.0% in both 2025 and 2024. Other operating expenses are primarily comprised of contract services, professional fees, repairs and maintenance, rents and leases, utilities, insurance (including professional liability insurance) and nonincome taxes. We have seen inflation have a negative impact on certain of these expenses and expect inflationary pressures will continue to impact operating expenses in 2026.
> Equity in earnings of affiliates was $78 million for 2025 and $23 million for 2024.
> Depreciation and amortization, as a percentage of revenues, were 4.6% in 2025 and 4.7% in 2024. Depreciation expense was $3.508 billion for 2025 and $3.294 billion for 2024. The increase of $214 million in depreciation expense relates primarily to capital expenditures at our existing facilities.
> Interest expense increased to $2.248 billion for 2025 from $2.061 billion for 2024. The $187 million increase in interest expense was primarily due to an increase in the average debt balance. The average effective interest rate for our long-term debt was 5.0% for both 2025 and 2024. Our average debt balance was $44.731 billion for 2025 compared to $41.388 billion for 2024.
> Gains on sales of facilities were $37 million for 2025 and $14 million for 2024.
> 68
> HCA HEALTHCARE, INC.
> MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION
> AND RESULTS OF OPERATIONS (Continued)
> Results of Operations (continued)

### HCA-000119312526044769-0298

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 340098–341552

> Cash provided by operating activities totaled $12.636 billion in 2025 compared to $10.514 billion in 2024 and $9.431 billion in 2023. The $2.122 billion increase in cash provided by operating activities for 2025, compared to 2024, was related primarily to the combined impact of a $1.319 billion increase in net income, excluding gains on sales of facilities and depreciation and amortization, positive changes in working capital of $524 million and a decline in income taxes paid of $104 million. The $1.083 billion increase in cash provided by operating activities for 2024, compared to 2023, was related primarily to an increase in net income of $542 million, excluding losses and gains on sales of facilities, and a positive change in working capital items of $351 million, mainly from a decline in inventories and other assets. Cash payments for interest and income taxes increased $165 million for 2025 compared to 2024. We had negative working capital of $567 million at December 31, 2025 and positive working capital of $1.237 billion at December 31, 2024. The decline in working capital is primarily due to the decline of $893 million in cash and cash equivalents and an increase in current liabilities of $1.173 billion, including $2.207 billion of outstanding commercial paper notes (short-term borrowings). We have the ability to refinance our outstanding commercial paper notes with our senior unsecured credit facility on a long-term basis.

### HCA-000119312526044769-0304

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 347579–348410

> Financing Activities (continued)
> During 2025, we entered into a new credit agreement that provides for $8.000 billion of senior unsecured revolving credit commitments with a term of five years (“senior unsecured credit facility”). Borrowings under the senior unsecured credit facility bear interest at a rate equal to the Secured Overnight Financing Rate plus 1.125% (plus, until October 23, 2025, a 0.10% credit spread adjustment, as the unsecured credit facility was amended on that date to remove the credit spread adjustment). We terminated our $4.500 billion senior secured asset-based revolving credit facility, our $3.500 billion senior secured revolving cash flow credit facility and our senior secured term loan facility of $1.238 billion. Finance leases and other secured debt totaled $1.021 billion at December 31, 2025.

### HCA-000119312526044769-0306

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 349644–350972

> During 2025, we established a commercial paper program under which we may issue unsecured commercial paper notes from time to time up to a maximum aggregate face or principal amount of $4.000 billion outstanding at any time. Amounts available under the program may be borrowed, repaid and reborrowed from time to time. The maturities of the commercial paper notes borrowings may vary, but will not exceed 397 days from the date of issue, and the proceeds from the program will be used for general corporate purposes. In connection with the commercial paper program, we intend to maintain a minimum available borrowing capacity under our $8.000 billion senior unsecured credit facility equal to the aggregate amount outstanding under the commercial paper program. At December 31, 2025, we had $2.207 billion of commercial paper outstanding, and there were no borrowings outstanding under our senior unsecured credit facility.
> During 2025, we repaid at maturity all $2.600 billion aggregate principal amount of 5.375% senior notes, all $1.400 billion aggregate principal amount of 5.25% senior notes, $291 million aggregate principal amount of 7.69% senior notes and $125 million aggregate principal amount of 7.58% medium-term notes. We also redeemed all $1.500 billion aggregate principal amount of 5.875% senior notes due 2026.

### HCA-000119312526044769-0418

debt_note, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 479508–480869

> During 2025, we established a commercial paper program under which we may issue unsecured commercial paper notes from time to time up to a maximum aggregate face or principal amount of $4.000 billion outstanding at any time. Amounts available under the program may be borrowed, repaid and reborrowed from time to time. The maturities of the commercial paper notes borrowings may vary, but will not exceed 397 days from the date of issue, and the proceeds from the program will be used for general corporate purposes. In connection with the commercial paper program, we intend to maintain a minimum available borrowing capacity under our $8.000 billion senior unsecured credit facility equal to the aggregate amount outstanding under the commercial paper program. At December 31, 2025, we had $2.207 billion of commercial paper outstanding, and there were no borrowings outstanding under our senior unsecured credit facility.
> Senior Unsecured Notes
> Senior unsecured notes consist of (i) $43.250 billion aggregate principal amount of senior notes with maturities ranging from 2026 to 2064 and (ii) an aggregate principal amount of $450 million debentures with maturities ranging from 2027 to 2095.
> General Debt Information
> Maturities of long-term debt in years 2027 through 2030 are $2.547 billion, $3.645 billion, $3.577 billion and $4.021 billion, respectively.

### HCA-000119312526191444-0055

liquidity, [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526191444/hca-20260331.htm), characters 68102–69032

> Cash used in financing activities totaled $830 million in the first quarter of 2026, compared to $1.495 billion in the first quarter of 2025. During the first quarter of 2026, net cash flows used in financing activities included a net increase of $1.377 billion in our indebtedness, payment of dividends of $183 million, repurchase of common stock of $1.571 billion and distributions to noncontrolling interests of $191 million. During the first quarter of 2025, net cash flows used in financing activities included a net increase of $1.558 billion in our indebtedness, payment of dividends of $180 million, repurchase of common stock of $2.506 billion and distributions to noncontrolling interests of $220 million.
> We have significant debt service requirements. Our debt totaled $48.023 billion at March 31, 2026. Our interest expense was $584 million for the first quarter of 2026 and $547 million for the first quarter of 2025.

### HCA-000119312526321077-0007

financial_statements, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 10268–11726

> FOR THE SIX MONTHS ENDED JUNE 30, 2026 AND 2025
> Unaudited
> (Dollars in millions)
> 2026
> 2025
> Cash flows from operating activities:
> Net income
> $
> 3,787
> $
> 3,716
> Adjustments to reconcile net income to net cash provided by operating activities:
> Increase (decrease) in cash from operating assets and liabilities:
> Accounts receivable
> (1,417
> )
> 320
> Inventories and other assets
> (26
> )
> (427
> )
> Accounts payable and accrued expenses
> (439
> )
> (676
> )
> Depreciation and amortization
> 1,874
> 1,723
> Income taxes
> 269
> 880
> Losses (gains) on sales of facilities
> (9
> )
> 2
> Amortization of debt issuance costs and discounts
> 23
> 25
> Share-based compensation
> 171
> 197
> Other
> 116
> 101
> Net cash provided by operating activities
> 4,349
> 5,861
> Cash flows from investing activities:
> Purchase of property and equipment
> (2,350
> )
> (2,167
> )
> Acquisition of hospitals and health care entities
> (386
> )
> (326
> )
> Sales of hospitals and health care entities
> 21
> 167
> Change in investments
> (120
> )
> 41
> Other
> (4
> )
> 2
> Net cash used in investing activities
> (2,839
> )
> (2,283
> )
> Cash flows from financing activities:
> Issuance of long-term debt
> 2,994
> 5,233
> Net change in short-term borrowings and revolving credit facility
> 2,679
> 1,768
> Repayment of long-term debt
> (2,608
> )
> (5,660
> )
> Distributions to noncontrolling interests
> (334
> )
> (394
> )
> Payment of debt issuance costs
> (17
> )
> (57
> )
> Payment of dividends
> (354
> )
> (351
> )
> Repurchase of common stock
> (3,635
> )
> (5,011
> )
> Other
> (259
> )
> (112
> )
> Net cash used in financing activities
> (1,534
> )
> (4,584
> )

### HCA-000119312526321077-0038

mdna, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 50682–51616

> Cash flows from operating activities declined $1.875 billion, from $4.210 billion for the second quarter of 2025 to $2.335 billion for the second quarter of 2026. The decline in cash provided by operating activities was primarily related to unfavorable working capital changes of $1.413 billion, including an increase in accounts receivable primarily related to Medicaid state directed and supplemental payment programs, as well as an increase in income taxes paid of $594 million related to the 2025 Internal Revenue Service (“IRS”) deferral of quarterly estimated income tax payments for Tennessee-based taxpayers until the fourth quarter of 2025, partially offset by a $28 million increase in net income, excluding the non-cash impact of losses and gains on sales of facilities.
> 18
> ITEM 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF
> FINANCIAL CONDITION AND RESULTS OF OPERATIONS (Continued)
> Results of Operations
> Revenue/Volume Trends

### HCA-000119312526321077-0066

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 82185–83601

> Cash used in investing activities was $2.839 billion in the first six months of 2026 compared to $2.283 billion in the first six months of 2025. Excluding acquisitions, capital expenditures were $2.350 billion in the first six months of 2026 and $2.167 billion in the first six months of 2025. Planned capital expenditures are expected to be approximately between $5.0 billion and $5.5 billion in 2026, excluding acquisitions. At June 30, 2026, there were projects under construction which had estimated additional costs to complete and equip over the next five years of approximately $8.6 billion. We expect to finance capital expenditures with internally generated and borrowed funds.
> Cash used in financing activities totaled $1.534 billion in the first six months of 2026, compared to $4.584 billion in the first six months of 2025. During the first six months of 2026, net cash flows used in financing activities included a net increase of $3.065 billion in our indebtedness, payment of dividends of $354 million, repurchase of common stock of $3.635 billion and distributions to noncontrolling interests of $334 million. During the first six months of 2025, net cash flows used in financing activities included a net increase of $1.341 billion in our indebtedness, payment of dividends of $351 million, repurchase of common stock of $5.011 billion and distributions to noncontrolling interests of $394 million.

### HCA-000119312526321077-0068

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 84624–85224

> In addition to cash flows from operations, available sources of capital include amounts available under our senior unsecured credit facility ($3.086 billion and $3.816 billion available as of June 30, 2026 and July 24, 2026, respectively, after giving effect to all issued and outstanding letters of credit and our intention to maintain a minimum available borrowing capacity equal to the aggregate amount outstanding under the commercial paper program ($3.890 billion and $4.000 billion as of June 30, 2026 and July 24, 2026, respectively)) and anticipated access to public and private debt markets.

### HCA-000119312526437871-0023

debt_note, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/hca-20260930.htm), characters 29947–31349

> NOTE 7 — DEBT
> A summary of our debt at September 30, 2026 and December 31, 2025, including related interest rates at September 30, 2026, follows (dollars in millions):
> September 30,
> 2026
> December 31,
> 2025
> Short-term borrowings:
> Commercial paper (average life of 26 days, weighted average rate of 4.2%)
> $
> 5,727
> $
> 2,207
> Long-term debt:
> Other debt (effective interest rate of 5.0%)
> 1,005
> 1,021
> Senior unsecured credit facility
> —
> —
> Senior unsecured notes payable through 2095 (effective interest rate of 5.1%)
> 44,200
> 43,700
> Debt issuance costs and discounts
> (439
> )
> (436
> )
> Total long-term debt (average life of 11.6 years, rates averaging 5.1%)
> 44,766
> 44,285
> Total debt
> 50,493
> 46,492
> Less amounts due within one year
> (8,093
> )
> (4,889
> )
> $
> 42,400
> $
> 41,603
> During April 2026, we issued $3.000 billion aggregate principal amount of senior notes comprised of (i) $1.000 billion aggregate principal amount of 4.700% senior notes due 2031, (ii) $750 million aggregate principal amount of 5.000% senior notes due 2033 and (iii) $1.250 billion aggregate principal amount of 5.300% senior notes due 2036. We used the net proceeds to repay borrowings under our commercial paper program (“CPP”) and for general corporate purposes.
> During May 2026, we redeemed all $1.500 billion aggregate principal amount of 5.250% senior notes due 2026 and all $1.000 billion aggregate principal amount of 5.375% senior notes due 2026.

## Run

Run `HCA-20261118T051136Z-DeepSeek-V4.1-Flash-1017`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 7 calls, 27,249 input (5,632 cached) and 17,761 output tokens, $0.0073, 381s. Verification: 35 calls, 16,480 input (4,480 cached) and 3,530 output tokens, $0.0234, 83s. Prices read 2026-11-17. Raw requests and responses: data/runs/HCA/HCA-20261118T051136Z-DeepSeek-V4.1-Flash-1017.jsonl.
