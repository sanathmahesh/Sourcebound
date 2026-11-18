"""Golden-sheet comparison and the blind labelling sheet."""

import csv
import io
import random

from sourcebound.contracts import CompanyMetrics, Memo
from sourcebound.evals.golden import compare_sheet, parse_golden_sheet
from sourcebound.evals.labelling import build_sheet, read_labels, sheet_csv
from sourcebound.paths import PROJECT_ROOT
from sourcebound.pipeline.golden_templates import INPUTS

PUBLISHED = PROJECT_ROOT / "data" / "published" / "companies"


def filled_gt_sheet() -> str:
    """A GT sheet filled in by 'hand' with values read from the 10-K (accession 0001628280-26-006708)."""
    rows = {1: "18,280", 2: "999", 5: "801"}  # revenue and cash as filed; operating income deliberately wrong
    lines = ["# Golden-set sheet: GOODYEAR (GT)", "", "| Field | Value |", "|---|---|",
             "| Units in filing (e.g. millions) | millions |", "", "## Inputs", "",
             "| # | Item | Where to look | Value in filing | Page or note |", "|---|---|---|---|---|"]
    for n, (item, where) in enumerate(INPUTS, start=1):
        lines.append(f"| {n} | {item} | {where} | {rows.get(n, '')} | |")
    lines += ["", "| # | Item | Formula | Your value |", "|---|---|---|---|",
              "| D3 | Debt / EBITDA | D2 / D1 | 4.57 |", "| D6 | FCF / debt (%) | (10 - 11) / D2 x 100 | -0.5% |",
              "", "| # | Question | Answer | Exact location (section and page) | Quote (a few words copied from the passage) |",
              "|---|---|---|---|---|", "| Q1 | Revolver size | $2.75 billion | Note 16, p. 92 | first lien revolving credit facility |"]
    return "\n".join(lines)


def test_parse_golden_sheet():
    sheet = parse_golden_sheet(filled_gt_sheet())
    assert sheet.unit == 1e6
    assert sheet.values["1"] == "18,280" and sheet.values["4"] == "" and sheet.values["D3"] == "4.57"
    assert sheet.facts[0].quote == "first lien revolving credit facility"


def test_compare_with_the_engine():
    cm = CompanyMetrics.model_validate_json((PUBLISHED / "GT" / "metrics.json").read_text())
    results = {r.row: r for r in compare_sheet(parse_golden_sheet(filled_gt_sheet()), cm)}
    assert results["1"].status == "match"  # 18,280 (RevenueFromContract..., accn 0001628280-26-006708)
    assert results["5"].status == "match"  # cash 801
    assert results["2"].status == "mismatch"  # 999 typed; engine 312 (derived)
    assert results["4"].status == "not_filled"
    assert results["D3"].status == "match"  # 6,198 / 1,357 = 4.567x
    assert results["D6"].status == "match"  # (796 - 826) / 6,198 = -0.48%


def memos():
    return [Memo.model_validate_json((PUBLISHED / t / "memo.json").read_text()) for t in ("WMT", "VZ")]


def test_labelling_sheet_hides_model_identity():
    wmt, vz = memos()
    rows, key = build_sheet([("secret-model-A", "run-xyz-1", wmt), ("secret-model-B", "run-xyz-2", vz)], seed=7)
    text = sheet_csv(rows)
    for hidden in ["secret-model", "run-xyz", "GLM", "zai-org", "deepseek", "DeepSeek", "rating_rationale-"]:
        assert hidden not in text
    assert set(key) == {r["id"] for r in rows}
    assert {key[r["id"]]["model"] for r in rows} == {"secret-model-A", "secret-model-B"}


def test_two_claims_per_section_twelve_per_memo_and_shuffled():
    wmt, vz = memos()
    rows, key = build_sheet([("a", "r1", wmt), ("b", "r2", vz)], seed=7)
    assert len(rows) == 24
    per_memo_section = {}
    for r in rows:
        k = key[r["id"]]
        per_memo_section.setdefault((k["model"], k["section"]), 0)
        per_memo_section[(k["model"], k["section"])] += 1
    assert set(per_memo_section.values()) == {2}
    assert [key[r["id"]]["model"] for r in rows] != sorted(key[r["id"]]["model"] for r in rows)  # interleaved
    again, _ = build_sheet([("a", "r1", wmt), ("b", "r2", vz)], seed=7)
    assert [r["claim"] for r in again] == [r["claim"] for r in rows]  # deterministic


def test_reading_labels_back():
    text = "id,claim,cited passage,my verdict,citation correct,notes\nL001,x,y,S,Y,\nL002,x,y,partially,n,odd\nL003,x,y,,,\n"
    labels = read_labels(io.StringIO(text))
    assert labels == {"L001": {"verdict": "supported", "citation_correct": True, "notes": ""},
                      "L002": {"verdict": "partially_supported", "citation_correct": False, "notes": "odd"}}
