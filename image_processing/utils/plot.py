from typing import Optional
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def show(img: Image.Image, title: Optional[str] = None) -> None:
    """Exibe a imagem com matplotlib."""
    arr = np.asarray(img)
    plt.figure()
    plt.imshow(arr)
    plt.axis("off")
    if title:
        plt.title(title)
    plt.show()

def plot_histogram(img: Image.Image, title: str = "Histograma RGB") -> None:
    """Plota histograma dos três canais RGB."""
    arr = np.asarray(img)
    plt.figure()
    for i, lbl in enumerate(["R", "G", "B"]):
        plt.hist(arr[..., i].ravel(), bins=256, alpha=0.5, label=lbl)
    plt.legend()
    plt.title(title)
    plt.xlabel("Intensidade")
    plt.ylabel("Frequência")
    plt.show()
