// Generate src/contracts/types.ts from src/contracts/schema.json (written by the Python side:
// uv run python -m sourcebound.pipeline.export_schema). The Pydantic models are the single source of the
// shapes; these types follow them. With --check, fail if the committed types are out of date.
import { readFileSync, writeFileSync } from "node:fs";
import { compile } from "json-schema-to-typescript";

const schemaFile = new URL("../src/contracts/schema.json", import.meta.url);
const typesFile = new URL("../src/contracts/types.ts", import.meta.url);
const banner = "/* Generated from schema.json by scripts/gen-types.mjs (npm run gen:types). Do not edit by hand. */";

const schema = JSON.parse(readFileSync(schemaFile, "utf8"));
// Field titles ("Ticker", "Metric Id") would each become a named alias (Ticker3, MetricId5); drop them so
// fields get inline types. Model titles stay, so each model is one named interface.
for (const model of Object.values(schema.$defs)) {
  for (const field of Object.values(model.properties ?? {})) delete field.title;
}
const types = await compile(schema, "SourceboundDataContract", {
  bannerComment: banner,
  unreachableDefinitions: true,
  additionalProperties: false,
});

if (process.argv.includes("--check")) {
  if (readFileSync(typesFile, "utf8") !== types) {
    console.error("src/contracts/types.ts is out of date: run npm run gen:types");
    process.exit(1);
  }
  console.log("types.ts is current");
} else {
  writeFileSync(typesFile, types);
  console.log("wrote src/contracts/types.ts");
}
