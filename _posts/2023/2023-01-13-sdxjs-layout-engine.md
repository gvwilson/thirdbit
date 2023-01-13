---
title: "Software Design by Example 11: Layout Engine"
date: 2023-01-13
year: 2023
---

You might be reading this as an HTML page,
an e-book (which is basically the same thing),
or on the printed page.
In each case,
a layout engine took some text and some layout instructions
and decided where to put each character and image.
[This chapter][sdxjs_layout] of [*Software Design by Example*][sdxjs]
builds a small layout engine to show how they work,
and also to show how inheritance and recursion can take advantage of each other.

I wrote this chapter before encountering Panchekha and Harrelson's [*Web Browser Engineering*][browser],
which I strongly recommend:
it does a great job of showing how one of the most important kinds of software ever created does what it does,
and I've learned a lot from [its chapter on page layout][browser_layout]
that I hope will make the Python version of this chapter clearer.

<figure id="layout-engine-layout" align="center">
  <img src="{{'/sdxjs/layout-engine/layout.svg' | relative_url}}" alt="Laying out rows and columns"/>
  <figcaption>Figure 11.3: Laying out rows and columns of fixed-size blocks.</figcaption>
</figure>

> Terms defined: attribute, cache, confirmation bias, design by contract, easy mode, layout engine, Liskov Substitution Principle, query selector, signature, z-buffering.

[browser]: https://browser.engineering/
[browser_layout]: https://browser.engineering/layout.html
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_layout]: {{'/sdxjs/layout-engine/' | relative_url}}
