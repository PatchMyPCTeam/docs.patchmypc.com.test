#!/usr/bin/env python3
import re, glob, os
from urllib.parse import unquote

IMG_EXT = r"(?:png|jpe?g|gif|webp|svg)"
# Last token that looks like a filename with an image extension
FILENAME_RE = re.compile(rf'([A-Za-z0-9._()\-\ ]+\.{IMG_EXT})', re.I)

def extract_filename(url: str) -> str:
    u = unquote(url)  # %28→(, %29→), %20→space
    u = u.split('?', 1)[0].split('#', 1)[0]
    m = FILENAME_RE.findall(u)
    return (m[-1] if m else os.path.basename(u)).strip()

def slug_filename(fn: str) -> str:
    base, ext = os.path.splitext(fn)
    base = re.sub(r'\s+', '-', base)                    # spaces -> dash
    base = re.sub(r'[^A-Za-z0-9_()\-.]+', '-', base)    # keep letters,digits,_,-,(),.
    base = re.sub(r'-{2,}', '-', base).strip('-')       # collapse --
    return f"{base}{ext.lower()}"

def to_root_url(url: str) -> str:
    return "/_images/" + slug_filename(extract_filename(url))

def build_md(alt: str, url: str) -> str:
    alt = alt or ""
    alt_md = alt.replace(']', r'\]')
    title  = alt.replace('"', r'\"')  # title = alt
    return f'![{alt_md}]({to_root_url(url)} "{title}")'

FILES = [p for g in ("**/*.md","**/*.MD","**/*.mdx","**/*.MDX","**/*.markdown","**/*.MARKDOWN")
         for p in glob.glob(g, recursive=True)]

# Remove <figure> wrappers and figcaptions (we rebuild clean Markdown)
FIGCAPTION = re.compile(r'<figcaption\b[^>]*>.*?</figcaption>', re.I | re.S)
FIG_WRAP   = re.compile(r'<figure\b[^>]*>(.*?)</figure>', re.I | re.S)

# <img src="..."> (alt optional)
HTML_IMG = re.compile(
    r'<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*?(?:\balt=["\']([^"\']*)["\'])?[^>]*>',
    re.I
)

# Markdown images — rebuild them too
MD_IMG = re.compile(r'!\[([^\]]*)\]\(\s*<?([^\s)]+)>?(?:\s+"[^"]*")?\s*\)', re.I)

changed = 0
for path in FILES:
    with open(path, encoding="utf-8") as f:
        s = f.read()
    o = s

    # 1) unwrap figures / drop captions
    s = FIGCAPTION.sub('', s)
    s = FIG_WRAP.sub(lambda m: m.group(1), s)

    # 2) <img> → strict Markdown
    s = HTML_IMG.sub(lambda m: build_md(m.group(2) or "", m.group(1)), s)

    # 3) existing Markdown → strict Markdown
    s = MD_IMG.sub(lambda m: build_md(m.group(1), m.group(2)), s)

    # 4) strip ../ or ./ before _images just in case
    s = re.sub(r'\]\(\s*<?(?:\.\./|\.?/)+_images/', '](/_images/', s)

    if s != o:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        print(f"Fixed: {path}")
        changed += 1

print(f"Normalized {changed} file(s).")
