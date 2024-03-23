"""NumPy array grid."""

import random
import numpy as np
from grid_generic import GridGeneric


class GridArray(GridGeneric):
    """Represent grid as NumPy array."""

    def __init__(self, width, height, depth):
        """Construct and fill."""
        super().__init__(width, height, depth)
        self._grid = np.zeros((width, height), dtype=int)
        for x in range(self.width()):
            for y in range(self.height()):
                self[x, y] = random.randint(1, depth)

    def __getitem__(self, key):
        """Get value at location."""
        return self._grid[*key]

    def __setitem__(self, key, value):
        """Set value at location."""
        self._grid[*key] = value
