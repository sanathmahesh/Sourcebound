# Credit memo: HCA Healthcare, Inc. (HCA)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4.1-Flash-1017`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-4**.
Sources: [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm); [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526191444/hca-20260331.htm); [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm)

Claims: 36 — 32 supported, 4 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 2; repairs: 2.

## Business profile

1. Revenue was **$65.0 billion** [F1] for the fiscal year ended 31 December 2023, **$70.6 billion** [F2] for the fiscal year ended 31 December 2024, **$75.6 billion** [F3] for the fiscal year ended 31 December 2025, and **$78.7 billion** [F4] for the twelve months to 30 September 2026.  
   ✅ supported (judge): All four revenue figures exactly match the XBRL-computed metric values cited.
2. EBITDA was **$15.6 billion** [F5] in the fiscal year ended 31 December 2025 and **$15.9 billion** [F6] in the twelve months to 30 September 2026.  
   ✅ supported (judge): Both EBITDA figures match the computed metric values exactly.
3. HCA is one of the leading health care services companies in the United States.  
   ✅ supported (judge): The passage directly states HCA Healthcare, Inc. is one of the leading health care services companies in the United States.
   - cites `HCA-000119312526044769-0004` ✓: “HCA Healthcare, Inc. is one of the leading health care services companies in the United States.”
4. Its facilities include general acute care, behavioral, and rehabilitation hospitals, as well as freestanding ambulatory surgery and endoscopy centers.  
   ✅ supported (judge): The passage states HCA operated general acute care, behavioral, and rehabilitation hospitals plus freestanding ambulatory surgery and endoscopy centers.
   - cites `HCA-000119312526044769-0004` ✓: “we operated 190 hospitals, comprised of 179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals.”
   - cites `HCA-000119312526044769-0004` ✓: “In addition, we operated 121 freestanding ambulatory surgery centers (“ASCs”) and 31 freestanding endoscopy centers.”
5. The company’s facilities are located in multiple states and England, which broadens its geographic footprint.  
   ✅ supported (judge): The filing states facilities are located in 19 states and England.
   - cites `HCA-000119312526044769-0004` ✓: “Our facilities are located in 19 states and England.”
6. Demand and reimbursement are exposed to third-party payer controls and competition for patients, which can pressure revenue stability.  
   ✅ supported (judge): The risk factors explicitly cite competition for patients and third-party payer controls that can reduce revenues.
   - cites `HCA-000119312526044769-0013` ✓: “Third-party payer controls designed to reduce costs and other payer practices intended to decrease inpatient services, surgical procedure volumes or reimbursement for services rendered may reduce our revenues.”
   - cites `HCA-000119312526044769-0013` ✓: “Our hospitals and other facilities face competition for patients from other hospitals and health care providers.”

## Financial risk

1. Debt / EBITDA was **3.17x** [F7] in the fiscal year ended 31 December 2023 and **3.17x** [F8] in the twelve months to 30 September 2026, while net leverage moved from **3.09x** [F9] to **3.11x** [F10], indicating stable leverage.  
   ✅ supported (judge): All four leverage figures in the claim match the computed XBRL metric values exactly, and characterizing 3.17x/3.17x and 3.09x→3.11x as stable leverage follows directly.
2. EBITDA / interest was **6.56x** [F11] in the fiscal year ended 31 December 2023 and **6.74x** [F12] in the twelve months to 30 September 2026, after **6.94x** [F13] in the fiscal year ended 31 December 2025, indicating stable debt service coverage.  
   ✅ supported (judge): All three coverage ratios (6.56x, 6.94x, 6.74x) match the computed metric values, and characterizing this narrow range as stable debt service coverage follows directly.
3. FCF / debt was **11.6%** [F14] in the fiscal year ended 31 December 2023 and **11.8%** [F15] in the twelve months to 30 September 2026, after **16.3%** [F16] in the fiscal year ended 31 December 2025, indicating stable free cash flow relative to debt.  
   ◐ partially supported (judge): The three ratio values match the metric scorecard exactly, but the characterization 'stable free cash flow relative to debt' is an interpretation that overstates the evidence — a middle-period spike to 16.3% between 11.6% and 11.8% suggests variability rather than stability, and the evidence contains no narrative supporting the stability conclusion.
4. Financing activity included long-term debt issuance and repayment as well as short-term borrowings, and a higher average debt balance contributed to increased interest expense.  
   ✅ supported (judge): Financing activities include long-term debt issuance and repayment and short-term borrowings, and the passage attributes the interest expense increase to a higher average debt balance.
   - cites `HCA-000119312526321077-0007` ✓: “Net change in short-term borrowings and revolving credit facility”
   - cites `HCA-000119312526044769-0295` ✓: “The $187 million increase in interest expense was primarily due to an increase in the average debt balance.”
5. Year-to-date operating cash flow declined compared with the prior-year period, which can pressure free cash flow and liquidity.  
   ✅ supported (judge): The passage states operating cash flow declined $1.512 billion year-to-date ($4.349B vs $5.861B), and the liquidity implication is a reasonable direct inference.
   - cites `HCA-000119312526321077-0064` ✓: “Cash provided by operating activities totaled $4.349 billion for the first six months of 2026 compared to $5.861 billion for the first six months of 2025.”
6. Capital spending remained a material use of cash, so free cash flow was generated after property and equipment purchases.  
   ✅ supported (judge): Operating cash flow of $4,349M exceeded the material $2,350M of property and equipment purchases, so free cash flow was generated after capex in both periods shown.
   - cites `HCA-000119312526321077-0007` ✓: “Purchase of property and equipment”

## Liquidity

1. Liquidity coverage was **1.30x** [F17] at the fiscal year ended 31 December 2025 but **0.86x** [F18] for the twelve months to 30 September 2026, so the metric shows weaker coverage of uses in the latest period.  
   ✅ supported (judge): The metric values show liquidity coverage of 1.30x at FY ended 31 December 2025 and 0.86x for the twelve months to 30 September 2026, matching the claim and its conclusion of weaker coverage.
2. For the twelve months to 30 September 2026, cash of **$908 million** [F19] and cash from operations of **$11.2 billion** [F20] are measured against short-term debt of **$8.1 billion** [F21], capital expenditure of **$5.2 billion** [F22] and dividends of **$681 million** [F23].  
   ✅ supported (judge): All figures in the claim match the computed metric values for the twelve months to 30 September 2026.
3. The coverage metric assumes no undrawn revolver capacity, while the company reports remaining availability under its senior unsecured credit facility after letters of credit and its intention to hold capacity equal to commercial paper outstanding.  
   ◐ partially supported (judge): The evidence supports the availability figures and the commercial paper capacity intention, but nothing in the evidence addresses the coverage metric or its assumption about undrawn revolver capacity.
   - cites `HCA-000119312526321077-0068` ✓: “available under our senior unsecured credit facility ($3.086 billion and $3.816 billion available as of June 30, 2026”
4. The revolver is a committed five-year senior unsecured facility sized at $**8.000** [quoted: HCA-000119312526044769-0304] billion, which replaced the prior secured facilities.  
   ✅ supported (judge): The passage confirms the $8.000 billion senior unsecured revolver with a five-year term and the termination of the prior secured facilities.
   - cites `HCA-000119312526044769-0304` ✓: “provides for $8.000 billion of senior unsecured revolving credit commitments with a term of five years”
   - cites `HCA-000119312526044769-0304` ✓: “We terminated our $4.500 billion senior secured asset-based revolving credit facility”
5. Planned capital spending for the year is expected to be financed from internally generated and borrowed funds, and construction projects in progress carry additional estimated completion costs spread over several years.  
   ✅ supported (judge): Passage states capital expenditures will be financed with internally generated and borrowed funds, and construction projects have estimated additional costs to complete over the next five years (several years).
   - cites `HCA-000119312526321077-0066` ✓: “Planned capital expenditures are expected to be approximately between $5.0 billion and $5.5 billion in 2026, excluding acquisitions.”
   - cites `HCA-000119312526321077-0066` ✓: “We expect to finance capital expenditures with internally generated and borrowed funds.”
6. The company describes significant debt service requirements, with interest expense a recurring cash cost alongside dividends and share repurchases.  
   ✅ supported (judge): The filing explicitly states significant debt service requirements and lists interest expense alongside dividends and share repurchases as recurring cash outflows.
   - cites `HCA-000119312526191444-0055` ✓: “We have significant debt service requirements. Our debt totaled $48.023 billion at March 31, 2026.”

## Maturity wall

1. The maturity profile shows **$2.5 billion** [F24] due in the second year, **$3.6 billion** [F25] in the third, **$3.6 billion** [F26] in the fourth and **$4.0 billion** [F27] in the fifth, while the first-year and post-fifth-year amounts are not available in the metric table.  
   ✅ supported (judge): The metric table contains exactly the four values cited ($2.5B, $3.6B, $3.6B, $4.0B for years two through five) and includes no first-year or post-fifth-year amounts, matching the claim.
2. Debt falling due in the near-term window shown in the metric table is **$7.4 billion** [F28], equal to **15.7%** [F29] of total debt of **$47.2 billion** [F30].  
   ✅ supported (judge): The claim's figures ($7.4 billion due within 24 months, 15.7% share, and $47.2 billion total debt) all match the metric values computed from the company's XBRL data for FY0 (fiscal year ended 31 December 2025).
3. Near-term maturity cover is **7.15x** [F31], calculated with undrawn revolver capacity of **$0** [F32] and short-term investments assumed at zero.  
   ✅ supported (judge): The metric value of 7.15x was computed with short-term investments assumed zero (not reported) and undrawn revolver capacity of $0 (not reported), exactly matching the claim.
4. Commercial paper borrowings carry short maturities that do not exceed **397** [quoted: HCA-000119312526044769-0418] days, and the company intends to hold available revolver capacity at least equal to the commercial paper outstanding.  
   ✅ supported (judge): Both parts of the claim are directly stated in the passage.
   - cites `HCA-000119312526044769-0418` ✓: “we intend to maintain a minimum available borrowing capacity under our $8.000 billion senior unsecured credit facility”
5. The company states that it faces significant debt service requirements.  
   ✅ supported (judge): The filing explicitly states the company has significant debt service requirements.
   - cites `HCA-000119312526321077-0067` ✓: “We have significant debt service requirements.”
6. Maturities have been addressed through new senior note issuances, with proceeds applied to repay credit facility borrowings and for general corporate purposes.  
   ◐ partially supported (judge): The evidence confirms new senior note issuances with proceeds used to repay credit facility borrowings and for general corporate purposes, but does not state that note maturities were addressed or repaid with these proceeds.
   - cites `HCA-000119312526044769-0415` ✓: “We used the net proceeds to repay borrowings under the senior unsecured credit facility and for general corporate purposes.”

## Key risks

1. The company carries significant indebtedness, which could limit its ability to raise additional capital to fund operations, reduce its flexibility to react to changes in the economy or its industry and impair its ability to meet obligations.  
   ✅ supported (judge): The claim closely paraphrases the risk factor, which states the company has significant indebtedness that could adversely affect its ability to raise additional capital, limit its ability to react to economic or industry changes, and prevent it from meeting its obligations.
   - cites `HCA-000119312526044769-0144` ✓: “Our indebtedness could adversely affect our ability to raise additional capital to fund our operations, limit our ability to react to changes in the economy”
2. For the twelve months to 30 September 2026, debt to EBITDA was **3.17x** [F8] and interest coverage was **6.74x** [F12].  
   ✅ supported (judge): Both metric values match the computed scorecard exactly for the stated period.
3. Refinancing risk is material because the ability to refinance debt on favorable terms depends on then-current economic and financial conditions that affect debt financing availability and pricing.  
   ✅ supported (judge): The passage directly states refinancing ability is affected by then-current economic and financial conditions influencing debt financing availability and pricing.
   - cites `HCA-000119312526044769-0147` ✓: “Our ability to refinance our indebtedness on favorable terms, or at all, is directly affected by the then current global economic and financial conditions”
4. The senior unsecured credit facility requires maintenance of a specified financial ratio, and a breach could trigger a default and acceleration of a significant portion of other outstanding debt.  
   ✅ supported (judge): The passage directly states the required financial ratio, and that a breach could trigger default and acceleration affecting other debt.
   - cites `HCA-000119312526044769-0149` ✓: “A breach of this or any other covenant could result in a default under our senior unsecured credit facility”
5. Staffing shortages and labor union activity may force higher wages, benefits and temporary staffing costs, weighing on capacity and results of operations.  
   ✅ supported (judge): The passage states personnel shortages and union activity may raise wages, benefits, temporary staffing costs, and adversely affect capacity and results of operations.
   - cites `HCA-000119312526044769-0151` ✓: “We may be required to increase wages and benefits to recruit and retain nurses and other medical support personnel”
6. Inflation and tariffs may raise operating costs faster than payer reimbursement updates, and general economic weakness has affected and may continue to affect results of operations, liquidity and the ability to repay debt.  
   ✅ supported (judge): The passage directly states inflationary pressures and tariffs may increase operating expenses faster than payer reimbursement updates, and that general economic conditions have and may continue to negatively impact results of operations, liquidity and ability to repay debt.
   - cites `HCA-000119312526044769-0233` ✓: “inflationary pressures and tariffs may increase operating expenses to a greater degree and faster than reflected in updates to the reimbursement systems”

## Rating rationale

1. The **SB-4** [F33] grade reflects a weighted score of **4.25** [F34] across the factors, and because all six factors were scored the grade is not provisional; it is a stylized internal scorecard grade, not a credit rating.  
   ✅ supported (judge): The metric values directly state the SB-4 grade is a stylized scorecard grade, not a credit rating, with a weighted score of 4.25, and that all six factors were scored so the grade is not provisional.
2. Interest coverage scores strongest, with a band of **3** [F35] and the largest weight at **25.0%** [F36], supported by EBITDA to interest of **6.74x** [F12] on an the twelve months to 30 September 2026 basis.  
   ✅ supported (judge): Metrics confirm interest coverage has band 3, the largest weight at 25.0%, and EBITDA/interest of 6.74x on a TTM 30 September 2026 basis; all other factors have lower weights.
3. Liquidity coverage is the weakest factor at band **6** [F37] with a weight of **15.0%** [F38], and near-term maturity cover also scores band **6** [F39] at a weight of **10.0%** [F40].  
   ✅ supported (judge): Liquidity coverage is band 6 (weakest) at weight 15.0% and near-term maturity cover is band 6 at weight 10.0%, matching the metric scorecard; all other factors score bands 3-4, so band 6 is the weakest.
4. Leverage sits in the middle of the scorecard, with debt to EBITDA of **3.17x** [F8] at band **4** [F41] and weight **20.0%** [F42] and net leverage of **3.11x** [F10] at band **4** [F43] and weight **10.0%** [F44], which holds the overall grade back.  
   ◐ partially supported (judge): The leverage metrics, bands, and weights match the scorecard exactly, but the assertion that leverage 'holds the overall grade back' is interpretive and not supported, since other factors (liquidity coverage and near-term maturity cover, both band 6) score worse than leverage's band 4.
5. The low liquidity band is tempered by committed revolver capacity, as the company entered a new credit agreement that provides for $**8.000** [quoted: HCA-000119312526044769-0304] billion of senior unsecured revolving credit commitments with a term of five years.  
   ✅ supported (judge): The passage states the company entered a new credit agreement providing $8.000 billion of senior unsecured revolving credit commitments with a five-year term, matching the claim exactly.
   - cites `HCA-000119312526044769-0304` ✓: “provides for $8.000 billion of senior unsecured revolving credit commitments with a term of five years”
6. Tempering the scorecard result, the company notes that refinancing conditions are outside its control: our ability to refinance our indebtedness on favorable terms, or at all, is directly affected by the then current global economic and financial conditions.  
   ✅ supported (judge): The passage states verbatim that the ability to refinance indebtedness on favorable terms, or at all, is directly affected by current global economic and financial conditions.
   - cites `HCA-000119312526044769-0147` ✓: “Our ability to refinance our indebtedness on favorable terms, or at all, is directly affected by the then current global economic and financial conditions”

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
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The three ratio values match the metric scorecard exactly, but the characterization 'stable free cash flow relative to debt' is an interpretation that overstates the evidence — a middle-period spike to 16.3% between 11.6% and 11.8% suggests variability rather than stability, and the evidence contains no narrative supporting the stability conclusion.): “FCF / debt was 11.6% in the fiscal year ended 31 December 2023 and 11.8% in the twelve months to 30 September 2026, after 16.3% in the fiscal year ended 31 December 2025, indicating stable free cash flow relative to debt.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The evidence supports the availability figures and the commercial paper capacity intention, but nothing in the evidence addresses the coverage metric or its assumption about undrawn revolver capacity.): “The coverage metric assumes no undrawn revolver capacity, while the company reports remaining availability under its senior unsecured credit facility after letters of credit and its intention to hold capacity equal to commercial paper outstanding.”
- [ ] **partially supported claim** (warning): Maturity wall: partially supported (The evidence confirms new senior note issuances with proceeds used to repay credit facility borrowings and for general corporate purposes, but does not state that note maturities were addressed or repaid with these proceeds.): “Maturities have been addressed through new senior note issuances, with proceeds applied to repay credit facility borrowings and for general corporate purposes.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The leverage metrics, bands, and weights match the scorecard exactly, but the assertion that leverage 'holds the overall grade back' is interpretive and not supported, since other factors (liquidity coverage and near-term maturity cover, both band 6) score worse than leverage's band 4.): “Leverage sits in the middle of the scorecard, with debt to EBITDA of 3.17x at band 4 and weight 20.0% and net leverage of 3.11x at band 4 and weight 10.0%, which holds the overall grade back.”

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
| F13 | EBITDA / interest (interest_coverage:FY0) | 6.94x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest 9,832,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DepreciationDepletionAndAmortization 3,523,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>InterestExpense 2,248,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F14 | FCF / debt (fcf_to_debt:FY-2) | 11.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 9,431,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,744,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 37,169,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>LongTermDebtCurrent 2,424,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityCurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm)<br>FinanceLeaseLiabilityNoncurrent 541,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020134](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| F15 | FCF / debt (fcf_to_debt:LTM) | 11.8% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtNoncurrent 42,400,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F16 | FCF / debt (fcf_to_debt:FY0) | 16.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F17 | Liquidity coverage (liquidity_coverage:FY0) | 1.30x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsOfDividends 679,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F18 | Liquidity coverage (liquidity_coverage:LTM) | 0.86x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F19 | Cash and cash equivalents (cash:LTM) | $908 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 908,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F20 | Cash from operations (cfo:LTM) | $11.2 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 12,636,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,810,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 10,277,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F21 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $8.1 billion | rank 1: DebtCurrent | DebtCurrent 8,093,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F22 | Capital expenditure (capex:LTM) | $5.2 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 4,944,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,707,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,455,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F23 | Dividends paid (dividends:LTM) | $681 million | rank 1: PaymentsOfDividends | PaymentsOfDividends 679,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>PaymentsOfDividends 519,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>PaymentsOfDividends 517,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F24 | Debt maturing in year two (maturity_year_2:FY0) | $2.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F25 | Debt maturing in year three (maturity_year_3:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 3,645,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F26 | Debt maturing in year four (maturity_year_4:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 3,577,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F27 | Debt maturing in year five (maturity_year_5:FY0) | $4.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 4,021,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F28 | Debt due within 24 months (debt_due_24m:FY0) | $7.4 billion | short_term_debt + maturity_year_2 | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F29 | Share of debt due within 24 months (share_due_24m:FY0) | 15.7% | (short_term_debt + maturity_year_2) / total_debt | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F30 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $47.2 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 41,603,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>FinanceLeaseLiabilityCurrent 133,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>FinanceLeaseLiabilityNoncurrent 625,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| F31 | Near-term maturity cover (near_term_maturity_cover:FY0) | 7.15x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | DebtCurrent 4,889,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,547,000,000 (at 2025-12-31, balance sheet) [10-K 0001193125-26-044769](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 1,040,000,000 (at 2025-12-31, balance sheet) [10-Q 0001193125-26-437871](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| F32 | Undrawn revolving credit capacity (undrawn_revolver:FY0) | $0 |  | — |
| F33 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 4.25 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F34 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 4.25 | sum of weight x band over the factors scored, divided by their weights | — |
| F35 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 3 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F36 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F37 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F38 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F39 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 6 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F40 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F41 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 4 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F42 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F43 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 4 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F44 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### HCA-000119312526044769-0004

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 5633–6593

> Item 1. Business
> General
> HCA Healthcare, Inc. is one of the leading health care services companies in the United States. At December 31, 2025, we operated 190 hospitals, comprised of 179 general acute care hospitals, seven behavioral hospitals, and four rehabilitation hospitals. In addition, we operated 121 freestanding ambulatory surgery centers (“ASCs”) and 31 freestanding endoscopy centers. Our facilities are located in 19 states and England.
> The terms “Company,” “HCA,” “HCA Healthcare,” “we,” “our” or “us,” as used herein and unless otherwise stated or indicated by context, refer to HCA Healthcare, Inc. and its affiliates. The term “affiliates” means direct and indirect subsidiaries of HCA Healthcare, Inc. and partnerships and joint ventures in which such subsidiaries are partners. The terms “facilities” or “hospitals” refer to entities owned and operated by affiliates of HCA, and the term “employees” refers to employees of affiliates of HCA.

### HCA-000119312526044769-0013

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 17414–18730

> We have been and could become the subject of government investigations, claims and litigation, as well as governmental and commercial payer audits.
> •
> We may be subject to liabilities from claims brought against our facilities, which are costly to defend and may require us to pay significant damages if not covered by insurance.
> 5
> Risks related to operations, strategy, demand and competition:
> •
> Our hospitals and other facilities face competition for patients from other hospitals and health care providers.
> •
> Any increase in the volume of uninsured patients or deterioration in the collectability of uninsured and patient due accounts could adversely affect our results of operations.
> •
> If our volume of patients with private health insurance coverage declines or we are unable to retain and negotiate favorable contracts with private third-party payers, including managed care plans, our revenues may be adversely affected.
> •
> Changes to physician utilization practices and treatment methodologies and other factors outside our control that impact demand for medical services may reduce our revenues.
> •
> Third-party payer controls designed to reduce costs and other payer practices intended to decrease inpatient services, surgical procedure volumes or reimbursement for services rendered may reduce our revenues.
> •

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

### HCA-000119312526044769-0151

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/hca-20251231.htm), characters 173459–174878

> Economic conditions, including macroeconomic uncertainties and inflationary pressure, workforce burnout, and public health conditions and other factors, have exacerbated workforce competition, personnel shortages and capacity constraints. New limitations on federal loan eligibility, other student loan changes imposed pursuant to the FBA and changes to immigration policies may also impact health care personnel shortages. We may be required to increase wages and benefits to recruit and retain nurses and other medical support personnel and to hire more expensive temporary or contract personnel.
> If there is additional union organizing activity or a significant portion of our employee base unionizes, it is possible our labor costs could increase. When negotiating collective bargaining agreements with unions, whether such agreements are renewals or first contracts, we have experienced, and could experience in the future, labor strikes. Our continued operation during any strikes could result in an increase to our labor costs. In addition, upon the expiration of existing collective bargaining agreements, we may not reach new agreements without union action, and any such new agreements may not be on terms satisfactory to us. The unavailability of staff, or the inability of the Company to control labor costs, could have a material, adverse effect on our capacity, growth prospects and results of operations.

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

### HCA-000119312526321077-0064

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 80633–81032

> Liquidity and Capital Resources
> Cash provided by operating activities totaled $4.349 billion for the first six months of 2026 compared to $5.861 billion for the first six months of 2025. The $1.512 billion decline in cash provided by operating activities, for the first six months of 2026 compared to the first six months of 2025, related primarily to unfavorable changes in working capital items of

### HCA-000119312526321077-0066

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 82185–83601

> Cash used in investing activities was $2.839 billion in the first six months of 2026 compared to $2.283 billion in the first six months of 2025. Excluding acquisitions, capital expenditures were $2.350 billion in the first six months of 2026 and $2.167 billion in the first six months of 2025. Planned capital expenditures are expected to be approximately between $5.0 billion and $5.5 billion in 2026, excluding acquisitions. At June 30, 2026, there were projects under construction which had estimated additional costs to complete and equip over the next five years of approximately $8.6 billion. We expect to finance capital expenditures with internally generated and borrowed funds.
> Cash used in financing activities totaled $1.534 billion in the first six months of 2026, compared to $4.584 billion in the first six months of 2025. During the first six months of 2026, net cash flows used in financing activities included a net increase of $3.065 billion in our indebtedness, payment of dividends of $354 million, repurchase of common stock of $3.635 billion and distributions to noncontrolling interests of $334 million. During the first six months of 2025, net cash flows used in financing activities included a net increase of $1.341 billion in our indebtedness, payment of dividends of $351 million, repurchase of common stock of $5.011 billion and distributions to noncontrolling interests of $394 million.

### HCA-000119312526321077-0067

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 83602–84623

> During April 2026, we issued $3.000 billion aggregate principal amount of senior notes comprised of (i) $1.000 billion aggregate principal amount of 4.700% senior notes due 2031, (ii) $750 million aggregate principal amount of 5.000% senior notes due 2033 and (iii) $1.250 billion aggregate principal amount of 5.300% senior notes due 2036. We used the net proceeds to repay borrowings under the commercial paper program and for general corporate purposes.
> During May 2026, we repaid all $1.500 billion aggregate principal amount of 5.250% senior notes due 2026 and all $1.000 billion aggregate principal amount of 5.375% senior notes due 2026.
> We have significant debt service requirements. Our debt totaled $49.718 billion at June 30, 2026. Our interest expense was $1.183 billion for the first six months of 2026 and $1.115 billion for the first six months of 2025.
> 26
> ITEM 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF
> FINANCIAL CONDITION AND RESULTS OF OPERATIONS (Continued)
> Liquidity and Capital Resources (continued)

### HCA-000119312526321077-0068

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/860730/000119312526321077/hca-20260630.htm), characters 84624–85224

> In addition to cash flows from operations, available sources of capital include amounts available under our senior unsecured credit facility ($3.086 billion and $3.816 billion available as of June 30, 2026 and July 24, 2026, respectively, after giving effect to all issued and outstanding letters of credit and our intention to maintain a minimum available borrowing capacity equal to the aggregate amount outstanding under the commercial paper program ($3.890 billion and $4.000 billion as of June 30, 2026 and July 24, 2026, respectively)) and anticipated access to public and private debt markets.

## Run

Run `HCA-20261118T071200Z-DeepSeek-V4.1-Flash-1017`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 8 calls, 30,537 input (23,100 cached) and 18,979 output tokens, $0.0065, 416s. Verification: 36 calls, 16,245 input (4,608 cached) and 3,358 output tokens, $0.0226, 58s. Prices read 2026-11-17. Raw requests and responses: data/runs/HCA/HCA-20261118T071200Z-DeepSeek-V4.1-Flash-1017.jsonl.
