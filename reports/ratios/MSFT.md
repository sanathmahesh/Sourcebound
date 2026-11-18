# MSFT: MICROSOFT CORP

Check report. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 789019
- Company facts downloaded from EDGAR: 2026-11-18T02:55:29+00:00; report generated 2026-11-18 03:19 UTC
- Latest 10-K: 10-K for the period ended 2026-06-30, filed 2026-07-29, accession 0001193125-26-323660 ([EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm))
- Latest 10-Q: 10-Q for the period ended 2026-09-30, filed 2026-10-28, accession 0001193125-26-436133 ([EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm))

## Periods

| Period | Flow items (income statement, cash flow) | Balance-sheet date |
|---|---|---|
| FY-2 | 2023-07-01 to 2024-06-30 | 2024-06-30 |
| FY-1 | 2024-07-01 to 2025-06-30 | 2025-06-30 |
| FY0 | 2025-07-01 to 2026-06-30 | 2026-06-30 |
| LTM | + FY0 (2025-07-01 to 2026-06-30) + current year-to-date (2026-07-01 to 2026-09-30) − prior-year year-to-date (2025-07-01 to 2025-09-30) | 2026-09-30 |

- LTM: LTM to 2026-09-30 = FY0 + (2026-07-01 to 2026-09-30) - (2025-07-01 to 2025-09-30), from 10-Q 0001193125-26-436133

## Summary

| Metric | FY-2 | FY-1 | FY0 | LTM |
|---|---|---|---|---|
| EBITDA | $129,433m | $156,528m | $194,237m | $205,691m |
| Debt / EBITDA | 0.61x | 0.57x | 0.55x | 0.52x |
| Net leverage | 0.02x | -0.03x (net cash) | 0.15x | 0.20x |
| EBITDA / interest | 44.10x | 65.63x | 63.66x | 63.82x |
| FCF / debt | 94.0% | 80.2% | 62.7% | 56.3% |
| Liquidity coverage | 2.58x | 2.52x | 1.71x | 1.56x |

## Warnings (2)

- **total_debt FY-2**: total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $78,775m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $72,082m (-8.5%). Check which matches the balance sheet.
- **maturity_ladder FY0**: maturity ladder $46,136m + short-term borrowings $0m + finance leases $66,594m = $112,730m, against total debt $106,888m (+5.5%)

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 78,775 · operating_income 109,433 · d_and_a 20,000 → **0.61x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 42,688 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,249 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | CommercialPaper | 2 | 6,693 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 27,145 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 109,433 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 15,200 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,800 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 89,323 · operating_income 128,528 · d_and_a 28,000 → **0.57x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 40,152 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,999 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | CommercialPaper | 2 | 0 | at 2025-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 46,172 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 128,528 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 22,000 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 6,000 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 106,888 · operating_income 155,237 · d_and_a 39,000 → **0.55x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 31,067 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 66,594 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 155,237 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 34,300 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,700 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 106,454 · operating_income 163,191 · d_and_a 42,500 → **0.52x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 31,090 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 4,391 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 70,973 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 155,237 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 45,915 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 37,961 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | Depreciation | 4 | 34,300 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 11,100 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | Depreciation | 4 | 7,100 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,700 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,000 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,500 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 78,775 · cash 18,315 · short_term_investments 57,228 · operating_income 109,433 · d_and_a 20,000 → **0.02x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 42,688 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,249 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | CommercialPaper | 2 | 6,693 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 27,145 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 18,315 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 57,228 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 109,433 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 15,200 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,800 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 89,323 · cash 30,242 · short_term_investments 64,323 · operating_income 128,528 · d_and_a 28,000 → **-0.03x (net cash)**  
**Status:** net cash: cash exceeds debt  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 40,152 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,999 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | CommercialPaper | 2 | 0 | at 2025-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 46,172 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 30,242 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 64,323 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 128,528 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 22,000 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 6,000 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 106,888 · cash 20,935 · short_term_investments 55,908 · operating_income 155,237 · d_and_a 39,000 → **0.15x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 31,067 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 66,594 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 20,935 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 55,908 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 155,237 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 34,300 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,700 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 106,454 · cash 20,281 · short_term_investments 44,228 · operating_income 163,191 · d_and_a 42,500 → **0.20x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 31,090 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 4,391 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 70,973 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 20,281 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 44,228 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 155,237 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 45,915 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 37,961 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | Depreciation | 4 | 34,300 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 11,100 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | Depreciation | 4 | 7,100 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,700 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,000 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,500 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

### EBITDA / interest — FY-2

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 109,433 · d_and_a 20,000 · interest_expense 2,935 → **44.10x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 109,433 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 15,200 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,800 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| interest_expense | InterestExpense | 1 | 2,935 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0000950170-24-087843 | 2024-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/0000950170-24-087843-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 128,528 · d_and_a 28,000 · interest_expense 2,385 → **65.63x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 128,528 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 22,000 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 6,000 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 2,385 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 155,237 · d_and_a 39,000 · interest_expense 3,051 → **63.66x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 155,237 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 34,300 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,700 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 3,051 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 163,191 · d_and_a 42,500 · interest_expense 3,223 → **63.82x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 155,237 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 45,915 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 37,961 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | Depreciation | 4 | 34,300 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | Depreciation | 4 | 11,100 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | Depreciation | 4 | 7,100 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 4,700 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,000 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,500 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 3,051 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 870 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 698 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 118,548 · capex 44,477 · total_debt 78,775 → **94.0%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 118,548 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 44,477 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 42,688 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,249 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | CommercialPaper | 2 | 6,693 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 27,145 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 136,162 · capex 64,551 · total_debt 89,323 → **80.2%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 136,162 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 64,551 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 40,152 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,999 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | CommercialPaper | 2 | 0 | at 2025-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 46,172 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 182,935 · capex 115,948 · total_debt 106,888 → **62.7%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 182,935 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 115,948 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 31,067 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 66,594 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 195,878 · capex 135,921 · total_debt 106,454 → **56.3%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 182,935 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 58,000 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 45,057 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 115,948 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 39,367 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 19,394 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 31,090 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 4,391 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 70,973 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

### Liquidity coverage — FY-2

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 18,315 · short_term_investments 57,228 · undrawn_revolver 0 · cfo 118,548 · short_term_debt 8,942 · capex 44,477 · dividends 21,771 → **2.58x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 18,315 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 57,228 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 118,548 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 2,249 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| short_term_debt | CommercialPaper | 2 | 6,693 | at 2024-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 44,477 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 21,771 | 2023-07-01 to 2024-06-30 (FY-2) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Liquidity coverage — FY-1

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 30,242 · short_term_investments 64,323 · undrawn_revolver 0 · cfo 136,162 · short_term_debt 2,999 · capex 64,551 · dividends 24,082 → **2.52x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 30,242 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 64,323 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 136,162 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 2,999 | at 2025-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| short_term_debt | CommercialPaper | 2 | 0 | at 2025-06-30 (balance sheet) | 10-K | 0000950170-25-100235 | 2025-07-30 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/0000950170-25-100235-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 64,551 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 24,082 | 2024-07-01 to 2025-06-30 (FY-1) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Liquidity coverage — FY0

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 20,935 · short_term_investments 55,908 · undrawn_revolver 0 · cfo 182,935 · short_term_debt 9,227 · capex 115,948 · dividends 26,445 → **1.71x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 20,935 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 55,908 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 182,935 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 115,948 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 26,445 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Liquidity coverage — LTM

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 20,281 · short_term_investments 44,228 · undrawn_revolver 0 · cfo 195,878 · short_term_debt 4,391 · capex 135,921 · dividends 27,033 → **1.56x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 20,281 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 44,228 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 182,935 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 58,000 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 45,057 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 4,391 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 115,948 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 39,367 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 19,394 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 26,445 | 2025-07-01 to 2026-06-30 (FY0) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 6,757 | 2026-07-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 6,169 | 2025-07-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

## Maturity ladder (FY0, from the latest 10-K)

| Bucket | Tag | Value ($m) | Accession |
|---|---|---|---|
| Debt maturing in the next twelve months | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | 9,250 | 0001193125-26-323660 |
| Debt maturing in year two | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 0 | 0001193125-26-323660 |
| Debt maturing in year three | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | 2,001 | 0001193125-26-323660 |
| Debt maturing in year four | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | 0 | 0001193125-26-323660 |
| Debt maturing in year five | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | 500 | 0001193125-26-323660 |
| Debt maturing after year five | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | 34,385 | 0001193125-26-323660 |
| **Total** | | 46,136 | |

### Debt due within 24 months — FY0

**Formula:** short_term_debt + maturity_year_2  
**Inputs ($m):** short_term_debt 9,227 · maturity_year_2 0 → **$9,227m**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 0 | at 2026-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |

### Share of debt due within 24 months — FY0

**Formula:** (short_term_debt + maturity_year_2) / total_debt  
**Inputs ($m):** short_term_debt 9,227 · maturity_year_2 0 · total_debt 106,888 → **8.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 0 | at 2026-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 31,067 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 66,594 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |

### Near-term maturity cover — FY0

**Formula:** (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)  
**Inputs ($m):** short_term_debt 9,227 · maturity_year_2 0 · cash 20,935 · short_term_investments 55,908 · undrawn_revolver 0 → **0.12x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | LongTermDebtCurrent | 2 | 9,227 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 0 | at 2026-06-30 (balance sheet) | 10-K | 0001193125-26-323660 | 2026-07-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/0001193125-26-323660-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 20,935 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| short_term_investments | ShortTermInvestments | 1 | 55,908 | at 2026-06-30 (balance sheet) | 10-Q | 0001193125-26-436133 | 2026-10-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/0001193125-26-436133-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

## Trends (direction from FY-2 to LTM)

| Ratio | FY-2 | FY-1 | FY0 | LTM | Direction |
|---|---|---|---|---|---|
| Debt / EBITDA | 0.61x | 0.57x | 0.55x | 0.52x | stable |
| Net leverage | 0.02x | -0.03x (net cash) | 0.15x | 0.20x | worsening |
| EBITDA / interest | 44.10x | 65.63x | 63.66x | 63.82x | improving |
| FCF / debt | 94.0% | 80.2% | 62.7% | 56.3% | worsening |
| Liquidity coverage | 2.58x | 2.52x | 1.71x | 1.56x | worsening |

## Scorecard

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

### Basis: latest — weighted 1.30, grade SB-1

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | LTM | 0.52 | 1 | 0.20 |  |
| Net debt / EBITDA | LTM | 0.20 | 1 | 0.10 |  |
| EBITDA / interest | LTM | 63.82 | 1 | 0.25 |  |
| FCF / debt | LTM | 56.32 | 1 | 0.20 |  |
| Liquidity sources / uses | LTM | 1.56 | 3 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 0.12 | 1 | 0.10 |  |

### Basis: FY0 — weighted 1.30, grade SB-1

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | FY0 | 0.55 | 1 | 0.20 |  |
| Net debt / EBITDA | FY0 | 0.15 | 1 | 0.10 |  |
| EBITDA / interest | FY0 | 63.66 | 1 | 0.25 |  |
| FCF / debt | FY0 | 62.67 | 1 | 0.20 |  |
| Liquidity sources / uses | FY0 | 1.71 | 3 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 0.12 | 1 | 0.10 |  |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 78,775 |
| FY-2 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-06-30 |
| FY-2 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-06-30 |
| FY-2 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 72,082 |
| FY-2 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2024-06-30 |
| FY-2 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2024-06-30 |
| FY-1 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 89,323 |
| FY-1 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-06-30 |
| FY-1 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-06-30 |
| FY-1 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 89,323 |
| FY-1 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2025-06-30 |
| FY-1 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2025-06-30 |
| FY0 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 106,888 |
| FY0 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-06-30 |
| FY0 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-06-30 |
| FY0 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 106,888 |
| FY0 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2026-06-30 |
| FY0 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2026-06-30 |
| LTM | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 106,454 |
| LTM | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-09-30 |
| LTM | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-09-30 |
| LTM | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 106,454 |
| LTM | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2026-09-30 |
| LTM | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2026-09-30 |

## Fallback log

### Not available (0)


### Reconciliation (6)

- **total_debt FY-2** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $78,775m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $72,082m (-8.5%). Check which matches the balance sheet.
- **total_debt FY-2**: LongTermDebt $44,937m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $2,249m, LongTermDebtNoncurrent $42,688m
- **total_debt FY-1**: LongTermDebt $43,151m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $2,999m, LongTermDebtNoncurrent $40,152m
- **total_debt FY0**: LongTermDebt $40,294m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $9,227m, LongTermDebtNoncurrent $31,067m
- **total_debt LTM**: LongTermDebt $35,481m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $4,391m, LongTermDebtNoncurrent $31,090m
- **maturity_ladder FY0** (warning): maturity ladder $46,136m + short-term borrowings $0m + finance leases $66,594m = $112,730m, against total debt $106,888m (+5.5%)

### Fallbacks beyond rank 1 (23)

- **revenue FY-2**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2023-07-01 to 2024-06-30
- **d_and_a FY-2**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2023-07-01 to 2024-06-30; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2023-07-01 to 2024-06-30; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2023-07-01 to 2024-06-30
- **short_term_debt FY-2**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2024-06-30
- **finance_lease_liabilities FY-2**: used rank 2 FinanceLeaseLiability because rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2024-06-30
- **dividends FY-2**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2023-07-01 to 2024-06-30
- **revenue FY-1**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2024-07-01 to 2025-06-30
- **d_and_a FY-1**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2024-07-01 to 2025-06-30; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2024-07-01 to 2025-06-30; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2024-07-01 to 2025-06-30
- **interest_expense FY-1**: used rank 2 InterestExpenseNonoperating because rank 1 InterestExpense: InterestExpense not reported for 2024-07-01 to 2025-06-30
- **short_term_debt FY-1**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2025-06-30
- **finance_lease_liabilities FY-1**: used rank 2 FinanceLeaseLiability because rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2025-06-30
- **dividends FY-1**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2024-07-01 to 2025-06-30
- **revenue FY0**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2025-07-01 to 2026-06-30
- **d_and_a FY0**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-07-01 to 2026-06-30; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-07-01 to 2026-06-30; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2025-07-01 to 2026-06-30
- **interest_expense FY0**: used rank 2 InterestExpenseNonoperating because rank 1 InterestExpense: InterestExpense not reported for 2025-07-01 to 2026-06-30
- **short_term_debt FY0**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2026-06-30
- **finance_lease_liabilities FY0**: used rank 2 FinanceLeaseLiability because rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2026-06-30
- **dividends FY0**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-07-01 to 2026-06-30
- **revenue LTM**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2025-07-01 to 2026-06-30
- **d_and_a LTM**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-07-01 to 2026-06-30; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-07-01 to 2026-06-30; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2025-07-01 to 2026-06-30
- **interest_expense LTM**: used rank 2 InterestExpenseNonoperating because rank 1 InterestExpense: InterestExpense not reported for 2025-07-01 to 2026-06-30
- **short_term_debt LTM**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2026-09-30
- **finance_lease_liabilities LTM**: used rank 2 FinanceLeaseLiability because rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2026-09-30
- **dividends LTM**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-07-01 to 2026-06-30

### Assumed zero: not reported (11)

- **short_term_debt FY-2**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **undrawn_revolver FY-2**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2024-06-30)
- **short_term_debt FY-1**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **undrawn_revolver FY-1**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2025-06-30)
- **short_term_debt FY0**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt FY0**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **undrawn_revolver FY0**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-06-30)
- **short_term_debt LTM**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt LTM**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **undrawn_revolver LTM**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-09-30)
- **short_term_borrowings FY0**: assumed zero: not reported (rank 1 ShortTermBorrowings: ShortTermBorrowings not reported at 2026-06-30; rank 2 CommercialPaper: CommercialPaper not reported at 2026-06-30)

### Restated values (most recently filed value used) (0)


### Different candidates across periods (1)

- **interest_expense all**: different candidates across periods (FY-2: rank 1 InterestExpense; FY-1: rank 2 InterestExpenseNonoperating; FY0: rank 2 InterestExpenseNonoperating; LTM: rank 2 InterestExpenseNonoperating)

### Possible structural change (0)


### Stale data (0)
