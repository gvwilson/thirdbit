"""List-of-lists grid."""

from grid_generic import GridGeneric


class GridFilled(GridGeneric):
    """Represent grid as list of lists and fill values."""

    def __init__(self, width, height, depth, values):
        """Construct and fill."""
        assert len(values) == width
        assert all(len(col) == height for col in values)
        super().__init__(width, height, depth)
        self._grid = [col[:] for col in values]

    def __getitem__(self, key):
        """Get value at location."""
        x, y = key
        return self._grid[x][y]

    def __setitem__(self, key, value):
        """Set value at location."""
        x, y = key
        self._grid[x][y] = value
