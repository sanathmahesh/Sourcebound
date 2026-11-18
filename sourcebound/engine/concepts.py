"""Load the concept fallback chains from config/concepts.yaml.

A "concept" is a financial item the ratios need (e.g. total debt). Companies report the same item under
different us-gaap tags, so each concept has a ranked chain of candidates: the resolver uses the first
candidate the company actually reports for the period. See the comments in config/concepts.yaml.
"""

from dataclasses import dataclass
from pathlib import Path

import yaml

KINDS = {"flow", "instant"}


@dataclass(frozen=True)
class Component:
    """One part of a candidate: a us-gaap tag, or another concept resolved through its own chain."""

    tag: str | None = None
    concept: str | None = None
    optional: bool = False
    negate: bool = False  # use minus the reported value (for tags reported as negative, e.g. net interest)

    def describe(self) -> str:
        name = self.tag if self.tag else f"[{self.concept}]"
        return f"−{name}" if self.negate else name


@dataclass(frozen=True)
class Candidate:
    rank: int
    components: tuple[Component, ...]
    flag: str | None = None

    def describe(self) -> str:
        """Human-readable form, e.g. 'LongTermDebtNoncurrent + [short_term_debt]'."""
        return " + ".join(c.describe() for c in self.components)


@dataclass(frozen=True)
class ConceptSpec:
    name: str
    label: str
    kind: str  # "flow" or "instant"
    required: bool
    chain: tuple[Candidate, ...]


def load_concepts(path: Path) -> dict[str, ConceptSpec]:
    return parse_concepts(yaml.safe_load(path.read_text()))


def parse_concepts(raw: dict) -> dict[str, ConceptSpec]:
    """Build ConceptSpecs from the parsed YAML and check that they are consistent."""
    specs = {}
    for name, body in raw.items():
        if body.get("kind") not in KINDS:
            raise ValueError(f"{name}: kind must be one of {sorted(KINDS)}, got {body.get('kind')!r}")
        chain = tuple(_parse_candidate(rank, entry) for rank, entry in enumerate(body["chain"], start=1))
        specs[name] = ConceptSpec(
            name=name,
            label=body["label"],
            kind=body["kind"],
            required=bool(body["required"]),
            chain=chain,
        )
    _check_references(specs)
    return specs


def _parse_candidate(rank: int, entry: dict) -> Candidate:
    if "tag" in entry:
        components = (Component(tag=entry["tag"], negate=bool(entry.get("negate", False))),)
    else:
        components = tuple(
            Component(
                tag=c.get("tag"),
                concept=c.get("concept"),
                optional=bool(c.get("optional", False)),
                negate=bool(c.get("negate", False)),
            )
            for c in entry["sum"]
        )
    return Candidate(rank=rank, components=components, flag=entry.get("flag"))


def _check_references(specs: dict[str, ConceptSpec]) -> None:
    """Every `concept:` component must name a known concept of the same kind (flow or instant)."""
    for spec in specs.values():
        for candidate in spec.chain:
            for component in candidate.components:
                if component.concept is None:
                    continue
                target = specs.get(component.concept)
                if target is None:
                    raise ValueError(f"{spec.name}: refers to unknown concept {component.concept!r}")
                if target.kind != spec.kind:
                    raise ValueError(f"{spec.name}: refers to {target.name}, which has a different kind")
