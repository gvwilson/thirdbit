"""Test grid operations."""

from grid_list_randomizer import GridListRandomizer


def test_grid_list_with_randomizer_function():
    def r(low, high):
        return 12345

    g = GridListRandomizer(2, 3, 4, r)
    assert g.width() == 2
    assert g.height() == 3
    assert g.depth() == 4
    for x in range(g.width()):
        for y in range(g.height()):
            assert g[x, y] == 12345
