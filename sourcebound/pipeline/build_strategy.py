"""Render the strategy artifacts and publish the About page's documents.

Run:  uv run python -m sourcebound.pipeline.build_strategy

1. docs/strategy/templates/*.md -> docs/strategy/*.md, figures filled from evals/results/results.json and the
   timing log (sourcebound/strategy/render.py).
2. docs/method.md, generated from config/grid.yaml and the engine's formulas.
3. data/published/about.json: the six artifacts (the decision log is hand-written), the method and the
   limitations, as Markdown for the About page.
No model is called.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from sourcebound import contracts as c
from sourcebound.paths import CONFIG_DIR, PROJECT_ROOT
from sourcebound.scorecard.grid import load_grid
from sourcebound.strategy import render as r
from sourcebound.strategy.method import method_markdown
from sourcebound.strategy.timings import read_timings

PUBLISHED_DIR = PROJECT_ROOT / "data" / "published"
METHOD_FILE = PROJECT_ROOT / "docs" / "method.md"
METHOD_EXAMPLE = "WMT"  # any company: the formula strings are the same for all


def render_artifacts() -> dict[str, str]:
    """{file name: rendered Markdown} for every template; raises if a figure would be typed by hand."""
    results = json.loads(r.RESULTS_FILE.read_text())
    timings = read_timings(r.TIMINGS_FILE)
    rendered = {}
    for template in sorted(r.TEMPLATE_DIR.glob("*.md")):
        text, spans = r.render(template.read_text(), results, timings)
        stray = r.stray_numbers(text, spans)
        if stray:
            raise ValueError(f"{template.name}: figures typed by hand: {stray}")
        rendered[template.name] = r.HEADER.format(name=template.name) + text
    return rendered


def method_text(published_dir: Path = PUBLISHED_DIR) -> str:
    example = c.CompanyMetrics.model_validate_json(
        (published_dir / "companies" / METHOD_EXAMPLE / "metrics.json").read_text())
    return method_markdown(load_grid(CONFIG_DIR / "grid.yaml"), example)


def _title(markdown: str) -> str:
    return next(line[2:].strip() for line in markdown.splitlines() if line.startswith("# "))


def about_documents() -> list[c.AboutDocument]:
    sources = [(path, "strategy") for path in sorted(r.STRATEGY_DIR.glob("0*.md"))]
    sources += [(METHOD_FILE, "method"), (PROJECT_ROOT / "LIMITATIONS.md", "reference")]
    documents = []
    for path, group in sources:
        markdown = path.read_text()
        documents.append(c.AboutDocument(id=path.stem.lower(), title=_title(markdown), group=group,
                                         markdown=markdown, source=str(path.relative_to(PROJECT_ROOT))))
    return documents


def main() -> None:
    for name, text in render_artifacts().items():
        (r.STRATEGY_DIR / name).write_text(text)
        print(f"wrote docs/strategy/{name}")
    METHOD_FILE.write_text(method_text())
    print("wrote docs/method.md")
    about = c.AboutFile(generated_at=datetime.now(timezone.utc).replace(microsecond=0), documents=about_documents())
    (PUBLISHED_DIR / "about.json").write_text(about.model_dump_json(indent=1) + "\n")
    print(f"wrote data/published/about.json ({len(about.documents)} documents)")


if __name__ == "__main__":
    main()
