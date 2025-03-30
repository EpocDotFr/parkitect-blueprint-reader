from parkitect_blueprint_reader.__version__ import __version__
from argparse import ArgumentParser
from typing import Dict


def read(filename: str, pretty: bool = False) -> Dict:
    pass


def cli() -> None:
    arg_parser = ArgumentParser(
        description='The staticjinjaplus CLI which should be your main and only way to interact with staticjinjaplus.'
    )

    arg_parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'parkitect-blueprint-reader {__version__}'
    )

    arg_parser.add_argument(
        '-f', '--filename',
        help='The blueprint image to read'
    )

    arg_parser.add_argument(
        '-p', '--pretty',
        help='Pretty-print output',
        action='store_true'
    )

    args = arg_parser.parse_args()


__all__ = ['read']
