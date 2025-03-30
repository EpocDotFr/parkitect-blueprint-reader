# Parkitect Blueprint Reader

TODO.

![Python versions](https://img.shields.io/pypi/pyversions/parkitect-blueprint-reader.svg) ![Version](https://img.shields.io/pypi/v/parkitect-blueprint-reader.svg) ![License](https://img.shields.io/pypi/l/parkitect-blueprint-reader.svg)

[PyPI](https://pypi.org/project/parkitect-blueprint-reader/) - [Documentation](https://github.com/EpocDotFr/parkitect-blueprint-reader?tab=readme-ov-file#usage) - [Source code](https://github.com/EpocDotFr/parkitect-blueprint-reader) - [Issue tracker](https://github.com/EpocDotFr/parkitect-blueprint-reader/issues) - [Changelog](https://github.com/EpocDotFr/parkitect-blueprint-reader/releases)

# Usage

TODO.

## Development

### Getting source code and installing the package with dev dependencies

  1. Clone the repository
  2. From the root directory, run: `pip install -e .[dev]` on Linux or `pip install -e ".[dev]"` on Windows

### Releasing the package

From the root directory, run `python setup.py upload`. This will build the package, create a git tag and publish on PyPI.

`__version__` in `parkitect_blueprint_reader/__version__.py` must be updated beforehand. It should adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

An associated GitHub release must be created following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.