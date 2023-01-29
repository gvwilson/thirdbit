---
title: "Software Design by Example"
date: 2022-10-24
year: 2022
---

The (hopefully) final version of
[*Software Design by Example: A Tool-Based Introduction with JavaScript*][sdxjs-online]
has gone to [the publisher][sdxjs-book],
and physical copies should be available by the end of the year.

Lots of things didn't get into the book,
partly because I ran out of steam but also because I wanted to see if the book had any impact before investing more effort.
The most important was a text editor about the size of kilo
([1](http://antirez.com/news/108), [2](https://viewsourcecode.org/snaptoken/kilo/))
with undo/redo (which is complex enough to need a whole chapter).
The second would be a message queue or pub/sub system like [RabbitMQ](https://www.rabbitmq.com/)
because partial failure in distributed systems is now a fact of most programmers' lives, but is rarely taught.
I would also have liked to include a [fuzz tester](https://www.fuzzingbook.org/),
the world's smallest useful [database](https://cstack.github.io/db_tutorial/),
something to show readers how model checking works,
and other tools.

But what I'd like most is to *edit* these chapters rather than write them.
It's not less work (trust me),
but I'd really like to help other people get a chance to raise their profiles.
So if you're a junior developer and would like to see your name in a book,
or an undergrad student who needs a senior project that combines research, design, coding, and writing,
please reach out,
especially if you're from an underrepresented or marginalized group.

We make beautiful things,
and we ought to share them.

---

I've also now started on a Python version;
the topics and some key ideas are listed below,
and I'd be [grateful for feedback](mailto:{{site.author.email}}) on what else you'd like to see included.

<table>
  <tr>
    <th>Tool</th>
    <th>Key Ideas</th>
  </tr>
  <tr>
    <td>unit testing framework</td>
    <td>code as data; introspection</td>
  </tr>
  <tr>
    <td>file backup</td>
    <td>hashing; interface vs. implementation</td>
  </tr>
  <tr>
    <td>an interpreter</td>
    <td>code as data; the read-eval-print cycle</td>
  </tr>
  <tr>
    <td>dataframes</td>
    <td>interface vs. implementation; performance optimization</td>
  </tr>
  <tr>
    <td>pipelines</td>
    <td>inheritance vs. composition; traceability; task execution</td>
  </tr>
  <tr>
    <td>a build manager</td>
    <td>dependencies as graphs; task execution</td>
  </tr>
  <tr>
    <td>pattern matching</td>
    <td>recursive search; composability</td>
  </tr>
  <tr>
    <td>a regular expression parser</td>
    <td>lazy vs. greedy execution; composability</td>
  </tr>
  <tr>
    <td>a web server</td>
    <td>event-driven computation; error handling; security</td>
  </tr>
  <tr>
    <td>a large file cache</td>
    <td>hashing; interface vs. implementation</td>
  </tr>
  <tr>
    <td>a log-structured database</td>
    <td>systems programming; performance optimization</td>
  </tr>
  <tr>
    <td>a persistence framework</td>
    <td>introspection; interface vs. implementation</td>
  </tr>
  <tr>
    <td>binary data storage</td>
    <td>interpreter internals</td>
  </tr>
  <tr>
    <td>a page templating tool</td>
    <td>code as data; introspection</td>
  </tr>
  <tr>
    <td>a package manager</td>
    <td>recursive search; performance optimization</td>
  </tr>
  <tr>
    <td>a page layout tool</td>
    <td>recursive search; interface vs. implementation</td>
  </tr>
  <tr>
    <td>a code quality checker</td>
    <td>recursive search; introspection; extensibility</td>
  </tr>
  <tr>
    <td>a code generator</td>
    <td>code as data</td>
  </tr>
  <tr>
    <td>a virtual machine</td>
    <td>interpreter internals</td>
  </tr>
  <tr>
    <td>an interactive debugger</td>
    <td>interpreter internals</td>
  </tr>
</table>

[sdxjs-book]: https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-JavaScript/Wilson/p/book/9781032330235
[sdxjs-online]: https://third-bit.com/sdxjs/
