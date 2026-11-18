"""Every file the site reads matches the data contract, and the committed JSON Schema is current."""

import json
from pathlib import Path

import pytest

from sourcebound import contracts as c
from sourcebound.paths import PROJECT_ROOT
from sourcebound.pipeline.export_schema import SCHEMA_FILE, schema_text

PUBLISHED = PROJECT_ROOT / "data" / "published"
TOP_LEVEL = {"index.json": c.SiteIndex, "watchlist.json": c.Watchlist, "state.json": c.WatchState,
             "evals.json": c.EvalsFile}
PER_COMPANY = {"metrics.json": c.CompanyMetrics, "memo.json": c.Memo, "verification.json": c.VerificationReport}


def published_files() -> list[tuple[Path, type]]:
    files = [(PUBLISHED / name, model) for name, model in TOP_LEVEL.items()]
    for company in sorted((PUBLISHED / "companies").iterdir()):
        files += [(company / name, model) for name, model in PER_COMPANY.items()]
    return files


@pytest.mark.parametrize("path,model", published_files(), ids=lambda v: str(v.relative_to(PUBLISHED)) if isinstance(v, Path) else "")
def test_published_file_matches_its_contract(path, model):
    model.model_validate_json(path.read_text())


def test_no_published_file_is_outside_the_contract():
    known = {path for path, _ in published_files()}
    found = {p for p in PUBLISHED.rglob("*") if p.is_file()}
    assert found - known == set()


def test_every_company_in_the_index_has_its_three_files():
    site = c.SiteIndex.model_validate_json((PUBLISHED / "index.json").read_text())
    assert len(site.companies) == 15
    for entry in site.companies:
        for name in PER_COMPANY:
            assert (PUBLISHED / "companies" / entry.ticker / name).exists(), f"{entry.ticker}/{name}"


def test_committed_schema_is_current():
    assert SCHEMA_FILE.read_text() == schema_text(), "run: uv run python -m sourcebound.pipeline.export_schema"


def test_schema_describes_every_published_root():
    defs = json.loads(schema_text())["$defs"]
    for name in ["SiteIndex", "CompanyMetrics", "Memo", "VerificationReport", "Watchlist", "WatchState",
                 "EvalsFile", "AskRequest", "AskResponse"]:
        assert name in defs
    assert "from" in defs["WatchFlag"]["properties"]  # the alias, as written to watchlist.json
