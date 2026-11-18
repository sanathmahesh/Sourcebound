// The site shell: sticky header with navigation and the theme toggle, the current screen, and the
// disclaimer on every page. Routing is by URL hash so the static host needs no rewrite rules:
// #/, #/memo/WMT, #/memo/WMT/verification, #/watchlist, #/results, #/about/<document>.
import { useEffect, useState } from "react";
import type { SiteIndex } from "./contracts/types";
import { useJson } from "./data";
import { formatDate } from "./format";
import { AboutPage } from "./pages/AboutPage";
import { MemoPage } from "./pages/MemoPage";
import { Portfolio } from "./pages/Portfolio";
import { ResultsPage } from "./pages/ResultsPage";
import { VerificationPage } from "./pages/VerificationPage";
import { WatchlistPage } from "./pages/WatchlistPage";
import { readTheme, saveTheme, type Theme } from "./theme";

export type Route =
  | { page: "portfolio" | "watchlist" | "results" | "missing" }
  | { page: "about"; doc?: string }
  | { page: "memo" | "verification"; ticker: string };

export function parseRoute(hash: string): Route {
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  if (parts.length === 0) return { page: "portfolio" };
  if (parts[0] === "memo" && parts[1] && /^[A-Za-z.]{1,10}$/.test(parts[1])) {
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
    case "memo": return <MemoPage key={route.ticker} ticker={route.ticker} />;
    case "verification": return <VerificationPage key={route.ticker} ticker={route.ticker} />;
    case "watchlist": return <WatchlistPage />;
    case "results": return <ResultsPage />;
    case "about": return <AboutPage doc={route.doc} />;
    default: return <main className="page"><p>Page not found. <a href="#/">Back to the portfolio</a>.</p></main>;
  }
}

const NAV = [["portfolio", "Portfolio", "#/"], ["watchlist", "Watchlist", "#/watchlist"], ["results", "Results", "#/results"],
  ["about", "About", "#/about"]] as const;

const DISCLAIMER = "Educational project. Not investment advice. SB grades are a student's stylized scorecard, not credit ratings.";

export function App() {
  const route = useRoute();
  const index = useJson<SiteIndex>("/data/index.json");
  const [theme, setTheme] = useState<Theme>(readTheme);
  useEffect(() => { document.documentElement.dataset.theme = theme; }, [theme]);
  const section = route.page === "memo" || route.page === "verification" ? "portfolio" : route.page;
  const switchTheme = () => { const next = theme === "dark" ? "light" : "dark"; setTheme(next); saveTheme(next); };

  return (
    <>
      <header className="site-header">
        <div className="site-header-inner">
          <a href="#/" className="wordmark">Sourcebound</a>
          <nav className="site-nav" aria-label="Main">
            {NAV.map(([id, label, href]) => (
              <a key={id} href={href} aria-current={section === id ? "page" : undefined}>{label}</a>
            ))}
          </nav>
          <button type="button" className="theme-toggle" onClick={switchTheme}>
            {theme === "dark" ? "Light theme" : "Dark theme"}
          </button>
        </div>
      </header>
      <Page route={route} />
      <footer className="site-footer">
        <p>{index.state === "ok" ? `Data as of ${formatDate(index.data.generated_at)}. ` : ""}
          {index.state === "ok" ? index.data.disclaimer : DISCLAIMER}</p>
      </footer>
    </>
  );
}
