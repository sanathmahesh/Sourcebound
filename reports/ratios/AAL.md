# AAL: American Airlines Group Inc.

Check report. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 6201
- Company facts downloaded from EDGAR: 2026-11-18T02:56:17+00:00; report generated 2026-11-18 03:19 UTC
- Latest 10-K: 10-K for the period ended 2025-12-31, filed 2026-02-18, accession 0000006201-26-000014 ([EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm))
- Latest 10-Q: 10-Q for the period ended 2026-09-30, filed 2026-10-22, accession 0000006201-26-000065 ([EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm))

## Periods

| Period | Flow items (income statement, cash flow) | Balance-sheet date |
|---|---|---|
| FY-2 | 2023-01-01 to 2023-12-31 | 2023-12-31 |
| FY-1 | 2024-01-01 to 2024-12-31 | 2024-12-31 |
| FY0 | 2025-01-01 to 2025-12-31 | 2025-12-31 |
| LTM | + FY0 (2025-01-01 to 2025-12-31) + current year-to-date (2026-01-01 to 2026-09-30) − prior-year year-to-date (2025-01-01 to 2025-09-30) | 2026-09-30 |

- LTM: LTM to 2026-09-30 = FY0 + (2026-01-01 to 2026-09-30) - (2025-01-01 to 2025-09-30), from 10-Q 0000006201-26-000065

## Summary

| Metric | FY-2 | FY-1 | FY0 | LTM |
|---|---|---|---|---|
| EBITDA | $5,334m | $4,814m | $3,667m | $2,891m |
| Debt / EBITDA | 6.14x | 6.30x | 7.88x | 10.21x |
| Net leverage | 4.70x | 4.83x | 6.26x | 7.31x |
| EBITDA / interest | 2.49x | 2.49x | 2.14x | 1.74x |
| FCF / debt | 3.7% | 4.3% | -2.4% | -0.3% |
| Liquidity coverage | 1.88x | 1.40x | 1.22x | 1.59x |

## Warnings (4)

- **total_debt FY-2**: total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $32,771m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $29,401m (-10.3%). Check which matches the balance sheet.
- **total_debt FY-1**: total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $30,350m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,280m (-16.7%). Check which matches the balance sheet.
- **total_debt FY0**: total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $28,895m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,366m (-12.2%). Check which matches the balance sheet.
- **total_debt LTM**: total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $29,523m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,395m (-14.0%). Check which matches the balance sheet.

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 32,771 · operating_income 3,034 · d_and_a 2,300 → **6.14x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 29,270 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,501 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 3,034 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,300 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 30,350 · operating_income 2,614 · d_and_a 2,200 → **6.30x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,154 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 5,196 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 2,614 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,200 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 28,895 · operating_income 1,467 · d_and_a 2,200 → **7.88x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,254 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,467 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,200 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 29,523 · operating_income 973 · d_and_a 1,918 → **10.21x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,943 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,580 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,467 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 521 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,015 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,890 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,446 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,418 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 32,771 · cash 681 · short_term_investments 7,000 · operating_income 3,034 · d_and_a 2,300 → **4.70x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 29,270 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,501 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 681 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 7,000 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 3,034 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,300 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 30,350 · cash 902 · short_term_investments 6,180 · operating_income 2,614 · d_and_a 2,200 → **4.83x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,154 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 5,196 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 902 | at 2024-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 6,180 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 2,614 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,200 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 28,895 · cash 1,056 · short_term_investments 4,882 · operating_income 1,467 · d_and_a 2,200 → **6.26x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,254 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 1,056 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 4,882 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,467 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,200 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 29,523 · cash 1,228 · short_term_investments 7,163 · operating_income 973 · d_and_a 1,918 → **7.31x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,943 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,580 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 1,228 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 7,163 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,467 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 521 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,015 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,890 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,446 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,418 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |

### EBITDA / interest — FY-2

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 3,034 · d_and_a 2,300 · interest_expense 2,145 → **2.49x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 3,034 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,300 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| interest_expense | InterestExpense | 1 | 2,145 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-24-000010 | 2024-02-21 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620124000010/0000006201-24-000010-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 2,614 · d_and_a 2,200 · interest_expense 1,934 → **2.49x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 2,614 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,200 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 1,934 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 1,467 · d_and_a 2,200 · interest_expense 1,716 → **2.14x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 1,467 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,200 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 1,716 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 973 · d_and_a 1,918 · interest_expense 1,664 → **1.74x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 1,467 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 521 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 1,015 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,890 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,446 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| d_and_a | DepreciationAndAmortization | 2 | 1,418 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 1,716 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 1,242 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| interest_expense | InterestExpenseNonoperating | 2 | 1,294 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 3,803 · capex 2,596 · total_debt 32,771 → **3.7%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,803 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,596 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 29,270 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,501 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 3,983 · capex 2,683 · total_debt 30,350 → **4.3%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,983 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,683 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,154 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 5,196 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 3,099 · capex 3,779 · total_debt 28,895 → **-2.4%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,099 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 3,779 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,254 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 4,267 · capex 4,358 · total_debt 29,523 → **-0.3%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,099 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 4,541 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,373 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 3,779 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,728 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,149 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,943 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,580 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |

### Liquidity coverage — FY-2

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 681 · short_term_investments 7,000 · undrawn_revolver 0 · cfo 3,803 · short_term_debt 3,501 · capex 2,596 · dividends 0 → **1.88x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 681 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 7,000 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,803 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 3,501 | at 2023-12-31 (balance sheet) | 10-K | 0000006201-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620125000010/0000006201-25-000010-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,596 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| dividends | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

### Liquidity coverage — FY-1

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 902 · short_term_investments 6,180 · undrawn_revolver 0 · cfo 3,983 · short_term_debt 5,196 · capex 2,683 · dividends 0 → **1.40x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 902 | at 2024-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 6,180 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,983 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 5,196 | at 2024-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,683 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| dividends | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

### Liquidity coverage — FY0

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 1,056 · short_term_investments 4,882 · undrawn_revolver 0 · cfo 3,099 · short_term_debt 3,641 · capex 3,779 · dividends 0 → **1.22x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 1,056 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 4,882 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,099 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 3,779 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| dividends | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

### Liquidity coverage — LTM

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 1,228 · short_term_investments 7,163 · undrawn_revolver 0 · cfo 4,267 · short_term_debt 3,580 · capex 4,358 · dividends 0 → **1.59x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 1,228 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 7,163 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,099 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 4,541 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 3,373 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 3,580 | at 2026-09-30 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 3,779 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,728 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| capex | PaymentsToAcquireProductiveAssets | 2 | 2,149 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| dividends | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

## Maturity ladder (FY0, from the latest 10-K)

| Bucket | Tag | Value ($m) | Accession |
|---|---|---|---|
| Debt maturing in the next twelve months | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | 3,641 | 0000006201-26-000014 |
| Debt maturing in year two | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 4,455 | 0000006201-26-000014 |
| Debt maturing in year three | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | 7,324 | 0000006201-26-000014 |
| Debt maturing in year four | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | 4,045 | 0000006201-26-000014 |
| Debt maturing in year five | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | 2,487 | 0000006201-26-000014 |
| Debt maturing after year five | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | 6,642 | 0000006201-26-000014 |
| **Total** | | 28,594 | |

### Debt due within 24 months — FY0

**Formula:** short_term_debt + maturity_year_2  
**Inputs ($m):** short_term_debt 3,641 · maturity_year_2 4,455 → **$8,096m**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 4,455 | at 2025-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |

### Share of debt due within 24 months — FY0

**Formula:** (short_term_debt + maturity_year_2) / total_debt  
**Inputs ($m):** short_term_debt 3,641 · maturity_year_2 4,455 · total_debt 28,895 → **28.0%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 4,455 | at 2025-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 25,254 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |

### Near-term maturity cover — FY0

**Formula:** (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)  
**Inputs ($m):** short_term_debt 3,641 · maturity_year_2 4,455 · cash 1,056 · short_term_investments 4,882 · undrawn_revolver 0 → **1.36x**  
**Flags:** cash: includes restricted cash  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | LongTermDebtCurrent | 2 | 3,641 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 4,455 | at 2025-12-31 (balance sheet) | 10-K | 0000006201-26-000014 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000014/0000006201-26-000014-index.htm) |
| cash | CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents | 2 | 1,056 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 4,882 | at 2025-12-31 (balance sheet) | 10-Q | 0000006201-26-000065 | 2026-10-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/6201/000000620126000065/0000006201-26-000065-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

## Trends (direction from FY-2 to LTM)

| Ratio | FY-2 | FY-1 | FY0 | LTM | Direction |
|---|---|---|---|---|---|
| Debt / EBITDA | 6.14x | 6.30x | 7.88x | 10.21x | worsening |
| Net leverage | 4.70x | 4.83x | 6.26x | 7.31x | worsening |
| EBITDA / interest | 2.49x | 2.49x | 2.14x | 1.74x | worsening |
| FCF / debt | 3.7% | 4.3% | -2.4% | -0.3% | worsening |
| Liquidity coverage | 1.88x | 1.40x | 1.22x | 1.59x | worsening |

## Scorecard

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

### Basis: latest — weighted 5.45, grade SB-5

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | LTM | 10.21 | 6 | 0.20 |  |
| Net debt / EBITDA | LTM | 7.31 | 6 | 0.10 |  |
| EBITDA / interest | LTM | 1.74 | 6 | 0.25 |  |
| FCF / debt | LTM | -0.31 | 6 | 0.20 |  |
| Liquidity sources / uses | LTM | 1.59 | 3 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 1.36 | 5 | 0.10 |  |

### Basis: FY0 — weighted 5.35, grade SB-5

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | FY0 | 7.88 | 6 | 0.20 |  |
| Net debt / EBITDA | FY0 | 6.26 | 6 | 0.10 |  |
| EBITDA / interest | FY0 | 2.14 | 5 | 0.25 |  |
| FCF / debt | FY0 | -2.35 | 6 | 0.20 |  |
| Liquidity sources / uses | FY0 | 1.22 | 4 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 1.36 | 5 | 0.10 |  |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2023-12-31 |
| FY-2 | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 32,771 |
| FY-2 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 32,902 |
| FY-2 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 29,401 |
| FY-2 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2023-12-31 |
| FY-2 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2023-12-31 |
| FY-1 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2024-12-31 |
| FY-1 | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 30,350 |
| FY-1 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 30,476 |
| FY-1 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 25,280 |
| FY-1 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2024-12-31 |
| FY-1 | 6 | DebtLongtermAndShorttermCombinedAmount | 30,118 |
| FY0 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2025-12-31 |
| FY0 | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 28,895 |
| FY0 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 29,007 |
| FY0 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 25,366 |
| FY0 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2025-12-31 |
| FY0 | 6 | DebtLongtermAndShorttermCombinedAmount | 28,594 |
| LTM | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2026-09-30 |
| LTM | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 29,523 |
| LTM | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 29,635 |
| LTM | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 25,395 |
| LTM | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2026-09-30 |
| LTM | 6 | DebtLongtermAndShorttermCombinedAmount | 29,321 |

## Fallback log

### Not available (0)


### Reconciliation (4)

- **total_debt FY-2** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $32,771m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $29,401m (-10.3%). Check which matches the balance sheet.
- **total_debt FY-1** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $30,350m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,280m (-16.7%). Check which matches the balance sheet.
- **total_debt FY0** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $28,895m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,366m (-12.2%). Check which matches the balance sheet.
- **total_debt LTM** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $29,523m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $25,395m (-14.0%). Check which matches the balance sheet.

### Fallbacks beyond rank 1 (28)

- **revenue FY-2**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2023-01-01 to 2023-12-31
- **short_term_debt FY-2**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2023-12-31
- **total_debt FY-2**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2023-12-31
- **cash FY-2**: used rank 2 CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents because rank 1 CashAndCashEquivalentsAtCarryingValue: CashAndCashEquivalentsAtCarryingValue not reported at 2023-12-31
- **short_term_investments FY-2**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2023-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2023-12-31
- **capex FY-2**: used rank 2 PaymentsToAcquireProductiveAssets because rank 1 PaymentsToAcquirePropertyPlantAndEquipment: PaymentsToAcquirePropertyPlantAndEquipment not reported for 2023-01-01 to 2023-12-31
- **revenue FY-1**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2024-01-01 to 2024-12-31
- **interest_expense FY-1**: used rank 2 InterestExpenseNonoperating because rank 1 InterestExpense: InterestExpense not reported for 2024-01-01 to 2024-12-31
- **short_term_debt FY-1**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2024-12-31
- **total_debt FY-1**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2024-12-31
- **cash FY-1**: used rank 2 CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents because rank 1 CashAndCashEquivalentsAtCarryingValue: CashAndCashEquivalentsAtCarryingValue not reported at 2024-12-31
- **short_term_investments FY-1**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2024-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2024-12-31
- **capex FY-1**: used rank 2 PaymentsToAcquireProductiveAssets because rank 1 PaymentsToAcquirePropertyPlantAndEquipment: PaymentsToAcquirePropertyPlantAndEquipment not reported for 2024-01-01 to 2024-12-31
- **revenue FY0**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2025-01-01 to 2025-12-31
- **interest_expense FY0**: used rank 2 InterestExpenseNonoperating because rank 1 InterestExpense: InterestExpense not reported for 2025-01-01 to 2025-12-31
- **short_term_debt FY0**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2025-12-31
- **total_debt FY0**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2025-12-31
- **cash FY0**: used rank 2 CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents because rank 1 CashAndCashEquivalentsAtCarryingValue: CashAndCashEquivalentsAtCarryingValue not reported at 2025-12-31
- **short_term_investments FY0**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2025-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2025-12-31
- **capex FY0**: used rank 2 PaymentsToAcquireProductiveAssets because rank 1 PaymentsToAcquirePropertyPlantAndEquipment: PaymentsToAcquirePropertyPlantAndEquipment not reported for 2025-01-01 to 2025-12-31
- **revenue LTM**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2025-01-01 to 2025-12-31
- **d_and_a LTM**: used rank 2 DepreciationAndAmortization because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2026-01-01 to 2026-09-30
- **interest_expense LTM**: used rank 2 InterestExpenseNonoperating because rank 1 InterestExpense: InterestExpense not reported for 2025-01-01 to 2025-12-31
- **short_term_debt LTM**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2026-09-30
- **total_debt LTM**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2026-09-30
- **cash LTM**: used rank 2 CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents because rank 1 CashAndCashEquivalentsAtCarryingValue: CashAndCashEquivalentsAtCarryingValue not reported at 2026-09-30
- **short_term_investments LTM**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-09-30; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-09-30
- **capex LTM**: used rank 2 PaymentsToAcquireProductiveAssets because rank 1 PaymentsToAcquirePropertyPlantAndEquipment: PaymentsToAcquirePropertyPlantAndEquipment not reported for 2025-01-01 to 2025-12-31

### Assumed zero: not reported (17)

- **short_term_debt FY-2**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt FY-2**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **dividends FY-2**: assumed zero: not reported (rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2023-01-01 to 2023-12-31; rank 2 PaymentsOfDividendsCommonStock: PaymentsOfDividendsCommonStock not reported for 2023-01-01 to 2023-12-31; rank 3 PaymentsOfOrdinaryDividends: PaymentsOfOrdinaryDividends not reported for 2023-01-01 to 2023-12-31)
- **undrawn_revolver FY-2**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2023-12-31)
- **short_term_debt FY-1**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt FY-1**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **dividends FY-1**: assumed zero: not reported (rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2024-01-01 to 2024-12-31; rank 2 PaymentsOfDividendsCommonStock: PaymentsOfDividendsCommonStock not reported for 2024-01-01 to 2024-12-31; rank 3 PaymentsOfOrdinaryDividends: PaymentsOfOrdinaryDividends not reported for 2024-01-01 to 2024-12-31)
- **undrawn_revolver FY-1**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2024-12-31)
- **short_term_debt FY0**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt FY0**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **dividends FY0**: assumed zero: not reported (rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-01-01 to 2025-12-31; rank 2 PaymentsOfDividendsCommonStock: PaymentsOfDividendsCommonStock not reported for 2025-01-01 to 2025-12-31; rank 3 PaymentsOfOrdinaryDividends: PaymentsOfOrdinaryDividends not reported for 2025-01-01 to 2025-12-31)
- **undrawn_revolver FY0**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2025-12-31)
- **short_term_debt LTM**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt LTM**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **dividends LTM**: assumed zero: not reported (rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-01-01 to 2025-12-31; rank 2 PaymentsOfDividendsCommonStock: PaymentsOfDividendsCommonStock not reported for 2025-01-01 to 2025-12-31; rank 3 PaymentsOfOrdinaryDividends: PaymentsOfOrdinaryDividends not reported for 2025-01-01 to 2025-12-31)
- **undrawn_revolver LTM**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-09-30)
- **short_term_borrowings FY0**: assumed zero: not reported (rank 1 ShortTermBorrowings: ShortTermBorrowings not reported at 2025-12-31; rank 2 CommercialPaper: CommercialPaper not reported at 2025-12-31)

### Restated values (most recently filed value used) (0)


### Different candidates across periods (2)

- **d_and_a all**: different candidates across periods (FY-2: rank 1 DepreciationDepletionAndAmortization; FY-1: rank 1 DepreciationDepletionAndAmortization; FY0: rank 1 DepreciationDepletionAndAmortization; LTM: rank 2 DepreciationAndAmortization)
- **interest_expense all**: different candidates across periods (FY-2: rank 1 InterestExpense; FY-1: rank 2 InterestExpenseNonoperating; FY0: rank 2 InterestExpenseNonoperating; LTM: rank 2 InterestExpenseNonoperating)

### Possible structural change (0)


### Stale data (0)
