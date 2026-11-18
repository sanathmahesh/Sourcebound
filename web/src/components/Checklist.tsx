// The reviewer checklist: progress, items grouped by category with severity in words, and a "Go to" link
// for items that point at a place in the memo. Ticks are kept in this browser's localStorage only.
import { useState } from "react";
import type { ChecklistItem } from "../contracts/types";
import { SEVERITY } from "../format";

export const CATEGORY_LABEL: Record<ChecklistItem["category"], string> = {
  unsupported_claim: "Unsupported claim",
  partially_supported_claim: "Partially supported claim",
  draft_problem: "Draft problem",
  not_available: "Figure not available",
  fallback: "Fallback used",
  assumed_zero: "Blank taken as zero",
  override: "Data override",
  reconciliation: "Reconciliation warning",
  structural_change: "Structural change",
  provisional_grade: "Provisional grade",
  stale_data: "Stale data",
};

export type ChecklistLink = { id: string; label: string } | null;

export function readTicks(key: string): string[] {
  try {
    return JSON.parse(localStorage.getItem(key) ?? "[]");
  } catch {
    return [];
  }
}

function writeTicks(key: string, ids: string[]): void {
  try {
    localStorage.setItem(key, JSON.stringify(ids));
  } catch {
    // Storage blocked (private window): ticks last until the page closes.
  }
}

/** Scroll to an element below the sticky header and flash it for 2.2 seconds. */
export function jumpTo(elementId: string): void {
  const target = document.getElementById(elementId);
  if (!target) return;
  window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - 90, behavior: "smooth" });
  target.classList.add("flash");
  window.setTimeout(() => target.classList.remove("flash"), 2200);
}

interface Props {
  items: ChecklistItem[];
  storageKey: string;
  linkFor: (item: ChecklistItem) => ChecklistLink;
}

export function Checklist({ items, storageKey, linkFor }: Props) {
  const [ticked, setTicked] = useState<Set<string>>(() => new Set(readTicks(storageKey)));
  const toggle = (id: string) => {
    const next = new Set(ticked);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    setTicked(next);
    writeTicks(storageKey, [...next]);
  };
  const done = items.filter((i) => ticked.has(i.id)).length;
  const categories = (Object.keys(CATEGORY_LABEL) as ChecklistItem["category"][]).filter((c) => items.some((i) => i.category === c));
  return (
    <section className="block" aria-label="Reviewer checklist">
      <div className="block-head">
        <h2 className="serif-h2">Reviewer checklist</h2>
        <span className="mono small-14">{done} of {items.length} reviewed</span>
      </div>
      {items.length > 0 && (
        <div className="pips" aria-hidden="true" style={{ gridTemplateColumns: `repeat(${items.length}, 1fr)` }}>
          {items.map((item, n) => <div key={item.id} className={n < done ? "pip on" : "pip"} />)}
        </div>
      )}
      {items.length === 0 && <p className="muted">Nothing to review.</p>}
      {items.length > 0 && done === items.length && (
        <div role="status" className="signed">✓ Signed off. All {items.length} items reviewed.</div>
      )}
      {categories.map((category) => (
        <div key={category} className="ck-group">
          <h3 className="eyebrow ck-group-head">{CATEGORY_LABEL[category]}</h3>
          {items.filter((i) => i.category === category).map((item) => {
            const link = linkFor(item);
            const id = `ck-${item.id}`;
            return (
              <div key={item.id} className="ck-item">
                <input type="checkbox" id={id} checked={ticked.has(item.id)} onChange={() => toggle(item.id)} />
                <label htmlFor={id} className={ticked.has(item.id) ? "done" : ""}>
                  <span className="sev">{SEVERITY[item.severity]}</span>{item.message}
                </label>
                {link && (
                  <a href={`#${link.id}`} className="ck-go" onClick={(e) => { e.preventDefault(); jumpTo(link.id); }}>
                    Go to {link.label} ↑
                  </a>
                )}
              </div>
            );
          })}
        </div>
      ))}
      <p className="muted small">Sign-off is stored in this browser only.</p>
    </section>
  );
}
