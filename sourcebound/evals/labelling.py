"""The blind claim-labelling sheet (PLAN.md 4.11 step 2 and 4.17).

From each golden-set memo, two claims per section are drawn at random (a fixed seed, so it is
reproducible), all rows are shuffled together, and nothing in the sheet says which model wrote a claim.
The mapping from row id to model and claim is kept in a separate key file.
"""

from __future__ import annotations

import csv
import io
import random

from sourcebound.contracts import Memo

COLUMNS = ["id", "claim", "cited passage", "my verdict", "citation correct", "notes"]
VERDICTS = {"s": "supported", "supported": "supported", "p": "partially_supported", "partially": "partially_supported",
            "partially supported": "partially_supported", "partially_supported": "partially_supported",
            "u": "unsupported", "unsupported": "unsupported"}
YES_NO = {"y": True, "yes": True, "true": True, "n": False, "no": False, "false": False}


def evidence_text(claim, memo: Memo) -> str:
    parts = []
    for n, citation in enumerate(claim.citations, start=1):
        passage = memo.passages.get(citation.chunk_id)
        source = f"{passage.form} for {passage.period_end}, {passage.section}" if passage else "passage missing"
        parts.append(f"[{n}] quote: “{citation.quote}”\n({source})\n{passage.text if passage else ''}")
    figures = [f"{memo.metrics[s.metric_id].label} ({s.metric_id.split(':')[-1]}) = {s.v}"
               for s in claim.segments if s.t == "metric" and s.metric_id in memo.metrics]
    if figures:
        parts.append("Engine figures: " + "; ".join(figures))
    return "\n\n".join(parts) or "(no citation and no engine figure)"


def build_sheet(memos: list[tuple[str, str, Memo]], seed: int, per_section: int = 2) -> tuple[list[dict], dict]:
    """memos: (model, run, memo). Returns the sheet rows and the key (row id -> model, run, claim)."""
    rng = random.Random(seed)
    drawn = []
    for model, run, memo in memos:
        for section in memo.sections:
            for claim in rng.sample(section.claims, min(per_section, len(section.claims))):
                drawn.append((model, run, memo, section.id, claim))
    rng.shuffle(drawn)
    rows, key = [], {}
    for n, (model, run, memo, section_id, claim) in enumerate(drawn, start=1):
        row_id = f"L{n:03d}"
        rows.append({"id": row_id, "claim": "".join(s.v for s in claim.segments),
                     "cited passage": evidence_text(claim, memo), "my verdict": "", "citation correct": "", "notes": ""})
        key[row_id] = {"model": model, "run": run, "ticker": memo.ticker, "section": section_id, "claim_id": claim.id}
    return rows, key


def sheet_csv(rows: list[dict]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def read_labels(handle) -> dict[str, dict]:
    """Rows the author has labelled: verdict (S/P/U or words) and citation correct (Y/N or blank)."""
    labels = {}
    for row in csv.DictReader(handle):
        verdict = VERDICTS.get(row.get("my verdict", "").strip().lower())
        if verdict is None:
            continue
        labels[row["id"]] = {"verdict": verdict,
                             "citation_correct": YES_NO.get(row.get("citation correct", "").strip().lower()),
                             "notes": row.get("notes", "").strip()}
    return labels
