# Sourcebound

A credit-analysis tool that drafts a credit memo on a US public company from its SEC filings and proves
every figure against source data. Educational project. Not investment advice.

Live: **https://sourcebound-app.vercel.app**

Status: all ten phases built and deployed (verified memos, model evaluation, the daily watchlist, the live
follow-up API, the strategy documents and the designed interface). Figures that need the author's labels and
hand-checked values are marked pending. See PLAN.md, RESULTS.md and MODEL_CARD.md.

## Setup

Requires [uv](https://docs.astral.sh/uv/) (it installs Python 3.12) and, for the interface, Node 22.

```bash
cp .env.example .env      # then set EDGAR_USER_AGENT to your name and email
uv sync
cd web && npm ci && cd ..
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
uv run python -m sourcebound.pipeline.export_schema    # data contract -> web/src/contracts/schema.json
uv run python -m sourcebound.pipeline.build_strategy   # strategy docs from templates + results, about.json
```

The site, locally (two terminals):

```bash
uv run --env-file .env uvicorn api.index:app --port 8000   # the live API (/api/ask costs a few cents a question)
cd web && npm run dev                                       # http://localhost:5173 (proxies /api to port 8000)
```

Frontend checks (in `web/`): `npm run gen:types` (TypeScript types from schema.json), `npm run check:types`,
`npm run typecheck`, `npm test`, `npm run build` (writes `web/dist/`, with the published JSON under `dist/data`).

## Deploy

`vercel.json` builds the Vite app as static files (with the published JSON under `/data`) and runs
`api/index.py`, the FastAPI app, as one Python function; `/api/*` is rewritten to it. The Vercel project is
`sourcebound`.

```bash
npx vercel@65.11.0 deploy --prod     # deploy this folder to production (pushes do not deploy by themselves; D61)
npx vercel@65.11.0 env ls            # server settings: SAIL_BASE_URL, SAIL_API_KEY (secret), SAIL_MODEL_WRITER,
                                     #   SAIL_MODEL_JUDGE, SAIL_SERVICE_TIER
npx vercel@65.11.0 firewall rules inspect "Rate limit follow-up questions"   # 10 per 10 minutes per IP on /api/ask
curl https://sourcebound-app.vercel.app/api/health
```

The daily watchlist (`.github/workflows/watchlist.yml`, 11:17 UTC) needs repository secrets: `EDGAR_USER_AGENT`
(your name and email, as in `.env`) and, to deploy new data, `VERCEL_TOKEN` (created in the Vercel dashboard),
`VERCEL_ORG_ID` and `VERCEL_PROJECT_ID`. Run it by hand from the Actions tab, or
`gh workflow run watchlist -f deploy=true` to force a deploy.

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
- RESULTS.md: measured results (generated). MODEL_CARD.md: intended use, limits and the review procedure.
- ASSUMPTIONS.md, LIMITATIONS.md, docs/strategy/06-decision-log.md.
