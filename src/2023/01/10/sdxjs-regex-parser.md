---
title: "Software Design by Example 8: Parsing Expressions"
date: 2023-01-10
---

While [Chapter 7][sdxjs_regex] explained how to build a simple regular expression matcher,
[Chapter 8][sdxjs_parsing] explains how to parse regular expression patterns,
and in doing so gives readers an idea of how more complicated parsers work.
The grammar that the final parser handles is pretty simple:

| Meaning | Character |
| ------- | --------- |
| Any literal character *c* | *c* |
| Beginning of input | `^` |
| End of input | `$` |
| Zero or more of the previous thing | `*` |
| Either/or | `|` |
| Grouping | `(…)` |

Even this grammar is enough to show why parsing is hard—hard enough that
people should use existing data formats rather than create new ones
and should generate data that can be parsed with off-the-shelf tools.
But from a design point of view,
it's a chance to introduce the idea of *actions as objects*.
Earlier chapters showed that functions are just another kind of data;
taking that up a level,
everything from "match these characters" in a parser to "move the cursor up a line" in an editor
or "compile this file" in a build tool
can and should be turned into an object
that can be put in a list,
concatenated with other actions,
and so on.

This idea is one of the reasons I hope someone who knows more about functional programming than I do
will some day add a third volume to this series
that shows how to implement these tools in a language like Haskell or [a superset of Elm][to_dont].
Those languages embody the same general design ideas in very different ways,
and I think I'd learn a lot from seeing how someone who thinks in those ways
translates these ideas into working code.

<figure id="regex-parser-mechanics" class="center">
  <img src="@root/sdxjs/regex-parser/mechanics.svg" alt="Mechanics of combining tokens" class="centered">
  <figcaption>Figure 8.2: Mechanics of combining tokens while parsing regular expressions.</figcaption>
</figure>

> Terms defined: finite state machine, literal, parser, precedence, token, Turing Machine, well formed, YAML.

[sdxjs_parsing]: https://third-bit.com/sdxjs/regex-parser/
[sdxjs_regex]: https://third-bit.com/sdxjs/pattern-matching/
[to_dont]: https://third-bit.com/2022/12/28/six-for-the-to-dont-list/
