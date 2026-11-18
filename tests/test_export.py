"""Metrics export: the data contract, the reviewer checklist, and validation of every published file."""

import json

import pytest

from sourcebound.contracts import CompanyMetrics
from sourcebound.engine.analysis import analyse_company
from sourcebound.engine.checklist import data_checklist
from sourcebound.engine.concepts import load_concepts
from sourcebound.overrides import Override
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.pipeline.export import build_company_metrics
from sourcebound.scorecard.grid import load_grid
from sourcebound.scorecard.scoring import score_company
from tests.helpers import load_fixture

GRID = load_grid(CONFIG_DIR / "grid.yaml")


@pytest.fixture(scope="module")
def gt():
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    return analyse_company("GT", load_fixture("companyfacts_GT.json"), load_fixture("submissions_GT.json"), specs)


@pytest.fixture(scope="module")
def exported(gt):
    return build_company_metrics(gt, GRID, sector="Autos")


def test_export_round_trips_through_the_contract(exported):
    again = CompanyMetrics.model_validate_json(exported.model_dump_json())
    assert again == exported


def test_metrics_are_keyed_like_memo_placeholders(exported):
    # The memo will write {{m:debt_to_ebitda:LTM}}; the key is "<metric_id>:<period>".
    for key in ["debt_to_ebitda:LTM", "liquidity_coverage:FY0", "near_term_maturity_cover:FY0", "total_debt:FY0"]:
        assert key in exported.metrics
    metric = exported.metrics["debt_to_ebitda:LTM"]
    assert (metric.metric_id, metric.period, metric.unit) == ("debt_to_ebitda", "LTM", "x")


def test_ratio_inputs_carry_full_lineage(exported):
    inputs = exported.metrics["interest_coverage:LTM"].inputs
    roles = {i.role for i in inputs}
    assert {"FY0", "current year-to-date", "prior-year year-to-date"} <= roles
    one = inputs[0]
    assert one.accession and one.url.startswith("https://www.sec.gov/Archives/edgar/data/42582/")
    assert one.fallback_rank >= 1 and one.tag


def test_assumed_zero_concept_exports_as_zero_with_a_note(exported):
    sti = exported.metrics["short_term_investments:FY0"]
    assert (sti.status, sti.value) == ("ok", 0)
    assert any("assumed zero" in n for n in sti.notes)


def test_scorecards_and_disclaimer(exported):
    assert exported.scorecard.basis == "latest" and exported.scorecard_fy0.basis == "FY0"
    assert "not credit ratings" in exported.scorecard.disclaimer


def test_checklist_groups_log_entries_by_subject(gt):
    items = data_checklist(gt, [score_company(GRID, gt, "latest")])
    fallback = [i for i in items if i.category == "fallback" and i.ref == "operating_income"]
    assert len(fallback) == 1  # one item for all four periods, not four
    assert "FY-2, FY-1, FY0, LTM" in fallback[0].message
    assert any(i.category == "assumed_zero" and i.ref == "short_term_investments" for i in items)
    assert any(i.category == "not_available" and i.ref == "maturity_after_year_5" for i in items)
    assert len({i.id for i in items}) == len(items)  # ids are unique


def test_checklist_lists_overrides_and_provisional_grades(gt):
    gt.overrides = [Override("GT", "cik", "test reason", "2026-11-17", cik=1)]
    card = score_company(GRID, gt, "latest")
    card.provisional = True
    items = data_checklist(gt, [card])
    gt.overrides = []
    assert any(i.category == "override" and "test reason" in i.message for i in items)
    assert any(i.category == "provisional_grade" for i in items)


def test_every_published_metrics_file_validates_against_the_contract():
    companies = __import__("yaml").safe_load((CONFIG_DIR / "companies.yaml").read_text())["companies"]
    files = sorted((PROJECT_ROOT / "data" / "published" / "companies").glob("*/metrics.json"))
    assert len(files) == len(companies), "every company in config/companies.yaml must have a published metrics.json"
    for path in files:
        parsed = CompanyMetrics.model_validate_json(path.read_text())
        assert parsed.ticker == path.parent.name
        assert json.loads(path.read_text())["schema_version"] == parsed.schema_version
