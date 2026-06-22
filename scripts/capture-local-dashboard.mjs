#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

async function loadPlaywright() {
  try {
    return await import("playwright");
  } catch {
    const bundledPath = process.env.PLAYWRIGHT_BUNDLE_PATH
      || "/Users/yvanfocsa/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright";
    return require(bundledPath);
  }
}

const { chromium } = await loadPlaywright();

const root = process.cwd();
const outDir = path.join(root, "livrables", "preuves", "local-run-captures");
const baseUrl = process.argv[2] || "http://127.0.0.1:8765";

fs.mkdirSync(outDir, { recursive: true });

const shots = [
  ["01-local-dashboard-overview.png", "/", 1440, 1100],
  ["02-local-alertes-soc.png", "/#alerts", 1440, 1100],
  ["03-local-sources-implementation.png", "/#implementation", 1440, 1100],
  ["04-local-dashboard-mobile.png", "/", 390, 1100],
];

const browser = await chromium.launch({ headless: true });
for (const [name, route, width, height] of shots) {
  const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
  await page.goto(baseUrl + route, { waitUntil: "networkidle" });
  await page.screenshot({ path: path.join(outDir, name), fullPage: true });
  await page.close();
  console.log(`Captured ${name}`);
}
await browser.close();
