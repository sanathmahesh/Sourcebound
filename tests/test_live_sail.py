"""Live smoke tests against Sail. Skipped by default; run with:  uv run pytest -m live"""

import pytest
from dotenv import load_dotenv

from sourcebound.llm.provider import LlmSettings, SailClient
from sourcebound.llm.schemas import DRAFT_FORMAT, SectionDraft, parse_json
from sourcebound.paths import ENV_FILE

pytestmark = pytest.mark.live


def test_writer_returns_a_valid_structured_draft():
    load_dotenv(ENV_FILE)
    settings = LlmSettings.from_env()
    reply = SailClient(settings).complete(
        model=settings.writer_model, max_completion_tokens=1000, reasoning_effort="low", response_format=DRAFT_FORMAT,
        messages=[{"role": "user", "content": "Return one qualitative claim with text 'Test claim.' and no citations."}])
    draft, error = parse_json(reply.content, SectionDraft)
    assert draft is not None, error
    assert reply.usage.output_tokens > 0
