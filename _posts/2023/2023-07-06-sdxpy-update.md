---
title: "Software Design in Python: Status Update"
date: 2023-07-06
year: 2023
---

The Python version of [*Software Design by Example*][sdxjs] is getting closer.
Here's where the content is falling short of my targets right now:

| Content   | Chapters Under Target |
| :-------- | --------------------: |
| Slides    |                  2/27 |
| Exercises |                  9/27 |
| Figures   |                 13/27 |
| Words     |                  7/27 |

In more detail:

| Title    | Slides | Exercises | Figures |    Words |
|:---------|-------:|----------:|--------:|---------:|
| Introduction |     10 |       _0_ |       2 |     1167 |
| Objects and Classes |     17 |       _2_ |       4 |   _1019_ |
| Finding Duplicate Files |     19 |         5 |       5 |   _1752_ |
| Matching Patterns |     22 |         8 |       4 |     1763 |
| Parsing Text |     15 |       _3_ |     _3_ |   _1194_ |
| Running Tests |     16 |         7 |       4 |     1933 |
| An Interpreter |     16 |         8 |     _2_ |     1933 |
| Functions and Closures |     19 |         4 |     _3_ |   _1422_ |
| Mocks, Protocols, and Decorators |    _5_ |       _2_ |     _3_ |     1842 |
| A File Archiver |     19 |         7 |     _3_ |     2132 |
| An HTML Validator |     20 |       _0_ |     _3_ |   _1296_ |
| A Template Expander |     23 |        10 |     _2_ |     2240 |
| A Code Linter |     20 |         7 |     _2_ |     2183 |
| Page Layout |     17 |        10 |       7 |     2277 |
| Performance Profiling |     26 |        11 |       8 |     3239 |
| Object Persistence |     15 |        10 |       4 |     3237 |
| Binary Data |     25 |         6 |       4 |     3896 |
| A Database |     27 |       _3_ |       4 |     2202 |
| A Build Manager |     18 |         8 |       4 |     1822 |
| A Package Manager |     23 |         8 |       4 |     3001 |
| Transferring Files |     19 |         4 |     _3_ |     1814 |
| Serving Web Pages |     18 |         9 |     _3_ |     2256 |
| A File Viewer |     32 |       _3_ |     _2_ |     2955 |
| Undo and Redo |     20 |       _0_ |     _2_ |   _1241_ |
| A Virtual Machine |     19 |        10 |       6 |     2242 |
| A Debugger |     21 |        10 |       4 |     2808 |
| Conclusion |    _3_ |       _0_ |       1 |      485 |
| Total    |    504 |       155 |      96 |    55351 |
| Average  |   18.7 |       5.7 |     3.6 |     2050 |

The syllabus has also evolved a bit—I still need to figure out
how to tie those three isolated chapters into the main narrative.

<div align="center">
<img src="{{'/files/2023/sdxpy-syllabus-2023-07-06.svg' | relative_url}}" alt="Syllabus for 'Software Design by Example in Python' as of 2023-07-06">
</div>

Finally,
the glossary now has 336 entries;
only 289 terms are indexed,
but that's always the very last step (at least for me).
There are 34 open issues in the book's GitHub repository
that will take anything from a few minutes to half a day to close,
and 7 suggestions for chapters in a second volume
that I've promised myself I'm not going to write.

[sdxjs]: {{'/sdxjs/' | relative_url}}
