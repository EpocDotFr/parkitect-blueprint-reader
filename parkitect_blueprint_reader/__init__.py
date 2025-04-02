from parkitect_blueprint_reader.__version__ import __version__
from typing import Dict, BinaryIO, Tuple
from bitstring import Bits, BitArray
from argparse import ArgumentParser
from math import floor
from sys import stdout
from PIL import Image
import json


def load(fp: BinaryIO) -> Dict:
    # TODO length
    # TODO checksum
    # TODO gzipped josn

    def pixel_to_coords(img: Image, pixel: int) -> Tuple[int, int]:
        return (
            pixel % img.width,
            floor(pixel / img.height)
        )

    def pixels_to_bitarray(img: Image, start: int, length: int) -> BitArray:
        ret = BitArray()

        for pixel in range(start, start + length):
            for band in img.getpixel(pixel_to_coords(img, pixel)):
                print(Bits(uint8=band).bin[-1])
                ret.append(
                    Bits(uint8=band)[-1:]
                )

        return ret

    with Image.open(fp, formats=('PNG',)) as img:
        print(
            pixels_to_bitarray(img, 0, 6).pp()
        )

        print(
            pixels_to_bitarray(img, 6, 8).uint32
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
