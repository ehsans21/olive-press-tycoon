"""Draws the app icons (olive branch over an oil drop). Run: python3 icons/make_icons.py"""
from PIL import Image, ImageDraw


def icon(size, pad):
    S = 1024
    im = Image.new('RGBA', (S, S), '#1e2a1f')
    d = ImageDraw.Draw(im)
    c = S / 2
    r = (S / 2) * (1 - pad)
    d.ellipse([c - r, c - r, c + r, c + r], fill='#2c3b2c')
    for (x, y, w, h, col) in [(-0.42, -0.30, 0.34, 0.13, '#8d9e7b'), (-0.30, -0.46, 0.30, 0.12, '#a3b293'), (0.10, -0.47, 0.30, 0.12, '#7b8c69')]:
        d.ellipse([c + x * r, c + y * r, c + (x + w) * r, c + (y + h) * r], fill=col)
    d.ellipse([c - 0.12 * r, c - 0.42 * r, c + 0.10 * r, c - 0.18 * r], fill='#3d2645')
    k = 0.62 * r
    d.polygon([(c, c - 0.25 * r), (c - 0.5 * k, c + 0.45 * k), (c + 0.5 * k, c + 0.45 * k)], fill='#e8b934')
    d.ellipse([c - 0.52 * k, c + 0.05 * k, c + 0.52 * k, c + 1.09 * k], fill='#e8b934')
    d.ellipse([c - 0.30 * k, c + 0.35 * k, c - 0.12 * k, c + 0.62 * k], fill='#f6dc85')
    return im.resize((size, size), Image.LANCZOS).convert('RGB')


for name, size, pad in [('icon-192', 192, 0.08), ('icon-512', 512, 0.08), ('maskable-512', 512, 0.22), ('apple-touch-icon', 180, 0.1)]:
    icon(size, pad).save(f'icons/{name}.png')
