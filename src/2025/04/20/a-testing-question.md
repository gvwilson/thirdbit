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

## The Code

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

    moves = [[-1, 0], [1, 0], [0, -1], [0, -1]]
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

## The Reveal

Did you notice the bug?
`[0, -1]` is repeated in the list of available moves;
the last entry should be `[0, 1]`.
This was an actual typo in an early draft of this function,
and none of my tests spotted it:

1.  The boundary cells of all grids are still zero.

1.  The sum of the grid's values is still the number of moves.

1.  Patching the random choice function to force a series of moves
    *fixes the underlying bug*.

If I had used `random.choice(list(range(len(moves))))` to choose an index into `moves`
and then used that move,
the final test might have revealed the problem,
but none of my statistical tests detected it,
and that scares me.

## Another Example

Another way to fill a grid is called [invasion percolation](https://en.wikipedia.org/wiki/Invasion_percolation).
In pseudo-Python, it works like this—or rather,
this code *almost* does the right thing:

```python
def invasion_percolation(size, depth):
    # Create grid of random numbers
    grid = Grid(size)
    for x in range(size):
        for y in range(size):
            grid[x, y] = random.randint(0, depth)

    # Mark the central cell
    x, y = size // 2, size // 2
    grid[x, y] = MARKED

    # Repeat until the marked region hits the boundary
    while (x != 0) and (y != 0) and (x != size - 1) and (y != size - 1):
        x, y = find_next_cell(grid)
        grid[x, y] = MARKED

# Find the next cell to fill
def find_next_cell(grid):
    # Set min_val to Infinity to ensure first cell qualifies
    min_x, min_y, min_val = None, None, Infinity

    # Check all cells
    for x in range(grid.size):
        for y in range(grid.size):
            # Already filled
            if grid[x, y] == MARKED:
                continue
            # Not adjacent to a marked cell
            if not adjacent(grid, x, y):
                continue
            # We have seen a lower value
            if grid[x, y] >= min_val:
                continue
            # A new winner
            min_x, min_y, min_val = x, y, grid[x, y]

    # Report results
    return min_x, min_y
```

Did you spot the problem?
I didn't:
I used a variation of this code for more than a year before realizing that
it is biased toward the (0, 0) corner of the grid.
To see why,
imagine that the entire "random" grid is filled with the value 1.
The first cell that the double loop finds
that's adjacent to the already-filled region
will always be to the lower left of the filled region,
because that will always be the first time the double loop encounters the value 1.
Replacing the 1's with random number in the range 0…depth doesn't fix this flaw;
it just makes it harder to spot.

The solution in this case is to find all the cells
that are adjacent to the already-filled region
*and* which are tied for lowest value,
then choose one of those at random.
My question is,
what test(s) could I plausibly have written before I realized my mistake
that would have told me my implementation had introduced an unwanted bias?
