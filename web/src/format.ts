// Display formatting for engine values. Mirrors sourcebound/memo/render.py format_metric, so a figure reads
// the same in a claim chip (formatted by Python) and in a table here (formatted by this file); a test checks
// this against every chip in the published memos. Formatting only: no figure is computed here.
import type { Metric } from "./contracts/types";

type Status = Metric["status"];

function grouped(fixed: string): string {
  const [whole, fraction] = fixed.split(".");
  const withCommas = whole.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return fraction === undefined ? withCommas : `${withCommas}.${fraction}`;
}

/**
 * x to d decimals exactly as Python's f"{x:.{d}f}": the double's exact value, ties to even. JavaScript's
 * toFixed breaks exact ties upwards (47.25 -> "47.3" where Python gives "47.2"), so it is not used directly.
 */
export function toFixedPy(x: number, d: number): string {
  const [whole, frac = ""] = Math.abs(x).toFixed(100).split(".");  // exact digits of the double
  const kept = BigInt(whole + frac.slice(0, d));
  const rest = frac.slice(d);
  const half = "5".padEnd(rest.length, "0");
  const n = rest > half || (rest === half && kept % 2n === 1n) ? kept + 1n : kept;
  const digits = n.toString().padStart(d + 1, "0");
  const text = d === 0 ? digits : `${digits.slice(0, -d)}.${digits.slice(-d)}`;
  return (x < 0 ? "-" : "") + text;
}

function usd(value: number): string {
  const sign = value < 0 ? "-" : "";
  const amount = Math.abs(value);
  if (amount >= 1e9) return `${sign}$${grouped(toFixedPy(amount / 1e9, 1))} billion`;
  if (amount >= 1e6) return `${sign}$${grouped(toFixedPy(amount / 1e6, 0))} million`;
  return `${sign}$${grouped(toFixedPy(amount, 0))}`;
}

/** An engine value as it reads in prose: $51.5 billion, 0.96x, 23.6%, or its status in words. */
export function formatValue(value: number | null, unit: string, status: Status): string {
  if (status === "not_available") return "not available";
  if (status === "not_meaningful") return "not meaningful";
  if (value === null) return status === "net_cash" ? "net cash" : "not available";
  let text: string;
  if (unit === "USD") text = usd(value);
  else if (unit === "x") text = `${toFixedPy(value, 2)}x`;
  else if (unit === "%") text = `${toFixedPy(value, 1)}%`;
  else text = String(value);
  return status === "net_cash" ? `${text} (net cash)` : text;
}

/** An XBRL input in full, as filed: $34,624,000,000. */
export function formatRaw(value: number, unit: string): string {
  if (unit === "USD") return `${value < 0 ? "-" : ""}$${grouped(toFixedPy(Math.abs(value), 0))}`;
  return `${grouped(String(value))} ${unit}`;
}

/** A measured rate with its sample size; "pending" when nothing has been measured yet. */
export function formatRate(rate: { value: number | null; n: number } | undefined): string {
  if (!rate || rate.value === null) return `pending (n = ${rate?.n ?? 0})`;
  return `${toFixedPy(rate.value * 100, 1)}% (n = ${rate.n})`;
}

/** A measured share as a percentage, one decimal: 92.3%. */
export function formatPct(share: number): string {
  return `${toFixedPy(share * 100, 1)}%`;
}

const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

/** An ISO date or date-time as the design shows it: 4 Aug 2026. */
export function formatDate(iso: string | null | undefined): string {
  if (!iso) return "not available";
  const [year, month, day] = iso.slice(0, 10).split("-");
  return `${Number(day)} ${MONTHS[Number(month) - 1]} ${year}`;
}

/** A USD amount in whole millions with thousands separators, for the maturity ladder: 3,542. */
export function formatMillions(value: number): string {
  return grouped(toFixedPy(value / 1e6, 0));
}

/** Each verdict as a glyph and words, so it never relies on colour alone. */
export const VERDICT = {
  supported: { glyph: "✓", words: "supported" },
  partially_supported: { glyph: "◐", words: "partially supported" },
  unsupported: { glyph: "✕", words: "unsupported" },
} as const;

export const SEVERITY = { info: "i information", warning: "! warning", alert: "‼ alert" } as const;
