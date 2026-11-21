// Entrypoint for gta6-meme-x-01.
// The entry is the X post itself: this program only copies POST.json
// from the repository root to /output/POST.json, where the gate reads
// the post's address. The meme picture lives on X (it is the post's
// first picture); the repository also carries it as meme.png,
// restored from meme-data.mjs by materialize-meme.mjs, for the record.
// Note: POST.json holds a placeholder until the post is live; the
// gate refuses the placeholder, so replace it with the real post
// address before submitting.
// Run locally with:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, "POST.json"), join(OUTPUT_DIR, "POST.json"));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
