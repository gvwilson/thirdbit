---
title: "Software Design by Example 3: Asynchronous Programming"
date: 2023-01-03
year: 2023
---

As I said in [the previous post][systems_programming_post],
JavaScript's mix of callbacks, promises, and `async`/`await` causes a lot of confusion.
Since asynchronous operation shapes the design of pretty much everything written in the language,
readers need more than a copy-paste-and-swear understanding of how these mechanisms work.
[This chapter][sdxjs_async_programming] therefore builds a partial replacement for promises step by step.
The explanation was inspired by Trey Huffine's [tutorial][huffine_promises],
which I encourage everyone to read if they want to know more.

In order to explain promises, though, the chapter first has to explain JavaScript's event loop.
To do *that*,
I had to step back and decide what *notional machine* I wanted to base my explanations on.
If I understand the term correctly,
a notional machine is a mental model of how a computer executes a program.
There isn't one "right" notional machine for any language:
the metaphors and level of detail depends on how much the learner is ready to know and needs to know.
(The difference between the former and the latter, by the way, is why lessons exist…)
I draft [a notional machine for Python][python_notional_machine] and [a notional machine for R][r_notional_machine]
as I was writing the first few examples for this book.
I never wrote one out for JavaScript,
but I think it would be a great [summative_assessment].

> Terms defined: call stack, character encoding, class, constructor, event loop, exception, fluent interface, method, method chaining, non-blocking execution, promise, promisification, protocol, UTF-8.

<figure id="async-programming-resolve" align="center">
  <img src="{{'/sdxjs/async-programming/resolve.svg' | relative_url}}" alt="How promises resolve"/>
  <figcaption>Figure 3.3: Order of operations when a promise resolves.</figcaption>
</figure>

[huffine_promises]: https://levelup.gitconnected.com/understand-javascript-promises-by-building-a-promise-from-scratch-84c0fd855720
[python_notional_machine]: https://third-bit.com/2018/04/12/notional-machine-for-python/
[r_notional_machine]: https://third-bit.com/2019/07/15/notional-machine-for-r/
[sdxjs_async_programming]: {{'/sdxjs/async-programming/' | relative_url}}
[summative_assessment]: https://teachtogether.tech/en/index.html#s:models-formative-assessment
[systems_programming_post]: {{'/2023/01/02/sdxjs-systems-programming/' | relative_url}}
