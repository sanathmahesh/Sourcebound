# Credit memo: KOHLS Corp (KSS)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4-Pro-0813`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-3** (provisional).
Sources: [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm); [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm); [10-Q for 2026-05-02](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/kss-20260502.htm)

Claims: 31 — 28 supported, 3 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 23; repairs: 1.

## Business profile

1. Kohl's generated revenue of **$17.5 billion** [F1] in the fiscal year ended 3 February 2024, **$16.2 billion** [F2] in the fiscal year ended 1 February 2025, **$15.5 billion** [F3] in the fiscal year ended 31 January 2026, and **$15.4 billion** [F4] in the twelve months to 1 August 2026.  
   ✅ supported (judge): All four revenue figures match the XBRL-computed metric values exactly.
2. EBITDA was **$1.3 billion** [F5] in the fiscal year ended 31 January 2026 and **$1.3 billion** [F6] in the twelve months to 1 August 2026.  
   ✅ supported (judge): Both EBITDA figures in the claim match the computed metric values exactly.
3. Kohl's operates in the highly competitive retail industry, with primary competitors including online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, and traditional department stores.  
   ✅ supported (judge): The filing states the retail industry is highly competitive and lists the exact competitor types named in the claim.
   - cites `KSS-000119312526115982-0012` ✓: “The retail industry is highly competitive.”
   - cites `KSS-000119312526115982-0012` ✓: “Our primary competitors are online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, traditional department stores, and other forms of retail commerce.”
4. The company's strategy emphasizes value, quality, and a frictionless customer experience across its omnichannel platforms.  
   ✅ supported (judge): The passage explicitly states the strategy of reestablishing leadership in value and quality and delivering a frictionless experience across omnichannel platforms.
   - cites `KSS-000119312526115982-0073` ✓: “reestablish Kohl’s as a leader in value and quality, and deliver a frictionless experience to customers across our omnichannel platforms.”
5. Many of the company's expenses, including store payroll and distribution costs, are variable in nature and generally move with sales.  
   ✅ supported (judge): The filing explicitly states that many expenses, including store payroll and distribution costs, are variable in nature and generally move with sales.
   - cites `KSS-000119312526115982-0077` ✓: “Many of our expenses, including store payroll and distribution costs, are variable in nature. These costs generally increase as sales increase, and decrease as sales decrease.”

## Financial risk

1. Debt/EBITDA was stable from the fiscal year ended 3 February 2024 through the twelve months to 1 August 2026, at **2.70x** [F7], **3.07x** [F8], **2.59x** [F9], and **2.53x** [F10], respectively.  
   ◐ partially supported (judge): The four ratio values match the computed metrics exactly, but describing the series as 'stable' is an interpretation the evidence doesn't establish — the ratio fluctuates notably (peaking at 3.07x in FY-1 before falling to 2.59x and 2.53x), a range of ~0.54x.
2. Net leverage improved from **2.57x** [F11] in the fiscal year ended 3 February 2024 and **2.95x** [F12] in the fiscal year ended 1 February 2025 to **2.08x** [F13] in the fiscal year ended 31 January 2026 and **1.89x** [F14] in the twelve months to 1 August 2026.  
   ✅ supported (judge): All four net leverage values and dates match the computed metric values exactly.
3. EBITDA/interest coverage improved from **4.26x** [F15] in the fiscal year ended 3 February 2024 and **3.69x** [F16] in the fiscal year ended 1 February 2025 to **4.60x** [F17] in the fiscal year ended 31 January 2026 and **4.96x** [F18] in the twelve months to 1 August 2026.  
   ✅ supported (judge): All four EBITDA/interest coverage figures and fiscal period labels match the computed XBRL metric values exactly.
4. FCF/debt improved from **14.9%** [F19] in the fiscal year ended 3 February 2024 and **5.0%** [F20] in the fiscal year ended 1 February 2025 to **29.4%** [F21] in the fiscal year ended 31 January 2026 and **31.7%** [F22] in the twelve months to 1 August 2026.  
   ✅ supported (judge): All four FCF/debt values in the claim match the scorecard metric values exactly.
5. The improvement in free cash flow was driven by stronger operating cash flow from higher net income and lower inventory, and by lower capital expenditures.  
   ✅ supported (judge): The passage states the free cash flow increase was driven by higher operating cash flow from higher net income and lower inventory, plus decreased capital expenditures.
   - cites `KSS-000119312526115982-0092` ✓: “The increase was primarily driven by more cash provided by operating activities due to a higher net income and inventory decreasing 7%”
   - cites `KSS-000119312526115982-0092` ✓: “capital expenditures decreased due to lower capital spend on the expansion of our E-commerce Fulfillment center in Etna, Ohio”
6. Debt reduction also contributed to the improvement in net leverage, as the company made net repayments under its revolving credit facility.  
   ✅ supported (judge): The cash flow statement shows net repayments under the revolving credit facility of $290 million, consistent with the claim of debt reduction via net revolver repayments.
   - cites `KSS-000119312526115982-0115` ✓: “Net (repayments) borrowings under revolving credit facility”

## Liquidity

1. Liquidity coverage was **5.81x** [F23] in the twelve months to 1 August 2026 and **4.80x** [F24] in the fiscal year ended 31 January 2026; in the twelve months to 1 August 2026, cash and cash equivalents were **$821 million** [F25], cash from operations was **$1.4 billion** [F26], capital expenditures were **$318 million** [F27], dividends paid were **$56 million** [F28], and short-term debt was **$0** [F29].  
   ◐ partially supported (judge): All figures match the computed metrics, but the claim states short-term debt was $0 as a fact, whereas the metric value explicitly notes this was assumed zero because it was not reported, going beyond the evidence.
2. The company maintains a $**1.5** [quoted: KSS-000119312526115982-0135] billion revolving credit facility, and as of the fiscal year ended 31 January 2026 it had $**44** [quoted: KSS-000119312526115982-0135] million of standby and trade letters of credit outstanding under the facility, which reduced available borrowing capacity.  
   ✅ supported (judge): The passage explicitly confirms the $1.5 billion revolving credit facility and $44 million of standby and trade letters of credit outstanding as of January 31, 2026, which reduced available borrowing capacity.
   - cites `KSS-000119312526115982-0135` ✓: “the $1.5 billion revolving credit facility”
   - cites `KSS-000119312526115982-0135` ✓: “we had $44 million of standby and trade letters of credit outstanding under the credit facility, which reduces the available borrowing capacity”
3. Management lists the line of credit under the revolving credit facility as a source of cash.  
   ✅ supported (judge): The passage explicitly lists 'Line of credit under our revolving credit facility' under Cash Sources.
   - cites `KSS-000119312526381893-0041` ✓: “Line of credit under our revolving credit facility”
4. The company was in compliance with all covenants of its various debt agreements as of the fiscal year ended 31 January 2026.  
   ✅ supported (judge): The filing explicitly states compliance with all debt covenants as of January 31, 2026.
   - cites `KSS-000119312526115982-0135` ✓: “we were in compliance with all covenants of the various debt agreements”

## Maturity wall

1. At the fiscal year ended 31 January 2026, debt maturing in the next twelve months was **$0** [F30], short-term debt was **$0** [F31], total debt was **$3.4 billion** [F32], and cash and cash equivalents were **$674 million** [F33].  
   ✅ supported (judge): All four claimed values match the XBRL-computed metrics for FY ended 31 January 2026.
2. The metric table provides no values for debt maturing in year two (**not available** [F34]), year three (**not available** [F35]), year four (**not available** [F36]), year five (**not available** [F37]), or after year five (**not available** [F38]).  
   ✅ supported (judge): All five debt maturity metrics (years two through five and after year five) are listed as not available in the metric table.
3. The metric table also provides no values for debt due within twenty-four months (**not available** [F39]), the share due within twenty-four months (**not available** [F40]), or near-term maturity cover (**not available** [F41]).  
   ✅ supported (judge): All three metric values (debt due within 24 months, share of debt due within 24 months, and near-term maturity cover) are reported as not available in the scorecard, matching the claim.
4. In the second quarter of **2025** [quoted: KSS-000119312526115982-0134], the company issued $**360** [quoted: KSS-000119312526115982-0134] million aggregate principal amount of **10.000** [quoted: KSS-000119312526115982-0134]% senior secured notes due **2030** [quoted: KSS-000119312526115982-0134] and received proceeds of $**357** [quoted: KSS-000119312526115982-0134] million, net of the debt discount.  
   ✅ supported (judge): The passage states exactly the issued amount, coupon, maturity, and net proceeds claimed.
   - cites `KSS-000119312526115982-0134` ✓: “issued $360 million aggregate principal amount of 10.000% senior secured notes due 2030 and received proceeds of $357 million”
5. In the second quarter of **2025** [quoted: KSS-000119312526115982-0134], $**353** [quoted: KSS-000119312526115982-0134] million in aggregate principal amount of the company's **4.25** [quoted: KSS-000119312526115982-0134]% notes matured and were repaid, and in the fourth quarter of **2025** [quoted: KSS-000119312526115982-0134] the company reduced its outstanding debt by $**87** [quoted: KSS-000119312526115982-0091] million aggregate principal through repurchases of various notes on the open market.  
   ✅ supported (judge): Both the Q2 2025 maturity/repayment of $353 million of 4.25% notes and the Q4 2025 $87 million open-market repurchase reduction are directly stated in the evidence.
   - cites `KSS-000119312526115982-0134` ✓: “$353 million in aggregate principal amount of our 4.25% notes matured and were repaid”
   - cites `KSS-000119312526115982-0091` ✓: “$87 million aggregate principal through repurchases of various notes on the open market”
6. As of August **1** [quoted: KSS-000119312526381893-0016], **2026** [quoted: KSS-000119312526381893-0016], the company was in compliance with all covenants of the various debt agreements, and during the second quarter of **2026** [quoted: KSS-000119312526381893-0016] it executed an amendment of its revolving credit agreement that extends the maturity of the revolving credit facility by five years to June **30** [quoted: KSS-000119312526381893-0016], **2031** [quoted: KSS-000119312526381893-0016].  
   ✅ supported (judge): Both the covenant compliance as of August 1, 2026 and the Q2 2026 credit agreement amendment extending maturity five years to June 30, 2031 are directly stated in the evidence.
   - cites `KSS-000119312526381893-0016` ✓: “As of August 1, 2026, we were in compliance with all covenants of the various debt agreements.”
   - cites `KSS-000119312526381893-0016` ✓: “executed an amendment of our revolving credit agreement that extends the maturity of the revolving credit facility by five years to June 30, 2031”

## Key risks

1. Further declines in credit ratings could restrict access to debt markets and increase the cost of new debt, weakening the company's ability to refinance maturing obligations.  
   ✅ supported (judge): The passage states that further downgrades would raise borrowing costs, adversely affect debt market access and terms for new issuances, and negatively impact access to capital and cost of debt financing.
   - cites `KSS-000119312526115982-0051` ✓: “Declines in our credit ratings may also adversely affect our ability to access the debt markets and the terms and our cost of funds for new debt issuances.”
2. A covenant breach under the revolving credit facility could trigger acceleration and cross-defaults, potentially requiring immediate repayment and disrupting liquidity.  
   ✅ supported (judge): The passage states that failure to comply with covenants in the revolving credit facility could result in default, acceleration (loans immediately due and payable), and cross-defaults under other indebtedness, affecting financial condition and cash flows (liquidity).
   - cites `KSS-000119312526115982-0052` ✓: “A default under our revolving credit facility could trigger a cross-default, acceleration, or other consequences under other indebtedness or financial instruments to which we are a party.”
3. The company's reliance on public debt markets and bank credit lines leaves refinancing vulnerable to market disruptions, limited liquidity, and interest rate fluctuations.  
   ✅ supported (judge): The passage directly states reliance on public debt markets and bank credit lines and that market disruptions, limited liquidity, and interest rate fluctuations may restrict access to these liquidity sources.
   - cites `KSS-000119312526115982-0050` ✓: “Changes in the credit and capital markets, including market disruptions, limited liquidity, and interest rate fluctuations may increase the cost of financing or restrict our access to these potential sources of future liquidity.”
4. A slowdown in the U.S. economy, an uncertain economic outlook, or a decline in consumer confidence could reduce consumer spending, adversely affecting operating results and cash available for debt service.  
   ◐ partially supported (judge): The evidence supports that such conditions could reduce consumer spending and adversely affect results of operations, but it does not mention any effect on cash available for debt service.
   - cites `KSS-000119312526115982-0017` ✓: “A slowdown in the U.S. economy, an uncertain economic outlook, or a decline in consumer confidence could adversely affect consumer spending habits”
5. Changes in global trade policies and tariffs could increase costs and disrupt the supply chain, with potential adverse effects on results of operations and liquidity.  
   ✅ supported (judge): The passage states changes in global trade policies and tariffs could increase costs and disrupt the supply chain, and separately that risk factors could adversely affect results of operations and liquidity, supporting the full claim.
   - cites `KSS-000119312526257402-0043` ✓: “Changes in global trade policies and the imposition of tariffs could increase our costs and disrupt our supply chain.”
   - cites `KSS-000119312526257402-0043` ✓: “These risk factors could materially and adversely affect our business, financial condition, results of operations, and liquidity.”

## Rating rationale

1. The SB grade is **SB-3** [F42], with a weighted score of **2.72** [F43]; the SB grade is a stylized internal scorecard grade, not a credit rating, and it is provisional because the near-term maturity cover factor is **not available** [F41] and the remaining weights were renormalised.  
   ✅ supported (judge): The scorecard confirms grade SB-3, weighted score 2.72, its stylized non-credit-rating nature, and provisional status due to unavailable near-term maturity cover with renormalised weights.
2. The strongest scorecard factors are liquidity sources / uses, at band **1** [F44] with weight **15.0%** [F45], and FCF / debt, at band **2** [F46] with weight **20.0%** [F47].  
   ✅ supported (judge): The metric values confirm liquidity sources / uses is band 1 with weight 15.0% and FCF / debt is band 2 with weight 20.0%, making them the two strongest factors by band (next is debt/EBITDA at band 3).
3. The weakest scorecard factor is EBITDA / interest, at band **4** [F48] with weight **25.0%** [F49]; debt / EBITDA and net debt / EBITDA are at band **3** [F50] and band **3** [F51], with weights **20.0%** [F52] and **10.0%** [F53].  
   ✅ supported (judge): All bands and weights in the claim match the scorecard metrics exactly, and EBITDA/interest at band 4 is the weakest (highest band) scored factor.
4. The earlier findings support the grade: net leverage improved to **1.89x** [F14], EBITDA/interest coverage improved to **4.96x** [F18], FCF/debt improved to **31.7%** [F22], and liquidity coverage was **5.81x** [F23].  
   ✅ supported (judge): All four cited metric values (net leverage 1.89x, EBITDA/interest 4.96x, FCF/debt 31.7%, liquidity coverage 5.81x) match exactly the computed metric values given, and the SB grade is the scorecard's result.
5. The competitive retail industry and reliance on public debt markets and bank credit lines, along with covenant and downgrade risks, temper the scorecard outcome.  
   ✅ supported (judge): Each element of the claim—competitive retail industry, reliance on public debt markets and credit lines, covenant restrictions, and downgrade risks—is directly stated in the evidence passages.
   - cites `KSS-000119312526115982-0012` ✓: “Our primary competitors are online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, traditional department stores, and other forms of retail commerce.”
   - cites `KSS-000119312526115982-0050` ✓: “We have historically relied on the public debt markets and lines of credit with financial institutions to raise capital”
   - cites `KSS-000119312526115982-0052` ✓: “Any failure to comply with these covenants could result in an event of default, allowing lenders to terminate their commitments”
   - cites `KSS-000119312526115982-0051` ✓: “Declines in our credit ratings may also adversely affect our ability to access the debt markets and the terms and our cost of funds for new debt issuances.”

## Reviewer checklist

- [ ] **not available** (warning): Debt maturing in year two not available in FY0: no candidate tag is reported (see the log).
- [ ] **not available** (warning): Debt maturing in year three not available in FY0: no candidate tag is reported (see the log).
- [ ] **not available** (warning): Debt maturing in year four not available in FY0: no candidate tag is reported (see the log).
- [ ] **not available** (warning): Debt maturing in year five not available in FY0: no candidate tag is reported (see the log).
- [ ] **not available** (warning): Debt maturing after year five not available in FY0: no candidate tag is reported (see the log).
- [ ] **fallback** (info): Revenue: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Depreciation and amortisation: used rank 2 DepreciationAndAmortization in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Interest expense: used rank 6 −InterestIncomeExpenseNet in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Capital expenditure: used rank 2 PaymentsToAcquireProductiveAssets in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper in FY-1, FY0.
- [ ] **fallback** (info): Debt maturing in the next twelve months: used rank 2 LongTermDebtCurrent in FY0.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt) assumed zero (not reported) in FY-2, LTM.
- [ ] **assumed zero** (info): Short-term investments assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): ShortTermBorrowings assumed zero (not reported) in FY-1, FY0.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): CommercialPaper assumed zero (not reported) in FY-1, FY0.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **provisional grade** (warning): SB grade (latest) is provisional: Debt due in 24 months / (cash + undrawn revolver) could not be scored; the remaining weights were renormalised.
- [ ] **provisional grade** (warning): SB grade (FY0) is provisional: Debt due in 24 months / (cash + undrawn revolver) could not be scored; the remaining weights were renormalised.
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The four ratio values match the computed metrics exactly, but describing the series as 'stable' is an interpretation the evidence doesn't establish — the ratio fluctuates notably (peaking at 3.07x in FY-1 before falling to 2.59x and 2.53x), a range of ~0.54x.): “Debt/EBITDA was stable from the fiscal year ended 3 February 2024 through the twelve months to 1 August 2026, at 2.70x, 3.07x, 2.59x, and 2.53x, respectively.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (All figures match the computed metrics, but the claim states short-term debt was $0 as a fact, whereas the metric value explicitly notes this was assumed zero because it was not reported, going beyond the evidence.): “Liquidity coverage was 5.81x in the twelve months to 1 August 2026 and 4.80x in the fiscal year ended 31 January 2026; in the twelve months to 1 August 2026, cash and cash equivalents were $821 million, cash from operations was $1.4 billion, capital expenditures were $318 million, dividends paid were $56 million, and short-term debt was $0.”
- [ ] **partially supported claim** (warning): Key risks: partially supported (The evidence supports that such conditions could reduce consumer spending and adversely affect results of operations, but it does not mention any effect on cash available for debt service.): “A slowdown in the U.S. economy, an uncertain economic outlook, or a decline in consumer confidence could reduce consumer spending, adversely affecting operating results and cash available for debt service.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $17.5 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 17,476,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F2 | Revenue (revenue:FY-1) | $16.2 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 16,221,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F3 | Revenue (revenue:FY0) | $15.5 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 15,527,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F4 | Revenue (revenue:LTM) | $15.4 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 15,527,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 6,682,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 6,779,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F5 | EBITDA (ebitda:FY0) | $1.3 billion | operating_income + d_and_a | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F6 | EBITDA (ebitda:LTM) | $1.3 billion | operating_income + d_and_a | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 347,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 350,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY-2) | 2.70x | total_debt / EBITDA | LongTermDebtNoncurrent 1,638,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityCurrent 74,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,242,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>OperatingIncomeLoss 717,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 749,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:FY-1) | 3.07x | total_debt / EBITDA | LongTermDebtNoncurrent 1,174,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 353,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityCurrent 72,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,008,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 433,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 743,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F9 | Debt / EBITDA (debt_to_ebitda:FY0) | 2.59x | total_debt / EBITDA | LongTermDebtNoncurrent 1,436,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>FinanceLeaseLiabilityCurrent 76,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,919,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F10 | Debt / EBITDA (debt_to_ebitda:LTM) | 2.53x | total_debt / EBITDA | LongTermDebtNoncurrent 1,325,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityCurrent 82,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,853,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 347,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F11 | Net leverage (net_leverage:FY-2) | 2.57x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 1,638,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityCurrent 74,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,242,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 183,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>OperatingIncomeLoss 717,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 749,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F12 | Net leverage (net_leverage:FY-1) | 2.95x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 1,174,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 353,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityCurrent 72,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,008,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 134,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 433,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 743,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F13 | Net leverage (net_leverage:FY0) | 2.08x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 1,436,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>FinanceLeaseLiabilityCurrent 76,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,919,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 674,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F14 | Net leverage (net_leverage:LTM) | 1.89x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 1,325,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityCurrent 82,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,853,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 821,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F15 | EBITDA / interest (interest_coverage:FY-2) | 4.26x | EBITDA / interest_expense | OperatingIncomeLoss 717,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 749,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>InterestIncomeExpenseNet -344,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F16 | EBITDA / interest (interest_coverage:FY-1) | 3.69x | EBITDA / interest_expense | OperatingIncomeLoss 433,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 743,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>InterestIncomeExpenseNet -319,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F17 | EBITDA / interest (interest_coverage:FY0) | 4.60x | EBITDA / interest_expense | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>InterestIncomeExpenseNet -288,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F18 | EBITDA / interest (interest_coverage:LTM) | 4.96x | EBITDA / interest_expense | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 347,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 350,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>InterestIncomeExpenseNet -288,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>InterestIncomeExpenseNet -126,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F19 | FCF / debt (fcf_to_debt:FY-2) | 14.9% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 1,168,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 577,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtNoncurrent 1,638,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityCurrent 74,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,242,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm) |
| F20 | FCF / debt (fcf_to_debt:FY-1) | 5.0% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 648,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 466,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtNoncurrent 1,174,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 353,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityCurrent 72,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,008,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F21 | FCF / debt (fcf_to_debt:FY0) | 29.4% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtNoncurrent 1,436,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>FinanceLeaseLiabilityCurrent 76,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,919,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F22 | FCF / debt (fcf_to_debt:LTM) | 31.7% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 478,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 506,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 146,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 200,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtNoncurrent 1,325,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityCurrent 82,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F23 | Liquidity coverage (liquidity_coverage:LTM) | 5.81x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 821,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 478,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 506,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 146,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 200,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsOfDividends 56,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F24 | Liquidity coverage (liquidity_coverage:FY0) | 4.80x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 674,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsOfDividends 56,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F25 | Cash and cash equivalents (cash:LTM) | $821 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 821,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F26 | Cash from operations (cfo:LTM) | $1.4 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 478,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 506,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F27 | Capital expenditure (capex:LTM) | $318 million | rank 2: PaymentsToAcquireProductiveAssets | PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 146,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 200,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F28 | Dividends paid (dividends:LTM) | $56 million | rank 1: PaymentsOfDividends | PaymentsOfDividends 56,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsOfDividends 28,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsOfDividends 28,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F29 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $0 |  | — |
| F30 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $0 | rank 2: LongTermDebtCurrent | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm) |
| F31 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $0 | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm) |
| F32 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $3.4 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 1,436,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>FinanceLeaseLiabilityCurrent 76,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,919,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F33 | Cash and cash equivalents (cash:FY0) | $674 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 674,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F34 | Debt maturing in year two (maturity_year_2:FY0) | not available |  | — |
| F35 | Debt maturing in year three (maturity_year_3:FY0) | not available |  | — |
| F36 | Debt maturing in year four (maturity_year_4:FY0) | not available |  | — |
| F37 | Debt maturing in year five (maturity_year_5:FY0) | not available |  | — |
| F38 | Debt maturing after year five (maturity_after_year_5:FY0) | not available |  | — |
| F39 | Debt due within 24 months (debt_due_24m:FY0) | not available | short_term_debt + maturity_year_2 | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm) |
| F40 | Share of debt due within 24 months (share_due_24m:FY0) | not available | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>LongTermDebtNoncurrent 1,436,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>FinanceLeaseLiabilityCurrent 76,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,919,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F41 | Near-term maturity cover (near_term_maturity_cover:FY0) | not available | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 674,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F42 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 2.72222 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F43 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 2.72222 | sum of weight x band over the factors scored, divided by their weights | — |
| F44 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 1 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F45 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F46 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 2 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F47 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F48 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 4 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F49 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F50 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 3 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F51 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 3 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F52 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F53 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### KSS-000119312526115982-0012

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 14108–15166

> We are committed to the highest integrity standards and maintain a Code of Ethics to guide ethical decision-making for associates. As a company of integrity, we expect our associates to be honest and accountable. Our ethics training, which we require all associates to take annually, is refreshed yearly to ensure topics covered are relevant and impactful. The training helps connect ethics to an associate's day-to-day job responsibilities and promotes honesty, integrity, and fairness.
> Competition
> The retail industry is highly competitive. Management considers product and value to be the most significant competitive factors in the industry. Merchandise mix, brands, service, loyalty programs, credit availability, and customer experience are also key competitive factors. Our primary competitors are online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, traditional department stores, and other forms of retail commerce. Our specific competitors vary from market to market.
> 5
> Table of Contents
> Merchandise Vendors

### KSS-000119312526115982-0017

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 20321–21729

> Our business is sensitive to the growth of the U.S. economy and the strength of the U.S. consumer. Consumer spending habits, including demand for the merchandise we sell, are affected by various factors beyond our control, including prevailing economic conditions, inflation and measures taken to control it, consumer responses to recessionary concerns, levels of employment, salaries and wage rates, prevailing interest rates, housing costs, energy and fuel costs, income tax rates and policies, consumer perception of economic conditions, and the consumer’s disposable income, credit availability, and debt levels. Our core moderate-income customer is especially sensitive to these factors. When the cost of basic necessities, such as food, fuel, and healthcare, increases, these customers often reduce their discretionary spending, which may negatively impact our results of operations. A slowdown in the U.S. economy, an uncertain economic outlook, or a decline in consumer confidence could adversely affect consumer spending habits and result in lower traffic to our physical stores and digital platforms, increased markdowns, reduced sale conversion rates, and an adverse effect on our results of operations. Because all of our physical stores are located in the United States, we are especially susceptible to deteriorations in the U.S. economy compared to more geographically diversified competitors.

### KSS-000119312526115982-0050

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 60902–61828

> We may be unable to raise additional capital or maintain credit on favorable terms, which could constrain our operational flexibility and increase our cost of doing business.
> We have historically relied on the public debt markets and lines of credit with financial institutions to raise capital and to partially fund our operations, growth, seasonal working capital needs, and strategic initiatives. In January 2023, we upsized and replaced our unsecured credit facility with a $1.5 billion senior secured, asset based revolving credit facility. Changes in the credit and capital markets, including market disruptions, limited liquidity, and interest rate fluctuations may increase the cost of financing or restrict our access to these potential sources of future liquidity. Our continued access to these liquidity sources on favorable terms depends on multiple factors, including our operating performance and credit ratings.

### KSS-000119312526115982-0051

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 61829–63109

> During 2024, S&P downgraded our senior unsecured credit rating from BB to BB- and Moody's downgraded our rating from Ba3 to B1. These downgrades have caused our cost of borrowing to increase. During 2025, Moody's further downgraded our senior unsecured credit rating from B1 to B3; however, further downgrades by Moody's do not trigger incremental interest rate increases on our existing debt. Further downgrades by S&P would cause our cost of borrowing to further increase. Declines in our credit ratings may also adversely affect our ability to access the debt markets and the terms and our cost of funds for new debt issuances. In addition, multiple further downgrades in our corporate credit rating could trigger less favorable terms under certain commercial arrangements, which could negatively impact our profitability and increase our costs. If our credit ratings were to be further downgraded, or general market conditions were to ascribe higher risk to our credit rating levels, our industry, or our Company, our access to capital and the cost of debt financing may be negatively impacted. Additionally, if unfavorable capital market conditions exist if and when we were to seek additional financing, we may not be able to raise sufficient capital on
> 16
> Table of Contents

### KSS-000119312526115982-0052

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 63110–64209

> favorable terms and on a timely basis (if at all). The terms of current and future debt agreements could restrict our business operations or cause future financing to be unavailable due to our covenant restrictions then in effect.
> Our existing debt agreements, particularly our revolving credit facility, contain restrictive covenants. Any failure to comply with these covenants could result in an event of default, allowing lenders to terminate their commitments thereunder and declare the outstanding loans thereunder to be immediately due and payable. A default under our revolving credit facility could trigger a cross-default, acceleration, or other consequences under other indebtedness or financial instruments to which we are a party. If our access to capital were to become significantly constrained or our cost of capital were to increase significantly, our financial condition, results of operations, and cash flows could be adversely affected.
> Our capital allocation strategy may be inefficient, may not yield the anticipated returns, or may not effectively support our long-term growth.

### KSS-000119312526115982-0073

mdna, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 84175–85615

> Kohl's remains committed to driving long-term shareholder value by providing our customers with great product, great value, and a great experience. To achieve this, we will offer a curated, more balanced assortment that fulfills needs across all customers, reestablish Kohl’s as a leader in value and quality, and deliver a frictionless experience to customers across our omnichannel platforms.
> 25
> Table of Contents
> Financial and Capital Outlook
> For fiscal year 2026, the Company currently expects the following:
> •
> Net sales and Comparable sales: A decrease of (2%) to flat
> •
> Adjusted operating margin: In the range of 2.8% to 3.4% (b)
> •
> Adjusted diluted EPS: In the range of $1.00 to $1.60 (b)
> •
> Capital Expenditures: Approximately $350 million to $400 million
> •
> Dividend: On February 25, 2026, Kohl’s Board of Directors declared a quarterly cash dividend on the Company’s common stock of $0.125 per share. The dividend is payable April 1, 2026 to shareholders of record at the close of business on March 18, 2026.
> (b)
> Non-GAAP financial measures. The Company provides adjusted operating margin and adjusted diluted earnings per share on a non-GAAP basis and does not provide a reconciliation of the Company’s forward looking guidance to the most directly comparable GAAP financial measures because of the inherent difficulty in forecasting and quantifying certain amounts that are necessary for such reconciliations.
> Results of Operations

### KSS-000119312526115982-0077

mdna, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 89661–91104

> SG&A includes compensation and benefit costs (including stores, corporate, buying, and distribution centers); occupancy and operating costs of our retail, distribution, and corporate facilities; freight expenses associated with moving merchandise from our distribution centers to our retail stores and among distribution and retail facilities other than expenses to fulfill digital sales; marketing expenses, offset by vendor payments for reimbursement of specific, incremental, and identifiable costs; expenses related to our credit card operations; and other administrative revenues and expenses. We do not include depreciation and amortization in SG&A. The classification of these expenses varies across the retail industry.
> Many of our expenses, including store payroll and distribution costs, are variable in nature. These costs generally increase as sales increase, and decrease as sales decrease. We measure our expenses as a percentage of revenue and changes in this percentage compared to the prior year. If the expense as a percent of revenue decreased from the prior year, the expense "leveraged". If the expense as a percent of revenue increased over the prior year, the expense "deleveraged".
> The following graph summarizes the changes in SG&A by expense type between 2024 and 2025:
> 28
> Table of Contents
> SG&A decreased $219 million, or 4.1%, to $5.1 billion in 2025. As a percentage of revenue, SG&A deleveraged by 5 basis points.

### KSS-000119312526115982-0091

liquidity, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 105584–106757

> In the second quarter of 2025, we issued $360 million aggregate principal amount of 10.000% senior secured notes due 2030 and received proceeds of $357 million, net of the debt discount. Also, during the second quarter of 2025, $353 million in aggregate principal amount of our 4.25% notes matured and were repaid.
> In the fourth quarter of 2025, we reduced our outstanding debt by $87 million aggregate principal through repurchases of various notes on the open market.
> In the second quarter of 2024, we completed a voluntary redemption of the remaining $113 million of outstanding 9.50% notes due May 15, 2025.
> Cash dividend payments were $56 million ($0.50 per share) in 2025 and $222 million ($2.00 per share) in 2024.
> 33
> Table of Contents
> There was no cash used for treasury stock purchases in 2025 or 2024. Share repurchases are discretionary in nature. The timing and amount of repurchases are based upon available cash balances, our stock price, and other factors. While we are not currently planning for share repurchases, we expect to resume share repurchases over the long-term following improvement in overall leverage.
> Adjusted Free Cash Flow (Non-GAAP measure)

### KSS-000119312526115982-0092

liquidity, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 106758–108198

> We generated $935 million of adjusted free cash flow for 2025 compared to $104 million in 2024. The increase was primarily driven by more cash provided by operating activities due to a higher net income and inventory decreasing 7% to last year compared to an increase of 2% in 2024. Additionally, capital expenditures decreased due to lower capital spend on the expansion of our E-commerce Fulfillment center in Etna, Ohio, which was completed in 2025 and fewer Sephora shop openings and other investments.
> In addition to net cash provided by operating activities, we provide Adjusted Free Cash Flow as a useful measure of our financial performance and position and our ability to generate additional cash flow from our business operations. We believe the presentation of Adjusted Free Cash Flow is relevant and useful for investors to evaluate the cash generated from operations consistent with the method used by management. Adjusted free cash flow is a non-GAAP financial measure which we define as net cash provided by operating activities and proceeds from financing obligations (which generally represent landlord reimbursements of construction costs) less capital expenditures and finance lease and financing obligation payments. Adjusted free cash flow is provided and should be evaluated in addition to, and not as an alternative to our other financial GAAP measures such as net cash provided by operating activities or net income.

### KSS-000119312526115982-0115

financial_statements, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 135063–136512

> (562)
> Financing activities
> Proceeds from issuance of debt, net of discount
> 357
> —
> —
> Deferred financing costs
> (11)
> —
> —
> Net (repayments) borrowings under revolving credit facility
> (290)
> 198
> 7
> Shares withheld for taxes on vested restricted shares
> (5)
> (10)
> (16)
> Dividends paid
> (56)
> (222)
> (220)
> Repayment of long-term borrowings
> (440)
> (113)
> (275)
> Discount (premium paid) on redemption of debt
> 11
> (5)
> —
> Finance lease and financing obligation payments
> (83)
> (79)
> (93)
> Proceeds from financing obligations
> 10
> 1
> 21
> Net cash used in financing activities
> (507)
> (230)
> (576)
> Net increase (decrease) in cash and cash equivalents
> 540
> (49)
> 30
> Cash and cash equivalents at beginning of period
> 134
> 183
> 153
> Cash and cash equivalents at end of period
> $674
> $134
> $183
> Supplemental information
> Interest paid, net of capitalized interest
> $295
> $312
> $331
> See accompanying Notes to Consolidated Financial Statements
> 45
> Table of Contents
> 1. Business and Summary of Accounting Policies
> Business
> As of January 31, 2026, we operated 1,153 stores and a website (www.Kohls.com). Our Kohl's stores and website sell moderately-priced proprietary and national brand apparel, footwear, accessories, beauty, and home products. Our Kohl's stores generally carry a consistent merchandise assortment with some differences attributable to local preferences and store size. Our website includes merchandise which is available in our stores, as well as merchandise which is available only online.

### KSS-000119312526115982-0134

debt_note, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 159292–160575

> In the fourth quarter of 2024, S&P downgraded our senior unsecured credit rating from BB to BB- and Moody’s downgraded our rating from Ba3 to B1. As a result of the downgrades, the interest rate on our 3.375% notes due May 2031 increased an additional 50 basis points in the second quarter of 2025 due to the coupon adjustment provision within the notes. During the second quarter of 2025, Moody's downgraded our senior unsecured credit rating from B1 to B3; however, further downgrades by Moody's do not trigger incremental interest rate increases. In total, the interest rate on the notes due May 2031 have increased 175 basis points since their issuance due to the coupon adjustment provision within the notes.
> In the second quarter of 2025, we issued $360 million aggregate principal amount of 10.000% senior secured notes due 2030 and received proceeds of $357 million, net of the debt discount. The notes are guaranteed by certain of our subsidiaries. Certain of these guarantees are secured by eleven distribution centers and E-commerce Fulfillment Centers, which are held by our subsidiaries, as well as the equity interests in one of our subsidiaries.
> Also in the second quarter of 2025, $353 million in aggregate principal amount of our 4.25% notes matured and were repaid.

### KSS-000119312526115982-0135

debt_note, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 160576–161937

> In the fourth quarter of 2025, we reduced our outstanding debt by $87 million through repurchases of our notes on the open market, resulting in a gain on extinguishment of debt of $11 million recognized in net interest expense.
> In the second quarter of 2024, we completed a voluntary redemption of the remaining $113 million of outstanding 9.50% notes due May 15, 2025. We recognized a $5 million loss on extinguishment of debt in net interest expense which is primarily a make whole premium paid to holders as a result of the redemption.
> Borrowings under the $1.5 billion revolving credit facility, recorded as short-term debt, were $0 as of January 31, 2026, and $290 million as of February 1, 2025. Outstanding borrowings under the credit facility bear interest at a variable rate based on SOFR plus the applicable margin. As of January 31, 2026, we had $44 million of standby and trade letters of credit outstanding under the credit facility, which reduces the available borrowing capacity.
> Our various debt agreements contain covenants including limitations on additional indebtedness and certain financial tests. As of January 31, 2026, we were in compliance with all covenants of the various debt agreements.
> We also had outstanding standby and trade letters of credit outside of the credit facility totaling approximately $5 million at January 31, 2026.

### KSS-000119312526257402-0043

risk_factors, [10-Q for 2026-05-02](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/kss-20260502.htm), characters 51118–51932

> Item 1A. Risk Factors
> In addition to the other information set forth in this Quarterly Report on Form 10-Q, careful consideration should be taken of the risk factors discussed in Part I, Item 1A, “Risk Factors,” in our Annual Report on Form 10-K for the fiscal year ended January 31, 2026. These risk factors could materially and adversely affect our business, financial condition, results of operations, and liquidity. Additional risks and uncertainties not currently known to us or that we currently deem immaterial may also have a material adverse effect on our business operations.
> There have been no significant changes in the Risk Factors described in our 2025 Form 10-K, except as follows:
> Changes in global trade policies and the imposition of tariffs could increase our costs and disrupt our supply chain.

### KSS-000119312526381893-0016

debt_note, [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/kss-20260801.htm), characters 18581–19752

> In the second quarter of 2025, we issued $360 million aggregate principal amount of 10.000% senior secured notes due 2030 and received proceeds of $357 million, net of the debt discount. The notes are guaranteed by certain of our subsidiaries. Certain of these guarantees are secured by eleven distribution centers and E-commerce Fulfillment Centers, which are held by our subsidiaries, as well as the equity interests in one of our subsidiaries.
> Also in the second quarter of 2025, $353 million in aggregate principal amount of our 4.25% notes matured and were repaid.
> Borrowings under the $1.5 billion revolving credit facility, recorded as short-term debt, were $0 as of August 1, 2026 and January 31, 2026 and $75 million as of August 2, 2025.
> During the second quarter of 2026, we executed an amendment of our revolving credit agreement that extends the maturity of the revolving credit facility by five years to June 30, 2031.
> 9
> Table of Contents
> Our various debt agreements contain covenants including limitations on additional indebtedness and certain financial tests. As of August 1, 2026, we were in compliance with all covenants of the various debt agreements.

### KSS-000119312526381893-0041

liquidity, [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/kss-20260801.htm), characters 49032–50267

> Our period-end cash and cash equivalents balance increased to $821 million from $174 million in the second quarter of 2025. Our Cash and cash equivalents balance includes short-term investments of $682 million and $17 million as of August 1, 2026, and August 2, 2025, respectively. Our investment policy is designed to preserve principal and liquidity of our short-term investments. This policy allows investments in large money market funds or in highly rated direct short-term instruments. We also place dollar limits on our investments in individual funds or instruments.
> 20
> Table of Contents
> The following table presents our primary uses and sources of cash:
> Cash Uses
> Cash Sources
> •
> Operational needs, including compensation and benefit costs, rent, taxes, and other operating costs
> •
> Inventory
> •
> Capital expenditures
> •
> Dividend payments
> •
> Debt repayments and repurchases
> •
> Share repurchases
> •
> Cash flow from operations
> •
> Line of credit under our revolving credit facility
> •
> Issuance of debt
> Six Months Ended
> (Dollars in Millions)
> August 1, 2026
> August 2, 2025
> Change
> Net cash provided by (used in):
> Operating activities
> $478
> $506
> $(28)
> Investing activities
> (153)
> (179)
> 26
> Financing activities
> (178)
> (287)
> 109
> Operating Activities

## Run

Run `KSS-20261118T062650Z-DeepSeek-V4-Pro-0813`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 7 calls, 27,279 input (5,632 cached) and 49,987 output tokens, $0.1586, 1333s. Verification: 31 calls, 15,421 input (4,355 cached) and 2,626 output tokens, $0.0197, 73s. Prices read 2026-11-17. Raw requests and responses: data/runs/KSS/KSS-20261118T062650Z-DeepSeek-V4-Pro-0813.jsonl.
