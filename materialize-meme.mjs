// Restores meme.png from the single-line base64 payload in
// meme-data.mjs (the snapshot push channel carries text only, so the
// PNG travels as text and is materialized back byte for byte).
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const { MEME_B64 } = await import(join(here, "meme-data.mjs"));
const bytes = Buffer.from(MEME_B64, "base64");
writeFileSync(join(here, "meme.png"), bytes);
console.log(`restored meme.png (${bytes.length} bytes)`);
