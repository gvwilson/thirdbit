import pytest
from jinja2 import Template

from util import Translation


@pytest.fixture
def lookup_table():
    return {
        "up": {
            "eu": "gora",
        },
        "down": {
            "eu": "behera",
        },
    }


def test_pure_extension_function():
    def func(arg):
        return arg.upper()

    template = Template("left {{func('middle')}} right")
    template.globals.update({"func": func})
    actual = template.render()
    assert actual == "left MIDDLE right"


def test_using_lookup_dict_other_lang(lookup_table):
    translator = Translation(lookup_table).translator("eu")
    template = Template("left {{ _('up') }} right")
    template.globals.update({"_": translator})
    actual = template.render()
    assert actual == "left gora right"


def test_using_lookup_dict_key_lang(lookup_table):
    translator = Translation(lookup_table).translator("en")
    template = Template("left {{ _('up') }} right")
    template.globals.update({"_": translator})
    actual = template.render()
    assert actual == "left up right"


def test_using_lookup_file():
    translator = Translation("test_translation.json").translator("eu")
    template = Template("left {{ _('down') }} right")
    template.globals.update({"_": translator})
    actual = template.render()
    assert actual == "left behera right"
