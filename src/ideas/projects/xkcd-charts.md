# Project Proposal: Multilingual XKCD-Style Charting Library

## Background Information

-   Sponsor: Greg Wilson, independent educator and software engineering author
-   Domain: data visualization, multilingual library design, foreign function interfaces
-   The sponsor has an existing Python and JavaScript charting library ([`chart-xkcd`][chart-xkcd]) that generates XKCD-style hand-drawn charts (bar, line, pie, scatter, radar, heatmap, stacked bar), as well as preliminary Gleam bindings ([`starch`][starch]) that wrap the JavaScript layer via Gleam's FFI mechanism
-   The goal is to generalize this work into a multilingual package with clean, idiomatic APIs in Python, JavaScript, Gleam, and Rust, underpinned by a systematic bindings-generation approach

## Project Description

-   Extend the existing `chart-xkcd` library so that developers in Python, JavaScript, Gleam, and Rust can create XKCD-style charts using idiomatic APIs without writing FFI glue by hand
-   The project has two principal components that interact closely:
    1.  Bindings generator: a tool and/or set of templates that reads a language-neutral description of the chart API (chart types, their parameters, and option records) and emits the per-language wrapper code, type definitions, and documentation stubs. The existing `starch` package demonstrates the kind of output this generator should produce for Gleam
    2.  Charting feature set: the chart types, options, and rendering logic that the bindings expose. This component may add new chart types or options not yet in `chart-xkcd`, and must ensure the feature set is expressible cleanly in all four target languages
-   The rendering core remains JavaScript (via the existing D3-based chart classes), so each language binding ultimately calls into the same rendering engine. The team must decide how each language reaches that engine: for example, Rust and Python may use WebAssembly, while Gleam calls the JavaScript runtime directly.
-   A successful outcome is a single repository in which a developer can declare a bar chart with labeled datasets in any of the four languages and get back an XKCD-style chart.

## Project Scope

-   A language-neutral API schema as the single source of truth for generating bindings. This is a classic "build vs. buy" decision.
-   Bindings generator for Python, JavaScript, Gleam (a pure functional language), and Rust (a low-level compiled language).
-   At minimum, all four bindings must support bar, line, pie, scatter, and heatmap chart types
-   Unit tests for the bindings generator
-   Integration and visual tests, including cross-language comparison tests
-   Documentation

## Project Challenges

-   Bindings generator design:
    -   A schema that is expressive enough to capture all options without becoming a second programming language
-   Multilingual testing:
    -   Each binding must be tested in its own language toolchain, which is an interesting CI challenge
-   Graphical output testing
    -   Pixel-level comparison is brittle because of floating-point differences across platforms
-   Rust rendering bridge:
    -   The team must either adapt the chart classes to run in a non-browser context or choose a JS runtime that provides a minimal DOM stub
-   Non-technical:
    -   Four target languages mean four communities of potential users with different conventions

## Number of Students

-   3-4 students preferred

## Sponsor-Provided Hardware and Software

-   None: all required tools are freely available
-   Sponsor will act as project manager, run standups, and review generated binding code

## Project Search Keywords

-   "data visualization"
-   "multilingual library"
-   "XKCD charts"

## Department of Software Engineering Required Deliverables

-   Standard departmental deliverables as listed by RIT SE

## Sponsor and Project Specific Deliverables

-   Language-neutral API schema
-   Bindings generator tool
-   Working bindings for all four languages installable from standard package managers
-   Source code in a public Git repository under an open-source license (MIT preferred)
-   Test suite covering:
    -   Generator correctness (textual output matches expected)
    -   Per-language integration tests (each binding produces valid SVG for each supported chart type)
    -   Visual regression tests with documented tolerance strategy and stored reference images
-   Technical design document
-   User guide

## Proprietary Information

-   No aspect of this project is proprietary

## Availability

-   Sponsor available for weekly 30-minute video calls; flexible on day and time; prefers morning slots (ET)
-   Responsive by email within 24 hours on weekdays

## Project Agreements and Assignment of Rights

-   Open-source agreement required: code is published publicly
-   Sponsor confirms all necessary clearances to use RIT standard open-source project agreement unmodified

[chart-xkcd]: https://github.com/gvwilson/chart.xkcd
[starch]: https://github.com/gvwilson/starch.gleam
