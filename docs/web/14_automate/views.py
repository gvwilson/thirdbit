"""Manage HTML views."""

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError
from flask import render_template_string

from util import ViewException

Env = Environment(
    loader=FileSystemLoader("./templates"),
)


def all_staff(data):
    return _use_template("staff.html", data)


def experiments(data, staff_id):
    return _use_template("experiments.html", data, staff_id=staff_id)

def heartbeat(data):
    return render_template_string("<p>{{ message }}</p>", message=data["message"])


def _use_template(template_name, data, **kwargs):
    try:
        template = Env.get_template(template_name)
        return template.render(data=data, **kwargs)
    except TemplateError as exc:
        raise ViewException(f"template error: {exc}")
