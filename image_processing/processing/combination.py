from typing import List
from PIL import Image

def blend(img_a: Image.Image, img_b: Image.Image, alpha: float = 0.5) -> Image.Image:
    """
    Combina duas imagens do mesmo tamanho através de blend.
    alpha=0.0 mantém só A; alpha=1.0 mantém só B.
    """
    if img_a.size != img_b.size:
        raise ValueError("As imagens precisam ter o mesmo tamanho para blend.")
    return Image.blend(img_a, img_b, alpha)

def concat_horizontal(images: List[Image.Image]) -> Image.Image:
    """Concatena imagens lado a lado, alinhando pela maior altura."""
    if not images:
        raise ValueError("Lista de imagens vazia.")
    h = max(im.height for im in images)
    widths = [int(im.width * (h / im.height)) for im in images]
    resized = [im.resize((w, h), Image.Resampling.LANCZOS) for im, w in zip(images, widths)]
    total_w = sum(w for w in widths)
    canvas = Image.new("RGB", (total_w, h))
    x = 0
    for im in resized:
        canvas.paste(im, (x, 0))
        x += im.width
    return canvas

def concat_vertical(images: List[Image.Image]) -> Image.Image:
    """Concatena imagens em coluna, alinhando pela maior largura."""
    if not images:
        raise ValueError("Lista de imagens vazia.")
    w = max(im.width for im in images)
    heights = [int(im.height * (w / im.width)) for im in images]
    resized = [im.resize((w, h), Image.Resampling.LANCZOS) for im, h in zip(images, heights)]
    total_h = sum(h for h in heights)
    canvas = Image.new("RGB", (w, total_h))
    y = 0
    for im in resized:
        canvas.paste(im, (0, y))
        y += im.height
    return canvas
