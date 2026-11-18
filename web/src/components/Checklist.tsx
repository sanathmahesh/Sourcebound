// The reviewer checklist: items grouped by category, each with a checkbox and a link to where it applies.
// Ticks are kept in this browser's localStorage only; nothing is sent anywhere.
import { useState } from "react";
import type { ChecklistItem } from "../contracts/types";

const CATEGORY_LABEL: Record<ChecklistItem["category"], string> = {
  unsupported_claim: "Unsupported claim",
  partially_supported_claim: "Partly supported claim",
  draft_problem: "Draft problem",
  not_available: "Figure not available",
  fallback: "Fallback tag used",
  assumed_zero: "Blank taken as zero",
  override: "Data override",
  reconciliation: "Reconciliation warning",
  structural_change: "Structural change",
  provisional_grade: "Provisional grade",
  stale_data: "Stale data",
};

function readTicks(key: string): string[] {
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

export function Checklist({ items, storageKey }: { items: ChecklistItem[]; storageKey: string }) {
  const [ticked, setTicked] = useState<Set<string>>(() => new Set(readTicks(storageKey)));
  const toggle = (id: string) => {
    const next = new Set(ticked);
    if (next.has(id)) next.delete(id);
    else next.add(id);
    setTicked(next);
    writeTicks(storageKey, [...next]);
  };
  const done = items.filter((i) => ticked.has(i.id)).length;
  const groups = [...new Set(items.map((i) => i.category))];
  return (
    <section className="checklist" aria-label="Reviewer checklist">
      <h2>Reviewer checklist</h2>
      <p>
        <strong>{done} of {items.length} reviewed</strong>
        {items.length > 0 && done === items.length && <span className="signed"> · Signed off</span>}
      </p>
      <p className="note">Sign-off is stored in this browser only.</p>
      {items.length === 0 && <p>Nothing to review.</p>}
      {groups.map((category) => (
        <div key={category}>
          <h3>{CATEGORY_LABEL[category]}</h3>
          <ul>
            {items.filter((i) => i.category === category).map((item) => (
              <li key={item.id}>
                <label>
                  <input type="checkbox" checked={ticked.has(item.id)} onChange={() => toggle(item.id)} />
                  {" "}<span className={`sev sev-${item.severity}`}>{item.severity}</span> {item.message}
                </label>
                {item.ref && <> <a href={`#claim-${item.ref}`} onClick={(e) => {
                  const target = document.getElementById(`claim-${item.ref}`);
                  if (target) { e.preventDefault(); target.scrollIntoView({ behavior: "smooth", block: "center" }); }
                }}>({item.ref})</a></>}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </section>
  );
}
