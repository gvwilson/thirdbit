"""List-of-lists grid."""

import random
from grid_generic import GridGeneric


class GridListRandomizer(GridGeneric):
    """Represent grid as list of lists."""

    def __init__(self, width, height, depth, rand=random.randint):
        """Construct and fill."""
        super().__init__(width, height, depth)
        self._rand = rand
        self._grid = []
        for x in range(self._width):
            row = []
            for y in range(self._height):
                row.append(self._rand(1, depth))
            self._grid.append(row)

    def __getitem__(self, key):
        """Get value at location."""
        x, y = key
        return self._grid[x][y]

    def __setitem__(self, key, value):
        """Set value at location."""
        x, y = key
        self._grid[x][y] = value
