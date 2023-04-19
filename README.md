# Parkitect blueprint reader

A Python CLI tool which display information about a given [Parkitect](https://themeparkitect.com/)'s blueprint.

## Prerequisites

Python >= 3.8.

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Usage

````shell
$ python run.py file
````

`file` must be either a local path or an URL to the desired blueprint.

## How it works

Parkitect is using a digital [steganography](https://en.wikipedia.org/wiki/Steganography) technique to store blueprint
data inside the blueprint image itself: it is leveraging the [least significant bit](https://en.wikipedia.org/wiki/Bit_numbering#Least_significant_bit_in_digital_steganography)
of each color channels (red, green, blue, alpha) of each pixels.

These bits forms bytes, which essentially contains:

  - a few bytes of metadata
  - gzipped JSON containing the actual blueprint data

References:

  - [Update 58 - Parkitect dev blog](https://themeparkitect.tumblr.com/post/126855975857/update-58)
  - [How are blueprints stored? - Reddit](https://www.reddit.com/r/ThemeParkitect/comments/qpa35q/how_are_blueprints_stored/)
  - [Parkitect Blueprint Investigator - GitHub](https://github.com/slothsoft/parkitect-blueprint-investigator)
