"""Parameters for single invasion percolation sweep."""

from dataclasses import dataclass


@dataclass
class ParamsSingle:
    """A single set of invasion percolation parameters."""

    kind: str
    width: int
    height: int
    depth: int
    seed: int = None
