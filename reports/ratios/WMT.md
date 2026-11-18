# WMT: Walmart Inc.

Phase-1 ratio check. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 104169
- Company facts downloaded from EDGAR: 2026-11-18T01:51:40+00:00; report generated 2026-11-18 02:25 UTC
- Latest 10-K: 10-K for the period ended 2026-01-31, filed 2026-03-13, accession 0000104169-26-000055 ([EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm))
- Latest 10-Q: 10-Q for the period ended 2026-07-31, filed 2026-08-28, accession 0000104169-26-000154 ([EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm))

## Periods

| Period | Flow items (income statement, cash flow) | Balance-sheet date |
|---|---|---|
| FY-2 | 2023-02-01 to 2024-01-31 | 2024-01-31 |
| FY-1 | 2024-02-01 to 2025-01-31 | 2025-01-31 |
| FY0 | 2025-02-01 to 2026-01-31 | 2026-01-31 |
| LTM | + FY0 (2025-02-01 to 2026-01-31) + current year-to-date (2026-02-01 to 2026-07-31) − prior-year year-to-date (2025-02-01 to 2025-07-31) | 2026-07-31 |

- LTM: LTM to 2026-07-31 = FY0 + (2026-02-01 to 2026-07-31) - (2025-02-01 to 2025-07-31), from 10-Q 0000104169-26-000154

## Summary

| Metric | FY-2 | FY-1 | FY0 | LTM |
|---|---|---|---|---|
| EBITDA | $38,865m | $42,321m | $44,028m | $47,373m |
| Debt / EBITDA | 1.21x | 1.08x | 1.17x | 1.21x |
| Net leverage | 0.95x | 0.87x | 0.93x | 0.96x |
| EBITDA / interest | 15.03x | 16.09x | 16.30x | 20.99x |
| FCF / debt | 32.2% | 27.6% | 29.0% | 23.6% |

## Warnings (4)

- **total_debt FY-2**: total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $46,891m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $39,579m (-15.6%). Check which matches the balance sheet.
- **total_debt FY-1**: total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $45,790m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $35,999m (-21.4%). Check which matches the balance sheet.
- **total_debt FY0**: total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $51,523m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $38,166m (-25.9%). Check which matches the balance sheet.
- **total_debt LTM**: total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $57,243m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $39,932m (-30.2%). Check which matches the balance sheet.

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 46,891 · operating_income 27,012 · d_and_a 11,853 → **1.21x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 36,132 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,447 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 878 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 725 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,709 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 27,012 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 11,853 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 45,790 · operating_income 29,348 · d_and_a 12,973 → **1.08x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 33,401 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,598 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 3,068 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 800 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,923 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 29,348 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 12,973 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 51,523 · operating_income 29,825 · d_and_a 14,203 → **1.17x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 34,624 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,542 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 6,596 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 856 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,905 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 57,243 · operating_income 32,280 · d_and_a 15,093 → **1.21x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 36,462 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,470 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 10,479 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 880 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,952 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 16,876 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | −14,421 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 7,746 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | −6,856 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 46,891 · cash 9,867 · short_term_investments 0 · operating_income 27,012 · d_and_a 11,853 → **0.95x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 36,132 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,447 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 878 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 725 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,709 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 9,867 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 27,012 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 11,853 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 45,790 · cash 9,037 · short_term_investments 0 · operating_income 29,348 · d_and_a 12,973 → **0.87x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 33,401 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,598 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 3,068 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 800 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,923 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 9,037 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 29,348 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 12,973 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 51,523 · cash 10,727 · short_term_investments 0 · operating_income 29,825 · d_and_a 14,203 → **0.93x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 34,624 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,542 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 6,596 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 856 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,905 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,727 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 57,243 · cash 11,529 · short_term_investments 0 · operating_income 32,280 · d_and_a 15,093 → **0.96x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 36,462 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,470 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 10,479 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 880 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,952 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 11,529 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 16,876 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | −14,421 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 7,746 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | −6,856 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

### EBITDA / interest — FY-2

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 27,012 · d_and_a 11,853 · interest_expense 2,585 → **15.03x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 27,012 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 11,853 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,259 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | FinanceLeaseInterestExpense | 3 | 326 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 29,348 · d_and_a 12,973 · interest_expense 2,630 → **16.09x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 29,348 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 12,973 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,249 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | FinanceLeaseInterestExpense | 3 | 381 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 29,825 · d_and_a 14,203 · interest_expense 2,701 → **16.30x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,318 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | FinanceLeaseInterestExpense | 3 | 383 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 32,280 · d_and_a 15,093 · interest_expense 2,257 → **20.99x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 16,876 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | −14,421 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 7,746 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | −6,856 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,318 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 711 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | −1,170 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| interest_expense | FinanceLeaseInterestExpense | 3 | 383 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | FinanceLeaseInterestExpense | 3 | 251 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| interest_expense | FinanceLeaseInterestExpense | 3 | −236 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 35,726 · capex 20,606 · total_debt 46,891 → **32.2%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 35,726 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 20,606 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 36,132 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,447 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 878 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 725 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,709 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 36,443 · capex 23,783 · total_debt 45,790 → **27.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 36,443 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 23,783 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 33,401 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,598 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 3,068 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 800 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,923 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 41,565 · capex 26,642 · total_debt 51,523 → **29.0%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 41,565 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 26,642 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 34,624 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,542 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 6,596 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 856 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,905 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 42,923 · capex 29,414 · total_debt 57,243 → **23.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 41,565 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 19,710 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | −18,352 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 26,642 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 14,181 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | −11,409 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 36,462 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 3,470 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | ShortTermBorrowings | 2 | 10,479 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 880 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 5,952 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 46,891 |
| FY-2 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-01-31 |
| FY-2 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-01-31 |
| FY-2 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 46,891 |
| FY-2 | 5 | DebtLongtermAndShorttermCombinedAmount | 39,579 |
| FY-1 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 45,790 |
| FY-1 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-01-31 |
| FY-1 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-01-31 |
| FY-1 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 45,790 |
| FY-1 | 5 | DebtLongtermAndShorttermCombinedAmount | 35,999 |
| FY0 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 51,523 |
| FY0 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-01-31 |
| FY0 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-01-31 |
| FY0 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 51,523 |
| FY0 | 5 | DebtLongtermAndShorttermCombinedAmount | 38,166 |
| LTM | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 57,243 |
| LTM | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-07-31 |
| LTM | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-07-31 |
| LTM | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2026-07-31 |
| LTM | 5 | DebtLongtermAndShorttermCombinedAmount | 39,932 |

## Fallback log

### Not available (0)


### Reconciliation (7)

- **total_debt FY-2** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $46,891m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $39,579m (-15.6%). Check which matches the balance sheet.
- **total_debt FY-2**: LongTermDebt $39,579m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $3,447m, LongTermDebtNoncurrent $36,132m
- **total_debt FY-1** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $45,790m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $35,999m (-21.4%). Check which matches the balance sheet.
- **total_debt FY-1**: LongTermDebt $35,999m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $2,598m, LongTermDebtNoncurrent $33,401m
- **total_debt FY0** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $51,523m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $38,166m (-25.9%). Check which matches the balance sheet.
- **total_debt FY0**: LongTermDebt $38,166m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $3,542m, LongTermDebtNoncurrent $34,624m
- **total_debt LTM** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $57,243m, but rank 5 DebtLongtermAndShorttermCombinedAmount = $39,932m (-30.2%). Check which matches the balance sheet.

### Fallbacks beyond rank 1 (12)

- **d_and_a FY-2**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2023-02-01 to 2024-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2023-02-01 to 2024-01-31
- **interest_expense FY-2**: used rank 3 InterestExpenseDebt + FinanceLeaseInterestExpense because rank 1 InterestExpense: InterestExpense not reported for 2023-02-01 to 2024-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2023-02-01 to 2024-01-31
- **short_term_debt FY-2**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2024-01-31
- **d_and_a FY-1**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2024-02-01 to 2025-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2024-02-01 to 2025-01-31
- **interest_expense FY-1**: used rank 3 InterestExpenseDebt + FinanceLeaseInterestExpense because rank 1 InterestExpense: InterestExpense not reported for 2024-02-01 to 2025-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2024-02-01 to 2025-01-31
- **short_term_debt FY-1**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2025-01-31
- **d_and_a FY0**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-02-01 to 2026-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-02-01 to 2026-01-31
- **interest_expense FY0**: used rank 3 InterestExpenseDebt + FinanceLeaseInterestExpense because rank 1 InterestExpense: InterestExpense not reported for 2025-02-01 to 2026-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2025-02-01 to 2026-01-31
- **short_term_debt FY0**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2026-01-31
- **d_and_a LTM**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-02-01 to 2026-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-02-01 to 2026-01-31
- **interest_expense LTM**: used rank 3 InterestExpenseDebt + FinanceLeaseInterestExpense because rank 1 InterestExpense: InterestExpense not reported for 2025-02-01 to 2026-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2025-02-01 to 2026-01-31
- **short_term_debt LTM**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2026-07-31

### Assumed zero: not reported (8)

- **short_term_debt FY-2**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_investments FY-2**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2024-01-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2024-01-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2024-01-31)
- **short_term_debt FY-1**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_investments FY-1**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2025-01-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2025-01-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2025-01-31)
- **short_term_debt FY0**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_investments FY0**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-01-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-01-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2026-01-31)
- **short_term_debt LTM**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_investments LTM**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-07-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-07-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2026-07-31)

### Restated values (most recently filed value used) (0)


### Different candidates across periods (0)
