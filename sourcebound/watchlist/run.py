"""The daily watchlist job (PLAN.md 4.10). No model call: this module does not import the model client.

Run:  uv run python -m sourcebound.watchlist.run

For each company: read its EDGAR filing list (one request) and compare the latest 10-K and 10-Q with
data/published/state.json. For a new filing, refresh the company facts, recompute ratios and scorecard
(metrics.json), and mark the memo stale. A company whose metrics do not yet include its latest filing
(facts can lag a filing by hours) is refreshed again on the next run. Flags are recomputed for every company.

Files are written only when their content changes (timestamps aside), so a quiet day changes nothing and the
GitHub Action commits nothing; once a week a heartbeat updates the "last checked" date anyway.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

from pydantic import BaseModel

from sourcebound.contracts import (
    CompanyMetrics, CompanyState, FilingRef, HeadlineRatio, IndexEntry, Memo, SiteIndex, VerificationCounts,
    VerificationReport, WatchFlag, WatchItem, Watchlist, WatchState,
)
from sourcebound.memo.render import format_metric
from sourcebound.paths import PROJECT_ROOT
from sourcebound.watchlist.detect import latest_filings
from sourcebound.watchlist.flags import compute_flags, ratio_changes

PUBLISHED = PROJECT_ROOT / "data" / "published"
HEARTBEAT = timedelta(days=7)
HEADLINE = ["debt_to_ebitda", "net_leverage", "interest_coverage", "fcf_to_debt", "liquidity_coverage"]


@dataclass
class WatchOutcome:
    changed: list[str] = field(default_factory=list)  # companies with a new filing
    written: list[Path] = field(default_factory=list)
    heartbeat: bool = False


def _company_dir(published: Path, ticker: str) -> Path:
    return published / "companies" / ticker


def _memo(published: Path, ticker: str) -> Memo | None:
    path = _company_dir(published, ticker) / "memo.json"
    return Memo.model_validate_json(path.read_text()) if path.exists() else None


def initial_state(now: datetime, tickers: list[str], fetch: Callable[[str], dict], published_dir: Path) -> WatchState:
    """The first state: today's latest filings, and existing memos counted as current."""
    companies = {}
    for ticker in tickers:
        k, q = latest_filings(fetch(ticker))
        memo = _memo(published_dir, ticker)
        companies[ticker] = CompanyState(latest_10k=k, latest_10q=q, memo_status="current" if memo else "missing",
                                         memo_date=memo.memo_date if memo else None)
    return WatchState(checked_at=now, last_heartbeat=now, companies=companies)


def _without(data: dict, keys: tuple[str, ...]) -> dict:
    return {k: v for k, v in data.items() if k not in keys}


def _differs(path: Path, model: BaseModel, ignore: tuple[str, ...]) -> bool:
    if not path.exists():
        return True
    new = json.loads(model.model_dump_json(by_alias=True))
    return _without(new, ignore) != _without(json.loads(path.read_text()), ignore)


def _write(path: Path, model: BaseModel) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(model.model_dump_json(indent=1, by_alias=True) + "\n")


def _latest(cs: CompanyState) -> FilingRef | None:
    filings = [f for f in (cs.latest_10k, cs.latest_10q) if f]
    return max(filings, key=lambda f: f.filed) if filings else None


def _ltm_date(cm: CompanyMetrics):
    return next((p.balance_sheet_date for p in cm.periods if p.label == "LTM"), None)


def build_site_files(now: datetime, state: WatchState, metrics: dict[str, CompanyMetrics], published: Path,
                     sectors: dict[str, str]) -> tuple[Watchlist, SiteIndex]:
    items, entries = [], []
    for ticker, cs in state.companies.items():
        cm = metrics[ticker]
        raised = compute_flags(cm)
        flags = [WatchFlag(type=f.type, severity=f.severity, rule=f.rule, metric_id=f.metric_id, from_=f.from_value,
                           to=f.to_value) for f in raised]
        items.append(WatchItem(ticker=ticker, name=cm.name, latest_filing=_latest(cs), data_to=_ltm_date(cm),
                               memo_status=cs.memo_status, memo_date=cs.memo_date,
                               changes=ratio_changes(cm, raised), flags=flags))
        verification_path = _company_dir(published, ticker) / "verification.json"
        counts = None
        if verification_path.exists():
            s = VerificationReport.model_validate_json(verification_path.read_text()).summary
            counts = VerificationCounts(claims=s.claims, supported=s.supported,
                                        partially_supported=s.partially_supported, unsupported=s.unsupported)
        memo = _memo(published, ticker)
        headline = []
        for metric_id in HEADLINE:
            m = cm.metrics.get(f"{metric_id}:LTM")
            if m:
                headline.append(HeadlineRatio(metric_id=metric_id, label=m.label, period="LTM", value=m.value,
                                              unit=m.unit, status=m.status, display=format_metric(m)))
        card = cm.scorecard
        entries.append(IndexEntry(
            ticker=ticker, name=cm.name, sector=sectors.get(ticker, cm.sector), grade=card.grade,
            score=card.weighted_score, provisional=card.provisional, ig_like=card.ig_like, headline=headline,
            latest_filing=_latest(cs), data_to=_ltm_date(cm), memo_status=cs.memo_status, memo_date=cs.memo_date,
            memo_model=memo.model if memo else None, verification=counts, open_flags=len(flags),
            flag_types=[f.type for f in flags]))
    return Watchlist(checked_at=now, items=items), SiteIndex(generated_at=now, companies=entries)


def run_watch(now: datetime, tickers: list[str], fetch: Callable[[str], dict],
              refresh: Callable[[str], CompanyMetrics], published_dir: Path = PUBLISHED,
              sectors: dict[str, str] | None = None) -> WatchOutcome:
    published = Path(published_dir)
    state_path = published / "state.json"
    fresh = not state_path.exists()
    state = initial_state(now, tickers, fetch, published) if fresh else WatchState.model_validate_json(state_path.read_text())
    outcome = WatchOutcome()
    metrics: dict[str, CompanyMetrics] = {}
    for ticker in tickers:
        k, q = latest_filings(fetch(ticker))
        cs = state.companies.get(ticker)
        memo = _memo(published, ticker)
        if cs is None:
            cs = CompanyState(latest_10k=k, latest_10q=q, memo_status="current" if memo else "missing",
                              memo_date=memo.memo_date if memo else None)
        new = [f for f, old in ((k, cs.latest_10k), (q, cs.latest_10q)) if f and (old is None or f.accession != old.accession)]
        metrics_path = _company_dir(published, ticker) / "metrics.json"
        cm = CompanyMetrics.model_validate_json(metrics_path.read_text()) if metrics_path.exists() else None
        behind = cm is None or any(f.accession not in {s.accession for s in cm.sources} for f in (k, q) if f)
        if new or behind:
            cm = refresh(ticker)
            if _differs(metrics_path, cm, ("generated_at", "data_fetched_at")):
                _write(metrics_path, cm)
                outcome.written.append(metrics_path)
        if new and not fresh:
            outcome.changed.append(ticker)
            cs = cs.model_copy(update={"memo_status": "stale" if memo else "missing"})
        state.companies[ticker] = cs.model_copy(update={"latest_10k": k, "latest_10q": q})
        metrics[ticker] = cm

    watchlist, index = build_site_files(now, state, metrics, published, sectors or {})
    targets = [(published / "watchlist.json", watchlist, ("checked_at",)), (published / "index.json", index, ("generated_at",))]
    changed_files = [(p, m) for p, m, ignore in targets if fresh or _differs(p, m, ignore)]
    state_changed = fresh or _differs(state_path, state, ("checked_at", "last_heartbeat"))
    anything = state_changed or changed_files or outcome.written
    outcome.heartbeat = not anything and now - state.last_heartbeat >= HEARTBEAT
    if anything or outcome.heartbeat:
        state = state.model_copy(update={"checked_at": now, "last_heartbeat": now})
        _write(state_path, state)
        outcome.written.append(state_path)
        if outcome.heartbeat:
            changed_files = [(published / "watchlist.json", watchlist)]
        for path, model in changed_files:
            _write(path, model)
            outcome.written.append(path)
    return outcome


def main() -> None:
    from sourcebound.edgar.filings import submissions_url
    from sourcebound.edgar.tickers import TICKERS_URL
    from sourcebound.engine.concepts import load_concepts
    from sourcebound.overrides import company_for, load_overrides
    from sourcebound.paths import CONFIG_DIR
    from sourcebound.pipeline.export import build_company_metrics, load_companies
    from sourcebound.pipeline.load import load_and_analyse, make_client
    from sourcebound.scorecard.grid import load_grid

    client = make_client()
    specs, grid = load_concepts(CONFIG_DIR / "concepts.yaml"), load_grid(CONFIG_DIR / "grid.yaml")
    overrides = load_overrides(CONFIG_DIR / "overrides.yaml")
    rows = load_companies()
    sectors = {r["ticker"]: r["sector"] for r in rows}
    tickers_json = client.get_json(TICKERS_URL)

    def fetch(ticker: str) -> dict:
        return client.get_json(submissions_url(company_for(ticker, tickers_json, overrides).cik), refresh=True)

    def refresh(ticker: str) -> CompanyMetrics:
        return build_company_metrics(load_and_analyse(client, ticker, specs, refresh=True), grid, sectors[ticker])

    now = datetime.now(timezone.utc).replace(microsecond=0)
    outcome = run_watch(now, [r["ticker"] for r in rows], fetch, refresh, sectors=sectors)
    print(f"checked {len(rows)} companies at {now:%Y-%m-%d %H:%M UTC}; new filings: {', '.join(outcome.changed) or 'none'}; "
          f"files written: {len(outcome.written)}{' (weekly heartbeat)' if outcome.heartbeat else ''}")


if __name__ == "__main__":
    main()
