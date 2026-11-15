#!/usr/bin/env python3
"""Make responsive WebP copies of blog images and record their sizes.

For every source image under images/ listed in SOURCES, writes
<name>-<width>.webp for each width in WIDTHS that is smaller than the
original, plus one at the original width, and stores the original size and
the available widths in _data/images.json. Templates (_includes/picture.html)
read that file to build srcset, width and height.

Run from the repo root after adding images:  python3 -I _tools/make_images.py
Needs ImageMagick (brew install imagemagick). Existing WebP files are kept unless the
source is newer.
"""
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"
SOURCES = ["fullstack", "agentic", "map3d", "about", "avatar.jpg", "nguyen-duc-duy.jpg"]
WIDTHS = [400, 800, 1200]
EXTS = {".jpg", ".jpeg", ".png"}
QUALITY = "78"


def size_of(path):
    """Displayed size, after applying the EXIF orientation (phone photos are often stored sideways)."""
    out = subprocess.run(["magick", str(path), "-auto-orient", "-format", "%w %h", "info:"],
                         capture_output=True, text=True, check=True).stdout
    w, h = out.split()
    return int(w), int(h)


def sources():
    for item in SOURCES:
        p = IMAGES / item
        if p.is_file():
            yield p
        elif p.is_dir():
            yield from sorted(f for f in p.rglob("*") if f.suffix.lower() in EXTS)


def main():
    data = {}
    for src in sources():
        w, h = size_of(src)
        widths = [x for x in WIDTHS if x < w] + [w]
        for tw in widths:
            out = src.with_name(f"{src.stem}-{tw}.webp")
            if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
                continue
            cmd = ["magick", str(src), "-auto-orient", "-strip"]
            if tw != w:
                cmd += ["-resize", f"{tw}x"]
            subprocess.run(cmd + ["-quality", QUALITY, str(out)], check=True)
        key = src.relative_to(IMAGES).as_posix()
        data[key] = {"w": w, "h": h, "widths": widths}
    target = ROOT / "_data" / "images.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{len(data)} images -> {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
