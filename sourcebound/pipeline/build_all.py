"""Build everything the site serves, in data/published/ (PLAN.md phase 6).

Run:  uv run python -m sourcebound.pipeline.build_all --memos-from evals/results/memos/GLM-5.3/run1
      uv run python -m sourcebound.pipeline.build_all            (generates all 15 memos: costs credit)

1. Export metrics.json for every company (no model).
2. Memos: copy already-verified memos from an evaluation run (--memos-from; no cost), or generate them with
   SAIL_MODEL_WRITER / SAIL_MODEL_JUDGE.
3. state.json (today's filing lists; every memo current), watchlist.json and index.json.
4. evals.json from evals/results/results.json.
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from sourcebound.contracts import CompanyMetrics, EvalsFile, Memo, WatchState
from sourcebound.paths import PROJECT_ROOT
from sourcebound.watchlist.run import PUBLISHED, _write, build_site_files, initial_state

RESULTS_JSON = PROJECT_ROOT / "evals" / "results" / "results.json"


def _metrics(published: Path, tickers: list[str]) -> dict[str, CompanyMetrics]:
    return {t: CompanyMetrics.model_validate_json((published / "companies" / t / "metrics.json").read_text())
            for t in tickers}


def write_site_files(state: WatchState, published: Path, sectors: dict[str, str]) -> None:
    now = datetime.now(timezone.utc).replace(microsecond=0)
    watchlist, index = build_site_files(now, state, _metrics(published, list(state.companies)), published, sectors)
    _write(published / "state.json", state)
    _write(published / "watchlist.json", watchlist)
    _write(published / "index.json", index)


def mark_memo_current(ticker: str, published: Path = PUBLISHED) -> None:
    """After the author regenerates (and reviews) a memo: record it as current and refresh the site files."""
    from sourcebound.pipeline.export import load_companies

    state_path = published / "state.json"
    if not state_path.exists():
        return
    state = WatchState.model_validate_json(state_path.read_text())
    memo = Memo.model_validate_json((published / "companies" / ticker / "memo.json").read_text())
    state.companies[ticker] = state.companies[ticker].model_copy(update={"memo_status": "current", "memo_date": memo.memo_date})
    write_site_files(state, published, {r["ticker"]: r["sector"] for r in load_companies()})


def publish_evals(published: Path = PUBLISHED) -> None:
    if RESULTS_JSON.exists():
        evals = EvalsFile(generated_at=datetime.now(timezone.utc).replace(microsecond=0),
                          source="evals/results/results.json", results=json.loads(RESULTS_JSON.read_text()))
        _write(published / "evals.json", evals)


def main() -> None:
    from sourcebound.edgar.filings import submissions_url
    from sourcebound.edgar.tickers import TICKERS_URL
    from sourcebound.overrides import company_for, load_overrides
    from sourcebound.paths import CONFIG_DIR
    from sourcebound.pipeline import export
    from sourcebound.pipeline.load import make_client

    parser = argparse.ArgumentParser(description="Build data/published/ for the site.")
    parser.add_argument("--memos-from", help="copy memos from this evaluation run directory instead of generating")
    args = parser.parse_args()
    rows = export.load_companies()
    tickers = [r["ticker"] for r in rows]
    sectors = {r["ticker"]: r["sector"] for r in rows}

    export.main([])  # step 1
    if args.memos_from:  # step 2
        source = PROJECT_ROOT / args.memos_from
        for t in tickers:
            for name in ("memo.json", "verification.json"):
                shutil.copy(source / "companies" / t / name, PUBLISHED / "companies" / t / name)
        print(f"copied {len(tickers)} verified memos from {args.memos_from}")
    else:
        from sourcebound.pipeline import generate_memo

        generate_memo.main_for(tickers)
    client = make_client()  # step 3
    overrides, tickers_json = load_overrides(CONFIG_DIR / "overrides.yaml"), client.get_json(TICKERS_URL)
    now = datetime.now(timezone.utc).replace(microsecond=0)
    state = initial_state(now, tickers, lambda t: client.get_json(
        submissions_url(company_for(t, tickers_json, overrides).cik)), PUBLISHED)
    write_site_files(state, PUBLISHED, sectors)
    publish_evals()  # step 4
    print("data/published/ built: metrics, memos, state, watchlist, index, evals")


if __name__ == "__main__":
    main()
