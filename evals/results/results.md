# Evaluation results

Generated 2026-11-18 07:51 UTC by `uv run python -m sourcebound.evals.report` from saved outputs only (no model calls). Costs at Sail list prices read 2026-11-17 (asap tier). Every share shows its sample size n.

## Per writer model (run 1, all companies; verification by the judge named)

| Writer | Judge | Memos | Claims/memo | Judge: supported | partially | unsupported | Raw numbers rejected/memo | Repairs/memo | Cost/memo: drafting | verification | total | Model time/memo | Run-to-run supported share (golden) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| deepseek-ai/DeepSeek-V4-Pro-0813 | zai-org/GLM-5.3 | 15 | 32.7 | 92% (n = 491) | 7% (n = 491) | 1% (n = 491) | 3.1 | 1.6 | $0.158 | $0.021 | $0.178 | 1365s | 89%–95% over 3 runs |
| deepseek-ai/DeepSeek-V4.1-Flash-1017 | zai-org/GLM-5.3 | 15 | 34.0 | 92% (n = 510) | 8% (n = 510) | 0% (n = 510) | 1.2 | 1.3 | $0.008 | $0.022 | $0.030 | 476s | 87%–88% over 3 runs |
| zai-org/GLM-5.3 | zai-org/GLM-5.3 | 15 | 35.1 | 86% (n = 526) | 13% (n = 526) | 1% (n = 526) | 2.3 | 2.1 | $0.081 | $0.026 | $0.107 | 251s | 78%–83% over 3 runs |

Judge verdicts are estimates until the judge is calibrated against the author's labels (below).

## Memo numeric accuracy (golden set, run 1)

| Writer | Engine figures equal to hand-verified value | Engine figures without a hand value | Quoted figures found in the cited passage |
|---|---|---|---|
| DeepSeek-V4-Pro-0813 | pending (n = 0) | 212 | 100% (n = 75) |
| DeepSeek-V4.1-Flash-1017 | pending (n = 0) | 276 | 100% (n = 23) |
| GLM-5.3 | pending (n = 0) | 280 | 100% (n = 65) |

## Engine numeric accuracy (golden sheets)

Accuracy (where the engine produced a value): pending (n = 0). Coverage (share of hand-verified items with an engine value): pending (n = 0). Per-row comparisons: evals/results/golden/.

## Retrieval recall

Fact questions whose located passage is in the top eight results: pending (n = 0).

## Author's labels

Labelled 0 of 180 rows.

| Writer | Unsupported (my labels) | Partially supported | Citation precision |
|---|---|---|---|
| DeepSeek-V4-Pro-0813 | pending (n = 0) | pending (n = 0) | pending (n = 0) |
| DeepSeek-V4.1-Flash-1017 | pending (n = 0) | pending (n = 0) | pending (n = 0) |
| GLM-5.3 | pending (n = 0) | pending (n = 0) | pending (n = 0) |

## Judge calibration

| Judge | Rows judged | Agreement with my labels | False-pass rate | Cost |
|---|---|---|---|---|
| deepseek-ai/DeepSeek-V4-Pro-0813 | 180 | pending (n = 0) | pending (n = 0) | $0.413 |
| zai-org/GLM-5.3 | 180 | pending (n = 0) | pending (n = 0) | $0.125 |

False pass: the judge says supported where I said unsupported.

## Seeded errors (share caught by each layer)

Judge deepseek-ai/DeepSeek-V4-Pro-0813:

| Corruption | n | Caught by code | Judge: unsupported | Judge: partially | Missed |
|---|---|---|---|---|---|
| negation | 60 | 0 | 57 | 0 | 3 |
| citation_swap | 43 | 43 | 0 | 0 | 0 |
| citation_swap_with_quote | 43 | 7 | 27 | 6 | 3 |
| raw_number | 24 | 24 | 0 | 0 | 0 |
| wrong_placeholder | 22 | 0 | 5 | 17 | 0 |

Judge zai-org/GLM-5.3:

| Corruption | n | Caught by code | Judge: unsupported | Judge: partially | Missed |
|---|---|---|---|---|---|
| negation | 60 | 0 | 54 | 4 | 2 |
| citation_swap | 43 | 43 | 0 | 0 | 0 |
| citation_swap_with_quote | 43 | 7 | 26 | 7 | 3 |
| raw_number | 24 | 24 | 0 | 0 | 0 |
| wrong_placeholder | 22 | 0 | 8 | 11 | 3 |

## Scorecard against agency ratings

pending: no agency ratings entered
