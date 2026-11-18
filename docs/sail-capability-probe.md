# Sail capability probe

Run 2026-11-18 04:00 UTC against https://api.sailresearch.com/v1, service tier `asap`, reasoning effort `medium` (the writer setting), max_completion_tokens 2000. Command: `uv run python -m sourcebound.pipeline.capability_probe`. Raw responses: data/runs/.

| Model | Check | Result | Detail | Calls | Input / cached / output tokens | Cost (US$) | Seconds |
|---|---|---|---|---|---|---|---|
| zai-org/GLM-5.3 | structured output (json_schema, strict) | pass | ok | 1 | 29 / 28 / 36 | 0.00012 | 1.1 |
| zai-org/GLM-5.3 | strict function tool call | pass | ok | 1 | 207 / 206 / 22 | 0.00011 | 1.2 |
| zai-org/GLM-5.3 | tool call then structured answer, in one request setup | **FAIL** | turn 1 did not call the tool: expected one get_metric call, got [] (content '{"answer": "done", "number": 2}') | 1 | 245 / 244 / 14 | 0.00009 | 1.2 |
| zai-org/GLM-5.3 | tool call, then structured answer in a separate request | pass | ok | 2 | 245 / 244 / 22 + 108 / 0 / 18 | 0.00027 | 2.2 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | structured output (json_schema, strict) | pass | ok | 1 | 21 / 20 / 112 | 0.00031 | 5.1 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | strict function tool call | pass | ok | 1 | 332 / 331 / 66 | 0.00020 | 3.1 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | tool call then structured answer, in one request setup | **FAIL** | turn 1 did not call the tool: expected one get_metric call, got [] (content '{"answer": "done", "number": 0}') | 1 | 368 / 367 / 31 | 0.00010 | 3.1 |
| deepseek-ai/DeepSeek-V4-Pro-0813 | tool call, then structured answer in a separate request | pass | ok | 2 | 368 / 367 / 97 + 149 / 0 / 39 | 0.00053 | 6.2 |
| deepseek-ai/DeepSeek-V4.1-Flash-1017 | structured output (json_schema, strict) | pass | ok | 1 | 121 / 46 / 30 | 0.00002 | 1.1 |
| deepseek-ai/DeepSeek-V4.1-Flash-1017 | strict function tool call | pass | ok | 1 | 347 / 346 / 60 | 0.00002 | 3.1 |
| deepseek-ai/DeepSeek-V4.1-Flash-1017 | tool call then structured answer, in one request setup | pass | ok | 2 | 458 / 383 / 75 + 543 / 468 / 30 | 0.00005 | 4.2 |
| deepseek-ai/DeepSeek-V4.1-Flash-1017 | tool call, then structured answer in a separate request | pass | ok | 2 | 384 / 383 / 60 + 244 / 0 / 30 | 0.00005 | 6.2 |

Total probe cost at list price: US$0.0019.

## GET /v1/models, as returned

- `zai-org/GLM-5.3`: `{"created": 1700000000, "id": "zai-org/GLM-5.3", "input_modalities": ["text"], "object": "model", "owned_by": "zai-org", "pricing_usd_per_million_tokens": {"asap": {"cached_input": 0.18, "input": 0.98, "output": 3.08}, "balanced": {"cached_input": 0.12, "input": 0.5, "output": 2.5}, "flex": {"cached_input": 0.08, "input": 0.4, "output": 1.8}}, "shutdown_date": null}`
- `deepseek-ai/DeepSeek-V4-Pro-0813`: `{"created": 1700000000, "id": "deepseek-ai/DeepSeek-V4-Pro-0813", "input_modalities": ["text"], "object": "model", "owned_by": "deepseek-ai", "pricing_usd_per_million_tokens": {"asap": {"cached_input": 0.04, "input": 0.92, "output": 2.77}, "balanced": {"cached_input": 0.03, "input": 0.74, "output": 2.22}, "flex": {"cached_input": 0.02, "input": 0.46, "output": 1.39}}, "shutdown_date": null}`
- `deepseek-ai/DeepSeek-V4.1-Flash-1017`: `{"created": 1700000000, "id": "deepseek-ai/DeepSeek-V4.1-Flash-1017", "input_modalities": ["text", "image"], "object": "model", "owned_by": "deepseek-ai", "pricing_usd_per_million_tokens": {"asap": {"cached_input": 0.006, "input": 0.09, "output": 0.3}, "balanced": {"cached_input": 0.005, "input": 0.07, "output": 0.22}, "flex": {"cached_input": 0.004, "input": 0.05, "output": 0.15}}, "shutdown_date": null}`

Context windows and output limits: not reported by GET /v1/models (fields listed above); the models page (https://docs.sailresearch.com/models.md, read 17 November 2026) lists a 1M-token context for all three.
