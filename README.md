# `pyheroicons`

[![PyPI version](https://badge.fury.io/py/pyheroicons.svg)](https://pypi.org/project/pyheroicons)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyheroicons)](https://pypi.org/project/pyheroicons)
[![Package Status](https://img.shields.io/pypi/status/pyheroicons)](https://pypi.org/project/pyheroicons)
[![CI Build](https://github.com/burakyilmaz321/pyheroicons/actions/workflows/lint_and_test.yml/badge.svg)](https://github.com/burakyilmaz321/pyheroicons/actions/workflows/lint_and_test.yml)

`pyheroicons` is a Python library that offers a convenient interface to the [Tailwind CSS Heroicons](https://heroicons.com/) icon set. This library allows developers to easily integrate Heroicons into Python-based web frameworks such as Django, Flask, or FastAPI by generating SVG icon template strings.

## Installation

To install `pyheroicons`, simply use pip:

```bash
pip install pyheroicons
```

## Usage

Import `heroicon` function from `pyheroicons` and use it to generate icon templates:

```python
from pyheroicons import heroicon
```

## `heroicon` API

- **name** The name of the Heroicon (e.g., "academic-cap").
- **variant** The variant of the icon ("outline", "solid", "mini", or "micro").
- **cls** Optional. A CSS class to apply to the SVG icon.
- **strokewidth** Optional. The stroke width of the icon. <ins>Only applicable if the original SVG contains a stroke-width attribute. i.e. Only works for the "outline" variant.</ins>

## Example usage

```python
icon_svg = heroicon(name="academic-cap", variant="outline", cls="icon-class", strokewidth="2")
print(icon_svg)
```

## Keeping Up-to-Date

`pyheroicons` aims to stay up-to-date with the Heroicons library. When a new version of Heroicons is released, `pyheroicons` will also release a corresponding version to ensure compatibility.

| pyheroicons Version | Heroicons Version |
| ------------------- | ----------------- |
| 1.2.0               | 2.1.5             |

## Contributing

Contributions to `pyheroicons` are welcomed!

## License

`pyheroicons` is released under the MIT License.
