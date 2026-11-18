// Screen 4: the watchlist. When it was last checked, a row per company, and each flag's rule and values.
import type { Watchlist, WatchFlag } from "../contracts/types";
import { useJson } from "../data";
import { Status } from "./Status";

function worst(flags: WatchFlag[]): string {
  if (flags.some((f) => f.severity === "alert")) return "alert";
  if (flags.some((f) => f.severity === "warning")) return "warning";
  return "none";
}

export function WatchlistPage() {
  const watch = useJson<Watchlist>("/data/watchlist.json");
  if (watch.state !== "ok") return <Status value={watch.state} message={watch.state === "error" ? watch.message : ""} />;
  const w = watch.data;
  const flagged = w.items.filter((i) => i.flags.length > 0).length;
  return (
    <section>
      <h1>Watchlist</h1>
      <p>Last checked {w.checked_at.replace("T", " ").slice(0, 16)} UTC. {flagged} of {w.items.length} companies have flags.</p>
      {flagged === 0 && <p>No deterioration flags.</p>}
      <div className="table-wrap">
        <table>
          <thead><tr><th>Company</th><th>Latest filing</th><th>Data to</th><th>Memo</th><th>Flags</th></tr></thead>
          <tbody>
            {w.items.map((item) => (
              <tr key={item.ticker}>
                <td><a href={`#/c/${item.ticker}`}>{item.name} ({item.ticker})</a></td>
                <td>{item.latest_filing ? `${item.latest_filing.form} filed ${item.latest_filing.filed}` : "none"}</td>
                <td>{item.data_to ?? "not available"}</td>
                <td><Status value={item.memo_status} />{item.memo_date ? ` (${item.memo_date})` : ""}</td>
                <td>
                  {item.flags.length === 0 ? "none" : (
                    <details>
                      <summary>{item.flags.length} ({worst(item.flags)})</summary>
                      <ul>
                        {item.flags.map((f, n) => (
                          <li key={n}><span className={`sev sev-${f.severity}`}>{f.severity}</span> {f.type}: {f.metric_id} from {f.from} to {f.to}.
                            <br /><span className="note">Rule: {f.rule}</span></li>
                        ))}
                      </ul>
                    </details>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
