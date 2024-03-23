"""Invasion percolation in Python."""

import random
import sys

from grid_list import GridList
from grid_array import GridArray


def main():
    """Main driver."""
    kind, width, height, depth, seed = setup()
    grid = initialize_grid(kind, width, height, depth)
    grid.fill()
    print_grid(kind, grid, seed)


def setup():
    """Get parameters."""
    kind = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    depth = int(sys.argv[4])

    if len(sys.argv) > 5:
        seed = int(sys.argv[5])
    else:
        seed = random.randrange(sys.maxsize)
    random.seed(seed)

    return kind, width, height, depth, seed


def initialize_grid(kind, width, height, depth):
    """Prepare grid for simulation."""
    lookup = {
        "list": GridList,
        "array": GridArray,
    }
    return lookup[kind](width, height, depth)


def print_grid(kind, grid, seed, details="full"):
    """Show the result."""
    print(kind, grid.width(), grid.height(), grid.depth(), seed)
    if details == "brief":
        return
    for y in range(grid.height() - 1, -1, -1):
        for x in range(grid.width()):
            if details == "numbers":
                sys.stdout.write(f"{grid[x, y]:02d} ")
            else:
                sys.stdout.write("X" if grid[x, y] == 0 else ".")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
