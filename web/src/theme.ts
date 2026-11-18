// Light or dark theme, set as data-theme on <html>. Light is the default; a choice is remembered in this
// browser when storage allows.
export type Theme = "light" | "dark";

const KEY = "sourcebound:theme";

export function readTheme(): Theme {
  try {
    return localStorage.getItem(KEY) === "dark" ? "dark" : "light";
  } catch {
    return "light";
  }
}

export function saveTheme(theme: Theme): void {
  try {
    localStorage.setItem(KEY, theme);
  } catch {
    // Storage blocked: the choice lasts until the page closes.
  }
}
