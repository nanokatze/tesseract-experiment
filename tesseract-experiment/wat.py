#!/usr/bin/python3
import sys

import PIL
import PIL.Image

TOLERANCE = 0.1
THRESHOLD = 0.6

def extract(im):
    im = im.copy()
    pixels = im.load()
    (w, h) = im.size
    for y in range(h):
        for x in range(w):
            col = tuple(x * (1 / 255) for x in pixels[x, y])
            (r, g, b) = (col[0], col[1], col[2])
            if ((r < THRESHOLD or g < THRESHOLD or b < THRESHOLD) or
                (abs(r - g) > TOLERANCE or
                 abs(g - b) > TOLERANCE or
                 abs(r - b) > TOLERANCE)):
                pixels[x, y] = (0, 0, 0)
    return im

if __name__ == "__main__":
    with PIL.Image.open(sys.argv[1]) as im:
        extract(im).save(sys.argv[2], "PNG")
