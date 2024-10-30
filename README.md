# rdp-limited-edition

[![PyPI - Version](https://img.shields.io/pypi/v/rdp-limited-edition.svg)](https://pypi.org/project/rdp-limited-edition)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rdp-limited-edition.svg)](https://pypi.org/project/rdp-limited-edition)

-----

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

Yet another [Ramer-Douglas-Peucker algorithm](https://martinfleischmann.net/line-simplification-algorithms/) implementation. **But this one is special!** It allows to additionally define the maximum number of points to retain.

**Pure [numpy](https://numpy.org/).** Hence the performance is not as fast as C/Rust implementations like [simplify(PyPI)](https://pypi.org/project/simplification/) or similar.

## Installation

```console
pip install rdp-limited-edition
```

## Usage

```python
from rdp_limited_edition import rdp_limed

# TBD
```

## License

`rdp-limited-edition` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
