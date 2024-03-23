"""Test grid operations."""

from grid_filled import GridFilled


def test_explicit_filling_fills_correctly():
    g = GridFilled(3, 3, 4, [[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    assert g.width() == 3
    assert g.height() == 3
    assert g.depth() == 4
    for x in range(g.width()):
        assert all(g[x, y] == x + 1 for y in range(g.height()))


def test_filling_with_straight_run_to_edge():
    g = GridFilled(3, 3, 4, [[4, 1, 4], [4, 4, 4], [4, 4, 4]])
    g.fill()
    assert g == GridFilled(3, 3, 4, [[4, 0, 4], [4, 0, 4], [4, 4, 4]])
