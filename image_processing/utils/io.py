from pathlib import Path
from typing import Union
from PIL import Image

PathLike = Union[str, Path]

def load_image(path: PathLike) -> Image.Image:
    """Carrega uma imagem do disco em RGB."""
    return Image.open(path).convert("RGB")

def save_image(img: Image.Image, path: PathLike, quality: int = 95) -> None:
    """Salva a imagem inferindo formato pela extensão do arquivo."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fmt = (path.suffix or ".png").replace(".", "").upper()
    img.save(path, format=fmt, quality=quality)
