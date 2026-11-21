// Packer for the meme entry: writes meme.png as one single line of
// base64 into meme-data.mjs (the snapshot push channel is text-only).
import { readFileSync, writeFileSync } from "node:fs";

const b64 = readFileSync("meme.png").toString("base64");
if (b64.length === 0 || b64.includes("\n")) {
  throw new Error("base64 encoding failed or wrapped");
}
writeFileSync(
  "meme-data.mjs",
  "// meme.png as one single line of base64 (snapshot push is text-only).\n" +
    `export const MEME_B64 = "${b64}";\n`
);
console.log(`packed ${b64.length} base64 chars into meme-data.mjs`);
