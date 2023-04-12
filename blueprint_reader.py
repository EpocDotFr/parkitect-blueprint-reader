from typing import Dict, BinaryIO
from PIL import Image


def read_blueprint(fp: BinaryIO) -> Dict:
    with Image.open(fp) as img:
        width, height = img.size

        pixels = img.load()

    fp.close()

    raw_data = b''

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]

            for band in range(4):
                raw_data += pixel[band] & 1

    return {}


__all__ = ['read_blueprint']
