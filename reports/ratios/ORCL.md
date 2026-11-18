# ORCL: ORACLE CORP

Check report. Every ratio is followed by the XBRL facts it used. Values in US$ millions.

- CIK: 1341439
- Company facts downloaded from EDGAR: 2026-11-18T02:56:16+00:00; report generated 2026-11-18 03:19 UTC
- Latest 10-K: 10-K for the period ended 2026-05-31, filed 2026-06-22, accession 0001193125-26-277521 ([EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm))
- Latest 10-Q: 10-Q for the period ended 2026-08-31, filed 2026-09-11, accession 0001193125-26-389274 ([EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm))

## Periods

| Period | Flow items (income statement, cash flow) | Balance-sheet date |
|---|---|---|
| FY-2 | 2023-06-01 to 2024-05-31 | 2024-05-31 |
| FY-1 | 2024-06-01 to 2025-05-31 | 2025-05-31 |
| FY0 | 2025-06-01 to 2026-05-31 | 2026-05-31 |
| LTM | + FY0 (2025-06-01 to 2026-05-31) + current year-to-date (2026-06-01 to 2026-08-31) − prior-year year-to-date (2025-06-01 to 2025-08-31) | 2026-08-31 |

- LTM: LTM to 2026-08-31 = FY0 + (2026-06-01 to 2026-08-31) - (2025-06-01 to 2025-08-31), from 10-Q 0001193125-26-389274

## Summary

| Metric | FY-2 | FY-1 | FY0 | LTM |
|---|---|---|---|---|
| EBITDA | $21,492m | $23,852m | $29,900m | $33,938m |
| Debt / EBITDA | 4.04x | 4.00x | 4.59x | 3.96x |
| Net leverage | 3.55x | 3.53x | 3.52x | 2.87x |
| EBITDA / interest | 6.12x | 6.67x | 6.50x | 6.65x |
| FCF / debt | 13.6% | -0.4% | -17.3% | -21.3% |
| Liquidity coverage | 1.34x | 0.96x | 0.93x | 0.94x |

## Warnings (1)

- **total_debt FY0**: total debt uses rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] = $137,242m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $129,541m (-5.6%). Check which matches the balance sheet.

## Ratios with their source facts

### Debt / EBITDA — FY-2

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 86,869 · operating_income 15,353 · d_and_a 6,139 → **4.04x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 76,264 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| total_debt | DebtCurrent | 1 | 10,605 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 0 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 15,353 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,129 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 3,010 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Debt / EBITDA — FY-1

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 95,502 · operating_income 17,678 · d_and_a 6,174 → **4.00x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 85,297 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | DebtCurrent | 1 | 7,271 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 257 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 2,677 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 17,678 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,867 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 2,307 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Debt / EBITDA — FY0

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 137,242 · operating_income 20,606 · d_and_a 9,294 → **4.59x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 122,342 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 620 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 7,081 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 20,606 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 7,623 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,671 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Debt / EBITDA — LTM

**Formula:** total_debt / EBITDA  
**Inputs ($m):** total_debt 134,522 · operating_income 23,057 · d_and_a 10,881 → **3.96x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 117,712 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | NotesPayableCurrent | 4 | 7,625 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 749 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 8,436 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 20,606 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 6,728 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 4,277 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | Depreciation | 4 | 7,623 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,156 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | Depreciation | 4 | 1,351 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,671 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 202 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 420 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

### Net leverage — FY-2

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 86,869 · cash 10,454 · short_term_investments 207 · operating_income 15,353 · d_and_a 6,139 → **3.55x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 76,264 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| total_debt | DebtCurrent | 1 | 10,605 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 0 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,454 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 207 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 15,353 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,129 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 3,010 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Net leverage — FY-1

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 95,502 · cash 10,786 · short_term_investments 417 · operating_income 17,678 · d_and_a 6,174 → **3.53x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 85,297 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | DebtCurrent | 1 | 7,271 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 257 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 2,677 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,786 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 417 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 17,678 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,867 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 2,307 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Net leverage — FY0

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 137,242 · cash 31,289 · short_term_investments 605 · operating_income 20,606 · d_and_a 9,294 → **3.52x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 122,342 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 620 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 7,081 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 31,289 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 605 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 20,606 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 7,623 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,671 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Net leverage — LTM

**Formula:** (total_debt - cash - short_term_investments) / EBITDA  
**Inputs ($m):** total_debt 134,522 · cash 36,369 · short_term_investments 708 · operating_income 23,057 · d_and_a 10,881 → **2.87x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| total_debt | LongTermNotesAndLoans | 5 | 117,712 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | NotesPayableCurrent | 4 | 7,625 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 749 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 8,436 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 36,369 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 708 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 20,606 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 6,728 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 4,277 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | Depreciation | 4 | 7,623 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,156 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | Depreciation | 4 | 1,351 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,671 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 202 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 420 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

### EBITDA / interest — FY-2

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 15,353 · d_and_a 6,139 · interest_expense 3,514 → **6.12x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 15,353 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,129 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 3,010 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| interest_expense | InterestExpense | 1 | 3,514 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### EBITDA / interest — FY-1

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 17,678 · d_and_a 6,174 · interest_expense 3,578 → **6.67x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 17,678 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,867 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 2,307 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| interest_expense | InterestExpense | 1 | 3,578 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### EBITDA / interest — FY0

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 20,606 · d_and_a 9,294 · interest_expense 4,599 → **6.50x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 20,606 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 7,623 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,671 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| interest_expense | InterestExpense | 1 | 4,599 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### EBITDA / interest — LTM

**Formula:** EBITDA / interest_expense  
**Inputs ($m):** operating_income 23,057 · d_and_a 10,881 · interest_expense 5,104 → **6.65x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| operating_income | OperatingIncomeLoss | 1 | 20,606 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 6,728 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| operating_income | OperatingIncomeLoss | 1 | 4,277 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | Depreciation | 4 | 7,623 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | Depreciation | 4 | 3,156 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | Depreciation | 4 | 1,351 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 1,671 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 202 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| d_and_a | AmortizationOfIntangibleAssets | 4 | 420 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| interest_expense | InterestExpense | 1 | 4,599 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| interest_expense | InterestExpense | 1 | 1,428 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| interest_expense | InterestExpense | 1 | 923 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

### FCF / debt — FY-2

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 18,673 · capex 6,866 · total_debt 86,869 → **13.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 18,673 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 6,866 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | LongTermNotesAndLoans | 5 | 76,264 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| total_debt | DebtCurrent | 1 | 10,605 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| total_debt | FinanceLeaseLiability | 2 | 0 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |

### FCF / debt — FY-1

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 20,821 · capex 21,215 · total_debt 95,502 → **-0.4%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 20,821 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 21,215 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | LongTermNotesAndLoans | 5 | 85,297 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | DebtCurrent | 1 | 7,271 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 257 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 2,677 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### FCF / debt — FY0

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 31,977 · capex 55,663 · total_debt 137,242 → **-17.3%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 31,977 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 55,663 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | LongTermNotesAndLoans | 5 | 122,342 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 620 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 7,081 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

### FCF / debt — LTM

**Formula:** (cfo - capex) / total_debt  
**Inputs ($m):** cfo 46,940 · capex 75,660 · total_debt 134,522 → **-21.3%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 31,977 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 23,103 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 8,140 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 55,663 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 28,499 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 8,502 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | LongTermNotesAndLoans | 5 | 117,712 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | NotesPayableCurrent | 4 | 7,625 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 749 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 8,436 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

### Liquidity coverage — FY-2

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 10,454 · short_term_investments 207 · undrawn_revolver 0 · cfo 18,673 · short_term_debt 10,605 · capex 6,866 · dividends 4,391 → **1.34x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,454 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 207 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 18,673 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| short_term_debt | DebtCurrent | 1 | 10,605 | at 2024-05-31 (balance sheet) | 10-K | 0000950170-25-087926 | 2025-06-18 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000095017025087926/0000950170-25-087926-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 6,866 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 4,391 | 2023-06-01 to 2024-05-31 (FY-2) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Liquidity coverage — FY-1

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 10,786 · short_term_investments 417 · undrawn_revolver 0 · cfo 20,821 · short_term_debt 7,271 · capex 21,215 · dividends 4,743 → **0.96x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 10,786 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 417 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 20,821 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| short_term_debt | DebtCurrent | 1 | 7,271 | at 2025-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 21,215 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 4,743 | 2024-06-01 to 2025-05-31 (FY-1) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Liquidity coverage — FY0

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 31,289 · short_term_investments 605 · undrawn_revolver 0 · cfo 31,977 · short_term_debt 7,199 · capex 55,663 · dividends 5,787 → **0.93x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 31,289 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 605 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 31,977 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| short_term_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 55,663 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 5,787 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Liquidity coverage — LTM

**Formula:** (cash + short_term_investments + undrawn_revolver + max(cfo, 0)) / (short_term_debt + capex + dividends)  
**Inputs ($m):** cash 36,369 · short_term_investments 708 · undrawn_revolver 0 · cfo 46,940 · short_term_debt 7,625 · capex 75,660 · dividends 5,939 → **0.94x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 36,369 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 708 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 31,977 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 23,103 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| cfo | NetCashProvidedByUsedInOperatingActivities | 1 | 8,140 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| short_term_debt | NotesPayableCurrent | 4 | 7,625 | at 2026-08-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 55,663 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 28,499 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| capex | PaymentsToAcquirePropertyPlantAndEquipment | 1 | 8,502 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 5,787 | 2025-06-01 to 2026-05-31 (FY0) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 1,565 | 2026-06-01 to 2026-08-31 (current year-to-date) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| dividends | PaymentsOfDividendsCommonStock | 2 | 1,413 | 2025-06-01 to 2025-08-31 (prior-year year-to-date, subtracted) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

## Maturity ladder (FY0, from the latest 10-K)

| Bucket | Tag | Value ($m) | Accession |
|---|---|---|---|
| Debt maturing in the next twelve months | LongTermDebtMaturitiesRepaymentsOfPrincipalInNextTwelveMonths | 7,210 | 0001193125-26-277521 |
| Debt maturing in year two | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 10,145 | 0001193125-26-277521 |
| Debt maturing in year three | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearThree | 5,500 | 0001193125-26-277521 |
| Debt maturing in year four | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFour | 7,250 | 0001193125-26-277521 |
| Debt maturing in year five | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearFive | 9,750 | 0001193125-26-277521 |
| Debt maturing after year five | LongTermDebtMaturitiesRepaymentsOfPrincipalAfterYearFive | 90,250 | 0001193125-26-277521 |
| **Total** | | 130,105 | |

### Debt due within 24 months — FY0

**Formula:** short_term_debt + maturity_year_2  
**Inputs ($m):** short_term_debt 7,199 · maturity_year_2 10,145 → **$17,344m**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 10,145 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |

### Share of debt due within 24 months — FY0

**Formula:** (short_term_debt + maturity_year_2) / total_debt  
**Inputs ($m):** short_term_debt 7,199 · maturity_year_2 10,145 · total_debt 137,242 → **12.6%**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 10,145 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | LongTermNotesAndLoans | 5 | 122,342 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| total_debt | FinanceLeaseLiabilityCurrent | 1 | 620 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| total_debt | FinanceLeaseLiabilityNoncurrent | 1 | 7,081 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |

### Near-term maturity cover — FY0

**Formula:** (short_term_debt + maturity_year_2) / (cash + short_term_investments + undrawn_revolver)  
**Inputs ($m):** short_term_debt 7,199 · maturity_year_2 10,145 · cash 31,289 · short_term_investments 605 · undrawn_revolver 0 → **0.54x**  

| Concept | Tag | Rank | Value ($m) | Period | Form | Accession | Filed | Link |
|---|---|---|---|---|---|---|---|---|
| short_term_debt | DebtCurrent | 1 | 7,199 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| maturity_year_2 | LongTermDebtMaturitiesRepaymentsOfPrincipalInYearTwo | 1 | 10,145 | at 2026-05-31 (balance sheet) | 10-K | 0001193125-26-277521 | 2026-06-22 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/0001193125-26-277521-index.htm) |
| cash | CashAndCashEquivalentsAtCarryingValue | 1 | 31,289 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| short_term_investments | AvailableForSaleSecuritiesDebtSecuritiesCurrent | 3 | 605 | at 2026-05-31 (balance sheet) | 10-Q | 0001193125-26-389274 | 2026-09-11 | [EDGAR](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/0001193125-26-389274-index.htm) |
| undrawn_revolver | — | — | 0 (assumed zero: not reported) | — | — | — | — | — |

## Trends (direction from FY-2 to LTM)

| Ratio | FY-2 | FY-1 | FY0 | LTM | Direction |
|---|---|---|---|---|---|
| Debt / EBITDA | 4.04x | 4.00x | 4.59x | 3.96x | stable |
| Net leverage | 3.55x | 3.53x | 3.52x | 2.87x | improving |
| EBITDA / interest | 6.12x | 6.67x | 6.50x | 6.65x | stable |
| FCF / debt | 13.6% | -0.4% | -17.3% | -21.3% | worsening |
| Liquidity coverage | 1.34x | 0.96x | 0.93x | 0.94x | worsening |

## Scorecard

**Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.**

### Basis: latest — weighted 4.35, grade SB-4

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | LTM | 3.96 | 4 | 0.20 |  |
| Net debt / EBITDA | LTM | 2.87 | 4 | 0.10 |  |
| EBITDA / interest | LTM | 6.65 | 3 | 0.25 |  |
| FCF / debt | LTM | -21.35 | 6 | 0.20 |  |
| Liquidity sources / uses | LTM | 0.94 | 6 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 0.54 | 3 | 0.10 |  |

### Basis: FY0 — weighted 4.55, grade SB-5

| Factor | Period | Value | Band | Weight | Note |
|---|---|---|---|---|---|
| Debt / EBITDA | FY0 | 4.59 | 5 | 0.20 |  |
| Net debt / EBITDA | FY0 | 3.52 | 4 | 0.10 |  |
| EBITDA / interest | FY0 | 6.50 | 3 | 0.25 |  |
| FCF / debt | FY0 | -17.26 | 6 | 0.20 |  |
| Liquidity sources / uses | FY0 | 0.93 | 6 | 0.15 |  |
| Debt due in 24 months / (cash + undrawn revolver) | FY0 | 0.54 | 3 | 0.10 |  |

## Debt reconciliation

Every total-debt candidate the company reports, for comparison with the one used (✔).

| Period | Rank | Candidate | Value ($m) |
|---|---|---|---|
| FY-2 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2024-05-31 |
| FY-2 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-05-31 |
| FY-2 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2024-05-31 |
| FY-2 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2024-05-31 |
| FY-2 | 5 ✔ | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | 86,869 |
| FY-2 | 6 | DebtLongtermAndShorttermCombinedAmount | 86,869 |
| FY-1 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2025-05-31 |
| FY-1 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-05-31 |
| FY-1 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2025-05-31 |
| FY-1 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2025-05-31 |
| FY-1 | 5 ✔ | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | 95,502 |
| FY-1 | 6 | DebtLongtermAndShorttermCombinedAmount | 92,568 |
| FY0 | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2026-05-31 |
| FY0 | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-05-31 |
| FY0 | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-05-31 |
| FY0 | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2026-05-31 |
| FY0 | 5 ✔ | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | 137,242 |
| FY0 | 6 | DebtLongtermAndShorttermCombinedAmount | 129,541 |
| LTM | 1 | LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities] | not usable: LongTermDebtNoncurrent not reported at 2026-08-31 |
| LTM | 2 | LongTermDebtAndCapitalLeaseObligations + [short_term_debt] | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-08-31 |
| LTM | 3 | LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings | not usable: LongTermDebtAndCapitalLeaseObligations not reported at 2026-08-31 |
| LTM | 4 | LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities] | not usable: LongTermDebt not reported at 2026-08-31 |
| LTM | 5 ✔ | LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] | 134,522 |
| LTM | 6 | DebtLongtermAndShorttermCombinedAmount | not usable: DebtLongtermAndShorttermCombinedAmount not reported at 2026-08-31 |

## Fallback log

### Not available (0)


### Reconciliation (1)

- **total_debt FY0** (warning): total debt uses rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] = $137,242m, but rank 6 DebtLongtermAndShorttermCombinedAmount = $129,541m (-5.6%). Check which matches the balance sheet.

### Fallbacks beyond rank 1 (19)

- **d_and_a FY-2**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2023-06-01 to 2024-05-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2023-06-01 to 2024-05-31; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2023-06-01 to 2024-05-31
- **finance_lease_liabilities FY-2**: used rank 2 FinanceLeaseLiability because rank 1 FinanceLeaseLiabilityCurrent + FinanceLeaseLiabilityNoncurrent: FinanceLeaseLiabilityCurrent not reported at 2024-05-31
- **total_debt FY-2**: used rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2024-05-31; rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt]: LongTermDebtAndCapitalLeaseObligations not reported at 2024-05-31; rank 3 LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings: LongTermDebtAndCapitalLeaseObligations not reported at 2024-05-31; rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities]: LongTermDebt not reported at 2024-05-31
- **short_term_investments FY-2**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2024-05-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2024-05-31
- **dividends FY-2**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2023-06-01 to 2024-05-31
- **d_and_a FY-1**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2024-06-01 to 2025-05-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2024-06-01 to 2025-05-31; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2024-06-01 to 2025-05-31
- **total_debt FY-1**: used rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2025-05-31; rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt]: LongTermDebtAndCapitalLeaseObligations not reported at 2025-05-31; rank 3 LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings: LongTermDebtAndCapitalLeaseObligations not reported at 2025-05-31; rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities]: LongTermDebt not reported at 2025-05-31
- **short_term_investments FY-1**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2025-05-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2025-05-31
- **dividends FY-1**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2024-06-01 to 2025-05-31
- **d_and_a FY0**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-06-01 to 2026-05-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-06-01 to 2026-05-31; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2025-06-01 to 2026-05-31
- **total_debt FY0**: used rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2026-05-31; rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt]: LongTermDebtAndCapitalLeaseObligations not reported at 2026-05-31; rank 3 LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings: LongTermDebtAndCapitalLeaseObligations not reported at 2026-05-31; rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities]: LongTermDebt not reported at 2026-05-31
- **short_term_investments FY0**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-05-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-05-31
- **dividends FY0**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-06-01 to 2026-05-31
- **revenue LTM**: used rank 2 RevenueFromContractWithCustomerExcludingAssessedTax because rank 1 Revenues: Revenues not reported for 2026-06-01 to 2026-08-31
- **d_and_a LTM**: used rank 4 Depreciation + AmortizationOfIntangibleAssets because rank 1 DepreciationDepletionAndAmortization: DepreciationDepletionAndAmortization not reported for 2025-06-01 to 2026-05-31; rank 2 DepreciationAndAmortization: DepreciationAndAmortization not reported for 2025-06-01 to 2026-05-31; rank 3 DepreciationAmortizationAndAccretionNet: DepreciationAmortizationAndAccretionNet not reported for 2025-06-01 to 2026-05-31
- **short_term_debt LTM**: used rank 4 NotesPayableCurrent because rank 1 DebtCurrent: DebtCurrent not reported at 2026-08-31; rank 2 LongTermDebtCurrent + ShortTermBorrowings + CommercialPaper: LongTermDebtCurrent not reported at 2026-08-31; rank 3 LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings + CommercialPaper: LongTermDebtAndCapitalLeaseObligationsCurrent not reported at 2026-08-31
- **total_debt LTM**: used rank 5 LongTermNotesAndLoans + [short_term_debt] + [finance_lease_liabilities] because rank 1 LongTermDebtNoncurrent + [short_term_debt] + [finance_lease_liabilities]: LongTermDebtNoncurrent not reported at 2026-08-31; rank 2 LongTermDebtAndCapitalLeaseObligations + [short_term_debt]: LongTermDebtAndCapitalLeaseObligations not reported at 2026-08-31; rank 3 LongTermDebtAndCapitalLeaseObligations + LongTermDebtAndCapitalLeaseObligationsCurrent + ShortTermBorrowings: LongTermDebtAndCapitalLeaseObligations not reported at 2026-08-31; rank 4 LongTermDebt + ShortTermBorrowings + [finance_lease_liabilities]: LongTermDebt not reported at 2026-08-31
- **short_term_investments LTM**: used rank 3 AvailableForSaleSecuritiesDebtSecuritiesCurrent because rank 1 ShortTermInvestments: ShortTermInvestments not reported at 2026-08-31; rank 2 MarketableSecuritiesCurrent: MarketableSecuritiesCurrent not reported at 2026-08-31
- **dividends LTM**: used rank 2 PaymentsOfDividendsCommonStock because rank 1 PaymentsOfDividends: PaymentsOfDividends not reported for 2025-06-01 to 2026-05-31

### Assumed zero: not reported (5)

- **undrawn_revolver FY-2**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2024-05-31)
- **undrawn_revolver FY-1**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2025-05-31)
- **undrawn_revolver FY0**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-05-31)
- **undrawn_revolver LTM**: assumed zero: not reported (rank 1 LineOfCreditFacilityRemainingBorrowingCapacity: LineOfCreditFacilityRemainingBorrowingCapacity not reported at 2026-08-31)
- **short_term_borrowings FY0**: assumed zero: not reported (rank 1 ShortTermBorrowings: ShortTermBorrowings not reported at 2026-05-31; rank 2 CommercialPaper: CommercialPaper not reported at 2026-05-31)

### Restated values (most recently filed value used) (1)

- **finance_lease_liabilities FY-1**: FinanceLeaseLiabilityNoncurrent at 2025-05-31: restated from 2,700,000,000 (accession 0000950170-25-087926, filed 2025-06-18) to 2,677,000,000 (accession 0001193125-26-277521, filed 2026-06-22); using the most recently filed value

### Different candidates across periods (2)

- **revenue all**: different candidates across periods (FY-2: rank 1 Revenues; FY-1: rank 1 Revenues; FY0: rank 1 Revenues; LTM: rank 2 RevenueFromContractWithCustomerExcludingAssessedTax)
- **short_term_debt all**: different candidates across periods (FY-2: rank 1 DebtCurrent; FY-1: rank 1 DebtCurrent; FY0: rank 1 DebtCurrent; LTM: rank 4 NotesPayableCurrent)

### Possible structural change (0)


### Stale data (0)
