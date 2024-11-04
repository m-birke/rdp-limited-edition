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
