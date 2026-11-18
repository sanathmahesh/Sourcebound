import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";
import type { ChecklistItem } from "../contracts/types";
import { Checklist } from "./Checklist";

const items: ChecklistItem[] = [
  { id: "ck-1", category: "unsupported_claim", severity: "warning", message: "Claim risk-4 is unsupported.", ref: "risk-4" },
  { id: "ck-2", category: "fallback", severity: "info", message: "Debt used a fallback tag.", ref: "total_debt:LTM" },
];

afterEach(() => { cleanup(); localStorage.clear(); });

describe("Checklist", () => {
  it("counts progress and shows signed off when every item is ticked", () => {
    render(<Checklist items={items} storageKey="test" />);
    expect(screen.getByText("0 of 2 reviewed")).toBeTruthy();
    fireEvent.click(screen.getByLabelText(/risk-4 is unsupported/));
    fireEvent.click(screen.getByLabelText(/fallback tag/));
    expect(screen.getByText(/Signed off/)).toBeTruthy();
  });

  it("remembers ticks in this browser only", () => {
    const first = render(<Checklist items={items} storageKey="test" />);
    fireEvent.click(screen.getByLabelText(/risk-4 is unsupported/));
    first.unmount();
    render(<Checklist items={items} storageKey="test" />);
    expect(screen.getByText("1 of 2 reviewed")).toBeTruthy();
    expect(screen.getByText(/stored in this browser only/)).toBeTruthy();
  });
});
