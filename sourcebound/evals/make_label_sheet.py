"""Export the blind labelling sheet from the golden-set run-1 memos of every writer.

Run:  uv run python -m sourcebound.evals.make_label_sheet

Writes evals/labels/labelling-sheet.csv (what the author fills in) and evals/labels/key.json (row -> model,
claim; do not open it while labelling). Refuses to overwrite a sheet that already has labels in it.
"""

from __future__ import annotations

import json

import yaml

from sourcebound.contracts import Memo
from sourcebound.evals.labelling import build_sheet, read_labels, sheet_csv
from sourcebound.evals.run_memos import EVAL_MEMOS, short_name
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.pipeline.export import load_companies

LABEL_DIR = PROJECT_ROOT / "evals" / "labels"
SHEET = LABEL_DIR / "labelling-sheet.csv"
KEY = LABEL_DIR / "key.json"
SEED = 20261118


def main() -> None:
    if SHEET.exists():
        with SHEET.open() as f:
            if read_labels(f):
                raise SystemExit(f"{SHEET.relative_to(PROJECT_ROOT)} already has labels; not overwriting it.")
    writers = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())["writers"]
    golden = [r["ticker"] for r in load_companies() if r["golden"]]
    memos, missing = [], []
    for writer in writers:
        run_dir = EVAL_MEMOS / short_name(writer) / "run1"
        for ticker in golden:
            path = run_dir / "companies" / ticker / "memo.json"
            if path.exists():
                memos.append((writer, str(run_dir.relative_to(PROJECT_ROOT)), Memo.model_validate_json(path.read_text())))
            else:
                missing.append(f"{short_name(writer)} {ticker}")
    if missing:
        raise SystemExit(f"golden run-1 memos missing: {', '.join(missing)}; run sourcebound.evals.run_memos --golden-only")
    rows, key = build_sheet(memos, seed=SEED)
    LABEL_DIR.mkdir(parents=True, exist_ok=True)
    SHEET.write_text(sheet_csv(rows))
    KEY.write_text(json.dumps(key, indent=1))
    print(f"{len(rows)} claims from {len(memos)} memos -> {SHEET.relative_to(PROJECT_ROOT)} (key in {KEY.name})")


if __name__ == "__main__":
    main()
