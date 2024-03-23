"""Invasion percolation in Python."""

import json
import random
import sys

from grid_lazy import GridLazy
from params_single import ParamsSingle


def invperc(params):
    """Invasion percolation."""
    random.seed(params.seed)
    grid = GridLazy(params.width, params.height, params.depth)
    grid.fill()
    return grid


def save_grid(writer, grid):
    """Show the result."""
    for y in range(grid.height() - 1, -1, -1):
        for x in range(grid.width()):
            writer.write("X" if grid[x, y] == 0 else ".")
        writer.write("\n")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as reader:
        params = ParamsSingle(**json.load(reader))
    grid, _ = invperc(params)
    if len(sys.argv) == 2:
        save_grid(sys.stdout, grid)
    else:
        with open(sys.argv[2], "w") as writer:
            save_grid(writer, grid)
