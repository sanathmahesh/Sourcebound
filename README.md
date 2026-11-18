# Sourcebound

A credit-analysis tool that drafts a credit memo on a US public company from its SEC filings and proves
every figure against source data. Educational project. Not investment advice.

Status: phase 6 of 10 (verified memos, model evaluation, daily watchlist and the published data). See PLAN.md.

## Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12).

```bash
cp .env.example .env      # then set EDGAR_USER_AGENT to your name and email
uv sync
```

## Run

```bash
uv run pytest                                          # all tests; no network
uv run python -m sourcebound.pipeline.export           # all 15: data/published/companies/*/metrics.json,
                                                       #   reports/scorecard.md, reports/coverage.md
uv run python -m sourcebound.pipeline.ratio_report     # per-company check reports -> reports/ratios/
uv run python -m sourcebound.pipeline.tag_discovery WMT VZ  # which tags companies report -> reports/tag-discovery.md
uv run python -m sourcebound.pipeline.golden_templates # blank golden-set sheets (never overwrites)
uv run python -m sourcebound.pipeline.build_index      # filing text -> data/index/<T>.json, reports/section-coverage.md
uv run python -m sourcebound.pipeline.search WMT "revolving credit facility" --section liquidity -k 5
uv run python -m sourcebound.pipeline.capability_probe # what each Sail model supports -> docs/sail-capability-probe.md
uv run python -m sourcebound.pipeline.generate_memo WMT VZ GT   # memos -> data/published/, reports/memos/ (costs credit)
uv run pytest -m live                                  # live smoke test against Sail (costs a fraction of a cent)
uv run python -m sourcebound.evals.report              # evaluation results from saved outputs -> evals/results/results.md
uv run python -m sourcebound.pipeline.build_all --memos-from evals/results/memos/GLM-5.3/run1   # data/published/
uv run python -m sourcebound.watchlist.run             # the daily job: new filings -> metrics, flags, stale memos
uv run python -m sourcebound.watchlist.simulate VZ     # simulated new filing on a copy of data/published
```

Model calls need SAIL_* variables in `.env` (see `.env.example`); the key is never printed or committed.

Add tickers to `export` or `ratio_report` to run a subset. Config: `config/concepts.yaml` (tag chains),
`config/grid.yaml` (scorecard, frozen as `grid-v1`), `config/overrides.yaml` (approved per-company
exceptions), `config/companies.yaml`.

The first run downloads three files per company from EDGAR into `data/raw/` (gitignored); later runs read
the cache. Delete `data/raw/` to download fresh data.

## Documents

- PLAN.md: the plan. CLAUDE.md: ground rules.
- NOTES.md: study notes, concepts and interview questions.
- evals/README.md: what you fill in by hand (golden sheets, agency ratings).
- ASSUMPTIONS.md, LIMITATIONS.md, docs/strategy/06-decision-log.md.
