# package-gisele
A Python image processing package built on Pillow, providing functions for resizing, rotating, cropping, flipping, converting to grayscale, blending, concatenating images, and visualization utilities.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install from PyPI:

pip install package-gisele
For local development:


python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e .
Usage

from image_processing import load_image, save_image, resize_image, to_grayscale
img = load_image("photo.jpg")
img = resize_image(img, width=800)   # keep aspect ratio
img = to_grayscale(img)
save_image(img, "photo_gray.jpg")

CLI
If installed locally or via pip, you can use the imgproc command:


imgproc input.jpg -o output.jpg --resize 800 0 --gray --rotate 15
Features
IO: load and save images

Transformations: resize, rotate, crop, flip, convert to grayscale
Combinations: blend, concatenate horizontally and vertically
Visualization: display images and RGB histograms

Author
Gisele Fonseca

## License
[MIT](https://choosealicense.com/licenses/mit/)