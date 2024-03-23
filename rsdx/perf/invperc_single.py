"""Invasion percolation in Python."""

import sys


from invperc_util import get_params, initialize_grid, initialize_random
from params_single import ParamsSingle


def main():
    """Main driver."""
    params = get_params(sys.argv[1], ParamsSingle)
    initialize_random(params)
    grid = initialize_grid(params)
    num_filled = grid.fill()
    if len(sys.argv) > 2:
        print_grid(params, grid, num_filled, details="full")


def print_grid(params, grid, num_filled, details="brief"):
    """Show the result."""
    print(params.kind, params.width, params.depth, params.seed, num_filled)
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
