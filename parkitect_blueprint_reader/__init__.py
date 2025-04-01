from parkitect_blueprint_reader.__version__ import __version__
from argparse import ArgumentParser
from typing import Dict, BinaryIO
from bitstring import Bits
from sys import stdout
from io import BytesIO
from PIL import Image
import json


def load(fp: BinaryIO) -> Dict:
    with Image.open(fp, formats=('PNG',)) as image:
        for i in range(10):
            r, g, b, a = image.getpixel((i, 0))

            rr = Bits(uint=r, length=8).bin[-1]
            rg = Bits(uint=g, length=8).bin[-1]
            rb = Bits(uint=b, length=8).bin[-1]
            ra = Bits(uint=a, length=8).bin[-1]

            print(rr, rg, rb, ra)


def loads(s: bytes) -> Dict:
    with BytesIO(s) as fp:
        return load(fp)


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
