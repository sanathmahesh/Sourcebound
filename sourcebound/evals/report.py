"""Compute every evaluation metric from saved outputs and write evals/results/results.md (and .json).

Run:  uv run python -m sourcebound.evals.report

No model is called: memos, verification reports, judge runs, seeded errors, the author's labels, golden
sheets and agency ratings are all read from disk. Every share carries its sample size; anything still
waiting for the author's input is reported as pending. Estimates never appear here.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean

import yaml

from sourcebound.contracts import CompanyMetrics, Memo, VerificationReport
from sourcebound.evals.golden import ROWS, compare_sheet, parse_golden_sheet
from sourcebound.evals.labelling import read_labels
from sourcebound.evals.metrics import judge_agreement, share, spearman, spread
from sourcebound.evals.ratings import IG_WORST_RANK, company_rank, load_agency_ratings
from sourcebound.evals.run_memos import EVAL_MEMOS, short_name
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.pipeline.export import load_companies
from sourcebound.retrieval.index import Hit, load_index, search
from sourcebound.verify.numbers import passage_numbers
from sourcebound.verify.quotes import normalise

EVALS = PROJECT_ROOT / "evals"
RESULTS = EVALS / "results"
PUBLISHED = PROJECT_ROOT / "data" / "published" / "companies"
COMMAND = "uv run python -m sourcebound.evals.report"


def load_eval_memos() -> list[tuple[str, int, str, Memo, VerificationReport]]:
    found = []
    for memo_path in sorted(EVAL_MEMOS.glob("*/run*/companies/*/memo.json")):
        writer, run = memo_path.parts[-5], int(memo_path.parts[-4][3:])
        report = VerificationReport.model_validate_json((memo_path.parent / "verification.json").read_text())
        found.append((writer, run, memo_path.parent.name, Memo.model_validate_json(memo_path.read_text()), report))
    return found


def writer_metrics(memos, golden: list[str]) -> dict:
    out = {}
    for writer in sorted({m[0] for m in memos}):
        first = [(t, m, r) for w, run, t, m, r in memos if w == writer and run == 1]
        claims = sum(r.summary.claims for _, _, r in first)
        cost = [m.run.drafting.cost_usd + m.run.verification.cost_usd for _, m, _ in first]
        repeats = {}
        for w, run, t, m, r in memos:
            if w == writer and t in golden:
                repeats.setdefault(run, []).append(r)
        per_run_supported = [share(sum(r.summary.supported for r in reps), sum(r.summary.claims for r in reps))["value"]
                             for reps in repeats.values()]
        out[writer] = {
            "model": first[0][1].model if first else writer,
            "memos_run1": len(first),
            "claims_per_memo": mean(r.summary.claims for _, _, r in first) if first else None,
            "judge_supported": share(sum(r.summary.supported for _, _, r in first), claims),
            "judge_partially": share(sum(r.summary.partially_supported for _, _, r in first), claims),
            "judge_unsupported": share(sum(r.summary.unsupported for _, _, r in first), claims),
            "raw_numbers_rejected_per_memo": mean(r.summary.raw_numbers_rejected for _, _, r in first) if first else None,
            "repairs_per_memo": mean(r.summary.repairs for _, _, r in first) if first else None,
            "cost_drafting_per_memo": mean(m.run.drafting.cost_usd for _, m, _ in first) if first else None,
            "cost_verification_per_memo": mean(m.run.verification.cost_usd for _, m, _ in first) if first else None,
            "cost_total_per_memo": mean(cost) if cost else None,
            "model_seconds_per_memo": mean(m.run.drafting.seconds + m.run.verification.seconds for _, m, _ in first)
            if first else None,
            "golden_runs": len(repeats),
            "run_to_run_judge_supported": spread([v for v in per_run_supported if v is not None]),
            "judge": first[0][1].judge_model if first else None,
        }
    return out


def golden_sheets() -> dict[str, object]:
    sheets = {}
    for path in sorted((EVALS / "golden").glob("*.md")):
        sheets[path.stem] = parse_golden_sheet(path.read_text())
    return sheets


def engine_accuracy(sheets) -> dict:
    compared = matched = filled = produced = 0
    per_company = {}
    for ticker, sheet in sheets.items():
        cm = CompanyMetrics.model_validate_json((PUBLISHED / ticker / "metrics.json").read_text())
        rows = compare_sheet(sheet, cm)
        filled_rows = [r for r in rows if r.status != "not_filled"]
        per_company[ticker] = {"filled": len(filled_rows), "match": sum(r.status == "match" for r in rows),
                               "mismatch": [r.row for r in rows if r.status == "mismatch"]}
        filled += len(filled_rows)
        produced += sum(r.engine is not None for r in filled_rows)
        compared += sum(r.status in ("match", "mismatch") for r in rows)
        matched += sum(r.status == "match" for r in rows)
        _write_golden_comparison(ticker, rows)
    return {"accuracy": share(matched, compared), "coverage": share(produced, filled), "per_company": per_company}


def _write_golden_comparison(ticker: str, rows) -> None:
    """'A script adds the tool's values and the match column afterwards' (PLAN.md 4.17), in a separate file."""
    lines = [f"# Golden-set comparison: {ticker}", "", f"Your sheet: evals/golden/{ticker}.md (unchanged). Command: {COMMAND}",
             "", "| Row | Engine figure | Your value | Engine value | Result |", "|---|---|---|---|---|"]
    for r in rows:
        engine = "—" if r.engine is None else (f"{r.engine:,.0f}" if r.kind == "amount" else f"{r.engine:.2f}")
        lines.append(f"| {r.row} | {r.key} | {r.hand or '—'} | {engine} | {r.status.replace('_', ' ')} |")
    (RESULTS / "golden").mkdir(parents=True, exist_ok=True)
    (RESULTS / "golden" / f"{ticker}.md").write_text("\n".join(lines) + "\n")


def memo_numeric_accuracy(memos, sheets) -> dict:
    out = {}
    for writer in sorted({m[0] for m in memos}):
        engine_checked = engine_matched = unmatched_keys = quoted = quoted_ok = 0
        for w, run, ticker, memo, _ in memos:
            if w != writer or run != 1 or ticker not in sheets:
                continue
            sheet = sheets[ticker]
            hand_by_key = {key: (row, kind) for row, (key, kind) in ROWS.items()}
            from sourcebound.evals.metrics import matches

            for section in memo.sections:
                for claim in section.claims:
                    for seg in claim.segments:
                        if seg.t == "quoted":
                            quoted += 1
                            passage = memo.passages.get(seg.chunk_id)
                            quoted_ok += bool(passage) and seg.v in passage_numbers(passage.text)
                        elif seg.t == "metric":
                            row = hand_by_key.get(seg.metric_id)
                            hand = sheet.values.get(row[0], "") if row else ""
                            metric = memo.metrics.get(seg.metric_id)
                            if not row or not hand or metric is None or metric.value is None or sheet.unit is None:
                                unmatched_keys += 1
                                continue
                            engine_checked += 1
                            engine_matched += matches(row[1], metric.value, hand, sheet.unit)
        out[writer] = {"engine_figures": share(engine_matched, engine_checked),
                       "engine_figures_without_hand_value": unmatched_keys,
                       "quoted_figures_in_cited_passage": share(quoted_ok, quoted)}
    return out


def quote_in_hits(quote: str, hits: list[Hit]) -> bool:
    target = normalise(quote)
    return bool(target) and any(target in normalise(h.chunk.text) for h in hits)


def retrieval_recall(sheets) -> dict:
    hits = total = 0
    for ticker, sheet in sheets.items():
        index = load_index(ticker)
        for fact in sheet.facts:
            if fact.quote.strip():
                total += 1
                hits += quote_in_hits(fact.quote, search(index, fact.question, k=8))
    return {"top8": share(hits, total)}


def labels_and_judges(memos) -> tuple[dict, dict]:
    sheet, key_file = EVALS / "labels" / "labelling-sheet.csv", EVALS / "labels" / "key.json"
    if not sheet.exists() or not key_file.exists():
        return {"status": "pending: labelling sheet not exported"}, {"status": "pending"}
    with sheet.open() as f:
        labels = read_labels(f)
    key = json.loads(key_file.read_text())
    per_writer = {}
    for writer in sorted({short_name(k["model"]) for k in key.values()}):
        rows = [labels[r] for r, k in key.items() if short_name(k["model"]) == writer and r in labels]
        cited = [x["citation_correct"] for x in rows if x["citation_correct"] is not None]
        per_writer[writer] = {"unsupported_rate": share(sum(x["verdict"] == "unsupported" for x in rows), len(rows)),
                              "partially_rate": share(sum(x["verdict"] == "partially_supported" for x in rows), len(rows)),
                              "citation_precision": share(sum(cited), len(cited))}
    calibration = {}
    for path in sorted((RESULTS / "judges").glob("*.json")):
        data = json.loads(path.read_text())
        common = [r for r in data["rows"] if r in labels]
        calibration[data["judge"]] = {
            "rows_judged": len(data["rows"]), "cost_usd": round(sum(r["cost_usd"] for r in data["rows"].values()), 4),
            **judge_agreement([labels[r]["verdict"] for r in common], [data["rows"][r]["verdict"] for r in common])}
    labelled = {"labelled_rows": len(labels), "sheet_rows": len(key), "per_writer": per_writer}
    return labelled, calibration


def seeded_errors() -> dict:
    out = {}
    for path in sorted((RESULTS / "seeded").glob("*.json")):
        data = json.loads(path.read_text())
        by_kind = {}
        for r in data["results"]:
            k = by_kind.setdefault(r["corruption"], {"n": 0, "code": 0, "judge_unsupported": 0, "judge_partial": 0, "missed": 0})
            k["n"] += 1
            if r["checked_by"] == "deterministic":
                k["code"] += 1
            elif r["verdict"] == "unsupported":
                k["judge_unsupported"] += 1
            elif r["verdict"] == "partially_supported":
                k["judge_partial"] += 1
            else:
                k["missed"] += 1
        out[data["judge"]] = by_kind
    return out


def scorecard_vs_agencies() -> dict:
    ratings = load_agency_ratings(EVALS / "agency_ratings.csv")
    if not ratings:
        return {"status": "pending: no agency ratings entered"}
    sb, agency, agree = [], [], 0
    for ticker, rows in ratings.items():
        cm = CompanyMetrics.model_validate_json((PUBLISHED / ticker / "metrics.json").read_text())
        if cm.scorecard.weighted_score is None:
            continue
        rank = company_rank(rows)
        sb.append(cm.scorecard.weighted_score)
        agency.append(rank)
        agree += bool(cm.scorecard.ig_like) == (rank <= IG_WORST_RANK)
    return {"spearman": spearman(sb, agency), "ig_hy_agreement": share(agree, len(sb)), "n": len(sb),
            "note": f"n = {len(sb)}: a small sample; the correlation is indicative only"}


def compute_results() -> dict:
    companies = load_companies()
    golden = [r["ticker"] for r in companies if r["golden"]]
    memos = load_eval_memos()
    sheets = golden_sheets()
    labelled, calibration = labels_and_judges(memos)
    prices = yaml.safe_load((CONFIG_DIR / "prices.yaml").read_text())
    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "command": COMMAND,
        "prices_read_on": prices["read_on"],
        "writers": writer_metrics(memos, golden),
        "memo_numeric_accuracy": memo_numeric_accuracy(memos, sheets),
        "engine_accuracy": engine_accuracy(sheets),
        "retrieval_recall": retrieval_recall(sheets),
        "labels": labelled,
        "judge_calibration": calibration,
        "seeded_errors": seeded_errors(),
        "scorecard_vs_agencies": scorecard_vs_agencies(),
    }


def _pct(s: dict | None) -> str:
    if not s or s.get("value") is None:
        return f"pending (n = {s.get('n', 0) if s else 0})"
    return f"{s['value']:.0%} (n = {s['n']})"


def _money(v) -> str:
    return "—" if v is None else f"${v:.3f}"


def render(results: dict) -> str:
    lines = ["# Evaluation results", "",
             f"Generated {results['generated_at']} by `{results['command']}` from saved outputs only (no model calls). "
             f"Costs at Sail list prices read {results['prices_read_on']} (asap tier). Every share shows its sample size n.",
             "", "## Per writer model (run 1, all companies; verification by the judge named)", "",
             "| Writer | Judge | Memos | Claims/memo | Judge: supported | partially | unsupported | Raw numbers rejected/memo "
             "| Repairs/memo | Cost/memo: drafting | verification | total | Model time/memo | Run-to-run supported share (golden) |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for writer, w in results["writers"].items():
        rr = w["run_to_run_judge_supported"]
        spread_text = (f"{rr['min']:.0%}–{rr['max']:.0%} over {rr['n']} runs" if rr.get("n") else "pending")
        lines.append(
            f"| {w['model']} | {w['judge']} | {w['memos_run1']} | {w['claims_per_memo']:.1f} | {_pct(w['judge_supported'])} | "
            f"{_pct(w['judge_partially'])} | {_pct(w['judge_unsupported'])} | {w['raw_numbers_rejected_per_memo']:.1f} | "
            f"{w['repairs_per_memo']:.1f} | {_money(w['cost_drafting_per_memo'])} | {_money(w['cost_verification_per_memo'])} | "
            f"{_money(w['cost_total_per_memo'])} | {w['model_seconds_per_memo']:.0f}s | {spread_text} |")
    if not results["writers"]:
        lines.append("| pending: no evaluation memos yet | | | | | | | | | | | | | |")
    lines += ["", "Judge verdicts are estimates until the judge is calibrated against the author's labels (below).",
              "", "## Memo numeric accuracy (golden set, run 1)", "",
              "| Writer | Engine figures equal to hand-verified value | Engine figures without a hand value | Quoted figures found in the cited passage |",
              "|---|---|---|---|"]
    for writer, m in results["memo_numeric_accuracy"].items():
        lines.append(f"| {writer} | {_pct(m['engine_figures'])} | {m['engine_figures_without_hand_value']} | "
                     f"{_pct(m['quoted_figures_in_cited_passage'])} |")
    e = results["engine_accuracy"]
    lines += ["", "## Engine numeric accuracy (golden sheets)", "",
              f"Accuracy (where the engine produced a value): {_pct(e['accuracy'])}. Coverage (share of hand-verified "
              f"items with an engine value): {_pct(e['coverage'])}. Per-row comparisons: evals/results/golden/.", "",
              "## Retrieval recall", "",
              f"Fact questions whose located passage is in the top eight results: {_pct(results['retrieval_recall']['top8'])}.",
              "", "## Author's labels", ""]
    labels = results["labels"]
    if "per_writer" in labels:
        lines.append(f"Labelled {labels['labelled_rows']} of {labels['sheet_rows']} rows.")
        lines += ["", "| Writer | Unsupported (my labels) | Partially supported | Citation precision |", "|---|---|---|---|"]
        for writer, w in labels["per_writer"].items():
            lines.append(f"| {writer} | {_pct(w['unsupported_rate'])} | {_pct(w['partially_rate'])} | {_pct(w['citation_precision'])} |")
    else:
        lines.append(labels["status"])
    lines += ["", "## Judge calibration", "", "| Judge | Rows judged | Agreement with my labels | False-pass rate | Cost |",
              "|---|---|---|---|---|"]
    for judge, j in results["judge_calibration"].items():
        if isinstance(j, dict) and "agreement" in j:
            lines.append(f"| {judge} | {j['rows_judged']} | {_pct(j['agreement'])} | {_pct(j['false_pass_rate'])} | ${j['cost_usd']:.3f} |")
    lines += ["", "False pass: the judge says supported where I said unsupported.", "",
              "## Seeded errors (share caught by each layer)", ""]
    for judge, kinds in results["seeded_errors"].items():
        lines += [f"Judge {judge}:", "", "| Corruption | n | Caught by code | Judge: unsupported | Judge: partially | Missed |",
                  "|---|---|---|---|---|---|"]
        for kind, k in kinds.items():
            lines.append(f"| {kind} | {k['n']} | {k['code']} | {k['judge_unsupported']} | {k['judge_partial']} | {k['missed']} |")
        lines.append("")
    s = results["scorecard_vs_agencies"]
    lines += ["## Scorecard against agency ratings", "",
              s.get("status") or f"Spearman rank correlation {s['spearman']:.2f}; IG/HY agreement {_pct(s['ig_hy_agreement'])}. {s['note']}."]
    return "\n".join(lines) + "\n"


def main() -> None:
    results = compute_results()
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "results.json").write_text(json.dumps(results, indent=1, default=str))
    (RESULTS / "results.md").write_text(render(results))
    print(f"written {(RESULTS / 'results.md').relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
