// The placeholder interface (phase 7): every screen working over the published data contract, plainly styled.
// Phase 9 replaces the look with the Claude Design handoff over the same data. Routing is by URL hash so the
// static host needs no rewrite rules: #/, #/c/WMT, #/c/WMT/verification, #/watchlist, #/results, #/about.
import { useEffect, useState } from "react";
import type { SiteIndex } from "./contracts/types";
import { useJson } from "./data";
import { AboutPage } from "./pages/AboutPage";
import { MemoPage } from "./pages/MemoPage";
import { Portfolio } from "./pages/Portfolio";
import { ResultsPage } from "./pages/ResultsPage";
import { VerificationPage } from "./pages/VerificationPage";
import { WatchlistPage } from "./pages/WatchlistPage";

export type Route =
  | { page: "portfolio" | "watchlist" | "results" | "missing" }
  | { page: "about"; doc?: string }
  | { page: "memo" | "verification"; ticker: string };

export function parseRoute(hash: string): Route {
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  if (parts.length === 0) return { page: "portfolio" };
  if (parts[0] === "c" && parts[1] && /^[A-Za-z.]{1,10}$/.test(parts[1])) {
    const ticker = parts[1].toUpperCase();
    if (parts.length === 2) return { page: "memo", ticker };
    if (parts.length === 3 && parts[2] === "verification") return { page: "verification", ticker };
  }
  if (parts.length === 1 && ["watchlist", "results", "about"].includes(parts[0])) {
    return { page: parts[0] as "watchlist" | "results" | "about" };
  }
  if (parts.length === 2 && parts[0] === "about" && /^[a-z0-9-]{1,60}$/.test(parts[1])) {
    return { page: "about", doc: parts[1] };
  }
  return { page: "missing" };
}

function useRoute(): Route {
  const [route, setRoute] = useState(() => parseRoute(window.location.hash));
  useEffect(() => {
    const onChange = () => { setRoute(parseRoute(window.location.hash)); window.scrollTo(0, 0); };
    window.addEventListener("hashchange", onChange);
    return () => window.removeEventListener("hashchange", onChange);
  }, []);
  return route;
}

function Page({ route }: { route: Route }) {
  switch (route.page) {
    case "portfolio": return <Portfolio />;
    case "memo": return <MemoPage ticker={route.ticker} />;
    case "verification": return <VerificationPage ticker={route.ticker} />;
    case "watchlist": return <WatchlistPage />;
    case "results": return <ResultsPage />;
    case "about": return <AboutPage doc={route.doc} />;
    default: return <p>Page not found. <a href="#/">Back to the portfolio</a>.</p>;
  }
}

export function App() {
  const route = useRoute();
  const index = useJson<SiteIndex>("/data/index.json");
  return (
    <>
      <header className="top">
        <a href="#/" className="brand">Sourcebound</a>
        <nav>
          <a href="#/">Portfolio</a>
          <a href="#/watchlist">Watchlist</a>
          <a href="#/results">Results</a>
          <a href="#/about">About</a>
        </nav>
      </header>
      <main>
        <Page route={route} />
      </main>
      <footer>
        <p>Data generated {index.state === "ok" ? index.data.generated_at.slice(0, 10) : "…"}.{" "}
          {index.state === "ok" ? index.data.disclaimer
            : "Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings."}</p>
      </footer>
    </>
  );
}
