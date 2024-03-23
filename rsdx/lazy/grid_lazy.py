"""Lazy-filling grid."""

import random

from grid_list import GridList


class GridLazy(GridList):
    """Only look at cells that might actually be filled next time."""

    def __init__(self, width, height, depth):
        """Construct and fill."""
        super().__init__(width, height, depth)
        self._candidates = {}

    def fill(self):
        """Fill grid one cell at a time."""
        x, y = self.width() // 2, self.height() // 2
        self[x, y] = 0
        num_filled = 1
        self.add_candidates(x, y)

        while True:
            x, y = self.choose_cell()
            self[x, y] = 0
            num_filled += 1
            if self.on_border(x, y):
                break
        return num_filled

    def choose_cell(self):
        """Choose the next cell to fill."""
        min_key = min(self._candidates.keys())
        available = list(sorted(self._candidates[min_key]))
        i = random.randrange(len(available))
        choice = available[i]
        del available[i]
        if not available:
            del self._candidates[min_key]
        else:
            self._candidates[min_key] = set(available)
        self.add_candidates(*choice)
        return choice

    def add_candidates(self, x, y):
        """Add candidates around (x, y)."""
        for ix in (x - 1, x + 1):
            self.add_one_candidate(ix, y)
        for iy in (y - 1, y + 1):
            self.add_one_candidate(x, iy)

    def add_one_candidate(self, x, y):
        """Add (x, y) if suitable."""
        if (x < 0) or (x >= self.width()) or (y < 0) or (y >= self.height()):
            return
        if self[x, y] == 0:
            return

        value = self[x, y]
        if value not in self._candidates:
            self._candidates[value] = set()
        self._candidates[value].add((x, y))
