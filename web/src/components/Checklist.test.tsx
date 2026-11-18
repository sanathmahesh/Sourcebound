import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import type { ChecklistItem } from "../contracts/types";
import { Checklist } from "./Checklist";

const items: ChecklistItem[] = [
  { id: "ck-1", category: "unsupported_claim", severity: "warning", message: "Claim risk-4 is unsupported.", ref: "risk-4" },
  { id: "ck-2", category: "fallback", severity: "info", message: "Debt used a fallback tag.", ref: "total_debt" },
];
const linkFor = (item: ChecklistItem) => (item.ref === "risk-4" ? { id: "claim-risk-4", label: "risk-4" } : null);

afterEach(() => { cleanup(); localStorage.clear(); });

describe("Checklist", () => {
  it("counts progress and shows signed off when every item is ticked", () => {
    render(<Checklist items={items} storageKey="test" linkFor={linkFor} />);
    expect(screen.getByText("0 of 2 reviewed")).toBeTruthy();
    fireEvent.click(screen.getByLabelText(/risk-4 is unsupported/));
    fireEvent.click(screen.getByLabelText(/fallback tag/));
    expect(screen.getByText("✓ Signed off. All 2 items reviewed.")).toBeTruthy();
  });

  it("states severity in words and links only items that point at a place in the memo", () => {
    render(<Checklist items={items} storageKey="test" linkFor={linkFor} />);
    expect(screen.getByText("! warning")).toBeTruthy();
    expect(screen.getByText("i information")).toBeTruthy();
    expect(screen.getAllByRole("link")).toHaveLength(1);
    expect(screen.getByRole("link").textContent).toBe("Go to risk-4 ↑");
  });

  it("remembers ticks in this browser only", () => {
    const first = render(<Checklist items={items} storageKey="test" linkFor={linkFor} />);
    fireEvent.click(screen.getByLabelText(/risk-4 is unsupported/));
    first.unmount();
    render(<Checklist items={items} storageKey="test" linkFor={linkFor} />);
    expect(screen.getByText("1 of 2 reviewed")).toBeTruthy();
    expect(screen.getByText(/stored in this browser only/)).toBeTruthy();
  });
});
