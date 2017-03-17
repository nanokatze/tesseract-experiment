#!/usr/bin/env python
from setuptools import setup

setup(
    name="tesseract-experiment",
    version="1.0",
    description="upvotes 2kinds and gives you eye cancer",
    url="",
    author="Constantine \"t3a\" Shablya",
    author_email="no",
    license="MIT",
    packages=["tesseract-experiment"],
    install_requires=[
        "Pillow",
        "pytesseract",
        "requests",
    ],
    zip_safe=False
)
