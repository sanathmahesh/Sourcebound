# Model recommendation

**Status: provisional.** The figures that decide the choice (human labels and judge calibration) are pending
until the author labels the claim sample, so this memo sets out what has been measured and the rule for
choosing, not the final choice.

Source of every figure: `evals/results/results.json`, generated {{r:generated_at|text}} by
`uv run python -m sourcebound.evals.report` from the saved model outputs. Costs are at Sail list prices
read on {{r:prices_read_on|text}}. Each rate shows its sample size (n).

## Writers: accuracy, latency and cost per memo

{{table:writers}}

What the rows mean:

- *Judge: supported / partly / unsupported*: the share of all drafted claims each verdict was given, by the
  provisional judge (GLM-5.3). GLM-5.3 also judged its own writing here, which may favour it.
- *Quoted figures found in the cited passage*: figures the model copied from filing text, checked by code.
- *Engine figures matching hand-checked values* and the two *human labels* rows: pending until the author's golden
  sheets and claim labels are entered.
- *Raw numbers rejected*: figures the writer typed instead of using a placeholder, caught by code before
  publication.
- *Model time*: the sum of the model calls' latencies for one memo.
- *Run-to-run*: the golden five companies drafted three times, to show how much results vary between runs.

## Judges: agreement with human labels

{{table:judges}}

The false-pass rate is the dangerous error: of the claims the author labels unsupported, the share the judge
called supported.

## Seeded errors: which check catches what

{{table:seeded}}

By design, typed figures and citations moved without their quote are caught by code; negations, swapped
placeholders and citations moved together with a real quote depend on the judge. The table shows how that
worked in practice.

## Rule for choosing (proposed before the labels are in)

1. **Judge first.** Choose the candidate with the lower false-pass rate on the labelled sample; if they are
   close, prefer the higher agreement, then the lower cost.
2. **Then the writer.** Re-judge every writer's claims with the chosen judge (from the saved drafts, no new
   drafting). Drop any writer whose human-labelled unsupported-claim rate is clearly worse than the best, given
   the sample sizes. Among the rest, prefer lower cost per memo, then lower model time.
3. **Record the choice** in the decision log with the figures and their sample sizes, and update this memo.

Until then, GLM-5.3 is the provisional writer and judge (a setting chosen in phase 4, not a result).
