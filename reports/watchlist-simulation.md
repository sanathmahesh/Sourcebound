# Watchlist simulation

Run 2026-11-18 07:57 UTC with `uv run python -m sourcebound.watchlist.simulate VZ` on a temporary copy of data/published, against live EDGAR filing lists.

Setup: VZ's state rolled back from 10-Q 0000732712-26-000052 (period 2026-09-30) to the previous 10-Q 0000732712-26-000046 (period 2026-06-30).

## Run 1: a 'new' filing

- New filings detected: VZ
- Companies refreshed (facts re-downloaded, metrics recomputed): VZ, XOM
- Files written: index.json, state.json, watchlist.json
- VZ memo status: **stale**; latest 10-Q now 0000732712-26-000052
- VZ flags (2):
  - liquidity_shortfall (warning): liquidity coverage below 1.2 (warning) or 1.0 (alert); 1.20x threshold -> 1.06x
  - near_term_maturities (alert): debt due within 12 months above 50% (warning) or 100% (alert) of cash, short-term investments and undrawn revolver; 50% threshold -> 145%

## Run 2: nothing new

- New filings detected: none
- Files written: 0; every published file byte-for-byte unchanged: **True**
