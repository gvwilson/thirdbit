"""Invasion percolation in Python."""

import csv
import sys
import time

from invperc_util import get_params, initialize_grid, initialize_random
from params_single import ParamsSingle
from params_sweep import ParamsSweep


COLUMNS = ("kind", "width", "height", "depth", "num_filled", "time")


def main():
    """Main driver."""
    params = get_params(sys.argv[1], ParamsSweep)
    initialize_random(params)
    results = []
    for p in generate_sweep(params):
        print(p)
        grid = initialize_grid(p)
        t_start = time.time()
        num_filled = grid.fill()
        t_elapsed = time.time() - t_start
        results.append(record_result(p, num_filled, t_elapsed))
    save_results(params, results)


def generate_sweep(params):
    """Generate next single parameter object."""
    for kind in params.kind:
        for size in params.size:
            for depth in params.depth:
                for run in range(params.runs):
                    yield ParamsSingle(kind, size, size, depth)


def record_result(params, num_filled, elapsed):
    """Record results of a single sweep."""
    return (params.kind, params.width, params.height, params.depth, num_filled, elapsed)


def save_results(params, results):
    """Display results as CSV."""
    kinds = "k+" + "+".join(k for k in params.kind)
    sizes = "z+" + "+".join(str(s) for s in params.size)
    depths = "d+" + "+".join(str(d) for d in params.depth)
    runs = f"r+{params.runs}"
    seed = f"s+{params.seed}"
    filename = f"{kinds}_{sizes}_{depths}_{runs}_{seed}.csv"
    with open(filename, "w") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(COLUMNS)
        writer.writerows(results)


if __name__ == "__main__":
    main()
