# Credit memo: Carnival Corp Ltd. (CCL)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `zai-org/GLM-5.3`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-4**.
Sources: [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm); [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm); [10-Q for 2026-02-28](https://www.sec.gov/Archives/edgar/data/815097/000081509726000037/ccl-20260228.htm); [10-Q for 2026-05-31](https://www.sec.gov/Archives/edgar/data/815097/000081509726000096/ccl-20260531.htm)

Claims: 36 — 28 supported, 8 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 4; repairs: 3.

## Business profile

1. Carnival Corporation & plc is the largest global cruise company and among the largest leisure travel companies, operating a portfolio of cruise lines that includes AIDA Cruises, Carnival Cruise Line, Costa Cruises, Cunard, Holland America Line, P&O Cruises, Princess Cruises and Seabourn.  
   ✅ supported (judge): The passage states the company is the largest global cruise company, among the largest leisure travel companies, and lists exactly the named cruise lines.
   - cites `CCL-000081509726000007-0011` ✓: “We are the largest global cruise company, and among the largest leisure travel companies, with a portfolio of world-class cruise lines”
2. The company generated revenue of **$26.6 billion** [F1] in the fiscal year ended 30 November 2025 and **$27.6 billion** [F2] in the twelve months to 31 August 2026, with EBITDA of **$7.3 billion** [F3] and **$7.3 billion** [F4] over the same periods, respectively.  
   ✅ supported (judge): All four figures in the claim match the XBRL-computed metric values for FY0 and LTM periods.
3. Revenue grew from **$21.6 billion** [F5] in the fiscal year ended 30 November 2023 to **$26.6 billion** [F1] in the fiscal year ended 30 November 2025, reflecting continued recovery and growth in the business.  
   ◐ partially supported (judge): The revenue figures ($21.6B FY2023, $26.6B FY2025) are confirmed by the metric values, but the characterization 'continued recovery and growth' is an interpretive statement not established by the evidence.
4. The brand portfolio is diversified across distinct customer segments, and the mobility of cruise ships allows the company to redeploy vessels between regions to meet changing demand, which can support more stable cash flows.  
   ✅ supported (judge): The evidence directly states each brand serves distinct customer segments and ship mobility allows redeployment to meet changing demand.
   - cites `CCL-000081509726000007-0016` ✓: “Each brand in our portfolio meets the needs of a distinct set of consumer psychographics and vacation needs”
   - cites `CCL-000081509726000007-0016` ✓: “The mobility of cruise ships enables us to move our vessels between regions in order to meet changing demand across different geographic areas.”
5. Distribution is diversified, with no group of travel agencies under common control accounting for **10** [quoted: CCL-000081509726000007-0030]% or more of revenues in **2025** [quoted: CCL-000081509726000007-0030], limiting reliance on any single distribution partner.  
   ✅ supported (judge): The evidence directly states that no group of travel agencies under common control accounted for 10% or more of revenues during 2025, and travel agents are described as part of a broad distribution network, supporting limited reliance on a single partner.
   - cites `CCL-000081509726000007-0030` ✓: “During 2025, no group of travel agencies under common control accounted for 10% or more of our revenues.”
6. Cash flows remain exposed to cyclicality and competitive pressures, as overcapacity and competition in the cruise and land-based vacation industry may negatively impact cruise sales, pricing and destination options.  
   ✅ supported (judge): The claim matches the risk factor about overcapacity and competition impacting cruise sales, pricing and destination options, which bears on cash flow risk.
   - cites `CCL-000081509726000037-0039` ✓: “Overcapacity and competition in the cruise and land-based vacation industry may negatively impact our cruise sales, pricing and destination options.”

## Financial risk

1. Debt / EBITDA improved steadily from **7.07x** [F6] in the fiscal year ended 30 November 2023 to **3.27x** [F7] in the twelve months to 31 August 2026.  
   ◐ partially supported (judge): The endpoint values 7.07x (FY ended 30 Nov 2023) and 3.27x (LTM to 31 Aug 2026) match the metric values, but 'improved steadily' implies a consistent trend across intervening periods, which the evidence (only two point-in-time values) does not establish.
2. Net leverage improved from **6.51x** [F8] in the fiscal year ended 30 November 2023 to **3.10x** [F9] in the twelve months to 31 August 2026, with total debt declining from **$26.6 billion** [F10] to **$23.9 billion** [F11].  
   ◐ partially supported (judge): Net leverage values of 6.51x and 3.10x are confirmed, and total debt of $23.9 billion for the LTM period is confirmed, but the $26.6 billion figure corresponds to the fiscal year ended 30 November 2025 (FY0), not the fiscal year ended 30 November 2023, so the starting debt figure is misattributed.
3. Interest coverage improved from **2.09x** [F12] in the fiscal year ended 30 November 2023 to **6.21x** [F13] in the twelve months to 31 August 2026, on LTM interest expense of **$1.2 billion** [F14].  
   ✅ supported (judge): All claim components match the computed metric values exactly.
4. FCF / debt improved from **3.3%** [F15] in the fiscal year ended 30 November 2023 to **13.3%** [F16] in the twelve months to 31 August 2026, with LTM cash from operations of **$6.8 billion** [F17] exceeding capital expenditure of **$3.6 billion** [F18].  
   ✅ supported (judge): All figures match the scorecard exactly: FCF/debt 3.3% to 13.3%, LTM CFO $6.8B and capex $3.6B.
5. The improvement in leverage and coverage metrics over the period was driven primarily by an improvement in earnings, with net income rising year over year through the trailing nine months.  
   ◐ partially supported (judge): The evidence supports rising net income ($2.3B to $2.7B) for the trailing nine months, but contains no data on leverage or coverage metrics improving or that earnings was the primary driver of any such improvement.
   - cites `CCL-000081509726000107-0054` ✓: “an improvement in our earnings with $2.7 billion of net income in 2026 compared to $2.3 billion of net income in 2025”
6. During the fiscal year ended 30 November 2025 the company actively managed its debt stack through issuance of new debt, modification and extinguishment of existing debt, and refinancing of syndicated debt, while capital spending remained concentrated in ship improvements, the new shipbuilding program and development of exclusive destinations.  
   ◐ partially supported (judge): The debt management activities for FY2025 are supported, but the capital spending description is only evidenced for the nine months ended August 31, 2026 (and the 2025 nine-month passage omits the new shipbuilding program), not the fiscal year ended November 30, 2025.
   - cites `CCL-000081509726000007-0222` ✓: “During the year ended November 30, 2025, the Company entered into various debt transactions that involved issuance of new debt, modification and extinguishment of existing debt”
   - cites `CCL-000081509726000107-0054` ✓: “Capital expenditures of $2.1 billion principally attributable to ship improvements, our ongoing new shipbuilding program and development of our portfolio of exclusive destinations”

## Liquidity

1. Liquidity coverage was **1.42x** [F19] for the twelve months to 31 August 2026, compared with **1.31x** [F20] for the fiscal year ended 30 November 2025, indicating liquidity sources covered projected twelve-month needs with a moderate cushion.  
   ✅ supported (judge): The metric values exactly match the claim: liquidity coverage of 1.42x for the twelve months to 31 August 2026 and 1.31x for FY ended 30 November 2025, with coverage above 1.0x supporting the moderate-cushion characterization.
2. Cash from operations of **$6.8 billion** [F17] exceeded the sum of capital expenditure of **$3.6 billion** [F18] and short-term debt of **$2.0 billion** [F21], so the largest near-term uses were covered internally before drawing on cash balances.  
   ✅ supported (judge): The metric values confirm cash from operations ($6.8B) exceeds capex ($3.6B) plus short-term debt ($2.0B), totaling $5.6B, so these uses were covered internally; the conclusion follows directly.
3. At the end of the twelve months to 31 August 2026, the company had $**4.5** [quoted: CCL-000081509726000107-0021] billion available for borrowing under the Revolving Facility, providing committed backstop liquidity in addition to its cash position of **$1.2 billion** [F22].  
   ✅ supported (judge): The $4.5 billion available Revolving Facility is stated in the passage, and the $1.2 billion cash figure matches the computed metric; the characterization as committed liquidity is consistent with the passage.
   - cites `CCL-000081509726000107-0021` ✓: “we had $4.5 billion available for borrowing under the Revolving Facility”
   - cites `CCL-000081509726000107-0021` ✓: “We may borrow or utilize available amounts under the Revolving Facility through June 2030, subject to the satisfaction of the conditions in the facility.”
4. The company also had $**10.7** [quoted: CCL-000081509726000107-0053] billion of undrawn export credit facilities to fund future ship deliveries, which supports funding of the newbuild program without drawing on general liquidity.  
   ◐ partially supported (judge): The $10.7 billion undrawn export credit facilities figure is supported, but the evidence does not state these facilities support funding 'without drawing on general liquidity.'
   - cites `CCL-000081509726000107-0053` ✓: “we had $10.7 billion of undrawn export credit facilities to fund future ship deliveries”
5. The company operates with a substantial working capital deficit that arises from its business model of collecting guest cruise deposits ahead of the sailing date, and these customer deposits are used alongside other cash sources to fund operations, service debt and support capital investments, so the deficit is a structural feature rather than an immediate liquidity strain.  
   ✅ supported (judge): The passage explicitly states the working capital deficit, its cause (advance guest deposits), their use of those deposits to fund operations, service debt and capital investments — all elements of the claim.
   - cites `CCL-000081509726000107-0053` ✓: “We operate with a substantial working capital deficit, largely due to our business model in which guest cruise ticket deposits”
   - cites `CCL-000081509726000107-0053` ✓: “These customer deposits are used alongside other cash sources to fund operations, service debt, and support capital investments.”
6. The Revolving Facility is subject to covenants that include maintaining minimum liquidity of $**1.5** [quoted: CCL-000081509726000107-0021] billion, a threshold the company appears to clear comfortably given its reported liquidity position.  
   ◐ partially supported (judge): The $1.5 billion minimum liquidity covenant is confirmed, but the evidence only shows $4.5 billion available under the Revolving Facility, not the company's actual reported liquidity position, so the 'clears comfortably' conclusion goes beyond the stated evidence.
   - cites `CCL-000081509726000107-0021` ✓: “Maintain minimum liquidity of $1.5 billion”

## Maturity wall

1. At the fiscal year ended 30 November 2025, scheduled debt maturities were **$2.6 billion** [F23] in year one, **$2.5 billion** [F24] in year two, **$4.0 billion** [F25] in year three, **$4.1 billion** [F26] in year four and **$2.9 billion** [F27] in year five, with **$11.3 billion** [F28] due after year five.  
   ✅ supported (judge): Claim's rounded maturities match the scheduled maturities table: 2026 $2,615M (~2.6B), 2027 $2,518M (~2.5B), 2028 $3,962M (~4.0B), 2029 $4,133M (~4.1B), 2030 $2,886M (~2.9B), thereafter $11,268M (~11.3B).
   - cites `CCL-000081509726000007-0177` ✓: “As of November 30, 2025, the scheduled maturities of our debt are as follows”
2. Debt due within the next two years at the fiscal year ended 30 November 2025 was **$5.1 billion** [F29], representing **19.2%** [F30] of total debt of **$26.6 billion** [F10].  
   ✅ supported (judge): Metric values confirm debt due within 24 months was $5.1B, which is 19.2% of total debt of $26.6B.
3. Near-term maturity cover at the fiscal year ended 30 November 2025 was **2.66x** [F31], calculated with cash and cash equivalents of **$1.9 billion** [F32] and undrawn revolving credit capacity of **$0** [F33] (assumed zero, as none was reported).  
   ✅ supported (judge): The claim matches the computed scorecard exactly: 2.66x cover, $1.9B cash, $0 undrawn revolver (assumed zero, not reported).
4. During the fiscal year ended 30 November 2025, the company issued multiple series of senior unsecured notes and borrowed under unsecured term loan facilities, and used the proceeds together with cash on hand to prepay higher-coupon debt instruments maturing in the near term, with aggregate prepayments of $**11.6** [quoted: CCL-000081509726000007-0180] billion.  
   ✅ supported (judge): Evidence states 2025 issuance of multiple senior unsecured notes series, unsecured term loan borrowings, and prepayment of higher-coupon debt with proceeds plus cash on hand totaling $11.6 billion.
   - cites `CCL-000081509726000007-0179` ✓: “used proceeds from debt issuances and borrowings, together with cash on hand, to prepay”
   - cites `CCL-000081509726000007-0180` ✓: “The aggregate amount of these prepayments was $11.6 billion.”
5. The company was in compliance with the applicable covenants under its debt agreements as of the fiscal year ended 30 November 2025 and as of the end of the twelve months to 31 August 2026, but cross-default and cross-acceleration clauses mean an event of default could make substantially all outstanding debt due and terminated.  
   ✅ supported (judge): Both passages explicitly state covenant compliance at November 30, 2025 and August 31, 2026, and describe the cross-default/cross-acceleration consequence.
   - cites `CCL-000081509726000007-0183` ✓: “we were in compliance with the applicable covenants under our debt agreements”
   - cites `CCL-000081509726000107-0022` ✓: “substantially all of our outstanding debt could become due, and our debt could be terminated”
6. In addition to the assumed zero undrawn revolving credit capacity, the company had $**7.8** [quoted: CCL-000081509726000007-0180] billion of undrawn export credit facilities as of the fiscal year ended 30 November 2025 available to fund planned ship deliveries.  
   ✅ supported (judge): The evidence states the company had $7.8 billion of undrawn export credit facilities as of November 30, 2025 to fund planned ship deliveries; while the claim's 'zero undrawn revolving credit capacity' isn't explicitly evidenced, the export facility part is directly stated.
   - cites `CCL-000081509726000007-0180` ✓: “we had $7.8 billion of undrawn export credit facilities to fund ship deliveries planned”

## Key risks

1. A breach of covenants or restrictions in Carnival's debt instruments could trigger a default, allowing creditors to declare the debt due and payable and to accelerate other borrowings under cross-default provisions, which is the most direct risk to refinancing and debt repayment.  
   ✅ supported (judge): The passage states covenant breaches could trigger default, creditors could declare debt due and payable, and cross-default provisions could accelerate other borrowings.
   - cites `CCL-000081509726000007-0080` ✓: “we may be required to seek covenant amendments or the relevant creditors could elect to declare the debt due and payable”
2. Carnival may also incur more debt in the future despite its existing leverage, which could further strain its ability to service and repay its obligations.  
   ✅ supported (judge): The passage directly states that despite its leverage, the company may incur more debt in the future.
   - cites `CCL-000081509726000007-0080` ✓: “Despite our leverage, we may incur more debt in the future.”
3. Fuel cost increases and fuel supply volatility would raise operating costs across Carnival's cruise operations and could reduce profitability, pressuring the cash flow available for debt service.  
   ◐ partially supported (judge): The passage supports that fuel cost increases and supply volatility raise cruise operating costs and can reduce profitability, but the claim's extension to pressuring cash flow available for debt service is not stated in the evidence.
   - cites `CCL-000081509726000007-0081` ✓: “Future increases in the global price of fuel would increase the cost of our cruise ship operations as well as some of our other expenses”
4. Emissions and sustainability regulations, including EU and UK regulations and the IMO Strategy, may require additional capital investments and increase operating costs, diverting cash flow that could otherwise support debt repayment.  
   ✅ supported (judge): The passage states EU and UK regulations and the IMO Strategy may require capital investments and increase operating costs, though the cash flow diversion/debt repayment framing is a credit memo inference.
   - cites `CCL-000081509726000007-0089` ✓: “requiring us to make capital investments in new equipment or technologies, pay for emission allowances, purchase carbon offset credits, or otherwise incur additional costs”
5. Macroeconomic and geopolitical conditions, including pandemics, inflation and higher interest rates, could reduce demand for cruises and negatively affect Carnival's financial condition, weakening the cash flows supporting its debt.  
   ✅ supported (judge): The risk factor directly states geopolitical conditions, pandemics, inflation and higher interest rates could reduce cruise demand and negatively affect financial condition and operations.
   - cites `CCL-000081509726000007-0068` ✓: “pandemics, inflation, higher interest rates and other general concerns impacting the ability or desire of people to travel could lead to a decline in demand for cruises”
6. In the twelve months to 31 August 2026, Carnival's debt to EBITDA was **3.27x** [F7], its EBITDA to interest coverage was **6.21x** [F13], and free cash flow to debt was **13.3%** [F16], indicating moderate leverage but limited annual free cash flow relative to the debt load.  
   ✅ supported (judge): All three metric values (debt/EBITDA 3.27x, EBITDA/interest 6.21x, FCF/debt 13.3%) are directly confirmed by the computed scorecard; the qualitative characterization follows reasonably from them, and the passage notes 'Despite our leverage, we may incur more debt in the future.'
   - cites `CCL-000081509726000007-0080` ✓: “If we breach the covenants or restrictions in our debt instruments, we could trigger a default under the terms of certain of our debt instruments.”

## Rating rationale

1. The SB grade for Carnival Corporation & plc is **SB-4** [F34], reflecting a weighted score of **3.95** [F35], and this is a stylized internal scorecard grade, not a credit rating; the grade is not provisional because all six factors were scored.  
   ✅ supported (judge): All claim elements (SB-4 grade, 3.95 weighted score, stylized not credit rating, not provisional since all six factors scored) match the computed scorecard metrics.
2. The strongest-scoring factor is EBITDA to interest, which sits in band **3** [F36] at **6.21x** [F13] for the twelve months to 31 August 2026 and carries the largest weight in the scorecard at **25.0%** [F37].  
   ✅ supported (judge): EBITDA/interest has the best band (3 vs 4/4/4/4/6 for other factors), the LTM value is 6.21x, and its 25.0% weight is the largest in the scorecard.
3. The weakest-scoring factor is near-term maturity cover, which sits in band **6** [F38] at **2.66x** [F31] for the fiscal year ended 30 November 2025 with a weight of **10.0%** [F39], partially offset by liquidity coverage in band **4** [F40] at **1.42x** [F19] carrying a weight of **15.0%** [F41].  
   ✅ supported (judge): All figures match the scorecard: near-term maturity cover 2.66x in band 6 (weakest) with weight 10.0%, and liquidity coverage 1.42x in band 4 with weight 15.0%.
4. The remaining factors of debt to EBITDA, net leverage and free cash flow to debt each sit in band **4** [F42] at **3.27x** [F7], **3.10x** [F9] and **13.3%** [F16] respectively, with weights of **20.0%** [F43], **10.0%** [F44] and **20.0%** [F45].  
   ✅ supported (judge): All three values (3.27x, 3.10x, 13.3%), bands (4) and weights (20%, 10%, 20%) match the scorecard and metric data.
5. The earlier findings support the scorecard outcome, as the company's diversified brand portfolio and the ability to redeploy vessels between regions can support more stable cash flows, and it remained in compliance with the covenants under its debt agreements.  
   ✅ supported (judge): The evidence states the diversified brand portfolio, vessel mobility between regions, and covenant compliance, matching all claim parts.
   - cites `CCL-000081509726000007-0016` ✓: “The mobility of cruise ships enables us to move our vessels between regions in order to meet changing demand across different geographic areas”
   - cites `CCL-000081509726000107-0022` ✓: “we were in compliance with the applicable covenants under our debt agreements”
6. The grade is tempered by earlier findings that cash flows remain exposed to industry overcapacity and competitive pressures, and that a covenant breach could allow creditors to accelerate borrowings under cross-default provisions.  
   ✅ supported (judge): Both parts of the claim are directly stated: industry overcapacity/competition risks and cross-default acceleration upon covenant breach.
   - cites `CCL-000081509726000037-0039` ✓: “Overcapacity and competition in the cruise and land-based vacation industry may negatively impact our cruise sales, pricing and destination options”
   - cites `CCL-000081509726000007-0080` ✓: “Borrowings under our other debt instruments that contain cross-default provisions may also be accelerated or become payable on demand”

## Reviewer checklist

- [ ] **fallback** (info): Revenue: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Depreciation and amortisation: used rank 2 DepreciationAndAmortization in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Interest expense: used rank 2 InterestExpenseNonoperating in FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): CommercialPaper assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Finance-lease liabilities (current plus non-current) assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term investments assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Dividends paid assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): ShortTermBorrowings assumed zero (not reported) in FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **partially supported claim** (warning): Business profile: partially supported (The revenue figures ($21.6B FY2023, $26.6B FY2025) are confirmed by the metric values, but the characterization 'continued recovery and growth' is an interpretive statement not established by the evidence.): “Revenue grew from $21.6 billion in the fiscal year ended 30 November 2023 to $26.6 billion in the fiscal year ended 30 November 2025, reflecting continued recovery and growth in the business.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The endpoint values 7.07x (FY ended 30 Nov 2023) and 3.27x (LTM to 31 Aug 2026) match the metric values, but 'improved steadily' implies a consistent trend across intervening periods, which the evidence (only two point-in-time values) does not establish.): “Debt / EBITDA improved steadily from 7.07x in the fiscal year ended 30 November 2023 to 3.27x in the twelve months to 31 August 2026.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (Net leverage values of 6.51x and 3.10x are confirmed, and total debt of $23.9 billion for the LTM period is confirmed, but the $26.6 billion figure corresponds to the fiscal year ended 30 November 2025 (FY0), not the fiscal year ended 30 November 2023, so the starting debt figure is misattributed.): “Net leverage improved from 6.51x in the fiscal year ended 30 November 2023 to 3.10x in the twelve months to 31 August 2026, with total debt declining from $26.6 billion to $23.9 billion.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The evidence supports rising net income ($2.3B to $2.7B) for the trailing nine months, but contains no data on leverage or coverage metrics improving or that earnings was the primary driver of any such improvement.): “The improvement in leverage and coverage metrics over the period was driven primarily by an improvement in earnings, with net income rising year over year through the trailing nine months.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The debt management activities for FY2025 are supported, but the capital spending description is only evidenced for the nine months ended August 31, 2026 (and the 2025 nine-month passage omits the new shipbuilding program), not the fiscal year ended November 30, 2025.): “During the fiscal year ended 30 November 2025 the company actively managed its debt stack through issuance of new debt, modification and extinguishment of existing debt, and refinancing of syndicated debt, while capital spending remained concentrated in ship improvements, the new shipbuilding program and development of exclusive destinations.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The $10.7 billion undrawn export credit facilities figure is supported, but the evidence does not state these facilities support funding 'without drawing on general liquidity.'): “The company also had $10.7 billion of undrawn export credit facilities to fund future ship deliveries, which supports funding of the newbuild program without drawing on general liquidity.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The $1.5 billion minimum liquidity covenant is confirmed, but the evidence only shows $4.5 billion available under the Revolving Facility, not the company's actual reported liquidity position, so the 'clears comfortably' conclusion goes beyond the stated evidence.): “The Revolving Facility is subject to covenants that include maintaining minimum liquidity of $1.5 billion, a threshold the company appears to clear comfortably given its reported liquidity position.”
- [ ] **partially supported claim** (warning): Key risks: partially supported (The passage supports that fuel cost increases and supply volatility raise cruise operating costs and can reduce profitability, but the claim's extension to pressuring cash flow available for debt service is not stated in the evidence.): “Fuel cost increases and fuel supply volatility would raise operating costs across Carnival's cruise operations and could reduce profitability, pressuring the cash flow available for debt service.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY0) | $26.6 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 26,622,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F2 | Revenue (revenue:LTM) | $27.6 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 26,622,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 21,263,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 20,292,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F3 | EBITDA (ebitda:FY0) | $7.3 billion | operating_income + d_and_a | OperatingIncomeLoss 4,483,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,790,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F4 | EBITDA (ebitda:LTM) | $7.3 billion | operating_income + d_and_a | OperatingIncomeLoss 4,483,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>OperatingIncomeLoss 3,678,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>OperatingIncomeLoss 3,748,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,790,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,172,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,064,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F5 | Revenue (revenue:FY-2) | $21.6 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 21,593,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F6 | Debt / EBITDA (debt_to_ebitda:FY-2) | 7.07x | total_debt / EBITDA | LongTermDebtNoncurrent 28,483,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-25-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509725000007/0000815097-25-000007-index.htm)<br>LongTermDebtCurrent 2,089,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-25-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509725000007/0000815097-25-000007-index.htm)<br>ShortTermBorrowings 0 (at 2023-11-30, balance sheet) [10-K 0000815097-24-000011](https://www.sec.gov/Archives/edgar/data/815097/000081509724000011/0000815097-24-000011-index.htm)<br>OperatingIncomeLoss 1,956,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,370,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:LTM) | 3.27x | total_debt / EBITDA | LongTermDebtNoncurrent 21,876,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,036,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>OperatingIncomeLoss 4,483,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>OperatingIncomeLoss 3,678,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>OperatingIncomeLoss 3,748,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,790,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,172,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,064,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F8 | Net leverage (net_leverage:FY-2) | 6.51x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 28,483,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-25-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509725000007/0000815097-25-000007-index.htm)<br>LongTermDebtCurrent 2,089,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-25-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509725000007/0000815097-25-000007-index.htm)<br>ShortTermBorrowings 0 (at 2023-11-30, balance sheet) [10-K 0000815097-24-000011](https://www.sec.gov/Archives/edgar/data/815097/000081509724000011/0000815097-24-000011-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 2,415,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>OperatingIncomeLoss 1,956,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,370,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F9 | Net leverage (net_leverage:LTM) | 3.10x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 21,876,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,036,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 1,220,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>OperatingIncomeLoss 4,483,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>OperatingIncomeLoss 3,678,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>OperatingIncomeLoss 3,748,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,790,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,172,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F10 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $26.6 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 24,037,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,603,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F11 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $23.9 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 21,876,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,036,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F12 | EBITDA / interest (interest_coverage:FY-2) | 2.09x | EBITDA / interest_expense | OperatingIncomeLoss 1,956,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,370,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>InterestExpense 2,066,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-24-000011](https://www.sec.gov/Archives/edgar/data/815097/000081509724000011/0000815097-24-000011-index.htm) |
| F13 | EBITDA / interest (interest_coverage:LTM) | 6.21x | EBITDA / interest_expense | OperatingIncomeLoss 4,483,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>OperatingIncomeLoss 3,678,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>OperatingIncomeLoss 3,748,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,790,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>DepreciationAndAmortization 2,172,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>DepreciationAndAmortization 2,064,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>InterestExpenseNonoperating 1,349,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>InterestExpenseNonoperating 862,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F14 | Interest expense (interest_expense:LTM) | $1.2 billion | rank 2: InterestExpenseNonoperating | InterestExpenseNonoperating 1,349,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>InterestExpenseNonoperating 862,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>InterestExpenseNonoperating 1,034,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F15 | FCF / debt (fcf_to_debt:FY-2) | 3.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 4,281,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,284,000,000 (2022-12-01 to 2023-11-30, FY-2) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>LongTermDebtNoncurrent 28,483,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-25-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509725000007/0000815097-25-000007-index.htm)<br>LongTermDebtCurrent 2,089,000,000 (at 2023-11-30, balance sheet) [10-K 0000815097-25-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509725000007/0000815097-25-000007-index.htm)<br>ShortTermBorrowings 0 (at 2023-11-30, balance sheet) [10-K 0000815097-24-000011](https://www.sec.gov/Archives/edgar/data/815097/000081509724000011/0000815097-24-000011-index.htm) |
| F16 | FCF / debt (fcf_to_debt:LTM) | 13.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 6,218,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 5,303,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 4,700,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,611,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 2,139,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 2,105,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtNoncurrent 21,876,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,036,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F17 | Cash from operations (cfo:LTM) | $6.8 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 6,218,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 5,303,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 4,700,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F18 | Capital expenditure (capex:LTM) | $3.6 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 3,611,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 2,139,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 2,105,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F19 | Liquidity coverage (liquidity_coverage:LTM) | 1.42x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 1,220,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 6,218,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 5,303,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 4,700,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,036,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,611,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 2,139,000,000 (2025-12-01 to 2026-08-31, current year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 2,105,000,000 (2024-12-01 to 2025-08-31, prior-year year-to-date) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F20 | Liquidity coverage (liquidity_coverage:FY0) | 1.31x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 1,928,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 6,218,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>LongTermDebtCurrent 2,603,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 3,611,000,000 (2024-12-01 to 2025-11-30, FY0) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F21 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $2.0 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 2,036,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F22 | Cash and cash equivalents (cash:LTM) | $1.2 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 1,220,000,000 (at 2026-08-31, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F23 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $2.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 2,615,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F24 | Debt maturing in year two (maturity_year_2:FY0) | $2.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,518,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F25 | Debt maturing in year three (maturity_year_3:FY0) | $4.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 3,962,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F26 | Debt maturing in year four (maturity_year_4:FY0) | $4.1 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 4,133,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F27 | Debt maturing in year five (maturity_year_5:FY0) | $2.9 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 2,886,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F28 | Debt maturing after year five (maturity_after_year_5:FY0) | $11.3 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 11,268,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F29 | Debt due within 24 months (debt_due_24m:FY0) | $5.1 billion | short_term_debt + maturity_year_2 | LongTermDebtCurrent 2,603,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,518,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm) |
| F30 | Share of debt due within 24 months (share_due_24m:FY0) | 19.2% | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtCurrent 2,603,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,518,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>LongTermDebtNoncurrent 24,037,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtCurrent 2,603,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F31 | Near-term maturity cover (near_term_maturity_cover:FY0) | 2.66x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtCurrent 2,603,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 2,518,000,000 (at 2025-11-30, balance sheet) [10-K 0000815097-26-000007](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/0000815097-26-000007-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 1,928,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F32 | Cash and cash equivalents (cash:FY0) | $1.9 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 1,928,000,000 (at 2025-11-30, balance sheet) [10-Q 0000815097-26-000107](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/0000815097-26-000107-index.htm) |
| F33 | Undrawn revolving credit capacity (undrawn_revolver:FY0) | $0 |  | — |
| F34 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 3.95 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F35 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 3.95 | sum of weight x band over the factors scored, divided by their weights | — |
| F36 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 3 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F37 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F38 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 6 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F39 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F40 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 4 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F41 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F42 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 4 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F43 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F44 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F45 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### CCL-000081509726000007-0011

business, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 14576–15947

> Item 1. Business.
> A. Overview
> I.Summary
> Carnival Corporation was incorporated in Panama in 1974 and Carnival plc was incorporated in England and Wales in 2000. Carnival Corporation and Carnival plc operate a dual listed company whereby the businesses of Carnival Corporation and Carnival plc are combined through a number of contracts and through provisions in Carnival Corporation’s Articles of Incorporation and By-Laws and Carnival plc’s Articles of Association. The two companies operate as if they are a single economic enterprise with a single executive management team and identical Boards of Directors, but each has retained its separate legal identity. Carnival Corporation and Carnival plc are both public companies with separate stock exchange listings and their own shareholders. Together with their consolidated subsidiaries, Carnival Corporation and Carnival plc are referred to collectively in this Form 10-K as “Carnival Corporation & plc,” “company,” “our,” “us” and “we.” We are the largest global cruise company, and among the largest leisure travel companies, with a portfolio of world-class cruise lines - AIDA Cruises, Carnival Cruise Line, Costa Cruises, Cunard, Holland America Line, P&O Cruises, Princess Cruises and Seabourn. During 2025, we sunset the P&O Cruises (Australia) brand and folded its Australia operations into Carnival Cruise Line.

### CCL-000081509726000007-0016

business, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 20970–22052

> Several years of exceptional performance has significantly strengthened our financial fitness—reducing debt, achieving strong profitability and double‑digit ROIC, surpassing the investment grade threshold and reinstating our dividend. We are fortifying our position through disciplined cost control and continued deleveraging. At the same time, our measured investments in newbuilds, major ship midlife refurbishment enhancements across our cruise lines and destination development, and continued focus on commercial excellence, are setting the stage for substantial long‑term growth and value creation.
> B. Global Cruise Industry
> I. Overview
> Cruising offers a broad range of products and services to suit vacationing guests of many ages, backgrounds and interests. Each brand in our portfolio meets the needs of a distinct set of consumer psychographics and vacation needs which allows us to penetrate large addressable customer segments. The mobility of cruise ships enables us to move our vessels between regions in order to meet changing demand across different geographic areas.

### CCL-000081509726000007-0030

business, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 38534–39335

> Travel agent partners are an integral part of our long-term cruise distribution network and are critical to our success. We utilize local sales teams to motivate travel agents to support our products and services with competitive pricing, promotional policies and joint marketing and advertising programs. During 2025, no group of travel agencies under common control accounted for 10% or more of our revenues. We also employ a wide variety of educational programs, including websites, seminars and videos, to train agents on our cruise brands and their products and services. In 2025, we held a variety of trainings and educational programs to continue to support and develop our travel agent partners, including ship visits to familiarize our travel agent partners with our products and services.
> 11

### CCL-000081509726000007-0068

risk_factors, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 85385–85776

> Operational Risk Factors
> a.Events and conditions around the world, including geopolitical uncertainty, war and other military actions, pandemics, inflation, higher interest rates and other general concerns impacting the ability or desire of people to travel could lead to a decline in demand for cruises as well as have significant negative impacts on our financial condition and operations.

### CCL-000081509726000007-0080

risk_factors, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 96685–97508

> If we breach the covenants or restrictions in our debt instruments, we could trigger a default under the terms of certain of our debt instruments. If that occurs, we may be required to seek covenant amendments or the relevant creditors could elect to declare the debt due and payable (or cancel any unfunded commitments, if applicable) and proceed against the collateral, if any, securing that debt. Borrowings under our other debt instruments that contain cross-default provisions may also be accelerated or become payable on demand, and our assets may not be sufficient to repay such indebtedness in full. Despite our leverage, we may incur more debt in the future.
> g. Increases in fuel costs, changes in the types of fuel consumed and availability of fuel supply may adversely impact our scheduled itineraries and costs.

### CCL-000081509726000007-0081

risk_factors, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 97509–98991

> We have been and may continue to be impacted by economic, market and political conditions around the world, regulatory requirements including emissions-related regulations, supply disruptions and related infrastructure needs, which make it difficult to predict the future cost and availability of fuel. The supply and availability of different fuel types in various markets in which we operate have in the past and may in the future experience increased volatility and lead to increased fuel costs and reduced profitability. Emission penalties and the costs of compliant fuels may also increase our energy costs. Future increases in the global price of fuel would increase the cost of our cruise ship operations as well as some of our other expenses, such as crew travel, freight and commodity prices. Increases in airfares, such as those resulting from increases in the cost of fuel, have in the past and may in the future increase our guests’ overall vacation costs and reduce demand for cruises, as many of our guests depend on airlines to transport them to or from the airports near the ports where our cruises embark and disembark. Refer to Compliance and Regulatory Risk Factor “b.” for additional discussion on emissions-related regulation changes on fuel costs.
> h. The loss of key team members, our inability to recruit or retain qualified shoreside and shipboard team members and increased labor costs could have an adverse effect on our business and results of operations.

### CCL-000081509726000007-0089

risk_factors, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 107465–108886

> Concerns and regulatory focus on sustainability and the impact of GHG and other emissions on the environment have impacted us and may in the future have material impacts on our business and operating results. Sustainability, environmental and emissions-related regulatory activity and developments that require us to reduce our emissions, which includes EU and UK regulations and the IMO Strategy, have impacted us and may in the future have a material impact on our business and financial results by requiring us to make capital investments in new equipment or technologies, pay for emission allowances, purchase carbon offset credits, or otherwise incur additional costs or take additional actions related to our emissions. Such activity has impacted and may continue to impact us indirectly by increasing our operating costs, including fuel costs. Regulatory developments may also result in the inability to operate ships that do not meet certain standards, impact the resale value of our ships in the future, restrict or limit our access to certain destinations and/or countries or impact our freedom to operate. Regulatory efforts, both internationally and in the U.S., are evolving and we cannot determine what final regulations will be enacted, modified, reversed or whether there will be international alignment or divergence of such efforts, or what their ultimate impact on our business will be. Refer to XVIII.

### CCL-000081509726000007-0177

debt_note, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 208308–209696

> Less: unamortized debt issuance costs and discounts (744) (738)
> 58
> Total Debt, net of unamortized debt issuance costs and discounts 26,640 27,475
> Less: current portion of long-term debt (2,603) (1,538)
> Long-Term Debt $ 24,037 $ 25,936
> (a)The reference rates, together with any applicable credit adjustment spread, for all of our floating rate debt have a 0.00% floor.
> (b)See “Debt Prepayments” below.
> (c)As part of the repricing of our senior secured term loans, we amended the loans’ margin from 2.75% to 2.00%. See “Repricing of Senior Secured Term Loans” below.
> (d)See “Convertible Notes” below.
> (e)During 2025, the euro floating rate loan agreement was amended to increase the principal amount by $112 million, extend its maturity from April 2025 to April 2029, amend the loan’s margin from 3.25% to 1.95% and remove the subsidiary guarantee.
> (f)Includes applicable credit adjustment spread.
> As of November 30, 2025, all of our outstanding debt is issued or guaranteed by substantially the same entities with the exception of the $1.8 billion of export credit facilities of Sun Princess Limited and Sun Princess II Limited, which do not guarantee our other outstanding debt.
> As of November 30, 2025, the scheduled maturities of our debt are as follows:
> (in millions)
> Year Principal Payments
> 2026 (a) $ 2,615
> 2027 2,518
> 2028 3,962
> 2029 4,133
> 2030 2,886
> Thereafter 11,268
> Total $ 27,383

### CCL-000081509726000007-0179

debt_note, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 210992–212485

> During 2025, we entered into amendments to reprice the outstanding principal amounts of our first-priority senior secured term loan facility maturing in 2027 and our first-priority senior secured term loan facility maturing in 2028 (“Repriced Loans”), which were included within the total Secured Subsidiary Guaranteed Loans balance in the debt table above. During 2025, the Repriced Loans were prepaid.
> 59
> Issuances and Borrowings
> During 2025, we issued the following senior unsecured notes:
> •$1.3 billion of 5.13% senior unsecured notes due 2029
> •$1.0 billion of 5.75% senior unsecured notes due 2030
> •$1.0 billion of 5.88% senior unsecured notes due 2031
> •$1.2 billion of 4.13% senior unsecured euro notes due 2031
> •$3.0 billion of 5.75% senior unsecured notes due 2032
> •$2.0 billion of 6.13% senior unsecured notes due 2033
> Additionally, we borrowed the following under unsecured term loan facilities maturing in 2027:
> •$0.4 billion bearing interest at a rate per annum equal to SOFR plus 1.13%
> •$0.3 billion bearing interest at a rate per annum equal to SOFR plus 1.25%
> •$0.3 billion bearing interest at a rate per annum equal to SOFR plus 1.38%
> Prepayments
> During 2025, we used proceeds from debt issuances and borrowings, together with cash on hand, to prepay the following debt instruments:
> •7.63% senior unsecured notes due 2026
> •5.75% senior unsecured notes due 2027
> •First-priority senior secured term loan facilities maturing in 2027 and 2028
> •10.38% senior priority notes due 2028

### CCL-000081509726000007-0180

debt_note, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 212486–213309

> •6.00% senior unsecured notes due 2029
> •10.50% senior unsecured notes due 2030
> The aggregate amount of these prepayments was $11.6 billion.
> Debt Extinguishment and Modification Costs
> During 2025, we recognized a total of $409 million of debt extinguishment and modification costs, including $271 million of premium paid on redemption, within our Consolidated Statements of Income (Loss) as a result of the above transactions.
> Export Credit Facility Borrowings
> During 2025, we borrowed $0.8 billion under export credit facilities due in semi-annual installments through 2037. As of November 30, 2025, we had $7.8 billion of undrawn export credit facilities to fund ship deliveries planned through 2033. As of November 30, 2025, the net book value of our ships subject to negative pledges was $19.3 billion.
> Convertible Notes

### CCL-000081509726000007-0183

debt_note, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 215921–216443

> At November 30, 2025, we were in compliance with the applicable covenants under our debt agreements. Generally, if an event of default under any debt agreement occurs, then, pursuant to cross-default and/or cross-acceleration clauses therein, substantially all of our outstanding debt could become due, and our debt could be terminated. Any financial covenant amendment may lead to increased costs, increased interest rates, additional restrictive covenants and other available lender protections that would be applicable.

### CCL-000081509726000007-0222

financial_statements, [10-K for 2025-11-30](https://www.sec.gov/Archives/edgar/data/815097/000081509726000007/ccl-20251130.htm), characters 266966–268461

> As of November 30, 2025, the Company had current debt of $2.6 billion, long-term debt of $24.0 billion, and recorded debt extinguishment and modification costs of $409 million. Debt is recorded at initial fair value, which normally reflects the proceeds received by the Company, net of debt issuance costs. Debt is subsequently stated at amortized cost. Debt issuance costs, discounts and premiums are generally amortized to interest expense using the straight-line method, which approximates the effective interest method, over the term of the debt. Debt issuance costs related to a recognized debt liability are presented as a direct deduction of the carrying amount of that debt, consistent with debt discounts. Debt issuance costs related to the Company’s revolving facility and export credit facilities not yet drawn are deferred and recorded as an asset. Debt issuance costs paid to lenders related to a recognized debt liability are netted against the proceeds from the related debt while debt issuance costs paid to third parties, or related to undrawn credit facilities, are presented separately within financing activities. Debt instruments are also evaluated by the Company for the existence of features that must be separated and accounted for as a derivative. During the year ended November 30, 2025, the Company entered into various debt transactions that involved issuance of new debt, modification and extinguishment of existing debt, and refinancing of existing syndicated debt.

### CCL-000081509726000037-0039

mdna, [10-Q for 2026-02-28](https://www.sec.gov/Archives/edgar/data/815097/000081509726000037/ccl-20260228.htm), characters 52043–53315

> •Overcapacity and competition in the cruise and land-based vacation industry may negatively impact our cruise sales, pricing and destination options.
> •Inability to implement our shipbuilding programs and ship repairs, maintenance and refurbishments may adversely impact our business operations and the satisfaction of our guests.
> •Changes in and non-compliance with laws and regulations under which we operate, such as those relating to health, environment, safety and security, data privacy and protection, anti-money laundering, anti-corruption, economic sanctions, trade protection measures, labor and employment, and tax may be costly and lead to litigation, enforcement actions, fines, penalties and reputational damage.
> •Factors associated with sustainability and the impact of greenhouse gases and other emissions on the environment could have a material impact on our business and operating results.
> •We may not successfully complete the proposed unification of our dual listed company (“DLC”) structure and the migration of Carnival Corporation’s legal incorporation to Bermuda, or, if we do, we may not realize the anticipated benefits and will be subject to Bermuda law, which differs in some respects compared to our current jurisdictions.
> 18
> Table of Contents

### CCL-000081509726000107-0021

debt_note, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/ccl-20260831.htm), characters 26816–28215

> As of August 31, 2026, we had $4.5 billion available for borrowing under the Revolving Facility. We may borrow or utilize available amounts under the Revolving Facility through June 2030, subject to the satisfaction of the conditions in the facility.
> Export Credit Facilities
> As of August 31, 2026, we had $10.7 billion of undrawn export credit facilities to fund ship deliveries planned through 2033. As of August 31, 2026, the net book value of our ships subject to negative pledges was $20.6 billion.
> Convertible Notes
> In December 2025, we settled $1.1 billion principal amount of the 2027 Convertible Notes, resulting in the issuance of 69.1 million shares of Carnival Corporation common stock and a cash payment of $500 million.
> Covenant Compliance
> As of August 31, 2026, the most restrictive covenants for our Revolving Facility, unsecured loans and export credit facilities include the following:
> •Maintain minimum interest coverage (adjusted EBITDA to consolidated net interest charges, as defined in the agreements) at a ratio of not less than 3.0 to 1.0
> •Maintain minimum issued capital and consolidated reserves (as defined in the agreements) of $5.0 billion
> •Limit our debt to capital (as defined in the agreements) percentage to a percentage not to exceed 65%
> •Maintain minimum liquidity of $1.5 billion
> •Limit the amounts of our secured assets as well as secured and other indebtedness

### CCL-000081509726000107-0022

debt_note, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/ccl-20260831.htm), characters 28216–28757

> At August 31, 2026, we were in compliance with the applicable covenants under our debt agreements. Generally, if an event of default under any debt agreement occurs, then, pursuant to cross-default and/or cross-acceleration clauses therein, substantially all of our outstanding debt could become due, and our debt could be terminated. Any financial covenant amendment may lead to increased costs, increased interest rates, additional restrictive covenants and other available lender protections that would be applicable.
> 11
> Table of Contents

### CCL-000081509726000107-0053

liquidity, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/ccl-20260831.htm), characters 69400–70702

> Liquidity, Financial Condition and Capital Resources
> As of August 31, 2026, we had $5.7 billion of liquidity including $1.2 billion of cash and cash equivalents and $4.5 billion available for borrowing under our multicurrency revolving credit facility. In addition, we had $10.7 billion of undrawn export credit facilities to fund future ship deliveries.
> We had a working capital deficit of $9.1 billion and $8.9 billion as of August 31, 2026 and November 30, 2025. We operate with a substantial working capital deficit, largely due to our business model in which guest cruise ticket deposits and the advance purchases of onboard and other services are collected ahead of the sailing date and recorded as a liability until recognized as revenue with a relatively low level of accounts receivable and inventories. These customer deposits are used alongside other cash sources to fund operations, service debt, and support capital investments.
> We are not a party to any off-balance sheet arrangements, including guarantee contracts, retained or contingent interests, certain derivative instruments and variable interest entities that either have, or are reasonably likely to have, a current or future material effect on our consolidated financial statements.
> Sources and Uses of Cash
> Operating Activities

### CCL-000081509726000107-0054

liquidity, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/815097/000081509726000107/ccl-20260831.htm), characters 70703–72158

> Our business provided $5.3 billion of net cash flows from operating activities during the nine months ended August 31, 2026, an increase of $603 million, compared to $4.7 billion provided for the same period in 2025. This was caused by an improvement in our earnings with $2.7 billion of net income in 2026 compared to $2.3 billion of net income in 2025, as well as the nonrecurrence of gains from the sale of one North America segment ship and one Europe segment ship in 2025 and other working capital changes, partially offset by the nonrecurrence of losses on debt extinguishment in 2025.
> Investing Activities
> During the nine months ended August 31, 2026, net cash used in investing activities was $2.2 billion. This was caused by:
> •Capital expenditures of $2.1 billion principally attributable to ship improvements, our ongoing new shipbuilding program and development of our portfolio of exclusive destinations
> •Advances of $50 million to two of our equity method investments
> During the nine months ended August 31, 2025, net cash used in investing activities was $1.8 billion. This was caused by:
> •Capital expenditures of $2.1 billion primarily attributable to ship improvements and developments in our port destinations and exclusive islands
> •Proceeds of $312 million substantially all from the sales of one North America segment ship and one Europe segment ship
> •Advances of $90 million to one of our equity method investments
> Financing Activities

## Run

Run `CCL-20261118T051157Z-GLM-5.3`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 9 calls, 33,580 input (12,800 cached) and 17,487 output tokens, $0.0765, 170s. Verification: 36 calls, 17,483 input (4,608 cached) and 3,640 output tokens, $0.0247, 68s. Prices read 2026-11-17. Raw requests and responses: data/runs/CCL/CCL-20261118T051157Z-GLM-5.3.jsonl.
