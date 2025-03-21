"""Generate migration to encrypt passwords."""

import argparse
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from pypika import Query, Table

from models import connect
from util import encrypt_password, make_secret


Env = Environment(
    loader=FileSystemLoader("."),
)


def main():
    """Main driver."""
    opt = parse_args()

    secret = opt.secret_value if opt.secret_value else make_secret()
    Path(opt.secret).write_text(secret)

    connection = connect()
    staff = Table("staff")
    query = Query.from_(staff).select(staff.staff_id, staff.password)
    all_staff = connection.execute(str(query)).fetchall()
    data = [
        {
            "staff_id": s["staff_id"],
            "password": s["password"],
            "encrypted": encrypt_password(secret, s["password"]),
        }
        for s in all_staff
    ]

    for template_path in (opt.fwd, opt.bwd):
        template = Env.get_template(template_path)
        sql = template.render(data=data)
        Path(opt.migrations, template_path).write_text(sql)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--bwd", type=str, required=True, help="backward migration template")
    parser.add_argument("--fwd", type=str, required=True, help="forward migration template")
    parser.add_argument("--migrations", type=str, required=True, help="migrations directory")
    parser.add_argument("--secret", type=str, required=True, help="where to store secret")
    parser.add_argument("--secret-value", type=str, help="secret value to use (optional)")
    return parser.parse_args()

if __name__ == "__main__":
    main()
