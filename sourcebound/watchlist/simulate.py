"""Phase-6 check: a simulated new filing, then a quiet rerun (PLAN.md phase 6 "Ends with").

Run:  uv run python -m sourcebound.watchlist.simulate VZ

Works on a temporary copy of data/published (the real files are untouched): rolls the company's state back
to its previous 10-Q, runs the daily job against live EDGAR (so the latest 10-Q looks new), then runs it again
with nothing new. Writes reports/watchlist-simulation.md.
"""

from __future__ import annotations

import shutil
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

from sourcebound.contracts import FilingRef, Watchlist, WatchState
from sourcebound.edgar.filings import parse_filings, submissions_url
from sourcebound.edgar.tickers import TICKERS_URL
from sourcebound.engine.concepts import load_concepts
from sourcebound.overrides import company_for, load_overrides
from sourcebound.paths import CONFIG_DIR, REPORTS_DIR
from sourcebound.pipeline.export import build_company_metrics, load_companies
from sourcebound.pipeline.load import load_and_analyse, make_client
from sourcebound.scorecard.grid import load_grid
from sourcebound.watchlist.run import PUBLISHED, run_watch


def main(ticker: str) -> None:
    client = make_client()
    specs, grid = load_concepts(CONFIG_DIR / "concepts.yaml"), load_grid(CONFIG_DIR / "grid.yaml")
    overrides = load_overrides(CONFIG_DIR / "overrides.yaml")
    rows = load_companies()
    sectors = {r["ticker"]: r["sector"] for r in rows}
    tickers_json = client.get_json(TICKERS_URL)

    def fetch(t: str) -> dict:
        return client.get_json(submissions_url(company_for(t, tickers_json, overrides).cik), refresh=True)

    refreshed = []

    def refresh(t: str):
        refreshed.append(t)
        return build_company_metrics(load_and_analyse(client, t, specs, refresh=True), grid, sectors[t])

    with tempfile.TemporaryDirectory() as tmp:
        site = Path(tmp) / "published"
        shutil.copytree(PUBLISHED, site)
        state = WatchState.model_validate_json((site / "state.json").read_text())
        quarters = [f for f in parse_filings(fetch(ticker)) if f.form == "10-Q"]
        previous = quarters[1]
        current = state.companies[ticker].latest_10q
        state.companies[ticker] = state.companies[ticker].model_copy(update={"latest_10q": FilingRef(
            form="10-Q", accession=previous.accession, period_end=previous.report_date, filed=previous.filed)})
        (site / "state.json").write_text(state.model_dump_json(indent=1, by_alias=True))

        now = datetime.now(timezone.utc).replace(microsecond=0)
        first = run_watch(now, [r["ticker"] for r in rows], fetch, refresh, published_dir=site, sectors=sectors)
        after = WatchState.model_validate_json((site / "state.json").read_text()).companies[ticker]
        item = next(i for i in Watchlist.model_validate_json((site / "watchlist.json").read_text()).items if i.ticker == ticker)
        refreshed_first = list(refreshed)
        snapshot = {p.relative_to(site): p.read_bytes() for p in site.rglob("*.json")}
        second = run_watch(now + timedelta(hours=1), [r["ticker"] for r in rows], fetch, refresh, published_dir=site,
                           sectors=sectors)
        unchanged = snapshot == {p.relative_to(site): p.read_bytes() for p in site.rglob("*.json")}

    lines = [
        "# Watchlist simulation", "",
        f"Run {now:%Y-%m-%d %H:%M UTC} with `uv run python -m sourcebound.watchlist.simulate {ticker}` on a temporary copy "
        "of data/published, against live EDGAR filing lists.", "",
        f"Setup: {ticker}'s state rolled back from 10-Q {current.accession} (period {current.period_end}) to the previous "
        f"10-Q {previous.accession} (period {previous.report_date}).", "",
        "## Run 1: a 'new' filing", "",
        f"- New filings detected: {', '.join(first.changed) or 'none'}",
        f"- Companies refreshed (facts re-downloaded, metrics recomputed): {', '.join(refreshed_first) or 'none'}",
        f"- Files written: {', '.join(sorted(str(p.relative_to(site)) for p in first.written))}",
        f"- {ticker} memo status: **{after.memo_status}**; latest 10-Q now {after.latest_10q.accession}",
        f"- {ticker} flags ({len(item.flags)}):",
    ]
    lines += [f"  - {f.type} ({f.severity}): {f.rule}; {f.from_} -> {f.to}" for f in item.flags] or ["  - none"]
    lines += ["", "## Run 2: nothing new", "",
              f"- New filings detected: {', '.join(second.changed) or 'none'}",
              f"- Files written: {len(second.written)}; every published file byte-for-byte unchanged: **{unchanged}**", ""]
    text = "\n".join(lines)
    (REPORTS_DIR / "watchlist-simulation.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main(sys.argv[1].upper() if len(sys.argv) > 1 else "VZ")
