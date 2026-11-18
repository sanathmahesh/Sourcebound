<!-- Generated from docs/templates/RESULTS.md by `uv run python -m sourcebound.pipeline.build_strategy`. Edit the template, not this file. -->

# Results

Measured results only. Every figure here is filled in by code from `evals/results/results.json`, generated
2026-11-18 07:51 UTC by `uv run python -m sourcebound.evals.report`; none is typed by hand. Each figure
carries its sample size, and each column is one writer model, named by its exact model ID. Costs use the
provider's list prices read on 2026-11-17.

Figures that need the author's hand-checked values or claim labels read "pending" until those exist. The judge
model's verdict shares are estimates (a language model grading another), so they are kept out of this file;
they are on the site's Results page and in the model recommendation.

## Per writer model

| Measure | `deepseek-ai/DeepSeek-V4-Pro-0813` | `deepseek-ai/DeepSeek-V4.1-Flash-1017` | `zai-org/GLM-5.3` |
|---|---|---|---|
| Numeric accuracy: computed figures matching the author's hand-checked values | pending (n = 0) | pending (n = 0) | pending (n = 0) |
| Citation precision: citations the author labelled correct | pending (n = 0) | pending (n = 0) | pending (n = 0) |
| Unsupported-claim rate: claims the author labelled unsupported | pending (n = 0) | pending (n = 0) | pending (n = 0) |
| Quoted figures found in the cited passage (code check) | 100.0% (n = 75) | 100.0% (n = 23) | 100.0% (n = 65) |
| Cost per memo, drafting and judging, at list prices | $0.178 (n = 15 memos) | $0.030 (n = 15 memos) | $0.107 (n = 15 memos) |
| Model time per memo, drafting and judging | 1365 s (n = 15 memos) | 476 s (n = 15 memos) | 251 s (n = 15 memos) |
| Typed figures rejected per first draft (code check) | 3.1 (n = 15 memos) | 1.2 (n = 15 memos) | 2.3 (n = 15 memos) |

## How each figure is measured

- **Numeric accuracy**: each computed figure in the golden-set memos is compared with the value the author
  checked by hand against the filing. Pending until the golden-set sheets are filled in.
- **Citation precision** and **unsupported-claim rate**: from a blind sample of claims the author labels without
  seeing the judge's verdict. Pending until the labels are entered.
- **Quoted figures found in the cited passage**: every figure the writer quoted from filing text is searched
  for in the passage its claim cites, by code.
- **Cost** and **model time**: summed from the saved provider responses for each first-run memo, then averaged.
  Every writer's memos were judged by `zai-org/GLM-5.3`, and the judging is included.
- **Typed figures rejected**: digits a writer typed instead of using a placeholder, which the validator
  rejected before any repair.

## Reproduce

```
uv run python -m sourcebound.evals.report           # recompute results.json from the saved runs
uv run python -m sourcebound.pipeline.build_strategy # re-render this file
```
