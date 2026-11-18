# Manual against tool-assisted effort

Does the tool save time without adding errors? This document holds the protocol, the log template and the
results. Every result comes from timings the author records in `evals/timings.csv`; none is estimated.

## Results

{{table:timings}}

"Errors found later" counts mistakes discovered afterwards, when the memo is checked against the author's
hand-verified golden sheet.

## Protocol

1. **Tasks.** (a) Write the six-section memo for one company from its latest 10-K and 10-Q. (b) Answer the five
   golden fact questions for one company.
2. **Conditions.** *Manual*: filings, a calculator and a blank memo outline only. *Tool-assisted*: start from
   Sourcebound's memo, work through the reviewer checklist, correct or remove anything wrong, and sign off.
3. **Companies.** Use a company in only one condition, so that knowing its filings from the first attempt does
   not speed up the second. Alternate which condition comes first from one company to the next.
4. **Timing.** Start when the first filing (or the memo) is opened; stop when the memo is complete (manual) or
   signed off (tool-assisted). Record whole minutes; note interruptions.
5. **Errors found later.** After both conditions, check each memo's figures and facts against the golden sheet
   and record the number of mistakes.
6. **Honesty.** Record every attempt, including abandoned or slow ones, with a note. Never round towards the
   expected answer.

## Log template

One row per timed task, in `evals/timings.csv`:

```
date,company,condition,task,start,end,minutes,errors found later,notes
```

`condition` is `manual` or `tool-assisted`; `task` is `memo` or `fact questions`.

## Limits of this comparison

One person (the author) does every task, so the results describe one analyst, not a team. Samples are small and
learning effects remain despite the counterbalancing. The comparison measures drafting and checking time only,
not the committee's review.
