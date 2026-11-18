# Credit memo: CLEVELAND-CLIFFS INC. (CLF)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4-Pro-0813`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-5**.
Sources: [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm); [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000070/clf-20260331.htm); [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000100/clf-20260630.htm)

Claims: 35 — 33 supported, 1 partially supported, 1 unsupported. Raw numbers rejected in first drafts: 1; repairs: 1.

## Business profile

1. Cleveland-Cliffs is a leading North America-based steel producer with a focus on value-added sheet products, particularly for the automotive industry.  
   ✅ supported (judge): The evidence passage states this verbatim.
   - cites `CLF-000076406526000100-0055` ✓: “We are a leading North America-based steel producer with focus on value-added sheet products, particularly for the automotive industry.”
2. The company is vertically integrated from iron ore mining, pellet production, direct reduced iron and ferrous scrap processing through primary steelmaking and downstream finishing, stamping, tooling and tubing.  
   ✅ supported (judge): The passage states the company is vertically integrated from mining of iron ore, pellets, DRI, and ferrous scrap processing through steelmaking and downstream finishing, stamping, tooling, and tubing, matching the claim.
   - cites `CLF-000076406526000100-0055` ✓: “We are vertically integrated from the mining of iron ore, production of pellets and direct reduced iron”
   - cites `CLF-000076406526000100-0055` ✓: “through primary steelmaking and downstream finishing, stamping, tooling, and tubing”
3. The company offers a full suite of flat steel products and is a leading supplier to the automotive sector.  
   ✅ supported (judge): Both parts of the claim are directly stated in the evidence.
   - cites `CLF-000076406526000115-0068` ✓: “We offer a full suite of flat steel products encompassing effectively all of our customers' needs. We are a leading supplier to the automotive sector”
4. Ferrous raw materials are primarily internally sourced from iron ore mines in Michigan and Minnesota, and the company sells into four broad market categories.  
   ✅ supported (judge): Both parts of the claim are stated directly in the evidence.
   - cites `CLF-000076406526000025-0024` ✓: “Ferrous raw materials for the production of steel are primarily internally sourced from our iron ore mines in Michigan and Minnesota”
   - cites `CLF-000076406526000025-0024` ✓: “We primarily sell our products to customers in four broad market categories.”
5. A sustained, significant decline in market pricing is one of the indicators that can trigger long-lived asset impairment, and adverse changes in these factors could have a material impact on the consolidated statements of operations and financial position.  
   ✅ supported (judge): The passage explicitly lists a sustained, significant decline in market pricing as an impairment indicator and states adverse changes could materially impact the consolidated statements of operations and financial position.
   - cites `CLF-000076406526000115-0108` ✓: “a sustained, significant decline in market pricing”
   - cites `CLF-000076406526000115-0108` ✓: “could have a material impact on our consolidated statements of operations and statements of financial position”
6. Revenue was **$22.0 billion** [F1] in the fiscal year ended 31 December 2023, **$19.2 billion** [F2] in the fiscal year ended 31 December 2024, **$18.6 billion** [F3] in the fiscal year ended 31 December 2025, and **$20.1 billion** [F4] in the twelve months to 30 September 2026; EBITDA was **-$344 million** [F5] in the fiscal year ended 31 December 2025 and **$770 million** [F6] in the twelve months to 30 September 2026.  
   ✅ supported (judge): All revenue and EBITDA figures in the claim match the metric values computed from XBRL data exactly.

## Financial risk

1. Debt/EBITDA rose from **2.05x** [F7] in the fiscal year ended 31 December 2023 to **9.93x** [F8] in the twelve months to 30 September 2026, and net leverage rose from **1.93x** [F9] to **9.83x** [F10].  
   ✅ supported (judge): All four leverage figures in the claim match the computed metric values exactly (2.05x→9.93x debt/EBITDA; 1.93x→9.83x net leverage).
2. EBITDA/interest coverage fell from **5.65x** [F11] in the fiscal year ended 31 December 2023 to **1.27x** [F12] in the twelve months to 30 September 2026, while FCF/debt fell from **48.4%** [F13] to **-6.3%** [F14].  
   ✅ supported (judge): All four metric values in the claim match the XBRL-computed scorecard exactly.
3. The deterioration in the fiscal year ended 31 December 2024 and the fiscal year ended 31 December 2025 reflected lower gross margins from a decrease in selling prices for steel products.  
   ✅ supported (judge): The passage directly attributes the 2025 vs 2024 variance to lower gross margins from decreased selling prices for steel products.
   - cites `CLF-000076406526000025-0215` ✓: “A $989 million decrease in net income after adjustments for non-cash items due to lower gross margins resulting from a decrease in selling prices for our steel products.”
4. Steelmaking Adjusted EBITDA increased compared with the prior-year periods, primarily due to higher gross margin, supporting a partial rebound in LTM coverage metrics.  
   ◐ partially supported (judge): The passage supports increased Steelmaking Adjusted EBITDA driven primarily by higher gross margin, but the claim about a partial rebound in LTM coverage metrics has no supporting evidence.
   - cites `CLF-000076406526000115-0083` ✓: “increased by $468 million and $927 million, respectively, as compared to the prior-year periods, primarily due to the increased gross margin from our Steelmaking operations.”
5. In the twelve months to 30 September 2026, cash from operations of **$116 million** [F15] was below capital expenditures of **$601 million** [F16], contributing to negative FCF/debt of **-6.3%** [F14].  
   ✅ supported (judge): All three figures—LTM cash from operations of $116M, capex of $601M, and FCF/debt of -6.3%—match the computed metric values exactly, and CFO below capex implies negative FCF.
6. The company expects total cash used for capital expenditures over the next **12** [quoted: CLF-000076406526000100-0087] months to be approximately $**900** [quoted: CLF-000076406526000100-0087] million, primarily for sustaining capital spend.  
   ✅ supported (judge): The passage states expected capex of ~$900 million over next 12 months, primarily sustaining capital spend.
   - cites `CLF-000076406526000100-0087` ✓: “We anticipate total cash used for capital expenditures during the next 12 months to be approximately $900 million, which primarily consists of sustaining capital spend”

## Liquidity

1. In the twelve months to 30 September 2026, liquidity coverage was **0.32x** [F17], compared with **0.10x** [F18] in the fiscal year ended 31 December 2025.  
   ✅ supported (judge): Both metric values match the claim exactly: LTM to 30 September 2026 liquidity coverage of 0.32x and FY ended 31 December 2025 of 0.10x.
2. In the twelve months to 30 September 2026, cash and cash equivalents were **$77 million** [F19] and cash from operations was **$116 million** [F15].  
   ✅ supported (judge): Both figures match the XBRL-computed metric values for the twelve months to 30 September 2026.
3. In the twelve months to 30 September 2026, capital expenditure was **$601 million** [F16], dividends paid were **$0** [F20], and short-term debt was **$0** [F21].  
   ✅ supported (judge): The claim's three figures match the computed XBRL metric values exactly: capex $601M, dividends paid $0 (not reported, assumed zero), and short-term debt $0 (not reported, assumed zero).
4. Management identified cash, cash from operations, ABL facility availability, and capital markets as primary liquidity sources and stated that they would be adequate for the next twelve months.  
   ✅ supported (judge): The passage lists exactly those four liquidity sources and states adequacy for the next 12 months.
   - cites `CLF-000076406526000115-0090` ✓: “Our primary sources of liquidity are Cash and cash equivalents, cash generated from our operations, availability under our ABL Facility and access to capital markets.”
   - cites `CLF-000076406526000115-0090` ✓: “We believe our liquidity and access to capital markets will be adequate to fund our cash requirements for the next 12 months and for the foreseeable future.”
5. In the twelve months to 30 September 2026, cash plus ABL facility availability equated to $**3.2** [quoted: CLF-000076406526000115-0090] billion in liquidity.  
   ✅ supported (judge): The passage explicitly states cash plus ABL availability equated to $3.2 billion in liquidity as of September 30, 2026.
   - cites `CLF-000076406526000115-0090` ✓: “The combination of cash and availability under our ABL Facility equated to $3.2 billion in liquidity”
6. At the fiscal year ended 31 December 2025, the ABL facility had a maximum borrowing base of $**4.75** [quoted: CLF-000076406526000025-0329] billion.  
   ✅ supported (judge): The passage states the ABL Facility had a maximum borrowing base of $4.75 billion as of December 31, 2025.
   - cites `CLF-000076406526000025-0329` ✓: “the ABL Facility has a maximum borrowing base of $4.75 billion”

## Maturity wall

1. As of the fiscal year ended 31 December 2025, the maturity schedule shows no debt due in the next twelve months (**$0** [F22]) or in year two (**$0** [F23]), with **$452 million** [F24] maturing in year three.  
   ✅ supported (judge): The XBRL-computed metric values match every figure in the claim: $0 next twelve months, $0 year two, $452 million year three.
2. Debt due within the next two years was **$0** [F25], or **0.0%** [F26] of total debt, and near-term maturity cover was **0.00x** [F27] at the fiscal year ended 31 December 2025.  
   ✅ supported (judge): The computed metric values directly state $0 debt due within 24 months, 0.0% share, and 0.00x near-term maturity cover for FY ended 31 Dec 2025.
3. As of the fiscal year ended 31 December 2025, amounts due in year four, year five, and after year five are **$1.3 billion** [F28], **$750 million** [F29], and **$4.9 billion** [F30], respectively.  
   ✅ supported (judge): All three claimed values match the XBRL-computed metric values for FY0.
4. During **2025** [quoted: CLF-000076406526000025-0218], the company used note issuance proceeds to extend debt maturities by redeeming all remaining **2027** [quoted: CLF-000076406526000025-0218] senior notes and repaying borrowings on its ABL Facility.  
   ✅ supported (judge): The passage states the company used proceeds from its 2025 note and share issuances to extend debt maturities by redeeming all remaining 2027 senior notes and repaying ABL Facility borrowings, exactly matching the claim.
   - cites `CLF-000076406526000025-0218` ✓: “we used the proceeds from these transactions to extend debt maturities by redeeming all remaining 2027 senior notes and repay borrowings on our ABL Facility.”
5. The ABL Facility matures in June **2028** [quoted: CLF-000076406526000025-0219] and has a maximum borrowing base of $**4.75** [quoted: CLF-000076406526000025-0219] billion.  
   ✅ supported (judge): Both the June 2028 maturity and $4.75 billion maximum borrowing base are directly stated in the passage.
   - cites `CLF-000076406526000025-0219` ✓: “Our ABL Facility, which matures in June 2028, has a maximum borrowing base of $4.75 billion.”
6. As of September **30** [quoted: CLF-000076406526000115-0091], **2026** [quoted: CLF-000076406526000115-0091], the company was in compliance with the ABL Facility liquidity requirements, and the springing financial covenant requiring a minimum fixed charge coverage ratio of **1.0** [quoted: CLF-000076406526000115-0091] to **1.0** [quoted: CLF-000076406526000115-0091] was not applicable.  
   ✅ supported (judge): The passage states compliance with ABL liquidity requirements as of September 30, 2026 and that the springing fixed charge coverage ratio covenant of 1.0 to 1.0 was not applicable.
   - cites `CLF-000076406526000115-0091` ✓: “we were in compliance with the ABL Facility liquidity requirements and, therefore, the springing financial covenant requiring a minimum fixed charge coverage ratio of 1.0 to 1.0 was not applicable”

## Key risks

1. For the twelve months to 30 September 2026, debt-to-EBITDA was **9.93x** [F8], EBITDA-to-interest coverage was **1.27x** [F12], liquidity coverage was **0.32x** [F17], and free cash flow to debt was **-6.3%** [F14].  
   ✅ supported (judge): All four claimed ratios match the computed LTM metric values exactly.
2. The company's existing and future indebtedness may limit cash flow available to invest in its businesses and could force it to take actions to satisfy debt obligations that may not be successful.  
   ✅ supported (judge): The claim directly restates the risk factor sentence in the evidence.
   - cites `CLF-000076406526000025-0102` ✓: “Our existing and future indebtedness may limit cash flow available to invest in the ongoing needs of our businesses”
3. The company may not be able to refinance all or a portion of its existing debt on commercially reasonable terms or at all, and any refinancing could be at higher interest rates and require more onerous covenants.  
   ✅ supported (judge): The passage states exactly that the company may not be able to refinance on commercially reasonable terms or at all, and refinancing could be at higher interest rates with more onerous covenants.
   - cites `CLF-000076406526000025-0105` ✓: “requiring us to refinance all or a portion of our existing debt. We may not be able to refinance on commercially reasonable terms or at all”
4. Because a portion of its borrowing capacity and outstanding indebtedness under the ABL Facility bears interest at a variable rate based on SOFR, higher-than-expected interest rates would increase the cash needed to service interest expense.  
   ✅ supported (judge): Both passages directly state that ABL Facility borrowings bear interest at a variable SOFR-based rate and that higher-than-expected rates would increase cash needed to service interest expense.
   - cites `CLF-000076406526000025-0106` ✓: “A portion of our borrowing capacity and any outstanding indebtedness under our ABL Facility bears interest at a variable rate based on SOFR.”
   - cites `CLF-000076406526000025-0103` ✓: “Higher-than-expected interest rates would increase the amount of cash we would need to allocate to servicing the interest expense on our debt”
5. Credit ratings downgrades could adversely affect the company's access to capital markets and the terms under which it purchases goods and services.  
   ✅ supported (judge): The passage directly states that downgrades by credit ratings agencies could adversely affect access to capital markets and the terms under which the company purchases goods and services.
   - cites `CLF-000076406526000025-0106` ✓: “access to the capital markets, and the terms under which we purchase goods and services could be adversely affected when credit ratings agencies downgrade our ratings”

## Rating rationale

1. The stylized internal scorecard grade is **SB-5** [F31], corresponding to a weighted score of **5.50** [F32]; the grade is not provisional because all six factors were scored, and it is not a credit rating.  
   ✅ supported (judge): The scorecard metrics confirm SB-5 grade, weighted score of 5.50, all six factors scored so not provisional, and it is stylized, not a credit rating.
2. The weakest factors are debt/EBITDA at band **6** [F33] with **20.0%** [F34] weight, net leverage at band **6** [F35] with **10.0%** [F36] weight, EBITDA/interest at band **6** [F37] with **25.0%** [F38] weight, FCF/debt at band **6** [F39] with **20.0%** [F40] weight, and liquidity coverage at band **6** [F41] with **15.0%** [F42] weight.  
   ✅ supported (judge): All five listed factors match the metric values exactly at band 6 with the stated weights, and the only remaining factor (near-term maturity cover) is at band 1, so these five are indeed the weakest.
3. The strongest factor is near-term maturity cover, scoring band **1** [F43] with **10.0%** [F44] weight.  
   ✅ supported (judge): Near-term maturity cover is the only factor in band 1 (all others are band 6), and its weight is 10.0%, matching the claim.
4. The weak leverage and coverage bands reflect the deterioration to **9.93x** [F8], **9.83x** [F10], **1.27x** [F12], and **-6.3%** [F14], driven by lower gross margins from a decrease in selling prices for steel products.  
   ✅ supported (judge): The four metric values (9.93x, 9.83x, 1.27x, -6.3%) and weak bands (band 6 of 6) match the scorecard, and the filing attributes the deterioration to lower gross margins from decreased selling prices for steel products.
   - cites `CLF-000076406526000025-0215` ✓: “lower gross margins resulting from a decrease in selling prices for our steel products”
5. Near-term maturity cover scores strongest because the maturity schedule shows no debt due in the next twelve months or year two.  
   ❌ unsupported (judge): While the maturity table confirms $0 due in 2026 and 2027, the scorecard shows near_term_maturity_cover in band 1 of 6 — the weakest band, not the strongest (other factors score band 6).
   - cites `CLF-000076406526000025-0329` ✓: “$ — $ — $ 452 $ 1,268 $ 750 $ 4,860 $ 7,330”
6. Liquidity coverage scores band **6** [F41] with **15.0%** [F42] weight, but liquidity is partly supported by management's view that cash, cash from operations, ABL facility availability, and capital markets will be adequate for the next twelve months.  
   ✅ supported (judge): The metrics confirm liquidity coverage scored band 6 with a 15.0% weight, and the passage confirms management's stated sources (cash, operations, ABL availability, capital markets) and belief that liquidity will be adequate for the next 12 months.
   - cites `CLF-000076406526000115-0090` ✓: “We believe our liquidity and access to capital markets will be adequate to fund our cash requirements for the next 12 months”

## Reviewer checklist

- [ ] **fallback** (info): Interest expense: used rank 5 −InterestIncomeExpenseNonoperatingNet in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt) assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term investments assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Dividends paid assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Finance-lease liabilities (current plus non-current) assumed zero (not reported) in LTM.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The passage supports increased Steelmaking Adjusted EBITDA driven primarily by higher gross margin, but the claim about a partial rebound in LTM coverage metrics has no supporting evidence.): “Steelmaking Adjusted EBITDA increased compared with the prior-year periods, primarily due to higher gross margin, supporting a partial rebound in LTM coverage metrics.”
- [ ] **unsupported claim** (warning): Rating rationale: unsupported (While the maturity table confirms $0 due in 2026 and 2027, the scorecard shows near_term_maturity_cover in band 1 of 6 — the weakest band, not the strongest (other factors score band 6).): “Near-term maturity cover scores strongest because the maturity schedule shows no debt due in the next twelve months or year two.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $22.0 billion | rank 1: Revenues | Revenues 21,996,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F2 | Revenue (revenue:FY-1) | $19.2 billion | rank 1: Revenues | Revenues 19,185,000,000 (2024-01-01 to 2024-12-31, FY-1) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F3 | Revenue (revenue:FY0) | $18.6 billion | rank 1: Revenues | Revenues 18,610,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F4 | Revenue (revenue:LTM) | $20.1 billion | rank 1: Revenues | Revenues 18,610,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>Revenues 15,760,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>Revenues 14,297,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F5 | EBITDA (ebitda:FY0) | -$344 million | operating_income + d_and_a | OperatingIncomeLoss -1,579,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 1,235,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F6 | EBITDA (ebitda:LTM) | $770 million | operating_income + d_and_a | OperatingIncomeLoss -1,579,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>OperatingIncomeLoss 49,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>OperatingIncomeLoss -1,248,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 1,235,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 780,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 963,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY-2) | 2.05x | total_debt / EBITDA | LongTermDebtNoncurrent 3,137,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>FinanceLeaseLiabilityCurrent 49,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>FinanceLeaseLiabilityNoncurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>OperatingIncomeLoss 659,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 973,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:LTM) | 9.93x | total_debt / EBITDA | LongTermDebtNoncurrent 7,645,000,000 (at 2026-09-30, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>OperatingIncomeLoss -1,579,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>OperatingIncomeLoss 49,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>OperatingIncomeLoss -1,248,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 1,235,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 780,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 963,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F9 | Net leverage (net_leverage:FY-2) | 1.93x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 3,137,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>FinanceLeaseLiabilityCurrent 49,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>FinanceLeaseLiabilityNoncurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 198,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>OperatingIncomeLoss 659,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 973,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F10 | Net leverage (net_leverage:LTM) | 9.83x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 7,645,000,000 (at 2026-09-30, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 77,000,000 (at 2026-09-30, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>OperatingIncomeLoss -1,579,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>OperatingIncomeLoss 49,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>OperatingIncomeLoss -1,248,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 1,235,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 780,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 963,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F11 | EBITDA / interest (interest_coverage:FY-2) | 5.65x | EBITDA / interest_expense | OperatingIncomeLoss 659,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 973,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>InterestIncomeExpenseNonoperatingNet -289,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F12 | EBITDA / interest (interest_coverage:LTM) | 1.27x | EBITDA / interest_expense | OperatingIncomeLoss -1,579,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>OperatingIncomeLoss 49,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>OperatingIncomeLoss -1,248,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 1,235,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>DepreciationDepletionAndAmortization 780,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>DepreciationDepletionAndAmortization 963,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>InterestIncomeExpenseNonoperatingNet -594,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>InterestIncomeExpenseNonoperatingNet -452,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F13 | FCF / debt (fcf_to_debt:FY-2) | 48.4% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 2,267,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 646,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>LongTermDebtNoncurrent 3,137,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>FinanceLeaseLiabilityCurrent 49,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm)<br>FinanceLeaseLiabilityNoncurrent 166,000,000 (at 2023-12-31, balance sheet) [10-K 0000764065-25-000058](https://www.sec.gov/Archives/edgar/data/764065/000076406525000058/0000764065-25-000058-index.htm) |
| F14 | FCF / debt (fcf_to_debt:LTM) | -6.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities -462,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 129,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -449,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 561,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 461,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 421,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>LongTermDebtNoncurrent 7,645,000,000 (at 2026-09-30, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F15 | Cash from operations (cfo:LTM) | $116 million | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities -462,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 129,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -449,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F16 | Capital expenditure (capex:LTM) | $601 million | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 561,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 461,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 421,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F17 | Liquidity coverage (liquidity_coverage:LTM) | 0.32x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 77,000,000 (at 2026-09-30, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -462,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 129,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -449,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 561,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 461,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 421,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F18 | Liquidity coverage (liquidity_coverage:FY0) | 0.10x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 57,000,000 (at 2025-12-31, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -462,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 561,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F19 | Cash and cash equivalents (cash:LTM) | $77 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 77,000,000 (at 2026-09-30, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F20 | Dividends paid (dividends:LTM) | $0 |  | — |
| F21 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $0 |  | — |
| F22 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $0 | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 0 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F23 | Debt maturing in year two (maturity_year_2:FY0) | $0 | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F24 | Debt maturing in year three (maturity_year_3:FY0) | $452 million | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 452,000,000 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F25 | Debt due within 24 months (debt_due_24m:FY0) | $0 | short_term_debt + maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F26 | Share of debt due within 24 months (share_due_24m:FY0) | 0.0% | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>LongTermDebtNoncurrent 7,253,000,000 (at 2025-12-31, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm)<br>FinanceLeaseLiabilityCurrent 67,000,000 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>FinanceLeaseLiabilityNoncurrent 335,000,000 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F27 | Near-term maturity cover (near_term_maturity_cover:FY0) | 0.00x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 57,000,000 (at 2025-12-31, balance sheet) [10-Q 0000764065-26-000115](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/0000764065-26-000115-index.htm) |
| F28 | Debt maturing in year four (maturity_year_4:FY0) | $1.3 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 1,268,000,000 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F29 | Debt maturing in year five (maturity_year_5:FY0) | $750 million | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 750,000,000 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F30 | Debt maturing after year five (maturity_after_year_5:FY0) | $4.9 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 4,860,000,000 (at 2025-12-31, balance sheet) [10-K 0000764065-26-000025](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/0000764065-26-000025-index.htm) |
| F31 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 5.5 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F32 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 5.5 | sum of weight x band over the factors scored, divided by their weights | — |
| F33 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 6 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F34 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F35 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 6 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F36 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F37 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 6 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F38 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F39 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 6 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F40 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F41 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F42 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F43 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 1 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F44 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### CLF-000076406526000025-0024

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 29288–30747

> Ferrous raw materials for the production of steel are primarily internally sourced from our iron ore mines in Michigan and Minnesota, our direct reduction plant in Ohio, and our scrap facilities in Illinois, Michigan, Mississippi, Ohio, Tennessee and Ontario. We also operate a coal mining complex in West Virginia and produce coke from our facilities in Indiana, Ohio, Pennsylvania and Ontario.
> Our Other Businesses primarily includes the Tubular and Tooling and Stamping operating segments that provide customer solutions with carbon and stainless steel tubing products, advanced-engineered solutions, tool design and build, hot- and cold-stamped steel components and complex assemblies.
> Refer to Part I – Item 2. Properties for additional information.
> 6 | CLF 2025 FORM 10-K
> Table of Contents
> PRODUCTS AND MARKETS
> 2025 Product Mix (By Revenue) Primary Products as of December 31, 2025
> ◦HOT-ROLLED
> ◦STAINLESS AND ELECTRICAL
> ◦OTHER
> ◦COLD-ROLLED
> ◦Scrap
> ◦COATED
> ◦GOES
> ◦Iron Ore
> ◦Aluminized
> ◦NOES
> ◦HBI
> ◦Electrogalvanized
> ◦Auto Chrome
> ◦Coal
> ◦Galvalume
> ◦PLATE
> ◦Coke
> ◦Galvanneal
> ◦SLAB AND OTHER STEEL PRODUCTS
> ◦NON-STEELMAKING
> ◦Hot-dipped Galvanized
> ◦Stamped Components
> ◦Tool and Die
> ◦Tubing
> As a fully integrated steel enterprise, we have a comprehensive portfolio of steel solutions. We primarily sell our products to customers in four broad market categories. The following table presents the percentage of our revenues to each of these markets during the year:

### CLF-000076406526000025-0102

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 116147–117339

> Our existing and future indebtedness may limit cash flow available to invest in the ongoing needs of our businesses, which could prevent us from fulfilling our obligations under our senior notes, ABL Facility and other debt, and we may be forced to take other actions to satisfy our obligations under our debt, which may not be successful.
> As of December 31, 2025, we had $6.9 billion aggregate principal amount of senior notes and $452 million aggregate borrowings under our ABL Facility outstanding (excluding $65 million of outstanding letters of credit and $402 million of finance leases) and $57 million of cash on our statement of consolidated financial position. The aggregate principal amount of revolver commitments under our ABL Facility is $4.75 billion, comprised of $4.25 billion of lending commitments available to be borrowed by us and certain of our U.S. subsidiaries, and $500 million of lending commitments available to be borrowed by certain of our Canadian subsidiaries. As of December 31, 2025, the aggregate borrowing availability under our ABL Facility was $3.2 billion based on amounts currently drawn, outstanding letters of credit obligations and our borrowing base.

### CLF-000076406526000025-0103

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 117340–118186

> A portion of our cash flow from operations is used to service debt under our senior notes and ABL Facility, reducing the availability of cash to fund capital expenditures, acquisitions or strategic development initiatives, and other general corporate purposes, or to retire debt or return capital to shareholders, including via share repurchases. While we currently expect the U.S. Federal Reserve to lower interest rates during 2026, decisions regarding the trajectory of future interest rates are uncertain, and there is risk that interest rates could be maintained or even increased. Higher-than-expected interest rates would increase the amount of cash we would need to allocate to servicing the interest expense on our debt for so long as we have an outstanding balance drawn under our ABL Facility.
> 21 | CLF 2025 FORM 10-K
> Table of Contents

### CLF-000076406526000025-0105

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 119563–120561

> Our level of indebtedness could have further consequences, including, but not limited to, increasing our vulnerability to adverse economic or industry conditions, placing us at a competitive disadvantage compared to other businesses in the industries in which we operate that are not as leveraged and that may be better positioned to withstand economic downturns and recessionary environments, limiting our flexibility to plan for, or react to, changes in our businesses and the industries in which we operate, and requiring us to refinance all or a portion of our existing debt. We may not be able to refinance on commercially reasonable terms or at all, and any refinancing of our debt could be at higher interest rates and may require us to comply with more onerous covenants, making it more difficult to obtain surety bonds, letters of credit or other financial assurances that may be demanded by our vendors or regulatory agencies, particularly during periods in which credit markets are weak.

### CLF-000076406526000025-0106

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 120562–122032

> In addition, our cost of financing or refinancing, access to the capital markets, and the terms under which we purchase goods and services could be adversely affected when credit ratings agencies downgrade our ratings, whether due to factors specific to our business or debt profile, a prolonged cyclical downturn in the steel, scrap metal and mining industries or macroeconomic trends (such as global or regional recessions), increases in pension and OPEB obligations, adverse impacts of inflation and high interest rates, or trends in credit and capital markets more generally. A portion of our borrowing capacity and any outstanding indebtedness under our ABL Facility bears interest at a variable rate based on SOFR. To the extent these interest rates increase, our interest expense will increase. Restricted access to capital markets and/or increased borrowing costs could have an adverse effect on our results of operations, cash flows, financial condition and liquidity.
> We continue to face ongoing risks arising out of the Stelco Acquisition and may be unable to realize the anticipated financial and other benefits from proposed strategic partnerships and asset divestitures.
> We completed the Stelco Acquisition in the fourth quarter of 2024. We remain subject to significant risks and uncertainties arising out of the Stelco Acquisition that may adversely affect us, including in connection with the following:
> •our ability to service additional debt incurred;

### CLF-000076406526000025-0215

mdna, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 242958–244427

> (In millions) 2025 2024
> Cash flows provided by (used in):
> Operating activities $ (462) $ 105
> Investing activities (479) (3,212)
> Financing activities 942 2,970
> Net increase (decrease) in cash and cash equivalents $ 1 $ (137)
> CASH FLOWS
> OPERATING ACTIVITIES
> Year Ended December 31,
> (In millions) 2025 2024 Variance
> Net loss $ (1,428) $ (714) $ (714)
> Non-cash adjustments to net loss 754 1,029 (275)
> Income taxes 13 (17) 30
> Pension and OPEB payments and contributions (154) (195) 41
> Working capital (receivables, inventories, payables and other liabilities) 353 2 351
> Net cash provided (used) by operating activities $ (462) $ 105 $ (567)
> The variance was driven by:
> •A $989 million decrease in net income after adjustments for non-cash items due to lower gross margins resulting from a decrease in selling prices for our steel products. See "— Steelmaking Results" above for further detail on our operating results.
> •A $351 million increase in cash provided by working capital is primarily related to a reduction in iron ore pellet inventory in comparison to the build of iron ore pellet inventory in the prior year and is also related to a reduction in payables due to cost-cutting efforts. These increases were partially offset by a decrease in accounts receivable collections year over year as a result of lower total revenue.
> INVESTING ACTIVITIES
> Year Ended December 31,
> (In millions) 2025 2024 Variance
> Purchase of property, plant and equipment $ (561) $ (695) $ 134

### CLF-000076406526000025-0218

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 246965–248091

> LIQUIDITY AND CAPITAL RESOURCES
> Our primary sources of liquidity are Cash and cash equivalents, cash generated from our operations, availability under our ABL Facility and access to the capital markets. Cash and cash equivalents, which totaled $57 million as of December 31, 2025, include cash on hand and on deposit, as well as short-term securities held for the primary purpose of general liquidity. The combination of cash and availability under our ABL Facility equated to $3.3 billion in liquidity as of December 31, 2025. During 2025, we issued $850 million in aggregate principal amount of our 7.500% 2031 Senior Notes and $1,125 million in aggregate principal amount of our 7.625% 2034 Senior Notes, as well as 75 million of our common shares resulting in $951 million of net cash proceeds. In totality, we used the proceeds from these transactions to extend debt maturities by redeeming all remaining 2027 senior notes and repay borrowings on our ABL Facility. We believe our liquidity and access to capital markets will be adequate to fund our cash requirements for the next 12 months and for the foreseeable future.

### CLF-000076406526000025-0219

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 248092–249061

> Our ABL Facility, which matures in June 2028, has a maximum borrowing base of $4.75 billion. The available borrowing base, which was $3.2 billion as of December 31, 2025, is determined by applying customary advance rates to eligible accounts receivable, inventory and certain mobile equipment. Our ABL Facility includes a $555 million sublimit for the issuance of letters of credit and a $200 million sublimit for swingline loans. As of December 31, 2025, outstanding letters of credit totaled $65 million, which reduced availability under our ABL Facility. We issue standby letters of credit with certain financial institutions in order to support business obligations, including, but not limited to, workers' compensation, operating agreements, employee severance, environmental obligations and insurance. Our ABL Facility agreement contains various financial and other covenants. As of December 31, 2025, we were in compliance with all of our ABL Facility covenants.

### CLF-000076406526000025-0329

debt_note, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/764065/000076406526000025/clf-20251231.htm), characters 382889–384083

> Borrowing capacity available $ 3,213
> 1 As of December 31, 2025, the ABL Facility has a maximum borrowing base of $4.75 billion. The available borrowing base is determined by applying customary advance rates to eligible accounts receivable, inventory and certain mobile equipment.
> 2 We issued standby letters of credit with certain financial institutions in order to support business obligations, including, but not limited to, operating agreements, employee severance, environmental obligations, workers' compensation, and insurance obligations.
> DEBT EXTINGUISHMENTS
> On October 3, 2025, we used the net proceeds from the issuance of our 7.625% 2034 Senior Notes to redeem $73 million in aggregate principal amount of our 7.000% 2027 Senior Notes, $56 million in aggregate principal amount of our 7.000% 2027 AK Senior Notes, and $556 million in aggregate principal amount of our 5.875% 2027 Senior Notes.
> MATURITIES
> The following represents a summary of our debt instrument maturities based on the principal amounts outstanding as of December 31, 2025 (in millions):
> 2026 2027 2028 2029 2030 Thereafter Total
> $ — $ — $ 452 $ 1,268 $ 750 $ 4,860 $ 7,330
> 84 | CLF 2025 FORM 10-K
> Table of Contents

### CLF-000076406526000100-0055

mdna, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000100/clf-20260630.htm), characters 68940–69464

> We are a leading North America-based steel producer with focus on value-added sheet products, particularly for the automotive industry. We are vertically integrated from the mining of iron ore, production of pellets and direct reduced iron, and processing of ferrous scrap through primary steelmaking and downstream finishing, stamping, tooling, and tubing. Headquartered in Cleveland, Ohio, we employ approximately 25,000 people across our operations in the United States and Canada.
> ECONOMIC OVERVIEW
> STEEL MARKET OVERVIEW

### CLF-000076406526000100-0087

mdna, [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000100/clf-20260630.htm), characters 107138–108602

> Our cash used for capital expenditures during the six months ended June 30, 2026 was $45 million higher than the prior-year period. Our cash used for capital expenditures primarily relates to sustaining capital spend, which includes infrastructure, mobile equipment, fixed equipment, product quality, environmental, and health and safety spend. Included within cash used for capital expenditures was $5 million related to our non-owned SunCoke Middletown VIE for the six months ended June 30, 2026, compared to a nominal amount for the six months ended June 30, 2025.
> We anticipate total cash used for capital expenditures during the next 12 months to be approximately $900 million, which primarily consists of sustaining capital spend and includes spending related to the major reline project at our Burns Harbor C blast furnace.
> FINANCING ACTIVITIES
> Six Months Ended
> June 30,
> (In millions) 2026 2025 Variance
> Net proceeds of senior notes $ — $ 850 $ (850)
> Net borrowings (repayments) under ABL Facility 444 (183) 627
> Other financing activities (69) (100) 31
> Net cash provided (used) by financing activities $ 375 $ 567 $ (192)
> The period-over-period change in financing activities reflects differences in our capital‑raising and borrowing activity:
> •For the six months ended June 30, 2025: We issued $850 million aggregate principal amount of 7.500% Senior Notes due 2031 at par. The net proceeds were used in part to repay borrowings under our ABL Facility; and

### CLF-000076406526000115-0068

mdna, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/clf-20260930.htm), characters 84395–85829

> One of our most critical strengths that differentiates us from others in our industry is a unique and powerful partnership with our unionized workforce, particularly the USW. We are currently engaged in good faith negotiations with the USW to renew various collective bargaining agreements across our mining and steelmaking operations. With over 18,000 employees subject to collective bargaining agreements, our strong and productive labor relationships are key to our long-term success and allow us to work together in achieving our goals. A clear example of the strength of our relationship is how we partner together to fight against dumped and illegally subsidized imported steel products. Our deep alignment with our represented employees is also recognized by our political leaders, who often publicly support us as a significant employer of a unionized workforce with a track record of working to maintain and increase middle class jobs.
> STRATEGY
> MAXIMIZE OUR COMMERCIAL STRENGTHS
> We offer a full suite of flat steel products encompassing effectively all of our customers' needs. We are a leading supplier to the automotive sector, where our portfolio of high-end products delivers a broad range of differentiated solutions for this highly sought-after customer base. As an established and reliable supplier of domestically produced automotive-grade steel, we expect to bolster our position as an industry leader going forward.

### CLF-000076406526000115-0083

mdna, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/clf-20260930.htm), characters 102318–103479

> Adjusted EBITDA from our Steelmaking segment for the three and nine months ended September 30, 2026, increased by $468 million and $927 million, respectively, as compared to the prior-year periods, primarily due to the increased gross margin from our Steelmaking operations. This gross margin increase included a net decrease in idled facilities charges, which is excluded from Adjusted EBITDA.
> RESULTS OF OPERATIONS
> REVENUES & GROSS MARGIN
> During the three and nine months ended September 30, 2026, our consolidated Revenues increased by $878 million and $1.5 billion, respectively, and our consolidated gross margin increased by $511 million and $1.2 billion, respectively, as compared to the prior-year periods. See "— Steelmaking Results" above for further detail on our operating results.
> SELLING, GENERAL AND ADMINISTRATIVE EXPENSES
> Selling, general and administrative expenses increased by $23 million and $32 million for the three and nine months ended September 30, 2026, respectively, as compared to the prior-year period. The increases were primarily driven by higher incentive based compensation.
> RESTRUCTURING AND OTHER CHARGES AND ASSET IMPAIRMENT

### CLF-000076406526000115-0090

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/clf-20260930.htm), characters 110879–111561

> LIQUIDITY AND CAPITAL RESOURCES
> Our primary sources of liquidity are Cash and cash equivalents, cash generated from our operations, availability under our ABL Facility and access to capital markets. Cash and cash equivalents, which totaled $77 million as of September 30, 2026, include cash on hand and on deposit, as well as short-term securities held for the primary purpose of general liquidity. The combination of cash and availability under our ABL Facility equated to $3.2 billion in liquidity as of September 30, 2026. We believe our liquidity and access to capital markets will be adequate to fund our cash requirements for the next 12 months and for the foreseeable future.

### CLF-000076406526000115-0091

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/clf-20260930.htm), characters 111562–112483

> Our ABL Facility, which matures in June 2028, has a maximum borrowing base of $4.75 billion. The available borrowing base is determined by applying customary advance rates to eligible accounts receivable, inventory and certain mobile equipment. As of September 30, 2026, outstanding letters of credit totaled $57 million, which reduced availability under our ABL Facility. We issue standby letters of credit with certain financial institutions in order to support business obligations, including, but not limited to, workers' compensation, operating agreements, employee severance, environmental obligations and insurance. Our ABL Facility agreement contains various financial and other covenants. As of September 30, 2026, we were in compliance with the ABL Facility liquidity requirements and, therefore, the springing financial covenant requiring a minimum fixed charge coverage ratio of 1.0 to 1.0 was not applicable.

### CLF-000076406526000115-0108

mdna, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/764065/000076406526000115/clf-20260930.htm), characters 130804–131526

> Long-lived assets are reviewed for impairment upon the occurrence of events or changes in circumstances that would indicate that the carrying value of the assets may not be recoverable. Such indicators may include: a significant decline in expected future cash flows; a sustained, significant decline in market pricing; a significant adverse change in legal or environmental factors or in the business climate; changes in estimates of our recoverable reserves; and unanticipated competition. Any adverse change in these factors could have a significant impact on the recoverability of our long-lived assets and could have a material impact on our consolidated statements of operations and statements of financial position.

## Run

Run `CLF-20261118T063545Z-DeepSeek-V4-Pro-0813`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 7 calls, 26,182 input (5,376 cached) and 48,781 output tokens, $0.1545, 1225s. Verification: 35 calls, 15,889 input (4,480 cached) and 2,963 output tokens, $0.0211, 73s. Prices read 2026-11-17. Raw requests and responses: data/runs/CLF/CLF-20261118T063545Z-DeepSeek-V4-Pro-0813.jsonl.
