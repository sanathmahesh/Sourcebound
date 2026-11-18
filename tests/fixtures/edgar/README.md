# EDGAR test fixtures

Trimmed copies of real SEC EDGAR responses, captured 18 November 2026 (UTC) by
`capture_fixtures.py` from the local cache. Each JSON file records its source URL and fetch time under
`_capture`.

| File | Source | Kept |
|---|---|---|
| `company_tickers_subset.json` | https://www.sec.gov/files/company_tickers.json | rows for WMT, VZ, GT |
| `submissions_<T>.json` | https://data.sec.gov/submissions/CIK##########.json | identity fields; 10-K/10-Q rows of filings.recent |
| `companyfacts_<T>.json` | https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json | us-gaap tags named in config/concepts.yaml; facts ending on or after 2021-01-01 |

Kept facts are unmodified: each retains its value, dates, accession number (`accn`), form and filing date.

To re-capture after changing the chains: run the ratio report once (to fill the cache), then
`uv run python tests/fixtures/edgar/capture_fixtures.py WMT VZ GT`, and re-check the expected values in
`tests/test_company_fixtures.py` against the new JSON.
