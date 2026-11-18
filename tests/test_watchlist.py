"""Watchlist run: detection, stale marking, idempotency and the weekly heartbeat. No network, no model."""

import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone

import pytest

from sourcebound.contracts import CompanyMetrics, SiteIndex, WatchState, Watchlist
from sourcebound.paths import PROJECT_ROOT
from sourcebound.watchlist.detect import latest_filings
from sourcebound.watchlist.run import initial_state, run_watch

SOURCE = PROJECT_ROOT / "data" / "published" / "companies" / "GT"
T0 = datetime(2026, 11, 18, 6, 0, tzinfo=timezone.utc)


def submissions(rows):
    cols = ["form", "accessionNumber", "filingDate", "reportDate", "primaryDocument"]
    return {"filings": {"recent": {c: [r[i] for r in rows] for i, c in enumerate(cols)}}}


@pytest.fixture
def site(tmp_path):
    (tmp_path / "companies" / "GT").mkdir(parents=True)
    for name in ("metrics.json", "memo.json", "verification.json"):
        shutil.copy(SOURCE / name, tmp_path / "companies" / "GT" / name)
    cm = CompanyMetrics.model_validate_json((SOURCE / "metrics.json").read_text())
    rows = [(s.form, s.accession, s.filed.isoformat(), s.period_end.isoformat(), "d.htm") for s in cm.sources]
    return tmp_path, cm, rows


def watch(site_dir, rows, cm, now, refreshed):
    def fetch(ticker):
        return submissions(rows)

    def refresh(ticker):
        refreshed.append(ticker)
        return cm

    return run_watch(now, ["GT"], fetch, refresh, published_dir=site_dir, sectors={"GT": "Autos"})


def test_latest_filings_ignore_amendments():
    k, q = latest_filings(submissions([
        ("10-Q/A", "a", "2026-12-01", "2026-09-30", "x"), ("10-Q", "q", "2026-11-05", "2026-09-30", "x"),
        ("10-K", "k", "2026-02-10", "2025-12-31", "x")]))
    assert (k.accession, q.accession) == ("k", "q")


def test_first_run_writes_files_then_a_quiet_day_writes_nothing(site):
    site_dir, cm, rows = site
    refreshed = []
    first = watch(site_dir, rows, cm, T0, refreshed)
    assert {p.name for p in first.written} == {"state.json", "watchlist.json", "index.json"}
    snapshot = {p: p.read_bytes() for p in site_dir.rglob("*.json")}
    second = watch(site_dir, rows, cm, T0 + timedelta(days=1), refreshed)
    assert second.written == [] and second.changed == [] and refreshed == []
    assert snapshot == {p: p.read_bytes() for p in site_dir.rglob("*.json")}


def test_new_filing_refreshes_flags_and_marks_the_memo_stale(site):
    site_dir, cm, rows = site
    watch(site_dir, rows, cm, T0, [])
    refreshed = []
    newer = [("10-Q", "0000000000-26-999999", "2027-02-01", "2026-12-31", "d.htm")] + rows
    outcome = watch(site_dir, newer, cm, T0 + timedelta(days=1), refreshed)
    assert outcome.changed == ["GT"] and refreshed == ["GT"]
    state = WatchState.model_validate_json((site_dir / "state.json").read_text())
    assert state.companies["GT"].memo_status == "stale"
    assert state.companies["GT"].latest_10q.accession == "0000000000-26-999999"
    watchlist = Watchlist.model_validate_json((site_dir / "watchlist.json").read_text())
    [item] = watchlist.items
    assert item.memo_status == "stale" and item.flags  # GT has open flags (e.g. liquidity below 1.0)
    index = SiteIndex.model_validate_json((site_dir / "index.json").read_text())
    assert index.companies[0].memo_status == "stale" and index.companies[0].open_flags == len(item.flags)


def test_watchlist_items_carry_the_change_since_the_prior_year_end(site):
    site_dir, cm, rows = site
    watch(site_dir, rows, cm, T0, [])
    item = Watchlist.model_validate_json((site_dir / "watchlist.json").read_text()).items[0]
    assert [(c.metric_id, c.label, c.display) for c in item.changes] == [
        ("debt_to_ebitda", "Debt / EBITDA", "+2.88x"), ("interest_coverage", "EBITDA / interest", "-0.66x")]


def test_weekly_heartbeat_updates_the_checked_date_only(site):
    site_dir, cm, rows = site
    watch(site_dir, rows, cm, T0, [])
    quiet = watch(site_dir, rows, cm, T0 + timedelta(days=6), [])
    assert quiet.written == []
    beat = watch(site_dir, rows, cm, T0 + timedelta(days=7), [])
    assert beat.heartbeat and {p.name for p in beat.written} == {"state.json", "watchlist.json"}
    assert Watchlist.model_validate_json((site_dir / "watchlist.json").read_text()).checked_at == T0 + timedelta(days=7)


def test_metrics_behind_the_filing_list_are_refreshed_again(site):
    """Company facts can lag a new filing; the next run tries again until the metrics include it."""
    site_dir, cm, rows = site
    newer = [("10-Q", "0000000000-26-999999", "2027-02-01", "2026-12-31", "d.htm")] + rows
    watch(site_dir, newer, cm, T0, [])  # first run records the new filing; metrics (cm) do not have it
    refreshed = []
    watch(site_dir, newer, cm, T0 + timedelta(days=1), refreshed)
    assert refreshed == ["GT"]


def test_initial_state_marks_existing_memos_current(site):
    site_dir, cm, rows = site
    state = initial_state(T0, ["GT"], lambda t: submissions(rows), published_dir=site_dir)
    assert state.companies["GT"].memo_status == "current"


def test_watchlist_code_imports_no_model_client():
    code = "import sys, sourcebound.watchlist.run; print('sourcebound.llm.provider' in sys.modules, 'openai' in sys.modules)"
    out = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, check=True).stdout.strip()
    assert out == "False False"


def test_a_refresh_that_changes_only_timestamps_writes_nothing(site):
    """Found by the live simulation: ExxonMobil is refreshed daily (its June 10-Q's facts sit under another
    registrant), and each refresh carries a new download time. That alone must not change any file."""
    site_dir, cm, rows = site
    newer = [("10-Q", "0000000000-26-999999", "2027-02-01", "2026-12-31", "d.htm")] + rows
    watch(site_dir, newer, cm, T0, [])
    later = cm.model_copy(update={"data_fetched_at": "2026-11-19T06:00:00+00:00",
                                  "generated_at": T0 + timedelta(days=1)})
    snapshot = {p: p.read_bytes() for p in site_dir.rglob("*.json")}
    refreshed = []

    def fetch(ticker):
        return submissions(newer)

    def refresh(ticker):
        refreshed.append(ticker)
        return later

    outcome = run_watch(T0 + timedelta(days=1), ["GT"], fetch, refresh, published_dir=site_dir, sectors={"GT": "Autos"})
    assert refreshed == ["GT"] and outcome.written == []
    assert snapshot == {p: p.read_bytes() for p in site_dir.rglob("*.json")}
