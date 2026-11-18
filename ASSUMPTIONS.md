# Assumptions

Simplifying assumptions the numbers rest on. Items 1–14 are seeded from PLAN.md section 4.14; later items
were added while building, with the phase that added them.

## Seeded from the plan

1. US non-financial 10-K filers only; no banks, insurers or companies with large captive finance arms.
2. EBITDA is unadjusted: operating income plus depreciation and amortisation.
3. Debt is reported borrowings; operating leases, pensions and guarantees are excluded.
4. Each period uses the most recently filed value.
5. LTM is derived from year-to-date figures.
6. Liquidity uses trailing cash flow as a stand-in for the next 12 months; undrawn revolver capacity
   counts only if tagged.
7. The maturity ladder comes from the annual 10-K.
8. Optional components that are not reported are treated as zero, logged, and shown to the reviewer.
9. The narrative corpus is the latest 10-K and later 10-Qs only.
10. The scorecard is financial-ratio-only, stylized, and frozen before comparison with agency ratings.
11. The judge is a language model; its verdicts are estimates calibrated against a human-labelled sample.
12. Reviewer sign-off in the interface is a demonstration stored in the browser.
13. Memos are dated snapshots; refreshed ratios may be newer than the memo.
14. Timings are self-recorded by a non-expert on a few companies.

## Added in phase 1

15. Facts come only from 10-K, 10-Q and their amendments; facts the company-facts API carries from other
    forms (8-K, registration statements) are ignored. Values in US dollars only.
16. A fact belongs to a period only if its start and end dates equal the period's window exactly.
17. "Annual" means 360 to 372 days between start and end dates (52-week, calendar and 53-week years).
18. FY0 is the annual window ending on the latest 10-K's report date (from the submissions API); FY-1 and
    FY-2 are the annual windows ending the day before the later year starts.
19. LTM uses the latest 10-Q's longest non-annual window ending on its report date (current year-to-date)
    and its longest window ending about a year earlier (prior-year year-to-date). The windows must line up
    (start dates, lengths within 7 days) or LTM is not available. With no 10-Q newer than the 10-K, LTM
    equals FY0, and the report says so.
20. One LTM value uses one candidate across all three windows; tags are never mixed within it.
21. Ranks are applied period by period, so different periods can resolve through different tags; this
    is noted in the log ("mixed ranks").
22. Short-term investments are a chain (the first of ShortTermInvestments, MarketableSecuritiesCurrent,
    AvailableForSaleSecuritiesDebtSecuritiesCurrent that is reported), not a sum, to avoid double counting.
23. "Pre-tax income from continuing operations" is matched by either of its two common us-gaap tags
    (ranks 2 and 3 of operating income).
24. Ratio edge cases apply in this order: missing input -> not available; zero debt -> leverage 0 and
    FCF / debt not meaningful; EBITDA <= 0 -> leverage and coverage not meaningful; interest expense <= 0
    -> coverage not meaningful.
25. Cash for net leverage is cash and cash equivalents plus short-term investments. FCF / debt is stated
    in percent; capital expenditure is used as reported (a positive payment).
26. The EDGAR cache does not expire. Delete data/raw/ to download fresh data.
27. Unit tests use synthetic values with the fictional accession prefix 0000000000. Real-company values
    appear only in fixture tests, each with its accession number.
28. Finance-lease liabilities count as debt for every company (approved 17 November 2026, decision D18).
    Operating leases, pensions and guarantees remain excluded (assumption 3).
29. InterestExpense and InterestExpenseNonoperating are taken to include finance-lease interest. When only
    InterestExpenseDebt is reported, FinanceLeaseInterestExpense is added (assumed zero if not reported).

## Added in phase 2

30. Debt due within 12 months is the balance-sheet short-term debt (short-term borrowings plus current
    portion of long-term debt) at each period's date; it counts as zero when no tag is reported (D19, D21).
31. Net interest (interest expense net of interest income) is used, flagged, when no gross interest-expense
    tag is reported (D19).
32. In liquidity and near-term cover, cash means cash and cash equivalents plus short-term investments.
33. The maturity ladder, debt due within 24 months (short-term debt + ladder year 2) and near-term maturity
    cover are as of FY0. The year-1 maturity falls back to the balance-sheet current portion of long-term
    debt when the table's year-1 tag is missing (D19).
34. The "latest" scorecard uses LTM ratios and the FY0 near-term maturity cover; a value on a band
    threshold takes the worse band; special statuses map to fixed bands as set out in D22.
35. Trend direction runs from FY-2 to LTM; stable within 10% (at least 0.1x) for multiples and within 2
    percentage points for percentages.
36. Revenue moving more than 40% between consecutive fiscal years raises a "possible structural change"
    warning; values are not adjusted.
37. A 10-K or 10-Q without facts in the company's XBRL data is skipped in favour of the newest one with
    facts, and flagged as stale data (D24).
38. ExxonMobil is analysed through its predecessor registrant, Exxon Mobil Corp, under an approved override;
    its latest figures are to 31 March 2026 (D20).
