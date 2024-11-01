# rdp-limited-edition

[![PyPI - Version](https://img.shields.io/pypi/v/rdp-limited-edition.svg)](https://pypi.org/project/rdp-limited-edition)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rdp-limited-edition.svg)](https://pypi.org/project/rdp-limited-edition)

-----

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Related Publications](#related-publications)
- [License](#license)

## About

Yet another [Ramer-Douglas-Peucker algorithm](https://martinfleischmann.net/line-simplification-algorithms/) implementation (line simplification). **But this one is special!** It allows to additionally define the maximum number of points to retain.
This means the algorithm stops to select additional points as soon as the maximum number ot points is reached although there would be more points outside of the tolerance band. To that, a negative tolerance allows to always get a defined number of points which are chosen accoring to the RDP algorithm. To provide this feature, no recursion is used.

**Pure [numpy](https://numpy.org/).** Hence the performance is not as fast as C/Rust implementations like [simplify](https://pypi.org/project/simplification/) or similar (approx. TODO times slower).

## Installation

```console
pip install rdp-limited-edition
```

## Usage

```python
import numpy as np
from rdp_limited_edition import rdp_limed

x = np.arange(360.0) * np.pi / 180.0
y = np.sin(x)

# let the tolerance be decisive
print(rdp_limed(x, y, max_points=x.shape[0], tolerance=0.005))

# get defined number of points
print(rdp_limed(x, y, max_points=10, tolerance=-1))

# or use both
print(rdp_limed(x, y, max_points=10, tolerance=0.1))
print(rdp_limed(x, y, max_points=10, tolerance=0.001))
```

## Related Publications

- D. H. Douglas and T. K. Peucker, “Algorithms for the reduction of the number of points required to represent a digitised line or its caricature,” The Canadian Cartographer, vol. 10, no. 2, pp. 112–122, Dec. 1973.

## License

`rdp-limited-edition` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
