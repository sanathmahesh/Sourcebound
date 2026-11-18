# Credit memo: Walmart Inc. (WMT)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4.1-Flash-1017`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-3**.
Sources: [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm); [10-Q for 2026-07-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm); [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm)

Claims: 34 — 29 supported, 5 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 1; repairs: 1.

## Business profile

1. Revenue was **$648.1 billion** [F1] in the fiscal year ended 31 January 2024, **$681.0 billion** [F2] in the fiscal year ended 31 January 2025, **$713.2 billion** [F3] in the fiscal year ended 31 January 2026, and **$735.8 billion** [F4] in the twelve months to 31 July 2026.  
   ✅ supported (judge): All four revenue figures match the XBRL-derived metric values exactly.
2. EBITDA was **$44.0 billion** [F5] in the fiscal year ended 31 January 2026 and **$47.4 billion** [F6] in the twelve months to 31 July 2026.  
   ✅ supported (judge): Both EBITDA figures match the metric values computed from XBRL data exactly.
3. The company is enhancing omnichannel capabilities through stores, eCommerce websites, mobile applications and service offerings, supporting its retail operations.  
   ✅ supported (judge): The evidence directly states the company is enhancing omnichannel capabilities through stores, eCommerce websites, mobile applications and service offerings.
   - cites `WMT-000010416926000055-0016` ✓: “We are enhancing our omnichannel capabilities through a combination of stores, eCommerce websites, mobile applications and service offerings”
4. Operations are organized into three segments, and international distribution facilities are located across Africa, Canada, Central America, Chile, China, India and Mexico.  
   ✅ supported (judge): The passages state the business has three segments and that international distribution facilities are located in exactly the listed countries.
   - cites `WMT-000010416926000055-0148` ✓: “the financial results of each of the three segments of our business”
   - cites `WMT-000010416926000055-0031` ✓: “Outside the U.S., we utilize a total of 179 distribution facilities strategically located in Africa, Canada, Central America, Chile, China, India and Mexico”
5. The retail markets are highly competitive and rapidly evolving, with new business models and well-funded competitors, which can pressure the company's competitive position.  
   ✅ supported (judge): The passage directly states the retail markets are highly competitive and rapidly evolving with new business models and well-funded competitors, and that competitors' advantages can affect the company's competitive position.
   - cites `WMT-000010416926000055-0027` ✓: “Each of these landscapes is highly competitive and rapidly evolving, and new business models and the entry of new, well-funded competitors continue to intensify this competition.”
6. Sales are seasonal, and historically the highest sales volume for each segment has occurred in the fourth quarter of the fiscal year.  
   ✅ supported (judge): The passage directly states the business is seasonal and that historically the highest sales volume for each segment occurs in the fourth quarter of the fiscal year.
   - cites `WMT-000010416926000055-0029` ✓: “Historically, our highest sales volume for each segment has occurred in the fourth quarter of our fiscal year.”

## Financial risk

1. Debt / EBITDA was **1.21x** [F7] in the fiscal year ended 31 January 2024, **1.08x** [F8] in the fiscal year ended 31 January 2025, **1.17x** [F9] in the fiscal year ended 31 January 2026 and **1.21x** [F10] for the twelve months to 31 July 2026, so leverage is stable across the period.  
   ✅ supported (judge): All four Debt/EBITDA figures match the metric values exactly, and ratios ranging 1.08x–1.21x support the characterization of stable leverage.
2. Net leverage moved from **0.95x** [F11] in the fiscal year ended 31 January 2024 to **0.96x** [F12] for the twelve months to 31 July 2026 and is likewise stable, remaining close to the level at which it started.  
   ✅ supported (judge): The metric values confirm net leverage of 0.95x in FY ended 31 Jan 2024 and 0.96x for the twelve months to 31 July 2026, so it remained stable near its starting level.
3. EBITDA / interest improved from **15.03x** [F13] in the fiscal year ended 31 January 2024 to **20.99x** [F14] for the twelve months to 31 July 2026, with interest expense of **$2.3 billion** [F15] covered by EBITDA of **$47.4 billion** [F6].  
   ✅ supported (judge): Every figure in the claim matches the computed metric values exactly: 15.03x, 20.99x, $2.3B interest, and $47.4B EBITDA (minor apparent mismatch in division is due to rounding of the dollar figures).
4. FCF / debt worsened from **32.2%** [F16] in the fiscal year ended 31 January 2024 to **23.6%** [F17] for the twelve months to 31 July 2026, as capital expenditure of **$29.4 billion** [F18] absorbed much of the **$42.9 billion** [F19] of cash from operations and total debt rose to **$57.2 billion** [F20] from **$51.5 billion** [F21] in the fiscal year ended 31 January 2026.  
   ✅ supported (judge): All figures match the metric scorecard: FCF/debt fell from 32.2% (FY ended 31 Jan 2024) to 23.6% (LTM to 31 Jul 2026), with LTM capex of $29.4B against CFO of $42.9B, and total debt of $57.2B (LTM) vs $51.5B (FY ended 31 Jan 2026).
5. The decline in free cash flow relative to debt reflects heavier capital spending, with fiscal **2026** [quoted: WMT-000010416926000055-0166] free cash flow growth held back by higher capital expenditures for omnichannel investment.  
   ◐ partially supported (judge): The evidence supports that FY2026 free cash flow growth was partially offset by a $2.9 billion capex increase for omnichannel, but says nothing about free cash flow declining relative to debt.
   - cites `WMT-000010416926000055-0166` ✓: “partially offset by an increase of $2.9 billion in capital expenditures to support our omnichannel growth strategy”
6. Total borrowings rose over the period because long-term debt issued exceeded repayments, which offsets some of the cash generated.  
   ◐ partially supported (judge): Issuances exceeding repayments and the $2.2B debt increase are supported, but the claim that this 'offsets some of the cash generated' goes beyond the evidence, which contains no cash generation figures.
   - cites `WMT-000010416926000055-0187` ✓: “Our total outstanding long-term debt increased $2.2 billion during fiscal 2026, primarily due to issuances of long-term debt.”
   - cites `WMT-000010416926000102-0063` ✓: “During the three months ended April 30, 2026, our total outstanding long-term debt increased $2.6 billion, primarily due to the issuance of new long-term debt in April 2026”

## Liquidity

1. Liquidity coverage was **1.18x** [F22] in the fiscal year ended 31 January 2026 and **1.07x** [F23] for the twelve months to 31 July 2026, so measured sources modestly exceed expected twelve-month uses.  
   ✅ supported (judge): The claimed liquidity coverage values of 1.18x (FY ended 31 January 2026) and 1.07x (twelve months to 31 July 2026) match the computed metrics, and values above 1.0x directly imply sources modestly exceed uses.
2. For the twelve months to 31 July 2026, cash of **$11.5 billion** [F24] and cash from operations of **$42.9 billion** [F19] compare with capital expenditure of **$29.4 billion** [F18], dividends of **$7.7 billion** [F25] and short-term debt of **$13.9 billion** [F26].  
   ✅ supported (judge): All five figures in the claim match the computed XBRL metric values for the twelve months to 31 July 2026.
3. The company had committed lines of credit in the U.S. of $**15.0** [quoted: WMT-000010416926000154-0069] billion at the latest balance sheet date, all undrawn.  
   ✅ supported (judge): The passage directly states committed U.S. lines of credit of $15.0 billion at July 31, 2026, all undrawn.
   - cites `WMT-000010416926000154-0069` ✓: “In total, we had committed lines of credit in the U.S. of $15.0 billion at July 31, 2026, all undrawn.”
4. These committed lines were renewed and extended, comprising a **364** [quoted: WMT-000010416926000154-0069]-day revolving credit facility of $**10.0** [quoted: WMT-000010416926000154-0069] billion and a five-year credit facility of $**5.0** [quoted: WMT-000010416926000154-0069] billion.  
   ✅ supported (judge): The passage states the company renewed and extended a 364-day revolving credit facility of $10.0 billion and a five-year credit facility of $5.0 billion.
   - cites `WMT-000010416926000154-0069` ✓: “the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion”
5. Free cash flow was negative in the most recent quarter, as payments for property and equipment exceeded net cash provided by operating activities.  
   ✅ supported (judge): The table shows Q1 FY2026 operating cash flow of $4,738M was exceeded by payments for property and equipment of $6,684M, yielding negative free cash flow of $(1,946)M.
   - cites `WMT-000010416926000102-0048` ✓: “Net cash provided by operating activities $ 4,738 $ 5,411”
   - cites `WMT-000010416926000102-0048` ✓: “Free cash flow $ (1,946) $ 425”
6. A downgrade of the company's credit ratings could raise borrowing costs and reduce flexibility in accessing the commercial paper market.  
   ✅ supported (judge): The filing states that a downgrade could increase borrowing costs and impair flexibility in accessing the commercial paper market.
   - cites `WMT-000010416926000102-0067` ✓: “Any downgrade of our credit ratings by a credit rating agency could increase our future borrowing costs”

## Maturity wall

1. Scheduled long-term debt maturities are **$3.5 billion** [F27] in the next twelve months, **$3.2 billion** [F28] in year two, **$3.4 billion** [F29] in year three, **$2.1 billion** [F30] in year four and **$2.6 billion** [F31] in year five, with **$23.3 billion** [F32] falling due after year five.  
   ✅ supported (judge): Every maturity figure in the claim matches the XBRL-computed metric values exactly.
2. Debt falling due within the next two years totals **$13.4 billion** [F33], equal to **26.0%** [F34] of total debt of **$51.5 billion** [F21], so most maturities sit beyond that window.  
   ✅ supported (judge): Both figures ($13.4B and 26.0%) and total debt ($51.5B) match the computed metrics, and since only 26.0% is due within 24 months, most maturities indeed sit beyond that window.
3. Near-term maturity cover is **1.25x** [F35], measured against short-term debt of **$10.1 billion** [F36] and cash of **$10.7 billion** [F37], with no undrawn revolver capacity or short-term investments included.  
   ✅ supported (judge): All claim components match the metric values: cover of 1.25x with short-term debt of $10.1B, cash of $10.7B, and short-term investments and undrawn revolver assumed zero (not reported).
4. The Company renewed and extended its **364** [quoted: WMT-000010416926000102-0012]-day and five-year revolving credit facilities, and its committed U.S. lines were undrawn.  
   ✅ supported (judge): The passage directly states the renewal and extension of both credit facilities and that the U.S. committed lines were undrawn.
   - cites `WMT-000010416926000102-0012` ✓: “the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion”
5. The committed lines of credit carry covenants, the tightest of which limits the amount of secured debt.  
   ✅ supported (judge): The passage states the committed lines of credit carry covenants, the most restrictive of which relates to the maximum amount of secured debt.
   - cites `WMT-000010416926000055-0257` ✓: “the Company has agreed to observe certain covenants, the most restrictive of which relates to the maximum amount of secured debt”
6. Recently issued senior unsecured notes contain no financial covenants and do not restrict dividends or share repurchases.  
   ✅ supported (judge): Evidence explicitly states the senior unsecured notes contain no financial covenants and do not restrict dividends or share repurchases.
   - cites `WMT-000010416926000154-0015` ✓: “These issuances do not contain any financial covenants and do not restrict the Company's ability to pay dividends or repurchase company stock”

## Key risks

1. An economic slowdown or recession could reduce consumer demand and adversely affect net sales and operating income, weakening the cash flow available to service debt.  
   ◐ partially supported (judge): The passage supports that a slowdown or recession could reduce consumer demand and adversely affect net sales and operating income, but it does not mention any effect on cash flow available to service debt.
   - cites `WMT-000010416926000055-0056` ✓: “overall economic slowdown or recession and other economic factors in the U.S., or in any of the other markets in which we operate, could adversely affect consumer demand”
   - cites `WMT-000010416926000055-0056` ✓: “adversely affect our net sales, growth rates, operating income and result in slower inventory turnover and greater markdowns of inventory”
2. A pandemic or other health crisis could disrupt supply chain operations and raise costs of doing business, which could pressure operating cash flow.  
   ✅ supported (judge): The filing states a pandemic could impact costs of doing business and supply chain operations, and could disrupt and adversely affect operations and financial performance, which encompasses operating cash flow pressure.
   - cites `WMT-000010416926000055-0059` ✓: “could impact our business operations, demand for our products and services, in-stock positions, costs of doing business, access to inventory, supply chain operations”
3. International operations expose the company to political instability and legal and regulatory constraints that could negatively affect operating results and cash flow.  
   ✅ supported (judge): The passage explicitly lists political instability and legal and regulatory constraints among factors that could negatively affect future operating results in Walmart International operations.
   - cites `WMT-000010416926000055-0098` ✓: “Our future operating results in these countries could be negatively affected by a variety of factors”
   - cites `WMT-000010416926000055-0098` ✓: “political conditions, including political instability, local and global economic conditions; legal and regulatory constraints”
4. Financial services offered through partners and the OnePay venture are subject to regulatory requirements, and noncompliance could result in fines, sanctions and penalties that reduce cash available for debt service.  
   ◐ partially supported (judge): The passage confirms the services, regulatory requirements, and potential fines/sanctions/penalties, but the claim's added consequence that these would 'reduce cash available for debt service' is not stated in the evidence.
   - cites `WMT-000010416926000055-0111` ✓: “Failure to comply with these laws and regulations could result in fines, sanctions, penalties and harm to our reputation.”

## Rating rationale

1. The SB grade of **SB-3** [F38] (weighted score **2.70** [F39]) is a stylized internal scorecard grade rather than a credit rating, and it is not provisional because all six factors were scored.  
   ✅ supported (judge): All elements of the claim are directly confirmed by the computed scorecard data: the grade is labeled a stylized scorecard grade not a credit rating, it equals SB-3 with weighted score 2.70, and all six factors have band scores (none unscored), so it is not provisional.
2. Interest coverage is the strongest factor, with **20.99x** [F14] placing it in band **1** [F40] at a **25.0%** [F41] weight.  
   ✅ supported (judge): Interest coverage of 20.99x is band 1 (strongest) with a 25.0% weight, and no other factor has both a band-1 score and a weight equal to or higher than 25%.
3. The weakest factors are liquidity coverage, at **1.07x** [F23] in band **5** [F42] with a **15.0%** [F43] weight, and near-term maturity cover, at **1.25x** [F35] in band **5** [F44] with a **10.0%** [F45] weight.  
   ✅ supported (judge): Both metrics match the scorecard values (1.07x band 5 weight 15.0%; 1.25x band 5 weight 10.0%), and band 5 is the weakest among all six factors (others are bands 1-3).
4. The liquidity and maturity bands temper the grade less than the measured ratios alone suggest, because the company had committed lines of credit in the U.S. of $**15.0** [quoted: WMT-000010416926000154-0069] billion at the latest balance sheet date, all undrawn.  
   ◐ partially supported (judge): The $15.0 billion of committed, undrawn U.S. lines at July 31, 2026 is directly supported, but the claim that these factors 'temper the grade less than the measured ratios alone suggest' is contradicted by the scorecard: liquidity coverage and near-term maturity cover both score band 5 of 6, stronger than the leverage/coverage ratios (bands 1–3), meaning they lift rather than temper the grade.
   - cites `WMT-000010416926000154-0069` ✓: “In total, we had committed lines of credit in the U.S. of $15.0 billion at July 31, 2026, all undrawn.”
5. Debt / EBITDA of **1.21x** [F10] and net leverage of **0.96x** [F12] both map to band **2** [F46] and band **2** [F47] at weights of **20.0%** [F48] and **10.0%** [F49] respectively.  
   ✅ supported (judge): Metric values and scorecard entries confirm both ratios' values, bands (2), and weights (20.0% and 10.0%).
6. FCF / debt of **23.6%** [F17] sits in band **3** [F50] at a **20.0%** [F51] weight, and the negative free cash flow in the most recent quarter tempers this factor.  
   ✅ supported (judge): 23.6% FCF/debt, band 3, and 20.0% weight are confirmed by the scorecard metrics, and the most recent quarter's free cash flow was negative ($-1,946 million), confirming all parts of the claim.
   - cites `WMT-000010416926000102-0048` ✓: “Payments for property and equipment (6,684) (4,986)”

## Reviewer checklist

- [ ] **fallback** (info): Depreciation and amortisation: used rank 3 DepreciationAmortizationAndAccretionNet in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Interest expense: used rank 3 InterestExpenseDebt + FinanceLeaseInterestExpense in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Dividends paid: used rank 2 PaymentsOfDividendsCommonStock in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): CommercialPaper assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term investments assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **reconciliation** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $46,891m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $39,579m (-15.6%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $45,790m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $35,999m (-21.4%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $51,523m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $38,166m (-25.9%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $57,243m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $39,932m (-30.2%). Check which matches the balance sheet.
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The evidence supports that FY2026 free cash flow growth was partially offset by a $2.9 billion capex increase for omnichannel, but says nothing about free cash flow declining relative to debt.): “The decline in free cash flow relative to debt reflects heavier capital spending, with fiscal 2026 free cash flow growth held back by higher capital expenditures for omnichannel investment.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (Issuances exceeding repayments and the $2.2B debt increase are supported, but the claim that this 'offsets some of the cash generated' goes beyond the evidence, which contains no cash generation figures.): “Total borrowings rose over the period because long-term debt issued exceeded repayments, which offsets some of the cash generated.”
- [ ] **partially supported claim** (warning): Key risks: partially supported (The passage supports that a slowdown or recession could reduce consumer demand and adversely affect net sales and operating income, but it does not mention any effect on cash flow available to service debt.): “An economic slowdown or recession could reduce consumer demand and adversely affect net sales and operating income, weakening the cash flow available to service debt.”
- [ ] **partially supported claim** (warning): Key risks: partially supported (The passage confirms the services, regulatory requirements, and potential fines/sanctions/penalties, but the claim's added consequence that these would 'reduce cash available for debt service' is not stated in the evidence.): “Financial services offered through partners and the OnePay venture are subject to regulatory requirements, and noncompliance could result in fines, sanctions and penalties that reduce cash available for debt service.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The $15.0 billion of committed, undrawn U.S. lines at July 31, 2026 is directly supported, but the claim that these factors 'temper the grade less than the measured ratios alone suggest' is contradicted by the scorecard: liquidity coverage and near-term maturity cover both score band 5 of 6, stronger than the leverage/coverage ratios (bands 1–3), meaning they lift rather than temper the grade.): “The liquidity and maturity bands temper the grade less than the measured ratios alone suggest, because the company had committed lines of credit in the U.S. of $15.0 billion at the latest balance sheet date, all undrawn.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $648.1 billion | rank 1: Revenues | Revenues 648,125,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F2 | Revenue (revenue:FY-1) | $681.0 billion | rank 1: Revenues | Revenues 680,985,000,000 (2024-02-01 to 2025-01-31, FY-1) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F3 | Revenue (revenue:FY0) | $713.2 billion | rank 1: Revenues | Revenues 713,163,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F4 | Revenue (revenue:LTM) | $735.8 billion | rank 1: Revenues | Revenues 713,163,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>Revenues 365,688,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>Revenues 343,011,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F5 | EBITDA (ebitda:FY0) | $44.0 billion | operating_income + d_and_a | OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 14,203,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F6 | EBITDA (ebitda:LTM) | $47.4 billion | operating_income + d_and_a | OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 14,421,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 14,203,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 7,746,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 6,856,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY-2) | 1.21x | total_debt / EBITDA | LongTermDebtNoncurrent 36,132,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>LongTermDebtCurrent 3,447,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>ShortTermBorrowings 878,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityCurrent 725,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,709,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>OperatingIncomeLoss 27,012,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 11,853,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:FY-1) | 1.08x | total_debt / EBITDA | LongTermDebtNoncurrent 33,401,000,000 (at 2025-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtCurrent 2,598,000,000 (at 2025-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>ShortTermBorrowings 3,068,000,000 (at 2025-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>FinanceLeaseLiabilityCurrent 800,000,000 (at 2025-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,923,000,000 (at 2025-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 29,348,000,000 (2024-02-01 to 2025-01-31, FY-1) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 12,973,000,000 (2024-02-01 to 2025-01-31, FY-1) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F9 | Debt / EBITDA (debt_to_ebitda:FY0) | 1.17x | total_debt / EBITDA | LongTermDebtNoncurrent 34,624,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 856,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,905,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 14,203,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F10 | Debt / EBITDA (debt_to_ebitda:LTM) | 1.21x | total_debt / EBITDA | LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 880,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,952,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 14,421,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F11 | Net leverage (net_leverage:FY-2) | 0.95x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 36,132,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>LongTermDebtCurrent 3,447,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>ShortTermBorrowings 878,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityCurrent 725,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,709,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 9,867,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>OperatingIncomeLoss 27,012,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 11,853,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F12 | Net leverage (net_leverage:LTM) | 0.96x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 880,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,952,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 11,529,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F13 | EBITDA / interest (interest_coverage:FY-2) | 15.03x | EBITDA / interest_expense | OperatingIncomeLoss 27,012,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 11,853,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>InterestExpenseDebt 2,259,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>FinanceLeaseInterestExpense 326,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F14 | EBITDA / interest (interest_coverage:LTM) | 20.99x | EBITDA / interest_expense | OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 14,421,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 14,203,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 7,746,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 6,856,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>InterestExpenseDebt 2,318,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>InterestExpenseDebt 711,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F15 | Interest expense (interest_expense:LTM) | $2.3 billion | rank 3: InterestExpenseDebt + FinanceLeaseInterestExpense | InterestExpenseDebt 2,318,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>InterestExpenseDebt 711,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>InterestExpenseDebt 1,170,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseInterestExpense 383,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>FinanceLeaseInterestExpense 251,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseInterestExpense 236,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F16 | FCF / debt (fcf_to_debt:FY-2) | 32.2% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 35,726,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 20,606,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtNoncurrent 36,132,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>LongTermDebtCurrent 3,447,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>ShortTermBorrowings 878,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityCurrent 725,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,709,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| F17 | FCF / debt (fcf_to_debt:LTM) | 23.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 19,710,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 18,352,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 14,181,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 11,409,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F18 | Capital expenditure (capex:LTM) | $29.4 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 14,181,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 11,409,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F19 | Cash from operations (cfo:LTM) | $42.9 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 19,710,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 18,352,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F20 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $57.2 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 880,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,952,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F21 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $51.5 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 34,624,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 856,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,905,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F22 | Liquidity coverage (liquidity_coverage:FY0) | 1.18x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 10,727,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsOfDividendsCommonStock 7,507,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F23 | Liquidity coverage (liquidity_coverage:LTM) | 1.07x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 11,529,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 19,710,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 18,352,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 14,181,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F24 | Cash and cash equivalents (cash:LTM) | $11.5 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 11,529,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F25 | Dividends paid (dividends:LTM) | $7.7 billion | rank 2: PaymentsOfDividendsCommonStock | PaymentsOfDividendsCommonStock 7,507,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsOfDividendsCommonStock 3,945,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsOfDividendsCommonStock 3,755,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F26 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $13.9 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F27 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $3.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 3,542,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F28 | Debt maturing in year two (maturity_year_2:FY0) | $3.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F29 | Debt maturing in year three (maturity_year_3:FY0) | $3.4 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 3,389,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F30 | Debt maturing in year four (maturity_year_4:FY0) | $2.1 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 2,143,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F31 | Debt maturing in year five (maturity_year_5:FY0) | $2.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 2,600,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F32 | Debt maturing after year five (maturity_after_year_5:FY0) | $23.3 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 23,255,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F33 | Debt due within 24 months (debt_due_24m:FY0) | $13.4 billion | short_term_debt + maturity_year_2 | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F34 | Share of debt due within 24 months (share_due_24m:FY0) | 26.0% | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtNoncurrent 34,624,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 856,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,905,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F35 | Near-term maturity cover (near_term_maturity_cover:FY0) | 1.25x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 10,727,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F36 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $10.1 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F37 | Cash and cash equivalents (cash:FY0) | $10.7 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 10,727,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F38 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 2.7 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F39 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 2.7 | sum of weight x band over the factors scored, divided by their weights | — |
| F40 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 1 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F41 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F42 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 5 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F43 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F44 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 5 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F45 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F46 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 2 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F47 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 2 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F48 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F49 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F50 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 3 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F51 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### WMT-000010416926000055-0016

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 19373–20362

> We are enhancing our omnichannel capabilities through a combination of stores, eCommerce websites, mobile applications and service offerings, as well as our supply chain, combined with approximately 2.1 million associates as of January 31, 2026, to better serve our customers. Our strategies increasingly include the use of AI-powered tools to support customer and member-facing experiences, associate productivity and operational efficiency across our ecosystem. Together, these elements produce a global retail ecosystem that we believe allows customers to view Walmart as their primary retail destination. As we execute on our strategy globally, our business continues to expand through offerings such as membership, advertising, marketplace and fulfillment services, and financial services. These offerings represent mutually reinforcing pieces of our omnichannel model centered on our customers around the world who are increasingly seeking convenience.
> Information About Our Segments

### WMT-000010416926000055-0027

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 31477–32779

> Competition. We compete with brick and mortar, eCommerce and omnichannel retailers operating discount, department, retail and wholesale grocery, drug, dollar, variety and specialty stores, supermarkets, supercenter-type stores, membership-only warehouse clubs, gasoline stations and social commerce platforms, as well as companies that offer services in digital advertising, fulfillment and delivery services, health and wellness and financial services. Our ability to develop and effectively operate different formats at the right locations and to deliver a customer-centric omnichannel experience largely determines our competitive position in the retail industry within the markets where we operate. Each of these landscapes is highly competitive and rapidly evolving, and new business models and the entry of new, well-funded competitors continue to intensify this competition. Some of our competitors have longer histories in these lines of business, more customers and greater brand recognition. They may be able to obtain more favorable terms from suppliers and business partners and to devote greater resources to the development of these businesses. In addition, for eCommerce and other internet-based businesses, newer or smaller businesses may be better able to innovate and compete with us.

### WMT-000010416926000055-0029

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 34261–34918

> •Opening new stores and clubs, as well as remodeling existing locations, to enhance the customer experience, support omnichannel capabilities, and strengthen our physical footprint in existing and new markets; and
> •Investing in technology, automation, and our associates to deliver growth, expand operating margins and improve returns.
> Seasonal Aspects of Operations. Our business is seasonal to a certain extent and varies by country due to different national and religious holidays, festivals and customs, as well as different weather patterns. Historically, our highest sales volume for each segment has occurred in the fourth quarter of our fiscal year.

### WMT-000010416926000055-0031

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 36363–37702

> We continue to invest in supply chain automation and our fulfillment and delivery capabilities to better serve our customers. In the U.S., we utilize a network of 192 distribution facilities located strategically throughout the country using a combination of our private truck fleet as well as contracting with common carriers. During fiscal 2026, we began combining the Sam's Club U.S. supply chain function with Walmart U.S. to streamline operations and leverage our enterprise systems and infrastructure over time. Outside the U.S., we utilize a total of 179 distribution facilities strategically located in Africa, Canada, Central America, Chile, China, India and Mexico, which process and distribute both imported and domestic products to where our customers live. For fiscal 2026, the majority of our purchases of store and club merchandise were shipped through these facilities, while most of the remaining merchandise we purchased was shipped directly from suppliers to our stores and clubs. As an omnichannel retailer, we ship merchandise purchased by customers on our eCommerce platforms by a number of methods from multiple locations, including leveraging our network of stores and clubs to fulfill and deliver customer orders, as well as shipping directly from eCommerce fulfillment centers and other distribution facilities.
> 9

### WMT-000010416926000055-0056

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 65609–66757

> consumer credit, higher consumer debt levels, changes in consumer spending and shopping patterns, fluctuations in currency exchange rates, higher tax rates, imposition of new taxes or other changes in tax laws, changes in healthcare laws, other regulatory changes, the imposition of export and import restrictions, tariffs, trade barriers or other measures that create barriers to or increase the costs associated with international trade, overall economic slowdown or recession and other economic factors in the U.S., or in any of the other markets in which we operate, could adversely affect consumer demand for the products and services we sell in the U.S. or such other markets, change the mix of products we sell to any one or more markets with a lower average gross margin, cause a slowdown in discretionary purchases of goods, adversely affect our net sales, growth rates, operating income and result in slower inventory turnover and greater markdowns of inventory, or otherwise materially adversely affect our operations and operating results and could result in impairment charges to intangible assets, goodwill or other long-lived assets.

### WMT-000010416926000055-0059

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 68654–69679

> The emergence, severity, magnitude and duration of global or regional pandemics, epidemics or other health crises are uncertain and difficult to predict. A pandemic, epidemic or contagious disease outbreak that affects humans or the food supply, such as the avian flu impact on poultry and egg production could impact our business operations, demand for our products and services, in-stock positions, costs of doing business, access to inventory, supply chain operations, ability to predict future performance, exposure to litigation and financial performance, among other things. In the event of any global or regional health crisis, customer demand for certain products may fluctuate, customer behaviors may change and consumer disposable income could be negatively impacted, which may challenge our ability to anticipate and/or adjust inventory levels to meet that demand. These risks and their impacts are difficult to predict and could otherwise disrupt and adversely affect our operations and our financial performance.

### WMT-000010416926000055-0098

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 113788–115074

> During fiscal 2026, our Walmart International operations generated approximately 19% of our consolidated net sales. Walmart International's operations in various countries also source goods and services from other countries. Our future operating results in these countries could be negatively affected by a variety of factors, most of which are beyond our control. These factors include political conditions, including political instability, local and global economic conditions; legal and regulatory constraints, such as regulation of product and service offerings including regulatory restrictions (such as foreign ownership restrictions) on eCommerce and retail operations in international markets, such as in India; restrictive governmental actions, such as trade protection measures or nationalization; antitrust and competition law regulatory matters, such as those underway in Canada, Mexico and India (relating to our Flipkart subsidiary); local product safety and environmental laws; tax regulations; local labor laws; anti-money laundering laws and regulations; trade policies; foreign exchange or currency regulations; laws and regulations regarding consumer and data protection; and other matters in any of the countries or regions in which we operate, now or in the future.

### WMT-000010416926000055-0111

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 128129–129197

> Additionally, through various financial service partners and our OnePay fintech venture, we offer various services such as money transfers, digital payment platforms, bill payment, money orders, check cashing, prepaid access, co-branded credit cards, limited access to cryptocurrency and equity investment products, installment lending and earned wage access. These products and services require us to comply with legal and regulatory requirements, including those intended to help detect and prevent fraud and other illicit activity, the sale and custody of equity and cryptocurrency products, privacy, information security, anti-money laundering and sanctions regimes and consumer protection under U.S. state and federal laws and regulations, as well as those of certain other countries. Failure to comply with these laws and regulations could result in fines, sanctions, penalties and harm to our reputation. Increased U.S. regulation of non-bank financial institutions may also result in additional requirements and scrutiny of certain financial services we offer.

### WMT-000010416926000055-0148

mdna, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 165167–166222

> ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS
> Overview
> This discussion, which presents our results for the fiscal years ended January 31, 2026 ("fiscal 2026"), January 31, 2025 ("fiscal 2025") and January 31, 2024 ("fiscal 2024"), should be read in conjunction with our Consolidated Financial Statements and the accompanying notes. We intend for this discussion to provide the reader with information that will assist in understanding our financial statements, the changes in certain key items in those financial statements from period to period and the primary factors that accounted for those changes. We also discuss certain performance metrics that management uses to assess the Company's performance. Additionally, the discussion provides information about the financial results of each of the three segments of our business to provide a better understanding of how each of those segments and its results of operations affect the financial condition and results of operations of the Company as a whole.

### WMT-000010416926000055-0166

mdna, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 184446–185924

> The increase in net cash provided by operating activities in fiscal 2026 is primarily due to an increase in cash provided by operating income, lower cash tax payments and the timing of certain payments. Free cash flow for fiscal 2026 increased when compared to fiscal 2025 due to an increase in cash provided by operating income, lower cash tax payments and timing of certain payments, partially offset by an increase of $2.9 billion in capital expenditures to support our omnichannel growth strategy. Net cash provided by operating activities for fiscal 2025 increased when compared to fiscal 2024 primarily due to an increase in cash provided by operating income and lapping the payment of accrued opioid legal charges in the prior year, partially offset by increased inventory purchases. Free cash flow for fiscal 2025 decreased when compared to fiscal 2024 due to an increase of $3.2 billion in capital expenditures to support our omnichannel growth strategy, partially offset by the increase in net cash provided by operating activities described above.
> 37
> Results of Operations
> Consolidated Results of Operations
> Fiscal Years Ended January 31,
> (Dollar amounts and retail square feet in millions) 2026 2025 2024
> Net sales $ 706,413 $ 674,538 $ 642,637
> Percentage change from comparable period 4.7 % 5.0 % 6.1 %
> Membership and other income(1)
> 6,750 6,447 5,488
> Total revenues
> 713,163 680,985 648,125
> Percentage change from comparable period 4.7 % 5.1 % 6.0 %
> Gross profit(2)

### WMT-000010416926000055-0187

liquidity, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 209559–211042

> Proceeds from issuance of long-term debt — 3,983 3,983
> Repayments of long-term debt (2,625) — (2,625)
> Reclassifications of long-term debt 3,569 (3,569) —
> Currency and other adjustments — 809 809
> Balances as of January 31, 2026 $ 3,542 $ 34,624 $ 38,166
> Our total outstanding long-term debt increased $2.2 billion during fiscal 2026, primarily due to issuances of long-term debt. Refer to Note 5 to our Consolidated Financial Statements for details on the issuances of long-term debt.
> Estimated contractual interest payments associated with our long-term debt amount to $17.3 billion, with approximately $1.7 billion expected to be paid in fiscal 2027. Estimated interest payments are based on our principal amounts and expected maturities of all debt outstanding as of January 31, 2026, and assumes interest rates remain at current levels for our variable rate instruments.
> 43
> Dividends
> Our total dividend payments were $7.5 billion, $6.7 billion and $6.1 billion for fiscal 2026, 2025 and 2024, respectively. Effective February 19, 2026, the Company approved the fiscal 2027 annual dividend of $0.99 per share, an increase over the fiscal 2026 annual dividend of $0.94 per share. For fiscal 2027, the annual dividend will be paid in four quarterly installments of $0.2475 per share, according to the following record and payable dates:
> Record Date Payable Date
> March 20, 2026 April 6, 2026
> May 8, 2026 May 26, 2026
> August 21, 2026 September 8, 2026
> December 11, 2026 January 4, 2027

### WMT-000010416926000055-0257

debt_note, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 292608–294062

> The committed lines of credit in the table above mature in April 2026 and April 2030, carry interest rates of the Secured Overnight Financing Rate plus 45 basis points, and incur commitment fees ranging between 1.5 and 4.0 basis points. In conjunction with the committed lines of credit listed in the table above, the Company has agreed to observe certain covenants, the most restrictive of which relates to the maximum amount of secured debt. Additionally, the Company has syndicated and fronted letters of credit available which totaled $2.0 billion and $2.1 billion as of January 31, 2026 and 2025, respectively, of which $1.7 billion and $1.5 billion was issued as of January 31, 2026 and 2025, respectively.
> 66
> The Company's long-term debt, which includes the fair value instruments further discussed in Note 7, consists of the following as of January 31, 2026 and 2025:
> January 31, 2026 January 31, 2025
> (Amounts in millions) Maturity Dates
> By Fiscal Year Amount
> Average Rate(1)
> Amount
> Average Rate(1)
> Unsecured debt
> Fixed 2027 - 2054 $ 32,032 3.9% $ 31,406 3.8%
> Variable 2028 750 4.1% — —%
> Total U.S. dollar denominated 32,782 31,406
> Euro denominated
> 2027 - 2030 1,955 4.0% 1,715 4.0%
> Sterling denominated
> 2031 - 2039 3,677 5.4% 3,336 5.4%
> Yen denominated
> 2028 388 0.5% 389 0.5%
> Total unsecured debt 38,802 36,846
> Total other(2)
> (636) (847)
> Total debt 38,166 35,999
> Less amounts due within one year (3,542) (2,598)
> Long-term debt $ 34,624 $ 33,401

### WMT-000010416926000102-0012

debt_note, [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm), characters 16455–17933

> Note 3. Short-term Borrowings and Long-term Debt
> The Company has various committed lines of credit in the U.S. to support its commercial paper program. In April 2026, the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion. In total, the Company had committed lines of credit in the U.S. of $15.0 billion at April 30, 2026 and January 31, 2026, all undrawn.
> The following table provides the changes in the Company's long-term debt for the three months ended April 30, 2026:
> (Amounts in millions) Long-term debt due within one year Long-term debt Total
> Balances as of February 1, 2026 $ 3,542 $ 34,624 $ 38,166
> Proceeds from issuance of long-term debt(1)
> — 4,230 4,230
> Repayments of long-term debt (1,504) — (1,504)
> Reclassifications of long-term debt 1,873 (1,873) —
> Currency and other adjustments
> (15) (94) (109)
> Balances as of April 30, 2026 $ 3,896 $ 36,887 $ 40,783
> (1)Proceeds from issuance of long-term debt are net of deferred loan costs and any related discount or premium.
> Debt Issuances
> Information on significant long-term debt issued during the three months ended April 30, 2026, for general corporate purposes, is as follows:
> (Amounts in millions)
> Issue Date Principal Amount Maturity Date
> Interest Rate
> Net Proceeds
> April 30, 2026 $ 350 April 30, 2029 Floating $ 349
> April 30, 2026 $ 650 April 30, 2029 4.000% $ 648
> April 30, 2026 $ 1,000 April 30, 2031 4.150% $ 994

### WMT-000010416926000102-0048

mdna, [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm), characters 60452–61555

> Although other companies report their free cash flow, numerous methods may exist for calculating a company's free cash flow. As a result, the method used by management to calculate our free cash flow may differ from the methods used by other companies to calculate their free cash flow.
> The following table sets forth a reconciliation of free cash flow, a non-GAAP financial measure, to net cash provided by operating activities, which we believe to be the GAAP financial measure most directly comparable to free cash flow, as well as information regarding net cash used in investing activities and net cash provided by financing activities.
> Three Months Ended April 30,
> (Amounts in millions) 2026 2025
> Net cash provided by operating activities $ 4,738 $ 5,411
> Payments for property and equipment (6,684) (4,986)
> Free cash flow $ (1,946) $ 425
> Net cash used in investing activities(1)
> $ (6,737) $ (5,093)
> Net cash provided by financing activities 2,328 8
> (1) Net cash used in investing activities includes payments for property and equipment, which is also included in our computation of free cash flow.

### WMT-000010416926000102-0063

liquidity, [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm), characters 78767–79839

> Balances as of April 30, 2026 $ 3,896 $ 36,887 $ 40,783
> (1)Proceeds from issuance of long-term debt are net of deferred loan costs and any related discount or premium.
> During the three months ended April 30, 2026, our total outstanding long-term debt increased $2.6 billion, primarily due to the issuance of new long-term debt in April 2026, less current year debt repayments. Refer to Note 3 to our Condensed Consolidated Financial Statements for details.
> Dividends
> Effective February 19, 2026, the Company approved the fiscal 2027 annual dividend of $0.99 per share, an increase over the fiscal 2026 annual dividend of $0.94 per share. For fiscal 2027, the annual dividend was or will be paid in four quarterly installments of $0.2475 per share, according to the following record and payable dates:
> Record Date Payable Date
> March 20, 2026 April 6, 2026
> May 8, 2026 May 26, 2026
> August 21, 2026 September 8, 2026
> December 11, 2026 January 4, 2027
> The dividend installments payable on April 6, 2026 and May 26, 2026 were paid as scheduled.
> Company Share Repurchase Program

### WMT-000010416926000102-0067

liquidity, [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm), characters 82991–84375

> Credit rating agencies review their ratings periodically and, therefore, the credit ratings assigned to us by each agency may be subject to revision at any time. Accordingly, we are not able to predict whether our current credit ratings will remain consistent over time. Factors that could affect our credit ratings include changes in our operating performance, the general economic environment, conditions in the retail industry, our financial position, including our total debt and capitalization, and changes in our business strategy. Any downgrade of our credit ratings by a credit rating agency could increase our future borrowing costs or impair our ability to access capital and credit markets on terms commercially acceptable to us. In addition, any downgrade of our current short-term credit ratings could impair our ability to access the commercial paper markets with the same flexibility that we have experienced historically, potentially requiring us to rely more heavily on more expensive types of debt financing. The credit rating agency ratings are not recommendations to buy, sell or hold our commercial paper or debt securities. Each rating may be subject to revision or withdrawal at any time by the assigning rating organization and should be evaluated independently of any other rating. Moreover, each credit rating is specific to the security to which it applies.

### WMT-000010416926000154-0015

debt_note, [10-Q for 2026-07-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm), characters 19950–20698

> April 30, 2026 $ 1,250 April 30, 2033 4.450% $ 1,244
> April 30, 2026 $ 1,000 April 30, 2036 4.750% $ 995
> Total $ 4,230
> These issuances are senior, unsecured notes which rank equally with all other senior, unsecured debt obligations of the Company, and are not convertible or exchangeable. These issuances do not contain any financial covenants and do not restrict the Company's ability to pay dividends or repurchase company stock.
> 9
> Table of Contents
> Maturities
> Information on significant long-term debt maturities during the six months ended July 31, 2026 is as follows:
> (Amounts in millions)
> Maturity Date Principal Amount Interest Rate Repayment
> April 8, 2026 €650 2.550% $ 754
> April 15, 2026 $750 4.000% 750
> July 8, 2026 $799 3.050% 799
> $ 2,303

### WMT-000010416926000154-0069

liquidity, [10-Q for 2026-07-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm), characters 86699–88164

> Net cash used in investing activities for the six months ended July 31, 2026 increased $3.1 billion when compared to the same period in the previous fiscal year. The increase was primarily due to increased payments for property and equipment and change in net proceeds received from sales of certain strategic investments in the previous fiscal year.
> Net Cash Used in Financing Activities
> Six Months Ended July 31,
> (Amounts in millions) 2026 2025
> Net cash used in financing activities $ (4,842) $ (6,993)
> Net cash used in financing activities decreased $2.2 billion for the six months ended July 31, 2026, when compared to the same period in the previous fiscal year. The decrease was primarily due to higher short-term borrowings and lower share repurchases, primarily offset by increased debt repayments in the current fiscal year.
> In April 2026, the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion. In total, we had committed lines of credit in the U.S. of $15.0 billion at July 31, 2026, all undrawn.
> Long-term Debt
> The following table provides the changes in our long-term debt for the six months ended July 31, 2026:
> (Amounts in millions) Long-term debt due within one year Long-term debt Total
> Balances as of February 1, 2026 $ 3,542 $ 34,624 $ 38,166
> Proceeds from issuance of long-term debt(1)
> — 4,230 4,230
> Repayments of long-term debt (2,303) — (2,303)

## Run

Run `WMT-20261118T050006Z-DeepSeek-V4.1-Flash-1017`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 7 calls, 28,096 input (5,632 cached) and 17,890 output tokens, $0.0074, 392s. Verification: 34 calls, 16,434 input (4,352 cached) and 3,654 output tokens, $0.0239, 76s. Prices read 2026-11-17. Raw requests and responses: data/runs/WMT/WMT-20261118T050006Z-DeepSeek-V4.1-Flash-1017.jsonl.
