import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { App } from "./App";
import "./styles.css";
import { readTheme } from "./theme";

document.documentElement.dataset.theme = readTheme();  // before the first paint, so the page never flashes

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
