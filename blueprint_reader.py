from typing import Dict, BinaryIO
from bitstring import Bits
from PIL import Image


def read_blueprint(fp: BinaryIO) -> Dict:
    with Image.open(fp) as img:
        width, height = img.size
        bands = len(img.getbands())

        pixels = img.load()

    fp.close()

    bits = ''

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]

            for band in range(bands):
                bits += str(pixel[band] & 1)

    with open('t.bin', 'wb') as fp:
        Bits(bin='0b' + bits).tofile(fp)

    return {}


__all__ = ['read_blueprint']
