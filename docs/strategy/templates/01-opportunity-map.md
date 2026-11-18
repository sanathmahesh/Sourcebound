# Opportunity map

**Status: draft for the author's review.** The ratings below are judgment, not measurement, and the author is
expected to change them. No market statistics are used.

Where could a language-model tool help a bank's investment and lending teams? Each workflow is rated on three
things:

- **Value**: time saved and decisions improved if the tool works.
- **Feasibility**: whether the data can be reached and the output checked against a source, with public tools.
- **Risk**: the harm if an error goes unnoticed (High is worse).

| Workflow | Value | Feasibility | Risk | One-line reason |
|---|---|---|---|---|
| Credit memo drafting | High | High | Medium | Much of a review is assembling figures and filing text, which XBRL and filings provide in checkable form; errors reach a credit committee, so every figure must be traceable. |
| Financial spreading | High | Medium | Medium | Entering statements into the bank's template is repetitive; public filers have XBRL, but private borrowers send PDFs. |
| Covenant extraction and monitoring | High | Low | High | Covenants sit in long credit agreements with bespoke definitions, and a missed breach is costly. |
| Portfolio surveillance of filings | Medium | High | Low | New filings are easy to detect and ratios are deterministic; flags only prompt a human to look. |
| New-issue document summaries | Medium | Medium | Medium | Offering documents are long and often private; summaries help triage but need careful citation. |
| Committee reporting packs | Medium | Medium | Medium | Assembling packs is routine, but the inputs are internal data a public prototype cannot reach. |
| Peer comparison screens | Medium | High | Low | Ratios across peers come straight from XBRL; the judgment stays with the analyst. |
| Earnings call and news monitoring | Medium | High | Medium | Text is plentiful, but sources vary in reliability and timing. |
| Onboarding document checks | Medium | Medium | High | Document checks are repetitive, but mistakes have regulatory consequences. |

## Why credit memo drafting

- It joins structured data (XBRL facts, which can be checked exactly) with narrative (which must be grounded
  in quoted passages), so it exercises the whole control story: computed figures, quoted figures, an
  independent judge and a human sign-off.
- It needs only public data (SEC EDGAR), so the prototype handles no confidential information.
- Banks already have a human review step for memos (the analyst and the credit committee), so the tool fits an
  existing control rather than inventing one.
- Portfolio surveillance came along cheaply, because it reuses the same ratio engine with no model at all.

## What would change the ratings

Access to a bank's own data (private borrowers' statements, credit agreements, internal ratings) would raise
the feasibility of spreading, covenant monitoring and committee packs. Evidence from the timing log
(02-effort-comparison.md) would replace the value judgments with measured effort for the memo workflow.
