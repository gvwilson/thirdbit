"""Test grid operations."""

from unittest.mock import patch

import pytest

from grid_array import GridArray
from grid_list import GridList


@pytest.mark.parametrize("cls", [GridArray, GridList])
def test_grid_list_parameterizing_classes(cls):
    with patch("random.randint", return_value=12345):
        g = cls(2, 3, 4)

    assert g.width() == 2
    assert g.height() == 3
    assert g.depth() == 4
    for x in range(g.width()):
        for y in range(g.height()):
            assert g[x, y] == 12345
