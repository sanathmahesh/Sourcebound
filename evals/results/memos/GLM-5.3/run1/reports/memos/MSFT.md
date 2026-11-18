# Credit memo: MICROSOFT CORP (MSFT)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `zai-org/GLM-5.3`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-1**.
Sources: [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm); [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)

Claims: 36 — 31 supported, 5 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 1; repairs: 2.

## Business profile

1. Microsoft is a technology company that creates platforms and applications powered by AI, with a mission to empower every person and every organization on the planet to achieve more.  
   ✅ supported (judge): The passage states verbatim that Microsoft is a technology company with that mission that creates AI-powered platforms and applications.
   - cites `MSFT-000119312526436133-0051` ✓: “Microsoft is a technology company committed to making digital technology and artificial intelligence (“AI”) available broadly and doing so responsibly”
2. The company operates and reports its financial performance through three segments: Productivity and Business Processes, Intelligent Cloud, and More Personal Computing.  
   ✅ supported (judge): The passage explicitly states the company reports through the three named segments.
   - cites `MSFT-000119312526323660-0010` ✓: “We operate our business and report our financial performance using three segments: Productivity and Business Processes, Intelligent Cloud, and More Personal Computing.”
3. The Productivity and Business Processes segment comprises Microsoft **365** [quoted: MSFT-000119312526323660-0011] Commercial and Consumer products and cloud services, LinkedIn, and Dynamics products and cloud services.  
   ✅ supported (judge): The passage lists exactly those components for the segment.
   - cites `MSFT-000119312526323660-0011` ✓: “LinkedIn, including Talent Solutions, Marketing Solutions, Premium Subscriptions, and Sales Solutions.”
   - cites `MSFT-000119312526323660-0011` ✓: “Microsoft 365 Commercial products and cloud services, including Microsoft 365 Commercial cloud, comprising Microsoft 365 Commercial, Enterprise Mobility + Security”
4. The company operates at substantial scale, with revenue of **$346.4 billion** [F1] in the twelve months to 30 September 2026, up from **$245.1 billion** [F2] in the fiscal year ended 30 June 2024, and EBITDA of **$205.7 billion** [F3] in the twelve months to 30 September 2026.  
   ✅ supported (judge): All three figures (LTM revenue $346.4B, FY2024 revenue $245.1B, LTM EBITDA $205.7B) match the computed XBRL metric values exactly.
5. Azure competes with other cloud service providers, and the company believes its hybrid cloud capability, global scale, and broad security portfolio differentiate it from competitors.  
   ✅ supported (judge): The passage states Azure faces competition from cloud providers, and that hybrid cloud, global scale, and broad security portfolio differentiate it from competitors.
   - cites `MSFT-000119312526323660-0019` ✓: “Azure’s competitive advantage includes enabling a hybrid cloud, allowing deployment of existing datacenters with our public cloud into a single, cohesive infrastructure”
   - cites `MSFT-000119312526323660-0019` ✓: “We believe our cloud’s global scale, coupled with our broad portfolio of identity and security solutions, allows us to effectively solve complex cybersecurity challenges for our customers”
6. Cash flow stability is supported by the company's demonstrated commitment to returning capital to shareholders, having declared dividends totaling $**27.0** [quoted: MSFT-000119312526323660-0158] billion and $**24.7** [quoted: MSFT-000119312526323660-0158] billion during the fiscal year ended 30 June 2026 and the fiscal year ended 30 June 2025, respectively.  
   ✅ supported (judge): The passage states dividends of $27.0 billion and $24.7 billion for fiscal 2026 and 2025 and the intent to continue returning capital to shareholders.
   - cites `MSFT-000119312526323660-0158` ✓: “our Board of Directors declared dividends totaling $27.0 billion and $24.7 billion, respectively. We intend to continue returning capital to shareholders”

## Financial risk

1. Debt / EBITDA was stable and low, easing from **0.61x** [F4] in the fiscal year ended 30 June 2024 to **0.52x** [F5] on an LTM basis, as EBITDA grew faster than debt.  
   ✅ supported (judge): The two metric values confirm Debt/EBITDA eased from 0.61x (FY ended 30 June 2024) to 0.52x on an LTM basis; a decline in the ratio implies EBITDA grew faster than debt, and these are low leverage levels.
2. Net leverage worsened over the period, moving from a net cash position of **-0.03x (net cash)** [F6] in the fiscal year ended 30 June 2025 to **0.20x** [F7] at LTM.  
   ✅ supported (judge): The metric values match the claim exactly: net leverage of -0.03x (net cash) in FY ended 30 June 2025 increasing to 0.20x at LTM, indicating worsening leverage.
3. EBITDA / interest improved from **44.10x** [F8] in the fiscal year ended 30 June 2024 to **63.82x** [F9] at LTM, leaving debt service coverage very high.  
   ✅ supported (judge): The metric values match the claim exactly: EBITDA/interest was 44.10x in FY ended 30 June 2024 and improved to 63.82x at LTM, a level that is very high coverage; 'very high' follows directly from these figures.
4. FCF / debt worsened, declining from **94.0%** [F10] in the fiscal year ended 30 June 2024 to **56.3%** [F11] at LTM, as capital expenditure of **$135.9 billion** [F12] absorbed much of the **$195.9 billion** [F13] in cash from operations.  
   ✅ supported (judge): All figures in the claim match the metric values exactly.
5. Microsoft has continued to repay rather than raise borrowings, with recent quarters showing increased cash used for repayments of debt, which helped keep Debt / EBITDA stable.  
   ◐ partially supported (judge): Increased cash used for debt repayments is supported, but the evidence does not show that repayments exceeded borrowings or that Debt/EBITDA remained stable; it also notes Microsoft actively issues debt.
   - cites `MSFT-000119312526436133-0075` ✓: “primarily due to a $4.9 billion increase in cash used for repayments of debt”
6. The deterioration in free cash flow relative to debt and the shift from a net cash position reflect a surge in capital spending on AI infrastructure, with cash used in investing up on a $**20.0** [quoted: MSFT-000119312526436133-0075] billion increase in additions to property and equipment.  
   ◐ partially supported (judge): The $20.0 billion increase in additions to property and equipment driving higher cash used in investing is supported, but the claim's framing about free cash flow relative to debt and a shift from a net cash position is not addressed by the evidence; also AI infrastructure link is only indirect.
   - cites `MSFT-000119312526436133-0075` ✓: “primarily due to a $20.0 billion increase in additions to property and equipment and a $6.7 billion increase in cash used in other investing primarily to facilitate the purchase of components”
   - cites `MSFT-000119312526323660-0138` ✓: “Microsoft Cloud gross margin percentage decreased to 66% driven by continued investments in AI infrastructure and growing AI product usage”

## Liquidity

1. Liquidity coverage stood at **1.56x** [F14] in the twelve months to 30 September 2026, down from **1.71x** [F15] in the fiscal year ended 30 June 2026, indicating that liquidity sources still cover the next twelve months' needs but with a reduced cushion.  
   ✅ supported (judge): The metric values confirm liquidity coverage of 1.56x for the twelve months to 30 September 2026 versus 1.71x for FY ended 30 June 2026, and since both exceed 1.0x, liquidity sources cover the next twelve months' needs with a smaller cushion.
2. Liquidity sources over the twelve months to 30 September 2026 comprised **$20.3 billion** [F16] of cash, **$44.2 billion** [F17] of short-term investments and **$195.9 billion** [F13] of cash from operations, against **$4.4 billion** [F18] of short-term debt, **$135.9 billion** [F12] of capital expenditure and **$27.0 billion** [F19] of dividends paid.  
   ✅ supported (judge): Every figure in the claim matches the corresponding LTM metric value computed from the XBRL data.
3. The liquidity coverage calculation assumes undrawn revolving credit capacity of **$0** [F20], as no undrawn revolver was reported, so coverage relies entirely on balance-sheet liquidity and operating cash flow.  
   ◐ partially supported (judge): The $0 undrawn revolver figure is an assumption from missing data (marked 'assumed zero: not reported'), so the first part is consistent with the evidence, but the assertion that coverage relies entirely on balance-sheet liquidity and operating cash flow goes beyond what the evidence shows.
4. Management states that existing cash, cash equivalents, short-term investments, cash flows from operations and access to capital markets are expected to be sufficient to fund operating activities and cash commitments, including dividends, debt maturities and material capital expenditures, for at least the next twelve months.  
   ✅ supported (judge): The claim accurately paraphrases management's statement in the liquidity section.
   - cites `MSFT-000119312526436133-0071` ✓: “sufficient to fund our operating activities and cash commitments for investing and financing activities, such as dividends, share repurchases, debt maturities, and material capital expenditures, for at least the next 12 months”
5. Cash, cash equivalents and short-term investments declined over the twelve months to 30 September 2026 relative to the fiscal year ended 30 June 2026, which narrows the liquidity buffer even though coverage remains above one times.  
   ◐ partially supported (judge): The decline from $76.8B to $64.5B is supported, but the evidence provides no coverage metric to support the 'coverage remains above one times' claim.
   - cites `MSFT-000119312526436133-0072` ✓: “Cash, cash equivalents, and short-term investments totaled $64.5 billion and $76.8 billion”
6. The short-term investment portfolio is well suited to liquidity purposes, consisting predominantly of highly liquid, investment-grade fixed-income securities diversified across issuers, with insignificant settlement risk.  
   ✅ supported (judge): The passage directly states the portfolio is for liquidity, consists predominantly of highly liquid investment-grade fixed-income securities diversified among issuers, with insignificant settlement risk.
   - cites `MSFT-000119312526436133-0072` ✓: “They consist predominantly of highly liquid investment-grade fixed-income securities, diversified among industries and individual issuers.”

## Maturity wall

1. Based on the maturity schedule as of the fiscal year ended 30 June 2026, long-term debt maturing over the next five years amounts to **$9.2 billion** [F21] in year one, **$0** [F22] in year two, **$2.0 billion** [F23] in year three, **$0** [F24] in year four, and **$500 million** [F25] in year five, with **$34.4 billion** [F26] due thereafter.  
   ✅ supported (judge): The maturity table as of June 30, 2026 matches all claim figures: 2027 $9,250M, 2028 $0, 2029 $2,001M, 2030 $0, 2031 $500M, thereafter $34,385M.
   - cites `MSFT-000119312526323660-0220` ✓: “The following table outlines maturities of our long-term debt, including the current portion, as of June 30, 2026:”
2. Of total debt of **$106.9 billion** [F27], only **8.6%** [F28], or **$9.2 billion** [F29], falls due within the next two years, indicating a limited near-term maturity wall.  
   ✅ supported (judge): Total debt ($106.9B), 8.6% share, and $9.2B due within 24 months all match the computed XBRL metrics; the 'limited near-term maturity wall' conclusion follows directly from a small near-term share.
3. Near-term maturity cover stands at **0.12x** [F30], reflecting **$20.9 billion** [F31] of cash and cash equivalents against **$9.2 billion** [F32] of short-term debt and no reported undrawn revolving credit capacity.  
   ✅ supported (judge): All claimed figures (0.12x cover, $20.9 billion cash, $9.2 billion short-term debt, and no reported undrawn revolver) match the computed metric values exactly, including the note that undrawn revolver capacity was assumed zero because it was not reported.
4. Management states that existing cash, short-term investments, cash flows from operations, and access to capital markets are expected to be sufficient to fund debt maturities for at least the next twelve months and for the foreseeable future.  
   ✅ supported (judge): Both passages state existing cash, short-term investments, cash flows from operations, and access to capital markets are expected to fund debt maturities and other commitments for at least the next 12 months and for the foreseeable future.
   - cites `MSFT-000119312526323660-0150` ✓: “We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities”
   - cites `MSFT-000119312526436133-0071` ✓: “such as dividends, share repurchases, debt maturities, and material capital expenditures, for at least the next 12 months and thereafter for the foreseeable future.”
5. The debt consists of senior unsecured obligations that rank equally with the company's other outstanding obligations, with interest paid semi-annually except for Euro-denominated debt, which is paid annually.  
   ✅ supported (judge): The passage states exactly that debt is senior unsecured, ranks equally with other obligations, and interest is paid semi-annually except Euro-denominated debt paid annually.
   - cites `MSFT-000119312526323660-0220` ✓: “Debt in the table above is comprised of senior unsecured obligations and ranks equally with our other outstanding obligations. Interest is paid semi-annually, except for the Euro-denominated debt, which is paid annually.”
6. The company issues debt to take advantage of favorable pricing and liquidity in the debt markets, and proceeds may be used for general corporate purposes including repayment of existing debt, indicating reliance on capital markets access for refinancing flexibility.  
   ✅ supported (judge): The passage directly states debt is issued for favorable pricing/liquidity in debt markets and proceeds may be used for general corporate purposes including repayment of existing debt; the refinancing-flexibility characterization follows directly from this disclosure.
   - cites `MSFT-000119312526323660-0155` ✓: “We issue debt to take advantage of favorable pricing and liquidity in the debt markets, reflecting our credit rating.”
   - cites `MSFT-000119312526436133-0075` ✓: “which may include, among other things, funding for working capital, capital expenditures, repurchases of capital stock, acquisitions, and repayment of existing debt.”

## Key risks

1. Microsoft's cloud and AI infrastructure buildout requires substantial and increasing capital expenditures and continued access to capital ahead of fully developed revenue streams, and adverse changes in interest rates, credit markets, or the company's credit ratings could raise its cost of capital or limit its ability to fund these investments.  
   ✅ supported (judge): The passage directly states both the substantial and increasing capex ahead of revenue streams and the risk that adverse interest rate, credit market, or credit rating changes could raise capital costs or limit funding.
   - cites `MSFT-000119312526436133-0100` ✓: “require substantial and increasing capital expenditures and continued access to capital, and are in advance of fully developed revenue streams”
   - cites `MSFT-000119312526436133-0100` ✓: “Funding these investments depends on our ability to generate sufficient cash flows and obtain financing on acceptable terms.”
2. The cost structure for AI products and services is subject to significant uncertainty, and if model training and inference costs, component, or energy costs increase or remain elevated while AI pricing declines, the company's margins, financial condition, and results of operations could be adversely affected.  
   ✅ supported (judge): The passage directly states every element of the claim about AI cost structure uncertainty and potential adverse effects on margins, financial condition, and results of operations.
   - cites `MSFT-000119312526436133-0102` ✓: “The cost structure for AI products and services is subject to significant uncertainty, including with respect to model training and inference costs”
3. Adverse economic or market conditions, including inflation, recession, or shifts in customer demand and technology investment cycles, could cause lower or delayed IT spending, disrupt the company's distribution channels, and increase allowances for doubtful accounts and write-offs of accounts receivable if customers' ability to pay is impaired.  
   ✅ supported (judge): All elements of the claim—lower/delayed IT spending, distribution channel disruption, and increased allowances/write-offs from impaired customer payment ability—are directly stated in the evidence.
   - cites `MSFT-000119312526436133-0159` ✓: “impair our customers’ ability to pay amounts owed, resulting in increased allowances for doubtful accounts and write-offs of accounts receivable”
   - cites `MSFT-000119312526323660-0103` ✓: “may cause lower or delayed IT spending and adversely affect our results of operations”
4. The company's investment portfolio is exposed to credit, liquidity, market, and interest rate risks that may be exacerbated by market downturns or a downgrade of the U.S. government credit rating, potentially requiring impairment charges that could adversely affect its financial condition and results of operations.  
   ✅ supported (judge): The claim accurately summarizes the passage: investments subject to credit, liquidity, market, and interest rate risks, exacerbated by market downturns or a U.S. government credit rating downgrade, potentially requiring impairment charges adversely affecting financial condition and results of operations.
   - cites `MSFT-000119312526436133-0160` ✓: “These investments are subject to general credit, liquidity, market, and interest rate risks, which may be exacerbated by market downturns”
5. Rapidly evolving AI legislation and regulation across multiple jurisdictions, including the EU's AI Act and new U.S. state audit and evaluation obligations for advanced AI models, may increase costs or restrict the provision and operation of the company's AI models and services.  
   ✅ supported (judge): The claim accurately paraphrases the passage, which states AI legislative and regulatory action is evolving rapidly across multiple jurisdictions, and specifically cites the EU AI Act and new U.S. state external audit/evaluation obligations as potentially increasing costs or impacting AI models and services.
   - cites `MSFT-000119312526436133-0144` ✓: “the EU’s AI Act may increase costs or impact the provision or operation of our AI models and services in the European market”
6. These risks should be weighed against the company's substantial debt-service capacity in the twelve months to 30 September 2026, with debt to EBITDA of **0.52x** [F5], interest coverage of **63.82x** [F9], and free cash flow to debt of **56.3%** [F11].  
   ✅ supported (judge): All three metrics (debt/EBITDA 0.52x, interest coverage 63.82x, FCF/debt 56.3%) match the scorecard for the twelve months to 30 September 2026, and the passage confirms substantial investment risks requiring cash flow generation and financing.
   - cites `MSFT-000119312526436133-0100` ✓: “Funding these investments depends on our ability to generate sufficient cash flows and obtain financing on acceptable terms.”

## Rating rationale

1. The SB grade for MICROSOFT CORP is **SB-1** [F33], based on a weighted score of **1.30** [F34], and this is a stylized internal scorecard grade, not a credit rating.  
   ✅ supported (judge): The scorecard metrics confirm SB grade SB-1 with weighted score 1.30, described as a stylized scorecard grade, not a credit rating.
2. The scorecard is strongest on debt service and balance sheet measures, with debt to EBITDA at **0.52x** [F5] (band **1** [F35], weight **20.0%** [F36]), net leverage at **0.20x** [F7] (band **1** [F37], weight **10.0%** [F38]), interest coverage at **63.82x** [F9] (band **1** [F39], weight **25.0%** [F40]), free cash flow to debt at **56.3%** [F11] (band **1** [F41], weight **20.0%** [F42]), and near-term maturity cover at **0.12x** [F30] (band **1** [F43], weight **10.0%** [F44]), all in the strongest band.  
   ◐ partially supported (judge): All five listed metrics, values, bands, and weights match the evidence, but the claim that the scorecard is strongest on debt service and balance sheet measures overall is contradicted by liquidity coverage at band 3 of 6 (weight 15%), so 'all in the strongest band' overstates it.
3. The weakest factor is liquidity coverage, which stands at **1.56x** [F14] in band **3** [F45] with a weight of **15.0%** [F46].  
   ✅ supported (judge): Liquidity coverage is 1.56x, in band 3 of 6, weighted 15.0%, and all other factors are in band 1, making it the weakest factor.
4. The grade is not provisional, because all six factors were scored, with band results ranging from **1** [F39] on the strongest factors to **3** [F45] on the weakest.  
   ✅ supported (judge): The scorecard confirms the grade is not provisional with all six factors scored, and band results range from 1 (strongest factors) to 3 (liquidity).
5. The grade is supported by management's statement that existing cash, short-term investments, cash flows from operations, and access to capital markets are expected to be sufficient to fund operating activities and cash commitments, including debt maturities and material capital expenditures, for at least the next twelve months and for the foreseeable future.  
   ✅ supported (judge): The passage states exactly that cash, short-term investments, operating cash flows, and capital markets access are expected to fund operating activities and cash commitments including debt maturities and material capital expenditures for at least the next 12 months and the foreseeable future.
   - cites `MSFT-000119312526436133-0071` ✓: “We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities”
6. The grade is tempered by the company's cloud and AI infrastructure buildout, which requires substantial and increasing capital expenditures and continued access to capital ahead of fully developed revenue streams, meaning adverse changes in interest rates, credit markets, or the company's credit ratings could raise its cost of capital or limit its ability to fund these investments.  
   ✅ supported (judge): The passage directly states the cloud/AI infrastructure buildout requires substantial and increasing capex and continued access to capital ahead of fully developed revenue streams, and that adverse changes in interest rates, credit markets, or credit ratings could raise cost of capital or limit investment funding.
   - cites `MSFT-000119312526436133-0100` ✓: “require substantial and increasing capital expenditures and continued access to capital, and are in advance of fully developed revenue streams”

## Reviewer checklist

- [ ] **fallback** (info): Revenue: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Depreciation and amortisation: used rank 4 Depreciation + AmortizationOfIntangibleAssets in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Finance-lease liabilities (current plus non-current): used rank 2 FinanceLeaseLiability in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Dividends paid: used rank 2 PaymentsOfDividendsCommonStock in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Interest expense: used rank 2 InterestExpenseNonoperating in FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): ShortTermBorrowings assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): CommercialPaper assumed zero (not reported) in FY0, LTM.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **reconciliation** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $78,775m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $72,082m (-8.5%). Check which matches the balance sheet.
- [ ] **reconciliation** (warning): maturity ladder $46,136m + short-term borrowings $0m + finance leases $66,594m = $112,730m, against total debt $106,888m (+5.5%)
- [ ] **partially supported claim** (warning): Financial risk: partially supported (Increased cash used for debt repayments is supported, but the evidence does not show that repayments exceeded borrowings or that Debt/EBITDA remained stable; it also notes Microsoft actively issues debt.): “Microsoft has continued to repay rather than raise borrowings, with recent quarters showing increased cash used for repayments of debt, which helped keep Debt / EBITDA stable.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The $20.0 billion increase in additions to property and equipment driving higher cash used in investing is supported, but the claim's framing about free cash flow relative to debt and a shift from a net cash position is not addressed by the evidence; also AI infrastructure link is only indirect.): “The deterioration in free cash flow relative to debt and the shift from a net cash position reflect a surge in capital spending on AI infrastructure, with cash used in investing up on a $20.0 billion increase in additions to property and equipment.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The $0 undrawn revolver figure is an assumption from missing data (marked 'assumed zero: not reported'), so the first part is consistent with the evidence, but the assertion that coverage relies entirely on balance-sheet liquidity and operating cash flow goes beyond what the evidence shows.): “The liquidity coverage calculation assumes undrawn revolving credit capacity of $0, as no undrawn revolver was reported, so coverage relies entirely on balance-sheet liquidity and operating cash flow.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The decline from $76.8B to $64.5B is supported, but the evidence provides no coverage metric to support the 'coverage remains above one times' claim.): “Cash, cash equivalents and short-term investments declined over the twelve months to 30 September 2026 relative to the fiscal year ended 30 June 2026, which narrows the liquidity buffer even though coverage remains above one times.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (All five listed metrics, values, bands, and weights match the evidence, but the claim that the scorecard is strongest on debt service and balance sheet measures overall is contradicted by liquidity coverage at band 3 of 6 (weight 15%), so 'all in the strongest band' overstates it.): “The scorecard is strongest on debt service and balance sheet measures, with debt to EBITDA at 0.52x (band 1, weight 20.0%), net leverage at 0.20x (band 1, weight 10.0%), interest coverage at 63.82x (band 1, weight 25.0%), free cash flow to debt at 56.3% (band 1, weight 20.0%), and near-term maturity cover at 0.12x (band 1, weight 10.0%), all in the strongest band.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:LTM) | $346.4 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 331,839,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 92,279,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 77,673,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F2 | Revenue (revenue:FY-2) | $245.1 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 245,122,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F3 | EBITDA (ebitda:LTM) | $205.7 billion | operating_income + d_and_a | OperatingIncomeLoss 155,237,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>OperatingIncomeLoss 45,915,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>OperatingIncomeLoss 37,961,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>Depreciation 34,300,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>Depreciation 11,100,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>Depreciation 7,100,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>AmortizationOfIntangibleAssets 4,700,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>AmortizationOfIntangibleAssets 1,000,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F4 | Debt / EBITDA (debt_to_ebitda:FY-2) | 0.61x | total_debt / EBITDA | LongTermDebtNoncurrent 42,688,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>LongTermDebtCurrent 2,249,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>CommercialPaper 6,693,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>FinanceLeaseLiability 27,145,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>OperatingIncomeLoss 109,433,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>Depreciation 15,200,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>AmortizationOfIntangibleAssets 4,800,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F5 | Debt / EBITDA (debt_to_ebitda:LTM) | 0.52x | total_debt / EBITDA | LongTermDebtNoncurrent 31,090,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtCurrent 4,391,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>FinanceLeaseLiability 70,973,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>OperatingIncomeLoss 155,237,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>OperatingIncomeLoss 45,915,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>OperatingIncomeLoss 37,961,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>Depreciation 34,300,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>Depreciation 11,100,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F6 | Net leverage (net_leverage:FY-1) | -0.03x (net cash) | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 40,152,000,000 (at 2025-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>LongTermDebtCurrent 2,999,000,000 (at 2025-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>CommercialPaper 0 (at 2025-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>FinanceLeaseLiability 46,172,000,000 (at 2025-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 30,242,000,000 (at 2025-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>ShortTermInvestments 64,323,000,000 (at 2025-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>OperatingIncomeLoss 128,528,000,000 (2024-07-01 to 2025-06-30, FY-1) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>Depreciation 22,000,000,000 (2024-07-01 to 2025-06-30, FY-1) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F7 | Net leverage (net_leverage:LTM) | 0.20x | (total_debt - cash - short_term_investments) / EBITDA | LongTermDebtNoncurrent 31,090,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtCurrent 4,391,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>FinanceLeaseLiability 70,973,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 20,281,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>ShortTermInvestments 44,228,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>OperatingIncomeLoss 155,237,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>OperatingIncomeLoss 45,915,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>OperatingIncomeLoss 37,961,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F8 | EBITDA / interest (interest_coverage:FY-2) | 44.10x | EBITDA / interest_expense | OperatingIncomeLoss 109,433,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>Depreciation 15,200,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>AmortizationOfIntangibleAssets 4,800,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>InterestExpense 2,935,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0000950170-24-087843](https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/0000950170-24-087843-index.htm) |
| F9 | EBITDA / interest (interest_coverage:LTM) | 63.82x | EBITDA / interest_expense | OperatingIncomeLoss 155,237,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>OperatingIncomeLoss 45,915,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>OperatingIncomeLoss 37,961,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>Depreciation 34,300,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>Depreciation 11,100,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>Depreciation 7,100,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>AmortizationOfIntangibleAssets 4,700,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>AmortizationOfIntangibleAssets 1,000,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F10 | FCF / debt (fcf_to_debt:FY-2) | 94.0% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 118,548,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 44,477,000,000 (2023-07-01 to 2024-06-30, FY-2) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>LongTermDebtNoncurrent 42,688,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>LongTermDebtCurrent 2,249,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>CommercialPaper 6,693,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm)<br>FinanceLeaseLiability 27,145,000,000 (at 2024-06-30, balance sheet) [10-K 0000950170-25-100235](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| F11 | FCF / debt (fcf_to_debt:LTM) | 56.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 182,935,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 58,000,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 45,057,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 115,948,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 39,367,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 19,394,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtNoncurrent 31,090,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtCurrent 4,391,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F12 | Capital expenditure (capex:LTM) | $135.9 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 115,948,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 39,367,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 19,394,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F13 | Cash from operations (cfo:LTM) | $195.9 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 182,935,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 58,000,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 45,057,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F14 | Liquidity coverage (liquidity_coverage:LTM) | 1.56x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 20,281,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>ShortTermInvestments 44,228,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 182,935,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 58,000,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 45,057,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtCurrent 4,391,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 115,948,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 39,367,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F15 | Liquidity coverage (liquidity_coverage:FY0) | 1.71x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 20,935,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>ShortTermInvestments 55,908,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 182,935,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 115,948,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>PaymentsOfDividendsCommonStock 26,445,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F16 | Cash and cash equivalents (cash:LTM) | $20.3 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 20,281,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F17 | Short-term investments (short_term_investments:LTM) | $44.2 billion | rank 1: ShortTermInvestments | ShortTermInvestments 44,228,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F18 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $4.4 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 4,391,000,000 (at 2026-09-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F19 | Dividends paid (dividends:LTM) | $27.0 billion | rank 2: PaymentsOfDividendsCommonStock | PaymentsOfDividendsCommonStock 26,445,000,000 (2025-07-01 to 2026-06-30, FY0) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>PaymentsOfDividendsCommonStock 6,757,000,000 (2026-07-01 to 2026-09-30, current year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>PaymentsOfDividendsCommonStock 6,169,000,000 (2025-07-01 to 2025-09-30, prior-year year-to-date) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F20 | Undrawn revolving credit capacity (undrawn_revolver:LTM) | $0 |  | — |
| F21 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $9.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 9,250,000,000 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F22 | Debt maturing in year two (maturity_year_2:FY0) | $0 | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F23 | Debt maturing in year three (maturity_year_3:FY0) | $2.0 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 2,001,000,000 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F24 | Debt maturing in year four (maturity_year_4:FY0) | $0 | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 0 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F25 | Debt maturing in year five (maturity_year_5:FY0) | $500 million | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 500,000,000 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F26 | Debt maturing after year five (maturity_after_year_5:FY0) | $34.4 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 34,385,000,000 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F27 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $106.9 billion | rank 1: LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | LongTermDebtNoncurrent 31,067,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>FinanceLeaseLiability 66,594,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F28 | Share of debt due within 24 months (share_due_24m:FY0) | 8.6% | (short_term_debt + maturity_year_2) / total_debt | LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>LongTermDebtNoncurrent 31,067,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>FinanceLeaseLiability 66,594,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F29 | Debt due within 24 months (debt_due_24m:FY0) | $9.2 billion | short_term_debt + maturity_year_2 | LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| F30 | Near-term maturity cover (near_term_maturity_cover:FY0) | 0.12x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 0 (at 2026-06-30, balance sheet) [10-K 0001193125-26-323660](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 20,935,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm)<br>ShortTermInvestments 55,908,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F31 | Cash and cash equivalents (cash:FY0) | $20.9 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 20,935,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F32 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $9.2 billion | rank 2: LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper | LongTermDebtCurrent 9,227,000,000 (at 2026-06-30, balance sheet) [10-Q 0001193125-26-436133](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| F33 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 1.3 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F34 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 1.3 | sum of weight x band over the factors scored, divided by their weights | — |
| F35 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 1 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F36 | Debt / EBITDA: scorecard weight (weight_debt_to_ebitda:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F37 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 1 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |
| F38 | Net debt / EBITDA: scorecard weight (weight_net_leverage:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F39 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 1 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F40 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F41 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 1 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F42 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F43 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 1 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F44 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F45 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 3 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F46 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |

## Passages cited

### MSFT-000119312526323660-0010

business, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 13120–14546

> Leveraging Windows to fuel our cloud business, grow our share of the PC market, and drive increased engagement with our services like Microsoft Edge, Bing, Copilot, Microsoft Teams, Microsoft 365 Consumer, XBOX Game Pass, and more.
> Our future growth depends on our ability to transcend current product category definitions, business models, and sales motions.
> 4
> PART I
> Item 1
> Commitment to Sustainability
> Microsoft is committed to sustainability and our approach to addressing climate change starts with the sustainability of our own business. In 2020, we announced goals to become a carbon negative, water positive, and zero waste company by 2030. Since announcing these goals, we have seen major changes in both the technology sector and in our understanding of what it will take to meet our goals. More information about our progress toward these goals can be found in our annual Environmental Sustainability Report.
> OPERATING SEGMENTS
> We operate our business and report our financial performance using three segments: Productivity and Business Processes, Intelligent Cloud, and More Personal Computing. Our segments provide management with a comprehensive financial view of our key businesses. The segments enable the alignment of strategies and objectives across the development, sales, marketing, and services organizations, and they provide a framework for timely and rational allocation of resources within businesses.

### MSFT-000119312526323660-0011

business, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 14547–16030

> Additional information on our operating segments and geographic and product information is contained in Note 18 – Segment Information and Geographic Data of the Notes to Financial Statements (Part II, Item 8 of this Form 10-K).
> Our reportable segments are described below.
> Productivity and Business Processes
> Our Productivity and Business Processes segment consists of products and services in our portfolio of productivity, communication, and information services, spanning a variety of devices and platforms. This segment primarily comprises:
> •
> Microsoft 365 Commercial products and cloud services, including Microsoft 365 Commercial cloud, comprising Microsoft 365 Commercial, Enterprise Mobility + Security, the cloud portion of Windows Commercial, the per-user portion of Power BI, Exchange, SharePoint, Microsoft Teams, Microsoft 365 Security and Compliance, and Microsoft 365 Copilot; and Microsoft 365 Commercial products, comprising Windows Commercial on-premises and Office licensed on-premises.
> •
> Microsoft 365 Consumer products and cloud services, including Microsoft 365 Consumer subscriptions, Office licensed on-premises, and other consumer services.
> •
> LinkedIn, including Talent Solutions, Marketing Solutions, Premium Subscriptions, and Sales Solutions.
> •
> Dynamics products and cloud services, including Dynamics 365, comprising a set of intelligent, cloud-based applications across ERP, CRM, Power Apps, and Power Automate; and on-premises ERP and CRM applications.

### MSFT-000119312526323660-0019

business, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 23922–25240

> Enterprise and partner services assist customers in developing, deploying, and managing Microsoft server solutions, Microsoft desktop solutions, and conversational AI and ambient intelligent solutions, along with providing training and certification to developers and IT professionals on various Microsoft products.
> Competition
> Azure faces diverse competition from cloud service providers and open-source offerings. Azure’s competitive advantage includes enabling a hybrid cloud, allowing deployment of existing datacenters with our public cloud into a single, cohesive infrastructure, and the ability to run at a scale that meets the needs of businesses of all sizes and complexities. Our AI offerings compete with AI products from hyperscalers, as well as products from other emerging competitors and other open-source offerings, many of which are also current or potential partners. Our Azure Security offerings include our cloud security solution and our security information and event management solution, which compete with providers in the cybersecurity and cloud security space. We believe our cloud’s global scale, coupled with our broad portfolio of identity and security solutions, allows us to effectively solve complex cybersecurity challenges for our customers and differentiates us from the competition.

### MSFT-000119312526323660-0103

risk_factors, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 120177–121379

> Adverse economic or market conditions could harm our business. Worsening economic conditions, including inflation, recession, pandemic, or other changes in economic conditions, periods of economic uncertainty, evolution of customer demand, technology investment cycles, interest rates, foreign exchange rates, or the timing and mix of customer spending, may cause lower or delayed IT spending and adversely affect our results of operations. If demand for computing power, PCs, servers, and other computing devices declines, or consumer or business spending for those products declines, our results of operations could be adversely affected.
> Our product distribution system relies on an extensive partner and retail network. OEMs building devices that run our software have also been a significant means of distribution. The impact of economic conditions on our partners, such as the bankruptcy of a major distributor, OEM, or retailer, could cause sales channel disruption.
> Challenging economic conditions also may impair the ability of our customers to pay for products and services they have purchased. As a result, allowances for doubtful accounts and write-offs of accounts receivable may increase.

### MSFT-000119312526323660-0138

mdna, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 154840–156336

> Microsoft Cloud gross margin percentage decreased to 66% driven by continued investments in AI infrastructure and growing AI product usage, offset in part by efficiency gains in Azure and Microsoft 365 Commercial cloud.
> Operating expenses increased $4.9 billion or 7% driven by continued investments in research and development compute capacity, AI talent, and data to support product development that benefits the entire portfolio, impairment and other related expenses in our XBOX business, investments in commercial sales, and higher Copilot advertising expenses.
> Operating income increased $26.7 billion or 21% driven by growth in Productivity and Business Processes and Intelligent Cloud.
> Revenue and operating income both included a favorable foreign currency impact of 2%.
> 37
> PART II
> Item 7
> Current year net income and diluted EPS were positively impacted by net gains from investments in OpenAI, which resulted in an increase in net income and diluted EPS of $5.0 billion and $0.67, respectively. Prior year net income and diluted EPS were negatively impacted by net losses from investments in OpenAI, which resulted in a decrease in net income and diluted EPS of $3.6 billion and $0.49, respectively.
> SEGMENT RESULTS OF OPERATIONS
> (In millions, except percentages)
> 2026
> 2025
> Percentage
> Change
> Productivity and Business Processes
> Revenue
> $
> 139,996
> $
> 120,810
> 16%
> Cost of revenue
> 25,017
> 22,422
> 12%
> Operating expenses
> 31,100
> 28,615
> 9%
> Operating income
> $
> 83,879
> $
> 69,773
> 20%
> Intelligent Cloud

### MSFT-000119312526323660-0150

liquidity, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 169639–170141

> LIQUIDITY AND CAPITAL RESOURCES
> We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities and cash commitments for investing and financing activities, such as dividends, share repurchases, debt maturities, and material capital expenditures, for at least the next 12 months and thereafter for the foreseeable future.
> 42
> PART II
> Item 7
> Cash, Cash Equivalents, and Investments

### MSFT-000119312526323660-0155

liquidity, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 174486–175851

> We issue debt to take advantage of favorable pricing and liquidity in the debt markets, reflecting our credit rating. The proceeds of these issuances were or will be used for general corporate purposes, which may include, among other things, funding for working capital, capital expenditures, repurchases of capital stock, acquisitions, and repayment of existing debt. Refer to Note 10 – Debt of the Notes to Financial Statements (Part II, Item 8 of this Form 10-K).
> 43
> PART II
> Item 7
> Unearned Revenue
> Unearned revenue comprises mainly unearned revenue related to volume licensing programs, which may include cloud services and Software Assurance (“SA”). Unearned revenue is generally invoiced annually at the beginning of each contract period for multi-year agreements and recognized ratably over the coverage period. Unearned revenue also includes payments for other offerings for which we have been paid in advance and earn the revenue when we transfer control of the product or service. Refer to Note 1 – Accounting Policies of the Notes to Financial Statements (Part II, Item 8 of this Form 10-K).
> The following table outlines the expected future recognition of unearned revenue as of June 30, 2026:
> (In millions)
> Three Months Ending
> September 30, 2026
> $
> 28,589
> December 31, 2026
> 22,556
> March 31, 2027
> 15,457
> June 30, 2027
> 6,363
> Thereafter
> 2,747
> Total
> $
> 75,712

### MSFT-000119312526323660-0158

mdna, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 177824–179309

> Dividends
> During fiscal years 2026 and 2025, our Board of Directors declared dividends totaling $27.0 billion and $24.7 billion, respectively. We intend to continue returning capital to shareholders in the form of dividends, subject to declaration by our Board of Directors. Refer to Note 15 – Stockholders’ Equity of the Notes to Financial Statements (Part II, Item 8 of this Form 10-K).
> Other Planned Uses of Capital
> We will continue to invest in sales, marketing, product support infrastructure, and existing and advanced areas of technology, as well as acquisitions that align with our business strategy. Additions to property and equipment will continue, including new facilities, datacenters, and computer systems for research and development, sales and marketing, support, and administrative staff. We will continue to invest in capital expenditures to support growth in our cloud offerings and our investments in AI training and other infrastructure. We have operating and finance leases for datacenters and related infrastructure, servers and network equipment, corporate offices, and research and development facilities. We have not engaged in any related party transactions or arrangements with unconsolidated entities or other persons that are reasonably likely to materially affect liquidity or the availability of capital resources.
> RECENT ACCOUNTING GUIDANCE
> Refer to Note 1 – Accounting Policies of the Notes to Financial Statements (Part II, Item 8 of this Form 10-K).

### MSFT-000119312526323660-0220

debt_note, [10-K for 2026-06-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm), characters 255018–255943

> Refer to Note 5 – Derivatives for further information on the interest rate swaps related to fixed-rate debt.
> As of June 30, 2026 and 2025, the estimated fair value of long-term debt, including the current portion, was $36.5 billion and $40.4 billion, respectively. The estimated fair values are based on Level 2 inputs.
> Debt in the table above is comprised of senior unsecured obligations and ranks equally with our other outstanding obligations. Interest is paid semi-annually, except for the Euro-denominated debt, which is paid annually. Cash paid for interest on our debt for fiscal years 2026, 2025, and 2024 was $1.5 billion, $1.6 billion, and $1.7 billion, respectively.
> 72
> PART II
> Item 8
> The following table outlines maturities of our long-term debt, including the current portion, as of June 30, 2026:
> (In millions)
> Year Ending June 30,
> 2027
> $
> 9,250
> 2028
> 0
> 2029
> 2,001
> 2030
> 0
> 2031
> 500
> Thereafter
> 34,385
> Total
> $
> 46,136

### MSFT-000119312526436133-0051

mdna, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 65211–66249

> We undertake no obligation to update or revise publicly any forward-looking statements, whether because of new information, future events, or otherwise.
> The following Management’s Discussion and Analysis of Financial Condition and Results of Operations (“MD&A”) is intended to help the reader understand the results of operations and financial condition of Microsoft Corporation. MD&A is provided as a supplement to, and should be read in conjunction with, our Annual Report on Form 10-K for the year ended June 30, 2026, and our consolidated financial statements and the accompanying Notes to Financial Statements (Part I, Item 1 of this Form 10-Q).
> OVERVIEW
> Microsoft is a technology company committed to making digital technology and artificial intelligence (“AI”) available broadly and doing so responsibly, with a mission to empower every person and every organization on the planet to achieve more. We create platforms and applications, powered by AI, that deliver innovative solutions that meet the evolving needs of our customers.

### MSFT-000119312526436133-0071

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 90846–91330

> LIQUIDITY AND CAPITAL RESOURCES
> We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities and cash commitments for investing and financing activities, such as dividends, share repurchases, debt maturities, and material capital expenditures, for at least the next 12 months and thereafter for the foreseeable future.
> Cash, Cash Equivalents, and Investments

### MSFT-000119312526436133-0072

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 91331–92412

> Cash, cash equivalents, and short-term investments totaled $64.5 billion and $76.8 billion as of September 30, 2026 and June 30, 2026, respectively. Equity and other investments were $37.8 billion and $36.3 billion as of September 30, 2026 and June 30, 2026, respectively. Our short-term investments are primarily intended to facilitate liquidity and capital preservation. They consist predominantly of highly liquid investment-grade fixed-income securities, diversified among industries and individual issuers. The investments are predominantly U.S. dollar-denominated securities, but also include foreign currency-denominated securities to diversify risk. Our fixed-income investments are exposed to interest rate risk and credit risk. The credit risk and average maturity of our fixed-income portfolio are managed to achieve economic returns that correlate to certain fixed-income indices. The settlement risk related to these investments is insignificant given that the short-term investments held are primarily highly liquid investment-grade fixed-income securities.
> Valuation

### MSFT-000119312526436133-0075

liquidity, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 94611–95995

> Cash from operations increased $12.9 billion to $58.0 billion for the three months ended September 30, 2026, primarily due to an increase in cash received from customers and a decrease in cash used to pay income taxes, offset in part by an increase in cash paid to suppliers. Cash used in financing increased $4.8 billion to $16.6 billion for the three months ended September 30, 2026, primarily due to a $4.9 billion increase in cash used for repayments of debt. Cash used in investing increased $7.4 billion to $42.0 billion for the three months ended September 30, 2026, primarily due to a $20.0 billion increase in additions to property and equipment and a $6.7 billion increase in cash used in other investing primarily to facilitate the purchase of components, offset in part by a $19.1 billion increase in cash from net investment purchases, sales, and maturities.
> 37
> PART I
> Item 2
> Debt Proceeds
> We issue debt to take advantage of favorable pricing and liquidity in the debt markets, reflecting our credit rating. The proceeds of these issuances were or will be used for general corporate purposes, which may include, among other things, funding for working capital, capital expenditures, repurchases of capital stock, acquisitions, and repayment of existing debt. Refer to Note 9 – Debt of the Notes to Financial Statements (Part I, Item 1 of this Form 10-Q).
> Unearned Revenue

### MSFT-000119312526436133-0100

risk_factors, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 120996–122430

> Our cloud and AI strategy requires substantial investments and depends on evolving customer demand, technological developments, competitive dynamics, and regulatory conditions, any of which could adversely affect our business, financial condition, and results of operations. We have made and are continuing to make significant capital and operational investments to develop, train, deploy, and support AI models and related cloud-based services, including building and expanding datacenters, acquiring necessary components, and securing energy resources. These investments are being made at significant scale and on an accelerated timeline, require substantial and increasing capital expenditures and continued access to capital, and are in advance of fully developed revenue streams. The associated revenue may not be realized in the expected timeframes or at expected levels. Our capital and operational investments are complex and involve projects in multiple locations around the world that expose us to increased compliance risks and political challenges, among others. Funding these investments depends on our ability to generate sufficient cash flows and obtain financing on acceptable terms. Adverse changes in interest rates, credit markets, investor sentiment, our credit ratings, or other factors affecting capital availability could increase our cost of capital or limit our ability to execute our infrastructure strategy.

### MSFT-000119312526436133-0102

risk_factors, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 123575–124057

> The cost structure for AI products and services is subject to significant uncertainty, including with respect to model training and inference costs, the availability and pricing of components, and energy costs. If these costs increase, remain elevated, or fail to decline, or if pricing for AI products and services declines as a result of competition, commoditization, or other market forces, our margins, financial condition, and results of operations could be adversely affected.

### MSFT-000119312526436133-0144

risk_factors, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 171446–172342

> AI: Legislative and regulatory action on AI is evolving rapidly and accelerating across multiple jurisdictions, which is increasing costs and may create liability and restrict opportunity. For example, the EU’s AI Act may increase costs or impact the provision or operation of our AI models and services in the European market and new external audit and evaluation obligations for advanced AI models and systems in several U.S. states may have similar effects. In addition, governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cybersecurity, or national security or may apply laws to AI models in ways we cannot anticipate. AI regulatory areas include model and system development and deployment, frontier model safety and security, transparency, content provenance, digital replicas, and AI companions.
> •

### MSFT-000119312526436133-0159

risk_factors, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 187969–188915

> Adverse economic or market conditions could harm our business. Worsening economic conditions, including inflation, recession, pandemic, or other changes in economic conditions, periods of economic uncertainty, evolution of customer demand, technology investment cycles, interest rates, foreign exchange rates, or the timing and mix of customer spending, may cause lower or delayed IT spending and adversely affect our results of operations. If demand for computing power, PCs, servers, and other computing devices declines, or consumer or business spending for those products declines, could adversely affect our results of operations. Such conditions could also disrupt our distribution channels, including through financial distress or bankruptcy of a significant distributor, OEM, or retailer, and impair our customers’ ability to pay amounts owed, resulting in increased allowances for doubtful accounts and write-offs of accounts receivable.

### MSFT-000119312526436133-0160

risk_factors, [10-Q for 2026-09-30](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm), characters 188916–189613

> We maintain an investment portfolio of various holdings, types, and maturities. These investments are subject to general credit, liquidity, market, and interest rate risks, which may be exacerbated by market downturns or events that affect global financial markets. If global financial markets decline for long periods, or if there is a downgrade of the U.S. government credit rating due to an actual or threatened default on government debt, our investment portfolio could be adversely affected and we could determine that more of our investments have experienced a decline in fair value, requiring impairment charges that could adversely affect our financial condition and results of operations.

## Run

Run `MSFT-20261118T061827Z-GLM-5.3`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 8 calls, 29,852 input (9,216 cached) and 15,612 output tokens, $0.0700, 124s. Verification: 36 calls, 16,884 input (4,608 cached) and 3,740 output tokens, $0.0244, 78s. Prices read 2026-11-17. Raw requests and responses: data/runs/MSFT/MSFT-20261118T061827Z-GLM-5.3.jsonl.
