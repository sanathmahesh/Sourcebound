# Evals: what the author fills in

Everything in this folder that holds a value is entered by hand by the author. Sourcebound never fills in
golden-set values, claim labels, agency ratings or timings.

## golden/<TICKER>.md — hand-verified figures (WMT, VZ, GT, HCA, CCL)

1. Open the 10-K linked at the top of the sheet. Fill in **Value in filing** and **Page or note** for
   inputs 1–19, in the filing's own units (usually millions). Do this **before** looking at
   `reports/ratios/<TICKER>.md` or `data/published/`, so your values are independent of the tool's.
2. Work out D1–D7 with a calculator from your own values, using the formulas given. They match the
   engine's definitions (finance leases count as debt; "debt due within 12 months" is row 7).
3. Answer Q1–Q5 with the exact section and page.
4. A phase-5 script adds Sourcebound's values and a match column. Pass rule: inputs equal after rounding to
   the filing's unit; ratios within 0.05x or 1 percentage point.

## agency_ratings.csv — agency ratings for the scorecard comparison

One row per company per agency:

```
ticker,agency,rating,date,source
XOM,S&P,<rating>,<date of the rating or of your lookup>,<URL or document>
```

Use the long-term issuer credit rating. Ratings are the agencies' property: by default the site shows only
aggregate agreement (rank correlation and IG/HY agreement), never per-company ratings. The scorecard code
never reads this file; `tests/test_scorecard.py` enforces it.
