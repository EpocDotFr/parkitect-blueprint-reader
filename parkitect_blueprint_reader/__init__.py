from parkitect_blueprint_reader.__version__ import __version__
from argparse import ArgumentParser
from sys import stderr, stdout
from typing import Dict


def read(filename: str, pretty: bool = False) -> Dict:
    pass


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


__all__ = ['read']
