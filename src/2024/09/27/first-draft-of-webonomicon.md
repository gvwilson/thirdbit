---
title: "First Draft of the Webonomicon"
date: 2024-09-27
---

A few months ago I mused about what might go into a lesson on [human-scale software][human].
[Juanan Pereira][pereira] and I have now sketched a rough outline,
tentatively titled [The Webonomicon][webonomicon].
The sections below shows the learner persona,
the technologies we discuss,
and the order of topics,
while [the repository][repo] has working code.
There's a lot left to do,
but we'd be grateful for feedback:
issues in [the repo][repo] are the best way to reach us.

## Learner Persona

-   Sabina, 28, has a master's degree in animal physiology
    and now works for a mid-sized veterinary pharmaceutical company.
-   She learned a bit of R in an undergraduate biostatistics course,
    then picked up Python in grad school.
    She spends several hours a week analyzing data with [Pandas][pandas]
    and visualizing it with [Plotly Express][plotly-express],
    and is comfortable with basic Git commands.
-   Sabina recently became responsible for maintaining a dashboard application built with [Dash][dash].
    She believes a better understanding of how web applications work in general
    will help her debug and extend it.
-   Sabina has tried doing asynchronous online courses a couple of times,
    but strongly prefers learning in real time with other people.

## Technologies

| Package                          | Purpose           |
| -------------------------------- | ----------------- |
| [Alpine.js][alpine]              | dynamic HTML      |
| [Beautiful Soup][bs4]            | HTML manipulation |
| [deno][deno]                     | JavaScript        |
| [FastHTML][fasthtml]             | web framework     |
| [Flask][flask]                   | web server        |
| [Frappe Charts][frappe-charts]   | charts            |
| [html5validator][html5validator] | validation        |
| [htmx][htmx]                     | interaction       |
| [httpx][httpx]                   | HTTP              |
| [Jinja2][jinja]                  | HTML templating   |
| [JWT][jwt]                       | authentication    |
| [Polars][polars]                 | tabular data      |
| [PrettyTable][prettytable]       | formatting        |
| [PyPika][pypika]                 | query builder     |
| [pytest][pytest]                 | testing           |
| [Selenium][selenium]             | testing           |
| [snailz][snailz]                 | synthetic data    |
| [SQLite][sqlite]                 | database          |
| [SVG.js][svgjs]                  | graphics          |

## Topics

1.  Introduction: what we will learn, how to set up, and the data we will use
1.  HTTP: how browsers and server talk to each other
1.  A Server: building a server with [Flask][flask]
1.  Using a Database: getting data from [SQLite][sqlite] using [PyPika][pypika]
1.  Testing the Server: testing the server with [pytest][pytest]
1.  Serving HTML: generating HTML with [Jinja][jinja] templates
1.  Using Forms: sending data to a server
1.  An Hour of JavaScript: variables, loops, functions, and callbacks
1.  JavaScript in the Browser: using the language in its native habitat
1.  Using HTMX: letting the [htmx][htmx] library do the hard work
1.  Database Migration: managing database schema changes
1.  Permissions: representing and checking who can do what
1.  Authentication: checking the user's identity
1.  Encryption: keeping secrets safe
1.  Testing in the Browser: using [Selenium][selenium] to test the user interface
1.  Dynamic Graphics: drawing pictures with [SVG.js][svgjs]
1.  A Graphical User Interface: handling interactivity in the browser
1.  Accessibility: because everyone should be comfortable
1.  Internationalization: because everyone should be welcome
1.  Logging and Auditing: keeping of track of what's happened
1.  Session: persistent sessions and [JWT][jwt]
1.  FastHTML: bringing it all together
1.  Designing a Workflow: thinking before coding

[alpine]: https://alpinejs.dev/
[bs4]: https://beautiful-soup-4.readthedocs.io/
[deno]: https://deno.com/
[fasthtml]: https://docs.fastht.ml/
[flask]: https://flask.palletsprojects.com/
[frappe-charts]: https://frappe.io/charts/docs
[html5validator]: https://pypi.org/project/html5validator/
[htmx]: https://htmx.org/
[httpx]: https://www.python-httpx.org/
[human]: @root/2024/06/14/human-scale-software/
[jinja]: https://jinja.palletsprojects.com/
[jwt]: https://en.wikipedia.org/wiki/JSON_Web_Token
[pereira]: https://ikasten.io/
[polars]: https://pola.rs/
[prettytable]: https://pypi.org/project/prettytable/
[pypika]: https://pypika.readthedocs.io/
[pytest]: https://docs.pytest.org/
[repo]: https://github.com/gvwilson/webonomicon
[selenium]: https://pypi.org/project/selenium/
[snailz]: https://github.com/gvwilson/snailz
[sqlite]: https://www.sqlite.org/
[svgjs]: https://svgjs.dev/
[webonomicon]: https://third-bit.com/web/
