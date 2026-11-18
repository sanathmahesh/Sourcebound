# Credit memo: GOODYEAR TIRE & RUBBER CO /OH/ (GT)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4-Pro-0813`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-6**.
Sources: [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm); [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026031866/gt-20260331.htm); [10-Q for 2026-06-30](https://www.sec.gov/Archives/edgar/data/42582/000162828026054032/gt-20260630.htm)

Claims: 34 — 30 supported, 3 partially supported, 1 unsupported. Raw numbers rejected in first drafts: 0; repairs: 3.

## Business profile

1. Goodyear is one of the world's leading tire manufacturers with a broad global footprint across the Americas, Europe, Middle East and Africa, and Asia Pacific.  
   ✅ supported (judge): The passage states Goodyear is one of the world's leading tire manufacturers with a broad global footprint and operations across the Americas, EMEA, and Asia Pacific segments.
   - cites `GT-000162828026006708-0097` ✓: “The Goodyear Tire & Rubber Company is one of the world's leading manufacturers of tires, with one of the most recognizable brand names in the world and operations in most regions of the world.”
   - cites `GT-000162828026006708-0006` ✓: “three operating segments representing our regional tire businesses: Americas; Europe, Middle East and Africa (“EMEA”); and Asia Pacific”
2. The company's principal business is the development, manufacture, distribution and sale of tires and related products for automobiles, trucks, buses, aircraft, motorcycles and farm implements.  
   ✅ supported (judge): The passage states the principal business exactly as claimed and lists automobiles, trucks, buses, aircraft, motorcycles and farm implements among tire lines.
   - cites `GT-000162828026006708-0006` ✓: “Our principal business is the development, manufacture, distribution and sale of tires and related products and services worldwide.”
   - cites `GT-000162828026006708-0006` ✓: “We manufacture and sell numerous lines of rubber tires for:
•automobiles
•trucks
•buses
•aircraft
•motorcycles
•farm implements, and
•various other applications.”
3. Goodyear's revenue was **$20.1 billion** [F1] in the fiscal year ended 31 December 2023, declining to **$18.9 billion** [F2] in the fiscal year ended 31 December 2024, **$18.3 billion** [F3] in the fiscal year ended 31 December 2025, and **$17.6 billion** [F4] in the twelve months to 30 September 2026.  
   ✅ supported (judge): All four revenue figures in the claim match the XBRL-computed metric values exactly.
4. EBITDA fell from **$1.4 billion** [F5] in the fiscal year ended 31 December 2025 to **$990 million** [F6] in the twelve months to 30 September 2026.  
   ✅ supported (judge): Both EBITDA figures match the metric values computed from XBRL data.
5. Goodyear faces significant global competition, and its market share could decline, which may affect the stability of its cash flows.  
   ✅ supported (judge): The risk factor bullet explicitly states Goodyear faces significant global competition and market share could decline, among factors that may cause actual results to differ and affect operating results and financial condition.
   - cites `GT-000162828026006708-0191` ✓: “we face significant global competition and our market share could decline”
6. The company has executed cost reductions and portfolio divestitures to improve leverage and reduce debt, supporting its financial position.  
   ✅ supported (judge): The passage explicitly states cost reduction actions (~$1.5B run-rate benefit) and using divestiture proceeds (~$2.2B) to reduce debt and improve leverage.
   - cites `GT-000162828026006708-0006` ✓: “Executing cost reduction actions driving an annual, run-rate benefit of approximately $1.5 billion”
   - cites `GT-000162828026006708-0006` ✓: “Improving our leverage, utilizing proceeds from divestitures to reduce our debt”

## Financial risk

1. Debt / EBITDA improved from **9.39x** [F7] in the fiscal year ended 31 December 2023 to **7.44x** [F8] in the twelve months to 30 September 2026.  
   ✅ supported (judge): Both metric values match the claim exactly.
2. Net leverage improved from **8.28x** [F9] in the fiscal year ended 31 December 2023 to **6.62x** [F10] in the twelve months to 30 September 2026.  
   ✅ supported (judge): Both metric values (8.28x for FY-2 and 6.62x for LTM) match the claim, showing improvement.
3. EBITDA / interest improved from **1.53x** [F11] in the fiscal year ended 31 December 2023 to **2.39x** [F12] in the twelve months to 30 September 2026.  
   ✅ supported (judge): The claimed values match the computed metric values exactly for both periods.
4. FCF / debt remained stable from the fiscal year ended 31 December 2023 to the twelve months to 30 September 2026, with **-0.2%** [F13] in the fiscal year ended 31 December 2023 and **1.2%** [F14] in the twelve months to 30 September 2026.  
   ✅ supported (judge): The metric values exactly match the claim: FCF/debt was -0.2% in FY2023 and 1.2% in the twelve months to 30 September 2026, both near zero and thus consistent with stability.
5. The improvement in leverage and interest coverage from the fiscal year ended 31 December 2023 through the fiscal year ended 31 December 2025 was driven by debt repayment with asset sale proceeds and lower interest expense on lower average debt, while net borrowings and lower segment operating income in early **2026** [quoted: GT-000162828026031866-0099] partially reversed the improvement into the twelve months to 30 September 2026.  
   ◐ partially supported (judge): The evidence supports the 2024-2025 debt repayment with asset sale proceeds, lower interest expense from lower average debt, early-2026 net borrowings, and lower segment operating income, but it does not cover fiscal 2023 leverage/interest coverage, actual leverage/interest coverage metrics, or the twelve months to 30 September 2026.
   - cites `GT-000162828026006708-0132` ✓: “Net cash used by financing activities was $1,770 million, primarily due to net debt repayments of $1,759 million.”
   - cites `GT-000162828026006708-0116` ✓: “The decrease is due to lower interest rates on lower average debt levels in 2025, due to the repayment of debt with proceeds from asset sales.”
   - cites `GT-000162828026031866-0099` ✓: “primarily related to net borrowings of $807 million in the first three months of 2026”
   - cites `GT-000162828026031866-0086` ✓: “a decrease of $100 million, or 51.3%, from $195 million in the first quarter of 2025”
6. FCF / debt stability was supported by lower capital expenditures in the fiscal year ended 31 December 2025 compared with the fiscal year ended 31 December 2024, along with asset sale proceeds, while lower segment operating income partially offset the benefit.  
   ✅ supported (judge): All parts are supported: capex fell from $1,188 million to $826 million, asset sales provided $1,802 million, and lower segment operating income ($245 million decrease) partially offset operating cash flow benefits.
   - cites `GT-000162828026006708-0137` ✓: “Capital expenditures were $826 million in 2025, compared to $1,188 million in 2024.”
   - cites `GT-000162828026006708-0132` ✓: “proceeds from the sales of the OTR tire business, the Dunlop brand and the Chemical Business”
   - cites `GT-000162828026006708-0123` ✓: “Total segment operating income in 2025 was $1,057 million, a decrease of $245 million, or 18.8%, from $1,302 million in 2024.”

## Liquidity

1. In the twelve months to 30 September 2026, liquidity coverage was **0.78x** [F15], compared with **0.94x** [F16] in the fiscal year ended 31 December 2025.  
   ✅ supported (judge): Both metric values (0.78x LTM to 30 Sep 2026 and 0.94x FY ended 31 Dec 2025) match the claim exactly.
2. At December **31** [quoted: GT-000162828026006708-0133], **2025** [quoted: GT-000162828026006708-0133], the company had $**4,421** [quoted: GT-000162828026006708-0133] million of unused availability under its various credit agreements.  
   ✅ supported (judge): The passage directly states $4,421 million of unused availability at December 31, 2025.
   - cites `GT-000162828026006708-0133` ✓: “At December 31, 2025 and 2024, we had $4,421 million and $3,555 million, respectively, of unused availability under our various credit agreements.”
3. At March **31** [quoted: GT-000162828026031866-0094], **2026** [quoted: GT-000162828026031866-0094], unused availability under the company's various credit agreements was $**2,975** [quoted: GT-000162828026031866-0094] million, compared with $**4,421** [quoted: GT-000162828026031866-0094] million at December **31** [quoted: GT-000162828026031866-0094], **2025** [quoted: GT-000162828026031866-0094].  
   ✅ supported (judge): Passage states exactly these unused availability figures at both dates.
   - cites `GT-000162828026031866-0094` ✓: “At March 31, 2026, we had $2,975 million of unused availability under our various credit agreements, compared to $4,421 million at December 31, 2025.”
4. The company has an €**800** [quoted: GT-000162828026070703-0047] million Amended and Restated Senior Secured European Revolving Credit Facility due **2028** [quoted: GT-000162828026070703-0047].  
   ✅ supported (judge): The evidence passage explicitly names the €800 million Amended and Restated Senior Secured European Revolving Credit Facility due 2028.
   - cites `GT-000162828026070703-0047` ✓: “€800 million Amended and Restated Senior Secured European Revolving Credit Facility due 2028”
5. Management stated that it believes the company's liquidity position is adequate to fund its operating and investing needs and debt maturities for the next twelve months.  
   ✅ supported (judge): The passage directly states management's belief that liquidity is adequate to fund operating and investing needs and debt maturities for the next twelve months.
   - cites `GT-000162828026006708-0133` ✓: “We believe that our liquidity position is adequate to fund our operating and investing needs and debt maturities for the next twelve months”
6. In the twelve months to 30 September 2026, cash and cash equivalents were **$812 million** [F17], cash from operations was **$748 million** [F18], capital expenditures were **$658 million** [F19], dividends paid were **$0** [F20], and short-term debt was **$1.3 billion** [F21].  
   ✅ supported (judge): All five figures match the XBRL-computed metric values exactly.

## Maturity wall

1. Debt maturities over the next five years are **$1.2 billion** [F22], **$1.0 billion** [F23], **$802 million** [F24], **$864 million** [F25], and **$506 million** [F26] for years one through five, respectively.  
   ✅ supported (judge): All five maturity values in the claim exactly match the XBRL-computed metric values for years one through five.
2. The share of total debt due within 24 months is **30.7%** [F27], or **$1.9 billion** [F28] out of **$6.2 billion** [F29].  
   ❌ unsupported (deterministic): unsupported: number check failed: number not from a placeholder or a cited passage: 24
   - flag: kept after failed repair: number not from a placeholder or a cited passage: 24
3. Near-term maturity cover is **2.38x** [F30], computed with cash of **$801 million** [F31] and assuming zero undrawn revolver and zero short-term investments.  
   ✅ supported (judge): The claim matches the computed metric (2.38x) and the cash figure ($801 million), with the same assumptions of zero short-term investments and zero undrawn revolver.
4. As of the twelve months to 30 September 2026, the company was in compliance with the financial covenant applicable to GEBV and its subsidiaries under the European revolving credit facility and the pan-European accounts receivable securitization facility.  
   ✅ supported (judge): The filing states that the financial covenant applicable to GEBV and its subsidiaries is included in both the European revolving credit facility and the pan-European accounts receivable securitization facility, and that the company was in compliance with it at September 30, 2026.
   - cites `GT-000162828026070703-0135` ✓: “At September 30, 2026, we were in compliance with this financial covenant.”
5. Management believes the company's liquidity position is adequate to fund operating and investing needs and debt maturities for the next twelve months.  
   ✅ supported (judge): The claim is stated verbatim in the filing's liquidity discussion.
   - cites `GT-000162828026070703-0119` ✓: “We believe that our liquidity position is adequate to fund our operating and investing needs and debt maturities for the next twelve months”

## Key risks

1. The company's substantial debt burden could make it more difficult to satisfy its obligations and impair its ability to obtain financing in the future.  
   ✅ supported (judge): The passage directly states the substantial debt could make it more difficult to satisfy obligations and impair ability to obtain future financing.
   - cites `GT-000162828026006708-0063` ✓: “We have a substantial amount of debt.”
   - cites `GT-000162828026006708-0063` ✓: “impair our ability to obtain financing in the future for working capital, capital expenditures, research and development, acquisitions or general corporate requirements”
2. The company's access to capital markets cannot be assured, and its liquidity depends on continued availability of third-party financing and supplier financing and accounts receivable factoring programs.  
   ✅ supported (judge): The passage states access to capital markets cannot be assured, and that liquidity depends on third-party financing and continued use of supplier financing and accounts receivable factoring programs.
   - cites `GT-000162828026006708-0062` ✓: “Our access to the capital markets cannot be assured and is dependent on, among other things, the ability and willingness of financial institutions to extend credit”
   - cites `GT-000162828026006708-0062` ✓: “If these programs become unavailable or less attractive to us or our suppliers, our liquidity could be adversely affected.”
3. Automotive production and sales are highly cyclical, and declines in new vehicle production or sales could reduce the company's sales volume and result in under-absorbed fixed costs at production facilities.  
   ✅ supported (judge): The passage explicitly states automotive production and sales are highly cyclical and that declines in new vehicle production/sales could cause under-absorbed fixed costs at production facilities.
   - cites `GT-000162828026006708-0054` ✓: “Automotive production and sales are highly cyclical and sensitive to general economic conditions and other factors”
   - cites `GT-000162828026006708-0054` ✓: “which could result in us incurring under-absorbed fixed costs at our production facilities”
4. Higher interest rates would increase debt service obligations on the company's variable-rate borrowings, requiring more available cash to service its indebtedness.  
   ✅ supported (judge): The passage directly states that increased interest rates would raise debt service obligations on variable-rate borrowings and require more available cash.
   - cites `GT-000162828026006708-0069` ✓: “If interest rates increase, our debt service obligations on the variable rate indebtedness would increase even though the amount borrowed remained the same”
   - cites `GT-000162828026006708-0069` ✓: “which would require us to use more of our available cash to service our indebtedness”
5. Tariff changes and other trade restrictions could reduce flexibility to use the company's global manufacturing footprint, increase supplier costs, and weaken demand in key markets.  
   ✅ supported (judge): The passage explicitly states tariffs may reduce flexibility to use the global manufacturing footprint, increased supplier costs, and could weaken demand in key markets.
   - cites `GT-000162828026006708-0049` ✓: “may reduce our flexibility to utilize our global manufacturing footprint to meet demand for our tires around the world”
   - cites `GT-000162828026006708-0049` ✓: “Broad-based tariffs and other trade restrictions have resulted in increased costs for our suppliers”
   - cites `GT-000162828026006708-0049` ✓: “tariffs and other trade restrictions may weaken the economies of key markets for us”

## Rating rationale

1. The SB grade is **SB-6** [F32], a stylized internal scorecard grade, not a credit rating, and reflects a weighted score of **5.55** [F33]; the grade is not provisional because all six factors were scored.  
   ✅ supported (judge): The metric values confirm grade SB-6, weighted score 5.55, stylized not a credit rating, and not provisional since all six factors were scored.
2. Debt / EBITDA of **7.44x** [F8] falls in scorecard band **6** [F34] with a weight of **20.0%** [F35], and net leverage of **6.62x** [F10] falls in scorecard band **6** [F36] with a weight of **10.0%** [F37].  
   ✅ supported (judge): Metric values match: Debt/EBITDA 7.44x in band 6 with 20.0% weight, net leverage 6.62x in band 6 with 10.0% weight.
3. Liquidity coverage of **0.78x** [F15] falls in scorecard band **6** [F38] with a weight of **15.0%** [F39], and near-term maturity cover of **2.38x** [F30] falls in scorecard band **6** [F40] with a weight of **10.0%** [F41].  
   ✅ supported (judge): Both metric values (0.78x and 2.38x) and their scorecard bands (6) and weights (15.0% and 10.0%) match the computed evidence exactly.
4. EBITDA / interest of **2.39x** [F12] falls in scorecard band **5** [F42] with a weight of **25.0%** [F43], and FCF / debt of **1.2%** [F14] falls in scorecard band **5** [F44] with a weight of **20.0%** [F45], making them the relatively strongest scorecard factors.  
   ◐ partially supported (judge): The values, bands (5) and weights (25.0%, 20.0%) are confirmed, but calling them 'the relatively strongest scorecard factors' is misleading: band 1 is strongest and band 6 weakest, so band 5 is the second-weakest band, merely slightly better than the four factors in band 6.
5. The company has executed cost reductions and portfolio divestitures to improve leverage and reduce debt, which supports the improvement in leverage metrics but does not offset the weak scorecard bands.  
   ◐ partially supported (judge): The passage confirms cost reductions, divestitures, and debt reduction actions, and the scorecard confirms weak leverage bands, but the evidence does not show that leverage metrics actually improved.
   - cites `GT-000162828026006708-0006` ✓: “Improving our leverage, utilizing proceeds from divestitures to reduce our debt”
6. Management believes the company's liquidity position is adequate to fund operating and investing needs and debt maturities for the next twelve months, which tempers the weakest liquidity-related scorecard bands, while a substantial debt burden and cyclical and trade-related risks temper the overall assessment.  
   ✅ supported (judge): The management liquidity statement, substantial debt burden, and cyclical/trade risks are all directly stated in the passages, and the scorecard confirms liquidity_coverage and near_term_maturity_cover sit in band 6 of 6 (the weakest bands), consistent with the claim's framing.
   - cites `GT-000162828026006708-0133` ✓: “our liquidity position is adequate to fund our operating and investing needs and debt maturities for the next twelve months”
   - cites `GT-000162828026006708-0063` ✓: “We have a substantial amount of debt”
   - cites `GT-000162828026006708-0054` ✓: “Automotive production and sales are highly cyclical”
   - cites `GT-000162828026006708-0049` ✓: “changes in tariffs, trade agreements or other trade restrictions”

## Reviewer checklist

- [ ] **not available** (warning): Debt maturing after year five not available in FY0: no candidate tag is reported (see the log).
- [ ] **fallback** (info): Revenue: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Operating income: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Total debt (borrowings plus finance-lease liabilities): used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Dividends paid: used rank 2 PaymentsOfDividendsCommonStock in FY-2, FY-1, FY0.
- [ ] **fallback** (info): Interest expense: used rank 2 InterestExpenseNonoperating in FY0, LTM.
- [ ] **assumed zero** (info): Short-term investments assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Dividends paid assumed zero (not reported) in LTM.
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The evidence supports the 2024-2025 debt repayment with asset sale proceeds, lower interest expense from lower average debt, early-2026 net borrowings, and lower segment operating income, but it does not cover fiscal 2023 leverage/interest coverage, actual leverage/interest coverage metrics, or the twelve months to 30 September 2026.): “The improvement in leverage and interest coverage from the fiscal year ended 31 December 2023 through the fiscal year ended 31 December 2025 was driven by debt repayment with asset sale proceeds and lower interest expense on lower average debt, while net borrowings and lower segment operating income in early 2026 partially reversed the improvement into the twelve months to 30 September 2026.”
- [ ] **unsupported claim** (warning): Maturity wall: unsupported (unsupported: number check failed: number not from a placeholder or a cited passage: 24): “The share of total debt due within 24 months is 30.7%, or $1.9 billion out of $6.2 billion.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The values, bands (5) and weights (25.0%, 20.0%) are confirmed, but calling them 'the relatively strongest scorecard factors' is misleading: band 1 is strongest and band 6 weakest, so band 5 is the second-weakest band, merely slightly better than the four factors in band 6.): “EBITDA / interest of 2.39x falls in scorecard band 5 with a weight of 25.0%, and FCF / debt of 1.2% falls in scorecard band 5 with a weight of 20.0%, making them the relatively strongest scorecard factors.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The passage confirms cost reductions, divestitures, and debt reduction actions, and the scorecard confirms weak leverage bands, but the evidence does not show that leverage metrics actually improved.): “The company has executed cost reductions and portfolio divestitures to improve leverage and reduce debt, which supports the improvement in leverage metrics but does not offset the weak scorecard bands.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $20.1 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 20,066,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F2 | Revenue (revenue:FY-1) | $18.9 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 18,878,000,000 (2024-01-01 to 2024-12-31, FY-1) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F3 | Revenue (revenue:FY0) | $18.3 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 18,280,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F4 | Revenue (revenue:LTM) | $17.6 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 18,280,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 12,671,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 13,363,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F5 | EBITDA (ebitda:FY0) | $1.4 billion | operating_income + d_and_a | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -133,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpenseNonoperating 445,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>DepreciationDepletionAndAmortization 1,045,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F6 | EBITDA (ebitda:LTM) | $990 million | operating_income + d_and_a | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -133,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -552,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -297,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 445,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpenseNonoperating 311,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 341,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DepreciationDepletionAndAmortization 1,045,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>DepreciationDepletionAndAmortization 731,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY-2) | 9.39x | total_debt / EBITDA | LongTermDebtAndCapitalLeaseObligations 6,831,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>DebtCurrent 793,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -721,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpense 532,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>DepreciationDepletionAndAmortization 1,001,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:LTM) | 7.44x | total_debt / EBITDA | LongTermDebtAndCapitalLeaseObligations 6,030,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DebtCurrent 1,339,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -133,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -552,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -297,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 445,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpenseNonoperating 311,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 341,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F9 | Net leverage (net_leverage:FY-2) | 8.28x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtAndCapitalLeaseObligations 6,831,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>DebtCurrent 793,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 902,000,000 (at 2023-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -721,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpense 532,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>DepreciationDepletionAndAmortization 1,001,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F10 | Net leverage (net_leverage:LTM) | 6.62x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtAndCapitalLeaseObligations 6,030,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DebtCurrent 1,339,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 812,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -133,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -552,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -297,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 445,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpenseNonoperating 311,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F11 | EBITDA / interest (interest_coverage:FY-2) | 1.53x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -721,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpense 532,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>DepreciationDepletionAndAmortization 1,001,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpense 532,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm) |
| F12 | EBITDA / interest (interest_coverage:LTM) | 2.39x | EBITDA / interest_expense | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -133,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -552,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest -297,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 445,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>InterestExpenseNonoperating 311,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>InterestExpenseNonoperating 341,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DepreciationDepletionAndAmortization 1,045,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>DepreciationDepletionAndAmortization 731,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F13 | FCF / debt (fcf_to_debt:FY-2) | -0.2% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 1,032,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 1,050,000,000 (2023-01-01 to 2023-12-31, FY-2) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>LongTermDebtAndCapitalLeaseObligations 6,831,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm)<br>DebtCurrent 793,000,000 (at 2023-12-31, balance sheet) [10-K 0000950170-25-020763](https://www.sec.gov/Archives/edgar/data/42582/000095017025020763/0000950170-25-020763-index.htm) |
| F14 | FCF / debt (fcf_to_debt:LTM) | 1.2% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 796,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -764,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -716,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 826,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 481,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 649,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>LongTermDebtAndCapitalLeaseObligations 6,030,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DebtCurrent 1,339,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F15 | Liquidity coverage (liquidity_coverage:LTM) | 0.78x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 812,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 796,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -764,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -716,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DebtCurrent 1,339,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 826,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 481,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 649,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F16 | Liquidity coverage (liquidity_coverage:FY0) | 0.94x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 801,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 796,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>DebtCurrent 870,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 826,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>PaymentsOfDividendsCommonStock 0 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F17 | Cash and cash equivalents (cash:LTM) | $812 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 812,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F18 | Cash from operations (cfo:LTM) | $748 million | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 796,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -764,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>NetCashProvidedByUsedInOperatingActivities -716,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F19 | Capital expenditure (capex:LTM) | $658 million | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 826,000,000 (2025-01-01 to 2025-12-31, FY0) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 481,000,000 (2026-01-01 to 2026-09-30, current year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 649,000,000 (2025-01-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F20 | Dividends paid (dividends:LTM) | $0 |  | — |
| F21 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $1.3 billion | rank 1: DebtCurrent | DebtCurrent 1,339,000,000 (at 2026-09-30, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F22 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $1.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 1,183,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F23 | Debt maturing in year two (maturity_year_2:FY0) | $1.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 1,035,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F24 | Debt maturing in year three (maturity_year_3:FY0) | $802 million | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 802,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F25 | Debt maturing in year four (maturity_year_4:FY0) | $864 million | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 864,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F26 | Debt maturing in year five (maturity_year_5:FY0) | $506 million | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 506,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F27 | Share of debt due within 24 months (share_due_24m:FY0) | 30.7% | (short_term_debt + maturity_year_2) / total_debt | DebtCurrent 870,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 1,035,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>LongTermDebtAndCapitalLeaseObligations 5,328,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DebtCurrent 870,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F28 | Debt due within 24 months (debt_due_24m:FY0) | $1.9 billion | short_term_debt + maturity_year_2 | DebtCurrent 870,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 1,035,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm) |
| F29 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $6.2 billion | rank 2: LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | LongTermDebtAndCapitalLeaseObligations 5,328,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>DebtCurrent 870,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F30 | Near-term maturity cover (near_term_maturity_cover:FY0) | 2.38x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | DebtCurrent 870,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 1,035,000,000 (at 2025-12-31, balance sheet) [10-K 0001628280-26-006708](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/0001628280-26-006708-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 801,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F31 | Cash and cash equivalents (cash:FY0) | $801 million | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 801,000,000 (at 2025-12-31, balance sheet) [10-Q 0001628280-26-070703](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/0001628280-26-070703-index.htm) |
| F32 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 5.55 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F33 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 5.55 | sum of weight x band over the factors scored, divided by their weights | — |
| F34 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 6 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F35 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F36 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 6 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F37 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F38 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F39 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F40 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 6 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F41 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F42 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 5 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F43 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F44 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 5 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F45 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### GT-000162828026006708-0006

business, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 8055–9321

> •Delivering gross proceeds of approximately $2.2 billion from portfolio optimization by completing the sales of our off-the-road (“OTR”) tire business, the Dunlop brand and our polymer chemicals business during 2025;
> •Executing cost reduction actions driving an annual, run-rate benefit of approximately $1.5 billion, including actions related to our manufacturing footprint, plant optimization, further improvement of our purchasing leverage, reduction of Selling, Administrative and General expenses (“SAG”) and improvements in our supply chain planning and logistics;
> •Engaging in brand optimization and tiering; and
> •Improving our leverage, utilizing proceeds from divestitures to reduce our debt.
> GENERAL INFORMATION REGARDING OUR SEGMENTS
> For the year ended December 31, 2025, we operated our business through three operating segments representing our regional tire businesses: Americas; Europe, Middle East and Africa (“EMEA”); and Asia Pacific.
> Our principal business is the development, manufacture, distribution and sale of tires and related products and services worldwide. We manufacture and sell numerous lines of rubber tires for:
> •automobiles
> •trucks
> •buses
> •aircraft
> •motorcycles
> •farm implements, and
> •various other applications.
> 1
> Table of Contents

### GT-000162828026006708-0049

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 57935–59420

> We have been, and could continue to be, negatively impacted by changes in tariffs, trade agreements or other trade restrictions on imported tires, raw materials and other goods or equipment.
> The maintenance of existing tariffs, the imposition of new tariffs, changes in existing tariff rates, changes in or the repeal of trade agreements or other trade restrictions, such as those the United States has considered with respect to Canada and Mexico, may reduce our flexibility to utilize our global manufacturing footprint to meet demand for our tires around the world. In addition, the imposition of tariffs in the United States may result in the tires subject to such tariffs being diverted to other regions of the world, such as Europe, Latin America or Asia, or in retaliatory tariffs or other actions by affected countries. Broad-based tariffs and other trade restrictions have resulted in increased costs for our suppliers who have, and may in the future, increase prices to us. Finally, tariffs and other trade restrictions may weaken the economies of key markets for us, such as China, resulting in lower economic growth rates and weakened demand for our products and services. These factors, individually or together, could materially adversely affect our results of operations, financial condition and liquidity.
> 12
> Table of Contents
> Our international operations have certain risks that may materially adversely affect our operating results, financial condition and liquidity.

### GT-000162828026006708-0054

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 63805–65024

> Automotive vehicle production and global tire industry demand continues to be difficult to predict. Although sales to our OE customers accounted for approximately 19% of our net sales in 2025, demand for our products by OE customers and production levels at our facilities are impacted by automotive vehicle production. Automotive production and sales are highly cyclical and sensitive to general economic conditions and other factors, such as credit availability, interest rates, tariffs, fuel prices, and consumer preference and confidence. Economic declines that result in a significant reduction in automotive production would have an adverse effect on our sales to OE customers. We may experience future declines in sales volume due to declines in new vehicle production and sales, the performance, discontinuation or sale of certain OE brands, platforms or programs, increased competition, or weakness in the demand for replacement tires, which could result in us incurring under-absorbed fixed costs at our production facilities or slowing the rate at which we are able to recover those costs. At various times, some regions around the world may be more particularly impacted by these factors than other regions.

### GT-000162828026006708-0062

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 73311–74726

> Risks Related to Our Capital Structure
> Our long-term ability to meet our obligations, to repay maturing indebtedness or to implement strategic initiatives may be dependent on our ability to access capital markets in the future and to improve our operating results.
> The adequacy of our liquidity depends on our ability to achieve an appropriate combination of operating improvements, financing from third parties and access to capital markets. We may need to undertake additional financing actions in the capital markets in order to ensure that our future liquidity requirements are addressed or to implement strategic initiatives. These actions may include the issuance of additional debt or equity, or the factoring of our accounts receivable.
> Our access to the capital markets cannot be assured and is dependent on, among other things, the ability and willingness of financial institutions to extend credit on terms that are acceptable to us or our suppliers, or to honor future draws on our existing lines of credit, and the degree of success we have in implementing our strategic initiatives. We have continued our use of supplier financing programs and the factoring of our accounts receivable in order to improve our working capital
> 15
> Table of Contents
> efficiency and reduce our costs. If these programs become unavailable or less attractive to us or our suppliers, our liquidity could be adversely affected.

### GT-000162828026006708-0063

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 74727–76190

> Future liquidity requirements, or our inability to access cash deposits or make draws on our lines of credit, also may make it necessary for us to incur additional debt. A substantial portion of our assets is subject to liens securing our indebtedness. As a result, we are limited in our ability to pledge our remaining assets as security for additional secured indebtedness.
> Our inability to access the capital markets or incur additional debt in the future could have a material adverse effect on our liquidity and operations, and could require us to consider further measures, including deferring planned capital expenditures, reducing discretionary spending, selling additional assets and restructuring existing debt.
> We have a substantial amount of debt, which could restrict our growth, place us at a competitive disadvantage or otherwise materially adversely affect our financial health.
> We have a substantial amount of debt. As of December 31, 2025, our debt (including finance leases) on a consolidated basis was approximately $6.2 billion. Our substantial amount of debt and other obligations could have important consequences. For example, it could:
> •make it more difficult for us to satisfy our obligations;
> •impair our ability to obtain financing in the future for working capital, capital expenditures, research and development, acquisitions or general corporate requirements;
> •increase our vulnerability to adverse economic and industry conditions;

### GT-000162828026006708-0069

risk_factors, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 81883–82726

> Certain of our borrowings are at variable rates of interest and expose us to interest rate risk. If interest rates increase, our debt service obligations on the variable rate indebtedness would increase even though the amount borrowed remained the same, which would require us to use more of our available cash to service our indebtedness. There can also be no assurance that we will be able to enter into swap agreements or other hedging arrangements in the future if we desire to do so, or that any existing or future hedging arrangements will offset increases in interest rates. As of December 31, 2025, we had approximately $1.2 billion of variable rate debt outstanding.
> Risks Related to Information Technology and Intellectual Property
> We may be adversely affected by any disruption in, or failure of, our information technology systems.

### GT-000162828026006708-0097

mdna, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 112710–113791

> ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS.
> All per share amounts are diluted and refer to Goodyear net income (loss).
> OVERVIEW
> The Goodyear Tire & Rubber Company is one of the world’s leading manufacturers of tires, with one of the most recognizable brand names in the world and operations in most regions of the world. We have a broad global footprint with 49 manufacturing facilities in 19 countries, including the United States. We operate our business through three operating segments representing our regional tire businesses: Americas; Europe, Middle East and Africa ("EMEA"); and Asia Pacific.
> This management's discussion and analysis provides comparisons of material changes in the consolidated financial statements for the years ended December 31, 2025 and 2024. For a comparison of the years ended December 31, 2024 and 2023, refer to Management's Discussion and Analysis of Financial Condition and Results of Operations included in our Annual Report on Form 10-K for the year ended December 31, 2024.
> Goodyear Forward

### GT-000162828026006708-0116

mdna, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 133410–134736

> For further information, refer to Note to the Consolidated Financial Statements No. 4, Costs Associated with Rationalization Programs.
> Goodwill and Intangible Asset Impairment
> During 2025, we recorded a non-cash impairment charge of $674 million ($674 million after-tax and minority) to fully impair our North America reporting unit's goodwill in our Americas segment. During 2024, we recorded a non-cash impairment charge of $125 million ($94 million after-tax and minority) primarily related to our lower tier indefinite-lived intangible assets related to the acquisition of Cooper Tire as a result of increased competition from lower tier imports in the market. For further information, refer to "Critical Accounting Policies - Goodwill and Intangible Assets" and Notes to the Consolidated Financial Statements No. 12, Goodwill and Intangible Assets, in this Form 10-K.
> Interest Expense
> Interest expense was $445 million in 2025, decreasing $77 million from $522 million in 2024. The decrease is due to lower interest rates on lower average debt levels in 2025, due to the repayment of debt with proceeds from asset sales. The average interest rate was 5.76% in 2025 compared to 6.24% in 2024. The average debt balance was $7,729 million in 2025 compared to $8,368 million in 2024.
> 29
> Table of Contents
> Gains on Asset Sales

### GT-000162828026006708-0123

mdna, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 141974–143201

> Segment information reflects our strategic business units ("SBUs"), which are organized to meet customer requirements and global competition and are segmented on a regional basis.
> Results of operations are measured based on net sales to unaffiliated customers and segment operating income. Each segment exports tires to other segments. The financial results of each segment exclude sales of tires exported to other segments, but include operating income derived from such transactions. Segment operating income is computed as follows: Net Sales less CGS (excluding asset write-offs, accelerated depreciation charges and accelerated lease costs) and SAG (including certain allocated corporate administrative expenses). Segment operating income also includes certain royalties and equity in earnings of most affiliates. Segment operating income does not include net rationalization charges, asset sales, goodwill and intangible asset impairment charges and certain other items.
> Total segment operating income in 2025 was $1,057 million, a decrease of $245 million, or 18.8%, from $1,302 million in 2024. Total segment operating margin (segment operating income divided by segment sales) in 2025 was 5.8% compared to 6.9% in 2024.

### GT-000162828026006708-0132

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 152069–153341

> LIQUIDITY AND CAPITAL RESOURCES
> Overview
> Our primary sources of liquidity are cash generated from our operating and financing activities. Our cash flows from operating activities are driven primarily by our operating results and changes in our working capital requirements and our cash flows from financing activities are dependent upon our ability to access credit or other capital. In 2025, we also improved our liquidity position through our Goodyear Forward portfolio optimization initiatives by completing the sales of the OTR tire business, the Dunlop brand and the Chemical Business.
> At December 31, 2025, we had $801 million of Cash and Cash Equivalents, compared to $810 million at December 31, 2024. Net cash used by financing activities was $1,770 million, primarily due to net debt repayments of $1,759 million. Cash provided by investing activities was $997 million, primarily representing proceeds from the sales of the OTR tire business, the Dunlop brand and the Chemical Business, as well as other asset dispositions, of $1,802 million, partially offset by capital expenditures of $826 million. Net cash provided by operating activities was $796 million, driven by our current year segment operating income and deferred revenue and income from asset sales.

### GT-000162828026006708-0133

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 153342–154783

> At December 31, 2025 and 2024, we had $4,421 million and $3,555 million, respectively, of unused availability under our various credit agreements. The table below provides unused availability by our significant credit facilities as of December 31:
> (In millions) 2025 2024
> First lien revolving credit facility $ 2,749 $ 2,049
> European revolving credit facility 940 832
> Chinese credit facilities 531 500
> Other foreign and domestic debt 201 174
> $ 4,421 $ 3,555
> We expect our 2026 cash flow requirements to include capital expenditures of approximately $825 million. We also expect interest expense to be $400 million to $425 million. We estimate rationalization payments to be approximately $225 million; income tax payments to be $150 million to $175 million, excluding one-time items; and contributions to our funded pension plans to be $25 million to $50 million. We expect to generate approximately $100 million of cash from working capital in 2026.
> We actively monitor our liquidity and intend to operate our business in a way that allows us to address our cash flow needs with our existing cash and available credit if they cannot be funded by cash generated from operating or other financing activities. We believe that our liquidity position is adequate to fund our operating and investing needs and debt maturities for the next twelve months and to provide us with the ability to respond to further changes in the business environment.

### GT-000162828026006708-0137

liquidity, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 158476–159962

> Net cash provided by operating activities was $796 million in 2025, compared to $698 million in 2024. The $98 million increase in net cash provided by operating activities was primarily due to $486 million of deferred revenue and income related to the product supply agreements, trademark licensing agreements and transition agreements entered into in connection with the sales of the OTR tire business, the Dunlop brand and the Chemical Business and a decrease in cash payments for interest of $101 million, partially offset by lower earnings in our SBUs of $245 million and an increase in rationalization payments of $233 million.
> The net decrease in cash used for working capital of $36 million reflects an increase in cash provided by Accounts Receivable of $88 million and a decrease in cash used for Inventories of $118 million, partially offset by an increase in cash used for Accounts Payable - Trade of $170 million.
> Investing Activities
> Net cash provided by investing activities was $997 million in 2025, compared to net cash used for investing activities of $1,005 million in 2024. The $2,002 million increase in cash provided by investing activities was primarily due to net cash provided by the sales of the OTR tire business, the Dunlop brand and the Chemical Business, as well as other asset dispositions, of $1,802 million in 2025, compared to $115 million in 2024. Capital expenditures were $826 million in 2025, compared to $1,188 million in 2024.
> Financing Activities

### GT-000162828026006708-0191

mdna, [10-K for 2025-12-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026006708/gt-20251231.htm), characters 222364–223742

> Certain information in this Annual Report on Form 10-K (other than historical data and information) may constitute forward-looking statements regarding events and trends that may affect our future operating results and financial position. The words “estimate,” “expect,” “intend” and “project,” as well as other words or expressions of similar meaning, are intended to identify forward-looking statements. You are cautioned not to place undue reliance on forward-looking statements, which speak only as of the date of this Annual Report on Form 10-K. Such statements are based on current expectations and assumptions, are inherently uncertain, are subject to risks and should be viewed with caution. Actual results and experience may differ materially from the forward-looking statements as a result of many factors, including:
> •if we do not successfully implement our strategic initiatives, our operating results, financial condition and liquidity may be materially adversely affected;
> •our ongoing obligations to the purchasers of our OTR tire business, the Dunlop brand and our Chemical Business may disrupt our current and future plans or operations;
> •we face significant global competition and our market share could decline;
> •our capital expenditures may not be adequate to maintain our competitive position and may not be implemented in a timely or cost-effective manner;

### GT-000162828026031866-0086

mdna, [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026031866/gt-20260331.htm), characters 104422–105483

> Results of operations are measured based on net sales to unaffiliated customers and segment operating income. Each segment exports tires to other segments. The financial results of each segment exclude sales of tires exported to other segments, but include operating income derived from such transactions. Segment operating income is computed as follows: Net Sales less CGS (excluding asset write-off and accelerated depreciation charges) and SAG (including certain allocated corporate administrative expenses). Segment operating income also includes certain royalties and equity in earnings of most affiliates.
> 29
> Table of Contents
> Segment operating income does not include net rationalization charges, asset sales, goodwill and other impairment charges, and certain other items.
> Total segment operating income for the first quarter of 2026 was $95 million, a decrease of $100 million, or 51.3%, from $195 million in the first quarter of 2025. Total segment operating margin in the first quarter of 2026 was 2.4%, compared to 4.6% in the first quarter of 2025.

### GT-000162828026031866-0094

liquidity, [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026031866/gt-20260331.htm), characters 112986–114412

> LIQUIDITY AND CAPITAL RESOURCES
> Our primary sources of liquidity are cash generated from our operating and financing activities. Our cash flows from operating activities are driven primarily by our operating results and changes in our working capital requirements and our cash flows from financing activities are dependent upon our ability to access credit or other capital.
> At March 31, 2026, we had $723 million in cash and cash equivalents, compared to $801 million at December 31, 2025. For the three months ended March 31, 2026, net cash used for operating activities was $718 million, reflecting the Company's cash used for working capital of $650 million and rationalization payments of $83 million. Net cash used for investing activities was $174 million, primarily representing capital expenditures of $175 million. Net cash provided by financing activities was $820 million, primarily due to net borrowings of $807 million.
> 31
> Table of Contents
> At March 31, 2026, we had $2,975 million of unused availability under our various credit agreements, compared to $4,421 million at December 31, 2025. The table below presents unused availability under our credit facilities at those dates:
> (In millions) March 31,
> 2026 December 31,
> 2025
> First lien revolving credit facility $ 1,713 $ 2,749
> European revolving credit facility 518 940
> Chinese credit facilities 541 531
> Other foreign and domestic debt 203 201
> $ 2,975 $ 4,421

### GT-000162828026031866-0099

liquidity, [10-Q for 2026-03-31](https://www.sec.gov/Archives/edgar/data/42582/000162828026031866/gt-20260331.htm), characters 119437–120387

> Net cash used for investing activities was $174 million in the first three months of 2026, compared to net cash provided by investing activities of $432 million in the first three months of 2025. The $606 million increase in net cash used for investing activities was primarily due to cash provided by asset dispositions of $720 million in the first three months of 2025 due to the sale of the OTR tire business, partially offset by decreased capital expenditures of $84 million.
> Financing Activities
> Net cash provided by financing activities was $820 million in the first three months of 2026, compared to net cash provided by financing activities of $211 million in the first three months of 2025. The $609 million increase in cash provided by financing activities was primarily related to net borrowings of $807 million in the first three months of 2026, compared to net borrowings of $198 million in the first three months of 2025.
> Credit Sources

### GT-000162828026070703-0047

debt_note, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/gt-20260930.htm), characters 59969–61326

> If Available Cash (as defined in the facility) plus the average quarterly availability under the facility is greater than 25% of the total commitments under the facility, amounts drawn under the facility will bear interest, at our option, at (i) 125 basis points over SOFR or (ii) 25 basis points over an alternate base rate (the higher of (a) the prime rate, (b) the federal funds effective rate or the overnight bank funding rate plus 50 basis points or (c) SOFR plus 100 basis points). If Available Cash plus the average quarterly availability under the facility is equal to or less than 25% of the total commitments under the facility, then amounts drawn under the facility will bear interest, at our option, at (i) 150 basis points over SOFR or (ii) 50 basis points over an alternate base rate. Based on our current liquidity, amounts drawn under this facility bear interest at SOFR plus 125 basis points. Undrawn amounts under the facility are subject to an annual commitment fee of 25 basis points.
> At September 30, 2026, we had $57 million of borrowings and $1 million of letters of credit issued under the revolving credit facility. At December 31, 2025, we had no borrowings and $1 million of letters of credit issued under the revolving credit facility.
> €800 million Amended and Restated Senior Secured European Revolving Credit Facility due 2028

### GT-000162828026070703-0119

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/gt-20260930.htm), characters 146122–147134

> We expect our 2026 full-year cash flow to include capital expenditures of approximately $675 million. We also expect interest expense to be approximately $425 million; rationalization payments to be approximately $210 million; income tax payments to be approximately $175 million, excluding one-time items; and cash contributions to our global pension plans to be approximately $25 million. We expect working capital to be neither a significant source nor significant use of cash for the full year 2026.
> We are continuing to actively monitor our liquidity and intend to operate our business in a way that allows us to address our cash flow needs with our existing cash and available credit if they cannot be funded by cash generated from operating or other financing activities. We believe that our liquidity position is adequate to fund our operating and investing needs and debt maturities for the next twelve months and to provide us with the ability to respond to further changes in the business environment.

### GT-000162828026070703-0135

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/42582/000162828026070703/gt-20260930.htm), characters 164455–165867

> In addition, our European revolving credit facility contains non-financial covenants similar to the non-financial covenants in our first lien revolving credit facility that are described above, similar non-financial covenants specifically applicable to GEBV and its subsidiaries, and a financial covenant applicable only to GEBV and its subsidiaries. This financial covenant provides that we are not permitted to allow GEBV’s ratio of Consolidated Net GEBV Indebtedness to Consolidated GEBV EBITDA for a period of four consecutive fiscal quarters to be greater than 3.0 to 1.0 at the end of any fiscal quarter. Consolidated Net GEBV Indebtedness is determined net of the sum of cash and cash equivalents in excess of $100 million held by GEBV and its subsidiaries, cash and cash equivalents in excess of $150 million held by the Parent Company and its U.S. subsidiaries, and availability under our first lien revolving credit facility if the ratio of EBITDA to Consolidated Interest Expense described above is not applicable and the conditions to borrowing under the first lien revolving credit facility are met. Consolidated Net GEBV Indebtedness also excludes loans from other consolidated Goodyear entities. This financial covenant is also included in
> 42
> Table of Contents
> our pan-European accounts receivable securitization facility. At September 30, 2026, we were in compliance with this financial covenant.

## Run

Run `GT-20261118T050357Z-DeepSeek-V4-Pro-0813`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 9 calls, 34,395 input (12,032 cached) and 45,814 output tokens, $0.1480, 912s. Verification: 33 calls, 17,477 input (4,224 cached) and 3,398 output tokens, $0.0242, 59s. Prices read 2026-11-17. Raw requests and responses: data/runs/GT/GT-20261118T050357Z-DeepSeek-V4-Pro-0813.jsonl.
