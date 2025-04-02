from parkitect_blueprint_reader.__version__ import __version__
from bitstring import Bits, BitArray
from argparse import ArgumentParser
from typing import Dict, BinaryIO
from sys import stdout
from PIL import Image
import json


def load(fp: BinaryIO) -> Dict:
    # TODO length
    # TODO checksum
    # TODO gzipped josn

    with Image.open(fp, formats=('PNG',)) as image:
        for i in range(0, 15, 2):
            pixel_byte = BitArray()

            for x in range(i, i + 2):
                for band in image.getpixel((x, 0)):
                    pixel_byte.append(
                        Bits(uint8=band)[-1:]
                    )

            print(pixel_byte.pp())


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
