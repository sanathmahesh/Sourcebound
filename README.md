# Sourcebound

A credit-analysis tool that drafts a credit memo on a US public company from its SEC filings and proves
every figure against source data. Educational project. Not investment advice.

Status: phase 1 of 10 (foundations, and four core ratios for Walmart, Verizon and Goodyear). See PLAN.md.

## Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12).

```bash
cp .env.example .env      # then set EDGAR_USER_AGENT to your name and email
uv sync
```

## Run

```bash
uv run pytest                                              # all tests; no network
uv run python -m sourcebound.pipeline.ratio_report WMT VZ GT   # ratios with their source facts -> reports/ratios/
uv run python -m sourcebound.pipeline.tag_discovery WMT VZ GT  # which tags each company reports -> reports/tag-discovery.md
```

The first run downloads three files per company from EDGAR into `data/raw/` (gitignored); later runs read
the cache. Delete `data/raw/` to download fresh data.

## Documents

- PLAN.md: the plan. CLAUDE.md: ground rules.
- NOTES.md: study notes, concepts and interview questions.
- ASSUMPTIONS.md, LIMITATIONS.md, docs/strategy/06-decision-log.md.
