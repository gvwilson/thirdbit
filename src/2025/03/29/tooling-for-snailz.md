---
title: Tooling for Snailz
date: 2025-03-29
---

I built [a synthetic data generator][snailz] last year to use in a "software design for data scientists" tutorial
that I never finished writing.
Over the last week I rewrote it as a way of exploring some new tools:

-   The command-line interface to [Claude][claude].
    I'm disgusted by the amorality of the AI industry,
    but am now convinced that the coding tools are here to stay:
    writing tests and refactoring code with Claude's help was *much* faster than doing it by hand.

-   [`uv`][uv] for managing the packages and virtual environment and for running commands.
    It's the first time I've used it as itself rather than running `uv pip whatever`;
    never going back.

-   [`ruff`][ruff] and [`pyright`][pyright] for checking the code.
    `ruff` is a joy,
    but checking type annotations with `pyright` cost me a couple of hours.
    It's not the tool's fault, though:
    figuring out how to annotate the last 5% of the code led to me writing my first [protocol][python-protocol]
    and then throwing up my hands and replacing it with `Any`.

-   [`pydantic`][pydantic] for storing and validating records,
    including the data that `snailz` generates and the parameters used in generation.
    I started with [`dataclasses`][dataclasses],
    but switched as soon as I found myself[^1] adding methods that `pydantic` already had.

-   [`doit`][doit] to run commands instead of [Make][gnu-make].
    I'm more comfortable with the latter,
    but I recognize that writing Makefiles is a dying art.

-   [`mkdocs`][mkdocs] for documentation instead of [Sphinx][sphinx] or [`pdoc`][pdoc][^2].
    I find `mkdocs` easier to work with than Sphinx,
    and `pdoc` doesn't support "extra" Markdown pages as well as `mkdocs`.
    (If the folks at [Astral][astral] are looking for new product ideas,
    a better documentation generator would have at least one paying customer the day it launched…)

-   [`pytest`][pytest], [`pyfakefs`][pyfakefs], and [`faker`][faker] for testing
    and [`click`][click] for building the command-line interface instead of [`argparse`][argparse].

[^1]: Well, myself and Claude…

[^2]: Please don't ever use `pdoc3`: someone who picks a swastika as a project logo and then argues that it's just a cultural symbol doesn't deserve your downloads.

[argparse]: https://docs.python.org/3/library/argparse.html
[astral]: https://astral.sh/
[claude]: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview
[click]: https://click.palletsprojects.com/
[dataclasses]: https://docs.python.org/3/library/dataclasses.html
[doit]: https://pydoit.org/
[faker]: https://faker.readthedocs.io/
[gnu-make]: https://www.gnu.org/software/make/
[mkdocs]: https://www.mkdocs.org/
[pdoc]: https://pdoc.dev/
[pydantic]: https://docs.pydantic.dev/
[pyfakefs]: https://pypi.org/project/pyfakefs/
[pyright]: https://pypi.org/project/pyright/
[pytest]: https://docs.pytest.org/
[python-protocol]: https://peps.python.org/pep-0544/
[ruff]: https://docs.astral.sh/ruff/
[snailz]: https://github.com/gvwilson/snailz
[sphinx]: https://www.sphinx-doc.org/
[uv]: https://docs.astral.sh/uv/
