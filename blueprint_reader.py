from PIL import Image, UnidentifiedImageError
from typing import Dict, BinaryIO, List
from bitstring import BitArray
import gzip
import json


class BlueprintReadError(Exception):
    pass


def _read_pixels(pixels: List, start: int, stop: int) -> BitArray:
    if start % 2 != 0 or stop % 2 != 0:
        raise ValueError('start and stop must be multiples of 2')

    bits = BitArray()
    last_bits = ''

    for p in range(start, stop):
        current_bits = ''.join(
            [str(pixels[p][band] & 1) for band in (3, 0, 1, 2)] # Alpha, Red, Green, Blue
        )

        if not last_bits:
            last_bits = current_bits
        else:
            bits.append('0b' + current_bits + last_bits)

            last_bits = ''

    return bits


def _decode(fp: BinaryIO) -> BitArray:
    try:
        with Image.open(fp, formats=['png']) as img:
            if img.mode != 'RGBA':
                fp.close()

                raise BlueprintReadError('Blueprints must be in RGBA mode')

            width, height = img.size

            if width != 512 or height != 512:
                fp.close()

                raise BlueprintReadError('Blueprints must be 512x512 pixels')

            pixels = list(img.getdata())
    except UnidentifiedImageError:
        fp.close()

        raise BlueprintReadError('Blueprints must be PNG images')

    fp.close()

    # header = _read_pixels(pixels, 0, 6).tobytes()

    # if header != bytes.fromhex('53 4D 01'):
    #     raise BlueprintReadError('Not a Parkitect blueprint')

    return _read_pixels(pixels, 0, 6)

    # size = _read_pixels(pixels, 6, 14).unpack('uint:32')[0]
    #
    # if not size:
    #     raise BlueprintReadError('Could not determine how many pixels to read')
    # elif size > len(pixels):
    #     raise BlueprintReadError('Invalid size value')
    #
    # return _read_pixels(pixels, 32, size)


def read_blueprint(fp: BinaryIO) -> Dict:
    data = _decode(fp)

    with open('actual.bin', 'wb') as fp:
        data.tofile(fp)

    # with gzip.open(f, 'r') as fp:
    #     data = json.loads(fp.read().decode('utf-8'))

    return {}


__all__ = ['read_blueprint']
