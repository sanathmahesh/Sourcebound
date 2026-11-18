<!-- Generated from docs/strategy/templates/03-model-recommendation.md by `uv run python -m sourcebound.pipeline.build_strategy`. Edit the template, not this file. -->

# Model recommendation

**Decision: `zai-org/GLM-5.3` as both writer and judge**, chosen by the author on 18 November 2026 (D62). No human
evaluation was done (the claim sample was never labelled and no hand-checked figures were entered), so the choice
rests on what code measured, below, not on human labels. Figures that needed those labels read "not measured".

Source of every figure: `evals/results/results.json`, generated 2026-11-18 07:51 UTC by
`uv run python -m sourcebound.evals.report` from the saved model outputs. Costs are at Sail list prices
read on 2026-11-17. Each rate shows its sample size (n).

## Writers: accuracy, latency and cost per memo

| Measure | DeepSeek-V4-Pro-0813 | DeepSeek-V4.1-Flash-1017 | GLM-5.3 |
|---|---|---|---|
| Model ID | deepseek-ai/DeepSeek-V4-Pro-0813 | deepseek-ai/DeepSeek-V4.1-Flash-1017 | zai-org/GLM-5.3 |
| Memos drafted (first run) | 15 | 15 | 15 |
| Claims per memo | 32.7 | 34.0 | 35.1 |
| Judge: supported | 92.3% (n = 491) | 91.6% (n = 510) | 85.9% (n = 526) |
| Judge: partly supported | 7.1% (n = 491) | 8.0% (n = 510) | 13.5% (n = 526) |
| Judge: unsupported | 0.6% (n = 491) | 0.4% (n = 510) | 0.6% (n = 526) |
| Quoted figures found in the cited passage | 100.0% (n = 75) | 100.0% (n = 23) | 100.0% (n = 65) |
| Engine figures matching hand-checked values | not measured (n = 0) | not measured (n = 0) | not measured (n = 0) |
| Unsupported-claim rate (human labels) | not measured (n = 0) | not measured (n = 0) | not measured (n = 0) |
| Citation precision (human labels) | not measured (n = 0) | not measured (n = 0) | not measured (n = 0) |
| Raw numbers rejected per memo | 3.1 | 1.2 | 2.3 |
| Repairs per memo | 1.6 | 1.3 | 2.1 |
| Cost per memo (USD, list price) | $0.178 | $0.030 | $0.107 |
| Model time per memo | 1365 s | 476 s | 251 s |
| Run-to-run: judge supported | 91.4% (89.3% to 94.6%, 3 runs) | 87.7% (87.1% to 88.3%, 3 runs) | 80.9% (77.8% to 83.4%, 3 runs) |

What the rows mean:

- *Judge: supported / partly / unsupported*: the share of all drafted claims each verdict was given, by the
  judge (GLM-5.3). These are estimates by a language model, and GLM-5.3 also judged its own writing here.
- *Quoted figures found in the cited passage*: figures the model copied from filing text, checked by code.
- *Engine figures matching hand-checked values* and the two *human labels* rows: not measured, because no golden
  sheets or claim labels were entered.
- *Raw numbers rejected*: figures the writer typed instead of using a placeholder, caught by code before
  publication.
- *Model time*: the sum of the model calls' latencies for one memo.
- *Run-to-run*: the golden five companies drafted three times, to show how much results vary between runs.

## Judges: agreement with human labels

| Judge | Claims judged | Agreement with human labels | False-pass rate | Cost (USD) |
|---|---|---|---|---|
| deepseek-ai/DeepSeek-V4-Pro-0813 | 180 | not measured (n = 0) | not measured (n = 0) | $0.4128 |
| zai-org/GLM-5.3 | 180 | not measured (n = 0) | not measured (n = 0) | $0.1248 |

Not measured: calibration needed the author's labels. The false-pass rate would be the dangerous error: of the
claims a person labels unsupported, the share the judge called supported.

## Seeded errors: which check catches what

| Judge | Error planted | n | Caught by code | Judge: unsupported | Judge: partly | Missed |
|---|---|---|---|---|---|---|
| deepseek-ai/DeepSeek-V4-Pro-0813 | negation | 60 | 0 of 60 | 57 of 60 | 0 of 60 | 3 of 60 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | citation swap | 43 | 43 of 43 | 0 of 43 | 0 of 43 | 0 of 43 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | citation swap with quote | 43 | 7 of 43 | 27 of 43 | 6 of 43 | 3 of 43 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | raw number | 24 | 24 of 24 | 0 of 24 | 0 of 24 | 0 of 24 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | wrong placeholder | 22 | 0 of 22 | 5 of 22 | 17 of 22 | 0 of 22 |
| zai-org/GLM-5.3 | negation | 60 | 0 of 60 | 54 of 60 | 4 of 60 | 2 of 60 |
| zai-org/GLM-5.3 | citation swap | 43 | 43 of 43 | 0 of 43 | 0 of 43 | 0 of 43 |
| zai-org/GLM-5.3 | citation swap with quote | 43 | 7 of 43 | 26 of 43 | 7 of 43 | 3 of 43 |
| zai-org/GLM-5.3 | raw number | 24 | 24 of 24 | 0 of 24 | 0 of 24 | 0 of 24 |
| zai-org/GLM-5.3 | wrong placeholder | 22 | 0 of 22 | 8 of 22 | 11 of 22 | 3 of 22 |

By design, typed figures and citations moved without their quote are caught by code; negations, swapped
placeholders and citations moved together with a real quote depend on the judge. The table shows how that
worked in practice.

## Why GLM-5.3

- **Speed.** It had the lowest model time per memo of the three writers: 251 s,
  against 476 s and 1365 s. The same model answers the live
  question box, where waiting time matters.
- **Cost.** $0.107 per memo, between $0.030 and $0.178.
- **Nothing to redo.** The published memos were drafted and verified with it, so keeping it needs no new model calls.
- **The figure checks do not depend on the choice.** For every writer, quoted figures were found in their cited
  passages and typed figures were caught by code before publication (see the rows above).
- **Not used to rank:** the judged-supported shares, which are one model's estimates, and the human-label
  measures, which were not collected.

## How the choice would be revisited

If claim labels are collected later:

1. **Judge first.** Choose the candidate with the lower false-pass rate on the labelled sample; if they are
   close, prefer the higher agreement, then the lower cost.
2. **Then the writer.** Re-judge every writer's claims with the chosen judge (from the saved drafts, no new
   drafting). Drop any writer whose human-labelled unsupported-claim rate is clearly worse than the best, given
   the sample sizes. Among the rest, prefer lower cost per memo, then lower model time.
3. **Record the choice** in the decision log with the figures and their sample sizes, and update this memo.
