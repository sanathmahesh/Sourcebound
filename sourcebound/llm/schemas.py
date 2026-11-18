"""What the models must return: JSON schemas sent with each request, and Pydantic models that check replies.

The schemas are written out by hand (no $ref), the plainest form for strict structured output.
"""

from __future__ import annotations

import json
import re
from typing import Literal

from pydantic import BaseModel, ConfigDict, ValidationError


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class DraftCitation(_Strict):
    chunk_id: str
    quote: str


class DraftClaim(_Strict):
    kind: Literal["quantitative", "qualitative"]
    text: str
    citations: list[DraftCitation]


class SectionDraft(_Strict):
    claims: list[DraftClaim]


class AskAnswer(_Strict):
    """The follow-up endpoint's final answer: memo-shaped claims, or out_of_scope with none."""

    status: Literal["ok", "out_of_scope"]
    claims: list[DraftClaim]


class JudgeVerdict(_Strict):
    verdict: Literal["supported", "partially_supported", "unsupported"]
    reason: str
    evidence_quote: str


_CITATION = {
    "type": "object",
    "properties": {"chunk_id": {"type": "string"}, "quote": {"type": "string"}},
    "required": ["chunk_id", "quote"],
    "additionalProperties": False,
}
DRAFT_SCHEMA = {
    "type": "object",
    "properties": {
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "kind": {"type": "string", "enum": ["quantitative", "qualitative"]},
                    "text": {"type": "string"},
                    "citations": {"type": "array", "items": _CITATION},
                },
                "required": ["kind", "text", "citations"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["claims"],
    "additionalProperties": False,
}
JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["supported", "partially_supported", "unsupported"]},
        "reason": {"type": "string"},
        "evidence_quote": {"type": "string"},
    },
    "required": ["verdict", "reason", "evidence_quote"],
    "additionalProperties": False,
}
ASK_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["ok", "out_of_scope"]},
        "claims": DRAFT_SCHEMA["properties"]["claims"],
    },
    "required": ["status", "claims"],
    "additionalProperties": False,
}
DRAFT_FORMAT = {"type": "json_schema", "json_schema": {"name": "section_draft", "strict": True, "schema": DRAFT_SCHEMA}}
ASK_FORMAT = {"type": "json_schema", "json_schema": {"name": "ask_answer", "strict": True, "schema": ASK_SCHEMA}}
JUDGE_FORMAT = {"type": "json_schema", "json_schema": {"name": "judge_verdict", "strict": True, "schema": JUDGE_SCHEMA}}


def parse_json(content: str | None, model: type[BaseModel]) -> tuple[BaseModel | None, str]:
    """(parsed, "") or (None, what was wrong). Tolerates a ```json fence around the object."""
    text = (content or "").strip()
    fenced = re.match(r"^```(?:json)?\s*(.*?)\s*```$", text, re.DOTALL)
    if fenced:
        text = fenced.group(1)
    try:
        return model.model_validate(json.loads(text)), ""
    except json.JSONDecodeError as exc:
        return None, f"not valid JSON ({exc.msg})"
    except ValidationError as exc:
        first = exc.errors()[0]
        return None, f"not valid against the schema ({'.'.join(str(p) for p in first['loc'])}: {first['msg']})"
