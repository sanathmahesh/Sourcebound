# Sourcebound: ground rules

Copied verbatim from section 2 of planning/03-opus-prompt.md. The full plan is in PLAN.md.

1. Build phase by phase, in the order in the plan. Within a phase, write the tests first, then the code.
   Commit when the phase's tests pass. Do not write code for a later phase early.
2. Stop after each phase and wait for my go-ahead. Your stop report must contain:
   (a) what you built; (b) the exact commands to run it; (c) what I should check by hand;
   (d) the real test output, including any failures; (e) assumptions and limitations added, and every
   fallback used; (f) what to read in NOTES.md; (g) questions and any scope changes you propose.
3. Never invent or silently substitute data.
   - If EDGAR, Sail, Vercel or any other source is unavailable or returns something unexpected, stop and
     ask me.
   - A missing XBRL fact is reported as "not available". It is never estimated, interpolated or copied
     from another period.
   - Financial values may be hardcoded only in test fixtures captured from real EDGAR responses, with the
     accession number recorded beside them.
   - Never fill in anything I am meant to supply: golden-set values, claim labels, agency ratings, timings.
4. Do not change the scope without asking. Put proposals in the stop report.
5. The language model never does arithmetic. Every figure comes from deterministic, tested code.
6. Keep ASSUMPTIONS.md, LIMITATIONS.md, NOTES.md and docs/strategy/06-decision-log.md current, updated in
   the same commit as the change that prompts them.
7. NOTES.md is my study guide. For each part of the system it holds: each finance or regulatory concept in
   plain English; why the part is built the way it is; and the interview questions I should be able to
   answer about it, each with a short model answer.
8. Secrets live only in .env (gitignored) and in server environment variables. Never commit, print or log
   them, and never let them reach the frontend. If I paste a key into chat, tell me to rotate it.
9. Follow SEC EDGAR fair-access rules: a declared User-Agent, a request rate well under the limit, and a
   cache for everything.
10. Outward-facing actions need my explicit go-ahead each time: creating or pushing to a remote, deploying,
    changing GitHub or Vercel settings.
11. The external facts in the plan were checked on 17 November 2026. Before you rely on one (Sail API
    behaviour and prices, Vercel limits, SEC endpoints, supervisory guidance), re-read the source and tell
    me if it has changed.
12. RESULTS.md and the strategy artifacts contain only measured numbers. Each number carries its sample
    size, date, model ID and the command that reproduces it. Estimates are labelled as estimates and kept
    out of RESULTS.md.
13. Write plainly: small functions, type hints, docstrings that say what and why. No abstractions without
    a second use.
14. This repo is standalone and shares nothing with any other project.
