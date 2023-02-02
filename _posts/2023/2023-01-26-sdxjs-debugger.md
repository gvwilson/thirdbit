---
title: "Software Design by Example 20: Debugger"
date: 2023-01-26
year: 2023
---

The [penultimate chapter][sdxjs_debugger] of [*Software Design by Example*][sdxjs]
explores one of the question that sparked this book:
how does an interactive breakpointing debugger work?
The first time I saw one in action I was completely baffled.
How could the computer stop where I wanted and then keep going?
How could it interact with me?
Finding out was a lot harder than it should have been:
there were (and are) lots of books and courses on compilers and operating systems,
but nothing that explained the workings of this magical, powerful tool.

This chapter answers my long-ago questions by building a simple single-stepping debugger
It also shows how to create unit tests for interactive applications.
That's a lot to pack into just two thousand words,
but most of the ideas have come up before.

I'm pleased that I was able to answer my younger self's questions.
However,
I'm still annoyed by the way debuggers are mostly left out of the curriculum.
Of the forty-odd students I interviewed for software engineering intern positions last year,
fewer than a dozen knew how to set a breakpoint in an IDE.
Andreas Zeller's [*The Debugging Book*][debugging_book] has [a very informative chapter][debugging_chapter],
and I recommend the whole book to every working programmer,
but I'll believe our profession is serious about building code that works
when every undergraduate computer science program has a full-semester course
on how to use tools to find and fix bugs.

<figure id="debugger-test-interact" class="center">
  <img src="{{'/sdxjs/debugger/test-interact.svg' | relative_url}}" alt="Testing interactive application" class="centered">
  <figcaption>Figure 20.2: Replacing input and output to test interactive applications.</figcaption>
</figure>

> Terms defined: breakpoint, source map, tab completion, watchpoint.

[debugging_book]: https://www.debuggingbook.org/
[debugging_chapter]: https://www.debuggingbook.org/html/Debugger.html
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_debugger]: {{'/sdxjs/debugger/' | relative_url}}
[sdxjs_vm]: {{'/sdxjs/virtual-machine/' | relative_url}}
