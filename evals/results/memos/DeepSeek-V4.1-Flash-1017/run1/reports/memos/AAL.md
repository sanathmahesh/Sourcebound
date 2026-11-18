# Credit memo: American Airlines Group Inc. (AAL)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4.1-Flash-1017`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-5**.
Sources: [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm); [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000032/aal-20260331.htm); [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000052/aal-20260630.htm)

Claims: 36 — 35 supported, 1 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 1; repairs: 3.

## Business profile

1. American Airlines Group is a holding company whose principal wholly owned subsidiaries include American Airlines, Envoy Aviation Group, PSA Airlines and Piedmont Airlines.  
   ✅ supported (judge): The passage directly states AAG is a holding company whose principal wholly owned subsidiaries are American Airlines, Envoy Aviation Group, PSA Airlines and Piedmont Airlines.
   - cites `AAL-000000620126000014-0013` ✓: “is a holding company and its principal, wholly-owned subsidiaries are”
   - cites `AAL-000000620126000014-0013` ✓: “American Airlines, Inc. (American), Envoy Aviation Group Inc., PSA Airlines, Inc. (PSA) and Piedmont Airlines, Inc. (Piedmont)”
2. It operates an airline network flying to over **350** [quoted: AAL-000000620126000014-0037] destinations in the United States and internationally, with international service to Canada, Mexico, the Caribbean, Central and South America, Europe, Qatar, China, Japan, South Korea, India, Australia and New Zealand.  
   ✅ supported (judge): Both the 350+ destinations and the full list of international service countries are directly stated in the evidence.
   - cites `AAL-000000620126000014-0037` ✓: “We fly to over 350 destinations in the United States and internationally”
   - cites `AAL-000000620126000014-0029` ✓: “we provide international service to Canada, Mexico, the Caribbean, Central and South America, Europe, Qatar, China, Japan, South Korea, India, Australia and New Zealand”
3. Revenue was **$54.6 billion** [F1] in the fiscal year ended 31 December 2025 and **$61.0 billion** [F2] in the twelve months to 30 September 2026, while EBITDA was **$3.7 billion** [F3] and **$2.9 billion** [F4], respectively.  
   ✅ supported (judge): All four figures in the claim match the XBRL-derived metric values exactly.
4. Pricing decisions on its routes are affected in large part by the need to meet competition from other airlines, which can pressure revenue.  
   ✅ supported (judge): The passage states pricing decisions on all routes are affected in large part by the need to meet competition from other airlines, and describes pricing pressure.
   - cites `AAL-000000620126000014-0028` ✓: “On all of our routes, pricing decisions are affected, in large part, by the need to meet competition from other airlines”
5. Worldwide macroeconomic, political and military events and oil and natural gas price volatility can contribute to weakened business conditions for the transportation industry, which may affect the company's operations.  
   ✅ supported (judge): The passage states that worldwide macroeconomic, political and military events and oil/gas price volatility could lead to weakened business conditions for the transportation industry and adversely impact the company's operations.
   - cites `AAL-000000620126000032-0072` ✓: “Worldwide macroeconomic, political and military events, including war, terrorist activity, and conflict in the Middle East”
   - cites `AAL-000000620126000032-0072` ✓: “have contributed, and are likely to continue to contribute, to oil and natural gas price volatility”
   - cites `AAL-000000620126000032-0072` ✓: “could lead to weakened business conditions for the transportation industry”
6. Airlines compete for market share by increasing route systems and markets served, and the American Eagle regional carriers add smaller markets and hub connections.  
   ✅ supported (judge): Both parts of the claim are directly stated in the evidence passage.
   - cites `AAL-000000620126000014-0029` ✓: “airlines compete for market share by increasing the size of their route system and the number of markets they serve”
   - cites `AAL-000000620126000014-0029` ✓: “The American Eagle regional carriers increase the number of markets we serve by flying to smaller markets and providing connections at our hubs”

## Financial risk

1. Debt / EBITDA worsened over the period, moving from **6.14x** [F5] in the fiscal year ended 31 December 2023 to **6.30x** [F6] in the fiscal year ended 31 December 2024, **7.88x** [F7] in the fiscal year ended 31 December 2025 and **10.21x** [F8] in the twelve months to 30 September 2026.  
   ✅ supported (judge): All four metric values match the claim exactly and show a rising (worsening) trend.
2. Net leverage followed the same worsening path, from **4.70x** [F9] in the fiscal year ended 31 December 2023 to **7.31x** [F10] in the twelve months to 30 September 2026, with total debt of **$29.5 billion** [F11] against LTM EBITDA of **$2.9 billion** [F4].  
   ✅ supported (judge): All figures in the claim match the XBRL-computed metrics exactly: 4.70x, 7.31x, $29.5B total debt, $2.9B LTM EBITDA.
3. EBITDA / interest weakened from **2.49x** [F12] in the fiscal year ended 31 December 2023 to **1.74x** [F13] in the twelve months to 30 September 2026, with LTM interest expense of **$1.7 billion** [F14] against EBITDA of **$2.9 billion** [F4].  
   ✅ supported (judge): All figures in the claim match the computed metric values: coverage fell from 2.49x to 1.74x, with LTM interest of $1.7B and EBITDA of $2.9B.
4. FCF / debt deteriorated from **3.7%** [F15] in the fiscal year ended 31 December 2023 to a negative **-0.3%** [F16] in the twelve months to 30 September 2026, as LTM capital expenditure of **$4.4 billion** [F17] broadly matched cash from operations of **$4.3 billion** [F18].  
   ✅ supported (judge): All figures in the claim (3.7% FY2023, -0.3% LTM, $4.4B capex, $4.3B CFO) match the computed metric values exactly.
5. Net interest expense declined in the first nine months of **2026** [quoted: AAL-000000620126000065-0113], so the weaker EBITDA / interest ratio was not driven by higher net interest cost.  
   ✅ supported (judge): The filing states net interest expense decreased $112 million (8.4%) in the first nine months of 2026 vs. 2025, so weaker coverage was not driven by higher net interest cost.
   - cites `AAL-000000620126000065-0113` ✓: “primarily due to repayments of higher interest debt, offset in part by the issuance of debt subsequent to the third quarter of 2025”
6. Long-term debt was both issued and repaid during the period, and the company stated it was in compliance with its debt covenants, including the AAdvantage Financing peak debt service coverage ratio test.  
   ✅ supported (judge): The cash flow statement shows proceeds from issuance of long-term debt ($5,933M) and payments on long-term debt and finance leases ($5,343M), and the filing states compliance with all covenants including the AAdvantage Financing peak debt service coverage ratio.
   - cites `AAL-000000620126000065-0050` ✓: “Payments on long-term debt and finance leases (5,343) (3,086)”
   - cites `AAL-000000620126000032-0095` ✓: “The AAdvantage Financing contains a peak debt service coverage ratio, pursuant to which failure to comply with a certain threshold may result in early repayment”
   - cites `AAL-000000620126000032-0095` ✓: “we were in compliance with each of the foregoing covenants”

## Liquidity

1. Liquidity coverage was **1.59x** [F19] for the twelve months to 30 September 2026, compared with **1.22x** [F20] for the fiscal year ended 31 December 2025.  
   ✅ supported (judge): Both metric values match the claim exactly: 1.59x LTM to 30 Sep 2026 and 1.22x FY ended 31 Dec 2025.
2. At the twelve months to 30 September 2026, cash of **$1.2 billion** [F21] together with short-term investments of **$7.2 billion** [F22] exceeded short-term debt of **$3.6 billion** [F23].  
   ✅ supported (judge): Cash $1.2B + short-term investments $7.2B = $8.4B, which exceeds short-term debt of $3.6B, matching the claim.
3. Cash from operations of **$4.3 billion** [F18] was close to capital expenditure of **$4.4 billion** [F17] for the twelve months to 30 September 2026, and dividends paid were **$0** [F24].  
   ✅ supported (judge): All figures match the computed metric values: CFO $4.3B ≈ capex $4.4B, dividends paid $0.
4. Reported total available liquidity of $**11.8** [quoted: AAL-000000620126000065-0088] billion consisted of $**8.3** [quoted: AAL-000000620126000065-0088] billion in unrestricted cash and short-term investments and $**3.5** [quoted: AAL-000000620126000065-0088] billion in undrawn capacity under revolving credit and other facilities.  
   ✅ supported (judge): The passage states all figures exactly as claimed.
   - cites `AAL-000000620126000065-0088` ✓: “we had $11.8 billion in total available liquidity, consisting of $8.3 billion in unrestricted cash and short-term investments”
   - cites `AAL-000000620126000065-0088` ✓: “$3.5 billion in total undrawn capacity under revolving credit and other facilities”
5. During **2026** [quoted: AAL-000000620126000065-0088] the aggregate revolving commitments were increased from $**3.0** [quoted: AAL-000000620126000065-0088] billion to $**3.1** [quoted: AAL-000000620126000065-0088] billion, supporting the undrawn capacity reported later in the year.  
   ✅ supported (judge): The passage states the revolving commitments increased from $3.0 billion to $3.1 billion during 2026, and $3.5 billion undrawn capacity was reported at September 30, 2026.
   - cites `AAL-000000620126000065-0088` ✓: “increased the aggregate revolving commitments under the 2013 Revolving Facility, the 2014 Revolving Facility and the 2023 Revolving Facility from $3.0 billion to $3.1 billion”
6. A significant portion of debt agreements require at least $**2.0** [quoted: AAL-000000620126000065-0117] billion of unrestricted cash and revolving availability, and the company reported compliance with these covenants.  
   ✅ supported (judge): The passage directly states the $2.0 billion covenant requirement and compliance with all covenants.
   - cites `AAL-000000620126000065-0117` ✓: “covenants requiring us to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents”
   - cites `AAL-000000620126000065-0117` ✓: “we were in compliance with each of the foregoing covenants”

## Maturity wall

1. The debt maturity ladder as of the fiscal year ended 31 December 2025 shows **$3.6 billion** [F25] due in the next twelve months, **$4.5 billion** [F26] in year two, **$7.3 billion** [F27] in year three, **$4.0 billion** [F28] in year four and **$2.5 billion** [F29] in year five, with **$6.6 billion** [F30] due after year five.  
   ✅ supported (judge): All six ladder figures match the metric values exactly.
2. Debt due within the next two years totals **$8.1 billion** [F31], equal to **28.0%** [F32] of total debt of **$28.9 billion** [F33] at the fiscal year ended 31 December 2025.  
   ✅ supported (judge): All figures ($8.1B debt due within 24 months, 28.0% share, $28.9B total debt at FYE 31 Dec 2025) match the computed XBRL metric values.
3. Near-term maturity cover is **1.36x** [F34] at the fiscal year ended 31 December 2025, with undrawn revolving credit capacity treated as **$0** [F35] because it was not reported.  
   ✅ supported (judge): The claim matches the computed metrics: near-term maturity cover is 1.36x for FY ended 31 Dec 2025 with undrawn revolver assumed $0 as not reported.
4. A significant portion of the company's debt financing agreements require it to maintain at least $**2.0** [quoted: AAL-000000620126000065-0117] billion of unrestricted cash and cash equivalents plus revolver availability, and the company reports compliance with these covenants.  
   ✅ supported (judge): The passage states that a significant portion of debt financing agreements require maintaining at least $2.0 billion of unrestricted cash and revolver availability, and that the company was in compliance with each of these covenants.
   - cites `AAL-000000620126000065-0117` ✓: “covenants requiring us to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents and amounts available to be drawn under revolving credit facilities”
5. The AAdvantage Financing carries a peak debt service coverage ratio test, and a failure to meet the applicable threshold may require early repayment in whole or in part of that financing, although compliance was maintained as of the most recent measurement dates.  
   ✅ supported (judge): The passage directly states the AAdvantage Financing contains a peak debt service coverage ratio whose breach may require early repayment in whole or in part, and that the company was in compliance as of the most recent measurement dates.
   - cites `AAL-000000620126000065-0117` ✓: “The AAdvantage Financing contains a peak debt service coverage ratio, pursuant to which failure to comply with a certain threshold may result in early repayment”
6. Repayment activity combined scheduled and early repayments, including retirement of senior secured notes and EETC equipment notes, partly offset by new long-term debt issuance.  
   ✅ supported (judge): The evidence states repayments included scheduled ($2.1B) and early repayments ($1.3B) covering 8.50% senior secured notes and EETC equipment notes, offset in part by $4.5B of long-term debt issuance proceeds.
   - cites `AAL-000000620126000052-0116` ✓: “consisting of $2.1 billion in scheduled repayments, $1.3 billion of early repayments, including $1.0 billion of the outstanding principal amount of the 8.50% senior secured notes”

## Key risks

1. Leverage is elevated relative to earnings, with debt to EBITDA of **10.21x** [F8] and interest coverage of **1.74x** [F13] in the twelve months to 30 September 2026, leaving a thin margin between operating earnings and interest cost.  
   ✅ supported (judge): Debt/EBITDA of 10.21x and EBITDA/interest coverage of 1.74x for the LTM ending 30 September 2026 match the metric values, and 1.74x coverage implies a thin margin between operating earnings and interest cost.
2. Free cash flow was negative relative to debt at **-0.3%** [F16] in the twelve months to 30 September 2026, and liquidity coverage stood at **1.59x** [F19], so internally generated funds are not reducing borrowings.  
   ✅ supported (judge): Both figures match the computed metric values exactly (-0.3% FCF/debt and 1.59x liquidity coverage), and the negative FCF/debt supports the inference that internal funds are not reducing borrowings.
3. The business plan requires heavy fleet and capital spending, and the company states it will need substantial liquidity and financing for aircraft and engines and may also need financing to refinance maturing obligations.  
   ✅ supported (judge): The passage states the business plan contemplates significant fleet investments, significant capital resources will be required, and the company will need substantial liquidity/financing to finance aircraft and engines and may require financing to refinance maturing obligations.
   - cites `AAL-000000620126000014-0066` ✓: “we will need substantial liquidity, financing or other capital resources to finance such aircraft and engines”
   - cites `AAL-000000620126000014-0066` ✓: “We may also require financing to refinance maturing obligations”
4. Access to new capital is uncertain given existing indebtedness, a non-investment grade corporate credit rating and limited unpledged collateral.  
   ✅ supported (judge): Passage explicitly lists existing indebtedness, non-investment grade credit rating, and collateral availability as factors making it difficult to raise additional capital.
   - cites `AAL-000000620126000014-0066` ✓: “It may be difficult for us to raise additional capital on acceptable terms, or at all”
   - cites `AAL-000000620126000014-0068` ✓: “currently a very significant portion of our assets are pledged to secure our indebtedness”
5. A substantial portion of long-term debt pays floating interest rates and is not hedged, so higher rates would raise interest expense and pressure cash flow available for fixed costs.  
   ✅ supported (judge): The passage directly states substantial floating-rate unhedged long-term debt whose higher rates would increase interest expense and impede funding fixed costs.
   - cites `AAL-000000620126000014-0071` ✓: “We have not entered into any derivative transactions to hedge our interest rate exposure.”
   - cites `AAL-000000620126000014-0071` ✓: “our interest expense will increase, in which event we may have difficulties making interest payments”
6. Debt documents carry financial covenants, including a minimum liquidity requirement, and restrictive covenants that can affect the availability of borrowings under revolving lines of credit.  
   ✅ supported (judge): The passage explicitly states debt contains financial covenants including a $2.0 billion minimum liquidity requirement, impacts availability of borrowings under revolving lines of credit, and contains restrictive covenants.
   - cites `AAL-000000620126000014-0069` ✓: “including the requirement to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents”
   - cites `AAL-000000620126000014-0069` ✓: “impact availability of borrowings under revolving lines of credit”

## Rating rationale

1. The weighted score **5.45** [F36] produces **SB-5** [F37], a stylized internal scorecard grade rather than a credit rating; all six factors were scored, so the grade is not provisional.  
   ✅ supported (judge): The computed scorecard confirms weighted score 5.45 maps to grade SB-5, explicitly labeled a stylized scorecard grade not a credit rating, with all six factors scored so the grade is not provisional.
2. Liquidity coverage is the strongest factor, at **1.59x** [F19] with band **3** [F38] and weight **15.0%** [F39], followed by near-term maturity cover at **1.36x** [F34] with band **5** [F40] and weight **10.0%** [F41].  
   ◐ partially supported (judge): The specific values (1.59x band 3 weight 15.0%; 1.36x band 5 weight 10.0%) match the evidence, but liquidity coverage is not the strongest factor — interest coverage has a higher weight (25%), as do debt/EBITDA and FCF/debt (20%).
3. The four weakest factors carry band **6** [F42] for debt / EBITDA at **10.21x** [F8] with weight **20.0%** [F43], net leverage at **7.31x** [F10] with band **6** [F44] and weight **10.0%** [F45], interest coverage at **1.74x** [F13] with band **6** [F46] and weight **25.0%** [F47], and FCF / debt at **-0.3%** [F16] with band **6** [F48] and weight **20.0%** [F49].  
   ✅ supported (judge): All four factors' values, bands (all 6), and weights (20%, 10%, 25%, 20%) match the scorecard metrics exactly.
4. The weak scores are consistent with the company's own discussion of significant indebtedness and the call on liquidity or cash flow to service debt.  
   ✅ supported (judge): The scorecard shows weak credit metrics (most leverage/coverage factors in band 5-6 of 6), consistent with the filing's discussion of significant indebtedness and dedicating liquidity or cash flow to servicing it.
   - cites `AAL-000000620126000014-0068` ✓: “We have significant amounts of indebtedness and other financial obligations”
   - cites `AAL-000000620126000014-0069` ✓: “require us to dedicate a substantial portion of our liquidity or cash flow from operations to payments on our indebtedness”
5. The stronger liquidity score is tempered by planned fleet investment and refinancing needs, and by the company's statement that it will need substantial liquidity and financing.  
   ✅ supported (judge): The passage directly states planned fleet investment (~$17.5B), possible refinancing, and that 'we will need substantial liquidity, financing or other capital resources.'
   - cites `AAL-000000620126000014-0066` ✓: “we will need substantial liquidity, financing or other capital resources to finance such aircraft and engines”
   - cites `AAL-000000620126000014-0066` ✓: “We may also require financing to refinance maturing obligations”
6. Compliance with the minimum liquidity covenant and the AAdvantage peak debt service coverage test supports the liquidity assessment.  
   ✅ supported (judge): The filing explicitly states compliance with the $2.0 billion minimum liquidity covenant and the AAdvantage peak debt service coverage ratio, which are the claim's cited compliance items supporting liquidity assessment.
   - cites `AAL-000000620126000065-0117` ✓: “The AAdvantage Financing contains a peak debt service coverage ratio”
   - cites `AAL-000000620126000065-0117` ✓: “we were in compliance with each of the foregoing covenants”

## Reviewer checklist

- [ ] **fallback** (info): Revenue: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Total debt (borrowings plus finance-lease liabilities): used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Cash and cash equivalents: used rank 2 CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term investments: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Capital expenditure: used rank 2 PaymentsToAcquireProductiveAssets in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Interest expense: used rank 2 InterestExpenseNonoperating in FY-1, FY0, LTM.
- [ ] **fallback** (info): Depreciation and amortisation: used rank 2 DepreciationAndAmortization in LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): ShortTermBorrowings assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): CommercialPaper assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Dividends paid assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **reconciliation** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $32,771m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $29,401m (-10.3%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $30,350m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,280m (-16.7%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $28,895m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,366m (-12.2%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $29,523m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,395m (-14.0%). Check which matches the balance sheet.
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The specific values (1.59x band 3 weight 15.0%; 1.36x band 5 weight 10.0%) match the evidence, but liquidity coverage is not the strongest factor — interest coverage has a higher weight (25%), as do debt/EBITDA and FCF/debt (20%).): “Liquidity coverage is the strongest factor, at 1.59x with band 3 and weight 15.0%, followed by near-term maturity cover at 1.36x with band 5 and weight 10.0%.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY0) | $54.6 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 54,633,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F2 | Revenue (revenue:LTM) | $61.0 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 54,633,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 46,982,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 40,634,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F3 | EBITDA (ebitda:FY0) | $3.7 billion | operating_income + d_and_a | OperatingIncomeLoss 1,467,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationDepletionAndAmortization 2,200,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F4 | EBITDA (ebitda:LTM) | $2.9 billion | operating_income + d_and_a | OperatingIncomeLoss 1,467,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>OperatingIncomeLoss 521,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,015,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,890,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationAndAmortization 1,446,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,418,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F5 | Debt / EBITDA (debt_to_ebitda:FY-2) | 6.14x | total_debt / EBITDA | LongTermDebtAndCapitalLeaseObligations 29,270,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm)<br>LongTermDebtCurrent 3,501,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm)<br>OperatingIncomeLoss 3,034,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationDepletionAndAmortization 2,300,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F6 | Debt / EBITDA (debt_to_ebitda:FY-1) | 6.30x | total_debt / EBITDA | LongTermDebtAndCapitalLeaseObligations 25,154,000,000 (at 2024-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>LongTermDebtCurrent 5,196,000,000 (at 2024-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>OperatingIncomeLoss 2,614,000,000 (2024-01-01 to 2024-12-31, FY-1) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationDepletionAndAmortization 2,200,000,000 (2024-01-01 to 2024-12-31, FY-1) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY0) | 7.88x | total_debt / EBITDA | LongTermDebtAndCapitalLeaseObligations 25,254,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,467,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationDepletionAndAmortization 2,200,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:LTM) | 10.21x | total_debt / EBITDA | LongTermDebtAndCapitalLeaseObligations 25,943,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,580,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,467,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>OperatingIncomeLoss 521,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,015,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,890,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationAndAmortization 1,446,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,418,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F9 | Net leverage (net_leverage:FY-2) | 4.70x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtAndCapitalLeaseObligations 29,270,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm)<br>LongTermDebtCurrent 3,501,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm)<br>CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents 681,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 7,000,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm)<br>OperatingIncomeLoss 3,034,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationDepletionAndAmortization 2,300,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F10 | Net leverage (net_leverage:LTM) | 7.31x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtAndCapitalLeaseObligations 25,943,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,580,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents 1,228,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 7,163,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,467,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>OperatingIncomeLoss 521,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,015,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,890,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F11 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $29.5 billion | rank 2: LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | LongTermDebtAndCapitalLeaseObligations 25,943,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,580,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F12 | EBITDA / interest (interest_coverage:FY-2) | 2.49x | EBITDA / interest_expense | OperatingIncomeLoss 3,034,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationDepletionAndAmortization 2,300,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>InterestExpense 2,145,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-24-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620124000010/0000006201-24-000010-index.htm) |
| F13 | EBITDA / interest (interest_coverage:LTM) | 1.74x | EBITDA / interest_expense | OperatingIncomeLoss 1,467,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>OperatingIncomeLoss 521,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>OperatingIncomeLoss 1,015,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,890,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>DepreciationAndAmortization 1,446,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>DepreciationAndAmortization 1,418,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>InterestExpenseNonoperating 1,716,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>InterestExpenseNonoperating 1,242,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F14 | Interest expense (interest_expense:LTM) | $1.7 billion | rank 2: InterestExpenseNonoperating | InterestExpenseNonoperating 1,716,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>InterestExpenseNonoperating 1,242,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>InterestExpenseNonoperating 1,294,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F15 | FCF / debt (fcf_to_debt:FY-2) | 3.7% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 3,803,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>PaymentsToAcquireProductiveAssets 2,596,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>LongTermDebtAndCapitalLeaseObligations 29,270,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm)<br>LongTermDebtCurrent 3,501,000,000 (at 2023-12-31, balance sheet) [10-K 0000006201-25-000010](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| F16 | FCF / debt (fcf_to_debt:LTM) | -0.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 3,099,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 4,541,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 3,373,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>PaymentsToAcquireProductiveAssets 3,779,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>PaymentsToAcquireProductiveAssets 2,728,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>PaymentsToAcquireProductiveAssets 2,149,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtAndCapitalLeaseObligations 25,943,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,580,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F17 | Capital expenditure (capex:LTM) | $4.4 billion | rank 2: PaymentsToAcquireProductiveAssets | PaymentsToAcquireProductiveAssets 3,779,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>PaymentsToAcquireProductiveAssets 2,728,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>PaymentsToAcquireProductiveAssets 2,149,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F18 | Cash from operations (cfo:LTM) | $4.3 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 3,099,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 4,541,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 3,373,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F19 | Liquidity coverage (liquidity_coverage:LTM) | 1.59x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents 1,228,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 7,163,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 3,099,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 4,541,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 3,373,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,580,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>PaymentsToAcquireProductiveAssets 3,779,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>PaymentsToAcquireProductiveAssets 2,728,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F20 | Liquidity coverage (liquidity_coverage:FY0) | 1.22x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents 1,056,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 4,882,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 3,099,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>PaymentsToAcquireProductiveAssets 3,779,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F21 | Cash and cash equivalents (cash:LTM) | $1.2 billion | rank 2: CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents 1,228,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F22 | Short-term investments (short_term_investments:LTM) | $7.2 billion | rank 3: AvailableForSaleSecuritiesDebtSecuritiesCurrent | AvailableForSaleSecuritiesDebtSecuritiesCurrent 7,163,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F23 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $3.6 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 3,580,000,000 (at 2026-09-30, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F24 | Dividends paid (dividends:LTM) | $0 |  | — |
| F25 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $3.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 3,641,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F26 | Debt maturing in year two (maturity_year_2:FY0) | $4.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 4,455,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F27 | Debt maturing in year three (maturity_year_3:FY0) | $7.3 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 7,324,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F28 | Debt maturing in year four (maturity_year_4:FY0) | $4.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 4,045,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F29 | Debt maturing in year five (maturity_year_5:FY0) | $2.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 2,487,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F30 | Debt maturing after year five (maturity_after_year_5:FY0) | $6.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 6,642,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F31 | Debt due within 24 months (debt_due_24m:FY0) | $8.1 billion | short_term_debt + maturity_year_2 | LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 4,455,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| F32 | Share of debt due within 24 months (share_due_24m:FY0) | 28.0% | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 4,455,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>LongTermDebtAndCapitalLeaseObligations 25,254,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F33 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $28.9 billion | rank 2: LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | LongTermDebtAndCapitalLeaseObligations 25,254,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F34 | Near-term maturity cover (near_term_maturity_cover:FY0) | 1.36x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtCurrent 3,641,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 4,455,000,000 (at 2025-12-31, balance sheet) [10-K 0000006201-26-000014](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm)<br>CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents 1,056,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 4,882,000,000 (at 2025-12-31, balance sheet) [10-Q 0000006201-26-000065](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| F35 | Undrawn revolving credit capacity (undrawn_revolver:FY0) | $0 |  | — |
| F36 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 5.45 | sum of weight x band over the factors scored, divided by their weights | — |
| F37 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 5.45 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F38 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 3 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F39 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F40 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 5 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F41 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F42 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 6 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F43 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F44 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 6 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F45 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F46 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 6 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F47 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F48 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 6 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F49 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### AAL-000000620126000014-0013

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 16866–17529

> ITEM 1. BUSINESS
> Overview
> American Airlines Group Inc. (AAG), a Delaware corporation, is a holding company and its principal, wholly-owned subsidiaries are American Airlines, Inc. (American), Envoy Aviation Group Inc., PSA Airlines, Inc. (PSA) and Piedmont Airlines, Inc. (Piedmont). AAG was formed in 1982, under the name AMR Corporation (AMR), as the parent company of American, which was founded in 1934, with roots tracing back to an air mail carrier in the Midwestern United States in 1926.
> AAG’s and American’s principal executive offices are located at 1 Skyview Drive, Fort Worth, Texas 76155 and their telephone number is 682-278-9000.
> Airline Operations

### AAL-000000620126000014-0028

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 34002–35038

> On all of our routes, pricing decisions are affected, in large part, by the need to meet competition from other airlines. Price competition occurs on a market-by-market basis through price discounts, changes in pricing structures, fare matching, targeted promotions and loyalty program initiatives. Airlines typically use discounted fares and other promotions to stimulate traffic during normally weak travel periods, when they begin service to new cities, when they have excess capacity, to generate cash flow, to maximize revenue per available seat mile or to establish, increase or preserve market share. Most airlines will quickly match price reductions in a particular market, and we have often elected to match discounted or promotional fares initiated by other air carriers in certain markets in order to compete in those markets. In addition, we face pricing pressures from so-called ultra-low-cost carriers, such as Allegiant Air, Frontier Airlines and Spirit Airlines, which compete in many of the markets in which we operate.

### AAL-000000620126000014-0029

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 35039–36448

> In addition to price competition, airlines compete for market share by increasing the size of their route system and the number of markets they serve. The American Eagle regional carriers increase the number of markets we serve by flying to smaller markets and providing connections at our hubs. Many of our competitors also own or have agreements with regional airlines that provide similar services at their hubs and other locations. We also compete on the basis of scheduling (frequency and flight times), availability of nonstop flights, on-time performance, type of equipment, cabin configuration, amenities provided to passengers, loyalty programs, the automation of travel agent reservation systems, onboard products, health and safety, sustainability initiatives and other services.
> International
> In addition to our extensive domestic service, we provide international service to Canada, Mexico, the Caribbean, Central and South America, Europe, Qatar, China, Japan, South Korea, India, Australia and New Zealand. In providing international air transportation, we compete with other U.S. airlines, foreign investor-owned airlines and foreign state-owned or state-affiliated airlines. Competition has also been increasing from low-cost airlines executing international long-haul expansion strategies, a trend we expect to continue, in particular with the introduction of long-range narrowbody aircraft.

### AAL-000000620126000014-0037

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 45493–46834

> For more discussion, see Part I, Item 1A. Risk Factors – “Union disputes, employee strikes and other labor-related disruptions may adversely affect our operations and financial performance.”
> Customers
> We fly to over 350 destinations in the United States and internationally, and we are committed to providing our customers with a world-class travel experience. We continued to rigorously measure and track customer satisfaction through passenger surveys in 2025, efforts that led to further improvements in the services we provide and our customer experience. In 2025, we appointed a Chief Customer Officer to lead a newly created Customer Experience organization, which drives the strategy and coordinates the implementation of initiatives that enhance our customers’ journeys. We continue to invest in the customer experience and our premium products and services, and in 2025, we advanced this strategy through the following:
> •introduced the new premium Flagship Suite® on our Boeing 787-9s and Airbus A321XLRs and announced plans to expand this product to our Boeing 777 fleet;
> 14
> Table of Contents
> •enhanced our inflight services with new food and beverage offerings as well as upgraded amenity kits;
> •redesigned the American Airlines mobile application to better support customers with new features and a more intuitive, modern design;

### AAL-000000620126000014-0066

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 78366–79519

> Our business plan contemplates continued significant investments related to our fleet, improving the experience of our customers, updating our facilities and deploying technology. Significant capital resources will be required to execute this plan. We estimate that, based on our commitments as of December 31, 2025, our planned aggregate expenditures for aircraft purchase commitments and certain engines on a consolidated basis for calendar years 2026 through 2030 would be approximately $17.5 billion. We may also require financing to refinance maturing obligations and to provide liquidity to fund other corporate requirements. Accordingly, we will need substantial liquidity, financing or other capital resources to finance such aircraft and engines and meet such other liquidity needs. It may be difficult for us to raise additional capital on acceptable terms, or at all, due to, among other factors: our substantial level of existing indebtedness; our non-investment grade corporate credit rating; volatile or otherwise unfavorable market conditions; and the availability of corporate assets to use as collateral for loans or other indebtedness.

### AAL-000000620126000014-0068

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 80891–82349

> An inability to obtain necessary financing on acceptable terms would limit our ability to execute necessary capital projects and would have a material adverse impact on our business, results of operations and financial condition.
> Our high level of debt and other obligations may limit our ability to fund general corporate requirements and obtain additional financing, may limit our flexibility in responding to competitive developments and may cause our business to be vulnerable to adverse economic and industry conditions.
> We have significant amounts of indebtedness and other financial obligations, including obligations to make future payments on flight equipment and property leases related to airport and other facilities, and substantial non-cancelable obligations under aircraft and related spare engine purchase agreements. Moreover, currently a very significant portion of our assets are pledged to secure our indebtedness. Our substantial indebtedness and other obligations, which are generally greater than the indebtedness and other obligations of our competitors, could have important consequences. For example, they may:
> •make it more difficult for us to satisfy our obligations under our indebtedness;
> 22
> Table of Contents
> •limit our ability to obtain additional funding for working capital, capital expenditures, acquisitions, investments and general corporate purposes, and adversely affect the terms on which such funding can be obtained;

### AAL-000000620126000014-0069

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 82350–83772

> •require us to dedicate a substantial portion of our liquidity or cash flow from operations to payments on our indebtedness and other obligations, thereby reducing the funds available for investment in our business and other purposes;
> •make us more vulnerable to economic downturns, industry conditions and catastrophic external events, particularly relative to competitors with lower relative levels of financial leverage;
> •significantly constrain our ability to respond, or respond quickly, to unexpected disruptions in our own operations, the U.S. or global economies, or the businesses in which we operate, or to take advantage of opportunities that would improve our business, operations, or competitive position versus other airlines;
> •limit our ability to withstand competitive pressures and reduce our flexibility in responding to changing business and economic conditions;
> •bear interest at floating rates, subjecting us to volatility in interest expenses as interest rates fluctuate;
> •contain financial covenants, including the requirement to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents and amounts available to be drawn under revolving credit facilities, as well as collateral coverage ratios and peak debt service coverage ratios;
> •impact availability of borrowings under revolving lines of credit; and
> •contain restrictive covenants that could, among other things:

### AAL-000000620126000014-0071

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/aal-20251231.htm), characters 85019–86335

> The obligations discussed above, including those imposed as a result of any additional financings we may undertake, could also impact our ability to obtain additional financing, if needed, and our flexibility in the conduct of our business, and could materially adversely affect our liquidity, results of operations and financial condition.
> Further, a substantial amount of our long-term indebtedness bears interest at floating interest rates, which tend to fluctuate based on general short-term interest rates, rates set by central banks, the supply of and demand for credit in treasury markets and general economic conditions. We have not entered into any derivative transactions to hedge our interest rate exposure. Accordingly, our interest expense for any particular period will fluctuate based on the relevant benchmark rate and other variable interest rates. To the extent the interest rates applicable to our floating rate debt increase, our interest expense will increase, in which event we may have difficulties making interest payments and funding our other fixed costs, and our available cash flow for general corporate requirements may be adversely affected.
> If our financial condition worsens, provisions in our credit card processing and other commercial agreements may adversely affect our liquidity.

### AAL-000000620126000032-0072

mdna, [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000032/aal-20260331.htm), characters 89509–90746

> ITEM 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS
> Part I, Item 2 of this report should be read in conjunction with Part II, Item 7 of AAG’s and American’s Annual Report on Form 10-K for the year ended December 31, 2025 (the 2025 Form 10-K). The information contained herein is not a comprehensive discussion and analysis of the financial condition and results of operations of AAG and American, but rather updates disclosures made in the 2025 Form 10-K.
> Financial Overview
> Business and Macroeconomic Conditions
> Worldwide macroeconomic, political and military events, including war, terrorist activity, and conflict in the Middle East (particularly if it intensifies or is prolonged) and in Ukraine, have contributed, and are likely to continue to contribute, to oil and natural gas price volatility. These factors, along with changes in U.S. or international trade policies and continued uncertainty surrounding such policies, could lead to weakened business conditions for the transportation industry, which may adversely impact our operations through increased supply chain challenges, commodity price volatility and a decline in discretionary spending and consumer confidence, among others.

### AAL-000000620126000032-0095

liquidity, [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/6201/000000620126000032/aal-20260331.htm), characters 120827–122242

> Additionally, a significant portion of our debt financing agreements contain covenants requiring us to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents and amounts available to be drawn under revolving credit facilities. The AAdvantage Financing contains a peak debt service coverage ratio, pursuant to which failure to comply with a certain threshold may result in early repayment, in whole or in part, of the AAdvantage Financing. As of the most recent applicable measurement dates, we were in compliance with each of the foregoing covenants.
> Sources and Uses of Cash
> AAG
> Operating Activities
> Our net cash provided by operating activities was $4.2 billion and $2.5 billion for the first quarter of 2026 and 2025, respectively, a $1.8 billion period-over-period increase driven primarily by working capital increases principally in our air traffic liability and loyalty program deferred revenue.
> Investing Activities
> Our net cash used in investing activities was $2.3 billion and $1.2 billion for the first quarter of 2026 and 2025, respectively.
> Our principal investing activities in the first quarter of 2026 included $1.5 billion in net purchases of short-term investments and $811 million of capital expenditures, which primarily related to the purchase of nine Boeing 737 MAX aircraft, two Embraer E175 aircraft, one Bombardier CRJ900 aircraft and six aircraft engines.

### AAL-000000620126000052-0116

liquidity, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000052/aal-20260630.htm), characters 150486–151493

> Our principal financing activities in the first six months of 2026 included $4.7 billion in long-term debt and finance lease repayments, consisting of $2.1 billion in scheduled repayments, $1.3 billion of early repayments, including $1.0 billion of the outstanding principal amount of the 8.50% senior secured notes and $310 million of equipment notes issued under EETCs, and $1.1 billion from the refinancing in connection with the 2014 Term Loan Facility. Additionally, we repaid all outstanding fuel financing obligations, including $914 million of repayments. These cash outflows were offset in part by $4.5 billion of proceeds from the issuance of long-term debt, primarily consisting of $2.7 billion from the issuance of EETCs, equipment loans and other notes payable in connection with the financing of certain aircraft and spare engines and proceeds from the 2014 Term Loan Facility, which refinanced $1.1 billion of existing term loans and provided $703 million of incremental term loan borrowings.

### AAL-000000620126000065-0050

financial_statements, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/aal-20260930.htm), characters 65646–67139

> 2026 2025
> Net cash provided by operating activities $ 4,440 $ 2,229
> Cash flows from investing activities:
> Capital expenditures and aircraft purchase deposits (2,660) (2,103)
> Proceeds from sale-leaseback transactions and sale of property and equipment 77 243
> Purchases of short-term investments (5,025) (4,801)
> Sales of short-term investments 2,751 4,944
> Decrease (increase) in restricted short-term investments 180 (20)
> Other investing activities (80) 280
> Net cash used in investing activities (4,757) (1,457)
> Cash flows from financing activities:
> Proceeds from issuance of long-term debt 5,933 2,169
> Payments on long-term debt and finance leases (5,343) (3,086)
> Other financing activities (113) 180
> Net cash provided by (used in) financing activities 477 (737)
> Net increase in cash and restricted cash 160 35
> Cash and restricted cash at beginning of period 1,038 893
> Cash and restricted cash at end of period (1)
> $ 1,198 $ 928
> Non-cash transactions:
> Right-of-use assets acquired through operating leases $ 465 $ 980
> Property and equipment acquired through finance leases and other 169 137
> Finance leases converted to operating leases 42 47
> Operating leases converted to finance leases — 104
> Supplemental information:
> Interest paid, net 1,044 1,179
> (1)The following table provides a reconciliation of cash and restricted cash to amounts reported within the condensed consolidated balance sheets:
> Cash $ 1,094 $ 825
> Restricted cash included in restricted cash and short-term investments 104 103

### AAL-000000620126000065-0088

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/aal-20260930.htm), characters 113324–114759

> Liquidity
> As of September 30, 2026, we had $11.8 billion in total available liquidity, consisting of $8.3 billion in unrestricted cash and short-term investments, and $3.5 billion in total undrawn capacity under revolving credit and other facilities.
> During the first nine months of 2026, we completed the following financing transactions (see Note 5 to AAG’s Condensed Consolidated Financial Statements in Part I, Item 1A for further information on 2026 financing activities):
> •repaid in full $629 million of the outstanding principal amount of the senior short-term term loan facility;
> •prepaid in full $1.0 billion of the outstanding principal amount of the 8.50% senior secured notes;
> •amended the terms of the 2025 AAdvantage Term Loan Facility to reduce the applicable interest rate margin;
> •increased the aggregate revolving commitments under the 2013 Revolving Facility, the 2014 Revolving Facility and the 2023 Revolving Facility from $3.0 billion to $3.1 billion and extended the maturity of each facility from June 2029 to March 2031;
> •extended the maturity date of a revolving credit facility that provides for borrowing capacity of up to $350 million by an additional year to March 2028;
> •extended the maturity date of the term loans under the 2014 Credit Agreement from January 2027 to May 2033, refinanced in full the existing term loans of approximately $1.1 billion and incurred incremental term loans of $703 million;

### AAL-000000620126000065-0113

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/aal-20260930.htm), characters 146383–147467

> Other income (expense), net (200) 41 (241) nm
> Total nonoperating expense, net $ (792) $ (570) $ (222) 38.9
> Interest income decreased $93 million, or 12.8%, in the first nine months of 2026 from the first nine months of 2025, primarily due to lower interest rates and a lower average balance of American’s short-term investments, resulting in reduced returns. Interest expense, net decreased $112 million, or 8.4%, in the first nine months of 2026 from the first nine months of 2025, primarily due to repayments of higher interest debt, offset in part by the issuance of debt subsequent to the third quarter of 2025.
> In the first nine months of 2026, other nonoperating expense, net, included $259 million of net special charges, primarily related to mark-to-market net unrealized losses associated with certain equity investments, an impairment charge related to American’s equity investment in Republic Holdings and costs associated with debt refinancings and extinguishments, offset in part by $56 million of non-service-related pension and other postretirement benefit plan income.

### AAL-000000620126000065-0117

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/aal-20260930.htm), characters 150800–152020

> Additionally, a significant portion of our debt financing agreements contain covenants requiring us to maintain an aggregate of at least $2.0 billion of unrestricted cash and cash equivalents and amounts available to be drawn under revolving credit facilities. The AAdvantage Financing contains a peak debt service coverage ratio, pursuant to which failure to comply with a certain threshold may result in early repayment, in whole or in part, of the AAdvantage Financing. As of the most recent applicable measurement dates, we were in compliance with each of the foregoing covenants.
> Sources and Uses of Cash
> AAG
> Operating Activities
> Our net cash provided by operating activities was $4.5 billion and $3.4 billion for the first nine months of 2026 and 2025, respectively, a $1.2 billion period-over-period increase driven primarily by working capital increases principally in our air traffic liability and loyalty program liability, offset in part by lower profitability in the first nine months of 2026 as compared to the same period in 2025.
> 57
> Table of Contents
> Investing Activities
> Our net cash used in investing activities was $4.8 billion and $1.5 billion for the first nine months of 2026 and 2025, respectively.

## Run

Run `AAL-20261118T063244Z-DeepSeek-V4.1-Flash-1017`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 9 calls, 37,105 input (13,056 cached) and 22,962 output tokens, $0.0091, 468s. Verification: 36 calls, 17,142 input (4,608 cached) and 3,098 output tokens, $0.0227, 79s. Prices read 2026-11-17. Raw requests and responses: data/runs/AAL/AAL-20261118T063244Z-DeepSeek-V4.1-Flash-1017.jsonl.
