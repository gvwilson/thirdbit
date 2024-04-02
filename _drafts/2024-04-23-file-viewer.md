---
title: "Software Design by Example in Python 23: A File Viewer"
date: 2024-04-23
year: 2024
---

I was running out of steam by the time I reached the end of
[the JavaScript version of *Software Design by Example*][sdxjs],
so I didn't include a few topics that I originally planned to.
"How to write a text editor" was one of them:
I have a lot more experience with back-end coding and traditional Unix command-line filters
than I do with user interfaces,
so the learning I'd have to do myself was daunting.

Then I stumbled over [this tutorial][lorgat_tutorial] by [Wasim Lorgat][lorgat]
and everything suddenly became a whole lot easier.
Lorgat starts with nothing more than `import curses`
and builds up a Nano-style editor one step at a time,
carefully explaining each trap someone might stumble into along the way.
[Chapter 23: A File Viewer][sdxpy_viewer] recapitulates the first half of his lesson,
adding some commentary on models versus views
and tracing the order of operations during startup in more detail
in order to set up the next chapter on implementing undo and redo.

<img class="centered" src="{{'/sdxpy/viewer/concept_map.svg' | relative_url}}" alt="Concept map for a file viewer"/>

> Terms defined: buffer (of text), delayed construction, enumeration, factory method, log file, synthetic data, viewport.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[lorgat]: https://wasimlorgat.com/
[lorgat_tutorial]: https://wasimlorgat.com/posts/editor.html
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxpy_viewer]: {{'/sdxpy/viewer/' | relative_url}}
