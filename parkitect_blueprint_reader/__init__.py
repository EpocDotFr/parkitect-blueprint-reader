from parkitect_blueprint_reader.__version__ import __version__
from argparse import ArgumentParser
from typing import Dict, BinaryIO
from sys import stdout
from io import BytesIO
from PIL import Image
import json


def load(fp: BinaryIO) -> Dict:
    image = Image.open(fp, formats=('PNG',))


def loads(s: bytes) -> Dict:
    with BytesIO(s) as fp:
        return load(fp)


def cli() -> None:
    arg_parser = ArgumentParser(
        description='CLI tool to read Parkitect\'s blueprints metadata'
    )

    arg_parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'parkitect-blueprint-reader {__version__}'
    )

    arg_parser.add_argument(
        '-f', '--filename',
        help='The blueprint file to read metadata from'
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
