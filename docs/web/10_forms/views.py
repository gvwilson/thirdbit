"""Manage HTML views."""

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError

from util import ViewException


Env = Environment(
    loader=FileSystemLoader("./templates"),
)


def all_staff(data):
    return _use_template("rows.html", data)


def _use_template(template_name, data):
    try:
        template = Env.get_template(template_name)
        return template.render(data=data)
    except TemplateError as exc:
        raise ViewException(f"template error: {exc}")
