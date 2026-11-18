# Model card

Sourcebound drafts a credit memo on a US public company from its SEC filings, and proves every figure and
claim against source data before a person reviews it. Educational project. Not investment advice. SB grades
are a student's stylized scorecard, not credit ratings.

## What is inside

- **Ratio engine** (deterministic code, no model): reads XBRL facts from SEC EDGAR, resolves each concept through
  a ranked list of tags, and computes the ratios, the maturity ladder and the SB scorecard. Every figure keeps
  its lineage: tag, period, form, accession number and filing date.
- **Retrieval**: filing text split into passages and searched with BM25, by section.
- **Writer model**: drafts each memo section as claims. Engine figures are written as placeholders that code
  fills in; a figure quoted from filing text must appear in the passage the claim cites.
- **Judge model**: a separate model call reads each claim with its cited passages and figures, and returns
  supported, partially supported or unsupported with a reason.
- **Follow-up box**: answers one question at a time with the same tools and checks; only claims the judge marks
  supported are shown, and the rest are listed as removed.
- Models are reached through Sail. The writer and the judge are both `zai-org/GLM-5.3`, the author's choice (see
  the model recommendation). Model IDs and prices are pinned in
  `config/models.yaml` and `config/prices.yaml` with the date they were read.

## Intended use

- A first draft for a credit analyst covering one of the fifteen companies in the portfolio, to be read,
  checked and edited by that analyst before any use.
- A demonstration of how generated text can be tied to source data: every figure clickable to its XBRL
  facts, every claim to its passage and verdict, and every doubt listed for sign-off.
- Teaching and interview preparation for the author.

## Out of scope

- Investment advice, or any decision to buy, sell or hold a security.
- A credit decision, a credit rating, or a substitute for one. An SB grade is a stylized scorecard.
- Companies outside the fifteen, private companies, and non-US filers.
- Any use without the human review below.
- Questions that are not about the chosen company's filings and credit profile; the follow-up box refuses them.

## Assumptions

The full list is in `ASSUMPTIONS.md`. The ones that matter most to a reader:

- A missing XBRL fact is shown as "not available" and never estimated; a few blanks are taken as zero and
  listed on the checklist.
- Last-twelve-months figures are built from the latest annual and quarterly filings; the maturity ladder is as
  of the last annual report.
- The judge's verdicts are estimates from a language model, not facts.

## Limitations

The full list is in `LIMITATIONS.md`. The ones that matter most to a reader:

- The judge can be wrong in both directions, and its error rate was never measured against human labels. The
  judge is the same model as the writer, so they may share blind spots.
- Figures can be correct but stale: a memo describes the filings it lists, and a newer filing marks it stale.
- XBRL tagging differs between companies; fallback tags and reconciliation warnings are listed, but a figure
  can still differ from what an analyst would take from the statements.
- Sign-off is kept in one browser; it is not an audit trail.

## Human review procedure

1. Check the memo date, the filings used and the stale banner. If the memo is stale, read the watchlist entry
   and treat the figures as of the date shown.
2. Work through the reviewer checklist from the top: unsupported and partially supported claims first, then
   figures not available, fallback tags, blanks taken as zero, reconciliation warnings and the provisional grade.
3. For every claim marked partially supported or unsupported, open its passages and decide whether to delete,
   rewrite or keep it with a note.
4. Open a sample of supported claims and computed figures and confirm them against the filing on EDGAR, using
   the links in the source panel.
5. Tick each checklist item only after acting on it. The memo is signed off when every item is ticked.
6. In a bank, record the reviewer, the time and the memo version on a server, and have a second person review
   the rating rationale. This prototype does neither.

## Evaluation

Measured results, with sample sizes, dates, model IDs and the command that reproduces them, are in
`RESULTS.md` and on the site's Results page. No human evaluation was done: the measures that needed human labels
or hand-checked values (numeric accuracy, citation precision, the unsupported-claim rate and the judge's error
rate) are marked "not measured".

## Monitoring

- A daily job checks EDGAR for new filings, recomputes the ratios, scorecard and flags, and marks memos stale.
  It makes no model call.
- Model IDs and prices are pinned with dates; any change of model means re-running the evaluation.
- The follow-up box is rate-limited per IP address at the edge, and each answer has a time limit.
