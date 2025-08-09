from setuptools import setup, find_packages
from pathlib import Path

README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="package-gisele",  # nome de distribuição no PyPI
    version="0.1.0",
    description="Pacote de processamento de imagens com operações de transformação, combinação e utilitários.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Gisele Fonseca",
    url="https://github.com/Giseleptbr/image-processing-package",
    packages=find_packages(exclude=("tests", "examples")),
    python_requires=">=3.9",
    install_requires=[
        "Pillow>=10.0.0",
        "numpy>=1.26.0",
        "matplotlib>=3.8.0",
    ],
    entry_points={
        "console_scripts": [
            # CLI simples (opcional). Ex.: imgproc in.jpg -o out.jpg
            "imgproc=image_processing.__main__:main",
        ]
    },
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Operating System :: OS Independent",
    ],
)
