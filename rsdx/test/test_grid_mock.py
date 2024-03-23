"""Test grid operations."""

from unittest.mock import patch

from grid_list import GridList


def test_grid_list_patching_randomization():
    with patch("random.randint", return_value=12345):
        g = GridList(2, 3, 4)

    assert g.width() == 2
    assert g.height() == 3
    assert g.depth() == 4
    for x in range(g.width()):
        for y in range(g.height()):
            assert g[x, y] == 12345
