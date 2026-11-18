# Risk and control table

Each way Sourcebound can fail, the control that catches it, the evidence that the control works, and the
matching term from the 2026 interagency model-risk guidance.

## Scope: what this table borrows, and what it does not claim

- The Federal Reserve, OCC and FDIC issued revised "Supervisory Guidance on Model Risk Management" on
  17 April 2026 (Fed SR 26-2, OCC Bulletin 2026-13, FDIC FIL-15-2026). For the Federal Reserve it replaces
  SR 11-7 (2011); the OCC and FDIC rescinded their own earlier versions.
- **This table borrows the guidance's vocabulary by choice.** It does not claim that the guidance applies to this
  project or that the project complies with it:
  - The guidance's "model" is a complex quantitative method applying statistical, economic or financial theory,
    and it "excludes simple arithmetic calculations ... as well as deterministic rule-based processes". The ratio
    engine is deterministic arithmetic, so it is not a model under this definition.
  - Its footnote 3 says generative AI and agentic AI models "are not within the scope of this guidance", and that
    a banking organization's own risk management and governance practices should determine controls for tools
    it does not cover. The writer, the judge and the follow-up loop are generative AI, so they are outside it.
  - It is expected to be most relevant to banking organizations with over $30 billion in total assets, and it
    "does not set forth enforceable standards or prescriptive requirements".
- For context only: OCC Bulletin 2026-54 (4 November 2026) gives OCC examiners a framework for banks' use of
  what it calls super intelligence, and states that it "does not establish supervisory expectations for banks".
  Its illustrative risk tiers list "internal document summarization for credit memos" in a moderate tier with
  mandatory human-in-the-loop review, which is how this tool is designed to be used.
- Sail (the model provider) is a third party. The interagency third-party risk-management guidance of June 2023
  (SR 23-4, OCC Bulletin 2023-17, FIL-29-2023) describes a life cycle of planning, due diligence and selection,
  contract negotiation, ongoing monitoring and termination. A replacement was proposed in September 2026 and is
  open for comment until 16 December 2026.

Evidence figures come from `evals/results/results.json` (generated {{r:generated_at|text}}), using the
provisional judge, zai-org/GLM-5.3. "Pending" figures need the author's golden values or claim labels.

## The table

| Failure mode | Control | Evidence it works | Guidance term (borrowed) |
|---|---|---|---|
| The engine picks the wrong XBRL fact (wrong tag, period or restated value) | Ranked fallback chains in config; period and year-to-date alignment checks; most recently filed value with restatements logged; fallbacks listed on the reviewer checklist | tests/test_resolver.py, tests/test_periods.py, tests/test_concepts_config.py; engine figures against hand-checked golden values: {{r:engine_accuracy>accuracy|rate}} | Model testing; documentation (the engine itself is not a model under the definition) |
| A missing figure is filled in with a guess | A missing fact is "not available", never estimated; it goes on the checklist | tests/test_ratios.py (`test_missing_input_is_not_available`), tests/test_periods.py (`test_missing_prior_year_is_reported_not_guessed`) | Model use: limitations |
| The writer types a wrong number | Engine figures are placeholders filled by code; any typed figure must appear in a cited passage | tests/test_number_and_quote_checks.py; raw numbers rejected per GLM-5.3 memo: {{r:writers>GLM-5.3>raw_numbers_rejected_per_memo|num1}}; seeded typed figures caught by code: {{r:seeded_errors>zai-org/GLM-5.3>raw_number>code|int}} of {{r:seeded_errors>zai-org/GLM-5.3>raw_number>n|int}} | Model development: conceptual soundness of the design; model testing |
| A quote is not in the passage it cites, or cites a passage the model never saw | Quote check against the cited passage; citations limited to passages shown | tests/test_number_and_quote_checks.py; seeded citations moved without their quote, caught by code: {{r:seeded_errors>zai-org/GLM-5.3>citation_swap>code|int}} of {{r:seeded_errors>zai-org/GLM-5.3>citation_swap>n|int}}; GLM-5.3 quoted figures found in the cited passage: {{r:memo_numeric_accuracy>GLM-5.3>quoted_figures_in_cited_passage|rate}} | Outcomes analysis |
| A claim overstates or contradicts its evidence | An independent judge reads each claim with its passages and metric values; partly supported and unsupported claims are marked and listed for review | Seeded negations judged unsupported: {{r:seeded_errors>zai-org/GLM-5.3>negation>judge_unsupported|int}} of {{r:seeded_errors>zai-org/GLM-5.3>negation>n|int}}; human-labelled unsupported-claim rate (GLM-5.3 writer): {{r:labels>per_writer>GLM-5.3>unsupported_rate|rate}} | Outcomes analysis; effective challenge |
| The judge passes an unsupported claim | Judge calibrated against a blind human-labelled sample; the judge is chosen by its false-pass rate; the reviewer checklist | GLM-5.3 false-pass rate: {{r:judge_calibration>zai-org/GLM-5.3>false_pass_rate|rate}}; agreement with labels: {{r:judge_calibration>zai-org/GLM-5.3>agreement|rate}} | Effective challenge; model validation |
| Writer and judge share a blind spot | Two judge candidates calibrated separately; seeded errors run through each | Seeded swapped placeholders missed by the GLM-5.3 judge: {{r:seeded_errors>zai-org/GLM-5.3>wrong_placeholder>missed|int}} of {{r:seeded_errors>zai-org/GLM-5.3>wrong_placeholder>n|int}}; by the DeepSeek-V4-Pro-0813 judge: {{r:seeded_errors>deepseek-ai/DeepSeek-V4-Pro-0813>wrong_placeholder>missed|int}} of {{r:seeded_errors>deepseek-ai/DeepSeek-V4-Pro-0813>wrong_placeholder>n|int}} | Aggregate risk |
| Results change from run to run | Fixed six-section pipeline; every request and response saved; run-to-run spread measured | GLM-5.3 share of claims judged supported across three runs: {{r:writers>GLM-5.3>run_to_run_judge_supported|spread}} | Ongoing model monitoring |
| A memo goes stale after a new filing | Daily job detects new filings, recomputes ratios and flags, and marks the memo stale until it is regenerated and reviewed | tests/test_watchlist.py (`test_new_filing_refreshes_flags_and_marks_the_memo_stale`); reports/watchlist-simulation.md | Ongoing model monitoring; model use |
| Output is used beyond its purpose (the SB grade read as a credit rating, or investment advice) | Disclaimer on every page; SB grades named as a stylized scorecard; the follow-up box refuses out-of-scope questions | tests/test_api.py (`test_out_of_scope_passes_through`); tests/test_scorecard.py (the scorecard never reads agency ratings) | Model use: intended purpose and limitations; statement of purpose |
| Unreviewed model text is published | The daily job makes no model call; memos are regenerated and reviewed by hand; live answers keep only supported claims and list the rest | tests/test_watchlist.py (`test_watchlist_code_imports_no_model_client`); tests/test_api.py (`test_claims_that_fail_verification_are_removed_with_the_reason`) | Governance and controls: roles and responsibilities |
| The provider changes, reprices or retires a model, or goes down | Model IDs and prices pinned in config with the date read; idempotent retries; plain "busy" and "unavailable" errors; saved outputs allow re-judging without new drafting | tests/test_llm_provider.py (`test_retries_reuse_the_same_idempotency_key`); tests/test_api.py (`test_provider_errors_map_to_plain_http_errors`); tests/test_replay.py | Vendor and other third-party products; third-party ongoing monitoring and termination |
| The API key leaks | Key only in .env and server environment variables; never printed or sent to the browser | tests/test_llm_provider.py (`test_settings_never_show_the_key`, `test_bad_request_is_not_retried_and_never_leaks_the_key`); a check of the built site before deploy | Governance and controls |
| Someone runs up the model bill through the public question box | Question length cap, bounded lookups, capped output tokens; a per-IP rate limit before production | tests/test_api.py (`test_bad_requests_get_400_with_a_plain_message`, `test_tool_loop_stops_after_three_rounds_then_asks_for_the_answer_without_tools`) | Governance and controls |
| Nobody can tell which model, prompt or data produced a memo | Each memo records its writer, judge, settings, price date, filings used and raw-output file; the decision log records every design choice | tests/test_published_contract.py (every published file matches its contract); docs/strategy/06-decision-log.md | Model inventory; documentation |

## What is missing

Pending figures need the author's golden values and claim labels. In a bank, the human sign-off would be recorded
on a server with the reviewer's name and time; here it stays in one browser. An independent validator, who
provides effective challenge, is part of the rollout plan, not of this prototype.
