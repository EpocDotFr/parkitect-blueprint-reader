from typing import Dict, BinaryIO
from PIL import Image


def read_blueprint(fp: BinaryIO) -> Dict:
    img = Image.open(fp)

    return {}


__all__ = ['read_blueprint']
