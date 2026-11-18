# Credit memo: ORACLE CORP (ORCL)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `deepseek-ai/DeepSeek-V4.1-Flash-1017`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-4**.
Sources: [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm); [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)

Claims: 34 — 27 supported, 7 partially supported, 0 unsupported. Raw numbers rejected in first drafts: 4; repairs: 3.

## Business profile

1. Oracle operates through three businesses — cloud and software, hardware and services — each of which constitutes a single operating segment.  
   ✅ supported (judge): The filing directly states Oracle has three businesses—cloud and software, hardware, and services—each comprised of a single operating segment.
   - cites `ORCL-000119312526277521-0010` ✓: “We have three businesses: cloud and software (formerly referred to as cloud and license); hardware; and services.”
   - cites `ORCL-000119312526389274-0063` ✓: “we discuss below the results of each of our three businesses—cloud and software, hardware and services—which are our operating segments”
2. Oracle's scale is reflected in revenue of **$67.4 billion** [F1] and EBITDA of **$29.9 billion** [F2] for the fiscal year ended 31 May 2026.  
   ✅ supported (judge): The metric values confirm revenue of $67.4B and EBITDA of $29.9B for FY ended 31 May 2026.
3. Revenue rose from **$53.0 billion** [F3] in the fiscal year ended 31 May 2024 to **$71.8 billion** [F4] in the twelve months to 31 August 2026, with operating income of **$23.1 billion** [F5] over the same trailing period.  
   ✅ supported (judge): All three figures in the claim match the computed XBRL metric values exactly.
4. The services business is a comparatively small share of revenues and carries lower margins than the cloud and software and hardware businesses, which tempers its contribution to overall profitability.  
   ✅ supported (judge): Passage states services was 8% and 9% of total revenues and has lower margins than cloud and software and hardware businesses, matching the claim's small share and margin drag.
   - cites `ORCL-000119312526277521-0166` ✓: “Our services business, which represented 8% and 9% of our total revenues in fiscal 2026 and 2025, respectively”
   - cites `ORCL-000119312526277521-0166` ✓: “Our services business has lower margins than our cloud and software and hardware businesses.”
5. Oracle continues to expand its cloud infrastructure footprint, adding data center capacity and new locations to meet expected customer demand, which supports revenue visibility but requires ongoing investment.  
   ◐ partially supported (judge): The passage supports expansion of data center capacity in new locations to meet expected demand and implies ongoing investment, but 'supports revenue visibility' is not stated in the evidence.
   - cites `ORCL-000119312526277521-0035` ✓: “We have invested in the rapid expansion of the Oracle Cloud by increasing existing data center capacity and adding data centers in new geographic locations to meet current and expected customer demand”
6. Customers commonly renew support and cloud contracts after initial purchases, giving the business a recurring revenue element, though competition across its segments focuses on cost, performance, scalability and reliability.  
   ✅ supported (judge): Renewal of support and cloud contracts after initial purchase and competitive factors including total cost of ownership, performance, scalability and reliability are both stated in the evidence.
   - cites `ORCL-000119312526277521-0010` ✓: “our customers can continue to benefit from our offerings, research and development efforts and deep IT expertise by electing to purchase and renew Oracle support offerings”
   - cites `ORCL-000119312526277521-0046` ✓: “Key competitive factors in each of the segments in which we currently compete and may compete in the future include: total cost of ownership”

## Financial risk

1. Debt / EBITDA was **4.04x** [F6] in the fiscal year ended 31 May 2024, **4.00x** [F7] in the fiscal year ended 31 May 2025, **4.59x** [F8] in the fiscal year ended 31 May 2026 and **3.96x** [F9] in the twelve months to 31 August 2026, a stable trend, with total debt of **$134.5 billion** [F10] at the end of the twelve months to 31 August 2026.  
   ✅ supported (judge): All cited Debt/EBITDA ratios (4.04x, 4.00x, 4.59x, 3.96x) and the $134.5 billion LTM total debt match the computed metric values exactly, and the 'stable trend' characterization is consistent with the narrow range around 4x.
2. Net leverage improved from **3.55x** [F11] in the fiscal year ended 31 May 2024 to **2.87x** [F12] in the twelve months to 31 August 2026, helped by EBITDA of **$33.9 billion** [F13] over the twelve months.  
   ✅ supported (judge): Both net leverage figures (3.55x at FY-2, 2.87x LTM) and the LTM EBITDA of $33.9 billion match the computed metric values exactly, showing improvement in leverage.
3. EBITDA / interest was stable, moving from **6.12x** [F14] in the fiscal year ended 31 May 2024 to **6.65x** [F15] in the twelve months to 31 August 2026, against interest expense of **$5.1 billion** [F16] for the twelve months to 31 August 2026.  
   ✅ supported (judge): Both coverage ratios and the interest expense figure match the computed metric values exactly, and the modest change from 6.12x to 6.65x is consistent with describing the ratio as stable.
4. FCF / debt worsened from **13.6%** [F17] in the fiscal year ended 31 May 2024 to **-21.3%** [F18] in the twelve months to 31 August 2026, as capital expenditure of **$75.7 billion** [F19] exceeded cash from operations of **$46.9 billion** [F20] over the period.  
   ✅ supported (judge): All figures in the claim match the metric values: FCF/debt worsened from 13.6% to -21.3%, with LTM capex of $75.7B exceeding cash from operations of $46.9B.
5. The deterioration in free cash flow relative to debt reflects a large increase in capital spending, and the company met part of that spending with new borrowings.  
   ◐ partially supported (judge): The evidence confirms very large capital expenditures ($55.7B) and borrowings (senior notes, short-term capex financing) used to fund spending, but it does not establish a deterioration in free cash flow relative to debt — operating cash flow actually increased 54%.
   - cites `ORCL-000119312526277521-0197` ✓: “partially offset by $55.7 billion of cash used for capital expenditures”
   - cites `ORCL-000119312526277521-0197` ✓: “was primarily due to proceeds from the issuance of senior notes, net of issuance costs, of $42.7 billion during fiscal 2026”
6. Interest expense rose on higher average borrowings from senior note issuance, partly offset by scheduled debt repayments, which supports the broadly flat interest coverage ratio.  
   ◐ partially supported (judge): The rise in interest expense from senior note issuance partly offset by scheduled repayments is stated, but the evidence says nothing about an interest coverage ratio or it being broadly flat (interest expense actually rose 29%/55%).
   - cites `ORCL-000119312526277521-0190` ✓: “Interest expense increased in fiscal 2026 relative to fiscal 2025 primarily due to higher average borrowings from the issuances of $43.0 billion of senior notes in fiscal 2026”
   - cites `ORCL-000119312526389274-0082` ✓: “partially offset by lower interest expense due to scheduled repayments of $8.1 billion of debt”

## Liquidity

1. Liquidity coverage was **0.94x** [F21] for the twelve months to 31 August 2026 and **0.93x** [F22] for the fiscal year ended 31 May 2026, on an assumption of undrawn revolving capacity of **$0** [F23], so measured sources fell marginally short of estimated uses.  
   ✅ supported (judge): Both coverage figures (0.94x LTM to 31 Aug 2026 and 0.93x FY ended 31 May 2026) and the $0 undrawn revolver assumption match the computed metric values, and ratios below 1.0x mean measured sources fell marginally short of estimated uses.
2. At the twelve months to 31 August 2026 cash of **$36.4 billion** [F24] and short-term investments of **$708 million** [F25] together exceeded short-term debt of **$7.6 billion** [F26].  
   ✅ supported (judge): Cash of $36.4B plus short-term investments of $0.708B totals $37.1B, which exceeds short-term debt of $7.6B, matching the claim.
3. Cash from operations of **$46.9 billion** [F20] was well below capital expenditure of **$75.7 billion** [F19] in the twelve months to 31 August 2026, while dividends absorbed **$5.9 billion** [F27].  
   ✅ supported (judge): All figures match the XBRL metrics: CFO of $46.9B is below capex of $75.7B for the LTM to 31 Aug 2026, and dividends paid were $5.9B; 'well below' is consistent with the $28.8B gap.
   - cites `ORCL-000119312526389274-0089` ✓: “our investments in capital assets to support the growth in our cloud and software business”
4. The company has a committed unsecured revolving credit facility that it may borrow, prepay and reborrow under, and it reported no outstanding borrowings under that agreement at the latest fiscal year-end.  
   ✅ supported (judge): Evidence states the revolving credit facility allows borrowing, prepaying and reborrowing, and no outstanding borrowings as of May 31, 2026 (latest fiscal year-end). Note the evidence doesn't explicitly say 'unsecured,' but interest is tied to the company's long-term senior unsecured debt rating, consistent with an unsecured facility; all other elements are directly stated.
   - cites `ORCL-000119312526277521-0299` ✓: “we may borrow, prepay and reborrow amounts under the Revolving Facility during the term of the Revolving Credit Agreement”
   - cites `ORCL-000119312526277521-0201` ✓: “we did not have any outstanding borrowings under the Revolving Credit Agreement”
5. A commercial paper program supplements the revolving facility, and the company states that net proceeds from commercial paper issuance are used for general corporate purposes.  
   ◐ partially supported (judge): The general corporate purposes use of commercial paper proceeds is stated, but the evidence does not state that the commercial paper program supplements the revolving facility.
   - cites `ORCL-000119312526277521-0302` ✓: “Our commercial paper program allows us to issue and sell unsecured short-term promissory notes”
   - cites `ORCL-000119312526277521-0201` ✓: “We used the net proceeds from the issuance of commercial paper for general corporate purposes.”
6. Operating cash flow is driven mainly by customer collections on cloud and software support agreements, which supports the recurring nature of internally generated liquidity.  
   ✅ supported (judge): The passage explicitly states operating cash flows' largest source is customer collections on cloud and software support agreements, indicating recurring internally generated liquidity.
   - cites `ORCL-000119312526389274-0088` ✓: “Our largest source of operating cash flows is cash collections from our customers following the purchase and renewal of their cloud and software support agreements.”

## Maturity wall

1. Debt maturing in the next twelve months is **$7.2 billion** [F28], followed by **$10.1 billion** [F29] in year two, **$5.5 billion** [F30] in year three, **$7.2 billion** [F31] in year four and **$9.8 billion** [F32] in year five, with **$90.2 billion** [F33] due after year five.  
   ✅ supported (judge): All five maturity amounts and the after-five-year figure match the XBRL-computed metric values exactly.
2. Debt falling due within the first two years totals **$17.3 billion** [F34], equal to **12.6%** [F35] of total debt of **$137.2 billion** [F36].  
   ✅ supported (judge): Both figures ($17.3B debt due within 24 months and 12.6% share, implying total debt of $137.2B) match the computed metric values exactly.
3. Near-term maturity cover is **0.54x** [F37], measured as cash of **$31.3 billion** [F38] against short-term debt of **$7.2 billion** [F39].  
   ✅ supported (judge): All figures in the claim match the computed XBRL metric values: cover 0.54x, cash $31.3B, short-term debt $7.2B.
4. During the fiscal year ended 31 May 2026 the company issued $**43.0** [quoted: ORCL-000119312526277521-0203] billion par value of senior notes, with proceeds usable for general corporate purposes including repayment of indebtedness.  
   ✅ supported (judge): Both passages state the $43.0 billion par value issuance in fiscal 2026 and that proceeds were for general corporate purposes including repayment of indebtedness.
   - cites `ORCL-000119312526277521-0203` ✓: “During fiscal 2026, we issued a total of $43.0 billion par value of senior notes”
   - cites `ORCL-000119312526277521-0204` ✓: “which may include capital expenditures, repayment of indebtedness, future investments or acquisitions”
5. The company replaced its prior revolving credit agreement with a new $**10.0** [quoted: ORCL-000119312526277521-0298] billion, five-year unsecured revolving facility for working capital and other general corporate purposes.  
   ✅ supported (judge): The passage states the prior $6.0 billion revolving agreement was terminated and a new $10.0 billion, five-year unsecured revolving facility was entered into for working capital and general corporate purposes.
   - cites `ORCL-000119312526277521-0298` ✓: “we entered into a new $10.0 billion, five-year revolving credit agreement”
   - cites `ORCL-000119312526277521-0298` ✓: “to us for working capital purposes and for other general corporate purposes”
6. The company stated that it was in compliance with all debt-related covenants at the end of the fiscal year ended 31 May 2026.  
   ✅ supported (judge): The filing explicitly states compliance with all debt-related covenants at May 31, 2026.
   - cites `ORCL-000119312526277521-0297` ✓: “We were in compliance with all debt-related covenants at May 31, 2026.”

## Key risks

1. The company faces refinancing risk because it may not be able to refinance existing debt on terms as favorable as current terms.  
   ✅ supported (judge): The passage explicitly states the company may not be able to refinance existing debt or that refinancing terms may not be as favorable as existing terms.
   - cites `ORCL-000119312526277521-0127` ✓: “we may not be able to refinance existing debt or that the terms of any refinancing may not be as favorable”
2. Repayment depends on generating sufficient cash flows, and additional indebtedness would increase fixed obligations and interest expense and could introduce restrictive covenants.  
   ✅ supported (judge): The passage directly states repayment depends on generating sufficient cash flows and that additional indebtedness increases fixed obligations, interest expense, and could include restrictive covenants.
   - cites `ORCL-000119312526277521-0126` ✓: “dependent upon our ability to manage our business operations, generate sufficient cash flows to service such debt”
   - cites `ORCL-000119312526277521-0126` ✓: “increased fixed obligations and increased interest expense and could also include covenants or other restrictions”
3. Some indebtedness may bear interest at variable rates, so increases in interest rates could raise debt service obligations.  
   ✅ supported (judge): The claim is a near-verbatim restatement of the risk factor passage.
   - cites `ORCL-000119312526277521-0126` ✓: “Some of our indebtedness may bear interest at variable rates, and increases in interest rates could increase our debt service obligations.”
4. Disruptions affecting financial institutions or broader capital markets could impair the company's ability to access capital.  
   ✅ supported (judge): The passage states bank failures or issues in broader financial systems may impact capital markets and the company's ability to access those markets.
   - cites `ORCL-000119312526277521-0136` ✓: “Bank failures or issues in the broader U.S. or global financial systems may have an impact on the broader capital markets and, in turn, our ability to access those markets.”

## Rating rationale

1. The SB grade of **SB-4** [F40], derived from a weighted score of **4.35** [F41], is a stylized internal scorecard grade rather than a credit rating, and it is not provisional because all six scorecard factors were scored.  
   ✅ supported (judge): All claim elements match the computed scorecard: grade SB-4 from weighted score 4.35, stylized grade not a credit rating, and not provisional since all six factors were scored.
2. Interest coverage is the strongest scoring factor, at **6.65x** [F15] in band **3** [F42] on the scorecard's scale, and it carries the largest weight at **25.0%** [F43].  
   ◐ partially supported (judge): The 6.65x value, band 3, and 25.0% largest weight are supported, but interest coverage is not uniquely the strongest factor: near-term maturity cover also scores band 3, so calling it 'the strongest scoring factor' overstates the evidence.
3. FCF / debt is the weakest scoring factor, at **-21.3%** [F18] in band **6** [F44] with a weight of **20.0%** [F45].  
   ◐ partially supported (judge): FCF / debt is indeed -21.3%, band 6, weight 20.0%, but liquidity coverage is also in band 6, so FCF / debt is not uniquely the weakest factor.
4. Liquidity coverage of **0.94x** [F21] likewise sits in the weakest band of **6** [F46] at a weight of **15.0%** [F47], and it is measured with undrawn revolving capacity assumed to be zero.  
   ✅ supported (judge): All elements match: liquidity coverage is 0.94x with undrawn revolver assumed zero, sits in band 6 of 6 (weakest), at a 15% weight.
5. Mid-scale leverage scores, with debt / EBITDA at **3.96x** [F9] in band **4** [F48] and net leverage at **2.87x** [F12] in band **4** [F49], are tempered by the refinancing and interest rate risks the company describes.  
   ✅ supported (judge): The leverage figures (3.96x debt/EBITDA band 4, 2.87x net leverage band 4) match the metric values, and the passages explicitly describe refinancing and interest rate risks tempering the leverage picture.
   - cites `ORCL-000119312526277521-0127` ✓: “we may not be able to refinance existing debt or that the terms of any refinancing may not be as favorable”
   - cites `ORCL-000119312526277521-0126` ✓: “Some of our indebtedness may bear interest at variable rates”
6. The weak liquidity score is partly offset by a revolving credit facility with no borrowings outstanding at the latest fiscal year-end and by operating cash flow generated mainly from customer collections on cloud and software support agreements.  
   ◐ partially supported (judge): The revolver and cash-flow-source parts are supported, but the claim of a 'weak liquidity score' is contradicted by the scorecard, where liquidity coverage scored band 6 of 6 (the best band).
   - cites `ORCL-000119312526277521-0299` ✓: “we did not have any outstanding borrowings under the Revolving Credit Agreement”
   - cites `ORCL-000119312526389274-0088` ✓: “Our largest source of operating cash flows is cash collections from our customers following the purchase and renewal of their cloud and software support agreements.”

## Reviewer checklist

- [ ] **fallback** (info): Depreciation and amortisation: used rank 4 Depreciation + AmortizationOfIntangibleAssets in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Finance-lease liabilities (current plus non-current): used rank 2 FinanceLeaseLiability in FY-2.
- [ ] **fallback** (info): Total debt (borrowings plus finance-lease liabilities): used rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Short-term investments: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Dividends paid: used rank 2 PaymentsOfDividendsCommonStock in FY-2, FY-1, FY0, LTM.
- [ ] **fallback** (info): Revenue: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax in LTM.
- [ ] **fallback** (info): Short-term debt (short-term borrowings plus current portion of long-term debt): used rank 4 NotesPayableCurrent in LTM.
- [ ] **assumed zero** (info): Undrawn revolving credit capacity assumed zero (not reported) in FY-2, FY-1, FY0, LTM.
- [ ] **assumed zero** (info): Short-term borrowings (including commercial paper) assumed zero (not reported) in FY0.
- [ ] **reconciliation** (warning): total debt uses rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] = $137,242m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $129,541m (-5.6%). Check which matches the balance sheet.
- [ ] **partially supported claim** (warning): Business profile: partially supported (The passage supports expansion of data center capacity in new locations to meet expected demand and implies ongoing investment, but 'supports revenue visibility' is not stated in the evidence.): “Oracle continues to expand its cloud infrastructure footprint, adding data center capacity and new locations to meet expected customer demand, which supports revenue visibility but requires ongoing investment.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The evidence confirms very large capital expenditures ($55.7B) and borrowings (senior notes, short-term capex financing) used to fund spending, but it does not establish a deterioration in free cash flow relative to debt — operating cash flow actually increased 54%.): “The deterioration in free cash flow relative to debt reflects a large increase in capital spending, and the company met part of that spending with new borrowings.”
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The rise in interest expense from senior note issuance partly offset by scheduled repayments is stated, but the evidence says nothing about an interest coverage ratio or it being broadly flat (interest expense actually rose 29%/55%).): “Interest expense rose on higher average borrowings from senior note issuance, partly offset by scheduled debt repayments, which supports the broadly flat interest coverage ratio.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The general corporate purposes use of commercial paper proceeds is stated, but the evidence does not state that the commercial paper program supplements the revolving facility.): “A commercial paper program supplements the revolving facility, and the company states that net proceeds from commercial paper issuance are used for general corporate purposes.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The 6.65x value, band 3, and 25.0% largest weight are supported, but interest coverage is not uniquely the strongest factor: near-term maturity cover also scores band 3, so calling it 'the strongest scoring factor' overstates the evidence.): “Interest coverage is the strongest scoring factor, at 6.65x in band 3 on the scorecard's scale, and it carries the largest weight at 25.0%.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (FCF / debt is indeed -21.3%, band 6, weight 20.0%, but liquidity coverage is also in band 6, so FCF / debt is not uniquely the weakest factor.): “FCF / debt is the weakest scoring factor, at -21.3% in band 6 with a weight of 20.0%.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The revolver and cash-flow-source parts are supported, but the claim of a 'weak liquidity score' is contradicted by the scorecard, where liquidity coverage scored band 6 of 6 (the best band).): “The weak liquidity score is partly offset by a revolving credit facility with no borrowings outstanding at the latest fiscal year-end and by operating cash flow generated mainly from customer collections on cloud and software support agreements.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY0) | $67.4 billion | rank 1: Revenues | Revenues 67,357,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F2 | EBITDA (ebitda:FY0) | $29.9 billion | operating_income + d_and_a | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F3 | Revenue (revenue:FY-2) | $53.0 billion | rank 1: Revenues | Revenues 52,961,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F4 | Revenue (revenue:LTM) | $71.8 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 67,357,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 19,345,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 14,926,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F5 | Operating income (operating_income:LTM) | $23.1 billion | rank 1: OperatingIncomeLoss | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F6 | Debt / EBITDA (debt_to_ebitda:FY-2) | 4.04x | total_debt / EBITDA | LongTermNotesAndLoans 76,264,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>DebtCurrent 10,605,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>FinanceLeaseLiability 0 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>OperatingIncomeLoss 15,353,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,129,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 3,010,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:FY-1) | 4.00x | total_debt / EBITDA | LongTermNotesAndLoans 85,297,000,000 (at 2025-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>DebtCurrent 7,271,000,000 (at 2025-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 257,000,000 (at 2025-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityNoncurrent 2,677,000,000 (at 2025-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 17,678,000,000 (2024-06-01 to 2025-05-31, FY-1) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,867,000,000 (2024-06-01 to 2025-05-31, FY-1) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 2,307,000,000 (2024-06-01 to 2025-05-31, FY-1) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:FY0) | 4.59x | total_debt / EBITDA | LongTermNotesAndLoans 122,342,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 620,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 7,081,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F9 | Debt / EBITDA (debt_to_ebitda:LTM) | 3.96x | total_debt / EBITDA | LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityCurrent 749,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 8,436,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F10 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $134.5 billion | rank 5: LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityCurrent 749,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 8,436,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F11 | Net leverage (net_leverage:FY-2) | 3.55x | (total_debt - cash - short_term_investments) / EBITDA | LongTermNotesAndLoans 76,264,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>DebtCurrent 10,605,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>FinanceLeaseLiability 0 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 10,454,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 207,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>OperatingIncomeLoss 15,353,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,129,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 3,010,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F12 | Net leverage (net_leverage:LTM) | 2.87x | (total_debt - cash - short_term_investments) / EBITDA | LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityCurrent 749,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 8,436,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 36,369,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F13 | EBITDA (ebitda:LTM) | $33.9 billion | operating_income + d_and_a | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,156,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 1,351,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 202,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F14 | EBITDA / interest (interest_coverage:FY-2) | 6.12x | EBITDA / interest_expense | OperatingIncomeLoss 15,353,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,129,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 3,010,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>InterestExpense 3,514,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F15 | EBITDA / interest (interest_coverage:LTM) | 6.65x | EBITDA / interest_expense | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,156,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 1,351,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 202,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F16 | Interest expense (interest_expense:LTM) | $5.1 billion | rank 1: InterestExpense | InterestExpense 4,599,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>InterestExpense 1,428,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>InterestExpense 923,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F17 | FCF / debt (fcf_to_debt:FY-2) | 13.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 18,673,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 6,866,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermNotesAndLoans 76,264,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>DebtCurrent 10,605,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>FinanceLeaseLiability 0 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| F18 | FCF / debt (fcf_to_debt:LTM) | -21.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 23,103,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,140,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 28,499,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 8,502,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F19 | Capital expenditure (capex:LTM) | $75.7 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 28,499,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 8,502,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F20 | Cash from operations (cfo:LTM) | $46.9 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 23,103,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,140,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F21 | Liquidity coverage (liquidity_coverage:LTM) | 0.94x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 36,369,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 23,103,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,140,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 28,499,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F22 | Liquidity coverage (liquidity_coverage:FY0) | 0.93x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 31,289,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 605,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsOfDividendsCommonStock 5,787,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F23 | Undrawn revolving credit capacity (undrawn_revolver:LTM) | $0 |  | — |
| F24 | Cash and cash equivalents (cash:LTM) | $36.4 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 36,369,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F25 | Short-term investments (short_term_investments:LTM) | $708 million | rank 3: AvailableForSaleSecuritiesDebtSecuritiesCurrent | AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F26 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $7.6 billion | rank 4: NotesPayableCurrent | NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F27 | Dividends paid (dividends:LTM) | $5.9 billion | rank 2: PaymentsOfDividendsCommonStock | PaymentsOfDividendsCommonStock 5,787,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsOfDividendsCommonStock 1,565,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsOfDividendsCommonStock 1,413,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F28 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $7.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 7,210,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F29 | Debt maturing in year two (maturity_year_2:FY0) | $10.1 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F30 | Debt maturing in year three (maturity_year_3:FY0) | $5.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 5,500,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F31 | Debt maturing in year four (maturity_year_4:FY0) | $7.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 7,250,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F32 | Debt maturing in year five (maturity_year_5:FY0) | $9.8 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 9,750,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F33 | Debt maturing after year five (maturity_after_year_5:FY0) | $90.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 90,250,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F34 | Debt due within 24 months (debt_due_24m:FY0) | $17.3 billion | short_term_debt + maturity_year_2 | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F35 | Share of debt due within 24 months (share_due_24m:FY0) | 12.6% | (short_term_debt + maturity_year_2) / total_debt | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermNotesAndLoans 122,342,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 620,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 7,081,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F36 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $137.2 billion | rank 5: LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | LongTermNotesAndLoans 122,342,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 620,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 7,081,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F37 | Near-term maturity cover (near_term_maturity_cover:FY0) | 0.54x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 31,289,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 605,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F38 | Cash and cash equivalents (cash:FY0) | $31.3 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 31,289,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F39 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:FY0) | $7.2 billion | rank 1: DebtCurrent | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F40 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 4.35 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F41 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 4.35 | sum of weight x band over the factors scored, divided by their weights | — |
| F42 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 3 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F43 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F44 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 6 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F45 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F46 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F47 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F48 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 4 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F49 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 4 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |

## Passages cited

### ORCL-000119312526277521-0010

business, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 12758–13701

> After an initial purchase of Oracle products and services, our customers can continue to benefit from our offerings, research and development efforts and deep IT expertise by electing to purchase and renew Oracle support offerings for their software and hardware deployments, which may include unspecified product upgrades and enhancements that we periodically deliver to our products, and by renewing their Oracle Cloud contracts with us.
> We have three businesses: cloud and software (formerly referred to as cloud and license); hardware; and services. Each business is comprised of a single operating segment. Item 7 Management’s Discussion and Analysis of Financial Condition and Results of Operations and Note 13 of Notes to Consolidated Financial Statements, both included elsewhere in this Annual Report, provide additional information related to our businesses and operating segments.
> Oracle Applications and Infrastructure Technologies

### ORCL-000119312526277521-0035

business, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 42166–43530

> Oracle Cloud Operations deliver our Oracle Cloud offerings to customers through a secure, reliable, scalable, enterprise grade cloud infrastructure platform managed by Oracle employees within a global network of data centers. The Oracle Cloud enables secure and isolated cloud-based instances for each of our customers to access the functionality of Oracle Cloud offerings via a broad spectrum of devices. Oracle Cloud Operations leverage automated software tools to enable the rapid delivery of the latest cloud technology capabilities to the Oracle Cloud as they become available and provide Oracle customers access to the latest Oracle releases. We have invested in the rapid expansion of the Oracle Cloud by increasing existing data center capacity and adding data centers in new geographic locations to meet current and expected customer demand. We expect this trend will continue.
> Manufacturing
> We rely on third-party manufacturing partners to produce most of our hardware products that we market and sell to customers and utilize internally to deliver Oracle Cloud offerings, and we distribute most of our hardware products from these partners’ facilities. Our manufacturing processes are substantially based on standardization of components across product types and centralization of assembly and distribution centers. Production of our
> 8
> Table of Contents

### ORCL-000119312526277521-0046

business, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 55373–56854

> For example, following our acquisition of Cerner Corporation, we also face competition from large healthcare IT providers such as Allscripts Healthcare Solutions, Inc., Arcadia Solutions, athenahealth, Inc., Epic Systems Corporation and InterSystems Corporation, among others. Moreover, we or our competitors may take certain strategic actions—including acquisitions, partnerships and joint ventures or repositioning of product lines—which invite even greater competition in one or more product offering categories.
> 11
> Table of Contents
> Key competitive factors in each of the segments in which we currently compete and may compete in the future include: total cost of ownership, performance, scalability, reliability, security, functionality, efficiency, ease of use, speed to production and quality of technical support. Our products and services sales and the relative strength of our products and services versus those of our competitors are also directly and indirectly affected by the following, among other factors:
> •
> market adoption of cloud-based IT offerings, including Oracle Cloud offerings;
> •
> our ability to develop AI technologies and features and to have access to AI technologies of competitors;
> •
> the ease of deployment, use, transacting for and maintenance of our products and services offerings;
> •
> compatibility between Oracle products and services deployed within local IT environments and public cloud IT environments, including our Oracle Cloud environments;
> •

### ORCL-000119312526277521-0126

risk_factors, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 151686–153131

> There are risks associated with our outstanding and future indebtedness. As of May 31, 2026, we had an aggregate of $129.5 billion of outstanding indebtedness that will mature between calendar year 2026 and calendar year 2066. We may incur additional indebtedness from time to time to finance capital expenditures, future investments or acquisitions, to finance the payment of cash dividends on or repurchases of our common stock, to refinance existing debt or for other purposes. Future financing or funding needs could differ from our projections. Our ability to pay interest and repay the principal for our indebtedness is dependent upon our ability to manage our business operations, generate sufficient cash flows to service such debt and the other factors discussed in this Risk Factors section. There can be no assurance that we will be able to manage any of these risks successfully. The incurrence of additional indebtedness will also result in increased fixed obligations and increased interest expense and could also include covenants or other restrictions that may impede our ability to manage our operations. Some of our indebtedness may bear interest at variable rates, and increases in interest rates could increase our debt service obligations. In addition, changes in interest rates could adversely affect the economics of certain long-term commitments or customer arrangements, particularly where pricing is fixed or committed.

### ORCL-000119312526277521-0127

risk_factors, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 153132–153879

> We have been refinancing portions of our outstanding debt as it matures, and we may continue to do so in the future. There is a risk that we may not be able to refinance existing debt or that the terms of any refinancing may not be as favorable as the terms of our existing debt. Furthermore, if prevailing interest rates or other factors at the time of refinancing result in higher interest rates upon refinancing, then the interest expense relating to that refinanced indebtedness would increase. More broadly, disruptions in credit markets, including reduced liquidity, changes in creditor sentiment or lender concentration limits, could increase our borrowing costs or limit our ability to access debt financing on acceptable terms, or at all.

### ORCL-000119312526277521-0136

risk_factors, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 162297–163755

> Macroeconomic developments such as the global or regional economic effects resulting from elevated inflation and interest rates, limited liquidity, adverse developments affecting financial institutions, the current wars and conflicts, evolving trade policies between the U.S. and international trade partners, including the imposition of tariffs and other trade measures or restrictions, or the occurrence of similar events in other countries that lead to uncertainty or instability in economic, political or market conditions could negatively affect our business, operating results, financial condition and outlook, which, in turn, could adversely affect our stock price. Any general weakening of, and related declining corporate confidence in, the global economy or the curtailment of government or corporate spending could cause current or potential customers to reduce or eliminate their IT budgets and spending, which could cause customers to delay, decrease or cancel purchases of our products and services or cause customers not to pay us or to delay paying us for previously purchased products and services. If any parties with whom we conduct business or invest our cash or cash equivalents are unable to meet their obligations to us, our business could be adversely affected. Bank failures or issues in the broader U.S. or global financial systems may have an impact on the broader capital markets and, in turn, our ability to access those markets.

### ORCL-000119312526277521-0166

mdna, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 192607–194018

> Our services business, which represented 8% and 9% of our total revenues in fiscal 2026 and 2025, respectively, helps customers and partners maximize the performance of their investments in Oracle applications and infrastructure technologies. We believe that our services are differentiated based on our focus on Oracle technologies, extensive experience, broad sets of intellectual property and best practices. Our services offerings include consulting services and customer success services (formerly referred to as advanced customer services). Services revenues are generally recognized over time as the services are performed. The cost of providing our services consists primarily of personnel-related expenses, technology infrastructure expenditures, facilities expenses and external contractor expenses. Our services business has lower margins than our cloud and software and hardware businesses. Our services revenues are affected by many factors including our strategy for, and the competitive position of, our services; customer demand for our cloud and software and hardware offerings and the related services that we may market and sell in connection with these offerings; general economic conditions; governmental budgetary constraints; personnel reductions in our customers’ IT departments; tighter controls over customer discretionary spending; and foreign currency rate fluctuations.
> Acquisitions

### ORCL-000119312526277521-0190

mdna, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 221953–223217

> The majority of the initiatives undertaken by the 2026 Restructuring Plan were effected to implement our continued emphasis in developing, marketing, selling and delivering our cloud-based offerings. Certain of the cost savings
> 49
> Table of Contents
> realized pursuant to the 2026 Restructuring Plan initiatives were offset by investments in resources and geographies that we believe better address the development, marketing, sale and delivery of our cloud-based offerings, including investments in the development and delivery of our second-generation cloud infrastructure. We may incur additional restructuring expenses in future periods due to the initiation of new restructuring plans or from changes in estimated costs associated with existing restructuring plans.
> Interest Expense:
> Year Ended May 31,
> Percent Change
> (Dollars in millions)
> 2026
> Actual
> Constant
> 2025
> Interest expense
> $
> 4,599
> 29%
> 29%
> $
> 3,578
> Interest expense increased in fiscal 2026 relative to fiscal 2025 primarily due to higher average borrowings from the issuances of $43.0 billion of senior notes in fiscal 2026 and an aggregate of $14.0 billion of senior notes in fiscal 2025, partially offset by lower interest expense due to scheduled repayments of debt made during fiscal 2026 and 2025.

### ORCL-000119312526277521-0197

liquidity, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 228709–230186

> was primarily due to proceeds from the issuance of senior notes, net of issuance costs, of $42.7 billion during fiscal 2026; $32.0 billion of cash inflows from our operations; $5.0 billion of cash proceeds from the issuance of Mandatory Convertible Preferred Stock, net of issuance costs; $4.9 billion of cash inflows from the sale of our investments, primarily in Ampere; $3.3 billion of cash inflows from short-term financing related to capital expenditures, net; and $1.3 billion of net cash provided by our employee stock programs, partially offset by $55.7 billion of cash used for capital expenditures; $5.8 billion of cash used to pay dividends to our common and preferred stockholders; $5.0 billion of cash used for scheduled repayments of debt; $851 million of cash used for repayment of commercial paper, net; $337 million of cash outflows for other financing activities, net; $864 million of cash used for purchases of non-current investments; and $95 million of cash used for repurchases of our common stock, in each case during fiscal 2026. Our cash and cash equivalents may be impacted by some or all of the aforementioned factors in future periods, the amounts and timing of which are variable.
> Year Ended May 31,
> (Dollars in millions)
> 2026
> Change
> 2025
> Net cash provided by operating activities
> $
> 31,977
> 54%
> $
> 20,821
> Net cash used for investing activities
> $
> (51,854
> )
> 139%
> $
> (21,711
> )
> Net cash provided by financing activities
> $
> 40,284
> *
> $
> 1,098
> *
> Not meaningful

### ORCL-000119312526277521-0201

liquidity, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 233996–235188

> Revolving Credit Agreement: In March 2026, we terminated our existing $6.0 billion, five-year revolving credit agreement. On the same date, we entered into a new $10.0 billion, five-year revolving credit agreement (the Revolving Credit Agreement). As of May 31, 2026, we did not have any outstanding borrowings under the Revolving Credit Agreement. The description above is a summary and is qualified in its entirety by reference to the full text of the Revolving Credit Agreement, which is incorporated by reference herein as Exhibit 10.14.
> Commercial Paper Program: In March 2026, our commercial paper program was increased to $10.0 billion. Our commercial paper program allows us to issue and sell unsecured short-term promissory notes (Commercial Paper Notes) pursuant to a private placement exemption from the registration requirements under federal and state securities laws pursuant to dealer agreements with various banks and an Issuing and Paying Agency Agreement with Deutsche Bank Trust Company Americas. There were $1.5 billion of outstanding Commercial Paper Notes as of May 31, 2026. We used the net proceeds from the issuance of commercial paper for general corporate purposes.

### ORCL-000119312526277521-0203

liquidity, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 236601–237943

> Common Stock: On February 2, 2026, we entered into an equity distribution agreement with ‎certain sales agents party thereto, pursuant to which we may sell shares of our common stock having aggregate sales proceeds of up to $20 billion from time to time through an “at-the-market” offering program (the ATM Program). As of May 31, 2026, we have not sold any shares of our common stock under the ATM Program.
> 53
> Table of Contents
> Senior Notes: During fiscal 2026, we issued a total of $43.0 billion par value of senior notes comprising the following:
> •
> $500 million of floating rate notes due February 2029;
> •
> $3.0 billion of 4.55% senior notes due February 2029;
> •
> $3.0 billion of 4.45% senior notes due September 2030;
> •
> $3.5 billion of 4.95% senior notes due February 2031;
> •
> $3.0 billion of 4.80% senior notes due September 2032;
> •
> $3.0 billion of 5.35% senior notes due May 2033;
> •
> $4.0 billion of 5.20% senior notes due September 2035;
> •
> $5.0 billion of 5.70% senior notes due February 2036;
> •
> $2.5 billion of 5.875% senior notes due September 2045;
> •
> $2.25 billion of 6.55% senior notes due February 2046;
> •
> $3.5 billion of 5.95% senior notes due September 2055;
> •
> $5.0 billion of 6.70% senior notes due February 2056;
> •
> $2.0 billion of 6.10% senior notes due September 2065; and
> •
> $2.75 billion of 6.85% senior notes due February 2066.

### ORCL-000119312526277521-0204

liquidity, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 237944–238610

> We issued the Mandatory Convertible Preferred Stock and the senior notes for general corporate purposes, which may include capital expenditures, repayment of indebtedness, future investments or acquisitions and payment of cash dividends on or repurchases of our common stock. Refer to Notes 6 and 10 of Notes to Consolidated Financial Statements included elsewhere in this Annual Report for additional information. The other terms and conditions of the senior notes are set forth in, and the foregoing description of the senior notes is qualified in its entirety by reference to, the Officers’ Certificates incorporated by reference herein as Exhibits 4.17 and 4.21.

### ORCL-000119312526277521-0297

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 338180–339466

> Interest is payable semi-annually for the senior notes listed in the above table, except for the floating-rate senior notes for which interest is payable quarterly. We may redeem some or all of the fixed-rate senior notes of each series prior to their maturity, subject to certain restrictions, and the payment of an applicable make-whole premium in certain instances except for the floating-rate senior notes, which may not be redeemed prior to their maturity.
> The senior notes rank pari passu with all existing and future notes issued pursuant to our commercial paper program (see additional discussion regarding our commercial paper program below) and all existing and future unsecured senior indebtedness of Oracle Corporation, including the Revolving Credit Agreement and the Term Loan Credit Agreement 2, each as defined and described further below. All existing and future liabilities of the subsidiaries of Oracle Corporation are or will be effectively senior to the senior notes and Commercial Paper Notes (defined below),
> 84
> Table of Contents
> borrowings under the Term Loan Credit Agreement 2 (defined below) and any future borrowings pursuant to the Revolving Credit Agreement. We were in compliance with all debt-related covenants at May 31, 2026.
> Revolving Credit Agreement

### ORCL-000119312526277521-0298

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 339467–340172

> On March 6, 2026, we terminated our existing $6.0 billion, five-year revolving credit agreement among us, as borrower, Bank of America, N.A., as administrative agent, and the lenders and other agents named therein, which was originally scheduled to terminate on March 8, 2027. On March 6, 2026, we entered into a new $10.0 billion, five-year revolving credit agreement (the Revolving Credit Agreement) among us, as borrower, Bank of America, N.A., as administrative agent, and the lenders and other agents named therein, which provides for an unsecured $10.0 billion, five-year revolving credit facility (the Revolving Facility) to us for working capital purposes and for other general corporate purposes.

### ORCL-000119312526277521-0299

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 340173–341155

> Subject to certain conditions stated in the Revolving Credit Agreement, we may borrow, prepay and reborrow amounts under the Revolving Facility during the term of the Revolving Credit Agreement. All amounts borrowed under the Revolving Credit Agreement will become due on March 6, 2031, unless the commitments are terminated earlier either at our request or, if an event of default occurs, by the lenders (or automatically in the case of certain bankruptcy-related events). Interest is based on either (a) a Term Secured Overnight Financing Rate (SOFR)-based formula plus a margin of 87.5 basis points to 150.0 basis points, depending on the credit rating assigned to our long-term senior unsecured debt, or (b) a Base Rate formula plus a margin of 0.0 basis point to 50.0 basis points, depending on the same such credit rating, each as set forth in the Revolving Credit Agreement. As of May 31, 2026, we did not have any outstanding borrowings under the Revolving Credit Agreement.

### ORCL-000119312526277521-0302

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 343782–345124

> Table of Contents
> •
> any remaining unpaid principal balance under the Term Loan Credit Agreement 2 will become fully due and payable on August 16, 2027 (subject to any extension of the Term Loan Credit Agreement 2 termination date, as set out below), unless the outstanding loans are prepaid earlier at the request of Oracle or accelerated by the lenders if an event of default occurs.
> The termination date of the Term Loan Credit Agreement 2 may be extended at our sole option by up to 2 years. The termination date of the Term Loan Credit Agreement 2 may also be further extended at each lender’s option by up to 2 years.
> Commercial Paper Program and Commercial Paper Notes
> On March 6, 2026, our commercial paper program was increased to $10.0 billion. Our commercial paper program allows us to issue and sell unsecured short-term promissory notes (Commercial Paper Notes) pursuant to a private placement exemption from the registration requirements under federal and state securities laws pursuant to dealer agreements with various banks and an Issuing and Paying Agency Agreement with Deutsche Bank Trust Company Americas.
> There were $1.5 billion and $2.3 billion of outstanding Commercial Paper Notes as of May 31, 2026 and 2025, respectively. We used the net proceeds from the issuance of commercial paper for general corporate purposes.

### ORCL-000119312526389274-0063

mdna, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm), characters 78376–79511

> In our results of operations discussion below, we provide an overview of our total consolidated revenues, total consolidated operating expenses and total consolidated operating margin, all of which are presented on a GAAP basis. We also present a GAAP-based discussion below for substantially all of the other expense items as presented in our condensed consolidated statements of operations that are not directly attributable to our three businesses.
> In addition, we discuss below the results of each of our three businesses—cloud and software, hardware and services—which are our operating segments as defined pursuant to ASC 280, Segment Reporting. The financial reporting for our three businesses that is presented below is presented in a manner that is consistent with that used by our CODMs. Our operating segment presentation below reflects revenues, direct costs and sales and marketing
> 24
> Table of Contents
> expenses that correspond to and are directly attributable to each of our three businesses. We also utilize these inputs to calculate and present a segment margin for each of our three businesses in the discussion below.

### ORCL-000119312526389274-0082

mdna, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm), characters 102940–104438

> Three Months Ended August 31,
> Percent Change
> (Dollars in millions)
> 2026
> Actual
> Constant
> 2025
> Interest expense
> $
> 1,428
> 55%
> 55%
> $
> 923
> Interest expense increased in the first quarter of fiscal 2027, relative to the first quarter of fiscal 2026, primarily due to higher average borrowings from the issuances of $43.0 billion of senior notes in fiscal 2026, partially offset by lower interest expense due to scheduled repayments of $8.1 billion of debt made during the first quarter of fiscal 2027 and full year of fiscal 2026.
> Non-Operating Income, net: Non-operating income, net consists primarily of interest income, net foreign currency exchange losses, the noncontrolling interests in the net profits of our majority-owned subsidiaries (primarily Oracle Financial Services Software Limited and Oracle Corporation Japan), net gains and losses related to marketable and non-marketable investments, including net gains and losses attributable to equity method investments and net other income and expenses, including net gains and losses from our investment portfolio related to our deferred compensation plan, for which an equal and offsetting amount was recorded to our operating expenses during the same period, and non-service net periodic pension income and losses.
> Three Months Ended August 31,
> Percent Change
> (Dollars in millions)
> 2026
> Actual
> Constant
> 2025
> Interest income
> $
> 306
> 197%
> 198%
> $
> 103
> Foreign currency losses, net
> (16
> )
> -48%
> -54%
> (31
> )
> Noncontrolling interests in income
> (53
> )
> 13%
> 13%

### ORCL-000119312526389274-0088

liquidity, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm), characters 109692–110912

> Table of Contents
> Three Months Ended August 31,
> (Dollars in millions)
> 2026
> Change
> 2025
> Net cash provided by operating activities
> $
> 23,103
> 184%
> $
> 8,140
> Net cash used for investing activities
> $
> (28,580
> )
> 228%
> $
> (8,718
> )
> Net cash provided by financing activities
> $
> 13,111
> *
> $
> 210
> *
> Not meaningful
> Cash flows from operating activities: Our largest source of operating cash flows is cash collections from our customers following the purchase and renewal of their cloud and software support agreements. Over the course of a fiscal year, we also generate cash from the sales of software licenses, hardware offerings and other services. Our primary uses of cash from operating activities are typically for employee-related expenditures, expenses related to data center leases and power for our cloud business, taxes, and interest payments.
> Net cash provided by operating activities increased by $15.0 billion in the first quarter of fiscal 2027, relative to the first quarter of fiscal 2026, primarily due to higher net income adjusted for certain non-cash charges and higher cash favorable working capital changes, net, which includes $11.4 billion cash inflows from customer prepayments with a significant financing component.

### ORCL-000119312526389274-0089

liquidity, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm), characters 110913–112262

> Cash flows from investing activities: The changes in cash flows from investing activities primarily relate to our investments in capital assets to support the growth in our cloud and software business and purchases, maturities and sales of our investments in marketable securities and other instruments.
> Net cash used for investing activities increased by $19.9 billion in the first quarter of fiscal 2027, relative to the first quarter of fiscal 2026, primarily due to a $20.0 billion increase in capital expenditures.
> Cash flows from financing activities: The changes in cash flows from financing activities primarily relate to borrowings and repayments related to our debt instruments, issuance of other financing or equity instruments, dividend payments, and net proceeds related to employee stock programs.
> Net cash provided by financing activities increased by $12.9 billion in the first quarter of fiscal 2027, relative to the first quarter of fiscal 2026, primarily due to net proceeds from the issuance of common stock via the ATM Program of $19.9 billion, partially offset by higher repayments of borrowings of $2.9 billion; higher net repayments of short-term financing related to capital expenditures of $2.8 billion; lower net cash proceeds from our employee stock programs of $1.1 billion; and higher dividend payments of $152 million.

## Run

Run `ORCL-20261118T062525Z-DeepSeek-V4.1-Flash-1017`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 9 calls, 37,666 input (15,616 cached) and 18,973 output tokens, $0.0078, 411s. Verification: 34 calls, 16,929 input (4,352 cached) and 3,448 output tokens, $0.0237, 68s. Prices read 2026-11-17. Raw requests and responses: data/runs/ORCL/ORCL-20261118T062525Z-DeepSeek-V4.1-Flash-1017.jsonl.
