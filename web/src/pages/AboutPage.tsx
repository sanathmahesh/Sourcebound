// Screen 6: About. The six strategy documents, the method and the limitations from /data/about.json, with a
// sticky side navigation grouped into Documents and Reference. Long-form reading with wide tables.
import { Markdown } from "../components/Markdown";
import type { AboutDocument, AboutFile } from "../contracts/types";
import { useJson } from "../data";
import { LoadError, Loading } from "./Status";

const GROUPS: { label: string; members: AboutDocument["group"][] }[] = [
  { label: "Documents", members: ["strategy"] },
  { label: "Reference", members: ["method", "reference"] },
];

export function AboutPage({ doc }: { doc?: string }) {
  const about = useJson<AboutFile>("/data/about.json");
  if (about.state === "loading") return <main className="page"><Loading what="the documents" /></main>;
  if (about.state === "error") return <main className="page"><LoadError what="the documents" /></main>;
  const documents = about.data.documents;
  const current = documents.find((d) => d.id === doc) ?? documents[0];
  const group = GROUPS.find((g) => current && g.members.includes(current.group));
  return (
    <main className="page about">
      <nav className="about-nav" aria-label="Documents">
        {GROUPS.map((g) => (
          <div key={g.label}>
            <div className="eyebrow about-group">{g.label}</div>
            <div className="about-links">
              {documents.filter((d) => g.members.includes(d.group)).map((d) => (
                <a key={d.id} href={`#/about/${d.id}`} aria-current={d.id === current?.id ? "page" : undefined}>
                  {d.id === current?.id ? "▸ " : ""}{d.title}
                </a>
              ))}
            </div>
          </div>
        ))}
      </nav>
      <article className="about-doc">
        <div className="eyebrow">About{group ? ` · ${group.label}` : ""}</div>
        {current ? <Markdown text={current.markdown} /> : <p>No documents yet.</p>}
        {current && <p className="muted small">Source: <span className="mono">{current.source}</span></p>}
      </article>
    </main>
  );
}
