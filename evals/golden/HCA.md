# Golden-set sheet: HCA Healthcare, Inc. (HCA)

Fill in **Value in filing** from the 10-K below **before** looking at Sourcebound's figures. Leave a
cell blank if the filing does not show the item; write 0 only when it shows zero or no such item.
A script adds Sourcebound's values and a match column afterwards.

| Field | Value |
|---|---|
| Company | HCA Healthcare, Inc. |
| Ticker | HCA |
| Form 10-K, fiscal year ended | 2025-12-31 |
| Accession number | 0001193125-26-044769 |
| Filed | 2026-02-10 |
| Filing | https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm |
| Units in filing (e.g. millions) | |
| Verified by | |
| Date verified | |

## Inputs

| # | Item | Where to look | Value in filing | Page or note |
|---|---|---|---|---|
| 1 | Revenue (total revenues) | Income statement, top line | | |
| 2 | Operating income (if there is no such line: pre-tax income from continuing operations + interest expense) | Income statement | | |
| 3 | Depreciation and amortisation | Cash flow statement, operating activities | | |
| 4 | Interest expense (including interest on finance leases) | Income statement or interest note | | |
| 5 | Cash and cash equivalents | Balance sheet | | |
| 6 | Short-term investments (0 if none) | Balance sheet | | |
| 7 | Short-term borrowings + current portion of long-term debt | Balance sheet, current liabilities | | |
| 8 | Long-term debt excluding current portion | Balance sheet | | |
| 9 | Finance-lease liabilities on their own lines, current + non-current (0 if inside the debt lines) | Balance sheet or lease note | | |
| 10 | Cash from operations | Cash flow statement | | |
| 11 | Capital expenditure | Cash flow statement, investing activities | | |
| 12 | Dividends paid (0 if none) | Cash flow statement, financing activities | | |
| 13 | Undrawn revolver capacity | Liquidity section of MD&A, or the debt note | | |
| 14 | Debt due in year 1 | Debt note, maturity table | | |
| 15 | Debt due in year 2 | Debt note, maturity table | | |
| 16 | Debt due in year 3 | Debt note, maturity table | | |
| 17 | Debt due in year 4 | Debt note, maturity table | | |
| 18 | Debt due in year 5 | Debt note, maturity table | | |
| 19 | Debt due later than year 5 | Debt note, maturity table | | |

## Derived, by calculator from your own values above

| # | Item | Formula | Your value |
|---|---|---|---|
| D1 | EBITDA | 2 + 3 | |
| D2 | Total debt | 7 + 8 + 9 | |
| D3 | Debt / EBITDA | D2 / D1 | |
| D4 | Net debt / EBITDA | (D2 - 5 - 6) / D1 | |
| D5 | EBITDA / interest | D1 / 4 | |
| D6 | FCF / debt (%) | (10 - 11) / D2 x 100 | |
| D7 | Liquidity coverage | (5 + 6 + 13 + 10, using 0 for 10 if it is negative) / (7 + 11 + 12) | |

Pass rule: inputs match after rounding to the filing's unit; ratios within 0.05x or 1 percentage point.

## Fact questions

| # | Question | Answer | Exact location (section and page) | Quote (a few words copied from the passage) |
|---|---|---|---|---|
| Q1 | Size and expiry of the main revolving credit facility | | | |
| Q2 | Financial covenants, and whether the company states it complies | | | |
| Q3 | Largest single debt maturity in the next three years | | | |
| Q4 | Management's stated sources of liquidity | | | |
| Q5 | The risk factor most relevant to repaying debt | | | |
