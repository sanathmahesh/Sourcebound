"""Golden-set sheet templates: blank for the author to fill, never overwritten once they exist."""

from sourcebound.engine.analysis import analyse_company
from sourcebound.engine.concepts import load_concepts
from sourcebound.paths import CONFIG_DIR
from sourcebound.pipeline.golden_templates import render_golden_sheet, write_golden_sheet
from tests.helpers import load_fixture


def gt():
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    return analyse_company("GT", load_fixture("companyfacts_GT.json"), load_fixture("submissions_GT.json"), specs)


def test_sheet_names_the_filing_and_leaves_values_blank():
    text = render_golden_sheet(gt())
    assert "0001628280-26-006708" in text and "2025-12-31" in text
    rows = [line for line in text.splitlines() if line.startswith("| ") and line.split("|")[1].strip().isdigit()]
    assert len(rows) == 19  # inputs 1-19
    for row in rows:
        cells = [c.strip() for c in row.split("|")[1:-1]]
        assert cells[3] == "" and cells[4] == "", row  # value and page columns are blank


def test_sheet_includes_finance_leases_and_engine_formulas():
    text = render_golden_sheet(gt())
    assert "Finance-lease liabilities" in text
    assert "| D2 | Total debt | 7 + 8 + 9 |" in text
    assert "| D7 | Liquidity coverage |" in text
    for q in ["Q1", "Q2", "Q3", "Q4", "Q5"]:
        assert f"| {q} |" in text


def test_existing_sheet_is_never_overwritten(tmp_path):
    analysis = gt()
    path = tmp_path / "GT.md"
    path.write_text("my filled-in values")
    assert write_golden_sheet(analysis, tmp_path) is False
    assert path.read_text() == "my filled-in values"
    (tmp_path / "GT.md").unlink()
    assert write_golden_sheet(analysis, tmp_path) is True
