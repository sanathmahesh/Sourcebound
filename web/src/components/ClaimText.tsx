// One claim: its text with figure chips, citation markers and the verdict, in words as well as style.
// Metric chips are computed from XBRL by the engine; quoted chips are copied from a filing passage.
import type { MemoClaim, Metric, Passage } from "../contracts/types";
import { VERDICT_LABEL } from "../format";
import type { OpenSource } from "../sources";

interface Props {
  claim: MemoClaim;
  metrics: Record<string, Metric>;
  passages: Record<string, Passage>;
  onOpen: OpenSource;
}

export function ClaimText({ claim, metrics, passages, onOpen }: Props) {
  const openPassage = (chunkId: string, quote?: string) => {
    const passage = passages[chunkId];
    if (passage) onOpen({ kind: "passage", chunkId, passage, quote, verdict: claim.verdict, reason: claim.judge_reason });
  };
  return (
    <span className={`claim claim-${claim.verdict}`} id={`claim-${claim.id}`}>
      {claim.segments.map((seg, n) => {
        if (seg.t === "metric" && seg.metric_id) {
          const metric = metrics[seg.metric_id];
          return (
            <button key={n} type="button" className="chip chip-metric" disabled={!metric}
              aria-label={`${seg.v}, computed from XBRL: show lineage`}
              onClick={() => metric && onOpen({ kind: "metric", key: seg.metric_id!, metric })}>
              {seg.v}<sup>XBRL</sup>
            </button>
          );
        }
        if (seg.t === "quoted" && seg.chunk_id) {
          return (
            <button key={n} type="button" className="chip chip-quoted"
              aria-label={`${seg.v}, quoted from the filing: show passage`} onClick={() => openPassage(seg.chunk_id!)}>
              {seg.v}<sup>quote</sup>
            </button>
          );
        }
        return <span key={n}>{seg.v}</span>;
      })}
      {claim.citations.map((cit, n) => (
        <button key={`c${n}`} type="button" className="cite" aria-label={`citation ${n + 1}: show passage`}
          onClick={() => openPassage(cit.chunk_id, cit.quote)}>[{n + 1}]</button>
      ))}{" "}
      <span className={`verdict verdict-${claim.verdict}`} title={claim.judge_reason}>{VERDICT_LABEL[claim.verdict]}</span>
    </span>
  );
}
