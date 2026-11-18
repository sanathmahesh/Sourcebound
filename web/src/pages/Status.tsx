// Loading, error and memo-status states, always in words (never colour alone).
const LABEL: Record<string, string> = {
  loading: "Loading…",
  error: "Could not load the data.",
  current: "current",
  stale: "stale: newer filing",
  missing: "no memo",
};

export function Status({ value, message = "" }: { value: string; message?: string }) {
  return (
    <span className={`status status-${value}`} role={value === "error" ? "alert" : undefined}>
      {LABEL[value] ?? value}{message ? ` ${message}` : ""}
    </span>
  );
}
