---
title: "Language and Library Features for Teaching"
date: 2023-08-10
year: 2023
---

I've written [several posts][features] in the past couple of years about
the minimal set of features I need in a language
in order to write books like
[*Software Design by Example*][sdxjs]
and [its upcoming translation into Python][sdxpy].
As the latter nears completion,
I thought it might be helpful to itemize
the libraries I need as well;
if you're building the standard library for a new language,
these might be a good place to start.
In order of priority, books like these need:

-   system utilities (command-line arguments, environment variables, etc.)
-   date/time handling
-   fixtures and mock objects for testing
-   globbing
-   file and path manipulation
-   HTML parser (e.g., BeautifulSoup)
-   CSV, JSON, and YAML (in that order)
-   hashing (e.g., SHA-256)
-   basic math functions
-   introspection (e.g., Python's `inspect` and `ast` modules)
-   HTTP request handling
-   string I/O
-   packing and unpacking binary data
-   a minimal HTTP server
-   terminal window control (e.g., `curses`)
-   dataframes (for analyzing performance data)
-   pretty-printing data structures
-   a plotting library (I realize this is probably too big for the standard library)

[features]: {{ '/2023/03/04/the-only-features-i-need/' | relative_url }}
[sdxjs]: {{ '/sdxjs/' | relative_url}}
[sdxpy]: {{ '/sdxpy/' | relative_url}}
