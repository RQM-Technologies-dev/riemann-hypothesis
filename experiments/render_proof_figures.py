"""Render the worked examples in the proof-reading guide using Pillow."""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "docs" / "figures"
INK = "#152f38"
TEAL = "#197c75"
FAINT = "#d6ded9"
PAPER = "#faf8ef"
ORANGE = "#a4482c"


def font(size, serif=False):
    names = ["DejaVuSerif.ttf", "/System/Library/Fonts/Supplemental/Georgia.ttf"] if serif else [
        "DejaVuSans.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf"
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    raise RuntimeError("Install the DejaVu fonts to render these figures.")


def sheet(title, subtitle):
    im = Image.new("RGB", (920, 430), PAPER)
    d = ImageDraw.Draw(im)
    d.text((32, 18), title, font=font(36, True), fill=INK)
    d.text((32, 73), subtitle, font=font(20), fill=INK)
    d.line((32, 117, 888, 117), fill=FAINT, width=2)
    return im, d


def depth_frame(e):
    im, d = sheet("How much survives multiplication?", "Each square is one unit of module length. Teal squares survive.")
    for row, (name, exponents) in enumerate([("A", (4, 0)), ("B", (2, 2))]):
        y = 148 + 104 * row
        d.text((32, y), f"{name}   {exponents}", font=font(24), fill=INK)
        for j, length in enumerate(exponents):
            for i in range(length):
                x, top = 242 + i * 64, y + j * 34
                d.rounded_rectangle((x, top, x+55, top+26), 3,
                                    fill=TEAL if i >= e else FAINT)
        rem = sum(max(k-e, 0) for k in exponents)
        d.text((600, y + 9), f"Remainder   {rem}", font=font(26, True), fill=TEAL)
    d.line((32, 360, 888, 360), fill=FAINT, width=2)
    d.text((32, 379), f"Depth  e = {e}", font=font(24), fill=INK)
    d.text((304, 379), "Both determinants have valuation 4.", font=font(22), fill=INK)
    return im


def pair_frame(k):
    im, d = sheet("One index from two conjugate places", "Gaussian integers   ·   prime 5   ·   theta map multiplies by 2 + i")
    terms = [("Image at w", k+1), ("Image at conjugate w", 0), ("Source dual defect", -k)]
    for i, (name, value) in enumerate(terms):
        y = 147 + 58*i
        d.text((32, y), name, font=font(21), fill=INK)
        d.line((530, y-6, 530, y+36), fill=INK, width=2)
        for n in range(abs(value)):
            x = 534 + 38*n if value > 0 else 491 - 38*n
            d.rectangle((x, y, x+32, y+25), fill=TEAL if value > 0 else ORANGE)
        d.text((780, y-2), f"{value:+d}" if value else "0", font=font(24), fill=INK)
    d.line((32, 347, 888, 347), fill=FAINT, width=2)
    d.text((32, 370), f"Source depth  k = {k}", font=font(23), fill=INK)
    d.text((370, 366), f"Paired defect   {k+1} + 0 − {k} = 1", font=font(26, True), fill=TEAL)
    return im


def zero_oscillations():
    im, d = sheet("Why the real part matters", "One model oscillation after dividing by the square root of x")
    for row, beta in enumerate((0.5, 0.7)):
        center = 188 + row * 118
        d.text((32, center-20), f"β = {beta:.1f}", font=font(24), fill=INK)
        points, upper, lower = [], [], []
        for i in range(681):
            t = 6 * i / 680
            amplitude = 14 * math.exp((beta-0.5)*t)
            x = 170+i
            upper.append((x, center-amplitude))
            lower.append((x, center+amplitude))
            points.append((x, center-amplitude*math.cos(4*t)))
        d.polygon(upper + list(reversed(lower)), fill=FAINT)
        d.line((170, center, 850, center), fill=PAPER, width=1)
        d.line(points, fill=TEAL if row == 0 else ORANGE, width=3)
    d.text((167, 369), "0", font=font(19), fill=INK)
    d.text((476, 367), "log x", font=font(20), fill=INK)
    d.text((838, 369), "6", font=font(19), fill=INK)
    return im

def save(name, frames):
    frames[0].save(OUT / (name + ".gif"), save_all=True, append_images=frames[1:],
                   duration=1500, loop=0, optimize=True, disposal=2)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    zero_oscillations().save(OUT / "zero-oscillations.png")
    save("scalar-depth", [depth_frame(e) for e in range(5)])
    save("paired-index", [pair_frame(k) for k in range(4)])
