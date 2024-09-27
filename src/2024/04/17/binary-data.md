---
title: "Software Design by Example in Python 17: Binary Data"
date: 2024-04-17
---

Packing and unpacking binary data is a well-trodden path
and a natural follow-on to [object persistence][sdxpy_persist].
After explaining how integers are stored in memory,
what bitwise operations do,
and UTF-8 character encoding,
[Chapter 17: Binary Data][sdxpy_binary] shows how to create self-describing binary records
whose first few bytes describe the format of the rest.
It's a lot for one chapter,
and I was pleased that people who'd never encountered the ideas before
could get through it in an hour.
In particular,
I remember feeling, "That can't possibly work," when I first ran into self-describing data.
It still feels a bit like magic,
but I'm comfortable with that now.

<img class="centered" src="@root/sdxpy/binary/concept_map.svg" alt="Concept map for binary data"/>

> Terms defined: ANSI character encoding, ASCII character encoding, bit mask, bit shifting, bitwise operation, boxed value, buffer (in memory), character encoding, code point, continuation byte, control code, escape sequence, exclusive or, format string, sign and magnitude, two's complement, Unicode, UTF-32, UTF-8, variable-length encoding.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: @root/sdxpy/
[sdxpy_binary]: @root/sdxpy/binary/
[sdxpy_persist]: @root/sdxpy/persist/
