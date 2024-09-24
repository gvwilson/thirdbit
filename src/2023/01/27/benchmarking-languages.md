---
title: "Benchmarking Languages"
date: 2023-01-27
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
for comparing the general-purpose languages vying to be the next [Python][python],
but I think we'd all learn a lot
if people implemented a few of the examples from [*Software Design by Example*][sdxjs]
in [Rust][rust], [Zig][zig], [Nim][nim], [Haskell][haskell], [Elixir][elixir], [F#][fsharp], [Scala][scala], and what-not.
My choices would be:

-   a text editor that supported undo and redo (something on the scale of [nano][nano] or [ted][ted])
-   a [file backup tool][sdxjs_backup] (basically, a baby version of Git)
-   a [build manager][sdxjs_build]
-   a [style checker][sdxjs_style]
-   a [web server][aosa_server]

Between them,
these five examples touch on
most of the core design ideas I used when programming,
such as actions as objects (the editor),
hashing (the file backup tool),
dependency  management (the build manager),
introspection (the style checker),
and asynchronous I/O (the web server).
They are also a nearly-complete minimal development stack—only "nearly" because
I felt the ideas in a unit testing framework overlapped enough with those in a style checker
that the set only needed one or the other.

I think these problems are different enough from each other
that each one's implementation would highlight something about the language
that would otherwise not be seen.
If you're teaching a software design class with an interesting new language
and want to give these to your students as assignments,
please let me know how it goes.

[aosa_server]: https://aosabook.org/en/500L/a-simple-web-server.html
[cowichan]: @root/2010/06/12/the-cowichan-problems/
[elixir]: https://elixir-lang.org/
[fsharp]: https://fsharp.org/
[haskell]: https://www.haskell.org/
[nano]: https://www.nano-editor.org/
[nim]: https://nim-lang.org/
[python]: https://www.python.org/
[rust]: https://www.rust-lang.org/
[scala]: https://scala-lang.org/
[sdxjs]: @root/sdxjs/
[sdxjs_backup]: @root/sdxjs/file-backup/
[sdxjs_build]: @root/sdxjs/build-manager/
[sdxjs_style]: @root/sdxjs/style-checker/
[sdxjs_test]: @root/sdxjs/unit-test/
[ted]: https://github.com/cesquivias/ted
[zig]: https://ziglang.org/
