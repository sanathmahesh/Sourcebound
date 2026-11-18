// Loading the static JSON under /data. Each file is fetched once per page load.
import { useEffect, useState } from "react";

const loaded = new Map<string, Promise<unknown>>();

export function fetchJson<T>(path: string): Promise<T> {
  let request = loaded.get(path);
  if (!request) {
    request = fetch(path).then((r) => {
      if (!r.ok) throw new Error(`${path}: HTTP ${r.status}`);
      return r.json();
    });
    loaded.set(path, request);
  }
  return request as Promise<T>;
}

export type Loaded<T> = { state: "loading" } | { state: "error"; message: string } | { state: "ok"; data: T };

export function useJson<T>(path: string): Loaded<T> {
  const [result, setResult] = useState<Loaded<T>>({ state: "loading" });
  useEffect(() => {
    let live = true;
    setResult({ state: "loading" });
    fetchJson<T>(path).then(
      (data) => { if (live) setResult({ state: "ok", data }); },
      (error: Error) => { if (live) setResult({ state: "error", message: error.message }); },
    );
    return () => { live = false; };
  }, [path]);
  return result;
}
