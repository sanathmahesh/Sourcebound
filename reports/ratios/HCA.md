# HCA: HCA Healthcare, Inc.

Check report. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 860730
- Company facts downloaded from EDGAR: 2026-11-18T02:55:28+00:00; report generated 2026-11-18 03:19 UTC
- Latest 10-K: 10-K for the period ended 2025-12-31, filed 2026-02-10, accession 0001193125-26-044769 ([EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm))
- Latest 10-Q: 10-Q for the period ended 2026-09-30, filed 2026-10-29, accession 0001193125-26-437871 ([EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm))

## Periods

| Period | Flow items (income statement, cash flow) | Balance-sheet date |
|---|---|---|
| FY-2 | 2023-01-01 to 2023-12-31 | 2023-12-31 |
| FY-1 | 2024-01-01 to 2024-12-31 | 2024-12-31 |
| FY0 | 2025-01-01 to 2025-12-31 | 2025-12-31 |
| LTM | + FY0 (2025-01-01 to 2025-12-31) + current year-to-date (2026-01-01 to 2026-09-30) − prior-year year-to-date (2025-01-01 to 2025-09-30) | 2026-09-30 |

- LTM: LTM to 2026-09-30 = FY0 + (2026-01-01 to 2026-09-30) - (2025-01-01 to 2025-09-30), from 10-Q 0001193125-26-437871

## Summary

| Metric | FY-2 | FY-1 | FY0 | LTM |
|---|---|---|---|---|
| EBITDA | $12,721m | $13,896m | $15,603m | $15,924m |
| Debt / EBITDA | 3.17x | 3.15x | 3.03x | 3.17x |
| Net leverage | 3.09x | 3.01x | 2.96x | 3.11x |
| EBITDA / interest | 6.56x | 6.74x | 6.94x | 6.74x |
| FCF / debt | 11.6% | 12.9% | 16.3% | 11.8% |
| Liquidity coverage | 1.32x | 1.21x | 1.30x | 0.86x |

## Warnings (3)

- **maturity_year_1 FY0**: not available: rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths not reported at 2025-12-31; rank 2 LongTermDebtCurrent: LongTermDebtCurrent not reported at 2025-12-31
- **maturity_after_year_5 FY0**: not available: rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive not reported at 2025-12-31
- **total_debt LTM**: total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $50,493m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $44,766m (-11.3%). Check which matches the balance sheet.

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 40,300 · operating_income 9,644 · d_and_a 3,077 → **3.17x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 37,169 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,424 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 166 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 541 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,706 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 1,938 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,077 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 43,817 · operating_income 10,584 · d_and_a 3,312 → **3.15x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 38,333 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | DebtCurrent | 1 | 4,698 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 162 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 624 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 8,523 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 2,061 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,312 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 47,250 · operating_income 12,080 · d_and_a 3,523 → **3.03x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 41,603 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 133 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 625 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 9,832 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,523 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 50,493 · operating_income 12,185 · d_and_a 3,739 → **3.17x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 42,400 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 8,093 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 9,832 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,151 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,160 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 1,790 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | InterestExpense | 1 | 1,676 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,523 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,828 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,612 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 40,300 · cash 935 · short_term_investments 0 · operating_income 9,644 · d_and_a 3,077 → **3.09x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 37,169 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,424 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 166 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 541 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 935 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,706 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 1,938 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,077 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 43,817 · cash 1,933 · short_term_investments 0 · operating_income 10,584 · d_and_a 3,312 → **3.01x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 38,333 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | DebtCurrent | 1 | 4,698 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 162 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 624 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 1,933 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 8,523 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 2,061 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,312 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 47,250 · cash 1,040 · short_term_investments 0 · operating_income 12,080 · d_and_a 3,523 → **2.96x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 41,603 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 133 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 625 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 1,040 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 9,832 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,523 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 50,493 · cash 908 · short_term_investments 0 · operating_income 12,185 · d_and_a 3,739 → **3.11x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtNoncurrent | 1 | 42,400 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 8,093 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 908 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 9,832 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,151 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,160 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 1,790 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | InterestExpense | 1 | 1,676 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,523 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,828 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,612 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |

### EBITDA / interest — FY-2

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 9,644 · d_and_a 3,077 · interest_expense 1,938 → **6.56x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,706 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 1,938 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,077 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| interest_expense | InterestExpense | 1 | 1,938 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 10,584 · d_and_a 3,312 · interest_expense 2,061 → **6.74x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 8,523 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 2,061 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,312 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| interest_expense | InterestExpense | 1 | 2,061 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 12,080 · d_and_a 3,523 · interest_expense 2,248 → **6.94x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 9,832 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,523 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| interest_expense | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 12,185 · d_and_a 3,739 · interest_expense 2,362 → **6.74x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 9,832 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,151 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 7,160 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| operating_income | InterestExpense | 1 | 1,790 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| operating_income | InterestExpense | 1 | 1,676 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 3,523 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,828 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 2,612 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| interest_expense | InterestExpense | 1 | 2,248 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| interest_expense | InterestExpense | 1 | 1,790 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| interest_expense | InterestExpense | 1 | 1,676 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 9,431 · capex 4,744 · total_debt 40,300 → **11.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 9,431 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,744 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 37,169 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | LongTermDebtCurrent | 2 | 2,424 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 166 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 541 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 10,514 · capex 4,875 · total_debt 43,817 → **12.9%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 10,514 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,875 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 38,333 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | DebtCurrent | 1 | 4,698 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 162 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 624 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 12,636 · capex 4,944 · total_debt 47,250 → **16.3%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 12,636 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,944 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 41,603 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 133 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 625 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 11,169 · capex 5,196 · total_debt 50,493 → **11.8%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 12,636 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 8,810 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 10,277 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,944 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 3,707 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 3,455 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 42,400 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 8,093 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |

### Liquidity coverage — FY-2

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 935 · short_term_investments 0 · undrawn_revolver 0 · cfo 9,431 · short_term_debt 2,424 · capex 4,744 · dividends 661 → **1.32x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 935 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 9,431 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| short_term_debt | LongTermDebtCurrent | 2 | 2,424 | at 2023-12-31 (balance sheet) | 10-K | 0000950170-25-020134 | 2025-02-14 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000095017025020134/0000950170-25-020134-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,744 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| dividends | PaymentsOfDividends | 1 | 661 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Liquidity coverage — FY-1

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 1,933 · short_term_investments 0 · undrawn_revolver 0 · cfo 10,514 · short_term_debt 4,698 · capex 4,875 · dividends 690 → **1.21x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 1,933 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 10,514 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| short_term_debt | DebtCurrent | 1 | 4,698 | at 2024-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,875 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| dividends | PaymentsOfDividends | 1 | 690 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Liquidity coverage — FY0

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 1,040 · short_term_investments 0 · undrawn_revolver 0 · cfo 12,636 · short_term_debt 4,889 · capex 4,944 · dividends 679 → **1.30x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 1,040 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 12,636 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| short_term_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,944 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| dividends | PaymentsOfDividends | 1 | 679 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Liquidity coverage — LTM

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 908 · short_term_investments 0 · undrawn_revolver 0 · cfo 11,169 · short_term_debt 8,093 · capex 5,196 · dividends 681 → **0.86x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 908 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 12,636 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 8,810 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 10,277 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| short_term_debt | DebtCurrent | 1 | 8,093 | at 2026-09-30 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 4,944 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 3,707 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 3,455 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| dividends | PaymentsOfDividends | 1 | 679 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| dividends | PaymentsOfDividends | 1 | 519 | 2026-01-01 to 2026-09-30 (current year-to-date) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| dividends | PaymentsOfDividends | 1 | 517 | 2025-01-01 to 2025-09-30 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |

## Maturity ladder (FY0, from the latest 10-K)

| Bucket | Tag | Value ($m) | Accession |
|---|---|---|---|
| Debt maturing in the next twelve months | — | not available | — |
| Debt maturing in year two | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 2,547 | 0001193125-26-044769 |
| Debt maturing in year three | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | 3,645 | 0001193125-26-044769 |
| Debt maturing in year four | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | 3,577 | 0001193125-26-044769 |
| Debt maturing in year five | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | 4,021 | 0001193125-26-044769 |
| Debt maturing after year five | — | not available | — |
| **Total** | | not available | |

### Debt due within 24 months — FY0

**Formula:** short_term_debt + maturity_year_2  
**Inputs ($m):** short_term_debt 4,889 · maturity_year_2 2,547 → **$7,436m**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 2,547 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Share of debt due within 24 months — FY0

**Formula:** (short_term_debt + maturity_year_2) / total_debt  
**Inputs ($m):** short_term_debt 4,889 · maturity_year_2 2,547 · total_debt 47,250 → **15.7%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 2,547 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | LongTermDebtNoncurrent | 1 | 41,603 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 133 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 625 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |

### Near-term maturity cover — FY0

**Formula:** (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)  
**Inputs ($m):** short_term_debt 4,889 · maturity_year_2 2,547 · cash 1,040 · short_term_investments 0 · undrawn_revolver 0 → **7.15x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 4,889 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 2,547 | at 2025-12-31 (balance sheet) | 10-K | 0001193125-26-044769 | 2026-02-10 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526044769/0001193125-26-044769-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 1,040 | at 2025-12-31 (balance sheet) | 10-Q | 0001193125-26-437871 | 2026-10-29 | [EDGAR](https://www.sec.gov/Archives/edgar/data/860730/000119312526437871/0001193125-26-437871-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

## Trends (direction from FY-2 to LTM)

| Ratio | FY-2 | FY-1 | FY0 | LTM | Direction |
|---|---|---|---|---|---|
| Debt / EBITDA | 3.17x | 3.15x | 3.03x | 3.17x | stable |
| Net leverage | 3.09x | 3.01x | 2.96x | 3.11x | stable |
| EBITDA / interest | 6.56x | 6.74x | 6.94x | 6.74x | stable |
| FCF / debt | 11.6% | 12.9% | 16.3% | 11.8% | stable |
| Liquidity coverage | 1.32x | 1.21x | 1.30x | 0.86x | worsening |

## Scorecard

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

### Basis: latest — weighted 4.25, grade SB-4

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | LTM | 3.17 | 4 | 0.20 |  |
| Net debt / EBITDA | LTM | 3.11 | 4 | 0.10 |  |
| EBITDA / interest | LTM | 6.74 | 3 | 0.25 |  |
| FCF / debt | LTM | 11.83 | 4 | 0.20 |  |
| Liquidity sources / uses | LTM | 0.86 | 6 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 7.15 | 6 | 0.10 |  |

### Basis: FY0 — weighted 3.75, grade SB-4

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | FY0 | 3.03 | 4 | 0.20 |  |
| Net debt / EBITDA | FY0 | 2.96 | 4 | 0.10 |  |
| EBITDA / interest | FY0 | 6.94 | 3 | 0.25 |  |
| FCF / debt | FY0 | 16.28 | 3 | 0.20 |  |
| Liquidity sources / uses | FY0 | 1.30 | 4 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 7.15 | 6 | 0.10 |  |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 40,300 |
| FY-2 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2023-12-31 |
| FY-2 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2023-12-31 |
| FY-2 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 40,300 |
| FY-2 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2023-12-31 |
| FY-2 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2023-12-31 |
| FY-1 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 43,817 |
| FY-1 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-12-31 |
| FY-1 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-12-31 |
| FY-1 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 43,817 |
| FY-1 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2024-12-31 |
| FY-1 | 6 | DebtLongtermAndShorttermCombinedAmount | 43,031 |
| FY0 | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 47,250 |
| FY0 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-12-31 |
| FY0 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-12-31 |
| FY0 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 45,043 |
| FY0 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2025-12-31 |
| FY0 | 6 | DebtLongtermAndShorttermCombinedAmount | 46,492 |
| LTM | 1 ✔ | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | 50,493 |
| LTM | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-09-30 |
| LTM | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-09-30 |
| LTM | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | 44,766 |
| LTM | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2026-09-30 |
| LTM | 6 | DebtLongtermAndShorttermCombinedAmount | 50,493 |

## Fallback log

### Not available (2)

- **maturity_year_1 FY0** (warning): not available: rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths not reported at 2025-12-31; rank 2 LongTermDebtCurrent: LongTermDebtCurrent not reported at 2025-12-31
- **maturity_after_year_5 FY0** (warning): not available: rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive not reported at 2025-12-31

### Reconciliation (4)

- **total_debt FY-2**: LongTermDebt $39,593m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $2,424m, LongTermDebtNoncurrent $37,169m
- **total_debt FY-1**: LongTermDebt $43,031m includes the current portion (LongTermDebt = current + noncurrent); LongTermDebtCurrent $4,698m, LongTermDebtNoncurrent $38,333m
- **total_debt LTM** (warning): total debt uses rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] = $50,493m, but rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] = $44,766m (-11.3%). Check which matches the balance sheet.
- **maturity_ladder FY0**: maturity ladder incomplete (a bucket is not reported), so it cannot be reconciled with total debt

### Fallbacks beyond rank 1 (5)

- **operating_income FY-2**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2023-01-01 to 2023-12-31
- **short_term_debt FY-2**: used rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper because rank 1 DebtCurrent: DebtCurrent not reported at 2023-12-31
- **operating_income FY-1**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2024-01-01 to 2024-12-31
- **operating_income FY0**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2025-01-01 to 2025-12-31
- **operating_income LTM**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2025-01-01 to 2025-12-31

### Assumed zero: not reported (12)

- **short_term_debt FY-2**: ShortTermBorrowings assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_debt FY-2**: CommercialPaper assumed zero: not reported (part of rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper)
- **short_term_investments FY-2**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2023-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2023-12-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2023-12-31)
- **undrawn_revolver FY-2**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2023-12-31)
- **short_term_investments FY-1**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2024-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2024-12-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2024-12-31)
- **undrawn_revolver FY-1**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2024-12-31)
- **short_term_investments FY0**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2025-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2025-12-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2025-12-31)
- **undrawn_revolver FY0**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2025-12-31)
- **finance_lease_liabilities LTM**: assumed zero: not reported (rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2026-09-30; rank 2 FinanceLeaseLiability: FinanceLeaseLiability not reported at 2026-09-30)
- **short_term_investments LTM**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-09-30; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-09-30; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2026-09-30)
- **undrawn_revolver LTM**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-09-30)
- **short_term_borrowings FY0**: assumed zero: not reported (rank 1 ShortTermBorrowings: ShortTermBorrowings not reported at 2025-12-31; rank 2 CommercialPaper: CommercialPaper not reported at 2025-12-31)

### Restated values (most recently filed value used) (0)


### Different candidates across periods (1)

- **short_term_debt all**: different candidates across periods (FY-2: rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper; FY-1: rank 1 DebtCurrent; FY0: rank 1 DebtCurrent; LTM: rank 1 DebtCurrent)

### Possible structural change (0)


### Stale data (0)
