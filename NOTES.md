# Study notes

My study guide to Sourcebound. For each part of the system: the finance or regulatory concepts in plain
English, why the part is built the way it is, and the interview questions I should be able to answer, each
with a short model answer. Sections are added as each phase is built.

## 0. The project in one paragraph

A **credit memo** is the written case a bank analyst makes about whether a borrower can repay its debt.
Sourcebound drafts one for a US public company from its SEC filings. Deterministic, tested code computes
every figure; a language model writes the prose around those figures; three checks prove where each number
and claim came from; anything unproven goes on a checklist for a human reviewer.
