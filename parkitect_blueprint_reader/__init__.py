from parkitect_blueprint_reader.__version__ import __version__
from typing import Dict, BinaryIO, Tuple
from bitstring import Bits, BitArray
from argparse import ArgumentParser
from math import floor
from sys import stdout
from PIL import Image
import json
import gzip


def _pixel_to_coords(img: Image, pixel: int) -> Tuple[int, int]:
    return (
        pixel % img.width,
        floor(pixel / img.height)
    )


def _pixels_to_bitarray(img: Image, start: int, length: int) -> BitArray:
    ret = BitArray()

    start *= 2
    length *= 2

    for pixel in range(start, start + length, 2):
        for p in (pixel + 1, pixel):
            for band in reversed(img.getpixel(_pixel_to_coords(img, p))):
                ret.append(
                    Bits(uint8=band)[-1:]
                )

    return ret


def load(fp: BinaryIO) -> Dict:
    # TODO gzip length
    # TODO gzipped json

    with Image.open(fp, formats=('PNG',)) as img:
        magic_number = _pixels_to_bitarray(img, 0, 3)

        if magic_number.hex != '534d01':
            raise ValueError('This image is not a Parkitect blueprint')

        gzip_size = _pixels_to_bitarray(img, 3, 4)
        gzip_size.reverse()

        checksum = _pixels_to_bitarray(img, 7, 16)

        return json.loads(
            gzip.decompress(
                _pixels_to_bitarray(img, 23, int(gzip_size.uint32 / 2)).bytes
            )
        )


def cli() -> None:
    arg_parser = ArgumentParser(
        description='CLI tool to read Parkitect\'s blueprints metadata.'
    )

    arg_parser.add_argument(
        'filename',
        help='The blueprint file to read metadata from'
    )

    arg_parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'parkitect-blueprint-reader {__version__}'
    )

    arg_parser.add_argument(
        '-p', '--pretty',
        help='Pretty-print output',
        action='store_true'
    )

    args = arg_parser.parse_args()

    with open(args.filename, 'rb') as fp:
        json.dump(
            load(fp),
            stdout,
            indent=4 if args.pretty else None,
            separators=None if args.pretty else (',', ':')
        )


__all__ = ['load']
