"""Build and write the published metrics file for each company (data/published/companies/<T>/metrics.json).

Run:  uv run python -m sourcebound.pipeline.export          (all companies in config/companies.yaml)
      uv run python -m sourcebound.pipeline.export WMT GT   (some)

Also writes reports/coverage.md and reports/scorecard.md for the companies exported.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

from sourcebound import contracts as c
from sourcebound.edgar.client import EdgarError
from sourcebound.edgar.filings import filing_index_url
from sourcebound.engine.analysis import CompanyAnalysis
from sourcebound.engine.checklist import data_checklist
from sourcebound.engine.concepts import load_concepts
from sourcebound.engine.ladder import BUCKETS
from sourcebound.engine.ratios import Ratio
from sourcebound.engine.resolver import Resolved, SourceFact
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.pipeline.load import load_and_analyse, make_client
from sourcebound.scorecard.grid import Grid, load_grid
from sourcebound.scorecard.scoring import Scorecard, score_company

PUBLISHED_DIR = PROJECT_ROOT / "data" / "published"


def load_companies() -> list[dict]:
    return yaml.safe_load((CONFIG_DIR / "companies.yaml").read_text())["companies"]


def _status(status: str) -> str:
    """Resolver statuses map onto the contract's: an assumed-zero value is a value (with a note)."""
    return "ok" if status == "assumed_zero" else status


def _input(fact: SourceFact, analysis: CompanyAnalysis) -> c.MetricInput:
    return c.MetricInput(
        label=analysis.specs[fact.concept].label,
        concept=fact.concept,
        tag=fact.tag,
        fallback_rank=fact.fallback_rank,
        value=fact.value,
        unit=fact.unit,
        period=f"{fact.start} to {fact.end}" if fact.start else f"at {fact.end}",
        role=fact.role,
        sign=fact.sign,
        form=fact.form,
        accession=fact.accession,
        filed=fact.filed,
        url=fact.url,
    )


def _notes(r: Resolved) -> list[str]:
    notes = list(r.flags)
    if r.status == "assumed_zero":
        notes.append("assumed zero: not reported")
    if r.status == "not_available":
        notes.append(f"not available: {r.reason}")
    return notes


def metric_from_resolved(r: Resolved, analysis: CompanyAnalysis) -> c.Metric:
    return c.Metric(
        metric_id=r.concept,
        period=r.period,
        label=r.label,
        value=r.value,
        unit="USD",
        status=_status(r.status),
        formula=f"rank {r.fallback_rank}: {r.candidate}" if r.fallback_rank else "",
        notes=_notes(r),
        inputs=[_input(f, analysis) for f in r.inputs],
    )


def metric_from_ratio(ratio: Ratio, analysis: CompanyAnalysis) -> c.Metric:
    notes = [f"{ratio.status.replace('_', ' ')}: {ratio.reason}"] if ratio.status != "ok" and ratio.reason else []
    for inp in ratio.inputs:
        notes += [f"{inp.concept}: {note}" for note in _notes(inp)]
    return c.Metric(
        metric_id=ratio.metric_id,
        period=ratio.period,
        label=ratio.label,
        value=ratio.value,
        unit=ratio.unit,
        status=ratio.status,
        formula=ratio.formula,
        notes=notes,
        inputs=[_input(f, analysis) for inp in ratio.inputs for f in inp.inputs],
    )


def _scorecard(card: Scorecard) -> c.Scorecard:
    return c.Scorecard(
        basis=card.basis,
        grid_version=card.grid_version,
        factors=[c.ScorecardFactor(**vars(f)) for f in card.factors],
        weighted_score=card.weighted_score,
        grade=card.grade,
        provisional=card.provisional,
        ig_like=card.ig_like,
    )


def build_company_metrics(analysis: CompanyAnalysis, grid: Grid, sector: str) -> c.CompanyMetrics:
    metrics = {}
    for concept, by_period in analysis.values.items():
        for label, r in by_period.items():
            metrics[f"{concept}:{label}"] = metric_from_resolved(r, analysis)
    for metric_id, by_period in analysis.ratios.items():
        for label, ratio in by_period.items():
            metrics[f"{metric_id}:{label}"] = metric_from_ratio(ratio, analysis)

    sources = [analysis.latest_10k] + ([analysis.latest_10q] if analysis.latest_10q else [])
    ladder = None
    if analysis.ladder is not None:
        labels = dict(BUCKETS)
        ladder = c.MaturityLadder(
            as_of=analysis.periods["FY0"].end,
            buckets=[c.LadderBucket(id=b.concept, label=labels[b.concept], value=b.value, status=_status(b.status),
                                    metric_key=f"{b.concept}:FY0") for b in analysis.ladder.buckets],
            total=analysis.ladder.total,
            metric_keys=[f"{m.metric_id}:FY0" for m in analysis.ladder.metrics],
        )
    latest, fy0 = score_company(grid, analysis, "latest"), score_company(grid, analysis, "FY0")
    return c.CompanyMetrics(
        ticker=analysis.ticker,
        name=analysis.name,
        cik=analysis.cik,
        sector=sector,
        generated_at=datetime.now(timezone.utc).replace(microsecond=0),
        data_fetched_at=analysis.data_fetched_at,
        sources=[c.Source(form=f.form, accession=f.accession, period_end=f.report_date, filed=f.filed,
                          url=filing_index_url(analysis.cik, f.accession)) for f in sources],
        periods=[c.PeriodInfo(label=p.label, balance_sheet_date=p.end, note=p.note,
                              flow_windows=[f"{'+' if part.sign > 0 else '−'} {part.role}: {part.window}"
                                            for part in p.parts]) for p in analysis.periods.values()],
        period_problems=analysis.period_problems,
        metrics=metrics,
        trends=[c.TrendRow(**vars(t)) for t in analysis.trends],
        maturity_ladder=ladder,
        scorecard=_scorecard(latest),
        scorecard_fy0=_scorecard(fy0),
        checklist=data_checklist(analysis, [latest, fy0]),
        log=[c.LogItem(**vars(e)) for e in analysis.log],
    )


def write_company_metrics(metrics: c.CompanyMetrics, out_dir: Path = PUBLISHED_DIR) -> Path:
    path = out_dir / "companies" / metrics.ticker / "metrics.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(metrics.model_dump_json(indent=1) + "\n")
    return path


def main(tickers: list[str]) -> None:
    from sourcebound.pipeline.phase2_reports import write_coverage_report, write_scorecard_report

    companies = {row["ticker"]: row for row in load_companies()}
    tickers = tickers or list(companies)
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    grid = load_grid(CONFIG_DIR / "grid.yaml")
    client = make_client()
    exported = []
    for ticker in tickers:
        try:
            analysis = load_and_analyse(client, ticker, specs)
        except (ValueError, EdgarError) as exc:  # stop and report; never work around
            print(f"{ticker}: could not be analysed: {exc}")
            continue
        metrics = build_company_metrics(analysis, grid, companies[ticker]["sector"])
        path = write_company_metrics(metrics)
        exported.append((analysis, metrics))
        card = metrics.scorecard
        print(f"{ticker}: {card.grade} ({card.weighted_score:.2f}{', provisional' if card.provisional else ''}) -> "
              f"{path.relative_to(PROJECT_ROOT)}")
    write_coverage_report(exported)
    write_scorecard_report(exported)


if __name__ == "__main__":
    main([t.upper() for t in sys.argv[1:]])
