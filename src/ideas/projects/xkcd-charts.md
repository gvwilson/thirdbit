# Project Proposal: Multilingual XKCD-Style Charting Library

## Background Information

The sponsor maintains an existing Python and JavaScript charting library (`chart-xkcd`) that generates charts in XKCD's hand-drawn style. The goal of this project is to generalize that work to create a multilingual package with clean, idiomatic APIs in Python, JavaScript, Gleam, and Rust, underpinned by a principled and systematic approach to bindings generation.

## Mentor

Greg Wilson is an independent educator and software engineering author who has spent decades teaching software development skills and designing learning materials for developers at all stages of their careers. 

## Project Description

This project asks the team to extend the existing `chart-xkcd` library so that developers working in Python, JavaScript, Gleam, or Rust can create XKCD-style hand-drawn charts using idiomatic APIs in their language of choice, without writing foreign function interface glue code by hand.

The project has two principal components that interact closely throughout the development process. The first component is a bindings generator that reads a language-neutral description of the chart API and emits the per-language wrapper code, type definitions, and documentation stubs. The existing `starch` package in Gleam demonstrates the kind of output this generator should produce for one target language. The team must design the schema language for describing the API, implement the generator, and validate its output against all four target languages.

The second component is the charting feature set: the chart types, configuration options, and rendering logic that the generated bindings expose. This component will extend the current `chart-xkcd` feature set with new chart types or options not yet implemented, but the central constraint is that every feature must be expressible cleanly in all four target languages, each of which has distinct type systems, module conventions, and idioms.

The rendering core will remain JavaScript, relying on the existing D3-based chart classes. Each language binding ultimately calls into the same rendering engine, and the team must design and justify the bridging strategy for each language. For example, Gleam can be compiled directly into JavaScript; this presents a different set of constraints than Rust, which typically requires either a WebAssembly build of the rendering core or a JavaScript runtime that provides a minimal DOM environment. A successful outcome is a single repository in which a developer can declare a bar chart with labeled datasets in any of the four supported languages and receive back a correctly rendered XKCD-style chart.

## Project Scope

The team's first major deliverable is a language-neutral API schema that serves as the single source of truth for generating bindings across all four target languages. Designing this schema requires a classic "build vs. buy" decision: the team must evaluate whether an existing interface description language such as OpenAPI or Protocol Buffers is appropriate, or whether the project's needs are sufficiently specific to justify a domain-specific language (DSL). The decision and its rationale must be documented in the technical design document.

The bindings generator must read the schema and emit idiomatic code for Python (packaged via PyPI), JavaScript (packaged via npm), Gleam (published via the Gleam package repository), and Rust (published via crates.io). "Idiomatic" means that each binding should feel natural to a developer already familiar with that language, and the generator must have unit tests that confirm the generator's textual output matches expected fixtures for each supported language.

At minimum, all four bindings must support bar, line, pie, scatter, and heatmap chart types. The team will write integration tests for each binding in its own language toolchain to confirm that a representative chart declaration in each language produces valid output. Visual regression tests must be defined with a documented tolerance strategy and stored reference images, in order to handle floating-point rendering differences across platforms and browser versions.

Documentation is a first-class deliverable. Each binding must have a user guide explaining installation from its respective package manager and at least one complete worked example. A technical design document must describe the overall architecture, the schema language and generator design, and the bridging strategy used for each target language.

Stretch goals include additional chart types (radar and stacked bar) and a web-based interactive demonstration page that renders a user-supplied chart description in all four languages side by side.

## Project Challenges

The bindings generator design is the project's most open-ended challenge. The schema must be expressive enough to capture optional parameters, nested configuration records, and enumerated types without becoming so complex that it is effectively a fifth programming language. Striking this balance requires the team to study existing approaches in other multilingual projects and to make defensible design decisions early in the project.

Multilingual testing presents another challenge: each binding must be tested in its own language's toolchain, which means the continuous integration pipeline must install and run four different build systems. Designing a CI configuration that is correct, maintainable, and reasonably fast across Python, JavaScript, Gleam, and Rust is a non-trivial systems engineering task in its own right.

Graphical output testing is inherently fragile. Pixel-level comparison of rendered charts can fail due to floating-point differences in layout calculations across platforms or browser versions. The team must choose and justify a tolerance strategy based on perceptual image similarity, structural SVG comparison, or some other mechanism, and document it clearly so that future contributors can understand the approach.

The Rust rendering bridge is probably the single greatest technical challenge. The rendering core of the existing library is D3-based JavaScript, and Rust cannot call that code directly without an intermediary. The team must either adapt the chart classes to run in a non-browser context using a headless JavaScript runtime, or produce a WebAssembly build of the rendering core that Rust can invoke. Both approaches involve significant unknowns that the team should prototype early to reduce risk.

On the non-technical side, four target languages mean four communities of potential users with different conventions, documentation expectations, and idioms. The team should prioritize correctness and consistency over completeness, ensuring that what is released is genuinely useful to developers in each community rather than superficially covering all four targets.

## Number of Students

3-4 students preferred.

## Sponsor-Provided Hardware and Software

No special hardware or software is required. All tools needed to complete this project are freely available, including open-source language runtimes, package managers, and development environments. The sponsor will act as project manager, participate in weekly standups, and review generated binding code throughout development.

## Project Search Keywords

- data visualization
- multilingual library
- XKCD charts
- foreign function interface
- code generation

## Department of Software Engineering Required Deliverables

Standard departmental deliverables as listed by the RIT Department of Software Engineering.

## Sponsor and Project Specific Deliverables

- Language-neutral API schema serving as the single source of truth for all generated bindings
- Bindings generator tool capable of emitting idiomatic code for all four target languages
- Working bindings for Python, JavaScript, Gleam, and Rust, each installable from its standard package manager
- Source code in a public Git repository under an open-source license (MIT preferred)
- Test suite covering: generator correctness (textual output matches expected fixtures), per-language integration tests (each binding produces valid SVG for each supported chart type), and visual regression tests with a documented tolerance strategy and stored reference images
- Technical design document describing the overall architecture, schema language, generator design, and bridging strategy for each target language
- User guide for each language binding, including installation instructions and at least one complete worked example

## Proprietary Information

No aspect of this project is proprietary. The project will be developed and published openly, and team members are free to discuss all aspects of their work with potential employers or graduate programs.

## Availability

The sponsor is available for weekly 30-minute video calls and is flexible on the day and time, with a preference for morning slots (Eastern Time). The sponsor responds to email within 24 hours on weekdays.

## Project Agreements and Assignment of Rights

The sponsor requires the open-source project agreement: all code will be published publicly under an open-source license. The sponsor confirms that all necessary internal clearances have been obtained to use the RIT standard open-source project agreement unmodified.
