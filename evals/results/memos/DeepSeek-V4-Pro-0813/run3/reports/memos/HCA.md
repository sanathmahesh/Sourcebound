# Credit memo: HCA Healthcare, Inc. (HCA)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4-Pro-0813`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-4**.
Sources: [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm); [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526191444/hca-20260331.htm); [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm)

Claims: 34 — 30 supported, 3 partially supported, 1 unsupported. Raw numbers rejected in first drafts: 3; repairs: 2.

## Business profile

1. Revenue was **$65.0 billion** [F1] in the fiscal year ended 31 December 2023, **$70.6 billion** [F2] in the fiscal year ended 31 December 2024, **$75.6 billion** [F3] in the fiscal year ended 31 December 2025, and **$78.7 billion** [F4] in the twelve months to 30 September 2026.  
   ✅ supported (judge): All four revenue figures match the metric values exactly.
2. EBITDA was **$15.6 billion** [F5] in the fiscal year ended 31 December 2025 and **$15.9 billion** [F6] in the twelve months to 30 September 2026.  
   ✅ supported (judge): Both claimed EBITDA figures match the metric values exactly.
3. HCA Healthcare is one of the leading health care services companies in the United States and, at the end of the fiscal year ended 31 December 2025, operated **190** [quoted: HCA-000119312526044769-0004] hospitals.  
   ✅ supported (judge): Both the leading health care services claim and the 190 hospitals at December 31, 2025 are directly stated.
   - cites `HCA-000119312526044769-0004` ✓: “HCA Healthcare, Inc. is one of the leading health care services companies in the United States.”
   - cites `HCA-000119312526044769-0004` ✓: “we operated 190 hospitals, comprised of 179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals.”
4. Its facilities include **179** [quoted: HCA-000119312526044769-0004] general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals, as well as **121** [quoted: HCA-000119312526044769-0004] freestanding ambulatory surgery centers and **31** [quoted: HCA-000119312526044769-0004] freestanding endoscopy centers.  
   ✅ supported (judge): The claim exactly matches the passage listing hospital and facility counts.
   - cites `HCA-000119312526044769-0004` ✓: “179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals. In addition, we operated 121 freestanding ambulatory surgery centers (“ASCs”) and 31 freestanding endoscopy centers.”
5. Its facilities are located in **19** [quoted: HCA-000119312526044769-0004] states and England.  
   ✅ supported (judge): The filing states facilities are located in 19 states and England.
   - cites `HCA-000119312526044769-0004` ✓: “Our facilities are located in 19 states and England.”
6. Admissions, average lengths of stay and reimbursement amounts continue to be negatively affected by third-party payer pre-admission authorization requirements, utilization review and pressure to maximize outpatient services.  
   ✅ supported (judge): The claim matches the filing passage almost verbatim, differing only in omitting 'and alternative health care delivery services for less acutely ill patients' after 'outpatient', which does not change the substance.
   - cites `HCA-000119312526044769-0079` ✓: “Admissions, average lengths of stay and reimbursement amounts continue to be negatively affected by third-party payer pre-admission authorization requirements, utilization review and pressure to maximize outpatient”

## Financial risk

1. Debt / EBITDA was **3.17x** [F7] in the fiscal year ended 31 December 2023 and **3.17x** [F8] in the twelve months to 30 September 2026, while net leverage was **3.09x** [F9] and **3.11x** [F10], respectively, indicating broadly stable leverage.  
   ✅ supported (judge): All four leverage figures in the claim (3.17x, 3.17x, 3.09x, 3.11x) match the computed metric values, and 'broadly stable' follows directly from the essentially unchanged ratios.
2. EBITDA / interest was **6.56x** [F11] in the fiscal year ended 31 December 2023 and **6.74x** [F12] in the twelve months to 30 September 2026, and FCF / debt was **11.6%** [F13] and **11.8%** [F14], respectively, indicating stable debt service capacity.  
   ✅ supported (judge): All four ratio values (6.56x, 6.74x, 11.6%, 11.8%) exactly match the computed metric values, and the near-identical figures reasonably indicate stable debt service capacity.
3. Total debt increased from **$47.2 billion** [F15] at the fiscal year ended 31 December 2025 to **$50.5 billion** [F16] at the twelve months to 30 September 2026, reflecting higher average debt balances.  
   ◐ partially supported (judge): The debt figures ($47.2B to $50.5B) are supported by the metric values, but the explanation that this reflects higher average debt balances is not evidenced for those periods — the average debt balance passage covers 2025 vs 2024.
   - cites `HCA-000119312526044769-0295` ✓: “Our average debt balance was $44.731 billion for 2025 compared to $41.388 billion for 2024.”
4. Interest expense increased in **2025** [quoted: HCA-000119312526044769-0295] primarily because the average debt balance increased, while the average effective interest rate on long-term debt was **5.0** [quoted: HCA-000119312526044769-0295]% for both **2025** [quoted: HCA-000119312526044769-0295] and **2024** [quoted: HCA-000119312526044769-0295].  
   ✅ supported (judge): The passage explicitly states the interest expense increase was primarily due to higher average debt balance and that the average effective interest rate on long-term debt was 5.0% in both years.
   - cites `HCA-000119312526044769-0295` ✓: “The $187 million increase in interest expense was primarily due to an increase in the average debt balance.”
   - cites `HCA-000119312526044769-0295` ✓: “The average effective interest rate for our long-term debt was 5.0% for both 2025 and 2024.”
5. Operating cash flow declined in the first half of **2026** [quoted: HCA-000119312526321077-0064] mainly due to unfavorable working capital changes, contributing to the worsening liquidity coverage.  
   ◐ partially supported (judge): The decline and its working capital cause are supported, but the 'worsening liquidity coverage' part is not addressed by the evidence.
   - cites `HCA-000119312526321077-0064` ✓: “Cash provided by operating activities totaled $4.349 billion for the first six months of 2026 compared to $5.861 billion for the first six months of 2025.”
   - cites `HCA-000119312526321077-0064` ✓: “related primarily to unfavorable changes in working capital items”

## Liquidity

1. For the twelve months ended the twelve months to 30 September 2026, liquidity coverage was **0.86x** [F17], compared with **1.30x** [F18] for the fiscal year ended 31 December 2025.  
   ✅ supported (judge): Both liquidity coverage figures (0.86x for the twelve months to 30 September 2026 and 1.30x for the fiscal year ended 31 December 2025) match the metric values computed from the XBRL data.
2. For the twelve months ended the twelve months to 30 September 2026, cash and cash equivalents were **$908 million** [F19], cash from operations was **$11.2 billion** [F20], capital expenditures were **$5.2 billion** [F21], dividends paid were **$681 million** [F22], and short-term debt was **$8.1 billion** [F23].  
   ✅ supported (judge): All five figures match the computed XBRL metric values for the twelve months to 30 September 2026.
3. The company entered into a new credit agreement in **2025** [quoted: HCA-000119312526044769-0304] that provides for $**8.000** [quoted: HCA-000119312526044769-0304] billion of senior unsecured revolving credit commitments with a term of five years.  
   ✅ supported (judge): The passage directly states all elements of the claim: new credit agreement in 2025, $8.000 billion senior unsecured revolving commitments, five-year term.
   - cites `HCA-000119312526044769-0304` ✓: “During 2025, we entered into a new credit agreement that provides for $8.000 billion of senior unsecured revolving credit commitments with a term of five years”
4. As of July **24** [quoted: HCA-000119312526321077-0068], **2026** [quoted: HCA-000119312526321077-0068], availability under the senior unsecured credit facility was $**3.816** [quoted: HCA-000119312526321077-0068] billion, after giving effect to issued and outstanding letters of credit and the minimum borrowing capacity related to the commercial paper program.  
   ✅ supported (judge): The passage states $3.816 billion available as of July 24, 2026 after letters of credit and minimum borrowing capacity for the commercial paper program.
   - cites `HCA-000119312526321077-0068` ✓: “$3.086 billion and $3.816 billion available as of June 30, 2026 and July 24, 2026, respectively, after giving effect to all issued and outstanding letters of credit”
5. Management expects **2026** [quoted: HCA-000119312526437871-0066] capital expenditures, excluding acquisitions, to be between $**5.0** [quoted: HCA-000119312526437871-0066] billion and $**5.5** [quoted: HCA-000119312526437871-0066] billion.  
   ✅ supported (judge): The passage states planned capital expenditures excluding acquisitions are expected to be between $5.0 billion and $5.5 billion in 2026.
   - cites `HCA-000119312526437871-0066` ✓: “Planned capital expenditures are expected to be between $5.0 billion and $5.5 billion in 2026, excluding acquisitions.”
6. The company expects to finance capital expenditures with internally generated and borrowed funds.  
   ✅ supported (judge): The passage explicitly states the company expects to finance capital expenditures with internally generated and borrowed funds.
   - cites `HCA-000119312526437871-0066` ✓: “We expect to finance capital expenditures with internally generated and borrowed funds.”

## Maturity wall

1. As of the fiscal year ended 31 December 2025, debt maturing in year two was **$2.5 billion** [F24], in year three **$3.6 billion** [F25], in year four **$3.6 billion** [F26], and in year five **$4.0 billion** [F27].  
   ✅ supported (judge): All four maturity values match the metric values computed from XBRL data.
2. Debt due within the short-term maturity window captured by **$7.4 billion** [F28] was **$7.4 billion** [F28], representing **15.7%** [F29] of total debt of **$47.2 billion** [F15] as of the fiscal year ended 31 December 2025.  
   ✅ supported (judge): All figures ($7.4B short-term debt, 15.7%, $47.2B total) match the computed metric values for FY0.
3. Near-term maturity cover was **7.15x** [F30] as of the fiscal year ended 31 December 2025.  
   ✅ supported (judge): The claimed 7.15x near-term maturity cover for FY ended 31 December 2025 matches the metric value computed from the company's XBRL data (with short-term investments and undrawn revolver assumed zero as not reported).
4. Senior unsecured notes and debentures have maturities that extend beyond the five-year maturity schedule.  
   ✅ supported (judge): Senior unsecured notes have maturities up to 2064 and debentures up to 2095, well beyond the five-year maturity schedule.
   - cites `HCA-000119312526044769-0418` ✓: “maturities ranging from 2026 to 2064”
   - cites `HCA-000119312526044769-0418` ✓: “debentures with maturities ranging from 2027 to 2095”
5. During the fiscal year ended 31 December 2025, HCA issued $**5.250** [quoted: HCA-000119312526044769-0415] billion aggregate principal amount of senior notes and used the net proceeds to repay borrowings under the senior unsecured credit facility and for general corporate purposes.  
   ✅ supported (judge): The filing explicitly states the issuance amount and use of proceeds exactly as claimed.
   - cites `HCA-000119312526044769-0415` ✓: “We issued $5.250 billion aggregate principal amount of senior notes”
   - cites `HCA-000119312526044769-0415` ✓: “We used the net proceeds to repay borrowings under the senior unsecured credit facility and for general corporate purposes.”
6. At the fiscal year ended 31 December 2025, HCA had $**2.207** [quoted: HCA-000119312526044769-0418] billion of commercial paper outstanding and no borrowings outstanding under its senior unsecured credit facility.  
   ✅ supported (judge): The passage states both the $2.207 billion commercial paper outstanding and no borrowings under the senior unsecured credit facility at December 31, 2025.
   - cites `HCA-000119312526044769-0418` ✓: “At December 31, 2025, we had $2.207 billion of commercial paper outstanding, and there were no borrowings outstanding under our senior unsecured credit facility.”

## Key risks

1. The company's significant indebtedness requires a portion of cash flows from operations to be dedicated to principal and interest, reducing its ability to use its cash flows.  
   ✅ supported (judge): The passage directly states that debt requires dedicating a portion of operating cash flows to principal and interest, reducing ability to use cash flows.
   - cites `HCA-000119312526044769-0145` ✓: “requiring a portion of cash flows from operations to be dedicated to the payment of principal and interest on our indebtedness, therefore reducing our ability to use our cash flows”
2. The company's ability to refinance its indebtedness on favorable terms, or at all, is directly affected by prevailing global economic and financial conditions.  
   ✅ supported (judge): The claim is a direct restatement of the passage.
   - cites `HCA-000119312526044769-0147` ✓: “Our ability to refinance our indebtedness on favorable terms, or at all, is directly affected by the then current global economic and financial conditions”
3. A covenant breach could lead to a situation in which there is no assurance of sufficient assets to repay the senior unsecured credit facility and other indebtedness.  
   ✅ supported (judge): The passage explicitly states that a covenant breach could trigger acceleration with no assurance of sufficient assets to repay the senior unsecured credit facility and other indebtedness.
   - cites `HCA-000119312526044769-0149` ✓: “there can be no assurance there will be sufficient assets to repay our senior unsecured credit facility and our other indebtedness.”
4. The company is exposed to higher interest costs on variable-rate borrowings or when refinancing debt in a rising- or high-rate environment.  
   ✅ supported (judge): The passage explicitly states the risk of increased interest rates on variable-rate borrowings or when refinancing debt in a rising or high rate environment.
   - cites `HCA-000119312526044769-0145` ✓: “increased interest rates on our existing borrowings that are at variable rates of interest or refinancing our debt in a rising or high rate environment”
5. There can be no assurance that the company will be able to raise additional funds on terms acceptable to it, if at all.  
   ✅ supported (judge): The claim is stated verbatim in the evidence passage.
   - cites `HCA-000119312526044769-0233` ✓: “There can be no assurance that we will be able to raise additional funds on terms acceptable to us, if at all.”

## Rating rationale

1. The scorecard results in an SB grade of **SB-4** [F31] and a weighted score of **4.25** [F32]; the grade is not provisional because all six factors were scored, and the SB grade is a stylized internal scorecard grade, not a credit rating.  
   ✅ supported (judge): All claim components match the computed scorecard metrics exactly.
2. The strongest scorecard factor is EBITDA / interest, which scores band **3** [F33] with a weight of **25.0%** [F34] against an LTM value of **6.74x** [F12].  
   ✅ supported (judge): EBITDA / interest has the strongest (lowest) band of the six factors at 3, with weight 25.0% and LTM 6.74x, all matching the evidence.
3. The weakest scorecard factors are liquidity sources / uses, at band **6** [F35] with a weight of **15.0%** [F36] and an LTM value of **0.86x** [F17], and the near-term maturity cover factor, at band **6** [F37] with a weight of **10.0%** [F38] and an FY0 value of **7.15x** [F30].  
   ❌ unsupported (deterministic): unsupported: number check failed: number not from a placeholder or a cited passage: 0
   - flag: kept after failed repair: number not from a placeholder or a cited passage: 0
4. Leverage and free cash flow factors fall in the middle of the scorecard: Debt / EBITDA is band **4** [F39] with weight **20.0%** [F40] and value **3.17x** [F8], net debt / EBITDA is band **4** [F41] with weight **10.0%** [F42] and value **3.11x** [F10], and FCF / debt is band **4** [F43] with weight **20.0%** [F44] and value **11.8%** [F14].  
   ✅ supported (judge): All figures match: Debt/EBITDA band 4, weight 20.0%, 3.17x; net debt/EBITDA band 4, weight 10.0%, 3.11x; FCF/debt band 4, weight 20.0%, 11.8%, and band 4 of 6 is mid-scorecard.
5. The scorecard outcome is supported by HCA's scale as one of the leading health care services companies in the United States, with **190** [quoted: HCA-000119312526044769-0004] hospitals operated at the end of the fiscal year ended 31 December 2025.  
   ✅ supported (judge): The passage states HCA is one of the leading health care services companies in the U.S. and operated 190 hospitals at December 31, 2025, matching the claim.
   - cites `HCA-000119312526044769-0004` ✓: “one of the leading health care services companies in the United States. At December 31, 2025, we operated 190 hospitals”
6. Third-party payer pressure, admission constraints and the obligation to dedicate operating cash flow to debt service temper the scorecard assessment.  
   ◐ partially supported (judge): The evidence supports third-party payer pressure, admission constraints, and debt service obligations, but nothing in the passages or scorecard metrics explicitly states these factors temper the scorecard assessment.
   - cites `HCA-000119312526044769-0079` ✓: “Admissions, average lengths of stay and reimbursement amounts continue to be negatively affected by third-party payer pre-admission authorization requirements”
   - cites `HCA-000119312526044769-0145` ✓: “requiring a portion of cash flows from operations to be dedicated to the payment of principal and interest on our indebtedness”

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
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The debt figures ($47.2B to $50.5B) are supported by the metric values, but the explanation that this reflects higher average debt balances is not evidenced for those periods — the average debt balance passage covers 2025 vs 2024.): “Total debt increased from $47.2 billion at the fiscal year ended 31 December 2025 to $50.5 billion at the twelve months to 30 September 2026, reflecting higher average debt balances.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The decline and its working capital cause are supported, but the 'worsening liquidity coverage' part is not addressed by the evidence.): “Operating cash flow declined in the first half of 2026 mainly due to unfavorable working capital changes, contributing to the worsening liquidity coverage.”
- [ ] **unsupported claim** (warning): Rating rationale: unsupported (unsupported: number check failed: number not from a placeholder or a cited passage: 0): “The weakest scorecard factors are liquidity sources / uses, at band 6 with a weight of 15.0% and an LTM value of 0.86x, and the near-term maturity cover factor, at band 6 with a weight of 10.0% and an FY0 value of 7.15x.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The evidence supports third-party payer pressure, admission constraints, and debt service obligations, but nothing in the passages or scorecard metrics explicitly states these factors temper the scorecard assessment.): “Third-party payer pressure, admission constraints and the obligation to dedicate operating cash flow to debt service temper the scorecard assessment.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $65.0 billion | rank 1: Revenues | Revenues 64,968,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F2 | Revenue (revenue:FY-1) | $70.6 billion | rank 1: Revenues | Revenues 70,603,000,000 (2024-01-01 to 2024-12-31, FY-1) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F3 | Revenue (revenue:FY0) | $75.6 billion | rank 1: Revenues | Revenues 75,600,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F4 | Revenue (revenue:LTM) | $78.7 billion | rank 1: Revenues | Revenues 75,600,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>Revenues 59,188,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>Revenues 56,087,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F5 | EBITDA (ebitda:FY0) | $15.6 billion | operating_income + d_and_a | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F6 | EBITDA (ebitda:LTM) | $15.9 billion | operating_income + d_and_a | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 1,676,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 2,828,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY-2) | 3.17x | total_debt / EBITDA | LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,706,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,077,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:LTM) | 3.17x | total_debt / EBITDA | LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 1,676,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F9 | Net leverage (net_leverage:FY-2) | 3.09x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 935,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,706,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,077,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F10 | Net leverage (net_leverage:LTM) | 3.11x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F11 | EBITDA / interest (interest_coverage:FY-2) | 6.56x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,706,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,077,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,938,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F12 | EBITDA / interest (interest_coverage:LTM) | 6.74x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,151,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 7,160,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 1,790,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>InterestExpense 1,676,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 2,828,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F13 | FCF / debt (fcf_to_debt:FY-2) | 11.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 9,431,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,744,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| F14 | FCF / debt (fcf_to_debt:LTM) | 11.8% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F15 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $47.2 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F16 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $50.5 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F17 | Liquidity coverage (liquidity_coverage:LTM) | 0.86x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F18 | Liquidity coverage (liquidity_coverage:FY0) | 1.30x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsOfDividends 679,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F19 | Cash and cash equivalents (cash:LTM) | $908 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F20 | Cash from operations (cfo:LTM) | $11.2 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F21 | Capital expenditure (capex:LTM) | $5.2 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F22 | Dividends paid (dividends:LTM) | $681 million | rank 1: PaymentsOfDividends | PaymentsOfDividends 679,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsOfDividends 519,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsOfDividends 517,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F23 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $8.1 billion | rank 1: DebtCurrent | DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F24 | Debt maturing in year two (maturity_year_2:FY0) | $2.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F25 | Debt maturing in year three (maturity_year_3:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 3,645,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F26 | Debt maturing in year four (maturity_year_4:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 3,577,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F27 | Debt maturing in year five (maturity_year_5:FY0) | $4.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 4,021,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F28 | Debt due within 24 months (debt_due_24m:FY0) | $7.4 billion | short_term_debt + maturity_year_2 | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F29 | Share of debt due within 24 months (share_due_24m:FY0) | 15.7% | (short_term_debt + maturity_year_2) / total_debt | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F30 | Near-term maturity cover (near_term_maturity_cover:FY0) | 7.15x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F31 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 4.25 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F32 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 4.25 | sum of weight x band over the factors scored, divided by their weights | — |
| F33 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 3 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F34 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F35 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F36 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F37 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 6 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F38 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F39 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 4 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F40 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F41 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 4 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F42 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F43 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 4 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F44 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### HCA-000119312526044769-0004

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 5633–6593

> Item 1. Business
> General
> HCA Healthcare, Inc. is one of the leading health care services companies in the United States. At December 31, 2025, we operated 190 hospitals, comprised of 179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals. In addition, we operated 121 freestanding ambulatory surgery centers (“ASCs”) and 31 freestanding endoscopy centers. Our facilities are located in 19 states and England.
> The terms “Company,” “HCA,” “HCA Healthcare,” “we,” “our” or “us,” as used herein and unless otherwise stated or indicated by context, refer to HCA Healthcare, Inc. and its affiliates. The term “affiliates” means direct and indirect subsidiaries of HCA Healthcare, Inc. and partnerships and joint ventures in which such subsidiaries are partners. The terms “facilities” or “hospitals” refer to entities owned and operated by affiliates of HCA, and the term “employees” refers to employees of affiliates of HCA.

### HCA-000119312526044769-0079

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 93332–94732

> In addition, changes in licensure or other laws or regulations and recognition of new provider types or payment models could impact our competitive position. See Item 1, “Business — Regulation and Other Factors.”
> We and the health care industry as a whole face the challenge of continuing to provide quality patient care while dealing with rising costs and strong competition for patients. Changes in medical technology, existing and future legislation, regulations and interpretations and contracting for provider services by third-party payers remain ongoing challenges.
> Admissions, average lengths of stay and reimbursement amounts continue to be negatively affected by third-party payer pre-admission authorization requirements, utilization review and pressure to maximize outpatient and alternative health care delivery services for less acutely ill patients. Increased competition, admission constraints and third-party payer pressures are expected to continue. To meet these challenges, we intend to expand and update our facilities or acquire or construct new facilities where appropriate, enhance the provision of a comprehensive array of outpatient services, offer market competitive pricing to group purchasers of health care services, upgrade facilities and equipment and offer new or expanded programs and services.
> Regulation and Other Factors
> Licensure, Certification and Accreditation

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

### HCA-000119312526044769-0233

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 268093–269564

> Other risks we face during periods of economic weakness and high unemployment include potential declines in the population covered under managed care agreements, increased patient decisions to postpone or cancel elective and nonemergency health care procedures (including delaying surgical procedures), which may lead to poorer health and higher acuity interventions, potential increases in the uninsured and underinsured populations, increased adoption of health plan structures that shift financial responsibility to patients and further difficulties in collecting patient receivables for copayment and deductible receivables. Further, inflationary pressures and tariffs may increase operating expenses to a greater degree and faster than reflected in updates to the reimbursement systems of governmental and private payers. General economic conditions, including inflation, when worsening or remaining volatile for an extended period of time, have and may continue to have, a negative impact on our results of operations, liquidity, ability to repay our outstanding debt and trading price of our common stock. These factors may affect the
> 51
> availability, terms or timing on which we may obtain any additional funding and our ability to access our cash. There can be no assurance that we will be able to raise additional funds on terms acceptable to us, if at all.
> We are exposed to market risk related to changes in the market values of securities and interest rates.

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

### HCA-000119312526044769-0304

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 347579–348410

> Financing Activities (continued)
> During 2025, we entered into a new credit agreement that provides for $8.000 billion of senior unsecured revolving credit commitments with a term of five years (“senior unsecured credit facility”). Borrowings under the senior unsecured credit facility bear interest at a rate equal to the Secured Overnight Financing Rate plus 1.125% (plus, until October 23, 2025, a 0.10% credit spread adjustment, as the unsecured credit facility was amended on that date to remove the credit spread adjustment). We terminated our $4.500 billion senior secured asset-based revolving credit facility, our $3.500 billion senior secured revolving cash flow credit facility and our senior secured term loan facility of $1.238 billion. Finance leases and other secured debt totaled $1.021 billion at December 31, 2025.

### HCA-000119312526044769-0415

debt_note, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 476122–477601

> NOTE 8 — DEBT
> A summary of our debt at December 31, 2025 and December 31, 2024, including related interest rates at December 31, 2025, follows (dollars in millions):
> 2025
> 2024
> Short-term borrowings:
> Commercial paper (average life of 18 days, weighted average rate of 4.3%)
> $
> 2,207
> $
> —
> Long-term debt:
> Senior secured term loan facility
> —
> 1,238
> Other senior secured debt (effective interest rate of 4.6%)
> 1,021
> 1,046
> Senior unsecured credit facilities
> —
> —
> Senior unsecured notes payable through 2095 (effective interest rate of 5.1%)
> 43,700
> 41,116
> Debt issuance costs and discounts
> (436
> )
> (369
> )
> Total long-term debt (average life of 11.9 years, rates averaging 5.1%)
> 44,285
> 43,031
> Total debt
> 46,492
> 43,031
> Less amounts due within one year
> 4,889
> 4,698
> $
> 41,603
> $
> 38,333
> 2025 Financing Activities
> We issued $5.250 billion aggregate principal amount of senior notes comprised of (i) $700 million aggregate principal amount of 5.000% senior notes due 2028, (ii) $300 million aggregate principal amount of floating rate senior notes due 2028, (iii) $750 million aggregate principal amount of 5.250% senior notes due 2030, (iv) $750 million aggregate principal amount of 5.500% senior notes due 2032, (v) $1.500 billion aggregate principal amount of 5.750% senior notes due 2035 and (vi) $1.250 billion aggregate principal amount of 6.200% senior notes due 2055. We used the net proceeds to repay borrowings under the senior unsecured credit facility and for general corporate purposes.

### HCA-000119312526044769-0418

debt_note, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 479508–480869

> During 2025, we established a commercial paper program under which we may issue unsecured commercial paper notes from time to time up to a maximum aggregate face or principal amount of $4.000 billion outstanding at any time. Amounts available under the program may be borrowed, repaid and reborrowed from time to time. The maturities of the commercial paper notes borrowings may vary, but will not exceed 397 days from the date of issue, and the proceeds from the program will be used for general corporate purposes. In connection with the commercial paper program, we intend to maintain a minimum available borrowing capacity under our $8.000 billion senior unsecured credit facility equal to the aggregate amount outstanding under the commercial paper program. At December 31, 2025, we had $2.207 billion of commercial paper outstanding, and there were no borrowings outstanding under our senior unsecured credit facility.
> Senior Unsecured Notes
> Senior unsecured notes consist of (i) $43.250 billion aggregate principal amount of senior notes with maturities ranging from 2026 to 2064 and (ii) an aggregate principal amount of $450 million debentures with maturities ranging from 2027 to 2095.
> General Debt Information
> Maturities of long-term debt in years 2027 through 2030 are $2.547 billion, $3.645 billion, $3.577 billion and $4.021 billion, respectively.

### HCA-000119312526321077-0064

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 80633–81032

> Liquidity and Capital Resources
> Cash provided by operating activities totaled $4.349 billion for the first six months of 2026 compared to $5.861 billion for the first six months of 2025. The $1.512 billion decline in cash provided by operating activities, for the first six months of 2026 compared to the first six months of 2025, related primarily to unfavorable changes in working capital items of

### HCA-000119312526321077-0068

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 84624–85224

> In addition to cash flows from operations, available sources of capital include amounts available under our senior unsecured credit facility ($3.086 billion and $3.816 billion available as of June 30, 2026 and July 24, 2026, respectively, after giving effect to all issued and outstanding letters of credit and our intention to maintain a minimum available borrowing capacity equal to the aggregate amount outstanding under the commercial paper program ($3.890 billion and $4.000 billion as of June 30, 2026 and July 24, 2026, respectively)) and anticipated access to public and private debt markets.

### HCA-000119312526437871-0066

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/hca-20260930.htm), characters 81385–82800

> Cash used in investing activities was $4.755 billion in the first nine months of 2026 compared to $3.671 billion in the first nine months of 2025. Excluding acquisitions, capital expenditures were $3.707 billion in the first nine months of 2026 and $3.455 billion in the first nine months of 2025. Planned capital expenditures are expected to be between $5.0 billion and $5.5 billion in 2026, excluding acquisitions. At September 30, 2026, there were projects under construction which had estimated additional costs to complete and equip over the next five years of approximately $8.6 billion. We expect to finance capital expenditures with internally generated and borrowed funds.
> Cash used in financing activities totaled $4.183 billion in the first nine months of 2026, compared to $7.551 billion in the first nine months of 2025. During the first nine months of 2026, net cash flows used in financing activities included a net increase of $3.788 billion in our indebtedness, payment of dividends of $519 million, repurchase of common stock of $6.605 billion and distributions to noncontrolling interests of $574 million. During the first nine months of 2025, net cash flows used in financing activities included a net increase of $1.305 billion in our indebtedness, payment of dividends of $517 million, repurchase of common stock of $7.509 billion and distributions to noncontrolling interests of $631 million.

## Run

Run `HCA-20261118T071152Z-DeepSeek-V4-Pro-0813`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 8 calls, 32,440 input (26,603 cached) and 61,273 output tokens, $0.1762, 1306s. Verification: 33 calls, 15,226 input (4,358 cached) and 2,716 output tokens, $0.0198, 41s. Prices read 2026-11-17. Raw requests and responses: data/runs/HCA/HCA-20261118T071152Z-DeepSeek-V4-Pro-0813.jsonl.
