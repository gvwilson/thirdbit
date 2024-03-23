"""Re-run everything."""

from collections import defaultdict
import csv
import json
from pathlib import Path
import random
import sys

from metaflow import FlowSpec, Parameter, step

from invperc import invperc
from measure import collect_density, estimate_density, measure_dimension
from params_single import ParamsSingle
from params_sweep import ParamsSweep


class InvPercFlow(FlowSpec):
    """Metaflow for invasion percolation."""

    sweep = Parameter("sweep", help="sweep parameter file", type=str, required=True)

    @step
    def start(self):
        """Collect parameters and run jobs."""
        sweep = load_params(self.sweep)
        self.args = make_sweeps(sweep)
        self.next(self.run_job, foreach="args")

    @step
    def run_job(self):
        """Run a sweep with one set of parameters."""
        grid = invperc(self.input)
        self.result = {
            "size": grid.width(),
            "depth": grid.depth(),
            "density": collect_density(grid),
            "dimension": measure_dimension(grid),
        }
        self.next(self.join)

    @step
    def join(self, inputs):
        """Combine results from all sweeps."""
        counts = defaultdict(int)
        dimensions = defaultdict(float)
        densities = defaultdict(list)

        for i in inputs:
            key = (i.result["size"], i.result["depth"])
            counts[key] += 1
            dimensions[key] += i.result["dimension"]
            densities[key].extend(i.result["density"])

        for key in densities:
            densities[key] = estimate_density(densities[key])

        self.results = {
            "counts": counts,
            "dimensions": dimensions,
            "densities": densities,
        }
        self.next(self.end)

    @step
    def end(self):
        """Report results."""
        table = [("size", "depth", "count", "dimension", "density_x", "density_k")]
        for key, count in sorted(self.results["counts"].items()):
            size, depth = key
            dim = self.results["dimensions"][key] / count
            table.append((size, depth, count, dim, *self.results["densities"][key]))
        csv.writer(sys.stdout, lineterminator="\n").writerows(table)


def load_params(filename):
    """Get sweep parameters from file."""
    return ParamsSweep(**json.loads(Path(filename).read_text()))


def make_sweeps(sweeps):
    """Convert sweep parameters into individual jobs."""
    random.seed(sweeps.seed)
    result = []
    for size in sweeps.size:
        for depth in sweeps.depth:
            for run in range(sweeps.runs):
                result.append(
                    ParamsSingle(
                        width=size,
                        height=size,
                        depth=depth,
                        seed=random.randrange(sys.maxsize),
                    )
                )
    return result


if __name__ == "__main__":
    InvPercFlow()
