"""Generate encrypted passwords for users."""

import argparse
from jinja2 import Environment, FileSystemLoader
from pypika import Query, Table
import random
import string

from models import connect


PIN_LENGTH = 4


Env = Environment(
    loader=FileSystemLoader("."),
)


def main():
    """Main driver."""
    opt = parse_args()
    random.seed(opt.seed)
    connection = connect()
    staff = Table("staff")
    query = Query.from_(staff).select(staff.staff_id, staff.personal, staff.family)
    all_staff = connection.execute(str(query)).fetchall()
    data = [
        {"staff_id": s["staff_id"], "username": make_username(s), "password": make_password()}
        for s in all_staff
    ]
    template = Env.get_template(opt.template)
    print(template.render(data=data))


def make_password():
    """Make a random password."""
    return "".join(random.choices(string.digits, k=PIN_LENGTH))


def make_username(staff):
    """Make username for staff member."""
    return f"{staff['personal'].lower()}.{staff['family'][0].lower()}"


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True, help="RNG seed")
    parser.add_argument("--template", type=str, required=True, help="SQL template")
    return parser.parse_args()



if __name__ == "__main__":
    main()
