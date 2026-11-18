"""Token prices (config/prices.yaml) and the cost of a call."""

from pathlib import Path

import yaml

from sourcebound.llm.provider import Usage


def load_prices(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def call_cost(prices: dict, model: str, usage: Usage) -> float:
    """US$ for one call at list price. Raises KeyError for a model with no recorded price."""
    p = prices["models"][model]
    uncached = usage.input_tokens - usage.cached_input_tokens
    return (uncached * p["input"] + usage.cached_input_tokens * p["cached_input"] + usage.output_tokens * p["output"]) / 1e6
