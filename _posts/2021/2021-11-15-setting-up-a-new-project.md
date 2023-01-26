---
title: "Setting Up a New Project"
date: 2021-11-15
year: 2021
---

I recently helped a group of about fifteen people set up a new research software engineering project
(where by "new" I mean "restart something that was in bits and pieces scattered across half the internet").
They all had GitHub accounts already,
and a couple of them had read *[Research Software Engineering with Python](https://merely-useful.tech/py-rse/)*,
but only one had any formal training as a programmer
(a 12-week bootcamp four years ago).
Here's what we did in order—I'd be grateful for suggestions about what we missed
or what you would reprioritize.

<div class="tightlist" markdown="1">
1.  Create a mailing list for the project.
    -   The team voted 2:1 for email over Slack because they want better search and fewer interruptions.
1.  Create a new GitHub organization for the project and add everyone to it.
    -   So that nothing belonging to the project is under a personal account.
1.  Create a new repo within that GitHub organization.
    -   Everything is in one repo for now, but that might change.
1.  Redefine the tags in that repo.
    -   Governance: `discussion` (including questions) and `proposal` (for votable items).
    -   Issues: `bug` and `request`.
    -   Pull requests: `fix`, `enhancement`, `docs`, and `refactor`.
    -   Meta: `paused`, `helped wanted`, `good first issue`.
1.  Add `README`, `LICENSE`, `CODE_OF_CONDUCT`, `GOVERNANCE`, `Makefile`, and `.gitignore` to the repo.
    -   We settled on Make because nobody could agree on what to use instead.
1.  Create two `pip` requirements files:
    -   `requirements.txt` is a minimal setup for using the software.
    -   `development.txt` sources that and adds everything needed for building, testing, and documenting.
1.  Create `socks`, `docs`, and `tests` directories in the root of the repo along with a `setup.py` file.
    -   Pretty standard structure for a `pip`-installable Python package (and no, "socks" isn't its real name).
1.  Set up `pytest` for running tests and `pdoc` for building documentation.
    -   `tests/conftest.py` for `pytest`.
    -   A docstring in every `__init__.py` file (rather than leaving it empty) to make `pdoc` happy.
    -   Use [Google-style docstrings](https://gist.github.com/redlotus/3bc387c2591e3e908c9b63b97b11d24e).
1.  Add targets to `Makefile` to:
    -   Build the package.
    -   Run the tests.
    -   Run the tests with coverage and display the coverage report (to identify untested code).
    -   Rebuild the documentation.
    -   Run `flake8`, `black`, and `isort` to check that the code meets style guidelines.
1.  Add a `workflow.yml` file with pre-commit checks.
1.  Add a script that uses [Jinja2](https://palletsprojects.com/p/jinja/) to turn hand-written documentation into HTML.
    -   The team has Markdown design notes and the beginnings of a tutorial that they want to put beside the `pdoc` docs.
    -   And a `glossary.md` file in [glosario](https://github.com/carpentries/glosario) format.
1.  Add a `data` directory with sample data for testing and a couple of real datasets.
    -   Each dataset is in its own subdirectory with a `MANIFEST.yml` file describing files, columns, provenance, etc.
1.  Add a `CITATION.cff` file with citation information.
    -   And make sure every contributor has an ORCID.
1.  Add a `bin` directory at the top level with various utility scripts.
    -   Most of which use the code in the `socks` directory directly (rather than through a local install of the package).
1.  Add a `results` directory at the top level with one sub-directory for each paper the team intends to produce.
    -   Each sub-directory under `results` has its own `Makefile`.
    -   `make all` in the project sub-directory regenerates everything.
    -   We haven't added a [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template yet, but we will.
1.  Add another Jinja2 script to convert CSV results files into HTML pages.
1.  Add a `static` directory with some CSS and JavaScript files.
    -   Because everyone wants their HTML tables to be dynamically sortable…
1.  Add a BibTeX file to the root `results` directory to be used by all project papers.
1.  Write a short code review checklist.
    -   How to run pre-commit checks, how and why to use the `logging` library, what exceptions to use for what, etc.
1.  Add a small utility script for loading program configurations.
    -   In order: system config, personal config, project config, config file specified on the command line, command-line flags.
1.  Choose a project logo.
    -   Which made discussion of build tools look calm and rational…
</div>

<em markdown="1">
Later: things people have suggested that we didn't include:

- a list of supported platforms (FlavorOfLinux, OS X Version, etc.) 
- a list of supported Python versions
- instructions for setting up, say, virtualenv, to make sure users are all on the same Python version
</em>
