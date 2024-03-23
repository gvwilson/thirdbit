"""Invasion percolation implementation utilities."""

import json
import random
import sys

from grid_list import GridList
from grid_array import GridArray


def get_params(filename, cls):
    """Get parameters."""
    with open(filename, "r") as reader:
        d = json.load(reader)
        return cls(**d)


def initialize_grid(params):
    """Prepare grid for simulation."""
    lookup = {
        "list": GridList,
        "array": GridArray,
    }
    assert params.kind in lookup, f"Unknown grid type {params.kind}"
    cls = lookup[params.kind]
    return cls(params.width, params.height, params.depth)


def initialize_random(params):
    """Initialize random number generation."""
    if params.seed is None:
        params.random.randrange(sys.maxsize)
    random.seed(params.seed)
