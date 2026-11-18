// What the source drawer can show: a metric's lineage, or a passage with the quote that was checked.
import type { Metric, Passage } from "./contracts/types";

export type DrawerSource =
  | { kind: "metric"; key: string; metric: Metric }
  | { kind: "passage"; chunkId: string; passage: Passage; quote?: string; verdict?: string; reason?: string };

export type OpenSource = (source: DrawerSource) => void;
