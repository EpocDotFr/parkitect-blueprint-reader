from blueprint_reader import read_blueprint, BlueprintReadError
from PIL import UnidentifiedImageError
from requests import RequestException
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
    try:
        if is_url(argument):
            response = requests.get(argument)
            response.raise_for_status()

            return BytesIO(response.content)

        return open(argument, 'rb')
    except RequestException as e:
        raise argparse.ArgumentTypeError(f'Cannot open remote file: {e}') from e
    except OSError as e:
        raise argparse.ArgumentTypeError(f'Cannot open local file: {e}') from e


def run() -> None:
    arg_parser = argparse.ArgumentParser(description='CLI tool which display information about a given Parkitect\'s blueprint')
    arg_parser.add_argument('file', type=path_or_url_argument, help='Either a local path or an URL to the desired blueprint')

    args = arg_parser.parse_args()

    try:
        info = read_blueprint(args.file)
    except UnidentifiedImageError:
        print(f'This does not look like an image')
    except BlueprintReadError as e:
        print(f'This image does not look like a Parkitect blueprint: {e}')
    else:
        print(info)

if __name__ == '__main__':
    run()
