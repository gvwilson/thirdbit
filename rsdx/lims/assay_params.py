"""Assay parameters dataclass."""

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import List


@dataclass
class Params:
    """Parameters for assay data."""

    treatment: str = None
    controls: List[str] = field(default_factory=list)


def load_params(filename):
    """Load parameters from file."""
    return Params(**json.loads(Path(filename).read_text()))
