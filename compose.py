#!/usr/bin/env python3
"""Composite the GTA 6 meme: take the generated skeleton-waiting scene,
add the big caption up top and paste make.fun's ghost (the official
press-kit mark) floating in the dark sky at the right, with a soft
magenta glow and the make.fun wordmark under it, so the ghost reads
as part of the scene rather than a corner sticker.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).parent
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SANS_B = str(FONT_DIR / "DejaVuSans-Bold.ttf")


def f(path, size):
    return ImageFont.truetype(path, size)


def main():
    base = Image.open(HERE / "media-generation-meme-base-0-8e51fffc-952e-44e6-b95a-d93a8fa4254f.png").convert("RGB")
    print("base size", base.size)
    d = ImageDraw.Draw(base)

    # Top caption, meme style: big white bold with black outline.
    caption = "13 YEARS LATER..."
    font = f(SANS_B, 72)
    w = d.textlength(caption, font=font)
    x = (base.width - w) // 2
    y = 36
    d.text((x, y), caption, font=font, fill=(255, 255, 255),
           stroke_width=4, stroke_fill=(0, 0, 0))

    # Soft magenta glow behind the ghost, then the ghost itself.
    ghost = Image.open(HERE / "ghost-mark.png").convert("RGBA")
    ghost = ghost.resize((210, 210), Image.LANCZOS)
    gx, gy = 760, 130
    glow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([gx - 30, gy - 30, gx + 240, gy + 240], fill=(255, 46, 136, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(28))
    base = Image.alpha_composite(base.convert("RGBA"), glow)
    base.paste(ghost, (gx, gy), ghost)
    d = ImageDraw.Draw(base)

    # make.fun wordmark under the ghost.
    label = "make.fun"
    lfont = f(SANS_B, 34)
    lw = d.textlength(label, font=lfont)
    d.text(((gx + 105) - lw / 2, gy + 216), label, font=lfont,
           fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))

    out = HERE / "meme.png"
    base.convert("RGB").save(out, format="PNG", optimize=True)
    print(out, out.stat().st_size)


if __name__ == "__main__":
    main()
