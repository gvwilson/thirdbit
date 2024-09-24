---
title: "Software Design by Example Summary"
date: 2023-01-29
---

I wrote 22 posts this month to summarize the chapters in [*Software Design by Example*][sdxjs]
and to ask [who'd be interested in taking an online class based on its Python successor][class].
The list below links to each post in the series,
and to the terms defined in each of the book's content chapters.

My next goal is to prepare an hour-long talk summarizing what I learned from writing this book.
It will cover some of the same material as ["Software Design for Data Scientists"][sd4ds] and [this paper][paper],
but will focus more on how to teach design and what junior programmers are ready to learn.
If you or your team would like to listen to me ramble,
I'd be very happy to deliver it online in exchange for a small donation to a mutually-agreed charity—please [reach out](mailto:gvwilson@third-bit.com)
if you're interested.

1.  [Introduction](@root/2023/01/01/sdxjs-introduction/)

1.  [Systems Programming](@root/2023/01/02/sdxjs-systems-programming/): anonymous function, asynchronous, Boolean, callback function, cognitive load, command-line argument, console, current working directory, destructuring assignment, edge case, filename extension, filesystem, filter, globbing, idiomatic, log message, path (in filesystem), protocol, scope, single-threaded, string interpolation.

1.  [Asynchronous Programming](@root/2023/01/03/sdxjs-async-programming/): call stack, character encoding, class, constructor, event loop, exception, fluent interface, method, method chaining, non-blocking execution, promise, promisification, protocol, UTF-8.

1.  [Unit Testing](@root/2023/01/04/sdxjs-unit-test/): absolute error, actual result (of test), assertion, caching, defensive programming, design pattern, dynamic loading, error (in a test), exception handler, expected result (of test), exploratory programming, fail (a test), fixture, global variable, introspection, lifecycle, pass (a test), relative error, side effect, Singleton pattern, test runner, test subject, throw (exception), unit test.

1.  [File Backup](@root/2023/01/05/sdxjs-file-backup/): Application Programming Interface, collision, comma-separated values, Coordinated Universal Time, cryptographic hash function, data migration, handler, hash code, hash function, JavaScript Object Notation, mock object, pipe, race condition, SHA-1 hash, stream, streaming API, Time of check/time of use, timestamp, version control system.

1.  [Data Tables](@root/2023/01/06/sdxjs-data-table/): character encoding, column-major storage, data frame, fixed-width (of strings), fixed-width (of strings), garbage collection, heterogeneous, homogeneous, immutable, index (in a database), JavaScript Object Notation, join, pad (a string), row-major storage, sparse matrix, SQL, tagged data, test harness.

1.  [Pattern Matching](@root/2023/01/09/sdxjs-pattern-matching/): base class, Chain of Responsibility pattern, child (in a tree), coupling, depth-first, derived class, Document Object Model, eager matching, eager matching, greedy algorithm, lazy matching, node, Open-Closed Principle, polymorphism, query selector, regular expression, scope creep, test-driven development.

1.  [Parsing Expressions](@root/2023/01/10/sdxjs-regex-parser/): finite state machine, literal, parser, precedence, token, Turing Machine, well formed, YAML.

1.  [Page Templates](@root/2023/01/11/sdxjs-page-templates/): bare object, dynamic scoping, environment, lexical scoping, stack frame, static site generator, Visitor pattern.

1.  [Build Manager](@root/2023/01/12/sdxjs-build-manager/): automatic variable, build manager, build recipe, build rule, build target, compiled language, cycle (in a graph), dependency, directed acyclic graph, driver, interpreted language, link (a program), pattern rule, runnable documentation, stale (in build), Template Method pattern, topological order.

1.  [Layout Engine](@root/2023/01/13/sdxjs-layout-engine/): attribute, cache, confirmation bias, design by contract, easy mode, layout engine, Liskov Substitution Principle, query selector, signature, z-buffering.

1.  [File Interpolator](@root/2023/01/16/sdxjs-file-interpolator/): header file, literate programming, loader, sandbox, search path, shell variable.

1.  [Module Loader](@root/2023/01/17/sdxjs-module-loader/): absolute path, alias, circular dependency, closure, directed graph, encapsulate, immediately-invoked function expression (IIFE), inner function, Least Recently Used cache, namespace, plugin architecture.

1.  [Style Checker](@root/2023/01/18/sdxjs-style-checker/): abstract syntax tree, Adapter pattern, column-major storage, dynamic lookup, generator function, intrinsic complexity, Iterator pattern, linter, Markdown, row-major storage, walk (a tree).

1.  [Code Generator](@root/2023/01/19/sdxjs-code-generator/): byte code, code coverage (in testing), compiler, Decorator pattern, macro, nested function, two hard problems in computer science.

1.  [Documentation Generator](@root/2023/01/20/sdxjs-doc-generator/): accumulator, block comment, deprecation, doc comment, line comment, slug.

1.  [Module Bundler](@root/2023/01/23/sdxjs-module-bundler/): entry point, module bundler, transitive closure.

1.  [Package Manager](@root/2023/01/24/sdxjs-package-manager/): backward-compatible, combinatorial explosion, heuristic, manifest, patch, prune, SAT solver, scoring function, seed, semantic versioning.

1.  [Virtual Machine](@root/2023/01/25/sdxjs-virtual-machine/): Application Binary Interface, assembler, assembly code, bitwise operation, disassembler, instruction pointer, instruction set, label (address in memory), op code, register, virtual machine, word (of memory).

1.  [Debugger](@root/2023/01/26/sdxjs-debugger/): breakpoint, source map, tab completion, watchpoint.

1.  [Conclusion](@root/2023/01/27/sdxjs-conclusion/)

1.  [Would You Take This Class?][class]

[class]: @root/2023/01/29/would-you-take-this-class/
[paper]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009809
[sd4ds]: @root/talks/sd4ds/#1
[sdxjs]: @root/sdxjs/
