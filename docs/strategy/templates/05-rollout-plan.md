# Rollout plan

How a bank could introduce a tool like Sourcebound safely. Thresholds are left for the model owner to set from
the calibration results; none is invented here.

## Stages

1. **Shadow.** A small pilot group writes memos as usual. The tool drafts the same memos in parallel, and the
   two are compared. Nothing from the tool reaches a credit committee.
2. **Assisted.** The tool's memo becomes the analyst's first draft. The analyst must work through the reviewer
   checklist and sign off; the memo the committee sees is the analyst's, with every figure still linked to its
   source.
3. **Wider use.** Extend sector by sector, starting with US public companies that file XBRL, the population the
   tool was tested on.

Each stage continues only if the monitoring below stays inside the limits set before the stage began.

## Pilot group

A few credit analysts and one reviewer, covering one sector of public borrowers, plus an independent
validator who did not build the tool and who challenges its design and results (effective challenge).

## The human review step

- Every unsupported or partly supported claim is fixed or removed before sign-off.
- Every checklist item (figure not available, fallback tag, blank taken as zero, stale data) is ticked by a named
  reviewer. In a bank, sign-off is recorded on a server with the reviewer's name, the time and the memo version;
  this prototype keeps it in one browser only.
- A second reviewer samples signed-off memos each month and labels their claims, which keeps the judge's error
  rate measured.

## What gets logged

- Every model request and response, with the model ID, prompt version, settings and price.
- The verification report for each memo: each figure's source, each claim's verdict and reason.
- The data date and the filings used.
- Checklist sign-offs and what the reviewer changed.
- Follow-up questions, answers and removed claims.
- Errors found after sign-off, with how they were found.

## What would trigger a rollback

- A wrong figure or claim found in a signed-off memo that the checks had marked verified.
- The judge's false-pass rate on the monthly labelled sample rising above the limit set from calibration.
- The share of claims removed or marked unsupported rising above its limit.
- The provider changing or retiring a model, its terms or its prices: re-run the evaluations before resuming.
- A provider outage longer than the business can wait: fall back to the manual process, which stays in place
  throughout the pilot.

Rollback means returning to the previous stage; the manual process is never switched off during the pilot.
