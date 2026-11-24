#!/usr/bin/env python3
"""Deterministic infographic: World News, Monday 23 November 2026. 1024x1024 PNG."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_text(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y

# ---------- colours ----------
NAVY = (10, 37, 64)
NAVY2 = (16, 54, 92)
GOLD = (245, 184, 61)
BG = (242, 244, 247)
INK = (16, 32, 54)
MUTED = (71, 85, 105)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---------- header ----------
d.rectangle([0, 0, W, 168], fill=NAVY)
d.rectangle([0, 168, W, 172], fill=GOLD)
# small pill
pill = "THE DAY IN ONE PAGE"
pf = font(BOLD, 20)
pw = d.textlength(pill, font=pf)
d.rounded_rectangle([28, 22, 28 + pw + 28, 22 + 34], radius=17, fill=NAVY2, outline=GOLD, width=2)
d.text((28 + 14, 28), pill, font=pf, fill=GOLD)
d.text((28, 64), "WORLD NEWS", font=font(BOLD, 62), fill=WHITE)
d.text((28, 128), "MONDAY,  23  NOVEMBER  2026", font=font(BOLD, 34), fill=GOLD)
# header right: globe mark
cx, cy, r = 948, 84, 46
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(21, 94, 143), outline=GOLD, width=3)
d.ellipse([cx - 20, cy - r, cx + 20, cy + r], outline=(255, 255, 255), width=2)
d.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=2)
d.arc([cx - r, cy - 26, cx + r, cy + 26], start=200, end=340, fill=(255, 255, 255), width=2)

# ---------- icons ----------
def icon_globe(d, x, y, s, col):
    d.ellipse([x, y, x + s, y + s], fill=col)
    d.ellipse([x + s * 0.28, y + s * 0.08, x + s * 0.72, y + s * 0.92], outline=WHITE, width=3)
    d.line([x + 6, y + s * 0.5, x + s - 6, y + s * 0.5], fill=WHITE, width=3)

def icon_ship(d, x, y, s, col):
    d.rounded_rectangle([x, y, x + s, y + s], radius=14, fill=col)
    # hull
    d.polygon([(x + 12, y + 52), (x + s - 12, y + 52), (x + s - 20, y + 66), (x + 20, y + 66)], fill=WHITE)
    d.rectangle([x + s // 2 - 2, y + 18, x + s // 2 + 2, y + 52], fill=WHITE)
    d.polygon([(x + s // 2 + 4, y + 20), (x + s // 2 + 4, y + 50), (x + s - 16, y + 50)], fill=GOLD)

def icon_chip(d, x, y, s, col):
    d.rounded_rectangle([x, y, x + s, y + s], radius=14, fill=col)
    for i in range(3):
        px = x + 16 + i * 20
        d.line([px, y + 6, px, y + 16], fill=WHITE, width=3)
        d.line([px, y + s - 16, px, y + s - 6], fill=WHITE, width=3)
        py = y + 16 + i * 20
        d.line([x + 6, py, x + 16, py], fill=WHITE, width=3)
        d.line([x + s - 16, py, x + s - 6, py], fill=WHITE, width=3)
    d.rounded_rectangle([x + 22, y + 22, x + s - 22, y + s - 22], radius=6, outline=WHITE, width=3)
    d.text((x + 32, y + 30), "AI", font=font(BOLD, 24), fill=WHITE)

def icon_capitol(d, x, y, s, col):
    d.rounded_rectangle([x, y, x + s, y + s], radius=14, fill=col)
    d.pieslice([x + 24, y + 12, x + s - 24, y + 44], start=180, end=360, fill=WHITE)
    d.rectangle([x + 22, y + 40, x + s - 22, y + 46], fill=WHITE)
    for i in range(4):
        cx0 = x + 22 + i * 12
        d.rectangle([cx0, y + 48, cx0 + 6, y + 64], fill=WHITE)
    d.rectangle([x + 16, y + 64, x + s - 16, y + 70], fill=WHITE)

def icon_plane(d, x, y, s, col):
    d.rounded_rectangle([x, y, x + s, y + s], radius=14, fill=col)
    # plane in side view, nose right: fuselage + tail + wings
    d.ellipse([x + 12, y + 32, x + 66, y + 48], fill=WHITE)
    d.polygon([(x + 14, y + 36), (x + 26, y + 22), (x + 32, y + 36)], fill=WHITE)
    d.polygon([(x + 38, y + 34), (x + 50, y + 14), (x + 56, y + 14), (x + 48, y + 34)], fill=WHITE)
    d.polygon([(x + 40, y + 46), (x + 50, y + 62), (x + 56, y + 62), (x + 48, y + 46)], fill=WHITE)
    d.polygon([(x + 56, y + 36), (x + 68, y + 40), (x + 56, y + 44)], fill=WHITE)

def icon_game(d, x, y, s, col):
    d.rounded_rectangle([x, y, x + s, y + s], radius=14, fill=col)
    d.text((x + 18, y + 18), "VI", font=font(BOLD, 40), fill=WHITE)
    d.ellipse([x + 52, y + 52, x + 60, y + 60], fill=GOLD)
    d.ellipse([x + 62, y + 52, x + 70, y + 60], fill=GOLD)

ICONS = {
    "globe": icon_globe,
    "ship": icon_ship,
    "chip": icon_chip,
    "capitol": icon_capitol,
    "plane": icon_plane,
    "game": icon_game,
}

STORIES = [
    dict(tag="CLIMATE  •  ANTALYA", accent=(16, 133, 88), icon="globe",
         head="COP31 talks collapse with no deal",
         body="After 49 hours overtime, the EU and 130 nations reject a draft with no fossil-fuel phase-out.",
         stat="49 HOURS OVERTIME"),
    dict(tag="WAR  •  LIBYA / KYIV", accent=(178, 44, 44), icon="ship",
         head="Ukraine says it sank a Russian warship",
         body="Drones hit the ship off Libya as Russian strikes on Kyiv kill at least 15.",
         stat="AT LEAST 15 KILLED IN KYIV"),
    dict(tag="TECH  •  AI CHIPS", accent=(21, 122, 60), icon="chip",
         head="Nvidia brings back Jensen Huang",
         body="Huang returns as CEO as the US blacklists a Singapore firm over chip diversion to China.",
         stat="MEGASPEED BLACKLISTED"),
    dict(tag="USA  •  CONGRESS", accent=(29, 78, 172), icon="capitol",
         head="Democrats win biggest House majority since 1992",
         body="Flipping a North Carolina seat gives Democrats their largest majority in 34 years.",
         stat="NORTH CAROLINA SEAT FLIPPED"),
    dict(tag="TRAVEL  •  THANKSGIVING", accent=(8, 110, 145), icon="plane",
         head="Delta glitch delays 1,000+ flights",
         body="A weight-and-balance system crash grounds planes in Atlanta on Thanksgiving Eve.",
         stat="FAA GROUND STOP IN ATLANTA"),
    dict(tag="GAMES  •  RECORD", accent=(124, 58, 237), icon="game",
         head="GTA VI makes $3.79B in one day",
         body="The launch sets an entertainment record, beating every film and game before it.",
         stat="$3.79 BILLION  •  DAY ONE"),
]

# ---------- grid ----------
GX, GY = 24, 188
CW, CH, GAP = 480, 240, 16
for i, s in enumerate(STORIES):
    col, row = i % 2, i // 2
    x = GX + col * (CW + GAP)
    y = GY + row * (CH + GAP)
    # card shadow + body
    d.rounded_rectangle([x + 2, y + 3, x + CW + 2, y + CH + 3], radius=18, fill=(210, 216, 224))
    d.rounded_rectangle([x, y, x + CW, y + CH], radius=18, fill=CARD)
    d.rounded_rectangle([x, y, x + CW, y + 7], radius=6, fill=s["accent"])
    d.rectangle([x, y + 4, x + CW, y + 7], fill=s["accent"])
    # icon
    ix, iy = x + 20, y + 24
    ICONS[s["icon"]](d, ix, iy, 76, s["accent"])
    # tag + headline + body, text block to the right of icon? No: tag above headline, full width below icon row
    # Layout: icon left, tag+headline right of icon
    tx = x + 112
    tw = CW - 112 - 20
    d.text((tx, y + 26), s["tag"], font=font(BOLD, 17), fill=s["accent"])
    head_lines = wrap(d, s["head"], font(BOLD, 27), tw)
    hy = y + 50
    hy = draw_text(d, tx, hy, head_lines, font(BOLD, 27), INK, 32)
    # body full width below
    body_lines = wrap(d, s["body"], font(REG, 20), CW - 40)
    draw_text(d, x + 20, y + 128, body_lines, font(REG, 20), MUTED, 27)
    # key-number pill at card bottom
    stat = s["stat"]
    sf = font(BOLD, 17)
    sw = d.textlength(stat, font=sf)
    tint = tuple(min(255, c + 225) if c < 60 else 235 for c in s["accent"])
    # light tint: blend accent with white
    tint = tuple(int(0.14 * c + 0.86 * 255) for c in s["accent"])
    d.rounded_rectangle([x + 20, y + CH - 48, x + 20 + sw + 28, y + CH - 48 + 32], radius=16, fill=tint)
    d.text((x + 20 + 14, y + CH - 48 + 6), stat, font=sf, fill=s["accent"])

# ---------- footer ----------
d.rounded_rectangle([24, 952, 1000, 1012], radius=14, fill=NAVY)
d.text((40, 962), "ALSO TODAY", font=font(BOLD, 17), fill=GOLD)
footer = "South Korea's education minister resigns over AI cheating  •  Indonesia candy factory fire kills at least 3  •  Houthis claim attack on Saudi oil refinery"
fl = wrap(d, footer, font(REG, 17), 1000 - 40 - 150)
draw_text(d, 40 + 118, 962, fl, font(REG, 17), WHITE, 22)

img.save("/home/hatch/workspace/makefun-news-20261123/entry.png", format="PNG", optimize=True)
print("saved")
