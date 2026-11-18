// What the source drawer can show: a metric's lineage, or a claim with its verdict and every passage it cites.
import type { MemoClaim, Metric, Passage } from "./contracts/types";

export type DrawerSource =
  | { kind: "metric"; key: string; metric: Metric }
  | { kind: "claim"; claim: MemoClaim; passages: Record<string, Passage>; judgeModel: string; focus?: string };

export type OpenSource = (source: DrawerSource) => void;
