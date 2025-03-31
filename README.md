# Parkitect Blueprint Reader

Python API and CLI tool to read [Parkitect](https://www.themeparkitect.com/)'s blueprints metadata.

![Python versions](https://img.shields.io/pypi/pyversions/parkitect-blueprint-reader.svg) ![Version](https://img.shields.io/pypi/v/parkitect-blueprint-reader.svg) ![License](https://img.shields.io/pypi/l/parkitect-blueprint-reader.svg)

[PyPI](https://pypi.org/project/parkitect-blueprint-reader/) - [Documentation](https://github.com/EpocDotFr/parkitect-blueprint-reader?tab=readme-ov-file#usage) - [Source code](https://github.com/EpocDotFr/parkitect-blueprint-reader) - [Issue tracker](https://github.com/EpocDotFr/parkitect-blueprint-reader/issues) - [Changelog](https://github.com/EpocDotFr/parkitect-blueprint-reader/releases)

## Prerequisites

  - Python >= 3.10

## Installation

### From PyPi

```shell
pip install parkitect-blueprint-reader
```

### Locally

After cloning/downloading the repo:

```shell
pip install .
```

## Usage

### API

The API consists of one `read()` method which reads metadata from the given blueprint file and returns the parsed data as a dictionary. Exceptions are thrown on
errors.

**Example usage**:

```python
import parkitect_blueprint_reader
from pprint import pprint

try:
    pprint(
      parkitect_blueprint_reader.read('coaster.png', pretty=True) # Pretty print is disabled by default
    )
except Exception as e:
  print(e)
```

### CLI

The CLI reads metadata from the given blueprint file, then writes the parsed data as JSON to `stdout`. If everything worked successfully, the return code will
be `0`; however in case of error the return code will be `1`, accompagned by the error message written to `stderr`.

**Example usage**:

```shell
parkitect-blueprint-reader coaster.png --pretty # Pretty print is disabled by default
```

## References

  - [Parkitect devlog - Update 58](https://www.texelraptor.com/blog/update-58)
  - [Reddit - How are blueprints stored?](https://www.reddit.com/r/ThemeParkitect/comments/qpa35q/how_are_blueprints_stored/)

## Development

### Getting source code and installing the package with dev dependencies

  1. Clone the repository
  2. From the root directory, run: `pip install -e .[dev]` on Linux or `pip install -e ".[dev]"` on Windows

### Releasing the package

From the root directory, run `python setup.py upload`. This will build the package, create a git tag and publish on PyPI.

`__version__` in `parkitect_blueprint_reader/__version__.py` must be updated beforehand. It should adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

An associated GitHub release must be created following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.