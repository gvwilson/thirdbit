---
title: "Benchmarking Languages"
date: 2023-01-30
year: 2023
---

Back in the 1980s, R.W. Hockney introduced two measures for quantifying the performance of pipelined machines.
The first, *r<sub>∞</sub>*, is the pipeline's maximum possible performance on an infinitely large data set.
The second, *n<sub>½</sub>*, is how much data you need in order to reach half that theoretical peak,
i.e.,
how big your problem has to be to offset startup overheads.
In the mid-90s,
I suggested that another performance measure would be equally interesting:
how long it takes to write code that achieves half a machine's rated performance.
I called it *p<sub>½</sub>*,
and observed that for many supercomputers it was effectively infinity,
since no real application ever achieves more than 10-20% of the performance that manufacturers claim.

I no longer believe that measuring time-to-solution is the right approach,
but I still think that we can learn a lot from comparing implementations of common problems in different languages.
The [Cowichan Problems][cowichan] that I proposed for measuring *p<sub>½</sub>* aren't right
for comparing the general-purpose languages vying to be the next Python,
but I think we'd all learn a lot
if people implemented a few of the examples from [*Software Design by Example*][sdxjs]
in Rust, Zig, Nim, Elixir, F#, Scala, and what-not.
My choices would be:

-   a text editor that supported undo and redo (something on the scale of [nano][nano] or [ted][ted])
-   a [file backup tool][sdxjs_backup] (basically, a baby version of Git)
-   a [build manager][sdxjs_build]
-   a [style checker][sdxjs_style]
-   a [web server][aosa_server]

I've chosen these five because between them they touch on
most of the core design ideas I use when I'm programming,
such as actions as objects (the editor),
hashing (the file backup tool),
graph manipulation (the build manager),
recursion and introspection (the style checker),
and asynchronous I/O (the web server).
Putting it another way,
I think these problems are different enough from each other
that each one's implementation would highlight something about the language
that would otherwise not be seen.

[aosa_server]: https://aosabook.org/en/500L/a-simple-web-server.html
[cowichan]: {{'/2010/06/12/the-cowichan-problems/' | relative_url}}
[nano]: https://www.nano-editor.org/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_backup]: {{'/sdxjs/file-backup/' | relative_url}}
[sdxjs_build]: {{'/sdxjs/build-manager/' | relative_url}}
[sdxjs_style]: {{'/sdxjs/style-checker/' | relative_url}}
[sdxjs_test]: {{'/sdxjs/unit-test/' | relative_url}}
[ted]: https://github.com/cesquivias/ted
