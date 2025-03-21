"""Render the plate designer from a template."""

import argparse
from jinja2 import Environment, FileSystemLoader


DOSAGES = ["5μL", "10μL", "20μL", "50μL"]
TREATMENTS = ["CQZ-1718", "CQA-986", "CQA-940", ""]


Env = Environment(
    loader=FileSystemLoader("."),
)


def main():
    """Main driver."""
    opt = parse_args()
    data = {
        "cols": "ABCD",
        "rows": "1234",
        "treatments": TREATMENTS,
        "dosages": DOSAGES,
    }
    template = Env.get_template(opt.template)
    print(template.render(**data))


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=str, required=True, help="SQL template")
    return parser.parse_args()


if __name__ == "__main__":
    main()
