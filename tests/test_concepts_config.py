"""The concept chains in config/concepts.yaml load and are internally consistent."""

import pytest

from sourcebound.engine.concepts import load_concepts, parse_concepts
from sourcebound.paths import CONFIG_DIR


def test_production_config_loads():
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    for name in ["operating_income", "d_and_a", "interest_expense", "total_debt", "cash", "cfo", "capex"]:
        assert name in specs
        assert specs[name].required
    assert not specs["short_term_investments"].required
    assert specs["total_debt"].kind == "instant"
    assert specs["cfo"].kind == "flow"


def test_ranks_follow_list_order():
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    ranks = [c.rank for c in specs["interest_expense"].chain]
    assert ranks == list(range(1, len(ranks) + 1))
    assert specs["interest_expense"].chain[-1].flag.startswith("proxy")


def test_candidate_description():
    specs = load_concepts(CONFIG_DIR / "concepts.yaml")
    assert specs["total_debt"].chain[1].describe() == "LongTermDebtNoncurrent + [short_term_debt]"
    assert specs["d_and_a"].chain[0].describe() == "DepreciationDepletionAndAmortization"


def test_unknown_concept_reference_is_rejected():
    raw = {"x": {"label": "X", "kind": "flow", "required": True, "chain": [{"sum": [{"concept": "nope"}]}]}}
    with pytest.raises(ValueError, match="nope"):
        parse_concepts(raw)


def test_bad_kind_is_rejected():
    raw = {"x": {"label": "X", "kind": "weekly", "required": True, "chain": [{"tag": "A"}]}}
    with pytest.raises(ValueError, match="kind"):
        parse_concepts(raw)


def test_concept_reference_must_have_same_kind():
    raw = {
        "a": {"label": "A", "kind": "flow", "required": True, "chain": [{"sum": [{"concept": "b"}]}]},
        "b": {"label": "B", "kind": "instant", "required": True, "chain": [{"tag": "B"}]},
    }
    with pytest.raises(ValueError, match="kind"):
        parse_concepts(raw)
