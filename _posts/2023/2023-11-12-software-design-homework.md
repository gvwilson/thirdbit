---
title: "Software Design Homework"
date: 2023-11-12
year: 2023
---

I'm giving a guest lecture this week in a course that's using the
Python version of [*Software Design by Example*][sdxpy] as a text,
and am thinking about assigning this as homework. Feedback would
be greatly appreciated.

1.  Clone the GitHub repository for the Python version of "Software
    Design by Example" from <https://github.com/gvwilson/sdxpy> and
    look in `./lib/mccole/extensions/includes.py`. This code is used
    to extract fragments of code from source files to include in the
    HTML that is generated for each chapter.

2.  `includes.py` works by searching for specially-formatted comments
    in source files. For example, if a Markdown file contains:

        [% inc file="example.py" keep="part" %]

    then `includes.py` will read `example.py` and extract the lines
    delimited by comments like this:

        # [part]
        ...code to include...
        # [/part]

3.  This mechanism works, but means that the source code is littered
    with comments like those shown above. A common alternative approach
    is to specify sections with line numbers like this:

        [% inc file="example.py" start="20" end="36" %]

    However, that is very fragile: if any lines are added to or
    removed from the file, all of the inclusion specifications may
    need to be updated.

4.  We can do better by taking advantage of the fact that the source
    code of a program is structured as a tree. We have several
    notations for selecting things from trees, the most widely used of
    which is CSS. For example, the CSS shown below

        div#example p.title {
            text-align: right;
            font-size: var(--tinytext);
            font-style: italic;
        }

    only applies to paragraphs with the class `title` located inside
    the `div` whose ID is `example`.

5.  Your assignment is to design and implement a tool for extracting
    bits of code from Python files inspired by tools like `pyastgrep`
    (see <https://github.com/spookylukey/pyastgrep/>).  Given a Python
    file like this:

        import sys

        def distractor():
            return None

        def example(param):
            value = 0
            while value < param:
                value *= 2
            while value % 3 != 0:
                value += 1
            return value

    and the selector:

        func[name="example"] body stmt[2:]

    your tool should return the three lines:

            while value % 3 != 0:
                value += 1
            return value

    because:

    a.  `func[name="example"]` selects the function whose name is
        `example`.

    b.  `body` selects the body of that function.

    c.  `stmt[2:]` select statements from the second to the end.
        (`stmt[0]` is the initial assignment to `value` and `stmt[1]`
        is the first `while` loop.)

6.  You may break the work down however you want, but we suggest
    tackling it in three parts:

    a.  A parser that turns selectors like the one shown above into
        one or more objects (see the chapter on parsing for an
        example).

    b.  A set of related classes that know how to match parts of a
        Python AST (see <https://docs.python.org/3/library/ast.html>)
        and return a set of lines (see the chapter on globbing for
	an example).

    c.  A comprehensive set of test cases for parts (a) and (b).

7.  The first step in this assignment is to decide what kinds of
    selection your tool will support and how that will be represented
    as selectors. For example:

    -   Will users be able to ask for the docstring of a particular
        method in a particular class?

    -   Will they be able to ask for *all* the docstrings of *all* the
        methods in a particular class?

    -   Will they be able to ask for just a class header without any of
        its methods?

    -   Will they be able to ask for a class and all its methods
        *except* all the methods whose names begin with a single
        underscore?

    None of these are required---it is up to your team to decide how
    simple or elaborate your selectors will be---but looking at
    examples of code extracts in your textbooks or in online examples
    will give you ideas about what authors will want to be able to do.

8.  Your solution must include:

    a.  A Markdown file describing the syntax and matching rules of
        the selectors you have implemented.

    b.  A test suite that covers 100% of the application code you
        have written (as determined by the Python `coverage` tool).

    Please note that particular attention will be paid to how, and
    how well, your library handles badly-written selectors, so make
    sure you test both correct and incorrect input.

[sdxpy]: {{'/sdxpy/' | relative_url}}
