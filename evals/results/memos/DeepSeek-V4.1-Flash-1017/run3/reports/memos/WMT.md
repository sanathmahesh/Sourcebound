# Credit memo: Walmart Inc. (WMT)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4.1-Flash-1017`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-3**.
Sources: [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm); [10-Q for 2026-07-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm); [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm)

Claims: 33 — 30 supported, 3 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 1; repairs: 1.

## Business profile

1. For the twelve months to 31 July 2026, Walmart reported revenue of **$735.8 billion** [F1] and EBITDA of **$47.4 billion** [F2].  
   ✅ supported (judge): Both figures match the computed XBRL metric values for the LTM period to 31 July 2026.
2. Walmart describes itself as an omnichannel retailer serving customers through stores, eCommerce websites, mobile applications and service offerings, supported by its supply chain.  
   ✅ supported (judge): The passage states Walmart enhances omnichannel capabilities through stores, eCommerce websites, mobile applications, service offerings and its supply chain to serve customers.
   - cites `WMT-000010416926000055-0016` ✓: “We are enhancing our omnichannel capabilities through a combination of stores, eCommerce websites, mobile applications and service offerings, as well as our supply chain”
3. Walmart International is building mutually reinforcing businesses in advertising, marketplace and fulfillment services, financial services and healthcare, broadening its offerings beyond merchandise.  
   ✅ supported (judge): The passage explicitly states Walmart International continues to build mutually reinforcing businesses in advertising, marketplace and fulfillment services, financial services and healthcare, alongside its merchandise offerings.
   - cites `WMT-000010416926000055-0023` ✓: “Walmart International continues to build mutually reinforcing businesses in areas such as advertising, marketplace and fulfillment services, financial services and healthcare.”
4. Walmart competes in highly competitive and rapidly evolving retail landscapes, where new business models and well-funded competitors intensify competition.  
   ✅ supported (judge): The claim is a direct paraphrase of the passage on competitive retail landscapes.
   - cites `WMT-000010416926000055-0027` ✓: “Each of these landscapes is highly competitive and rapidly evolving, and new business models and the entry of new, well-funded competitors continue to intensify this competition.”
5. Walmart states that its business is seasonal to a certain extent and varies by country due to holidays, festivals, customs and weather patterns.  
   ✅ supported (judge): The claim matches the seasonal aspects passage exactly, though it omits the detail about Q4 being the highest sales volume quarter.
   - cites `WMT-000010416926000055-0029` ✓: “Our business is seasonal to a certain extent and varies by country due to different national and religious holidays, festivals and customs, as well as different weather patterns.”

## Financial risk

1. Debt / EBITDA moved from **1.21x** [F3] in the fiscal year ended 31 January 2024 to **1.21x** [F4] in the twelve months to 31 July 2026 and net leverage from **0.95x** [F5] to **0.96x** [F6], so both leverage measures are broadly stable across the period.  
   ✅ supported (judge): The metric values exactly match the claimed figures (1.21x to 1.21x Debt/EBITDA; 0.95x to 0.96x net leverage), which supports describing both leverage measures as broadly stable.
2. EBITDA / interest improved from **15.03x** [F7] in the fiscal year ended 31 January 2024 to **20.99x** [F8] in the twelve months to 31 July 2026, with LTM EBITDA of **$47.4 billion** [F2] against interest expense of **$2.3 billion** [F9].  
   ✅ supported (judge): All figures in the claim match the computed metric values exactly.
3. Earnings in the LTM period benefited from tariff refunds that were recorded as a reduction to cost of sales, although a significant portion was reinvested in price and other customer-facing initiatives.  
   ✅ supported (judge): Evidence states tariff refunds were recorded as a reduction to cost of sales and a significant portion was reinvested in price and other customer-facing initiatives.
   - cites `WMT-000010416926000154-0043` ✓: “the Company received approximately $2.9 billion in tariff refunds pursuant to the CBP process, which were recorded as a reduction to cost of sales”
4. FCF / debt declined from **32.2%** [F10] in the fiscal year ended 31 January 2024 to **23.6%** [F11] in the twelve months to 31 July 2026, as capital expenditure of **$29.4 billion** [F12] absorbed a large share of cash from operations of **$42.9 billion** [F13].  
   ✅ supported (judge): All figures (32.2% FY-2, 23.6% LTM, $29.4B capex, $42.9B CFO) match the computed metric values, and capex of $29.4B against CFO of $42.9B reasonably supports that capex absorbed a large share of operating cash flow.
   - cites `WMT-000010416926000055-0166` ✓: “partially offset by an increase of $2.9 billion in capital expenditures to support our omnichannel growth strategy”
5. Total debt rose from **$51.5 billion** [F14] at the fiscal year ended 31 January 2026 to **$57.2 billion** [F15] at the twelve months to 31 July 2026, reflecting long-term debt issuance partly offset by repayments.  
   ✅ supported (judge): The $51.5B to $57.2B total debt figures match the XBRL metric values, and the passage confirms the increase was driven by new long-term debt issuance less repayments.
   - cites `WMT-000010416926000102-0063` ✓: “our total outstanding long-term debt increased $2.6 billion, primarily due to the issuance of new long-term debt in April 2026, less current year debt repayments”
6. Capital spending continues to be directed mainly toward automation, eCommerce, supply chain and store and club investments, which supports the reported increase in capital expenditure.  
   ✅ supported (judge): The passage explicitly states the capital allocation strategy toward automation, eCommerce, supply chain and store and club investments, and the table shows total capital expenditures increased from $11,409 million to $14,181 million.
   - cites `WMT-000010416926000154-0052` ✓: “allocating the majority of our capital to higher-return areas focused on automation such as eCommerce, supply chain and store and club investments”

## Liquidity

1. Liquidity coverage, which weighs cash, undrawn facilities and cash from operations against near-term obligations, was **1.18x** [F16] at the fiscal year ended 31 January 2026 and **1.07x** [F17] for the twelve months to 31 July 2026, so sources cover uses with a modest margin.  
   ◐ partially supported (judge): The 1.18x FY and 1.07x LTM liquidity coverage figures match the computed metrics, but the claim asserts undrawn facilities were included when the scorecard shows the undrawn revolver was assumed zero because it was not reported, and no narrative passages support the coverage characterization.
2. Cash and cash equivalents of **$11.5 billion** [F18] at the twelve months to 31 July 2026 compare with short-term debt of **$13.9 billion** [F19].  
   ✅ supported (judge): Both figures match the computed metric values for the LTM to 31 July 2026.
3. Cash from operations of **$42.9 billion** [F13] over the twelve months to 31 July 2026 covered capital expenditure of **$29.4 billion** [F12] and dividends of **$7.7 billion** [F20] with funds left over.  
   ✅ supported (judge): Metric values confirm CFO of $42.9B exceeds capex ($29.4B) plus dividends ($7.7B), leaving ~$5.8B left over.
4. Committed bank lines supplement internal cash generation, with the U.S. facilities fully available rather than drawn.  
   ✅ supported (judge): The filings confirm committed U.S. lines of credit of $15.0 billion exist to support the commercial paper program and are fully undrawn/available, complementing internal cash sources.
   - cites `WMT-000010416926000154-0069` ✓: “In total, we had committed lines of credit in the U.S. of $15.0 billion at July 31, 2026, all undrawn.”
   - cites `WMT-000010416926000055-0256` ✓: “The Company has various committed lines of credit in the U.S. to support its commercial paper program”
5. The two U.S. facilities were renewed and extended, and they carry combined availability of $**15.0** [quoted: WMT-000010416926000102-0062] billion.  
   ✅ supported (judge): The passage confirms both facilities were renewed and extended and total $15.0 billion in U.S. committed lines of credit.
   - cites `WMT-000010416926000102-0062` ✓: “In April 2026, the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion.”
6. Access to short-term funding is sensitive to the company's credit ratings, and a downgrade could raise borrowing costs or narrow market access.  
   ✅ supported (judge): The passage explicitly states that short-term rating downgrades could impair commercial paper access and downgrades could raise borrowing costs or impair market access.
   - cites `WMT-000010416926000102-0067` ✓: “Any downgrade of our credit ratings by a credit rating agency could increase our future borrowing costs or impair our ability to access capital and credit markets”

## Maturity wall

1. Scheduled long-term debt maturities are **$3.5 billion** [F21] in year one, **$3.2 billion** [F22] in year two, **$3.4 billion** [F23] in year three, **$2.1 billion** [F24] in year four and **$2.6 billion** [F25] in year five, with **$23.3 billion** [F26] falling due after year five.  
   ✅ supported (judge): All five yearly maturity figures and the after-year-five amount match the XBRL-computed metric values exactly.
2. Debt due within the near-term window is **$13.4 billion** [F27], equal to **26.0%** [F28] of total debt of **$51.5 billion** [F14], so most obligations sit further out.  
   ✅ supported (judge): The $13.4B near-term debt, 26.0% share, and $51.5B total debt all match the computed metric values, and since only 26% is due within 24 months, most obligations do sit further out.
3. Near-term maturity cover is **1.25x** [F29], measured against cash of **$10.7 billion** [F30] and short-term debt of **$10.1 billion** [F31], with undrawn revolver capacity taken as **$0** [F32] in that calculation.  
   ✅ supported (judge): All claim figures match the computed metrics: cover 1.25x, cash $10.7B, short-term debt $10.1B, undrawn revolver $0 (not reported, assumed zero).
4. Committed bank lines provide additional liquidity outside the maturity-cover metric: "In total, the Company had committed lines of credit in the U.S. of $**15.0** [quoted: WMT-000010416926000102-0012] billion at April **30** [quoted: WMT-000010416926000102-0012], **2026** [quoted: WMT-000010416926000102-0012] and January **31** [quoted: WMT-000010416926000102-0012], **2026** [quoted: WMT-000010416926000102-0012], all undrawn."  
   ✅ supported (judge): The passage states exactly that the company had $15.0 billion of committed U.S. lines of credit at April 30, 2026 and January 31, 2026, all undrawn.
   - cites `WMT-000010416926000102-0012` ✓: “In total, the Company had committed lines of credit in the U.S. of $15.0 billion at April 30, 2026 and January 31, 2026, all undrawn.”
5. The committed lines carry maintenance covenants, the tightest of which limits secured borrowing rather than leverage generally: "the Company has agreed to observe certain covenants, the most restrictive of which relates to the maximum amount of secured debt".  
   ✅ supported (judge): The passage directly states the committed lines carry covenants, the most restrictive of which relates to the maximum amount of secured debt.
   - cites `WMT-000010416926000055-0257` ✓: “the Company has agreed to observe certain covenants, the most restrictive of which relates to the maximum amount of secured debt”
6. Refinancing during the period was done through senior unsecured notes that carry no financial covenants: "These issuances do not contain any financial covenants which restrict the Company's ability to pay dividends or repurchase Company stock."  
   ✅ supported (judge): The evidence explicitly states the fiscal 2026 issuances are senior unsecured notes and contain no financial covenants restricting dividends or stock repurchases.
   - cites `WMT-000010416926000055-0258` ✓: “These issuances do not contain any financial covenants which restrict the Company's ability to pay dividends or repurchase Company stock.”

## Key risks

1. Drug pricing and reimbursement pressure in the pharmacy business could reduce operating results and cash flow available to service debt.  
   ✅ supported (judge): The risk factor passage lists drug pricing and reimbursement pressures that could adversely affect results of operations and liquidity, matching the claim.
   - cites `WMT-000010416926000055-0090` ✓: “changes in the health insurance market generally; increased governmental focus on reducing drug prices”
   - cites `WMT-000010416926000055-0044` ✓: “could, in ways we may or may not be able to accurately predict, materially and adversely affect our business, results of operations, financial position and liquidity”
2. Regulatory, trade and currency risks in international operations could disrupt operations and weaken cash flow.  
   ✅ supported (judge): The passage lists regulatory, trade protection, and foreign exchange/currency risks in international operations that could negatively affect operating results.
   - cites `WMT-000010416926000055-0098` ✓: “political instability, local and global economic conditions; legal and regulatory constraints”
   - cites `WMT-000010416926000055-0044` ✓: “could, in ways we may or may not be able to accurately predict, materially and adversely affect our business, results of operations, financial position and liquidity”
3. Compliance failures in the financial services offerings could result in fines and penalties that consume cash.  
   ◐ partially supported (judge): The passage supports that compliance failures in financial services could result in fines, sanctions and penalties, but does not state that these would consume cash.
   - cites `WMT-000010416926000055-0111` ✓: “Failure to comply with these laws and regulations could result in fines, sanctions, penalties and harm to our reputation.”
4. An economic slowdown or recession could reduce consumer demand and pressure sales and operating cash flow.  
   ✅ supported (judge): The risk factor states that overall economic slowdown or recession could adversely affect consumer demand and net sales, and the risk factors generally cover effects on liquidity and operating results.
   - cites `WMT-000010416926000055-0056` ✓: “overall economic slowdown or recession and other economic factors in the U.S.”
   - cites `WMT-000010416926000055-0044` ✓: “could, in ways we may or may not be able to accurately predict, materially and adversely affect our business, results of operations, financial position and liquidity”

## Rating rationale

1. The **SB-3** [F33] grade, with weighted score **2.70** [F34], is a stylized internal scorecard grade, not a credit rating; all factors were scored, so it is not provisional.  
   ✅ supported (judge): The scorecard output confirms the SB-3 grade is a stylized scorecard grade, not a credit rating, with weighted score 2.70, and that all six factors were scored (not provisional).
2. Interest coverage is the strongest factor, with **20.99x** [F8] at band **1** [F35] and weight **25.0%** [F36].  
   ✅ supported (judge): Metric values show EBITDA/interest at 20.99x, band 1 (strongest), and the highest weight at 25%.
3. Debt / EBITDA of **1.21x** [F4] and net leverage of **0.96x** [F6] score in bands **2** [F37] and **2** [F38] at weights **20.0%** [F39] and **10.0%** [F40], while FCF / debt of **23.6%** [F11] scores in band **3** [F41] at weight **20.0%** [F42].  
   ✅ supported (judge): All metrics, bands, and weights match the scorecard evidence exactly.
4. Liquidity coverage of **1.07x** [F17] and near-term maturity cover of **1.25x** [F29] are the weakest factors, at bands **5** [F43] and **5** [F44] and weights **15.0%** [F45] and **10.0%** [F46].  
   ✅ supported (judge): All values match the scorecard: both liquidity factors are band 5 with weights 15% and 10%, and are the weakest (all other factors are bands 1-3); the ratios 1.07x and 1.25x match the computed metrics.
5. The grade is supported by the strongest interest coverage band and mid-range leverage bands, while the weaker liquidity and near-term maturity bands temper it; committed U.S. lines were renewed and extended, and the senior unsecured notes carry no financial covenants.  
   ◐ partially supported (judge): Committed U.S. lines were renewed/extended and the senior unsecured notes lack financial covenants, and liquidity (band 5) and near-term maturity (band 5) bands do temper the grade, but characterizing debt/EBITDA and net debt/EBITDA at band 2 of 6 as 'mid-range' understates them (band 2 is stronger than mid-range, near the best band).
   - cites `WMT-000010416926000154-0069` ✓: “the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion.”
   - cites `WMT-000010416926000055-0258` ✓: “These issuances do not contain any financial covenants which restrict the Company's ability to pay dividends or repurchase Company stock.”
6. Earnings support is tempered because LTM results benefited from tariff refunds, a significant portion of which was reinvested in price and other customer-facing initiatives.  
   ✅ supported (judge): The passage confirms LTM results included ~$2.9B of tariff refunds recorded as a reduction to cost of sales, with a significant portion invested into customer-facing initiatives, primarily price investment.
   - cites `WMT-000010416926000154-0043` ✓: “the Company received approximately $2.9 billion in tariff refunds pursuant to the CBP process, which were recorded as a reduction to cost of sales”

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
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The 1.18x FY and 1.07x LTM liquidity coverage figures match the computed metrics, but the claim asserts undrawn facilities were included when the scorecard shows the undrawn revolver was assumed zero because it was not reported, and no narrative passages support the coverage characterization.): “Liquidity coverage, which weighs cash, undrawn facilities and cash from operations against near-term obligations, was 1.18x at the fiscal year ended 31 January 2026 and 1.07x for the twelve months to 31 July 2026, so sources cover uses with a modest margin.”
- [ ] **partially supported claim** (warning): Key risks: partially supported (The passage supports that compliance failures in financial services could result in fines, sanctions and penalties, but does not state that these would consume cash.): “Compliance failures in the financial services offerings could result in fines and penalties that consume cash.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (Committed U.S. lines were renewed/extended and the senior unsecured notes lack financial covenants, and liquidity (band 5) and near-term maturity (band 5) bands do temper the grade, but characterizing debt/EBITDA and net debt/EBITDA at band 2 of 6 as 'mid-range' understates them (band 2 is stronger than mid-range, near the best band).): “The grade is supported by the strongest interest coverage band and mid-range leverage bands, while the weaker liquidity and near-term maturity bands temper it; committed U.S. lines were renewed and extended, and the senior unsecured notes carry no financial covenants.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:LTM) | $735.8 billion | rank 1: Revenues | Revenues 713,163,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>Revenues 365,688,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>Revenues 343,011,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F2 | EBITDA (ebitda:LTM) | $47.4 billion | operating_income + d_and_a | OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 14,421,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 14,203,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 7,746,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 6,856,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F3 | Debt / EBITDA (debt_to_ebitda:FY-2) | 1.21x | total_debt / EBITDA | LongTermDebtNoncurrent 36,132,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>LongTermDebtCurrent 3,447,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>ShortTermBorrowings 878,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityCurrent 725,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,709,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>OperatingIncomeLoss 27,012,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 11,853,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F4 | Debt / EBITDA (debt_to_ebitda:LTM) | 1.21x | total_debt / EBITDA | LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 880,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,952,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 14,421,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F5 | Net leverage (net_leverage:FY-2) | 0.95x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 36,132,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>LongTermDebtCurrent 3,447,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>ShortTermBorrowings 878,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityCurrent 725,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,709,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 9,867,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>OperatingIncomeLoss 27,012,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 11,853,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F6 | Net leverage (net_leverage:LTM) | 0.96x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 880,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,952,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 11,529,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F7 | EBITDA / interest (interest_coverage:FY-2) | 15.03x | EBITDA / interest_expense | OperatingIncomeLoss 27,012,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 11,853,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>InterestExpenseDebt 2,259,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>FinanceLeaseInterestExpense 326,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F8 | EBITDA / interest (interest_coverage:LTM) | 20.99x | EBITDA / interest_expense | OperatingIncomeLoss 29,825,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>OperatingIncomeLoss 16,876,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>OperatingIncomeLoss 14,421,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 14,203,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>DepreciationAmortizationAndAccretionNet 7,746,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>DepreciationAmortizationAndAccretionNet 6,856,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>InterestExpenseDebt 2,318,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>InterestExpenseDebt 711,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F9 | Interest expense (interest_expense:LTM) | $2.3 billion | rank 3: InterestExpenseDebt + FinanceLeaseInterestExpense | InterestExpenseDebt 2,318,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>InterestExpenseDebt 711,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>InterestExpenseDebt 1,170,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseInterestExpense 383,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>FinanceLeaseInterestExpense 251,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseInterestExpense 236,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F10 | FCF / debt (fcf_to_debt:FY-2) | 32.2% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 35,726,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 20,606,000,000 (2023-02-01 to 2024-01-31, FY-2) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtNoncurrent 36,132,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>LongTermDebtCurrent 3,447,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>ShortTermBorrowings 878,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityCurrent 725,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,709,000,000 (at 2024-01-31, balance sheet) [10-K 0000104169-25-000021](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| F11 | FCF / debt (fcf_to_debt:LTM) | 23.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 19,710,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 18,352,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 14,181,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 11,409,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F12 | Capital expenditure (capex:LTM) | $29.4 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 14,181,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 11,409,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F13 | Cash from operations (cfo:LTM) | $42.9 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 19,710,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 18,352,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F14 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $51.5 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 34,624,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 856,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,905,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F15 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $57.2 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 36,462,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 880,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,952,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F16 | Liquidity coverage (liquidity_coverage:FY0) | 1.18x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 10,727,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsOfDividendsCommonStock 7,507,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F17 | Liquidity coverage (liquidity_coverage:LTM) | 1.07x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 11,529,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 41,565,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 19,710,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 18,352,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 26,642,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 14,181,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F18 | Cash and cash equivalents (cash:LTM) | $11.5 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 11,529,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F19 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $13.9 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 3,470,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 10,479,000,000 (at 2026-07-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F20 | Dividends paid (dividends:LTM) | $7.7 billion | rank 2: PaymentsOfDividendsCommonStock | PaymentsOfDividendsCommonStock 7,507,000,000 (2025-02-01 to 2026-01-31, FY0) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>PaymentsOfDividendsCommonStock 3,945,000,000 (2026-02-01 to 2026-07-31, current year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>PaymentsOfDividendsCommonStock 3,755,000,000 (2025-02-01 to 2025-07-31, prior-year year-to-date) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F21 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $3.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 3,542,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F22 | Debt maturing in year two (maturity_year_2:FY0) | $3.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F23 | Debt maturing in year three (maturity_year_3:FY0) | $3.4 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 3,389,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F24 | Debt maturing in year four (maturity_year_4:FY0) | $2.1 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 2,143,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F25 | Debt maturing in year five (maturity_year_5:FY0) | $2.6 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 2,600,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F26 | Debt maturing after year five (maturity_after_year_5:FY0) | $23.3 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 23,255,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F27 | Debt due within 24 months (debt_due_24m:FY0) | $13.4 billion | short_term_debt + maturity_year_2 | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| F28 | Share of debt due within 24 months (share_due_24m:FY0) | 26.0% | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>LongTermDebtNoncurrent 34,624,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityCurrent 856,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>FinanceLeaseLiabilityNoncurrent 5,905,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F29 | Near-term maturity cover (near_term_maturity_cover:FY0) | 1.25x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 3,237,000,000 (at 2026-01-31, balance sheet) [10-K 0000104169-26-000055](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 10,727,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F30 | Cash and cash equivalents (cash:FY0) | $10.7 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 10,727,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F31 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $10.1 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 3,542,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm)<br>ShortTermBorrowings 6,596,000,000 (at 2026-01-31, balance sheet) [10-Q 0000104169-26-000154](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| F32 | Undrawn revolving credit capacity (undrawn_revolver:FY0) | $0 |  | — |
| F33 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 2.7 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F34 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 2.7 | sum of weight x band over the factors scored, divided by their weights | — |
| F35 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 1 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F36 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F37 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 2 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F38 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 2 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F39 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F40 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F41 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 3 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F42 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F43 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 5 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F44 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 5 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F45 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F46 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### WMT-000010416926000055-0016

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 19373–20362

> We are enhancing our omnichannel capabilities through a combination of stores, eCommerce websites, mobile applications and service offerings, as well as our supply chain, combined with approximately 2.1 million associates as of January 31, 2026, to better serve our customers. Our strategies increasingly include the use of AI-powered tools to support customer and member-facing experiences, associate productivity and operational efficiency across our ecosystem. Together, these elements produce a global retail ecosystem that we believe allows customers to view Walmart as their primary retail destination. As we execute on our strategy globally, our business continues to expand through offerings such as membership, advertising, marketplace and fulfillment services, and financial services. These offerings represent mutually reinforcing pieces of our omnichannel model centered on our customers around the world who are increasingly seeking convenience.
> Information About Our Segments

### WMT-000010416926000055-0023

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 26826–27961

> Merchandise and Other Offerings. The merchandising strategy for Walmart International is similar to that of our operations in the U.S. in terms of the breadth and scope of merchandise offered for sale. While brand name merchandise accounts for a majority of our sales, we have both leveraged U.S. private brands and developed market specific private brands to serve our customers with high quality, low priced items. Along with the private brands we market globally, such as "Equate," "George," "Great Value," "Holiday Time," "Mainstays," "Marketside," "Member's Mark" and "Parent's Choice," our international markets have developed market specific brands including "Aurrera" and "Lider." In addition, we have developed and continue to grow our relationships with regional and local suppliers in each market to ensure reliable sources of quality merchandise that is equal to national brands at low prices. Consistent with its strategy, Walmart International continues to build mutually reinforcing businesses in areas such as advertising, marketplace and fulfillment services, financial services and healthcare.
> Sam's Club U.S. Segment

### WMT-000010416926000055-0027

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 31477–32779

> Competition. We compete with brick and mortar, eCommerce and omnichannel retailers operating discount, department, retail and wholesale grocery, drug, dollar, variety and specialty stores, supermarkets, supercenter-type stores, membership-only warehouse clubs, gasoline stations and social commerce platforms, as well as companies that offer services in digital advertising, fulfillment and delivery services, health and wellness and financial services. Our ability to develop and effectively operate different formats at the right locations and to deliver a customer-centric omnichannel experience largely determines our competitive position in the retail industry within the markets where we operate. Each of these landscapes is highly competitive and rapidly evolving, and new business models and the entry of new, well-funded competitors continue to intensify this competition. Some of our competitors have longer histories in these lines of business, more customers and greater brand recognition. They may be able to obtain more favorable terms from suppliers and business partners and to devote greater resources to the development of these businesses. In addition, for eCommerce and other internet-based businesses, newer or smaller businesses may be better able to innovate and compete with us.

### WMT-000010416926000055-0029

business, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 34261–34918

> •Opening new stores and clubs, as well as remodeling existing locations, to enhance the customer experience, support omnichannel capabilities, and strengthen our physical footprint in existing and new markets; and
> •Investing in technology, automation, and our associates to deliver growth, expand operating margins and improve returns.
> Seasonal Aspects of Operations. Our business is seasonal to a certain extent and varies by country due to different national and religious holidays, festivals and customs, as well as different weather patterns. Historically, our highest sales volume for each segment has occurred in the fourth quarter of our fiscal year.

### WMT-000010416926000055-0044

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 52833–54284

> ITEM 1A. RISK FACTORS
> The risks described below could, in ways we may or may not be able to accurately predict, materially and adversely affect our business, results of operations, financial position and liquidity. Our business operations could also be affected by additional factors that apply to all companies operating in the U.S. and globally. The following risk factors do not identify all risks that we may face. The disclosures below reflect our beliefs and opinions as to risk factors that could materially and adversely affect our business operations and our securities in the future. References to past events are provided by way of example only and are not intended to be a complete listing or a representation as to whether or not such risk factors have occurred in the past or their likelihood of occurring in the future.
> Strategic Risks
> Failure to successfully execute our omnichannel strategy and the cost of our investments in eCommerce and technology may materially adversely affect our market position, net sales and financial performance.
> The retail business continues to rapidly evolve with consumers embracing the digital shopping experience and expecting a robust online marketplace of goods available for purchase and delivery. As a result, the portion of total consumer expenditures with retailers and wholesale clubs occurring through digital platforms is increasing and the pace of this increase could continue to accelerate.

### WMT-000010416926000055-0056

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 65609–66757

> consumer credit, higher consumer debt levels, changes in consumer spending and shopping patterns, fluctuations in currency exchange rates, higher tax rates, imposition of new taxes or other changes in tax laws, changes in healthcare laws, other regulatory changes, the imposition of export and import restrictions, tariffs, trade barriers or other measures that create barriers to or increase the costs associated with international trade, overall economic slowdown or recession and other economic factors in the U.S., or in any of the other markets in which we operate, could adversely affect consumer demand for the products and services we sell in the U.S. or such other markets, change the mix of products we sell to any one or more markets with a lower average gross margin, cause a slowdown in discretionary purchases of goods, adversely affect our net sales, growth rates, operating income and result in slower inventory turnover and greater markdowns of inventory, or otherwise materially adversely affect our operations and operating results and could result in impairment charges to intangible assets, goodwill or other long-lived assets.

### WMT-000010416926000055-0090

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 103972–105452

> drugs customers purchase at our pharmacies between brands and generics); changes in the health insurance market generally; increased governmental focus on reducing drug prices including most favored nation pricing policies, maximum fair price negotiations, and direct-to-consumer pharmacy delivery models; changes in the scope of or the elimination of Medicare Part D or Medicaid drug programs; increased competition from other retail pharmacy operations including competitors offering online retail pharmacy options and/or home delivery options; further consolidation and strategic alliances among third-party payers, PBMs or purchasers of drugs; overall economic conditions and the ability of our pharmacy customers to pay for drugs prescribed for them to the extent the costs are not reimbursed by a third-party; failure to meet any performance or incentive thresholds to which our level of third-party reimbursement may be subject; changes in laws or regulations or the practices of third-party payers and PBMs related to the use of third-party financial assistance to assist our pharmacy customers with paying for drugs prescribed for them; and any additional changes in the state or federal regulatory environment for the retail pharmacy industry and the pharmaceutical industry, including as a result of health reform efforts and other changes to or novel interpretations of existing state or federal laws, rules and regulations that affect our retail pharmacy business.
> 20

### WMT-000010416926000055-0098

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 113788–115074

> During fiscal 2026, our Walmart International operations generated approximately 19% of our consolidated net sales. Walmart International's operations in various countries also source goods and services from other countries. Our future operating results in these countries could be negatively affected by a variety of factors, most of which are beyond our control. These factors include political conditions, including political instability, local and global economic conditions; legal and regulatory constraints, such as regulation of product and service offerings including regulatory restrictions (such as foreign ownership restrictions) on eCommerce and retail operations in international markets, such as in India; restrictive governmental actions, such as trade protection measures or nationalization; antitrust and competition law regulatory matters, such as those underway in Canada, Mexico and India (relating to our Flipkart subsidiary); local product safety and environmental laws; tax regulations; local labor laws; anti-money laundering laws and regulations; trade policies; foreign exchange or currency regulations; laws and regulations regarding consumer and data protection; and other matters in any of the countries or regions in which we operate, now or in the future.

### WMT-000010416926000055-0111

risk_factors, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 128129–129197

> Additionally, through various financial service partners and our OnePay fintech venture, we offer various services such as money transfers, digital payment platforms, bill payment, money orders, check cashing, prepaid access, co-branded credit cards, limited access to cryptocurrency and equity investment products, installment lending and earned wage access. These products and services require us to comply with legal and regulatory requirements, including those intended to help detect and prevent fraud and other illicit activity, the sale and custody of equity and cryptocurrency products, privacy, information security, anti-money laundering and sanctions regimes and consumer protection under U.S. state and federal laws and regulations, as well as those of certain other countries. Failure to comply with these laws and regulations could result in fines, sanctions, penalties and harm to our reputation. Increased U.S. regulation of non-bank financial institutions may also result in additional requirements and scrutiny of certain financial services we offer.

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

### WMT-000010416926000055-0256

debt_note, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 291736–292607

> Note 5. Short-term Borrowings and Long-term Debt
> Short-term borrowings consist of commercial paper and lines of credit. Short-term borrowings as of January 31, 2026 and 2025 were $6.6 billion and $3.1 billion, respectively, with weighted-average interest rates of 4.0% and 5.3%, respectively.
> The Company has various committed lines of credit in the U.S. to support its commercial paper program which are summarized in the following table:
> January 31, 2026 January 31, 2025
> (Amounts in millions) Available Drawn Undrawn Available Drawn Undrawn
> Five-year credit facility(1)
> $ 5,000 $ — $ 5,000 $ 5,000 $ — $ 5,000
> 364-day revolving credit facility(1)
> 10,000 — 10,000 10,000 — 10,000
> Total $ 15,000 $ — $ 15,000 $ 15,000 $ — $ 15,000
> (1)In April 2025, the Company renewed and extended its existing 364-day revolving credit facility as well as its five year credit facility.

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

### WMT-000010416926000055-0258

debt_note, [10-K for 2026-01-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/wmt-20260131.htm), characters 294063–295540

> (1)The average rate represents the weighted-average stated rate for each corresponding debt category, based on year-end balances and year-end interest rates.
> (2)Includes deferred loan costs, discounts, fair value hedges, foreign-held debt and secured debt.
> Annual maturities of long-term debt during the next five years and thereafter are as follows:
> (Amounts in millions) Annual
> Fiscal Year Maturities
> 2027 $ 3,542
> 2028 3,237
> 2029 3,389
> 2030 2,143
> 2031 2,600
> Thereafter 23,255
> Total $ 38,166
> Debt Issuances
> Information on significant issuances of long-term debt during fiscal 2026, for general corporate purposes, is as follows:
> (Amounts in millions)
> Issue Date Principal Amount Maturity Date Interest Rate Net Proceeds
> April 28, 2025 $750 April 28, 2027 Floating $ 749
> April 28, 2025 $750 April 28, 2027 4.100% 748
> April 28, 2025 $1,000 April 28, 2030 4.350% 993
> April 28, 2025 $1,500 April 28, 2035 4.900% 1,493
> Total $ 3,983
> These issuances are senior, unsecured notes which rank equally with all other senior, unsecured debt obligations of the Company, and are not convertible or exchangeable. These issuances do not contain any financial covenants which restrict the Company's ability to pay dividends or repurchase Company stock.
> Maturities
> The following tables provide details of significant long-term debt maturities during fiscal 2026 and 2025, respectively:
> (Amounts in millions)
> Maturity Date Principal Amount Interest Rate Repayment
> June 26, 2025 $875 3.550% $ 875

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

### WMT-000010416926000102-0062

liquidity, [10-Q for 2026-04-30](https://www.sec.gov/Archives/edgar/data/104169/000010416926000102/wmt-20260430.htm), characters 77282–78766

> Net cash used in investing activities for the three months ended April 30, 2026 increased $1.6 billion when compared to the same period in the previous fiscal year. The increase was primarily due to increased payments for property and equipment.
> 24
> Table of Contents
> Net Cash Provided by Financing Activities
> Three Months Ended April 30,
> (Amounts in millions) 2026 2025
> Net cash provided by financing activities $ 2,328 $ 8
> Net cash provided by financing activities increased $2.3 billion for the three months ended April 30, 2026, when compared to the same period in the previous fiscal year. The increase was primarily due to lower share repurchases and higher short-term borrowings, primarily offset by debt repayments in the current fiscal year.
> In April 2026, the Company renewed and extended its existing 364-day revolving credit facility of $10.0 billion as well as its five-year credit facility of $5.0 billion. In total, we had committed lines of credit in the U.S. of $15.0 billion at April 30, 2026, all undrawn.
> Long-term Debt
> The following table provides the changes in our long-term debt for the three months ended April 30, 2026:
> (Amounts in millions) Long-term debt due within one year Long-term debt Total
> Balances as of February 1, 2026 $ 3,542 $ 34,624 $ 38,166
> Proceeds from issuance of long-term debt(1)
> — 4,230 4,230
> Repayments of long-term debt (1,504) — (1,504)
> Reclassifications of long-term debt 1,873 (1,873) —
> Currency and other adjustments
> (15) (94) (109)

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

### WMT-000010416926000154-0043

mdna, [10-Q for 2026-07-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm), characters 52809–54308

> The Company engaged in the process established by the U.S. Customs and Border Protection ("CBP") for refunds of tariffs that the Company paid as the importer of record under the International Emergency Economic Powers Act. During the quarter ended July 31, 2026, the Company received approximately $2.9 billion in tariff refunds pursuant to the CBP process, which were recorded as a reduction to cost of sales and represent substantially all of the refunds requested by the Company. A significant portion of these refunds was invested into customer-focused initiatives during the current quarter, primarily through price investment and other cost mitigation strategies, with continued prioritization of price investment expected through fiscal 2027.
> For a detailed discussion on results of operations by reportable segment, refer to "Results of Operations" below.
> Company Performance Metrics
> We are committed to helping customers save money and live better through everyday low prices, supported by everyday low costs. At times, we adjust our business strategies to maintain and strengthen our competitive positions in the countries in which we operate. We define our financial priorities as follows:
> •Growth - serve customers through a seamless omnichannel experience;
> •Margin - improve our operating income margin through productivity initiatives as well as category and business mix; and
> •Returns - improve our Return on Investment through margin improvement and disciplined capital spend.
> Growth

### WMT-000010416926000154-0052

mdna, [10-Q for 2026-07-31](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm), characters 64487–65852

> Our strategy includes allocating the majority of our capital to higher-return areas focused on automation such as eCommerce, supply chain and store and club investments. The following table provides additional detail regarding our capital expenditures:
> (Amounts in millions) Six Months Ended July 31,
> Allocation of Capital Expenditures 2026 2025
> Supply chain, customer-facing initiatives, technology and other
> $ 7,659 $ 6,688
> Store and club remodels 3,623 2,917
> New stores and clubs, including expansions and relocations 1,087 577
> Total U.S. $ 12,369 $ 10,182
> Walmart International 1,812 1,227
> Total Capital Expenditures $ 14,181 $ 11,409
> Free Cash Flow
> Free cash flow is considered a non-GAAP financial measure. Management believes, however, that free cash flow, which measures our ability to generate additional cash from our business operations, is an important financial measure for use in evaluating the Company's financial performance. Free cash flow should be considered in addition to, rather than as a substitute for, consolidated net income as a measure of our performance and net cash provided by operating activities as a measure of our liquidity. See Liquidity and Capital Resources for discussions of GAAP metrics including net cash provided by operating activities, net cash used in investing activities and net cash provided by financing activities.

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

Run `WMT-20261118T070358Z-DeepSeek-V4.1-Flash-1017`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 7 calls, 30,500 input (21,773 cached) and 18,967 output tokens, $0.0066, 427s. Verification: 33 calls, 17,507 input (4,224 cached) and 3,136 output tokens, $0.0234, 47s. Prices read 2026-11-17. Raw requests and responses: data/runs/WMT/WMT-20261118T070358Z-DeepSeek-V4.1-Flash-1017.jsonl.
