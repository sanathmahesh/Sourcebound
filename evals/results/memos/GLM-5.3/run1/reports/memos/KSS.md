# Credit memo: KOHLS Corp (KSS)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `zai-org/GLM-5.3`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-3** (provisional).
Sources: [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm); [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm); [10-Q for 2026-05-02](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/kss-20260502.htm)

Claims: 35 — 32 supported, 3 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 0; repairs: 1.

## Business profile

1. Kohl's operates an omnichannel retail business, offering a curated assortment of merchandise to customers across its stores and digital platforms.  
   ✅ supported (judge): The passage states Kohl's offers a curated assortment and serves customers across its omnichannel platforms.
   - cites `KSS-000119312526115982-0073` ✓: “we will offer a curated, more balanced assortment that fulfills needs across all customers”
   - cites `KSS-000119312526115982-0073` ✓: “deliver a frictionless experience to customers across our omnichannel platforms”
2. Revenue has declined over the past several years, from **$17.5 billion** [F1] in the fiscal year ended 3 February 2024 to **$16.2 billion** [F2] in the fiscal year ended 1 February 2025 and **$15.5 billion** [F3] in the fiscal year ended 31 January 2026, standing at **$15.4 billion** [F4] for the twelve months to 1 August 2026.  
   ✅ supported (judge): All four revenue figures and their fiscal period labels match the XBRL-computed metric values exactly, showing a consistent decline.
3. The company generates EBITDA of **$1.3 billion** [F5] for the fiscal year ended 31 January 2026 and **$1.3 billion** [F6] for the twelve months to 1 August 2026, on operating income of **$624 million** [F7] and **$592 million** [F8] respectively.  
   ✅ supported (judge): All four figures (EBITDA $1.3B for FY and LTM; operating income $624M and $592M) match the computed metric values exactly.
4. Kohl's operates in a highly competitive retail industry, with competitors including online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, and traditional department stores, which limits pricing power and pressures cash flow stability.  
   ✅ supported (judge): The passage confirms a highly competitive retail industry with exactly the listed competitor types; the pricing power/cash flow clause is a reasonable general characterization consistent with the stated intense competition.
   - cites `KSS-000119312526115982-0012` ✓: “The retail industry is highly competitive. Management considers product and value to be the most significant competitive factors”
   - cites `KSS-000119312526115982-0012` ✓: “Our primary competitors are online retailers, off-price retailers, warehouse clubs, mass merchandisers, specialty stores, traditional department stores”
5. Many of the company's expenses, including store payroll and distribution costs, are variable in nature, rising and falling with sales, which provides some downside protection for margins when revenue declines.  
   ✅ supported (judge): The filing explicitly states many expenses including store payroll and distribution costs are variable, increasing and decreasing with sales, which directly implies reduced margin pressure when revenue declines.
   - cites `KSS-000119312526115982-0077` ✓: “Many of our expenses, including store payroll and distribution costs, are variable in nature. These costs generally increase as sales increase, and decrease as sales decrease.”
   - cites `KSS-000119312526381893-0032` ✓: “Many of our expenses, including store payroll and distribution costs, are variable in nature.”
6. The digital channel is a growing part of the business, with the company reporting a digital sales increase of **4** [quoted: KSS-000119312526257402-0027]% year over year, although digital growth carried elevated shipping costs.  
   ✅ supported (judge): The passage states digital sales increased 4% year over year and that this drove elevated shipping costs.
   - cites `KSS-000119312526257402-0027` ✓: “partially offset by elevated shipping costs driven by our digital sales increase of 4% year over year”

## Financial risk

1. Debt / EBITDA was stable over the review window, at **2.70x** [F9] in the fiscal year ended 3 February 2024 and **2.53x** [F10] in the twelve months to 1 August 2026, after peaking at **3.07x** [F11] in the fiscal year ended 1 February 2025.  
   ✅ supported (judge): All three stated Debt/EBITDA values (2.70x FY ended 3 Feb 2024, 3.07x FY ended 1 Feb 2025 peak, 2.53x LTM to 1 Aug 2026) match the scorecard metrics exactly, and the modest range is consistent with describing the ratio as stable.
2. Net leverage improved from **2.95x** [F12] in the fiscal year ended 1 February 2025 to **1.89x** [F13] in the twelve months to 1 August 2026, aided by ongoing repayment of long-term borrowings and a build in cash and cash equivalents during the twelve months to 1 August 2026.  
   ✅ supported (judge): The metric values confirm net leverage fell from 2.95x to 1.89x, and the cash flow statement shows repayment of long-term borrowings of 113 and a net increase in cash and cash equivalents (from $674 to $821) during the recent period.
   - cites `KSS-000119312526381893-0006` ✓: “Repayment of long-term borrowings (113) (353)”
   - cites `KSS-000119312526381893-0006` ✓: “Net increase in cash and cash equivalents 147”
3. The deterioration in leverage in the fiscal year ended 1 February 2025 reflected new borrowing, as the company issued debt with net proceeds of $**357** [quoted: KSS-000119312526115982-0115] million and drew on the revolving credit facility, before repaying $**440** [quoted: KSS-000119312526115982-0115] million of long-term borrowings in the fiscal year ended 31 January 2026.  
   ◐ partially supported (judge): The $357 million debt issuance, revolver activity, and $440 million repayment all occurred in the fiscal year ended January 31, 2026 (the first column), not the fiscal year ended 1 February 2025 as claimed; also the revolver was net repaid $290 million in FY2026, while the $198 million draw occurred in FY2025.
   - cites `KSS-000119312526115982-0115` ✓: “Proceeds from issuance of debt, net of discount 357”
   - cites `KSS-000119312526115982-0115` ✓: “Repayment of long-term borrowings (440) (113) (275)”
4. EBITDA / interest improved from **4.26x** [F14] in the fiscal year ended 3 February 2024 to **4.96x** [F15] in the twelve months to 1 August 2026, supported by an earnings recovery, with operating income rising to $**624** [quoted: KSS-000119312526115982-0071] million in the fiscal year ended 31 January 2026 from $**433** [quoted: KSS-000119312526115982-0071] million the prior year on higher gross margin and lower SG&A.  
   ✅ supported (judge): The EBITDA/interest improvement (4.26x to 4.96x) matches the computed metric values, and the operating income figures and gross margin/SG&A drivers are stated in the filing.
   - cites `KSS-000119312526115982-0071` ✓: “Operating income was $624 million compared to $433 million in the prior year.”
   - cites `KSS-000119312526115982-0071` ✓: “Selling, general & administration ("SG&A") expenses decreased 4.1% year-over-year, to $5.1 billion.”
5. FCF / debt improved markedly from **5.0%** [F16] in the fiscal year ended 1 February 2025 to **31.7%** [F17] in the twelve months to 1 August 2026, driven by stronger operating cash flow from higher net income and a **7** [quoted: KSS-000119312526115982-0092]% inventory reduction, together with lower capital expenditures.  
   ✅ supported (judge): The 5.0% and 31.7% FCF/debt values match the scorecard metrics, and the passage directly attributes the improvement to higher net income, a 7% inventory decrease, and lower capital expenditures.
   - cites `KSS-000119312526115982-0092` ✓: “We generated $935 million of adjusted free cash flow for 2025 compared to $104 million in 2024.”
   - cites `KSS-000119312526115982-0092` ✓: “capital expenditures decreased due to lower capital spend on the expansion of our E-commerce Fulfillment center in Etna, Ohio, which was completed in 2025”
6. The improving free cash flow trend has continued into the twelve months to 1 August 2026, as capital expenditures fell further under the company's reduced fiscal **2026** [quoted: KSS-000119312526381893-0042] spend plans, which anticipate capital expenditures of approximately $**350** [quoted: KSS-000119312526381893-0042] to $**400** [quoted: KSS-000119312526381893-0042] million.  
   ◐ partially supported (judge): The $350–$400 million fiscal 2026 capex plan and reduced capex are supported, but the claimed improving free cash flow trend is contradicted: operating cash flow fell from $506 million to $478 million in the first half.
   - cites `KSS-000119312526381893-0042` ✓: “The decrease in cash used in investing activities was primarily driven by our reduced capital expenditure plans for fiscal 2026.”
   - cites `KSS-000119312526381893-0042` ✓: “In 2026, we anticipate capital expenditures of approximately $350 to $400 million as we continue to invest in our business, including enhancing omnichannel capabilities.”

## Liquidity

1. Liquidity coverage stood at **5.81x** [F18] as of the twelve months to 1 August 2026, an increase from **4.80x** [F19] in the fiscal year ended 31 January 2026, indicating that liquidity sources are well in excess of the next twelve months' needs.  
   ✅ supported (judge): The metric values confirm liquidity coverage of 5.81x for the twelve months to 1 August 2026, up from 4.80x for FY ended 31 January 2026, and a coverage ratio well above 1x directly indicates liquidity sources exceeding the next twelve months' needs.
2. As of the twelve months to 1 August 2026, the company held **$821 million** [F20] in cash and cash equivalents and reported **$0** [F21] of short-term debt outstanding.  
   ✅ supported (judge): Both figures match the computed XBRL metric values: cash and cash equivalents of $821 million and short-term debt of $0 (not reported, assumed zero) for the twelve months to 1 August 2026.
3. Over the twelve months to 1 August 2026, the company generated **$1.4 billion** [F22] in cash from operations, which comfortably exceeded capital expenditures of **$318 million** [F23] and dividends paid of **$56 million** [F24].  
   ✅ supported (judge): All three figures match the XBRL-computed LTM metrics, and $1.4B in operating cash flow clearly exceeds the combined $374M of capex and dividends.
4. As of the fiscal year ended 31 January 2026, borrowings under the $**1.5** [quoted: KSS-000119312526115982-0135] billion revolving credit facility were $**0** [quoted: KSS-000119312526115982-0135], and the company had $**44** [quoted: KSS-000119312526115982-0135] million of standby and trade letters of credit outstanding under the credit facility, which reduces the available borrowing capacity.  
   ✅ supported (judge): The passage states borrowings under the $1.5 billion revolving credit facility were $0 as of January 31, 2026, and $44 million of standby and trade letters of credit were outstanding under the credit facility, reducing available borrowing capacity.
   - cites `KSS-000119312526115982-0135` ✓: “Borrowings under the $1.5 billion revolving credit facility, recorded as short-term debt, were $0 as of January 31, 2026”
   - cites `KSS-000119312526115982-0135` ✓: “we had $44 million of standby and trade letters of credit outstanding under the credit facility, which reduces the available borrowing capacity”
5. The company was in compliance with all covenants of its various debt agreements as of the fiscal year ended 31 January 2026.  
   ✅ supported (judge): The passage directly states the company was in compliance with all covenants of its various debt agreements as of January 31, 2026.
   - cites `KSS-000119312526115982-0135` ✓: “As of January 31, 2026, we were in compliance with all covenants of the various debt agreements.”
6. Management anticipates capital expenditures of approximately $**350** [quoted: KSS-000119312526381893-0042] to $**400** [quoted: KSS-000119312526381893-0042] million as it continues to invest in the business, including enhancing omnichannel capabilities.  
   ✅ supported (judge): The passage states exactly that the company anticipates capital expenditures of approximately $350 to $400 million as it continues to invest in the business, including enhancing omnichannel capabilities.
   - cites `KSS-000119312526381893-0042` ✓: “In 2026, we anticipate capital expenditures of approximately $350 to $400 million as we continue to invest in our business”

## Maturity wall

1. As of the fiscal year ended 31 January 2026, debt maturing in the next twelve months was **$0** [F25], short-term debt was **$0** [F26], and total debt was **$3.4 billion** [F27], indicating no debt is due within the next twelve months.  
   ✅ supported (judge): All three claim components match the XBRL-computed metric values exactly.
2. During the second quarter of the twelve months to 1 August 2026, the company amended its revolving credit agreement to extend the maturity of the revolving credit facility by five years to June **30** [quoted: KSS-000119312526381893-0016], **2031** [quoted: KSS-000119312526381893-0016].  
   ✅ supported (judge): The evidence explicitly states the amendment occurred in Q2 2026 extending the revolver maturity by five years to June 30, 2031.
   - cites `KSS-000119312526381893-0016` ✓: “we executed an amendment of our revolving credit agreement that extends the maturity of the revolving credit facility by five years to June 30, 2031”
3. Borrowings under the $**1.5** [quoted: KSS-000119312526381893-0016] billion revolving credit facility were $**0** [quoted: KSS-000119312526381893-0016] at the end of the fiscal year ended 31 January 2026 and at the twelve months to 1 August 2026, leaving the facility available as a liquidity backstop.  
   ✅ supported (judge): The passage explicitly states $0 borrowings under the $1.5 billion revolver as of both August 1, 2026 and January 31, 2026, implying full availability.
   - cites `KSS-000119312526381893-0016` ✓: “Borrowings under the $1.5 billion revolving credit facility, recorded as short-term debt, were $0 as of August 1, 2026 and January 31, 2026”
4. During fiscal **2025** [quoted: KSS-000119312526115982-0091] the company issued $**360** [quoted: KSS-000119312526115982-0091] million aggregate principal amount of **10.000** [quoted: KSS-000119312526115982-0091]% senior secured notes due **2030** [quoted: KSS-000119312526115982-0091], repaid $**353** [quoted: KSS-000119312526115982-0091] million of **4.25** [quoted: KSS-000119312526115982-0091]% notes that matured, and reduced outstanding debt by $**87** [quoted: KSS-000119312526115982-0091] million through open-market note repurchases.  
   ✅ supported (judge): All three claim components are directly stated in the evidence: $360M 10.000% senior secured notes due 2030 issued in Q2 2025, $353M of 4.25% notes matured and repaid, and $87M debt reduction via open-market note repurchases in Q4 2025.
   - cites `KSS-000119312526115982-0091` ✓: “In the second quarter of 2025, we issued $360 million aggregate principal amount of 10.000% senior secured notes due 2030”
   - cites `KSS-000119312526115982-0091` ✓: “In the fourth quarter of 2025, we reduced our outstanding debt by $87 million aggregate principal through repurchases of various notes on the open market”
5. The debt agreements contain covenants including limitations on additional indebtedness and certain financial tests, and the company was in compliance with all covenants as of the end of the fiscal year ended 31 January 2026 and the twelve months to 1 August 2026.  
   ✅ supported (judge): The first passage states covenants include limitations on additional indebtedness and certain financial tests with compliance as of August 1, 2026, and the second states compliance as of January 31, 2026.
   - cites `KSS-000119312526381893-0016` ✓: “Our various debt agreements contain covenants including limitations on additional indebtedness and certain financial tests”
   - cites `KSS-000119312526115982-0094` ✓: “a springing financial covenant relating to our fixed charge coverage ratio and restrictions on indebtedness, liens, investments, asset dispositions, and restricted payments”
6. The interest rate on the **3.375** [quoted: KSS-000119312526115982-0134]% notes due May **2031** [quoted: KSS-000119312526115982-0134] has increased **175** [quoted: KSS-000119312526115982-0134] basis points since issuance because downgrades triggered the notes' coupon adjustment provision, raising the cost of that outstanding maturity.  
   ✅ supported (judge): The passage states the 3.375% notes due May 2031 increased 175 basis points since issuance due to the coupon adjustment provision triggered by downgrades, matching the claim exactly.
   - cites `KSS-000119312526115982-0134` ✓: “the interest rate on the notes due May 2031 have increased 175 basis points since their issuance due to the coupon adjustment provision within the notes”

## Key risks

1. Kohl's has experienced successive credit rating downgrades that have already raised its cost of borrowing, and further downgrades could impair its access to the debt markets and increase the cost of new debt issuances, which is a key risk to refinancing capacity.  
   ✅ supported (judge): All elements of the claim are stated in the passage: downgrades have already raised borrowing costs, further downgrades could impair debt market access and raise cost of new issuances.
   - cites `KSS-000119312526115982-0051` ✓: “Declines in our credit ratings may also adversely affect our ability to access the debt markets and the terms and our cost of funds for new debt issuances.”
2. The company relies on the public debt markets and credit lines to fund operations, seasonal working capital and strategic initiatives, and market disruptions or limited liquidity could restrict access to these sources of future liquidity; its liquidity position may therefore depend on maintaining favorable terms under its senior secured, asset based revolving credit facility.  
   ✅ supported (judge): All parts of the claim are directly stated in the filing passage.
   - cites `KSS-000119312526115982-0050` ✓: “Changes in the credit and capital markets, including market disruptions, limited liquidity, and interest rate fluctuations may increase the cost of financing or restrict our access to these potential sources of future liquidity.”
   - cites `KSS-000119312526115982-0050` ✓: “In January 2023, we upsized and replaced our unsecured credit facility with a $1.5 billion senior secured, asset based revolving credit facility.”
3. The company's debt agreements, particularly its revolving credit facility, contain restrictive covenants, and a failure to comply could trigger an event of default, cross-default, or acceleration of other indebtedness, a direct risk to repayment capacity.  
   ✅ supported (judge): The passage directly states the revolving credit facility has restrictive covenants and that noncompliance could cause default, cross-default, or acceleration of other debt.
   - cites `KSS-000119312526115982-0052` ✓: “A default under our revolving credit facility could trigger a cross-default, acceleration, or other consequences under other indebtedness”
4. Cash flow is exposed to macroeconomic weakness because the core moderate-income customer is especially sensitive to economic conditions, and a U.S. economic slowdown or decline in consumer confidence could reduce traffic and results of operations, particularly given that all stores are in the United States.  
   ✅ supported (judge): All elements of the claim are directly stated in the passage.
   - cites `KSS-000119312526115982-0017` ✓: “A slowdown in the U.S. economy, an uncertain economic outlook, or a decline in consumer confidence could adversely affect consumer spending habits”
5. Profitability and cash flow from the credit card program, in which the company shares in net risk-adjusted revenue, could be pressured by rapid interest rate fluctuations, rising funding costs, increased credit losses from deteriorating macroeconomic conditions, and a consumer shift toward alternative payment methods.  
   ✅ supported (judge): The passage explicitly states the company shares in net risk-adjusted revenue and lists rapid interest rate fluctuations/increased funding costs, increased credit losses from macro deterioration, and consumer shift to alternative payments as pressures on credit card profitability.
   - cites `KSS-000119312526115982-0035` ✓: “increases in funding costs, including significant or rapid interest rate fluctuations, could adversely impact the profitability of our credit card operations”

## Rating rationale

1. The scorecard assigns Kohl's an SB grade of **SB-3** [F28], reflecting a weighted score of **2.72** [F29], and the SB grade is a stylized internal scorecard grade, not a credit rating.  
   ✅ supported (judge): The scorecard metrics show SB grade SB-3, weighted score 2.72, and describe the SB grade as a stylized scorecard grade, not a credit rating.
2. The strongest-scoring factors are liquidity sources / uses, at band **1** [F30] with a weight of **15.0%** [F31], and FCF / debt, at band **2** [F32] with a weight of **20.0%** [F33].  
   ✅ supported (judge): The metric values confirm liquidity sources / uses is band 1 at weight 15.0% and FCF / debt is band 2 at weight 20.0%, and no other factor scores in band 1 or 2.
3. The weakest-scoring factor is EBITDA / interest at band **4** [F34] with the largest weight of **25.0%** [F35], while Debt / EBITDA and net debt / EBITDA both sit at the middle band of **3** [F36] and **3** [F37] with weights of **20.0%** [F38] and **10.0%** [F39] respectively.  
   ✅ supported (judge): EBITDA/interest has the weakest band (4 of 6) with the highest weight (25%), and Debt/EBITDA and net debt/EBITDA are both band 3 with weights 20% and 10%, matching the metric values.
4. The SB grade is provisional because the near-term maturity cover factor, which carries a weight of **10.0%** [F40], is **not available** [F41] and could not be scored, so the remaining factor weights were renormalised.  
   ✅ supported (judge): The metric value for the scorecard confirms the 10% weight, the unavailable metric, renormalisation, and provisional SB-3 grade.
5. The strong liquidity score is supported by earlier findings that the $**1.5** [quoted: KSS-000119312526381893-0016] billion revolving credit facility remained undrawn through the twelve months to 1 August 2026 and had its maturity extended, and that the company was in compliance with all covenants of its debt agreements.  
   ◐ partially supported (judge): The maturity extension and covenant compliance are supported, and the facility was undrawn as of Aug 1, 2026, but the claim that it 'remained undrawn through the twelve months' is contradicted by $75 million drawn as of Aug 2, 2025; also the 'strong liquidity score' is not supported since the liquidity coverage metric scored band 1 of 6 with the near-term maturity cover not scored (provisional grade SB-3).
   - cites `KSS-000119312526381893-0016` ✓: “Borrowings under the $1.5 billion revolving credit facility, recorded as short-term debt, were $0 as of August 1, 2026 and January 31, 2026”
   - cites `KSS-000119312526115982-0135` ✓: “As of January 31, 2026, we were in compliance with all covenants of the various debt agreements.”
6. The SB grade is tempered by earlier findings that successive credit rating downgrades have already raised the company's cost of borrowing and could impair access to debt markets, and that the moderate-income customer base is especially sensitive to weakness in the U.S. economy.  
   ✅ supported (judge): Both cited factors are directly stated in the filings: downgrades raised borrowing costs and may impair debt market access, and the moderate-income customer base is especially sensitive to U.S. economic weakness.
   - cites `KSS-000119312526115982-0051` ✓: “These downgrades have caused our cost of borrowing to increase.”
   - cites `KSS-000119312526115982-0017` ✓: “Our core moderate-income customer is especially sensitive to these factors.”

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
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The $357 million debt issuance, revolver activity, and $440 million repayment all occurred in the fiscal year ended January 31, 2026 (the first column), not the fiscal year ended 1 February 2025 as claimed; also the revolver was net repaid $290 million in FY2026, while the $198 million draw occurred in FY2025.): “The deterioration in leverage in the fiscal year ended 1 February 2025 reflected new borrowing, as the company issued debt with net proceeds of $357 million and drew on the revolving credit facility, before repaying $440 million of long-term borrowings in the fiscal year ended 31 January 2026.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The $350–$400 million fiscal 2026 capex plan and reduced capex are supported, but the claimed improving free cash flow trend is contradicted: operating cash flow fell from $506 million to $478 million in the first half.): “The improving free cash flow trend has continued into the twelve months to 1 August 2026, as capital expenditures fell further under the company's reduced fiscal 2026 spend plans, which anticipate capital expenditures of approximately $350 to $400 million.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The maturity extension and covenant compliance are supported, and the facility was undrawn as of Aug 1, 2026, but the claim that it 'remained undrawn through the twelve months' is contradicted by $75 million drawn as of Aug 2, 2025; also the 'strong liquidity score' is not supported since the liquidity coverage metric scored band 1 of 6 with the near-term maturity cover not scored (provisional grade SB-3).): “The strong liquidity score is supported by earlier findings that the $1.5 billion revolving credit facility remained undrawn through the twelve months to 1 August 2026 and had its maturity extended, and that the company was in compliance with all covenants of its debt agreements.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $17.5 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 17,476,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F2 | Revenue (revenue:FY-1) | $16.2 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 16,221,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F3 | Revenue (revenue:FY0) | $15.5 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 15,527,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F4 | Revenue (revenue:LTM) | $15.4 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 15,527,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 6,682,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 6,779,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F5 | EBITDA (ebitda:FY0) | $1.3 billion | operating_income + d_and_a | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F6 | EBITDA (ebitda:LTM) | $1.3 billion | operating_income + d_and_a | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 347,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 350,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F7 | Operating income (operating_income:FY0) | $624 million | rank 1: OperatingIncomeLoss | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F8 | Operating income (operating_income:LTM) | $592 million | rank 1: OperatingIncomeLoss | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F9 | Debt / EBITDA (debt_to_ebitda:FY-2) | 2.70x | total_debt / EBITDA | LongTermDebtNoncurrent 1,638,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityCurrent 74,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,242,000,000 (at 2024-02-03, balance sheet) [10-K 0000950170-25-042662](https://www.sec.gov/Archives/edgar/data/885639/000095017025042662/0000950170-25-042662-index.htm)<br>OperatingIncomeLoss 717,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 749,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F10 | Debt / EBITDA (debt_to_ebitda:LTM) | 2.53x | total_debt / EBITDA | LongTermDebtNoncurrent 1,325,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityCurrent 82,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,853,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 347,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F11 | Debt / EBITDA (debt_to_ebitda:FY-1) | 3.07x | total_debt / EBITDA | LongTermDebtNoncurrent 1,174,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 353,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityCurrent 72,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,008,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 433,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 743,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F12 | Net leverage (net_leverage:FY-1) | 2.95x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 1,174,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 353,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityCurrent 72,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,008,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 134,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 433,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 743,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F13 | Net leverage (net_leverage:LTM) | 1.89x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 1,325,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityCurrent 82,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,853,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 821,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F14 | EBITDA / interest (interest_coverage:FY-2) | 4.26x | EBITDA / interest_expense | OperatingIncomeLoss 717,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 749,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>InterestIncomeExpenseNet -344,000,000 (2023-01-29 to 2024-02-03, FY-2) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F15 | EBITDA / interest (interest_coverage:LTM) | 4.96x | EBITDA / interest_expense | OperatingIncomeLoss 624,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>OperatingIncomeLoss 307,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>OperatingIncomeLoss 339,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 700,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>DepreciationAndAmortization 347,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>DepreciationAndAmortization 350,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>InterestIncomeExpenseNet -288,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>InterestIncomeExpenseNet -126,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F16 | FCF / debt (fcf_to_debt:FY-1) | 5.0% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 648,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 466,000,000 (2024-02-04 to 2025-02-01, FY-1) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtNoncurrent 1,174,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 353,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityCurrent 72,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,008,000,000 (at 2025-02-01, balance sheet) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F17 | FCF / debt (fcf_to_debt:LTM) | 31.7% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 478,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 506,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 146,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 200,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtNoncurrent 1,325,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityCurrent 82,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F18 | Liquidity coverage (liquidity_coverage:LTM) | 5.81x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 821,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 478,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 506,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 146,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 200,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsOfDividends 56,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F19 | Liquidity coverage (liquidity_coverage:FY0) | 4.80x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 674,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsOfDividends 56,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm) |
| F20 | Cash and cash equivalents (cash:LTM) | $821 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 821,000,000 (at 2026-08-01, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F21 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $0 |  | — |
| F22 | Cash from operations (cfo:LTM) | $1.4 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 1,380,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 478,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 506,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F23 | Capital expenditure (capex:LTM) | $318 million | rank 2: PaymentsToAcquireProductiveAssets | PaymentsToAcquireProductiveAssets 372,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsToAcquireProductiveAssets 146,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsToAcquireProductiveAssets 200,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F24 | Dividends paid (dividends:LTM) | $56 million | rank 1: PaymentsOfDividends | PaymentsOfDividends 56,000,000 (2025-02-02 to 2026-01-31, FY0) [10-K 0001193125-26-115982](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/0001193125-26-115982-index.htm)<br>PaymentsOfDividends 28,000,000 (2026-02-01 to 2026-08-01, current year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>PaymentsOfDividends 28,000,000 (2025-02-02 to 2025-08-02, prior-year year-to-date) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F25 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $0 | rank 2: LongTermDebtCurrent | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm) |
| F26 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $0 | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm) |
| F27 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $3.4 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 1,436,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>LongTermDebtCurrent 0 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-257402](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/0001193125-26-257402-index.htm)<br>FinanceLeaseLiabilityCurrent 76,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm)<br>FinanceLeaseLiabilityNoncurrent 1,919,000,000 (at 2026-01-31, balance sheet) [10-Q 0001193125-26-381893](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/0001193125-26-381893-index.htm) |
| F28 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 2.72222 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F29 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 2.72222 | sum of weight x band over the factors scored, divided by their weights | — |
| F30 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 1 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F31 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F32 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 2 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F33 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F34 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 4 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F35 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F36 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 3 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F37 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 3 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F38 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F39 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F40 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F41 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | not available | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |

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

### KSS-000119312526115982-0035

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 43655–45143

> Our credit card operations facilitate merchandise sales and generate additional revenue from fees related to extending credit. The profitability of our credit card program is sensitive to the economic health of our core moderate-income customer. The private label and co-branded Kohl's credit card accounts are owned by an unrelated third-party, but we share in the net risk-adjusted revenue of the portfolio, which is defined as the sum of finance charges, late fees, and other revenue less write-offs of uncollectible accounts. Changes in funding costs related to interest rate fluctuations are shared similar to the revenue when interest rates exceed defined amounts. Although management currently believes that increases in funding costs will be largely offset by increases in finance charge revenue, increases in funding costs, including significant or rapid interest rate fluctuations, could adversely impact the profitability of our credit card operations. Further deterioration in macroeconomic conditions, including persistent inflation or rising unemployment, could increase credit losses and write-offs, reducing the net revenue we receive from our credit card program. Additionally, consumer preference is shifting toward alternative payment methods, including “buy now, pay later” and other digital payment methods. A shift away from our branded credit products could reduce customer loyalty and the higher-margin transactions often associated with use of our credit card.
> 12

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

### KSS-000119312526115982-0071

mdna, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 81365–82721

> Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations
> Executive Summary
> Kohl's is a leading omnichannel retailer operating 1,153 stores and a website (www.Kohls.com) as of January 31, 2026. Our Kohl's stores and website sell moderately-priced proprietary and national brand apparel, footwear, accessories, beauty, and home products. Our Kohl's stores generally carry a consistent merchandise assortment with some differences attributable to local preferences and store size. Our website includes merchandise which is available in our stores, as well as merchandise that is available only online.
> Key financial results for 2025 as compared to 2024 include:
> •
> Net sales decreased 4.0%, to $14.8 billion, with comparable sales down 3.1%.
> •
> Gross margin as a percent of net sales was 37.5%, an increase of 34 basis points.
> •
> Selling, general & administration ("SG&A") expenses decreased 4.1% year-over-year, to $5.1 billion. As a percentage of total revenue, SG&A expenses were 32.8%, an increase of 5 basis points year-over-year.
> •
> Gain on legal settlement was $129 million from a credit card interchange fee lawsuit settlement.
> •
> Operating income was $624 million compared to $433 million in the prior year. As a percentage of total revenue, operating income was 4.0%, an increase of 135 basis points year-over-year.
> •

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

### KSS-000119312526115982-0094

liquidity, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/885639/000119312526115982/kss-20260131.htm), characters 109288–109724

> Our senior secured, asset based revolving credit facility contains customary events of default and financial, affirmative and negative covenants, including but not limited to, a springing financial covenant relating to our fixed charge coverage ratio and restrictions on indebtedness, liens, investments, asset dispositions, and restricted payments. As of January 31, 2026, we were in compliance with all covenants.
> 34
> Table of Contents

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

### KSS-000119312526257402-0027

mdna, [10-Q for 2026-05-02](https://www.sec.gov/Archives/edgar/data/885639/000119312526257402/kss-20260502.htm), characters 34280–35568

> Gross margin is calculated as net sales less cost of merchandise sold. For the first quarter of 2026, gross margin was 39.9% of net sales, an increase of 4 basis points to last year. The increase was caused by merchandise mix with increased proprietary brand penetration, partially offset by elevated shipping costs driven by our digital sales increase of 4% year over year.
> Selling, General, and Administrative Expense
> Quarter Ended
> (Dollars in Millions)
> May 2, 2026
> May 3, 2025
> Change
> SG&A
> $1,145
> $1,164
> $(19)
> As a percent of total revenue
> 36.2%
> 36.0%
> 15
> bps
> SG&A includes compensation and benefit costs (including stores, corporate, buying, and distribution centers); occupancy and operating costs of our retail, distribution, and corporate facilities; freight expenses associated with moving merchandise from our distribution centers to our retail stores and among distribution and retail facilities other than expenses to fulfill digital sales; marketing expenses, offset by vendor payments for reimbursement of specific, incremental, and identifiable costs; expenses related to our credit card operations; and other administrative revenues and expenses. We do not include depreciation and amortization in SG&A. The classification of these expenses varies across the retail industry.

### KSS-000119312526381893-0006

financial_statements, [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/kss-20260801.htm), characters 7925–8994

> 506
> Investing activities
> Acquisition of property and equipment
> (146)
> (200)
> Proceeds from sale of property and equipment
> —
> 21
> Other
> (7)
> —
> Net cash used in investing activities
> (153)
> (179)
> Financing activities
> Proceeds from issuance of debt, net of discount
> —
> 357
> Deferred financing costs
> —
> (8)
> Net repayments under revolving credit facility
> —
> (215)
> Shares withheld for taxes on vested restricted shares
> (8)
> (4)
> Dividends paid
> (28)
> (28)
> Repayment of long-term borrowings
> (113)
> (353)
> Discount on redemption of debt
> 15
> —
> Finance lease and financing obligation payments
> (44)
> (46)
> Proceeds from financing obligations
> —
> 10
> Net cash used in financing activities
> (178)
> (287)
> Net increase in cash and cash equivalents
> 147
> 40
> Cash and cash equivalents at beginning of period
> 674
> 134
> Cash and cash equivalents at end of period
> $821
> $174
> Supplemental information
> Interest paid, net of capitalized interest
> $146
> $147
> See accompanying Notes to Consolidated Financial Statements
> 6
> Table of Contents
> KOHL’S CORPORATION
> NOTES TO CONSOLIDATED FINANCIAL STATEMENTS
> 1. Basis of Presentation

### KSS-000119312526381893-0016

debt_note, [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/kss-20260801.htm), characters 18581–19752

> In the second quarter of 2025, we issued $360 million aggregate principal amount of 10.000% senior secured notes due 2030 and received proceeds of $357 million, net of the debt discount. The notes are guaranteed by certain of our subsidiaries. Certain of these guarantees are secured by eleven distribution centers and E-commerce Fulfillment Centers, which are held by our subsidiaries, as well as the equity interests in one of our subsidiaries.
> Also in the second quarter of 2025, $353 million in aggregate principal amount of our 4.25% notes matured and were repaid.
> Borrowings under the $1.5 billion revolving credit facility, recorded as short-term debt, were $0 as of August 1, 2026 and January 31, 2026 and $75 million as of August 2, 2025.
> During the second quarter of 2026, we executed an amendment of our revolving credit agreement that extends the maturity of the revolving credit facility by five years to June 30, 2031.
> 9
> Table of Contents
> Our various debt agreements contain covenants including limitations on additional indebtedness and certain financial tests. As of August 1, 2026, we were in compliance with all covenants of the various debt agreements.

### KSS-000119312526381893-0032

mdna, [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/kss-20260801.htm), characters 38781–40249

> Three Months Ended
> Six Months Ended
> (Dollars in Millions)
> August 1, 2026
> August 2, 2025
> Change
> August 1, 2026
> August 2, 2025
> Change
> SG&A
> $1,188
> $1,199
> $(11)
> $2,333
> $2,363
> $(30)
> As a percent of total revenue
> 33.8%
> 33.8%
> 0
> bps
> 34.9%
> 34.9%
> 6
> bps
> SG&A includes compensation and benefit costs (including stores, corporate, buying, and distribution centers); occupancy and operating costs of our retail, distribution, and corporate facilities; freight expenses associated with moving merchandise from our distribution centers to our retail stores and among distribution and retail facilities other than expenses to fulfill digital sales; marketing expenses, offset by vendor payments for reimbursement of specific, incremental, and identifiable costs; expenses related to our credit card operations; and other administrative revenues and expenses. We do not include depreciation and amortization in SG&A. The classification of these expenses varies across the retail industry.
> 17
> Table of Contents
> Many of our expenses, including store payroll and distribution costs, are variable in nature. These costs generally increase as sales increase and decrease as sales decrease. We measure our expenses as a percentage of revenue and changes in this percentage compared to the prior year. If the expense as a percent of revenue decreased from the prior year, the expense "leveraged." If the expense as a percent of revenue increased over the prior year, the expense "deleveraged."

### KSS-000119312526381893-0042

liquidity, [10-Q for 2026-08-01](https://www.sec.gov/Archives/edgar/data/885639/000119312526381893/kss-20260801.htm), characters 50268–51605

> Our operating cash outflows generally consist of payments to our employees for wages, salaries and other employee benefits, payments to our merchandise vendors for inventory (net of vendor allowances), payments to our shipping carriers, and payments to our landlords for rent. Operating cash outflows also include payments for income taxes and interest payments on our debt borrowings.
> Operating activities provided $478 million of cash in the first half of 2026 compared to $506 million in the first half of 2025. The decrease in cash provided by operating activities is primarily driven by timing of payments.
> Investing Activities
> Our investing cash outflows include payments for capital expenditures, including investments in new and existing stores, improvements to supply chain, and technology costs. Our investing cash inflows are generally from proceeds from sales of property and real estate.
> Investing activities used $153 million in the first half of 2026 compared to $179 million in the first half of 2025. The decrease in cash used in investing activities was primarily driven by our reduced capital expenditure plans for fiscal 2026.
> In 2026, we anticipate capital expenditures of approximately $350 to $400 million as we continue to invest in our business, including enhancing omnichannel capabilities.
> Financing Activities

## Run

Run `KSS-20261118T062626Z-GLM-5.3`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 7 calls, 29,030 input (5,632 cached) and 16,888 output tokens, $0.0760, 134s. Verification: 35 calls, 18,138 input (4,480 cached) and 3,854 output tokens, $0.0261, 71s. Prices read 2026-11-17. Raw requests and responses: data/runs/KSS/KSS-20261118T062626Z-GLM-5.3.jsonl.
