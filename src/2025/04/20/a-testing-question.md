---
title: A Testing Question
date: 2025-04-20
---

I have been thinking some more about how to teach testing to scientists who are learning how to program,
and I'm hoping one of my readers will have suggestions.
The bit of Python below creates a square NxN grid and then fills it using a random orthogonal walk.
Each time the walker visits a cell, the cell's count is incremented;
filling stops when the walker reaches the boundary (i.e., absorbing boundary conditions).

How can I test this?
The easy bits are:

1.  Generate a few hundred grids and make sure the boundary cells are all zero.

1.  Compare the sum of the grid values with the number of moves made by the walker (they should be equal).

1.  Patch the random choice function to force a series of moves (e.g., always up) and then check the resulting grid.

However, these tests are necessary but not sufficient.
If my choice of moves was biased in some direction,
for example,
none of these tests would reveal that.
If I generate enough grids and look at the distribution of values,
it should approximate a 2D Gaussian,
but I'd have to generate a _lot_ of grids to get close,
and it's difficult to specify what "close" actually means.
Is 20% relative error after 1000 grids good enough?
That test will pass for some random number generation seeds and fail for others;
I could tweak the seed until the test passes,
but that feels as grubby as [p-hacking](https://en.wikipedia.org/wiki/Data_dredging).
If you have suggestions,
please [get in touch](mailto:gvwilson@third-bit.com).

```python
import argparse
import csv
import io
import random


class Grid:
    """Store a grid of numbers."""

    def __init__(self, size):
        """Construct empty grid."""
        assert size > 0, f"Grid size must be positive not {size}"
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def __getitem__(self, key):
        """Get grid element."""
        x, y = key
        return self.grid[x][y]

    def __setitem__(self, key, value):
        """Set grid element."""
        x, y = key
        self.grid[x][y] = value

    def __str__(self):
        """Convert to string."""
        output = io.StringIO()
        csv.writer(output).writerows(self.grid)
        return output.getvalue()


def cmdline_args():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True, help="RNG seed")
    parser.add_argument("--size", type=int, required=True, help="grid size")
    return parser.parse_args()


def fill_grid(grid):
    """Fill in a grid."""

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    center = grid.size // 2
    size_1 = grid.size - 1
    x, y = center, center
    num = 0

    while (x != 0) and (y != 0) and (x != size_1) and (y != size_1):
        grid[x, y] += 1
        num += 1
        m = random.choice(moves)
        x += m[0]
        y += m[1]

    return num


if __name__ == "__main__":
    args = cmdline_args()
    random.seed(args.seed)
    grid = Grid(args.size)
    fill_grid(grid)
    print(grid)
```
