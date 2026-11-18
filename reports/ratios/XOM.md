# XOM: EXXON MOBIL CORP

Check report. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 34088
- Company facts downloaded from EDGAR: 2026-11-18T03:15:14+00:00; report generated 2026-11-18 03:19 UTC
- Latest 10-K: 10-K for the period ended 2025-12-31, filed 2026-02-18, accession 0000034088-26-000045 ([EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm))
- Latest 10-Q: 10-Q for the period ended 2026-03-31, filed 2026-05-04, accession 0000034088-26-000067 ([EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm))

## Periods

| Period | Flow items (income statement, cash flow) | Balance-sheet date |
|---|---|---|
| FY-2 | 2023-01-01 to 2023-12-31 | 2023-12-31 |
| FY-1 | 2024-01-01 to 2024-12-31 | 2024-12-31 |
| FY0 | 2025-01-01 to 2025-12-31 | 2025-12-31 |
| LTM | + FY0 (2025-01-01 to 2025-12-31) + current year-to-date (2026-01-01 to 2026-03-31) − prior-year year-to-date (2025-01-01 to 2025-03-31) | 2026-03-31 |

- LTM: LTM to 2026-03-31 = FY0 + (2026-01-01 to 2026-03-31) - (2025-01-01 to 2025-03-31), from 10-Q 0000034088-26-000067

## Summary

| Metric | FY-2 | FY-1 | FY0 | LTM |
|---|---|---|---|---|
| EBITDA | $74,273m | $73,311m | $67,864m | $64,390m |
| Debt / EBITDA | 0.56x | 0.57x | 0.64x | 0.74x |
| Net leverage | 0.14x | 0.25x | 0.48x | 0.61x |
| EBITDA / interest | 87.48x | 73.61x | 112.54x | 92.91x |
| FCF / debt | 80.5% | 73.6% | 54.2% | 39.4% |
| Liquidity coverage | 2.12x | 1.70x | 1.14x | 0.93x |

## Warnings (3)

- **filings LTM**: the newest 10-Q, 0000034088-26-000093 (period ended 2026-06-30, filed 2026-08-03), has no facts in this company's XBRL data; using 0000034088-26-000067 (period ended 2026-03-31) instead
- **maturity_after_year_5 FY0**: not available: rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive not reported at 2025-12-31
- **total_debt FY0**: total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $43,537m, but rank 3 LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings = $40,475m (-7.0%). Check which matches the balance sheet.

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 41,573 · operating_income 53,632 · d_and_a 20,641 → **0.56x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 37,483 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| total_debt | DebtCurrent | 1 | 4,090 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 52,783 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 849 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 20,641 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 41,710 · operating_income 49,869 · d_and_a 23,442 → **0.57x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 36,755 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | DebtCurrent | 1 | 4,955 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 48,873 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 996 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 23,442 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 43,537 · operating_income 41,871 · d_and_a 25,993 → **0.64x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 34,241 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 41,268 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 25,993 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 47,661 · operating_income 37,328 · d_and_a 27,062 → **0.74x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 33,130 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 14,531 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 41,268 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 6,967 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 11,600 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 295 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | InterestExpense | 1 | 205 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 25,993 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 6,771 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 5,702 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 41,573 · cash 31,539 · short_term_investments 0 · operating_income 53,632 · d_and_a 20,641 → **0.14x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 37,483 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| total_debt | DebtCurrent | 1 | 4,090 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 31,539 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 52,783 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 849 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 20,641 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 41,710 · cash 23,029 · short_term_investments 0 · operating_income 49,869 · d_and_a 23,442 → **0.25x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 36,755 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | DebtCurrent | 1 | 4,955 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 23,029 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 48,873 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 996 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 23,442 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 43,537 · cash 10,681 · short_term_investments 0 · operating_income 41,871 · d_and_a 25,993 → **0.48x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 34,241 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,681 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 41,268 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 25,993 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 47,661 · cash 8,435 · short_term_investments 0 · operating_income 37,328 · d_and_a 27,062 → **0.61x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 33,130 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 14,531 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 8,435 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 41,268 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 6,967 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 11,600 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 295 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | InterestExpense | 1 | 205 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 25,993 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 6,771 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 5,702 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

### EBITDA / interest — FY-2

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 53,632 · d_and_a 20,641 · interest_expense 849 → **87.48x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 52,783 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 849 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 20,641 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| interest_expense | InterestExpense | 1 | 849 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 49,869 · d_and_a 23,442 · interest_expense 996 → **73.61x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 48,873 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 996 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 23,442 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| interest_expense | InterestExpense | 1 | 996 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 41,871 · d_and_a 25,993 · interest_expense 603 → **112.54x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 41,268 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 25,993 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| interest_expense | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 37,328 · d_and_a 27,062 · interest_expense 693 → **92.91x**  
**Flags:** operating_income: derived: pre-tax income from continuing operations plus interest expense  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 41,268 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 6,967 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest | 2 | 11,600 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| operating_income | InterestExpense | 1 | 295 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| operating_income | InterestExpense | 1 | 205 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 25,993 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 6,771 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| d_and_a | DepreciationDepletionAndAmortization | 1 | 5,702 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| interest_expense | InterestExpense | 1 | 603 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| interest_expense | InterestExpense | 1 | 295 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| interest_expense | InterestExpense | 1 | 205 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 55,369 · capex 21,919 · total_debt 41,573 → **80.5%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 55,369 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 21,919 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 37,483 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| total_debt | DebtCurrent | 1 | 4,090 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 55,022 · capex 24,306 · total_debt 41,710 → **73.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 55,022 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 24,306 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 36,755 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | DebtCurrent | 1 | 4,955 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 51,970 · capex 28,358 · total_debt 43,537 → **54.2%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 51,970 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 28,358 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 34,241 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 47,722 · capex 28,930 · total_debt 47,661 → **39.4%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 51,970 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 8,705 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 12,953 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 28,358 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 6,470 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 5,898 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 33,130 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 14,531 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

### Liquidity coverage — FY-2

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 31,539 · short_term_investments 0 · undrawn_revolver 0 · cfo 55,369 · short_term_debt 4,090 · capex 21,919 · dividends 14,941 → **2.12x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 31,539 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 55,369 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| short_term_debt | DebtCurrent | 1 | 4,090 | at 2023-12-31 (balance sheet) | 10-K | 0000034088-25-000010 | 2025-02-19 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408825000010/0000034088-25-000010-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 21,919 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 14,941 | 2023-01-01 to 2023-12-31 (FY-2) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Liquidity coverage — FY-1

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 23,029 · short_term_investments 0 · undrawn_revolver 0 · cfo 55,022 · short_term_debt 4,955 · capex 24,306 · dividends 16,704 → **1.70x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 23,029 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 55,022 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| short_term_debt | DebtCurrent | 1 | 4,955 | at 2024-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 24,306 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 16,704 | 2024-01-01 to 2024-12-31 (FY-1) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Liquidity coverage — FY0

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 10,681 · short_term_investments 0 · undrawn_revolver 0 · cfo 51,970 · short_term_debt 9,296 · capex 28,358 · dividends 17,231 → **1.14x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,681 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 51,970 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| short_term_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 28,358 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 17,231 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Liquidity coverage — LTM

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 8,435 · short_term_investments 0 · undrawn_revolver 0 · cfo 47,722 · short_term_debt 14,531 · capex 28,930 · dividends 17,230 → **0.93x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 8,435 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 51,970 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 8,705 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 12,953 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| short_term_debt | DebtCurrent | 1 | 14,531 | at 2026-03-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 28,358 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 6,470 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 5,898 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 17,231 | 2025-01-01 to 2025-12-31 (FY0) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 4,334 | 2026-01-01 to 2026-03-31 (current year-to-date) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 4,335 | 2025-01-01 to 2025-03-31 (prior-year year-to-date, subtracted) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

## Maturity ladder (FY0, from the latest 10-K)

| Bucket | Tag | Value ($m) | Accession |
|---|---|---|---|
| Debt maturing in the next twelve months | LongTermDebtCurrent | 6,200 | 0000034088-26-000045 |
| Debt maturing in year two | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 2,500 | 0000034088-26-000045 |
| Debt maturing in year three | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | 1,700 | 0000034088-26-000045 |
| Debt maturing in year four | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | 1,700 | 0000034088-26-000045 |
| Debt maturing in year five | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | 5,300 | 0000034088-26-000045 |
| Debt maturing after year five | — | not available | — |
| **Total** | | not available | |

### Debt due within 24 months — FY0

**Formula:** short_term_debt + maturity_year_2  
**Inputs ($m):** short_term_debt 9,296 · maturity_year_2 2,500 → **$11,796m**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 2,500 | at 2025-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |

### Share of debt due within 24 months — FY0

**Formula:** (short_term_debt + maturity_year_2) / total_debt  
**Inputs ($m):** short_term_debt 9,296 · maturity_year_2 2,500 · total_debt 43,537 → **27.1%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 2,500 | at 2025-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| total_debt | LongTermDebtAndCapitalLeaseObligations | 2 | 34,241 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| total_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |

### Near-term maturity cover — FY0

**Formula:** (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)  
**Inputs ($m):** short_term_debt 9,296 · maturity_year_2 2,500 · cash 10,681 · short_term_investments 0 · undrawn_revolver 0 → **1.10x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 9,296 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 2,500 | at 2025-12-31 (balance sheet) | 10-K | 0000034088-26-000045 | 2026-02-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000045/0000034088-26-000045-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,681 | at 2025-12-31 (balance sheet) | 10-Q | 0000034088-26-000067 | 2026-05-04 | [EDGAR](https://www.sec.gov/Archives/edgar/data/34088/000003408826000067/0000034088-26-000067-index.htm) |
| short_term_investments | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

## Trends (direction from FY-2 to LTM)

| Ratio | FY-2 | FY-1 | FY0 | LTM | Direction |
|---|---|---|---|---|---|
| Debt / EBITDA | 0.56x | 0.57x | 0.64x | 0.74x | worsening |
| Net leverage | 0.14x | 0.25x | 0.48x | 0.61x | worsening |
| EBITDA / interest | 87.48x | 73.61x | 112.54x | 92.91x | stable |
| FCF / debt | 80.5% | 73.6% | 54.2% | 39.4% | worsening |
| Liquidity coverage | 2.12x | 1.70x | 1.14x | 0.93x | worsening |

## Scorecard

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

### Basis: latest — weighted 2.45, grade SB-2

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | LTM | 0.74 | 1 | 0.20 |  |
| Net debt / EBITDA | LTM | 0.61 | 2 | 0.10 |  |
| EBITDA / interest | LTM | 92.91 | 1 | 0.25 |  |
| FCF / debt | LTM | 39.43 | 2 | 0.20 |  |
| Liquidity sources / uses | LTM | 0.93 | 6 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 1.10 | 5 | 0.10 |  |

### Basis: FY0 — weighted 2.00, grade SB-2

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | FY0 | 0.64 | 1 | 0.20 |  |
| Net debt / EBITDA | FY0 | 0.48 | 1 | 0.10 |  |
| EBITDA / interest | FY0 | 112.54 | 1 | 0.25 |  |
| FCF / debt | FY0 | 54.23 | 1 | 0.20 |  |
| Liquidity sources / uses | FY0 | 1.14 | 5 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 1.10 | 5 | 0.10 |  |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2023-12-31 |
| FY-2 | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 41,573 |
| FY-2 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 41,492 |
| FY-2 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2023-12-31 |
| FY-2 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2023-12-31 |
| FY-2 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2023-12-31 |
| FY-1 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2024-12-31 |
| FY-1 | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 41,710 |
| FY-1 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 41,647 |
| FY-1 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2024-12-31 |
| FY-1 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2024-12-31 |
| FY-1 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2024-12-31 |
| FY0 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2025-12-31 |
| FY0 | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 43,537 |
| FY0 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | 40,475 |
| FY0 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2025-12-31 |
| FY0 | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2025-12-31 |
| FY0 | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2025-12-31 |
| LTM | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2026-03-31 |
| LTM | 2 ✔ | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | 47,661 |
| LTM | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligationsCurrent not reported at 2026-03-31 |
| LTM | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2026-03-31 |
| LTM | 5 | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermNotesAndLoans not reported at 2026-03-31 |
| LTM | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2026-03-31 |

## Fallback log

### Not available (1)

- **maturity_after_year_5 FY0** (warning): not available: rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive: LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive not reported at 2025-12-31

### Reconciliation (2)

- **total_debt FY0** (warning): total debt uses rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] = $43,537m, but rank 3 LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings = $40,475m (-7.0%). Check which matches the balance sheet.
- **maturity_ladder FY0**: maturity ladder incomplete (a bucket is not reported), so it cannot be reconciled with total debt

### Fallbacks beyond rank 1 (15)

- **operating_income FY-2**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2023-01-01 to 2023-12-31
- **total_debt FY-2**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2023-12-31
- **dividends FY-2**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2023-01-01 to 2023-12-31
- **operating_income FY-1**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2024-01-01 to 2024-12-31
- **total_debt FY-1**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2024-12-31
- **dividends FY-1**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2024-01-01 to 2024-12-31
- **operating_income FY0**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2025-01-01 to 2025-12-31
- **total_debt FY0**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2025-12-31
- **dividends FY0**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-01-01 to 2025-12-31
- **operating_income LTM**: used rank 2 IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest + [interest_expense] because rank 1 OperatingIncomeLoss: OperatingIncomeLoss not reported for 2025-01-01 to 2025-12-31
- **total_debt LTM**: used rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2026-03-31
- **dividends LTM**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-01-01 to 2025-12-31
- **maturity_year_1 FY0**: used rank 2 LongTermDebtCurrent because rank 1 LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths: LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths not reported at 2025-12-31
- **short_term_borrowings FY0**: used rank 2 CommercialPaper because rank 1 ShortTermBorrowings: ShortTermBorrowings not reported at 2025-12-31
- **finance_lease_liabilities FY0**: used rank 2 FinanceLeaseLiability because rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2025-12-31

### Assumed zero: not reported (8)

- **short_term_investments FY-2**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2023-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2023-12-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2023-12-31)
- **undrawn_revolver FY-2**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2023-12-31)
- **short_term_investments FY-1**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2024-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2024-12-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2024-12-31)
- **undrawn_revolver FY-1**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2024-12-31)
- **short_term_investments FY0**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2025-12-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2025-12-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2025-12-31)
- **undrawn_revolver FY0**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2025-12-31)
- **short_term_investments LTM**: assumed zero: not reported (rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-03-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-03-31; rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent: AvailableForSaleSecuritiesDebtSecuritiesCurrent not reported at 2026-03-31)
- **undrawn_revolver LTM**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-03-31)

### Restated values (most recently filed value used) (0)


### Different candidates across periods (0)


### Possible structural change (0)


### Stale data (1)

- **filings LTM** (warning): the newest 10-Q, 0000034088-26-000093 (period ended 2026-06-30, filed 2026-08-03), has no facts in this company's XBRL data; using 0000034088-26-000067 (period ended 2026-03-31) instead
