"""Invasion percolation in Python."""

import random
import sys


# Create a width X height grid.
def make_grid(width, height, depth):
    grid = []
    for x in range(width):
        row = []
        for y in range(height):
            row.append(random.randint(1, depth))
        grid.append(row)
    return grid


# Choose the next cell to fill in.
def choose_cell(grid):
    least, cx, cy = None, None, None
    for x in range(len(grid)):
        row = grid[x]
        for y in range(len(row)):
            temp = grid[x][y]
            if not adjacent(grid, x, y):
                continue
            if (least is None) or ((temp != 0) and (temp < least)):
                least, cx, cy = temp, x, y
    return cx, cy


# Is (x, y) adjacent to a filled cell?
def adjacent(grid, x, y):
    x_1, y_1 = x + 1, y + 1
    if (x > 0) and (grid[x - 1][y] == 0):
        return True
    if (x_1 < len(grid)) and (grid[x_1][y] == 0):
        return True
    if (y > 0) and (grid[x][y - 1] == 0):
        return True
    if (y_1 < len(grid[x])) and (grid[x][y_1] == 0):
        return True
    return False


# Is this cell on the border of the grid?
def on_border(width, height, x, y):
    if (x == 0) or (x == width - 1):
        return True
    if (y == 0) or (y == height - 1):
        return True
    return False


# Show the result.
def print_grid(grid, width, height, depth, seed, as_numbers=False):
    print(width, height, depth, seed)
    height = len(grid[0])
    for y in range(height - 1, -1, -1):
        for x in range(len(grid)):
            if as_numbers:
                sys.stdout.write(f"{grid[x][y]:02d} ")
            else:
                sys.stdout.write("X" if grid[x][y] == 0 else ".")
        sys.stdout.write("\n")


# Grid size and range of fill values.
width = int(sys.argv[1])
height = int(sys.argv[2])
depth = int(sys.argv[3])

# Random number generation.
if len(sys.argv) > 4:
    seed = int(sys.argv[4])
else:
    seed = random.randrange(sys.maxsize)
random.seed(seed)

# Create initial grid
grid = make_grid(width, height, depth)

# Fill central cell.
grid[width // 2][height // 2] = 0

# Fill other cells.
while True:
    x, y = choose_cell(grid)
    grid[x][y] = 0
    if on_border(width, height, x, y):
        break

# Show result.
print_grid(grid, width, height, depth, seed)
