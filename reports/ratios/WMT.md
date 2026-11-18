# WMT: Walmart Inc.

Phase-1 ratio check. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 104169
- Company facts downloaded from EDGAR: 2026-11-18T01:51:40+00:00; report generated 2026-11-18 02:06 UTC
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
| Debt / EBITDA | 1.02x | 0.85x | 0.87x | 0.84x |
| Net leverage | 0.76x | 0.64x | 0.62x | 0.60x |
| EBITDA / interest | 17.20x | 18.82x | 18.99x | 25.48x |
| FCF / debt | 38.2% | 35.2% | 39.1% | 33.8% |

## Warnings (5)

- **total_debt FY-1**: total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $35,999m, but rank 2 LongTermDebtNoncurrent + [short_term_debt] = $39,067m (+8.5%). Check which matches the balance sheet.
- **total_debt FY-1**: total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $35,999m, but rank 3 LongTermDebt + ShortTermBorrowings = $39,067m (+8.5%). Check which matches the balance sheet.
- **total_debt FY0**: total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $38,166m, but rank 2 LongTermDebtNoncurrent + [short_term_debt] = $44,762m (+17.3%). Check which matches the balance sheet.
- **total_debt FY0**: total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $38,166m, but rank 3 LongTermDebt + ShortTermBorrowings = $44,762m (+17.3%). Check which matches the balance sheet.
- **total_debt LTM**: total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $39,932m, but rank 2 LongTermDebtNoncurrent + [short_term_debt] = $50,411m (+26.2%). Check which matches the balance sheet.

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 39,579 · operating_income 27,012 · d_and_a 11,853 → **1.02x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 39,579 | at 2024-01-31 (balance sheet) | 10-Q | 0000104169-24-000178 | 2024-12-06 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416924000178/0000104169-24-000178-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 27,012 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 11,853 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 35,999 · operating_income 29,348 · d_and_a 12,973 → **0.85x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 35,999 | at 2025-01-31 (balance sheet) | 10-Q | 0000104169-25-000191 | 2025-12-03 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000191/0000104169-25-000191-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 29,348 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 12,973 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 38,166 · operating_income 29,825 · d_and_a 14,203 → **0.87x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 38,166 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 39,932 · operating_income 32,280 · d_and_a 15,093 → **0.84x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 39,932 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 16,876 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | −14,421 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 7,746 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | −6,856 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 39,579 · cash 9,867 · short_term_investments 0 · operating_income 27,012 · d_and_a 11,853 → **0.76x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 39,579 | at 2024-01-31 (balance sheet) | 10-Q | 0000104169-24-000178 | 2024-12-06 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416924000178/0000104169-24-000178-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 9,867 | at 2024-01-31 (balance sheet) | 10-K | 0000104169-25-000021 | 2025-03-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000021/0000104169-25-000021-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 27,012 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 11,853 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 35,999 · cash 9,037 · short_term_investments 0 · operating_income 29,348 · d_and_a 12,973 → **0.64x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 35,999 | at 2025-01-31 (balance sheet) | 10-Q | 0000104169-25-000191 | 2025-12-03 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000191/0000104169-25-000191-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 9,037 | at 2025-01-31 (balance sheet) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 29,348 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 12,973 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 38,166 · cash 10,727 · short_term_investments 0 · operating_income 29,825 · d_and_a 14,203 → **0.62x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 38,166 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,727 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 39,932 · cash 11,529 · short_term_investments 0 · operating_income 32,280 · d_and_a 15,093 → **0.60x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 39,932 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
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
**Inputs ($m):** operating_income 27,012 · d_and_a 11,853 · interest_expense 2,259 → **17.20x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 27,012 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 11,853 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,259 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 29,348 · d_and_a 12,973 · interest_expense 2,249 → **18.82x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 29,348 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 12,973 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,249 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 29,825 · d_and_a 14,203 · interest_expense 2,318 → **18.99x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 29,825 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| d_and_a | DepreciationAmortizationAndAccretionNet | 3 | 14,203 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| interest_expense | InterestExpenseDebt | 3 | 2,318 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 32,280 · d_and_a 15,093 · interest_expense 1,859 → **25.48x**  

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

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 35,726 · capex 20,606 · total_debt 39,579 → **38.2%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 35,726 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 20,606 | 2023-02-01 to 2024-01-31 (FY-2) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 39,579 | at 2024-01-31 (balance sheet) | 10-Q | 0000104169-24-000178 | 2024-12-06 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416924000178/0000104169-24-000178-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 36,443 · capex 23,783 · total_debt 35,999 → **35.2%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 36,443 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 23,783 | 2024-02-01 to 2025-01-31 (FY-1) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 35,999 | at 2025-01-31 (balance sheet) | 10-Q | 0000104169-25-000191 | 2025-12-03 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416925000191/0000104169-25-000191-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 41,565 · capex 26,642 · total_debt 38,166 → **39.1%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 41,565 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 26,642 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 38,166 | at 2026-01-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 42,923 · capex 29,414 · total_debt 39,932 → **33.8%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 41,565 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 19,710 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | −18,352 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 26,642 | 2025-02-01 to 2026-01-31 (FY0) | 10-K | 0000104169-26-000055 | 2026-03-13 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000055/0000104169-26-000055-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 14,181 | 2026-02-01 to 2026-07-31 (current year-to-date) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | −11,409 | 2025-02-01 to 2025-07-31 (prior-year year-to-date, subtracted) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |
| total_debt | DebtLongtermAndShorttermCombinedAmount | 1 | 39,932 | at 2026-07-31 (balance sheet) | 10-Q | 0000104169-26-000154 | 2026-08-28 | [EDGAR](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/0000104169-26-000154-index.htm) |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 ✔ | DebtLongtermAndShorttermCombinedAmount | 39,579 |
| FY-2 | 2 | LongTermDebtNoncurrent + [short_term_debt] | 40,457 |
| FY-2 | 3 | LongTermDebt + ShortTermBorrowings | 40,457 |
| FY-2 | 4 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-01-31 |
| FY-1 | 1 ✔ | DebtLongtermAndShorttermCombinedAmount | 35,999 |
| FY-1 | 2 | LongTermDebtNoncurrent + [short_term_debt] | 39,067 |
| FY-1 | 3 | LongTermDebt + ShortTermBorrowings | 39,067 |
| FY-1 | 4 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-01-31 |
| FY0 | 1 ✔ | DebtLongtermAndShorttermCombinedAmount | 38,166 |
| FY0 | 2 | LongTermDebtNoncurrent + [short_term_debt] | 44,762 |
| FY0 | 3 | LongTermDebt + ShortTermBorrowings | 44,762 |
| FY0 | 4 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-01-31 |
| LTM | 1 ✔ | DebtLongtermAndShorttermCombinedAmount | 39,932 |
| LTM | 2 | LongTermDebtNoncurrent + [short_term_debt] | 50,411 |
| LTM | 3 | LongTermDebt + ShortTermBorrowings | not usable: LongTermDebt not reported at 2026-07-31 |
| LTM | 4 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-07-31 |

## Fallback log

### Not available (0)


### Reconciliation (8)

- **total_debt FY-2**: LongTermDebt $39,579m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $3,447m, LongTermDebtNoncurrent $36,132m
- **total_debt FY-1** (warning): total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $35,999m, but rank 2 LongTermDebtNoncurrent + [short_term_debt] = $39,067m (+8.5%). Check which matches the balance sheet.
- **total_debt FY-1** (warning): total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $35,999m, but rank 3 LongTermDebt + ShortTermBorrowings = $39,067m (+8.5%). Check which matches the balance sheet.
- **total_debt FY-1**: LongTermDebt $35,999m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $2,598m, LongTermDebtNoncurrent $33,401m
- **total_debt FY0** (warning): total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $38,166m, but rank 2 LongTermDebtNoncurrent + [short_term_debt] = $44,762m (+17.3%). Check which matches the balance sheet.
- **total_debt FY0** (warning): total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $38,166m, but rank 3 LongTermDebt + ShortTermBorrowings = $44,762m (+17.3%). Check which matches the balance sheet.
- **total_debt FY0**: LongTermDebt $38,166m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $3,542m, LongTermDebtNoncurrent $34,624m
- **total_debt LTM** (warning): total debt uses rank 1 DebtLongtermAndShorttermCombinedAmount = $39,932m, but rank 2 LongTermDebtNoncurrent + [short_term_debt] = $50,411m (+26.2%). Check which matches the balance sheet.

### Fallbacks beyond rank 1 (12)

- **d_and_a FY-2**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2023-02-01 to 2024-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2023-02-01 to 2024-01-31
- **interest_expense FY-2**: used rank 3 InterestExpenseDebt because rank 1 InterestExpense: InterestExpense not reported for 2023-02-01 to 2024-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2023-02-01 to 2024-01-31
- **short_term_debt FY-2**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2024-01-31
- **d_and_a FY-1**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2024-02-01 to 2025-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2024-02-01 to 2025-01-31
- **interest_expense FY-1**: used rank 3 InterestExpenseDebt because rank 1 InterestExpense: InterestExpense not reported for 2024-02-01 to 2025-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2024-02-01 to 2025-01-31
- **short_term_debt FY-1**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2025-01-31
- **d_and_a FY0**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-02-01 to 2026-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-02-01 to 2026-01-31
- **interest_expense FY0**: used rank 3 InterestExpenseDebt because rank 1 InterestExpense: InterestExpense not reported for 2025-02-01 to 2026-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2025-02-01 to 2026-01-31
- **short_term_debt FY0**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2026-01-31
- **d_and_a LTM**: used rank 3 DepreciationAmortizationAndAccretionNet because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-02-01 to 2026-01-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-02-01 to 2026-01-31
- **interest_expense LTM**: used rank 3 InterestExpenseDebt because rank 1 InterestExpense: InterestExpense not reported for 2025-02-01 to 2026-01-31; rank 2 InterestExpenseNonoperating: InterestExpenseNonoperating not reported for 2025-02-01 to 2026-01-31
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
