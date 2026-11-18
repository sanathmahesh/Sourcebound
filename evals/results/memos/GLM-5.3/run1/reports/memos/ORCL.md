# Credit memo: ORACLE CORP (ORCL)

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

Drafted 2026-11-18 by `zai-org/GLM-5.3`, each claim checked by `zai-org/GLM-5.3` and by code. SB grade: **SB-4**.
Sources: [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm); [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)

Claims: 35 — 29 supported, 5 partially supported, 1 unsupported. Raw numbers rejected in first drafts: 1; repairs: 2.

## Business profile

1. Oracle operates three businesses—cloud and software, hardware, and services—each comprising a single operating segment, and it competes in markets where key competitive factors include total cost of ownership, performance, scalability, reliability and security.  
   ✅ supported (judge): The passages directly state the three single-segment businesses and list the competitive factors including all items cited.
   - cites `ORCL-000119312526277521-0010` ✓: “We have three businesses: cloud and software (formerly referred to as cloud and license); hardware; and services.”
   - cites `ORCL-000119312526277521-0046` ✓: “Key competitive factors in each of the segments in which we currently compete and may compete in the future include: total cost of ownership, performance, scalability, reliability, security”
2. Oracle's scale is substantial, with revenue growing from **$53.0 billion** [F1] in the fiscal year ended 31 May 2024 to **$67.4 billion** [F2] in the fiscal year ended 31 May 2026 and **$71.8 billion** [F3] in the twelve months to 31 August 2026.  
   ✅ supported (judge): All three revenue figures in the claim match the metric values computed from XBRL data.
3. The company generates strong profitability at scale, with EBITDA of **$29.9 billion** [F4] in the fiscal year ended 31 May 2026 and **$33.9 billion** [F5] in the twelve months to 31 August 2026.  
   ✅ supported (judge): Both EBITDA figures in the claim match the XBRL-derived metric values exactly ($29.9B FY0 and $33.9B LTM); 'strong profitability' is an interpretive framing but the factual content is verified.
4. Cash flows are supported by recurring revenue, as after an initial purchase of Oracle products and services customers can continue to benefit from Oracle's offerings and renew support for their software and hardware deployments and their Oracle Cloud contracts.  
   ✅ supported (judge): The passage directly states customers can renew Oracle support and Oracle Cloud contracts after an initial purchase, matching the claim.
   - cites `ORCL-000119312526277521-0010` ✓: “After an initial purchase of Oracle products and services, our customers can continue to benefit from our offerings, research and development efforts and deep IT expertise”
5. The services business is a small part of the mix, representing **8** [quoted: ORCL-000119312526389274-0060]% of total revenues on a trailing four-quarter basis, and it carries lower margins than the cloud and software and hardware businesses.  
   ✅ supported (judge): Both the 8% trailing four-quarter revenue share and the lower margins vs. cloud/software and hardware are stated in the passage.
   - cites `ORCL-000119312526389274-0060` ✓: “Our services business, which represented 8% of our total revenues on a trailing four-quarter basis, helps customers and partners maximize the performance of their investments in Oracle applications and infrastructure technologies.”
   - cites `ORCL-000119312526389274-0060` ✓: “Our services business has lower margins than our cloud and software and hardware businesses.”
6. Oracle has invested heavily in expanding its cloud infrastructure platform through a global network of data centers, adding capacity in existing and new geographic locations to meet expected customer demand, a trend the company expects to continue.  
   ✅ supported (judge): The passage directly states Oracle invested in expanding the Oracle Cloud by increasing existing data center capacity and adding new geographic locations to meet current and expected demand, and that it expects this trend to continue.
   - cites `ORCL-000119312526277521-0035` ✓: “We have invested in the rapid expansion of the Oracle Cloud by increasing existing data center capacity and adding data centers”

## Financial risk

1. Gross debt / EBITDA was stable over the review window, moving from **4.04x** [F6] in the fiscal year ended 31 May 2024 to **3.96x** [F7] in the twelve months to 31 August 2026 after peaking at **4.59x** [F8] in the fiscal year ended 31 May 2026, while net leverage improved steadily from **3.55x** [F9] to **2.87x** [F10].  
   ◐ partially supported (judge): The gross leverage endpoints (4.04x to 3.96x) and the 4.59x FY0 peak, plus the net leverage endpoints (3.55x to 2.87x), match the metrics, but the claim that net leverage 'improved steadily' goes beyond the evidence since no intermediate net leverage values are provided.
2. EBITDA / interest was stable across the period, with coverage of **6.12x** [F11] in the fiscal year ended 31 May 2024, **6.50x** [F12] in the fiscal year ended 31 May 2026 and **6.65x** [F13] in the twelve months to 31 August 2026.  
   ✅ supported (judge): All three coverage figures (6.12x, 6.50x, 6.65x) match the computed metric values exactly, and the modest variation supports the characterization of stability.
3. Interest expense increased over the period primarily because of higher average borrowings from large senior note issuances, partially offset by scheduled debt repayments.  
   ✅ supported (judge): Both passages state interest expense rose due to higher average borrowings from large senior note issuances, partially offset by scheduled debt repayments.
   - cites `ORCL-000119312526277521-0190` ✓: “higher average borrowings from the issuances of $43.0 billion of senior notes in fiscal 2026 and an aggregate of $14.0 billion of senior notes in fiscal 2025”
   - cites `ORCL-000119312526389274-0082` ✓: “scheduled repayments of $8.1 billion of debt made during the first quarter of fiscal 2027 and full year of fiscal 2026”
4. The worsening in FCF / debt from **13.6%** [F14] in the fiscal year ended 31 May 2024 to **-21.3%** [F15] in the twelve months to 31 August 2026 was driven by a sharp increase in capital expenditures to support cloud and software growth, which outpaced growth in operating cash flows, leaving LTM capital expenditure of **$75.7 billion** [F16] well above cash from operations of **$46.9 billion** [F17].  
   ✅ supported (judge): The ratios, LTM capex ($75.7B), and LTM CFO ($46.9B) match the metric values, and the 10-K passage attributes the deterioration to a $34.4B increase in capital expenditures to support cloud and software growth, which far exceeded the $11.2B increase in operating cash flows.
   - cites `ORCL-000119312526277521-0198` ✓: “Net cash used for investing activities increased by $30.1 billion in fiscal 2026 relative to fiscal 2025 primarily due to a $34.4 billion increase in capital expenditures”
   - cites `ORCL-000119312526389274-0088` ✓: “Net cash provided by operating activities increased by $15.0 billion in the first quarter of fiscal 2027, relative to the first quarter of fiscal 2026”
5. The improvement in net leverage to **2.87x** [F10] in the twelve months to 31 August 2026 was supported by strong operating cash generation, including customer prepayments, and by cash from note issuances, alongside scheduled debt repayments that reduced total debt from **$137.2 billion** [F18] to **$134.5 billion** [F19].  
   ✅ supported (judge): The net leverage of 2.87x and the decline in total debt from $137.2 billion (FY2026) to $134.5 billion (LTM to 31 Aug 2026) are confirmed by the metric values; the passages confirm strong operating cash generation including $4.6 billion of customer prepayments, $42.7 billion of senior note issuance proceeds, and scheduled debt repayments ($5.0 billion in fiscal 2026 plus additional repayments in Q1 fiscal 2027, totaling $8.1 billion across the LTM window).
   - cites `ORCL-000119312526277521-0198` ✓: “which includes $4.6 billion cash inflows from customer prepayments with significant financing component”
   - cites `ORCL-000119312526277521-0197` ✓: “proceeds from the issuance of senior notes, net of issuance costs, of $42.7 billion during fiscal 2026”
   - cites `ORCL-000119312526389274-0082` ✓: “scheduled repayments of $8.1 billion of debt made during the first quarter of fiscal 2027 and full year of fiscal 2026”

## Liquidity

1. Measured liquidity coverage was **0.93x** [F20] in the fiscal year ended 31 May 2026 and **0.94x** [F21] in the twelve months to 31 August 2026, indicating that liquidity sources as calculated fall modestly short of next-twelve-month needs.  
   ✅ supported (judge): Both liquidity coverage values (0.93x FY0 and 0.94x LTM) are confirmed by the computed metric values, and coverage below 1.0x directly implies sources fall modestly short of next-twelve-month needs.
2. Primary liquidity sources at the twelve months to 31 August 2026 comprised cash and cash equivalents of **$36.4 billion** [F22], short-term investments of **$708 million** [F23] and cash from operations of **$46.9 billion** [F17].  
   ✅ supported (judge): All three figures match the computed metric values exactly.
3. Projected next-twelve-month needs at the twelve months to 31 August 2026 include capital expenditure of **$75.7 billion** [F16], dividends of **$5.9 billion** [F24] and short-term debt of **$7.6 billion** [F25].  
   ◐ partially supported (judge): The dollar figures match the LTM metrics, but the claim characterizes them as projected next-twelve-month needs, whereas the evidence only provides historical twelve-month actuals, not projections.
4. The measured shortfall overstates liquidity risk because the coverage metric assumes no undrawn revolver capacity, whereas the company maintains an undrawn $**10.0** [quoted: ORCL-000119312526277521-0298] billion, five-year revolving credit facility.  
   ✅ supported (judge): The filing confirms an undrawn $10.0 billion five-year revolving credit facility, supporting the claim that the coverage metric ignores available revolver capacity.
   - cites `ORCL-000119312526277521-0298` ✓: “we entered into a new $10.0 billion, five-year revolving credit agreement (the Revolving Credit Agreement)”
   - cites `ORCL-000119312526277521-0299` ✓: “we did not have any outstanding borrowings under the Revolving Credit Agreement”
5. The company also maintains a commercial paper program that was increased to $**10.0** [quoted: ORCL-000119312526277521-0302] billion, providing additional short-term funding flexibility.  
   ✅ supported (judge): Evidence directly states the commercial paper program was increased to $10.0 billion and issues unsecured short-term promissory notes.
   - cites `ORCL-000119312526277521-0302` ✓: “our commercial paper program was increased to $10.0 billion”
6. Net proceeds of $**19.9** [quoted: ORCL-000119312526389274-0089] billion from common stock issuance under the ATM Program in the most recent quarter provided incremental liquidity beyond the sources captured in the coverage ratio.  
   ◐ partially supported (judge): The $19.9 billion ATM net proceeds in Q1 fiscal 2027 is supported, but the evidence says nothing about a coverage ratio or whether these proceeds were outside its captured sources.
   - cites `ORCL-000119312526389274-0089` ✓: “net proceeds from the issuance of common stock via the ATM Program of $19.9 billion”

## Maturity wall

1. Debt maturing in each of the five years following the fiscal year ended 31 May 2026 amounts to **$7.2 billion** [F26], **$10.1 billion** [F27], **$5.5 billion** [F28], **$7.2 billion** [F29] and **$9.8 billion** [F30], respectively, with a further **$90.2 billion** [F31] maturing after year five.  
   ✅ supported (judge): All five annual maturity amounts and the after-year-five amount match the computed metric values exactly.
2. Of total debt of **$137.2 billion** [F18] at the fiscal year ended 31 May 2026, **$17.3 billion** [F32] is due over the coming two years, representing **12.6%** [F33] of total debt, and near-term maturity cover stands at **0.54x** [F34].  
   ✅ supported (judge): All figures (total debt $137.2B, $17.3B due within 24 months, 12.6%, 0.54x near-term maturity cover) match the computed metric values exactly.
3. The company reported that it was in compliance with all debt-related covenants at the end of the fiscal year ended 31 May 2026.  
   ✅ supported (judge): The filing states directly that the company was in compliance with all debt-related covenants at May 31, 2026.
   - cites `ORCL-000119312526277521-0297` ✓: “We were in compliance with all debt-related covenants at May 31, 2026.”
4. The Revolving Credit Agreement requires the ratio of Consolidated EBITDA to Consolidated Net Interest Expense of Oracle and its subsidiaries to be not less than **3.0** [quoted: ORCL-000119312526277521-0300] to **1.0** [quoted: ORCL-000119312526277521-0300] at the end of any fiscal quarter while the agreement is effective.  
   ✅ supported (judge): The filing states the exact covenant: Consolidated EBITDA to Consolidated Net Interest Expense not less than 3.0 to 1.0 at the end of any fiscal quarter while the agreement is effective.
   - cites `ORCL-000119312526277521-0300` ✓: “shall not be less than 3.0 to 1.0 at the end of any fiscal quarter during the period that the Revolving Credit Agreement is effective”
5. In the fiscal year ended 31 May 2025 the company terminated the Term Loan Credit Agreement and borrowed up to the maximum commitment of $**5.6** [quoted: ORCL-000119312526277521-0301] billion under Term Loan Credit Agreement **2** [quoted: ORCL-000119312526277521-0301], and in the fiscal year ended 31 May 2026 it replaced its existing $**6.0** [quoted: ORCL-000119312526277521-0298] billion revolving credit agreement with a new $**10.0** [quoted: ORCL-000119312526277521-0298] billion, five-year Revolving Credit Agreement.  
   ✅ supported (judge): Both parts match the evidence: the FY2025 term loan termination and $5.6 billion borrowing under Term Loan Credit Agreement 2, and the March 6, 2026 (fiscal 2026) replacement of the $6.0 billion revolver with a new $10.0 billion, five-year Revolving Credit Agreement.
   - cites `ORCL-000119312526277521-0301` ✓: “we terminated our Term Loan Credit Agreement and repaid the principal amount outstanding together with interest accrued up to the date of repayment”
   - cites `ORCL-000119312526277521-0298` ✓: “we terminated our existing $6.0 billion, five-year revolving credit agreement”
   - cites `ORCL-000119312526277521-0298` ✓: “we entered into a new $10.0 billion, five-year revolving credit agreement (the Revolving Credit Agreement)”
6. During the fiscal year ended 31 May 2026 the company issued $**43.0** [quoted: ORCL-000119312526277521-0203] billion par value of senior notes, and in the first quarter of fiscal **2027** [quoted: ORCL-000119312526389274-0087] its cash outflows included $**3.1** [quoted: ORCL-000119312526389274-0087] billion of cash used for scheduled repayments of debt and $**1.1** [quoted: ORCL-000119312526389274-0087] billion of cash used for repayment of commercial paper.  
   ✅ supported (judge): All three figures are directly stated in the evidence: $43.0B senior notes issued in fiscal 2026, and $3.1B scheduled debt repayments and $1.1B commercial paper repayment in Q1 fiscal 2027.
   - cites `ORCL-000119312526277521-0203` ✓: “During fiscal 2026, we issued a total of $43.0 billion par value of senior notes”
   - cites `ORCL-000119312526389274-0087` ✓: “$3.1 billion of cash used for scheduled repayments of debt”
   - cites `ORCL-000119312526389274-0087` ✓: “$1.1 billion of cash used for repayment of commercial paper”

## Key risks

1. In the twelve months to 31 August 2026, Oracle's Debt/EBITDA was **3.96x** [F7], EBITDA/interest was **6.65x** [F13], FCF/debt was **-21.3%** [F15], and liquidity coverage was **0.94x** [F21].  
   ✅ supported (judge): All four metric values in the claim match the computed metric scorecard exactly.
2. Oracle has been refinancing maturing debt and may not be able to refinance existing debt or obtain refinancing terms as favorable as its existing debt, and higher interest rates upon refinancing would increase interest expense on the refinanced indebtedness.  
   ✅ supported (judge): The passage directly states all parts of the claim: refinancing of maturing debt, risk of unfavorable refinancing terms, and increased interest expense from higher rates upon refinancing.
   - cites `ORCL-000119312526277521-0127` ✓: “There is a risk that we may not be able to refinance existing debt or that the terms of any refinancing may not be as favorable as the terms of our existing debt.”
3. Disruptions in credit markets, including reduced liquidity or changes in creditor sentiment, could increase Oracle's borrowing costs or limit its ability to access debt financing on acceptable terms, or at all.  
   ✅ supported (judge): The passage states almost verbatim that credit market disruptions including reduced liquidity or changes in creditor sentiment could increase borrowing costs or limit access to debt financing on acceptable terms, or at all.
   - cites `ORCL-000119312526277521-0127` ✓: “disruptions in credit markets, including reduced liquidity, changes in creditor sentiment or lender concentration limits, could increase our borrowing costs or limit our ability to access debt financing on acceptable terms, or at all.”
4. Oracle's ability to pay interest and repay principal on its indebtedness depends on its ability to generate sufficient cash flows, and some of its indebtedness bears interest at variable rates, so increases in interest rates could increase its debt service obligations.  
   ✅ supported (judge): The passage directly states both that Oracle's ability to pay interest and repay principal depends on generating sufficient cash flows and that some indebtedness bears interest at variable rates, so interest rate increases could raise debt service obligations.
   - cites `ORCL-000119312526277521-0126` ✓: “Our ability to pay interest and repay the principal for our indebtedness is dependent upon our ability to manage our business operations, generate sufficient cash flows to service such debt”
   - cites `ORCL-000119312526277521-0126` ✓: “Some of our indebtedness may bear interest at variable rates, and increases in interest rates could increase our debt service obligations.”
5. Macroeconomic weakness could cause customers to delay, decrease or cancel purchases or to delay paying Oracle for previously purchased products and services, and bank failures or issues in the broader financial system could impair Oracle's access to capital markets.  
   ✅ supported (judge): Both parts of the claim are directly stated in the passage: macroeconomic weakness could cause customers to delay, decrease or cancel purchases or delay paying for previously purchased products and services, and bank failures or broader financial system issues could impair access to capital markets.
   - cites `ORCL-000119312526277521-0136` ✓: “cause customers to delay, decrease or cancel purchases of our products and services or cause customers not to pay us or to delay paying us”
   - cites `ORCL-000119312526277521-0136` ✓: “Bank failures or issues in the broader U.S. or global financial systems may have an impact on the broader capital markets and, in turn, our ability to access those markets.”
6. Failure to accurately anticipate, pay for and manage future data center capacity needs in a timely manner to meet customer demand is a disclosed risk that could pressure Oracle's cash flows.  
   ✅ supported (judge): The passage explicitly lists failure to anticipate, pay for, plan for and manage future data center capacity needs in a timely manner to meet customer demand as a risk factor, and this risk section is framed around effects such as greater-than-anticipated costs.
   - cites `ORCL-000119312526277521-0059` ✓: “we are unable to accurately anticipate, pay for, plan for and manage future data center capacity needs in a timely manner to meet current or expected customer demand”

## Rating rationale

1. The scorecard yields a grade of **SB-4** [F35] on a weighted score of **4.35** [F36], and this SB grade is a stylized internal scorecard grade, not a credit rating, and is not provisional because all six factors were scored.  
   ✅ supported (judge): The metric values state SB grade SB-4, weighted score 4.35, note it is a stylized scorecard grade not a credit rating, and confirm the grade is not provisional since all six factors were scored.
2. The strongest-scoring factors are interest coverage, in band **3** [F37] with the largest weight of **25.0%** [F38], and near-term maturity cover, in band **3** [F39] with a weight of **10.0%** [F40].  
   ◐ partially supported (judge): Both factors are indeed in band 3 with weights of 25% and 10%, and interest coverage carries the largest weight; however, near-term maturity cover's 10% weight only ties net debt/EBITDA, so calling these two 'the strongest-scoring factors' overstates the evidence.
3. The weakest-scoring factors are FCF/debt, in band **6** [F41] with a weight of **20.0%** [F42], and liquidity coverage, in band **6** [F43] with a weight of **15.0%** [F44], while the leverage measures sit in the middle at band **4** [F45] for Debt/EBITDA and band **4** [F46] for net leverage.  
   ✅ supported (judge): All stated bands and weights match the scorecard metrics: FCF/debt band 6 at 20%, liquidity coverage band 6 at 15%, Debt/EBITDA band 4, and net leverage band 4.
4. The strong interest coverage score is supported by coverage that remained stable even as interest expense rose on higher average borrowings from large senior note issuances, partially offset by scheduled debt repayments.  
   ❌ unsupported (judge): The evidence confirms interest expense rose on higher average borrowings from senior note issuances, partially offset by scheduled repayments, but nothing supports that interest coverage remained stable; the scorecard shows interest_coverage at band 3 of 6, indicating middling—not strong—coverage, with no stability trend shown.
   - cites `ORCL-000119312526277521-0190` ✓: “primarily due to higher average borrowings from the issuances of $43.0 billion of senior notes”
   - cites `ORCL-000119312526389274-0082` ✓: “partially offset by lower interest expense due to scheduled repayments of $8.1 billion of debt”
5. The weakest factor, FCF/debt in band **6** [F41], reflects the sharp increase in capital expenditures to expand the Oracle Cloud, a trend the company expects will continue, which outpaced growth in operating cash flows.  
   ✅ supported (judge): Capex rose $34.4B to support cloud growth, outpacing the $11.2B increase in operating cash flows, and Oracle states its data center expansion for the Oracle Cloud is expected to continue.
   - cites `ORCL-000119312526277521-0035` ✓: “We have invested in the rapid expansion of the Oracle Cloud by increasing existing data center capacity and adding data centers in new geographic locations”
   - cites `ORCL-000119312526277521-0198` ✓: “primarily due to a $34.4 billion increase in capital expenditures”
6. The liquidity coverage score in band **6** [F43] overstates liquidity risk because the metric assumes no undrawn revolver capacity, whereas the company maintains an undrawn revolving credit facility that tempers this weakest-band reading.  
   ◐ partially supported (judge): The evidence confirms an undrawn $10.0B revolving facility exists, but nothing in the evidence describes the liquidity_coverage metric's methodology or shows it assumes no undrawn revolver capacity; indeed another factor explicitly incorporates undrawn revolver.
   - cites `ORCL-000119312526277521-0298` ✓: “which provides for an unsecured $10.0 billion, five-year revolving credit facility (the Revolving Facility) to us for working capital purposes and for other general corporate purposes”
   - cites `ORCL-000119312526277521-0299` ✓: “we may borrow, prepay and reborrow amounts under the Revolving Facility during the term of the Revolving Credit Agreement”

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
- [ ] **partially supported claim** (warning): Financial risk: partially supported (The gross leverage endpoints (4.04x to 3.96x) and the 4.59x FY0 peak, plus the net leverage endpoints (3.55x to 2.87x), match the metrics, but the claim that net leverage 'improved steadily' goes beyond the evidence since no intermediate net leverage values are provided.): “Gross debt / EBITDA was stable over the review window, moving from 4.04x in the fiscal year ended 31 May 2024 to 3.96x in the twelve months to 31 August 2026 after peaking at 4.59x in the fiscal year ended 31 May 2026, while net leverage improved steadily from 3.55x to 2.87x.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The dollar figures match the LTM metrics, but the claim characterizes them as projected next-twelve-month needs, whereas the evidence only provides historical twelve-month actuals, not projections.): “Projected next-twelve-month needs at the twelve months to 31 August 2026 include capital expenditure of $75.7 billion, dividends of $5.9 billion and short-term debt of $7.6 billion.”
- [ ] **partially supported claim** (warning): Liquidity: partially supported (The $19.9 billion ATM net proceeds in Q1 fiscal 2027 is supported, but the evidence says nothing about a coverage ratio or whether these proceeds were outside its captured sources.): “Net proceeds of $19.9 billion from common stock issuance under the ATM Program in the most recent quarter provided incremental liquidity beyond the sources captured in the coverage ratio.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (Both factors are indeed in band 3 with weights of 25% and 10%, and interest coverage carries the largest weight; however, near-term maturity cover's 10% weight only ties net debt/EBITDA, so calling these two 'the strongest-scoring factors' overstates the evidence.): “The strongest-scoring factors are interest coverage, in band 3 with the largest weight of 25.0%, and near-term maturity cover, in band 3 with a weight of 10.0%.”
- [ ] **unsupported claim** (warning): Rating rationale: unsupported (The evidence confirms interest expense rose on higher average borrowings from senior note issuances, partially offset by scheduled repayments, but nothing supports that interest coverage remained stable; the scorecard shows interest_coverage at band 3 of 6, indicating middling—not strong—coverage, with no stability trend shown.): “The strong interest coverage score is supported by coverage that remained stable even as interest expense rose on higher average borrowings from large senior note issuances, partially offset by scheduled debt repayments.”
- [ ] **partially supported claim** (warning): Rating rationale: partially supported (The evidence confirms an undrawn $10.0B revolving facility exists, but nothing in the evidence describes the liquidity_coverage metric's methodology or shows it assumes no undrawn revolver capacity; indeed another factor explicitly incorporates undrawn revolver.): “The liquidity coverage score in band 6 overstates liquidity risk because the metric assumes no undrawn revolver capacity, whereas the company maintains an undrawn revolving credit facility that tempers this weakest-band reading.”

## Figures and their sources

| Ref | Figure | Value | Formula | XBRL facts |
|---|---|---|---|---|
| F1 | Revenue (revenue:FY-2) | $53.0 billion | rank 1: Revenues | Revenues 52,961,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F2 | Revenue (revenue:FY0) | $67.4 billion | rank 1: Revenues | Revenues 67,357,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F3 | Revenue (revenue:LTM) | $71.8 billion | rank 2: RevenueFromContractWithCustomerExcludingAssessedTax | RevenueFromContractWithCustomerExcludingAssessedTax 67,357,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 19,345,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>RevenueFromContractWithCustomerExcludingAssessedTax 14,926,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F4 | EBITDA (ebitda:FY0) | $29.9 billion | operating_income + d_and_a | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F5 | EBITDA (ebitda:LTM) | $33.9 billion | operating_income + d_and_a | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,156,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 1,351,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 202,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F6 | Debt / EBITDA (debt_to_ebitda:FY-2) | 4.04x | total_debt / EBITDA | LongTermNotesAndLoans 76,264,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>DebtCurrent 10,605,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>FinanceLeaseLiability 0 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>OperatingIncomeLoss 15,353,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,129,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 3,010,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F7 | Debt / EBITDA (debt_to_ebitda:LTM) | 3.96x | total_debt / EBITDA | LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityCurrent 749,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 8,436,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F8 | Debt / EBITDA (debt_to_ebitda:FY0) | 4.59x | total_debt / EBITDA | LongTermNotesAndLoans 122,342,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 620,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 7,081,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F9 | Net leverage (net_leverage:FY-2) | 3.55x | (total_debt - cash - short_term_investments) / EBITDA | LongTermNotesAndLoans 76,264,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>DebtCurrent 10,605,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>FinanceLeaseLiability 0 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 10,454,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 207,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>OperatingIncomeLoss 15,353,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,129,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 3,010,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F10 | Net leverage (net_leverage:LTM) | 2.87x | (total_debt - cash - short_term_investments) / EBITDA | LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityCurrent 749,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 8,436,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 36,369,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F11 | EBITDA / interest (interest_coverage:FY-2) | 6.12x | EBITDA / interest_expense | OperatingIncomeLoss 15,353,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,129,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 3,010,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>InterestExpense 3,514,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F12 | EBITDA / interest (interest_coverage:FY0) | 6.50x | EBITDA / interest_expense | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>InterestExpense 4,599,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F13 | EBITDA / interest (interest_coverage:LTM) | 6.65x | EBITDA / interest_expense | OperatingIncomeLoss 20,606,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>OperatingIncomeLoss 6,728,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>OperatingIncomeLoss 4,277,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 7,623,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>Depreciation 3,156,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>Depreciation 1,351,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AmortizationOfIntangibleAssets 1,671,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>AmortizationOfIntangibleAssets 202,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F14 | FCF / debt (fcf_to_debt:FY-2) | 13.6% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 18,673,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 6,866,000,000 (2023-06-01 to 2024-05-31, FY-2) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermNotesAndLoans 76,264,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>DebtCurrent 10,605,000,000 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm)<br>FinanceLeaseLiability 0 (at 2024-05-31, balance sheet) [10-K 0000950170-25-087926](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| F15 | FCF / debt (fcf_to_debt:LTM) | -21.3% | (cfo - capex) / total_debt | NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 23,103,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,140,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 28,499,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 8,502,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F16 | Capital expenditure (capex:LTM) | $75.7 billion | rank 1: PaymentsToAcquirePropertyPlantAndEquipment | PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 28,499,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 8,502,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F17 | Cash from operations (cfo:LTM) | $46.9 billion | rank 1: NetCashProvidedByUsedInOperatingActivities | NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 23,103,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,140,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F18 | Total debt (borrowings plus finance-lease liabilities) (total_debt:FY0) | $137.2 billion | rank 5: LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | LongTermNotesAndLoans 122,342,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 620,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 7,081,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F19 | Total debt (borrowings plus finance-lease liabilities) (total_debt:LTM) | $134.5 billion | rank 5: LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | LongTermNotesAndLoans 117,712,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityCurrent 749,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 8,436,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F20 | Liquidity coverage (liquidity_coverage:FY0) | 0.93x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 31,289,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 605,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsOfDividendsCommonStock 5,787,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F21 | Liquidity coverage (liquidity_coverage:LTM) | 0.94x | (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends) | CashAndCashEquivalentsAtCarryingValue 36,369,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 31,977,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 23,103,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NetCashProvidedByUsedInOperatingActivities 8,140,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 55,663,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsToAcquirePropertyPlantAndEquipment 28,499,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F22 | Cash and cash equivalents (cash:LTM) | $36.4 billion | rank 1: CashAndCashEquivalentsAtCarryingValue | CashAndCashEquivalentsAtCarryingValue 36,369,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F23 | Short-term investments (short_term_investments:LTM) | $708 million | rank 3: AvailableForSaleSecuritiesDebtSecuritiesCurrent | AvailableForSaleSecuritiesDebtSecuritiesCurrent 708,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F24 | Dividends paid (dividends:LTM) | $5.9 billion | rank 2: PaymentsOfDividendsCommonStock | PaymentsOfDividendsCommonStock 5,787,000,000 (2025-06-01 to 2026-05-31, FY0) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>PaymentsOfDividendsCommonStock 1,565,000,000 (2026-06-01 to 2026-08-31, current year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>PaymentsOfDividendsCommonStock 1,413,000,000 (2025-06-01 to 2025-08-31, prior-year year-to-date) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F25 | Short-term debt (short-term borrowings plus current portion of long-term debt) (short_term_debt:LTM) | $7.6 billion | rank 4: NotesPayableCurrent | NotesPayableCurrent 7,625,000,000 (at 2026-08-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F26 | Debt maturing in the next twelve months (maturity_year_1:FY0) | $7.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths 7,210,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F27 | Debt maturing in year two (maturity_year_2:FY0) | $10.1 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F28 | Debt maturing in year three (maturity_year_3:FY0) | $5.5 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree 5,500,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F29 | Debt maturing in year four (maturity_year_4:FY0) | $7.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour 7,250,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F30 | Debt maturing in year five (maturity_year_5:FY0) | $9.8 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive 9,750,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F31 | Debt maturing after year five (maturity_after_year_5:FY0) | $90.2 billion | rank 1: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive 90,250,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F32 | Debt due within 24 months (debt_due_24m:FY0) | $17.3 billion | short_term_debt + maturity_year_2 | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| F33 | Share of debt due within 24 months (share_due_24m:FY0) | 12.6% | (short_term_debt + maturity_year_2) / total_debt | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermNotesAndLoans 122,342,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>FinanceLeaseLiabilityCurrent 620,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>FinanceLeaseLiabilityNoncurrent 7,081,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F34 | Near-term maturity cover (near_term_maturity_cover:FY0) | 0.54x | (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver) | DebtCurrent 7,199,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo 10,145,000,000 (at 2026-05-31, balance sheet) [10-K 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm)<br>CashAndCashEquivalentsAtCarryingValue 31,289,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm)<br>AvailableForSaleSecuritiesDebtSecuritiesCurrent 605,000,000 (at 2026-05-31, balance sheet) [10-Q 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| F35 | SB grade (a stylized scorecard grade, not a credit rating) (sb_grade:latest) | 4.35 | weighted score mapped to SB-1 ... SB-6 (config/grid.yaml) | — |
| F36 | SB weighted score (1 strongest, 6 weakest) (sb_score:latest) | 4.35 | sum of weight x band over the factors scored, divided by their weights | — |
| F37 | EBITDA / interest: scorecard band (1 strongest, 6 weakest) (band_interest_coverage:latest) | 3 | band of interest_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F38 | EBITDA / interest: scorecard weight (weight_interest_coverage:latest) | 25.0% | config/grid.yaml (grid-v1) | — |
| F39 | Debt due in 24 months / (cash + undrawn revolver): scorecard band (1 strongest, 6 weakest) (band_near_term_maturity_cover:latest) | 3 | band of near_term_maturity_cover:FY0 on config/grid.yaml (grid-v1) | — |
| F40 | Debt due in 24 months / (cash + undrawn revolver): scorecard weight (weight_near_term_maturity_cover:latest) | 10.0% | config/grid.yaml (grid-v1) | — |
| F41 | FCF / debt: scorecard band (1 strongest, 6 weakest) (band_fcf_to_debt:latest) | 6 | band of fcf_to_debt:LTM on config/grid.yaml (grid-v1) | — |
| F42 | FCF / debt: scorecard weight (weight_fcf_to_debt:latest) | 20.0% | config/grid.yaml (grid-v1) | — |
| F43 | Liquidity sources / uses: scorecard band (1 strongest, 6 weakest) (band_liquidity_coverage:latest) | 6 | band of liquidity_coverage:LTM on config/grid.yaml (grid-v1) | — |
| F44 | Liquidity sources / uses: scorecard weight (weight_liquidity_coverage:latest) | 15.0% | config/grid.yaml (grid-v1) | — |
| F45 | Debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_debt_to_ebitda:latest) | 4 | band of debt_to_ebitda:LTM on config/grid.yaml (grid-v1) | — |
| F46 | Net debt / EBITDA: scorecard band (1 strongest, 6 weakest) (band_net_leverage:latest) | 4 | band of net_leverage:LTM on config/grid.yaml (grid-v1) | — |

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

### ORCL-000119312526277521-0059

risk_factors, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 72382–73851

> supply chain costs, energy costs or other costs to develop, produce or distribute our products and services result in greater costs than anticipated;
> •
> we are unable to accurately anticipate, pay for, plan for and manage future data center capacity needs in a timely manner to meet current or expected customer demand;
> •
> we fail to meet our contractual service level commitments;
> •
> there is a delay in market acceptance of and difficulty in transitioning new and existing customers to new, enhanced or acquired product lines or services;
> •
> sanctions, tariffs, export controls, geopolitical instability, strained economic relationships between countries and related market disruptions or other regulatory, legislative or trade and non-tariff barriers, including retaliatory measures, impede or prevent us from serving certain customers based on their location, jurisdiction of incorporation, ownership, control or other ties to restricted jurisdictions, or restrict us or our customers from operating in specific jurisdictions;
> •
> inflation, trade policy, geopolitical conditions and other macroeconomic factors reduce customer demand or their ability to pay for our products and services or cause us to be unable to meet current or expected customer demand;
> •
> there are changes in IT trends that we do not adequately anticipate or timely address with our product development efforts;
> •
> we do not optimize complementary product lines and services in a timely manner; or
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

### ORCL-000119312526277521-0198

liquidity, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 230187–231635

> Cash flows from operating activities: Our largest source of operating cash flows is cash collections from our customers following the purchase and renewal of their cloud and software support agreements. Over the course of a fiscal year, we also generate cash from the sales of software licenses, hardware offerings and other services. Our primary uses of cash from operating activities are typically for employee-related expenditures, expenses related to data center leases and power for our cloud business, taxes, and interest payments.
> Net cash provided by operating activities increased by $11.2 billion in fiscal 2026 relative to fiscal 2025 primarily due to higher net income adjusted for certain non-cash charges and higher cash favorable working capital changes, net, which includes $4.6 billion cash inflows from customer prepayments with significant financing component.
> Cash flows from investing activities: The changes in cash flows from investing activities primarily relate to our investments in capital assets to support the growth in our cloud and software business and purchases, maturities and sales of our investments in marketable securities and other instruments.
> Net cash used for investing activities increased by $30.1 billion in fiscal 2026 relative to fiscal 2025 primarily due to a $34.4 billion increase in capital expenditures, partially offset by $4.3 billion of cash proceeds from the sale of our investment in Ampere.

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

### ORCL-000119312526277521-0300

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 341156–342288

> The Revolving Credit Agreement contains certain customary representations and warranties, covenants and events of default, including the requirement that the ratio of “Consolidated EBITDA” to “Consolidated Net Interest Expense” (each term as defined in the Revolving Credit Agreement) of Oracle and its subsidiaries shall not be less than 3.0 to 1.0 at the end of any fiscal quarter during the period that the Revolving Credit Agreement is effective. If an event of default occurs under the Revolving Credit Agreement and is not cured within applicable grace periods or waived, any unpaid amounts under the Revolving Credit Agreement may be declared immediately due and payable and the commitments under the agreement may be terminated.
> Term Loan Credit Agreements
> During fiscal 2023, pursuant to a term loan credit agreement (Term Loan Credit Agreement) providing for an aggregate term loan commitment of $5.6 billion, we borrowed $4.7 billion under term loan 1 facility (Term Loan 1 Facility) and $960 million under term loan 2 facility (Term Loan 2 Facility and, together with the Term Loan 1 Facility, the Term Loan Facilities).

### ORCL-000119312526277521-0301

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 342289–343781

> During fiscal 2025, we terminated our Term Loan Credit Agreement and repaid the principal amount outstanding together with interest accrued up to the date of repayment. Simultaneously, we borrowed up to the maximum commitment amount of $5.6 billion pursuant to a term loan credit agreement (Term Loan Credit Agreement 2) executed on the same date. The critical terms of the Term Loan Credit Agreement 2 are similar to the critical terms of the Term Loan Credit Agreement, except for terms related to the interest, the consolidation of two term loan facilities under Term Loan Credit Agreement into a single facility under the Term Loan Credit Agreement 2 and the options to extend the Term Loan Credit Agreement 2. Interest is based on either (a) a Term SOFR-based formula plus a margin of 112.5 basis points to 162.5 basis points, depending on the credit rating assigned to our long-term senior unsecured debt, or (b) a Base Rate formula plus a margin of 12.5 basis points to 62.5 basis points, depending on the same such credit rating, each as set forth in the Term Loan Credit Agreement 2.
> The Term Loan Credit Agreement 2 provides for repayment of borrowing as follows:
> •
> an amount equal to the amount borrowed reduced by any prepayments multiplied by 1.25% on September 30, 2024 and quarterly thereafter until June 30, 2026;
> •
> an amount equal to the amount borrowed reduced by any prepayments multiplied by 2.50% on September 30, 2026 and quarterly thereafter until June 30, 2027; and
> 85

### ORCL-000119312526277521-0302

debt_note, [10-K for 2026-05-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm), characters 343782–345124

> Table of Contents
> •
> any remaining unpaid principal balance under the Term Loan Credit Agreement 2 will become fully due and payable on August 16, 2027 (subject to any extension of the Term Loan Credit Agreement 2 termination date, as set out below), unless the outstanding loans are prepaid earlier at the request of Oracle or accelerated by the lenders if an event of default occurs.
> The termination date of the Term Loan Credit Agreement 2 may be extended at our sole option by up to 2 years. The termination date of the Term Loan Credit Agreement 2 may also be further extended at each lender’s option by up to 2 years.
> Commercial Paper Program and Commercial Paper Notes
> On March 6, 2026, our commercial paper program was increased to $10.0 billion. Our commercial paper program allows us to issue and sell unsecured short-term promissory notes (Commercial Paper Notes) pursuant to a private placement exemption from the registration requirements under federal and state securities laws pursuant to dealer agreements with various banks and an Issuing and Paying Agency Agreement with Deutsche Bank Trust Company Americas.
> There were $1.5 billion and $2.3 billion of outstanding Commercial Paper Notes as of May 31, 2026 and 2025, respectively. We used the net proceeds from the issuance of commercial paper for general corporate purposes.

### ORCL-000119312526389274-0060

mdna, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm), characters 74948–76294

> Our services business, which represented 8% of our total revenues on a trailing four-quarter basis, helps customers and partners maximize the performance of their investments in Oracle applications and infrastructure technologies. We believe that our services are differentiated based on our focus on Oracle technologies, extensive experience, broad sets of intellectual property and best practices. Our services offerings include consulting services and customer success services. Services revenues are generally recognized over time as the services are performed. The cost of providing our services consists primarily of personnel-related expenses, technology infrastructure expenditures, facilities expenses and external contractor expenses. Our services business has lower margins than our cloud and software and hardware businesses. Our services revenues are affected by many factors including our strategy for, and the competitive position of, our services; customer demand for our cloud and software and hardware offerings and the related services that we may market and sell in connection with these offerings; general economic conditions; governmental budgetary constraints; personnel reductions in our customers’ IT departments; tighter controls over customer discretionary spending; and foreign currency rate fluctuations.
> Acquisitions

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

### ORCL-000119312526389274-0087

liquidity, [10-Q for 2026-08-31](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm), characters 108204–109691

> Cash, cash equivalents and marketable securities: Cash and cash equivalents primarily consist of deposits held at major banks, money market funds and other securities with original maturities of 90 days or less. Marketable securities consist primarily of time deposits with original maturities at the time of purchase greater than 90 days. The increase in cash, cash equivalents and marketable securities as of August 31, 2026 in comparison to May 31, 2026 was primarily due to $23.1 billion of cash inflows from our operations, which includes $11.4 billion of customer prepayments with a significant financing component; and $19.9 billion of cash proceeds from the issuance of common stock via the ATM Program, net of issuance costs, partially offset by $28.5 billion of cash used for capital expenditures; $3.1 billion of cash used for scheduled repayments of debt; $2.6 billion of restricted cash that was reclassed to prepaid expenses and other current assets; $1.6 billion of cash used to pay dividends to our common and preferred stockholders; $1.1 billion of cash used for repayment of commercial paper; $830 million of cash outflows for short-term financing related to capital expenditures, net; and $242 million of cash outflows for other financing activities, net, in each case during the first quarter of fiscal 2027. Our cash and cash equivalents may be impacted by some or all of the aforementioned factors in future periods, the amounts and timing of which are variable.
> 33

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

Run `ORCL-20261118T062236Z-GLM-5.3`; service tier asap; reasoning effort {'writer': 'medium', 'judge': 'low'}.
Drafting: 8 calls, 32,436 input (8,960 cached) and 26,446 output tokens, $0.1061, 196s. Verification: 35 calls, 19,421 input (4,480 cached) and 3,943 output tokens, $0.0276, 65s. Prices read 2026-11-17. Raw requests and responses: data/runs/ORCL/ORCL-20261118T062236Z-GLM-5.3.jsonl.
