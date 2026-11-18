"""Build each company's search index from its filings, and the section-coverage report.

Run:  uv run python -m sourcebound.pipeline.build_index          (all companies)
      uv run python -m sourcebound.pipeline.build_index WMT VZ   (some)

Corpus per company (PLAN.md 4.7): the latest 10-K and every 10-Q filed after it. Each primary document is
downloaded (cached), turned into text, split into sections and chunks, and indexed with BM25. Writes
data/index/<TICKER>.json and reports/section-coverage.md.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

from sourcebound.edgar.client import EdgarClient, EdgarError
from sourcebound.edgar.filings import Filing, document_url, parse_filings, submissions_url
from sourcebound.edgar.html_text import html_to_text
from sourcebound.edgar.sections import Span, detect_sections
from sourcebound.engine.concepts import load_concepts
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT, REPORTS_DIR
from sourcebound.pipeline.load import load_and_analyse, make_client
from sourcebound.retrieval.chunking import FilingMeta, chunk_filing
from sourcebound.retrieval.index import CompanyIndex, build_company_index, save_index

TARGET_LABELS = {
    "10-K": ["business", "risk_factors", "mdna", "liquidity", "market_risk", "financial_statements", "debt_note"],
    "10-Q": ["financial_statements", "debt_note", "mdna", "liquidity", "market_risk", "risk_factors"],
}


@dataclass
class FilingCoverage:
    ticker: str
    meta: FilingMeta
    spans: list[Span]
    text_length: int
    chunk_counts: dict[str, int]


def corpus_filings(filings: list[Filing], latest_10k: Filing) -> list[Filing]:
    """The latest 10-K, then every original 10-Q filed after it, oldest first."""
    later = [f for f in filings if f.form == "10-Q" and f.filed > latest_10k.filed]
    return [latest_10k] + sorted(later, key=lambda f: (f.filed, f.accession))


def build_company(client: EdgarClient, ticker: str, specs) -> tuple[CompanyIndex, list[FilingCoverage]]:
    analysis = load_and_analyse(client, ticker, specs)
    filings = parse_filings(client.get_json(submissions_url(analysis.cik)))
    all_chunks, metas, coverage = [], [], []
    for f in corpus_filings(filings, analysis.latest_10k):
        url = document_url(analysis.cik, f)
        text = html_to_text(client.get_text(url))
        spans = detect_sections(text, f.form)
        meta = FilingMeta(analysis.ticker, f.accession, f.form, f.filed.isoformat(), f.report_date.isoformat(), url)
        chunks = chunk_filing(text, spans, meta)
        counts: dict[str, int] = {}
        for c in chunks:
            counts[c.section] = counts.get(c.section, 0) + 1
        all_chunks += chunks
        metas.append(meta)
        coverage.append(FilingCoverage(analysis.ticker, meta, spans, len(text), counts))
    return build_company_index(analysis.ticker, metas, all_chunks), coverage


def render_section_coverage(results: list[FilingCoverage]) -> str:
    lines = [
        "# Section coverage",
        "",
        "For each filing in each company's corpus: which sections were found, and how many passages each has.",
        "`n` = found, with n passages; `–` = not found (its text stays under its parent section or `unlabelled`).",
        "Labels come only from headings found in the text; nothing is guessed. Headings are listed below.",
        "",
        "| Ticker | Form | Period | business | risk_factors | mdna | liquidity | market_risk | "
        "financial_statements | debt_note | unlabelled share | passages |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    columns = ["business", "risk_factors", "mdna", "liquidity", "market_risk", "financial_statements", "debt_note"]
    for cov in results:
        targets = TARGET_LABELS["10-Q" if cov.meta.form.startswith("10-Q") else "10-K"]
        cells = []
        for label in columns:
            if label not in targets:
                cells.append("n/a")
            else:
                cells.append(str(cov.chunk_counts[label]) if cov.chunk_counts.get(label) else "–")
        unlabelled = sum(s.end - s.start for s in cov.spans if s.label == "unlabelled") / max(cov.text_length, 1)
        lines.append(
            f"| {cov.ticker} | {cov.meta.form} | {cov.meta.period_end} | " + " | ".join(cells)
            + f" | {unlabelled:.0%} | {sum(cov.chunk_counts.values())} |"
        )
    lines += ["", "## Headings found", ""]
    for cov in results:
        lines.append(f"### {cov.ticker} {cov.meta.form} {cov.meta.period_end} ({cov.meta.accession})")
        lines.append("")
        seen = set()
        for span in cov.spans:
            if span.label in ("unlabelled", "other_item") or span.label in seen:
                continue
            seen.add(span.label)
            lines.append(f"- {span.label}: \"{span.heading[:120]}\"")
        lines.append("")
    return "\n".join(lines) + "\n"


def main(tickers: list[str]) -> None:
    from sourcebound.pipeline.export import load_companies

    tickers = tickers or [c["ticker"] for c in load_companies()]
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    client = make_client()
    coverage: list[FilingCoverage] = []
    for ticker in tickers:
        try:
            index, filing_coverage = build_company(client, ticker, specs)
        except (ValueError, EdgarError) as exc:  # stop and report; never work around
            print(f"{ticker}: could not be indexed: {exc}")
            continue
        path = save_index(index)
        coverage += filing_coverage
        size = path.stat().st_size / 1e6
        print(f"{ticker}: {len(index.filings)} filings, {len(index.chunks)} passages -> "
              f"{path.relative_to(PROJECT_ROOT)} ({size:.1f} MB)")
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTS_DIR / "section-coverage.md").write_text(render_section_coverage(coverage))


if __name__ == "__main__":
    main([t.upper() for t in sys.argv[1:]])
