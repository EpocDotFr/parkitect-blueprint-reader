from blueprint_reader import read_blueprint
from urllib.parse import urlparse
from typing import BinaryIO
from io import BytesIO
import requests
import argparse


def is_url(url: str) -> bool:
  try:
    result = urlparse(url)

    return all([result.scheme, result.netloc])
  except ValueError:
    return False


def path_or_url_argument(argument: str) -> BinaryIO:
    if is_url(argument):
        return BytesIO(requests.get(argument).content)

    return open(argument, 'rb')


def run() -> None:
    arg_parser = argparse.ArgumentParser(description='CLI tool which display information about a given Parkitect\'s blueprint')
    arg_parser.add_argument('file', type=path_or_url_argument, help='Either a local path or an URL to the desired blueprint')

    args = arg_parser.parse_args()

    print(read_blueprint(args.file))


if __name__ == '__main__':
    run()
