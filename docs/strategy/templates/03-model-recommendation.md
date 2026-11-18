# Model recommendation

**Decision: `zai-org/GLM-5.3` as both writer and judge**, chosen by the author on 18 November 2026 (D62). No human
evaluation was done (the claim sample was never labelled and no hand-checked figures were entered), so the choice
rests on what code measured, below, not on human labels. Figures that needed those labels read "not measured".

Source of every figure: `evals/results/results.json`, generated {{r:generated_at|text}} by
`uv run python -m sourcebound.evals.report` from the saved model outputs. Costs are at Sail list prices
read on {{r:prices_read_on|text}}. Each rate shows its sample size (n).

## Writers: accuracy, latency and cost per memo

{{table:writers}}

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

{{table:judges}}

Not measured: calibration needed the author's labels. The false-pass rate would be the dangerous error: of the
claims a person labels unsupported, the share the judge called supported.

## Seeded errors: which check catches what

{{table:seeded}}

By design, typed figures and citations moved without their quote are caught by code; negations, swapped
placeholders and citations moved together with a real quote depend on the judge. The table shows how that
worked in practice.

## Why GLM-5.3

- **Speed.** It had the lowest model time per memo of the three writers: {{r:writers>GLM-5.3>model_seconds_per_memo|sec0}},
  against {{r:writers>DeepSeek-V4.1-Flash-1017>model_seconds_per_memo|sec0}} and {{r:writers>DeepSeek-V4-Pro-0813>model_seconds_per_memo|sec0}}. The same model answers the live
  question box, where waiting time matters.
- **Cost.** {{r:writers>GLM-5.3>cost_total_per_memo|usd3}} per memo, between {{r:writers>DeepSeek-V4.1-Flash-1017>cost_total_per_memo|usd3}} and {{r:writers>DeepSeek-V4-Pro-0813>cost_total_per_memo|usd3}}.
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
