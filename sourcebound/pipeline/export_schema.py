"""Write the data contract as one JSON Schema file, which the frontend's TypeScript types are generated from.

Run:  uv run python -m sourcebound.pipeline.export_schema      (then: cd web && npm run gen:types)

contracts.py is the single source of the shapes. The published files are described as they are written
(serialization mode, so fields with defaults are always present); the request body of /api/ask is described
as it is accepted (validation mode). A test fails if the committed schema is out of date.
"""

from __future__ import annotations

import json

from pydantic.json_schema import models_json_schema

from sourcebound import contracts as c
from sourcebound.paths import PROJECT_ROOT

SCHEMA_FILE = PROJECT_ROOT / "web" / "src" / "contracts" / "schema.json"
PUBLISHED_MODELS = [c.SiteIndex, c.CompanyMetrics, c.Memo, c.VerificationReport, c.Watchlist, c.WatchState,
                    c.EvalsFile, c.AboutFile, c.AskResponse]


def contract_schema() -> dict:
    models = [(m, "serialization") for m in PUBLISHED_MODELS] + [(c.AskRequest, "validation")]
    _, schema = models_json_schema(models, title="Sourcebound data contract")
    return schema


def schema_text() -> str:
    return json.dumps(contract_schema(), indent=1, sort_keys=True) + "\n"


def main() -> None:
    SCHEMA_FILE.parent.mkdir(parents=True, exist_ok=True)
    SCHEMA_FILE.write_text(schema_text())
    print(f"wrote {SCHEMA_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
