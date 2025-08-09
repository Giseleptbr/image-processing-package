from typing import Optional, Tuple
from PIL import Image

def resize_image(img: Image.Image, width: Optional[int] = None, height: Optional[int] = None, keep_ratio: bool = True) -> Image.Image:
    """
    Redimensiona a imagem.
    - Se keep_ratio=True e apenas um lado for informado, preserva proporção.
    - Pelo menos width ou height deve ser informado.
    """
    if keep_ratio:
        if width and not height:
            r = width / img.width
            height = int(img.height * r)
        elif height and not width:
            r = height / img.height
            width = int(img.width * r)
    if not width or not height:
        raise ValueError("Informe width ou height (ou ambos).")
    return img.resize((int(width), int(height)), Image.Resampling.LANCZOS)

def rotate_image(img: Image.Image, degrees: float, expand: bool = True) -> Image.Image:
    """Gira a imagem em graus."""
    return img.rotate(degrees, expand=expand)

def crop_image(img: Image.Image, box: Tuple[int, int, int, int]) -> Image.Image:
    """Recorta a imagem. box = (left, top, right, bottom)."""
    return img.crop(box)

def flip_horizontal(img: Image.Image) -> Image.Image:
    """Espelha horizontalmente."""
    return img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

def flip_vertical(img: Image.Image) -> Image.Image:
    """Espelha verticalmente."""
    return img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

def to_grayscale(img: Image.Image) -> Image.Image:
    """Converte para escala de cinza (3 canais para compatibilidade)."""
    return img.convert("L").convert("RGB")
