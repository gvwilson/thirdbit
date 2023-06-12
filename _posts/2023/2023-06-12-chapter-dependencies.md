---
title: "Chapter Dependencies"
date: 2023-06-12
year: 2023
---

I'm making [slow but steady progress][progress]
on the Python version of [*Software Design by Example*][sdxjs],
and would be grateful for help with something
that's been in the back of my mind for a while.
Every one of my books has a [glossary][sdxjs-glossary] and an [index][sdxjs-index].
I create both by manually adding markup to the Markdown source files for each chapter,
but I believe it should be possible to do the following:

1.  Identify all uses in all chapters of all the terms in the glossary
    (matching inflected variants like "refactoring" and "refactored" to "refactor")
    so that I can decide which uses should be in the index.

2.  Identify all uses in all chapters of all glossary terms
    so that I can make sure each first use is highlighted.
    (I want tooling to help with this because I sometimes rearrange chapters,
    and re-checking after each shuffle is tedious and error-prone.)

3.  Given the sets of terms defined and used in each chapter,
    construct a graph like the one shown below
    to show which chapters are prerequisites for which.
    (The final book will put chapters in a strict order,
    but their actual relationship is only a partial order.)

<div align="center">
<img src="{{'/files/2023/sd4ds-preliminary-syllabus.svg' | relative_url}}" alt="Preliminary syllabus dependency graph for software design book">
</div>

What ties these needs together is the notion of dependency management.
When I ask a package manager to install library A,
part of its job is to figure out that A depends on B and C,
both of which depend on D.
Similarly,
when my code imports B,
my language's runtime is responsible for loading D as well.
In theory,
dynamic imports with constructed names make this impossible to do 100% of the time,
but in practice the problem is mostly solvable.

I'd like to do the same for lessons.
I'd like to be able to point a tool at a set of lessons and have it tell me
what ideas are explained in each
and which lessons depend on ideas that are explained elsewhere
so that I can build a curriculum,
check for circularity,
and so on.
I think this ought to be possible using tools like [NLTK][nltk] and [spaCy][spacy],
but I don't know enough about natural language processing
to accomplish anything useful in the 3–4 hours I've budgeted for this.
(A big part of getting a book out the door is putting strict limits on
the time you spend [shaving yaks][yak-shaving].)
If you can help,
or if you have a couple of scripts I could tinker with,
please [reach out](mailto:{{site.author.email}}).

[nltk]: https://www.nltk.org/
[progress]: {{'/2023/06/04/slow-progress/' | relative_url}}
[sdxjs]: https://third-bit.com/sdxjs/
[sdxjs-glossary]: https://third-bit.com/sdxjs/glossary/
[sdxjs-index]: https://third-bit.com/sdxjs/contents/
[spacy]: https://spacy.io/
[yak-shaving]: https://en.wiktionary.org/wiki/yak_shaving
