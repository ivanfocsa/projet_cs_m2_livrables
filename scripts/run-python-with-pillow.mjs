#!/usr/bin/env node
import fs from "node:fs";
import { spawnSync } from "node:child_process";

const bundledPython = "/Users/yvanfocsa/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3";
const candidates = [
  process.env.PYTHON,
  "python3",
  fs.existsSync(bundledPython) ? bundledPython : undefined,
  "python",
].filter(Boolean);

const [, , script, ...args] = process.argv;

if (!script) {
  console.error("Usage: node scripts/run-python-with-pillow.mjs <script.py> [...args]");
  process.exit(2);
}

function hasPillow(python) {
  const result = spawnSync(python, ["-c", "from PIL import Image"], { encoding: "utf8" });
  return result.status === 0;
}

const python = candidates.find(hasPillow);

if (!python) {
  console.error("No Python runtime with Pillow was found. Install Pillow with: python3 -m pip install pillow");
  process.exit(1);
}

const result = spawnSync(python, [script, ...args], { stdio: "inherit" });
process.exit(result.status ?? 1);
