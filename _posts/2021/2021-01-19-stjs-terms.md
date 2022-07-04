---
title: "Software Tools in JavaScript: Terms"
date: 2021-01-19
year: 2021
---

I still have 48 figures to draw for *[Software Design by Example Using JavaScript]({{'/sdxjs/' | relative_url}})*,
but to follow up on [this post about its topics]({{ '/2021/01/11/stjs-alpha/' | relative_url }})
and [this post about using glossaries to summarize lesson content]({{ '/2021/01/17/the-page-is-not-the-lesson/' | relative_url }}),
here's a list of the terms defined in each chapter.
What I want to build (or find) next is a tool that will take data like this,
find related uses ("glob" for "globbing", "method chain" for "method chaining", etc.),
and tell me if I'm using ideas before explaining them.
I don't want to have to list all possible synonyms by hand,
any more than I want to have to list all the functions that a module calls.
Instead,
what I want for lesson maintenance is something that will tell me when I've broken something up
by adding, cutting, or moving material.

<table>
  <tr><td colspan="3"><strong>Systems Programming</strong></td></tr>
  <tr><td>anonymous function</td>	<td>asynchronous</td>	<td>Boolean</td></tr>
  <tr><td>callback</td>	<td>cognitive load</td>	<td>command-line argument</td></tr>
  <tr><td>console</td>	<td>current working directory</td>	<td>destructuring assignment</td></tr>
  <tr><td>edge case</td>	<td>filesystem</td>	<td>filter</td></tr>
  <tr><td>globbing</td>	<td>idiomatic</td>	<td>log message</td></tr>
  <tr><td>path</td>	<td>promise</td>	<td>protocol</td></tr>
  <tr><td>scope</td>	<td>single-threaded</td>	<td>string interpolation</td></tr>

  <tr><td colspan="3"><strong>Asynchronous Programming</strong></td></tr>
  <tr><td>call stack</td>	<td>character encoding</td>	<td>class</td></tr>
  <tr><td>constructor</td>	<td>event loop</td>	<td>exception</td></tr>
  <tr><td>method</td>	<td>method chaining</td>	<td>non-blocking execution</td></tr>
  <tr><td>promisification</td>	<td>UTF-8</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Unit Testing</strong></td></tr>
  <tr><td>actual result</td>	<td>assertion</td>	<td>caching</td></tr>
  <tr><td>defensive programming</td>	<td>design pattern</td>	<td>dynamic loading</td></tr>
  <tr><td>error (test)</td>	<td>exception handler</td>	<td>expected result</td></tr>
  <tr><td>exploratory programming</td>	<td>fail (test)</td>	<td>fixture</td></tr>
  <tr><td>global variable</td>	<td>introspection</td>	<td>lifecycle</td></tr>
  <tr><td>pass (test)</td>	<td>side effect</td>	<td>Singleton pattern</td></tr>
  <tr><td>test runner</td>	<td>throw exception</td>	<td>unit test</td></tr>

  <tr><td colspan="3"><strong>File Backup</strong></td></tr>
  <tr><td>collision</td>	<td>cryptographic hash function</td>	<td>csv</td></tr>
  <tr><td>handler</td>	<td>hash code</td>	<td>hash function</td></tr>
  <tr><td>JSON</td>	<td>mock object</td>	<td>pipe</td></tr>
  <tr><td>race condition</td>	<td>stream</td>	<td>timestamp</td></tr>
  <tr><td>time of check/time of use</td><td>UTC</td>	<td>version control system</td></tr>

  <tr><td colspan="3"><strong>Data Tables</strong></td></tr>
  <tr><td>column major</td>	<td>data frame</td>	<td>garbage collection</td></tr>
  <tr><td>heterogeneous</td>	<td>homogeneous</td>	<td>immutable</td></tr>
  <tr><td>row major</td>	<td>SQL</td>	<td>tagged data</td></tr>
  <tr><td>test harness</td>	<td></td>	<td></td></tr>

  <tr><td colspan="3"><strong>Pattern Matching</strong></td></tr>
  <tr><td>base class</td>	<td>Chain of Responsibility pattern</td>	<td>depth-first search</td></tr>
  <tr><td>derived class</td>	<td>greedy algorithm</td>	<td>query selector</td></tr>
  <tr><td>regular expression</td>	<td>test-driven development</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Parsing Expressions</strong></td></tr>
  <tr><td>literal</td>	<td>precedence</td>	<td>token</td></tr>
  <tr><td>well-formed</td>	<td>YAML</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Page Templates</strong></td></tr>
  <tr><td>bare object</td>	<td>DOM</td>	<td>dynamic scoping</td></tr>
  <tr><td>environment</td>	<td>lexical scoping</td>	<td>stack frame</td></tr>
  <tr><td>Visitor pattern</td>	<td></td>	<td></td></tr>

  <tr><td colspan="3"><strong>Build Manager</strong></td></tr>
  <tr><td>automatic variable</td>	<td>build manager</td>	<td>build recipe</td></tr>
  <tr><td>build rule</td>	<td>build stale</td>	<td>build target</td></tr>
  <tr><td>compiled language</td>	<td>cycle</td>	<td>directed acyclic graph</td></tr>
  <tr><td>dependency</td>	<td>driver</td>	<td>interpreted language</td></tr>
  <tr><td>link</td>	<td>pattern rule</td>	<td>runnable documentation</td></tr>
  <tr><td>Template Method pattern</td>	<td>topological order</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Layout Engine</strong></td></tr>
  <tr><td>attribute</td>	<td>cache</td>	<td>confirmation bias</td></tr>
  <tr><td>coupling</td>	<td>DOM selector</td>	<td>easy mode</td></tr>
  <tr><td>layout engine</td>	<td>function signature</td>	<td></td></tr>

  <tr><td colspan="3"><strong>File Interpolator</strong></td></tr>
  <tr><td>header file</td>	<td>loader</td>	<td>sandbox</td></tr>
  <tr><td>search path</td>	<td>shell variable</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Module Loader</strong></td></tr>
  <tr><td>absolute path</td>	<td>alias</td>	<td>circular dependency</td></tr>
  <tr><td>closure</td>	<td>directed graph</td>	<td>encapsulate</td></tr>
  <tr><td>immediately-invoked function expression</td>	<td>namespace</td>	<td>plugin architecture</td></tr>

  <tr><td colspan="3"><strong>Style Checker</strong></td></tr>
  <tr><td>abstract syntax tree</td>	<td>dynamic lookup</td>	<td>generator function</td></tr>
  <tr><td>iterator pattern</td>	<td>linter</td>	<td>Markdown</td></tr>
  <tr><td>walk (tree)</td>	<td></td>	<td></td></tr>

  <tr><td colspan="3"><strong>Code Generator</strong></td></tr>
  <tr><td>byte code</td>	<td>code coverage</td>	<td>Decorator pattern</td></tr>
  <tr><td>macro</td>	<td>nested function</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Documentation Generator</strong></td></tr>
  <tr><td>accumulator</td>	<td>block comment</td>	<td>doc comment</td></tr>
  <tr><td>line comment</td>	<td>slug</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Module Bundler</strong></td></tr>
  <tr><td>entry point</td>	<td>module bundler</td>	<td>transitive closure</td></tr>

  <tr><td colspan="3"><strong>Package Manager</strong></td></tr>
  <tr><td>backward-compatible</td>	<td>combinatorial explosion</td>	<td>heuristic</td></tr>
  <tr><td>manifest</td>	<td>patch</td>	<td>prune</td></tr>
  <tr><td>SAT solver</td>	<td>semantic versioning</td>	<td></td></tr>

  <tr><td colspan="3"><strong>Virtual Machine</strong></td></tr>
  <tr><td>Application Binary Interface</td>	<td>assembler</td>	<td>assembly code</td></tr>
  <tr><td>bitwise operation</td>	<td>compiler</td>	<td>instruction pointer</td></tr>
  <tr><td>instruction set</td>	<td>label address</td>	<td>op code</td></tr>
  <tr><td>register</td>	<td>virtual machine</td>	<td>word (memory)</td></tr>

  <tr><td colspan="3"><strong>Debugger</strong></td></tr>
  <tr><td>breakpoint</td>	<td>source map</td>	<td></td></tr>
</table>
