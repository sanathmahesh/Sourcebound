# Results

Measured results only. Every figure here is filled in by code from `evals/results/results.json`, generated
{{r:generated_at|text}} by `uv run python -m sourcebound.evals.report`; none is typed by hand. Each figure
carries its sample size, and each column is one writer model, named by its exact model ID. Costs use the
provider's list prices read on {{r:prices_read_on|text}}.

Figures that need the author's hand-checked values or claim labels read "pending" until those exist. The judge
model's verdict shares are estimates (a language model grading another), so they are kept out of this file;
they are on the site's Results page and in the model recommendation.

## Per writer model

| Measure | `{{r:writers>DeepSeek-V4-Pro-0813>model|text}}` | `{{r:writers>DeepSeek-V4.1-Flash-1017>model|text}}` | `{{r:writers>GLM-5.3>model|text}}` |
|---|---|---|---|
| Numeric accuracy: computed figures matching the author's hand-checked values | {{r:memo_numeric_accuracy>DeepSeek-V4-Pro-0813>engine_figures|rate}} | {{r:memo_numeric_accuracy>DeepSeek-V4.1-Flash-1017>engine_figures|rate}} | {{r:memo_numeric_accuracy>GLM-5.3>engine_figures|rate}} |
| Citation precision: citations the author labelled correct | {{r:labels>per_writer>DeepSeek-V4-Pro-0813>citation_precision|rate}} | {{r:labels>per_writer>DeepSeek-V4.1-Flash-1017>citation_precision|rate}} | {{r:labels>per_writer>GLM-5.3>citation_precision|rate}} |
| Unsupported-claim rate: claims the author labelled unsupported | {{r:labels>per_writer>DeepSeek-V4-Pro-0813>unsupported_rate|rate}} | {{r:labels>per_writer>DeepSeek-V4.1-Flash-1017>unsupported_rate|rate}} | {{r:labels>per_writer>GLM-5.3>unsupported_rate|rate}} |
| Quoted figures found in the cited passage (code check) | {{r:memo_numeric_accuracy>DeepSeek-V4-Pro-0813>quoted_figures_in_cited_passage|rate}} | {{r:memo_numeric_accuracy>DeepSeek-V4.1-Flash-1017>quoted_figures_in_cited_passage|rate}} | {{r:memo_numeric_accuracy>GLM-5.3>quoted_figures_in_cited_passage|rate}} |
| Cost per memo, drafting and judging, at list prices | {{r:writers>DeepSeek-V4-Pro-0813>cost_total_per_memo|usd3}} (n = {{r:writers>DeepSeek-V4-Pro-0813>memos_run1|int}} memos) | {{r:writers>DeepSeek-V4.1-Flash-1017>cost_total_per_memo|usd3}} (n = {{r:writers>DeepSeek-V4.1-Flash-1017>memos_run1|int}} memos) | {{r:writers>GLM-5.3>cost_total_per_memo|usd3}} (n = {{r:writers>GLM-5.3>memos_run1|int}} memos) |
| Model time per memo, drafting and judging | {{r:writers>DeepSeek-V4-Pro-0813>model_seconds_per_memo|sec0}} (n = {{r:writers>DeepSeek-V4-Pro-0813>memos_run1|int}} memos) | {{r:writers>DeepSeek-V4.1-Flash-1017>model_seconds_per_memo|sec0}} (n = {{r:writers>DeepSeek-V4.1-Flash-1017>memos_run1|int}} memos) | {{r:writers>GLM-5.3>model_seconds_per_memo|sec0}} (n = {{r:writers>GLM-5.3>memos_run1|int}} memos) |
| Typed figures rejected per first draft (code check) | {{r:writers>DeepSeek-V4-Pro-0813>raw_numbers_rejected_per_memo|num1}} (n = {{r:writers>DeepSeek-V4-Pro-0813>memos_run1|int}} memos) | {{r:writers>DeepSeek-V4.1-Flash-1017>raw_numbers_rejected_per_memo|num1}} (n = {{r:writers>DeepSeek-V4.1-Flash-1017>memos_run1|int}} memos) | {{r:writers>GLM-5.3>raw_numbers_rejected_per_memo|num1}} (n = {{r:writers>GLM-5.3>memos_run1|int}} memos) |

## How each figure is measured

- **Numeric accuracy**: each computed figure in the golden-set memos is compared with the value the author
  checked by hand against the filing. Pending until the golden-set sheets are filled in.
- **Citation precision** and **unsupported-claim rate**: from a blind sample of claims the author labels without
  seeing the judge's verdict. Pending until the labels are entered.
- **Quoted figures found in the cited passage**: every figure the writer quoted from filing text is searched
  for in the passage its claim cites, by code.
- **Cost** and **model time**: summed from the saved provider responses for each first-run memo, then averaged.
  Every writer's memos were judged by `{{r:writers>GLM-5.3>judge|text}}`, and the judging is included.
- **Typed figures rejected**: digits a writer typed instead of using a placeholder, which the validator
  rejected before any repair.

## Reproduce

```
uv run python -m sourcebound.evals.report           # recompute results.json from the saved runs
uv run python -m sourcebound.pipeline.build_strategy # re-render this file
```
