---
title: "A New Stack"
date: 2024-04-18
---

I'm tired of teaching tools that are older than most of the people learning them,
butif I teach something that isn't (yet) widely used
my learners won't be able to collaborate with their colleagues,
and most new tools will never catch on.
That said,
people don't seem to be excited by
the outline I've sketched for [*Research Software Design by Example*][rsdx],
so I can either add it to my ever-growing list of books I've started but not finished
or make it more exciting by using a new set of tools.
I can't reach too far ahead if I do the latter,
which makes tool selection a balancing act.
I'd be grateful for [feedback](mailto:gvwilson@third-bit.com) on the list below.

| Old                | New                  | Because                                                 | Modified   |
| ------------------ | -------------------- | ------------------------------------------------------- | ---------- |
| [Bash][bash]       | [Nushell][nushell]   | risky, but [Fish][fish] feels too conservative          |            |
| [Git][git]         | sadly, still Git     | I really wish [Gitless][gitless] had taken off…         |            |
| [Make][make]       | [Just][just]         | finally, a better build tool I can believe in           | 2024-04-19 |
| [SQLite][sqlite]   | [DuckDB][duckdb]     | a better choice for data science?                       |            |
| [Python][python]   | still Python         | despite the mess that is Python packaging               |            |
| [Pandas][pandas]   | [Polars][polars]     | better ergonomics and performance                       |            |
| [Seaborn][seaborn] | [Plotly][plotly]     | I like it so much that I joined the company :-)         |            |
| [Jupyter][jupyter] | [Marimo][marimo]     | also risky, but it really does feel like a step forward |            |
| [LaTeX][latex]     | ???                  | maybe [Typst][typst] but see below                      |            |
| —                  | [Metaflow][metaflow] | the most Pythonic option available                      |            |
| —                  | [DVC][dvc]           | preferred to [Git-LFS][git-lfs]                         |            |
| —                  | [Ark][ark]           | the best little Python SSG I've found                   |            |
| —                  | [VSCode][vscode]     | mostly for the debugger                                 |            |
| —                  | [Docker][docker]     | as ubiquitous as Git but <strike>much</strike> less user-hostile |            |

A few notes:

-   Several of these tools are implemented in [Rust][rust] rather than C,
    which makes me hope that Rust is on the same slow-but-steady growth curve as [Python][python].

-   I really like where [Nushell][nushell] is going with structured data,
    and being built in [Rust][rust] is a plus,
    but my first few experiments with it did leave me feeling that it still has a lot of rough edges.

-   [Typst][typst] seems to be a plausible post-TeX typesetting tool,
    but (a) I wish they had used an existing scripting language
    (e.g., one of the [Rust][rust]-based implementations of [Lua][lua])
    instead of creating a new one,
    and (b) it looks like their GUI is web-only and closed source,
    both of which make me very nervous.

-   [VSCode][vscode] and the various [JetBrains][jetbrains] IDEs are far too heavy for my liking,
    but there doesn't seem to be anything else out there
    that supports multiple languages well.
    (Yes, I'm very familiar with [Emacs][emacs];
    no, I don't think it's the right answer.)

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
[emacs]: https://www.gnu.org/software/emacs/
[fish]: https://fishshell.com
[git]: https://git-scm.com
[git-lfs]: https://git-lfs.com
[gitless]: https://gitless.com
[htmx]: https://htmx.org
[jetbrains]: https://www.jetbrains.com/
[js]: https://en.wikipedia.org/wiki/JavaScript
[jupyter]: https://jupyter.org
[just]: https://just.systems/
[latex]: https://www.latex-project.org
[lua]: https://www.lua.org/
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
[rust]: https://www.rust-lang.org/
[seaborn]: https://seaborn.pydata.org
[sqlite]: https://sqlite.org
[typst]: https://typst.app
[vscode]: https://code.visualstudio.com
[wasm]: https://en.wikipedia.org/wiki/WebAssembly
[why-i-draw]: @root/2024/03/01/why-i-draw/
