"""Generate, verify and publish a credit memo for one company.

Run:  uv run python -m sourcebound.pipeline.generate_memo WMT VZ GT
      uv run python -m sourcebound.pipeline.generate_memo WMT --writer deepseek-ai/DeepSeek-V4.1-Flash-1017

Fixed pipeline (decision D5), the same for every company:
1. For each of the first five sections: retrieve passages (fixed queries, section filter), draft with the
   writer (one repair allowed), then verify every claim (numbers, quotes, judge).
2. Rating rationale: the scorecard plus the claims verified as supported, with only their cited passages.
3. Assemble the memo (a dated snapshot with its own metrics and passages), the verification report and the
   reviewer checklist; write them with a readable Markdown copy and every raw request and response.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

from sourcebound import contracts as c
from sourcebound.llm.prices import call_cost, load_prices
from sourcebound.llm.provider import LlmResult, LlmSettings, SailClient
from sourcebound.memo.draft import SectionContext, draft_section
from sourcebound.memo.metric_table import build_table, rationale_keys, scorecard_context
from sourcebound.memo.render import period_phrases
from sourcebound.memo.retrieve import retrieve_for_section
from sourcebound.memo.sections import SECTION_SPECS
from sourcebound.paths import CONFIG_DIR, ENV_FILE, PROJECT_ROOT, REPORTS_DIR
from sourcebound.retrieval.chunking import Chunk
from sourcebound.retrieval.index import load_index
from sourcebound.verify.checklist import memo_checklist
from sourcebound.verify.claims import verify_claim

PUBLISHED_DIR = PROJECT_ROOT / "data" / "published"
RUNS_DIR = PROJECT_ROOT / "data" / "runs"


class RecordingClient:
    """Wraps the model client and keeps every request and result, labelled with the pipeline stage."""

    def __init__(self, inner) -> None:
        self.inner = inner
        self.stage = ""
        self.records: list[tuple[str, dict, LlmResult]] = []

    def complete(self, **request) -> LlmResult:
        result = self.inner.complete(**request)
        self.records.append((self.stage, request, result))
        return result


def _totals(records, prices: dict, prefix: str) -> c.CallTotals:
    chosen = [(req, res) for stage, req, res in records if stage.startswith(prefix)]
    return c.CallTotals(
        calls=len(chosen),
        input_tokens=sum(r.usage.input_tokens for _, r in chosen),
        cached_input_tokens=sum(r.usage.cached_input_tokens for _, r in chosen),
        output_tokens=sum(r.usage.output_tokens for _, r in chosen),
        cost_usd=round(sum(call_cost(prices, req["model"], r.usage) for req, r in chosen), 6),
        seconds=round(sum(r.seconds for _, r in chosen), 2),
    )


def _passage(chunk: Chunk) -> c.Passage:
    return c.Passage(text=chunk.text, section=chunk.section, form=chunk.form, filed=chunk.filed,
                     period_end=chunk.period_end, accession=chunk.accession, url=chunk.url,
                     start=chunk.start, end=chunk.end)


def _claims_for(spec_id, outcome, ctx, client, judge_model, effort, max_tokens) -> list[c.MemoClaim]:
    claims = []
    for n, draft_claim in enumerate(outcome.draft.claims, start=1):
        flags = [f"kept after failed repair: {p.split(': ', 1)[1]}" for p in outcome.problems
                 if p.startswith(f"claim {n}:")]
        client.stage = f"verify:{spec_id}-{n}"
        claim, _ = verify_claim(f"{spec_id}-{n}", draft_claim, ctx, client, model=judge_model,
                                reasoning_effort=effort, max_tokens=max_tokens, flags=flags)
        claims.append(claim)
    return claims


def generate_memo(ticker: str, client, *, settings: LlmSettings, prices: dict, writer_model: str | None = None,
                  judge_model: str | None = None, published_dir: Path = PUBLISHED_DIR, runs_dir: Path = RUNS_DIR,
                  reports_dir: Path = REPORTS_DIR, metrics_dir: Path | None = None) -> tuple[c.Memo, c.VerificationReport]:
    """metrics_dir: where metrics.json is read (default: published_dir); memo files go to published_dir."""
    config = yaml.safe_load((CONFIG_DIR / "models.yaml").read_text())
    efforts, limits = config["reasoning_effort"], config["max_completion_tokens"]
    writer, judge = writer_model or settings.writer_model, judge_model or settings.judge_model
    started = datetime.now(timezone.utc).replace(microsecond=0)
    company_dir = Path(published_dir) / "companies" / ticker
    metrics_file = Path(metrics_dir or published_dir) / "companies" / ticker / "metrics.json"
    cm = c.CompanyMetrics.model_validate_json(metrics_file.read_text())
    index = load_index(ticker)
    table, all_metrics = build_table(cm)
    periods = period_phrases(cm.periods)
    trends = [f"{t.label}: {t.direction}" for t in cm.trends]
    recorder = RecordingClient(client)
    sections: list[c.MemoSection] = []
    contexts: dict[str, SectionContext] = {}
    raw_rejections, repairs, failed = 0, 0, 0

    def run_section(spec, passages, rows, extra_trends, findings, notes, judge_evidence=()):
        nonlocal raw_rejections, repairs, failed
        ctx = SectionContext(spec, cm.name, rows, table, periods, passages, extra_trends, findings, list(judge_evidence))
        contexts[spec.id] = ctx
        recorder.stage = f"draft:{spec.id}"
        outcome = draft_section(recorder, model=writer, reasoning_effort=efforts["writer"],
                                max_tokens=limits["writer"], ctx=ctx)
        raw_rejections += sum("number not from a placeholder" in p for p in outcome.initial_problems)
        repairs += outcome.repaired
        claims = []
        if outcome.draft is None:
            failed += 1
            notes.append(f"no usable draft: {outcome.error}")
        else:
            if outcome.error:
                notes.append(outcome.error)
            claims = _claims_for(spec.id, outcome, ctx, recorder, judge, efforts["judge"], limits["judge"])
        sections.append(c.MemoSection(id=spec.id, title=spec.title, claims=claims,
                                      passages_shown=[p.id for p in passages], notes=notes))

    for spec in SECTION_SPECS[:-1]:
        passages, notes = retrieve_for_section(index, spec)
        rows = [table[k] for k in spec.metric_keys if k in table]
        run_section(spec, passages, rows, trends if spec.id == "financial_risk" else [], [], notes)

    # Rating rationale: the scorecard and the supported findings, with only the passages they cite.
    findings, cited = [], {}
    for section in sections:
        ctx = contexts[section.id]
        for claim in section.claims:
            if claim.verdict != "supported":
                continue
            ids = [cit.chunk_id for cit in claim.citations]
            findings.append("".join(s.v for s in claim.segments) + (f" [cites {', '.join(ids)}]" if ids else ""))
            cited |= {cid: ctx.shown()[cid] for cid in ids}
    card = cm.scorecard
    status, scorecard_evidence = scorecard_context(cm)
    rationale = SECTION_SPECS[-1]
    run_section(rationale, list(cited.values()), [table[k] for k in rationale_keys(cm) if k in table],
                status, findings, [], scorecard_evidence)

    # Assemble.
    run_id = f"{ticker}-{started:%Y%m%dT%H%M%SZ}-{writer.split('/')[-1]}"
    raw_path = Path(ticker) / f"{run_id}.jsonl"
    referenced, cited_chunks = set(), {}
    for section in sections:
        shown = contexts[section.id].shown()
        for claim in section.claims:
            referenced |= {s.metric_id for s in claim.segments if s.t == "metric"}
            for chunk_id in [s.chunk_id for s in claim.segments if s.t == "quoted"] + [x.chunk_id for x in claim.citations]:
                if chunk_id in shown:
                    cited_chunks[chunk_id] = shown[chunk_id]
    if cm.maturity_ladder:
        referenced |= {b.metric_key for b in cm.maturity_ladder.buckets} | set(cm.maturity_ladder.metric_keys)
    referenced |= {f"{f.id}:{f.period}" for f in card.factors if f.period}
    sources = {s.accession: s for s in cm.sources}
    for f in index.filings:
        sources.setdefault(f.accession, c.Source(form=f.form, accession=f.accession, period_end=f.period_end,
                                                 filed=f.filed, url=f.url))
    memo = c.Memo(
        ticker=ticker, name=cm.name, memo_date=started.date(), model=writer, judge_model=judge,
        grade=card.grade, grade_provisional=card.provisional, sources=list(sources.values()), sections=sections,
        metrics={k: all_metrics[k] for k in sorted(referenced) if k in all_metrics},
        passages={cid: _passage(ch) for cid, ch in sorted(cited_chunks.items())},
        trends=cm.trends, maturity_ladder=cm.maturity_ladder, scorecard=card,
        checklist=memo_checklist(cm.checklist, sections),
        run=c.RunInfo(run_id=run_id, started_at=started, writer_model=writer, judge_model=judge,
                      service_tier=settings.service_tier, reasoning_effort=efforts,
                      prices_read_on=str(prices.get("read_on", "")),
                      drafting=_totals(recorder.records, prices, "draft:"),
                      verification=_totals(recorder.records, prices, "verify:"),
                      raw_outputs=str(raw_path)),
    )
    claims = [(s, cl) for s in sections for cl in s.claims]
    report = c.VerificationReport(
        ticker=ticker, memo_date=memo.memo_date, writer_model=writer, judge_model=judge,
        summary=c.VerificationSummary(
            claims=len(claims),
            supported=sum(cl.verdict == "supported" for _, cl in claims),
            partially_supported=sum(cl.verdict == "partially_supported" for _, cl in claims),
            unsupported=sum(cl.verdict == "unsupported" for _, cl in claims),
            checked_by_judge=sum(cl.checked_by == "judge" for _, cl in claims),
            checked_deterministically=sum(cl.checked_by == "deterministic" for _, cl in claims),
            metric_figures=sum(seg.t == "metric" for _, cl in claims for seg in cl.segments),
            quoted_figures=sum(seg.t == "quoted" for _, cl in claims for seg in cl.segments),
            raw_numbers_rejected=raw_rejections, repairs=repairs, sections_without_draft=failed),
        numbers=[c.NumberTrace(claim_id=cl.id, kind=seg.t, value=seg.v, metric_id=seg.metric_id, chunk_id=seg.chunk_id)
                 for _, cl in claims for seg in cl.segments if seg.t in ("metric", "quoted")],
        claims=[c.ClaimCheck(claim_id=cl.id, section=s.id, kind=cl.kind, verdict=cl.verdict, checked_by=cl.checked_by,
                             reason=cl.judge_reason, citation_checks=[x.check for x in cl.citations], flags=cl.flags)
                for s, cl in claims],
        fallback_log=[entry for entry in cm.log if entry.kind in ("fallback", "assumed_zero", "not_available")],
        warnings=[entry for entry in cm.log if entry.severity == "warning"],
    )

    company_dir.mkdir(parents=True, exist_ok=True)
    (company_dir / "memo.json").write_text(memo.model_dump_json(indent=1) + "\n")
    (company_dir / "verification.json").write_text(report.model_dump_json(indent=1) + "\n")
    raw_file = Path(runs_dir) / raw_path
    raw_file.parent.mkdir(parents=True, exist_ok=True)
    with raw_file.open("w") as out:
        for stage, request, res in recorder.records:
            out.write(json.dumps({"stage": stage, "request": request, "response": res.raw,
                                  "usage": vars(res.usage), "cost_usd": call_cost(prices, request["model"], res.usage),
                                  "seconds": res.seconds, "attempts": res.attempts}, default=str) + "\n")
    from sourcebound.pipeline.memo_report import render_memo_markdown

    Path(reports_dir, "memos").mkdir(parents=True, exist_ok=True)
    Path(reports_dir, "memos", f"{ticker}.md").write_text(render_memo_markdown(memo, report))
    return memo, report


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate and verify credit memos.")
    parser.add_argument("tickers", nargs="+")
    parser.add_argument("--writer", help="writer model (default SAIL_MODEL_WRITER)")
    parser.add_argument("--judge", help="judge model (default SAIL_MODEL_JUDGE)")
    args = parser.parse_args()
    main_for([t.upper() for t in args.tickers], args.writer, args.judge)


def main_for(tickers: list[str], writer: str | None = None, judge: str | None = None) -> None:
    """Generate, verify and publish memos; each one is then recorded as current in state.json."""
    from sourcebound.pipeline.build_all import mark_memo_current

    load_dotenv(ENV_FILE)
    settings = LlmSettings.from_env()
    client = SailClient(settings)
    prices = load_prices(CONFIG_DIR / "prices.yaml")
    for ticker in tickers:
        memo, report = generate_memo(ticker, client, settings=settings, prices=prices,
                                     writer_model=writer, judge_model=judge)
        mark_memo_current(ticker)
        s, run = report.summary, memo.run
        print(f"{ticker}: {s.claims} claims: {s.supported} supported, {s.partially_supported} partly, "
              f"{s.unsupported} unsupported; {s.raw_numbers_rejected} raw numbers rejected; {s.repairs} repairs; "
              f"cost ${run.drafting.cost_usd + run.verification.cost_usd:.3f} "
              f"(drafting ${run.drafting.cost_usd:.3f}, verification ${run.verification.cost_usd:.3f}); "
              f"model time {run.drafting.seconds + run.verification.seconds:.0f}s")


if __name__ == "__main__":
    main()
