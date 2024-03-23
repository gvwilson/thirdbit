"""Parameters for invasion percolation sweep."""

from dataclasses import dataclass


@dataclass
class ParamsSweep:
    """A range of invasion percolation parameters."""

    size: list[int]
    depth: list[int]
    runs: int
    seed: int = None
