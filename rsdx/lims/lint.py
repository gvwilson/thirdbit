"""Run checks on assay data."""

import argparse
from pathlib import Path

import numpy as np

from assay_params import load_params


DATA_SHAPE = (7, 5)
MACHINE_HEADER = "Weyland-Yutani 470"


def main():
    """Main driver."""
    args = parse_args()
    params = load_params(args.params)

    design_files = load_all_files(args.designs)
    assay_files = load_all_files(args.assays)

    messages = lint_all(args)
    for filename, data in design_files.items():
        messages.extend(lint_design(params, filename, data))
    for filename, data in assay_files.items():
        messages.extend(lint_assay(params, filename, data))

    for m in messages:
        print(m)


def lint_all(args):
    """Do global linting."""
    messages = []
    for name, func in globals().items():
        if name.startswith("_lint_all_") and callable(func):
            messages.extend(func(args))
    return messages


def lint_assay(params, filename, data):
    """Run checks on a single assay file."""
    return lint_single_file(params, "_lint_assay_", filename, data)


def lint_design(params, filename, data):
    """Run checks on a single design file."""
    return lint_single_file(params, "_lint_design_", filename, data)


def lint_single_file(params, prefix, filename, data):
    """Do one kind of linting on a single set of files."""
    messages = []
    for name, func in globals().items():
        if name.startswith(prefix) and callable(func):
            messages.extend(func(params, filename, data))
    return messages


def load_all_files(dirpath):
    """Load all files in directory."""
    return {filename: load_file(filename) for filename in Path(dirpath).iterdir()}


def load_file(filename):
    """Load design or assay file as numpy array."""
    return np.loadtxt(filename, delimiter=",", dtype="str")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--assays", type=str, required=True, help="assay results directory"
    )
    parser.add_argument(
        "--designs", type=str, required=True, help="assay designs directory"
    )
    parser.add_argument(
        "--params", type=str, required=True, help="assay parameters file"
    )
    return parser.parse_args()


def _lint_all_match(args):
    """Do design and result files match 1-1?"""
    design_files = set(p.name for p in Path(args.designs).iterdir())
    assay_files = set(p.name for p in Path(args.assays).iterdir())
    messages = []
    for title, files in (
        ("design but not assay", design_files - assay_files),
        ("assay but not design", assay_files - design_files),
    ):
        if files:
            files = sorted(str(f) for f in files)
            messages.append(f"in {title}: {', '.join(files)}")
    return messages


def _lint_assay_data_shape(params, filename, data):
    """Check shape of assay data."""
    if data.shape != DATA_SHAPE:
        return [f"assay file {filename} has wrong shape {data.shape}"]
    return []


def _lint_assay_machine_header(params, filename, data):
    """Check shape of assay data."""
    if data[0, 0] != MACHINE_HEADER:
        return [f"assay file {filename} has wrong machine header {data[0, 0]}"]
    return []


def _lint_design_data_contents(params, filename, data):
    """Check contents of data portion of file."""
    allowed = {params.treatment} | set(params.controls)
    unknown = set(data[3:7, 1:5].flatten()) - allowed
    if unknown:
        return [
            f"design file {filename} has unknown value(s) {', '.join(sorted(unknown))}"
        ]
    return []


def _lint_design_data_shape(params, filename, data):
    """Check shape of assay design."""
    if data.shape != DATA_SHAPE:
        return [f"design file {filename} has wrong shape {data.shape}"]
    return []


if __name__ == "__main__":
    main()
