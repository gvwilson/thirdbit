---
title: "Software Design by Example in Python 5: Parsing Text"
date: 2024-04-05
---

[Chapter 5: Parsing Text][sdxpy_parse] shows how to write a parser
by building one for the filename globbing expressions introduced in [the previous chapter][sdxpy_glob].
It makes the usual distinction between tokenizing and constructing an abstract syntax tree;
the latter concept comes up several times later,
so I arranged material to get it out of the way early.

The parser in this chapter is simpler than
[the one in the JavaScript version][sdxjs_parse]
because teaching this material online convinced me
that the larger parser wouldn't fit in my self-imposed hour-per-lesson budget.
As I've said [elsewhere][t3],
no lesson plan survives first contact with learners;
I realize it's never going to happen,
but I think we'd be better off if technical books came with a list
of the times their authors have taught the material to a live audience.

<img class="centered" src="@root/sdxpy/parse/concept_map.svg" alt="Concept map for parsing text"/>

And on a personal note,
today is my last day at Deep Genomics.
I have three weeks to work on [some][sql_tutorial] [side][sys_tutorial] [projects][rsdx],
and then I will start work at [Plotly][plotly] on April 29.

> Terms defined: abstract syntax tree, concrete class, CSV, grammar, JSON, operator overloading, parser, token, tokenizer, YAML.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[plotly]: https://plotly.com/
[rsdx]: https://gvwilson.github.io/rsdx/
[sdxjs_parse]: @root/sdxjs/regex-parser/
[sdxpy]: @root/sdxpy/
[sdxpy_glob]: @root/sdxpy/glob/
[sdxpy_parse]: @root/sdxpy/parse/
[sql_tutorial]: https://gvwilson.github.io/sql-tutorial
[sys_tutorial]: https://gvwilson.github.io/sys-tutorial
[t3]: https://teachtogether.tech/
