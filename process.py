"""Clean up headshots listed in prospects.json.

Usage:  .venv/bin/python -I process.py [--force]
For each prospect with an `image` in headshots/raw and no processed copy yet in
headshots/final (or all of them with --force):
  - transparent images: trim empty margins
  - plain or busy backgrounds: cut the person out with rembg (local, free)
  - waist-up shots: crop to head-and-shoulders
  - resize to max 300px and save as WebP
"""
import json, os, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "headshots", "raw")
FINAL = os.path.join(HERE, "headshots", "final")
force = "--force" in sys.argv
os.makedirs(FINAL, exist_ok=True)

session = None
def cutout(img):
    global session
    from rembg import remove, new_session
    if session is None:
        session = new_session("u2net_human_seg")
    return remove(img, session=session)

for pr in json.load(open(os.path.join(HERE, "prospects.json"))):
    f = pr.get("image")
    if not f or not os.path.exists(os.path.join(RAW, f)):
        continue
    out = os.path.join(FINAL, os.path.splitext(f)[0] + ".webp")
    if os.path.exists(out) and not force:
        continue
    img = Image.open(os.path.join(RAW, f))
    img.load()
    has_alpha = img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info)
    img = img.convert("RGBA")
    transparent = has_alpha and img.getchannel("A").getextrema()[0] < 250
    did = False
    if not transparent:
        img = cutout(img)
        did = True
    box = img.getchannel("A").point(lambda a: 255 if a > 20 else 0).getbbox()
    if box:
        l, t, r, b = box
        img = img.crop((l, max(0, t - 6), r, img.height))
        if img.height > 0.8 * img.width:  # waist-up: keep head and shoulders
            img = img.crop((0, 0, img.width, int(img.width * 0.78)))
    img.thumbnail((300, 300), Image.LANCZOS)
    img.save(out, "WEBP", quality=82, method=6)
    print(f"{f:<36} {'cutout' if did else 'transparent':<12} {img.size}")
