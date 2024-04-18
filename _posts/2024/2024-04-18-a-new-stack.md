---
title: "A New Stack"
date: 2024-04-18
year: 2024
---

I'm tired of teaching tools that are older than most of the people learning them,
but:

1.  if I teach something that isn't (yet) widely used,
    my learners won't be able to collaborate with their colleagues,
    and

2.  most new tools will never catch on.

That said,
people don't seem to be excited by
the outline I've sketched for [*Research Software Design by Example*][rsdx],
so I can either:

1.  add it to my ever-growing list of books I've started but not finished,
    or

2.  make it more exciting by using a new set of tools.

I can't reach too far ahead if I do the latter,
which makes tool selection a balancing act.
I'd be grateful for [feedback](mailto:{{site.author.email}}) on the list below.

| Old                | New                  | Because                                                 |
| ------------------ | -------------------- | ------------------------------------------------------- |
| [Bash][bash]       | [Nushell][nushell]   | risky, but [Fish][fish] feels too conservative          |
| [Git][git]         | sadly, still Git     | I really wish [Gitless][gitless] had taken off…         |
| [Make][make]       | ???                  | none of the (many) alternatives are a clear winner      |
| [SQLite][sqlite]   | [DuckDB][duckdb]     | a better choice for data science?                       |
| [Python][python]   | still Python         | people need to be able to get real work done            |
| [Pandas][pandas]   | [Polars][polars]     | better ergonomics and performance                       |
| [Seaborn][seaborn] | [Plotly][plotly]      | I like it so much that I joined the company :-)         |
| [Jupyter][jupyter] | [Marimo][marimo]     | also risky, but it really does feel like a step forward |
| [LaTeX][latex]     | ???                  | maybe [Typst][typst] if they open source the GUI?       |
| —                  | [Metaflow][metaflow] | the most Pythonic option available                      |
| —                  | [DVC][dvc]           | preferred to [Git-LFS][git-lfs]                         |
| —                  | [Ark][ark]           | the best little Python SSG I've found                   |
| —                  | [VSCode][vscode]     | mostly for the debugger                                 |
| —                  | [Docker][docker]     | as ubiquitous as Git but much less user-hostile         |

What's missing:

-   Something for creating diagrams that supports diff and merge.
    (No, I'm not going to teach [a text-to-diagram compiler][why-i-draw].)

-   Something on top of that for making slideshows
    (ideally an extension to Marimo, but that depends on diff and merge for diagrams).

-   I have no idea what to teach people right now about building interactive GUIs.
    The answer two years ago was [JavaScript][js],
    but [WebAssembly][wasm] may or may not enable people to use Python instead—i.e.,
    to avoid the considerable overhead of learning a second programming language.
    I don't know what that means for [React][react] versus [Elm][elm] versus [htmx][htmx]
    versus any of a dozen things I don't even know I should be paying attention to…

-   I also have no idea what to teach people about LLMs,
    but find consolation in knowing that no-one else does either.

[ark]: https://www.dmulholl.com/docs/ark/main/
[bash]: https://www.gnu.org/software/bash/
[docker]: https://www.docker.com
[duckdb]: https://duckdb.org
[dvc]: https://dvc.org
[elm]: https://elm-lang.org
[fish]: https://fishshell.com
[git]: https://git-scm.com
[git-lfs]: https://git-lfs.com
[gitless]: https://gitless.com
[htmx]: https://htmx.org
[js]: https://en.wikipedia.org/wiki/JavaScript
[jupyter]: https://jupyter.org
[latex]: https://www.latex-project.org
[make]: https://www.gnu.org/software/make/
[marimo]: https://marimo.io
[metaflow]: https://metaflow.org
[nushell]: https://www.nushell.sh
[pandas]: https://pandas.pydata.org
[plotly]: https://plotly.com/graphing-libraries/
[polars]: https://pola.rs
[python]: https://www.python.org
[react]: https://react.dev
[rsdx]: https://gvwilson.github.io/rsdx/
[seaborn]: https://seaborn.pydata.org
[sqlite]: https://sqlite.org
[typst]: https://typst.app
[vscode]: https://code.visualstudio.com
[wasm]: https://en.wikipedia.org/wiki/WebAssembly
[why-i-draw]: {{'/2024/03/01/why-i-draw/' | relative_url}}
