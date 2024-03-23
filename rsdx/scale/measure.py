"""Measure density and fractal dimension of grids."""

from collections import defaultdict
from math import sqrt

import numpy as np
import pandas as pd


def collect_density(grid):
    """Calculate density versus distance from center of grid."""
    assert grid.width() == grid.height()
    size = grid.width()

    cx, cy = size // 2, size // 2
    count_cells = defaultdict(int)
    count_filled = defaultdict(int)
    for x in range(size):
        for y in range(size):
            dist_2 = (x - cx) ** 2 + (y - cy) ** 2
            count_cells[dist_2] += 1
            if grid[x, y] == 0:
                count_filled[dist_2] += 1

    return [
        (sqrt(dist_2), count_filled[dist_2] / count_cells[dist_2])
        for dist_2 in sorted(count_cells.keys())
    ]


def estimate_density(densities):
    """Estimate linear fit for density vs. distance."""
    df = pd.DataFrame(densities, columns=["distance", "count"])
    return np.polyfit(df["distance"], df["count"], 1)


def measure_dimension(grid):
    """Estimate fractal dimension of grid."""
    assert grid.width() == grid.height()
    size = grid.width()
    grid = np.logical_not(np.array(grid.values(), dtype=bool))

    boxes = []
    ruler = 1
    while ruler < size:
        count = 0
        for x in range(size // ruler):
            for y in range(size // ruler):
                count = (
                    count
                    + grid[
                        (x * ruler) : ((x + 1) * ruler), (y * ruler) : ((y + 1) * ruler)
                    ].any()
                )
        boxes.append((ruler, count))
        ruler *= 2

    df = pd.DataFrame(boxes, columns=["ruler", "count"])
    dim = -np.polyfit(np.log(df["ruler"]), np.log(df["count"]), 1)[0]
    return dim
