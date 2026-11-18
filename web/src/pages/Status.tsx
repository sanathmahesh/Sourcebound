// Loading and error states, and a memo's status, always in words and glyphs (never colour alone).
import type { IndexEntry } from "../contracts/types";

export function Loading({ what }: { what: string }) {
  return <div role="status" className="state-block muted">Loading {what}…</div>;
}

export function LoadError({ what }: { what: string }) {
  return (
    <div role="alert" className="state-block">
      <strong>✕ Could not load {what}.</strong>{" "}
      <span className="muted">The data file is missing or malformed. Reload to try again.</span>
    </div>
  );
}

const MEMO_STATUS: Record<IndexEntry["memo_status"], { text: string; className: string }> = {
  current: { text: "✓ Current", className: "" },
  stale: { text: "! Stale", className: "warn" },
  missing: { text: "○ No memo", className: "muted" },
};

export function MemoStatus({ status }: { status: IndexEntry["memo_status"] }) {
  const s = MEMO_STATUS[status];
  return <span className={s.className}>{s.text}</span>;
}
