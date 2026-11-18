# Decision log

Each entry: the decision, why, and the alternatives rejected. Entries D1–D10 are seeded from PLAN.md
section 4.2 (fixed before building started, 17 November 2026). Later entries were made while building and
say which phase made them. Where the plan named no rejected alternative, the entry says so rather than
inventing one.

## Fixed in the plan (PLAN.md 4.2)

### D1. Backend Python 3.12, FastAPI, pandas, pytest; frontend React, Vite, TypeScript
- **Why:** mainstream, readable stacks that the author can explain; Python is the natural home for
  financial data handling and evaluation code; FastAPI runs as a Vercel Python function.
- **Rejected:** none recorded in the plan.

### D2. Inference through Sail Research, behind one interface configured by environment variables
- **Why:** an OpenAI-compatible API giving access to several open-weight models from different labs at
  low list prices, with paid credit already in place. One interface means the model is a config value.
- **Rejected:** the Claude API (the plan fixes Sail as the provider).

### D3. Three writer models: zai-org/GLM-5.3, deepseek-ai/DeepSeek-V4-Pro-0813, deepseek-ai/DeepSeek-V4.1-Flash-1017
- **Why:** two mid-priced models from different labs and one very cheap one, so the recommendation can
  show a cost-against-accuracy trade-off.
- **Rejected:** none recorded in the plan.

### D4. Numbers by placeholder
- **Decision:** the model writes tokens such as `{{m:net_leverage:LTM}}` and code substitutes the value.
- **Why:** a figure the model never types cannot be mistyped; every printed number traces to the engine.
- **Rejected:** letting the model copy numbers from a table, because copying errors are silent.

### D5. The memo is a fixed pipeline, not an agent
- **Why:** the same retrieval steps every time make the memo auditable and repeatable. Only the live
  follow-up endpoint uses a bounded tool loop (two read-only tools, at most three rounds), because
  questions are open-ended.
- **Rejected:** an agentic memo writer that chooses its own lookups (not auditable or repeatable).

### D6. Retrieval: our own BM25 plus routing by filing section; index shipped as JSON files
- **Why:** Sail serves no embedding model; BM25 is small enough to explain line by line and needs no
  second vendor. Retrieval recall is measured in the evals; embeddings are proposed only if measured
  recall is poor.
- **Rejected for now:** local embeddings (large serverless bundle, slow cold starts); a second embedding
  vendor (a second key and provider).

### D7. Hosting: Vercel Hobby, own project, static frontend plus FastAPI as a Python function
- **Why:** free tier, CDN for static JSON, one Python function for the live endpoint. Nothing is held in
  memory between requests; memos, verification reports and the watchlist are generated ahead of time and
  shipped as static JSON with filing dates shown.
- **Rejected:** none recorded in the plan.

### D8. Watchlist refresh: a daily GitHub Actions job with no model call; memo marked stale until regenerated locally and reviewed
- **Why:** the Sail key stays only in Vercel and on the author's laptop, and no memo is published without
  human review, which matches the project's own control story.
- **Rejected:** Vercel Cron (functions cannot write files); automatic memo regeneration (publishes
  unreviewed output).

### D9. Rate limiting: a Vercel Firewall rate-limit rule keyed by IP on /api/ask
- **Why:** no database needed.
- **Rejected:** none recorded in the plan.

### D10. Interface designed separately in Claude Design
- **Decision:** build the data contract first, then a plain placeholder interface, then implement the
  handed-off design in a later phase.
- **Why:** the contract is the stable part; the design can change without touching the engine.
- **Rejected:** none recorded in the plan.

## Made while building
