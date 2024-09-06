---
title: "How I Explain Code"
date: 2024-09-06
year: 2024
---

I recently built a very small static site generator because…
well, the reasons don't matter (and aren't actually compelling),
but sharing it with someone gave me an opportunity to think about
how I explain my code to someone else.
The explanation is below and the code follows;
I hope it's useful.

-   Start with the `main()` function
    -   Parse command-line arguments and store the result in `opt`
    -   Create an `Environment` for loading templates (explained below)
    -   Create a set called `skip` of top-level directories to ignore
    -   Find all the files that need to be rendered or just copied
    -   For each file:
        -   If it's a Markdown file, render it
        -   Otherwise, copy it

-   So what' an "environment"?
    -   This program uses Jinja2 to stuff content into HTML templates
    -   Jinja2 needs to know where to find the HTML templates
    -   So we create an `Environment` with a `FileSystemLoader`
        and tell that `FileSystemLoader` where to look
    -   `opt` holds the result of parsing command-line arguments,
        and `opt.templates` is the path to the templates directory

-   Now let's take a look at `find_files()`
    -   It returns a dictionary whose keys are file paths
        and whose values are the contents of those files
    -   It uses a dictionary comprehension to do this instead of a loop
        -   First line of the comprehension specifies key and value
        -   Second line is what to look at
        -   Third is the condition for inclusion
    -   We use `read_file()` to read a file
        -   If the file is a text file, use `read_text()`
        -   Otherwise, use `read_bytes()` (e.g., for images)
    -   To find files we *might* be interested in we use a "glob"
        -   The name is short for "global" and is old-fashioned Unix terminology
        -   `opt.root` is the root directory of our project
        -   The pattern `**/*.*` matches everything in subdirectories (`**/`)
            with a two-part name (`*.*`)
    -   The condition in the dictionary comprehension uses a function
        `is_interesting_file()`
        -   If you're not a file, you're not interesting
        -   If your name starts with `.` (as in `.gitignore`),
            you're not interesting
        -   If your suffixes isn't in `SUFFIXES` (defined at the top of the file),
            you're not interesting
        -   If your parent directory's name starts with `.` (as in `.git`),
            you're not interesting
        -   If we have a set of things to skip
            and your path starts with one of those things,
            you're not interesting
        -   Otherwise, OK, fine, you're interesting

-   Back to `main()` and the loop over files
    -   If the file *isn't* Markdown, we just copy it
    -   …after making sure the output directory exists

-   And finally, `render_markdown()`
    -   Use a library function `markdown()` to convert Markdown to HTML
        -   `MARKDOWN_EXTENSIONS` (defined at the top of the file)
            is a list of extra features we want to enable,
            such as Markdown tables
    -   Next, load the `page.html` template
        -   A more sophisticated tool would allow authors to specify a template
            in the header of the Markdown file or as a command-line argument
    -   Then ask the template to take the HTML produced from the Markdown
        and stuff it into the HTML template we just loaded
        -   `page.html` has a placeholder `{{content}}` to show where

-   We could stop here, but we want to fix up the generated HTML a bit
    -   So we parse the HTML produced by Jinja2 using Beautiful Soup
        to get a tree of objects in memory (as opposed to a great big string)
    -   And then apply several functions to it in order
    -   Each of these functions take the current document tree
        and returns a modified one
    -   Once that's done, we make sure the output directory exists
        and then write the document tree as HTML text
        -   Potentially renaming it from upper case to lower case

-   So what are these transformations?
    -   `do_markdown_links()` finds hyperlinks to `.md` files
        and turns them into hyperlinks to `.html` files
        -   We write hyperlinks to `.md` files in the source
            so that files will inter-link correctly when viewed on GitHub
        -   But our final website will have `.html` files,
            so we need to convert
    -   `do_root_path_prefix()` looks for links whose names start with `@root`
        and turn them into relative links up to the root directory of the project
        -   For example, `@root/static/page.css` becomes `./static/page.css`
            if the Markdown file in in the root directory of the project
            but `../../static/page.css` if the file is two levels down
    -   `do_title()` finds the `H1` heading in the HTML page
        and copies its contents into the `<title>` element of the page
    -   We can easily add more transformation functions
        -   And in fact the full version of this program has transformers
            to handle bibliography citations and glossary references

-   In answer to a couple of questions:
    -   I organize code more-or-less alphabetically out of habit;
        I know people who try to organize in calling order,
        but that breaks down as soon as you have utility functions that are called in multiple places.
    -   I *explain* code more or less in execution order

```py
"""Convert a pile of Markdown files to HTML."""

import argparse
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from markdown import markdown
from pathlib import Path


MARKDOWN_EXTENSIONS = ["attr_list", "def_list", "fenced_code", "md_in_html", "tables"]
SUFFIXES_BIN = {".ico", ".jpg", ".png"}
SUFFIXES_SRC = {".css", ".html", ".js", ".md", ".py", ".sh", ".txt"}
SUFFIXES_TXT = SUFFIXES_SRC | {".csv", ".json", ".svg"}
SUFFIXES = SUFFIXES_BIN | SUFFIXES_TXT

RENAMES = {
    "CODE_OF_CONDUCT.md": "code_of_conduct.md",
    "CONTRIBUTING.md": "contributing.md",
    "LICENSE.md": "license.md",
    "README.md": "index.md",
}


def main():
    """Main driver."""
    opt = parse_args()

    env = Environment(loader=FileSystemLoader(opt.templates))
    skips = {opt.out, opt.templates}

    files = find_files(opt, skips)
    for filepath, content in files.items():
        if filepath.suffix == ".md":
            render_markdown(env, opt.out, filepath, content)
        else:
            copy_file(opt.out, filepath, content)


def copy_file(output_dir, source_path, content):
    """Copy a file verbatim."""
    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_file(output_path, content)


def do_markdown_links(doc, source_path):
    """Fix .md links in HTML."""
    for node in doc.select("a[href]"):
        if node["href"].endswith(".md"):
            node["href"] = node["href"].replace(".md", ".html").lower()


def do_root_path_prefix(doc, source_path):
    """Fix @root links in HTML."""
    depth = len(source_path.parents) - 1
    prefix = "./" if (depth == 0) else "../" * depth
    targets = (
        ("a[href]", "href"),
        ("link[href]", "href"),
        ("script[src]", "src"),
    )
    for selector, attr in targets:
        for node in doc.select(selector):
            if "@root/" in node[attr]:
                node[attr] = node[attr].replace("@root/", prefix)


def do_title(doc, source_path):
    """Make sure title element is filled in."""
    doc.title.string = doc.h1.get_text()


def find_files(opt, skips=None):
    """Collect all interesting files."""
    return {
        filepath: read_file(filepath)
        for filepath in Path(opt.root).glob("**/*.*")
        if is_interesting_file(filepath, skips)
    }


def is_interesting_file(filepath, skips):
    """Is this file worth checking?"""
    if not filepath.is_file():
        return False
    if str(filepath).startswith("."):
        return False
    if filepath.suffix not in SUFFIXES:
        return False
    if str(filepath.parent.name).startswith("."):
        return False
    if (skips is not None) and any(str(filepath).startswith(s) for s in skips):
        return False
    return True


def make_output_path(output_dir, source_path):
    """Build output path."""
    if source_path.name in RENAMES:
        source_path = Path(source_path.parent, RENAMES[source_path.name])
    source_path = Path(str(source_path).replace(".md", ".html"))
    return Path(output_dir, source_path)


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="docs", help="output directory")
    parser.add_argument("--root", type=str, default=".", help="root directory")
    parser.add_argument("--templates", type=str, default="templates", help="templates directory")
    return parser.parse_args()


def read_file(filepath):
    """Read file as bytes or text."""
    if filepath.suffix in SUFFIXES_TXT:
        return filepath.read_text()
    else:
        return filepath.read_bytes()


def render_markdown(env, output_dir, source_path, content):
    """Convert Markdown to HTML."""
    html = markdown(content, extensions=MARKDOWN_EXTENSIONS)
    template = env.get_template("page.html")
    html = template.render(content=html)

    transformers = (
        do_markdown_links,
        do_title,
        do_root_path_prefix, # must be last
    )
    doc = BeautifulSoup(html, "html.parser")
    for func in transformers:
        func(doc, source_path)

    output_path = make_output_path(output_dir, source_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(doc))


def write_file(filepath, content):
    """Write file as bytes or text."""
    if filepath.suffix in SUFFIXES_TXT:
        return filepath.write_text(content)
    else:
        return filepath.write_bytes(content)


if __name__ == "__main__":
    main()
```
