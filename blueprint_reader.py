from PIL import Image, UnidentifiedImageError
from typing import Dict, BinaryIO, List
from bitstring import Bits
import gzip
import json


class BlueprintReadError(Exception):
    pass


def read_pixel(pixels: List, p: int) -> str:
    return ''.join([
        str(pixels[p][band] & 1) for band in (3, 0, 1, 2) # Alpha, Red, Green, Blue
    ])


def read_pixels(pixels: List, start: int, stop: int) -> Bits:
    if start % 2 != 0 or stop % 2 != 0:
        raise ValueError('start and stop must be multiples of 2')

    return Bits(bin='0b' + ''.join([
        read_pixel(pixels, p + 1) + read_pixel(pixels, p) for p in range(start, stop, 2)
    ]))


def read_blueprint(fp: BinaryIO) -> Dict:
    try:
        with Image.open(fp, formats=['png']) as img:
            if img.mode != 'RGBA':
                raise BlueprintReadError('Blueprints must be in RGBA mode')

            width, height = img.size

            if width != 512 or height != 512:
                raise BlueprintReadError('Blueprints must be 512x512 pixels')

            pixels = list(img.getdata())
    except UnidentifiedImageError:
        raise BlueprintReadError('Blueprints must be PNG images')
    finally:
        fp.close()

    # TODO Read and validate header
    # header = read_pixels(pixels, 0, 6).tobytes()

    # if header != bytes.fromhex('53 4D 01'):
    #     raise BlueprintReadError('Not a Parkitect blueprint')

    data = read_pixels(pixels, 0, 6)

    # TODO Read and validate gzip data size
    # gzip_size = read_pixels(pixels, 6, 16).unpack('uint:16')[0]
    #
    # if not gzip_size:
    #     raise BlueprintReadError('Could not determine gzip data size')
    # elif gzip_size > 512 * 512 / 2: # Number of pixels divided by 2 (1 byte is stored using 2 pixels)
    #     raise BlueprintReadError('Invalid gzip data size value')

    # TODO Read and validate checksum

    # TODO Read gzipped data, return parsed JSON data
    # return json.loads(
    #    gzip.decompress(
    #        read_pixels(pixels, 16, gzip_size * 2).tobytes()
    #    )
    # )

    with open('actual.bin', 'wb') as fp:
        data.tofile(fp)

    return {}


__all__ = [
    'read_blueprint',
    'BlueprintReadError',
]
