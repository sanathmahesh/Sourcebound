// The site is static: the React app plus the published JSON (../data/published), served under /data.
// In development the JSON is read from disk and /api is proxied to a local uvicorn (see README);
// in a build the JSON is copied into dist/data, so the deployed site and the repo hold the same files.
import { cpSync, createReadStream, existsSync, statSync } from "node:fs";
import { join, normalize } from "node:path";
import { fileURLToPath } from "node:url";
import react from "@vitejs/plugin-react";
import { defineConfig, type Plugin } from "vitest/config";

const PUBLISHED = fileURLToPath(new URL("../data/published", import.meta.url));

function publishedData(): Plugin {
  return {
    name: "sourcebound-published-data",
    configureServer(server) {
      server.middlewares.use("/data", (req, res, next) => {
        const file = normalize(join(PUBLISHED, decodeURIComponent((req.url ?? "/").split("?")[0])));
        if (!file.startsWith(PUBLISHED) || !existsSync(file) || !statSync(file).isFile()) return next();
        res.setHeader("Content-Type", "application/json");
        createReadStream(file).pipe(res);
      });
    },
    writeBundle(options) {
      cpSync(PUBLISHED, join(options.dir ?? "dist", "data"), { recursive: true });
    },
  };
}

export default defineConfig({
  plugins: [react(), publishedData()],
  server: { proxy: { "/api": "http://127.0.0.1:8000" } },
  test: { environment: "jsdom", setupFiles: ["src/test-setup.ts"] },
});
