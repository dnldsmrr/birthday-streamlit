import base64
import mimetypes
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).parent
VIDEO_DIR = BASE_DIR / "assets" / "videos"
PHOTO_DIR = BASE_DIR / "assets" / "photos"
TEMPLATE_PATH = BASE_DIR / "template.html"

VIDEO_DIR.mkdir(parents=True, exist_ok=True)
PHOTO_DIR.mkdir(parents=True, exist_ok=True)

VIDEO_EXT = (".mp4", ".webm", ".mov")
PHOTO_EXT = (".jpg", ".jpeg", ".png", ".webp")

DEMO_VIDEO = "https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
DEFAULT_ICONS = "['🌸','🎂','🎶','📷','💌','🌙']"


def to_data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(str(path))
    mime = mime or "application/octet-stream"
    data = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{data}"


def build_gallery_cards() -> str:
    files = sorted(p for p in VIDEO_DIR.iterdir() if p.suffix.lower() in VIDEO_EXT)

    if not files:
        # folder assets/videos masih kosong -> pakai video contoh biar preview tetap kelihatan
        pairs = [(DEMO_VIDEO, f"[Caption video {i + 1}]") for i in range(6)]
    else:
        pairs = [(to_data_uri(p), f"[{p.stem}]") for p in files]

    cards = []
    for src, caption in pairs:
        cards.append(
            f'<div class="polaroid" data-cap="{caption}">'
            f'<video class="gallery-video" src="{src}" muted loop playsinline preload="metadata"></video>'
            f"</div>"
        )
    return "\n".join(cards)


def build_memory_icons() -> str:
    files = sorted(p for p in PHOTO_DIR.iterdir() if p.suffix.lower() in PHOTO_EXT)

    if len(files) < 2:
        # folder assets/photos kosong / kurang dari 2 foto -> tetap pakai emoji, gak diubah
        return DEFAULT_ICONS

    files = files[:8]  # maksimal 8 pasang biar grid gak kepanjangan
    items = [f'\'<img src="{to_data_uri(p)}">\'' for p in files]
    return "[" + ",".join(items) + "]"


html = TEMPLATE_PATH.read_text(encoding="utf-8")
html = html.replace("<!--GALLERY_VIDEOS-->", build_gallery_cards())
html = html.replace("__MEMORY_ICONS__", build_memory_icons())

st.set_page_config(page_title="21th raisa's birthday", layout="centered")
components.html(html, height=860, scrolling=True)
