"""Test grid operations."""

from grid_array import GridArray
from grid_list import GridList


def test_grid_array_constructed_correctly():
    g = GridArray(2, 3, 4)
    assert g.width() == 2
    assert g.height() == 3
    assert g.depth() == 4
    for x in range(g.width()):
        for y in range(g.height()):
            assert g[x, y] > 0


def test_grid_list_constructed_correctly():
    g = GridList(2, 3, 4)
    assert g.width() == 2
    assert g.height() == 3
    assert g.depth() == 4
    for x in range(g.width()):
        for y in range(g.height()):
            assert g[x, y] > 0
