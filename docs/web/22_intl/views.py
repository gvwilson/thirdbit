"""Manage HTML views."""

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError

from util import ViewException, get_translations


SUPPORTED_LANGUAGES = ["uc", "en"]


Env = Environment(
    loader=FileSystemLoader("./templates"),
)


def all_staff(data, accept_languages):
    return _use_template("staff.html", data, accept_languages)


def experiments(data, accept_languages, staff_id):
    return _use_template("experiments.html", data, accept_languages, staff_id=staff_id)


def heartbeat(data, accept_languages):
    return _use_template("heartbeat.html", data, accept_languages)


def _use_template(template_name, data, accept_languages, **kwargs):
    try:
        template = Env.get_template(template_name)
        lang = accept_languages.best_match(SUPPORTED_LANGUAGES)
        translator = get_translations().translator(lang)
        template.globals.update({"_": translator})
        return template.render(data=data, **kwargs)
    except TemplateError as exc:
        raise ViewException(f"template error: {exc}")
