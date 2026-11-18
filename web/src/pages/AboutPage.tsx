// Screen 6: About. The six strategy documents, the method and the limitations from /data/about.json, with a
// side navigation. Long-form reading with wide tables (each table scrolls on its own at phone width).
import { Markdown } from "../components/Markdown";
import type { AboutFile } from "../contracts/types";
import { useJson } from "../data";
import { Status } from "./Status";

const GROUPS = [["strategy", "Strategy documents"], ["method", "Method"], ["reference", "Reference"]] as const;

export function AboutPage({ doc }: { doc?: string }) {
  const about = useJson<AboutFile>("/data/about.json");
  if (about.state !== "ok") return <Status value={about.state} message={about.state === "error" ? about.message : ""} />;
  const documents = about.data.documents;
  const current = documents.find((d) => d.id === doc) ?? documents[0];
  return (
    <div className="about">
      <nav className="about-nav" aria-label="Documents">
        {GROUPS.map(([group, label]) => (
          <div key={group}>
            <h2>{label}</h2>
            <ul>
              {documents.filter((d) => d.group === group).map((d) => (
                <li key={d.id}>
                  <a href={`#/about/${d.id}`} aria-current={d.id === current?.id ? "page" : undefined}>{d.title}</a>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </nav>
      <article className="about-doc">
        {current ? <Markdown text={current.markdown} /> : <p>No documents yet.</p>}
        {current && <p className="note">Source: {current.source}</p>}
      </article>
    </div>
  );
}
