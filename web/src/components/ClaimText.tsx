// One claim: its text with boxed figure chips, then its verdict as a bordered label (glyph and words).
// Metric chips are computed from XBRL by the engine; quoted chips, in curly quotes, are copied from a filing
// passage. Every claim in a memo was checked, so every claim carries its verdict, whatever its kind.
import type { MemoClaim, Metric, Passage } from "../contracts/types";
import { VERDICT } from "../format";
import type { OpenSource } from "../sources";

interface Props {
  claim: MemoClaim;
  metrics: Record<string, Metric>;
  passages: Record<string, Passage>;
  judgeModel: string;
  onOpen: OpenSource;
}

export function ClaimText({ claim, metrics, passages, judgeModel, onOpen }: Props) {
  const openClaim = (focus?: string) => onOpen({ kind: "claim", claim, passages, judgeModel, focus });
  const verdict = VERDICT[claim.verdict];
  return (
    <span className={`claim claim-${claim.verdict}`} id={`claim-${claim.id}`}>
      {claim.segments.map((seg, n) => {
        if (seg.t === "metric" && seg.metric_id) {
          const metric = metrics[seg.metric_id];
          const missing = !metric || metric.status === "not_available";
          return (
            <button key={n} type="button" className={`chip chip-metric${missing ? " chip-na" : ""}`} disabled={!metric}
              title="Computed from XBRL. Show formula and inputs."
              aria-label={`${seg.v}, computed from XBRL: show formula and inputs`}
              onClick={() => metric && onOpen({ kind: "metric", key: seg.metric_id!, metric })}>
              {seg.v}
            </button>
          );
        }
        if (seg.t === "quoted" && seg.chunk_id) {
          return (
            <button key={n} type="button" className="chip chip-quoted" title="Quoted from filing text. Show passage."
              aria-label={`${seg.v}, quoted from the filing: show passage`} onClick={() => openClaim(seg.chunk_id!)}>
              “{seg.v}”
            </button>
          );
        }
        return <span key={n} className="claim-text">{seg.v}</span>;
      })}
      <button type="button" className={`verdict verdict-${claim.verdict}`}
        title={`Show passage and verdict: ${verdict.words}`}
        aria-label={`Verdict: ${verdict.words}. Show the passage and the judge's reason`} onClick={() => openClaim()}>
        {verdict.glyph} {verdict.words}
      </button>
    </span>
  );
}

/** A claim's text without chips, as one string: quoted figures keep their curly quotes. */
export function claimPlainText(claim: MemoClaim): string {
  return claim.segments.map((s) => (s.t === "quoted" ? `“${s.v}”` : s.v)).join("");
}
