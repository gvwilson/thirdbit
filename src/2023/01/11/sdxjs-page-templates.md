---
title: "Software Design by Example 9: Page Templates"
date: 2023-01-11
---

Some day I'll blog about the tools I built to create [*Software Design by Example*][sdxjs],
but if you're interested in that kind of thing,
check out Bob Nystrom's articles ([[1][crafting_1]], [[2][crafting_2]])
about how he built [*Crafting Interpreters*][crafting],
which is the most beautiful book about programming I've seen in years.
(It's worth buying a copy of the book just to admire the production values.)

[This book][sdxjs] uses a static site generator called [Ivy][ivy],
which in turn relies on a page templating tool called [Ibis][ibis].
Thousands of these have been written in the last thirty years;
most use one of three designs:

1.  Mix commands in a language such as JavaScript with the HTML or Markdown
    using some kind of marker to indicate which parts are commands
    and which parts are to be taken as-is.

2.  Create a mini-language with its own commands.
    Mini-languages are appealing because they are smaller and safer than general-purpose languages,
    but experience shows that they eventually grow
    most of the features of a general-purpose language.
    Again, some kind of marker must be used to show
    which parts of the page are code and which are ordinary text.

3.  Put directives in specially-named attributes in the HTML.
    This approach has been the least popular,
    but since pages are valid HTML,
    it eliminates the need for a special parser.

[This chapter][sdxjs_templates] used the third strategy,
partly for novelty's sake and partly because it saved us writing a parser.
What the chapter shows is that even an apparently simple task of filling in strings
requires the implementation of variables and scope—in short,
a programming language.
There are lots of ways to get this wrong;
hopefully,
this chapter will help readers get it right if it's ever their turn.

<figure id="page-templates-options" class="center">
  <img src="@root/sdxjs/page-templates/options.svg" alt="Three options for page templates" class="centered">
  <figcaption>Figure 9.1: Three different ways to implement page templating.</figcaption>
</figure>

> Terms defined: bare object, dynamic scoping, environment, lexical scoping, stack frame, static site generator, Visitor pattern.

## A Note on Open Source Etiquette

While using [Ivy][ivy] and [Ibis][ibis] on another project,
I ran into a problem that I'd never encountered before.
[Ibis][ibis] is hosted on PyPI at <https://pypi.org/project/ibis/>,
installed with `pip install ibis`,
and imported with `import ibis`.
There is another project called the [Ibis Framework][ibis_framework]
that is hosted on PyPI at <https://pypi.org/project/ibis-framework/>,
installed with `pip install ibis-framework`,
but which is *also* imported with `import ibis`.
That naming conflict makes it impossible to use the two together
without manually renaming one or the other.

[Ibis-the-templating-engine][ibis] was created first,
which I presume is why [Ibis-the-framework][ibis_framework] uses a two-part name.
I recognize that [Ibis-the-framework][ibis_framework] is a bigger project
than [Ibis-the-templating-engine][ibis],
and that the space of package names is getting pretty crowded,
but I still think the authors of the latter should have chosen a different name
to avoid the import conflict.

[crafting]: https://craftinginterpreters.com/
[crafting_1]: http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/
[crafting_2]: http://journal.stuffwithstuff.com/2021/07/29/640-pages-in-15-months/
[ibis]: http://www.dmulholl.com/docs/ibis/master/
[ibis_framework]: https://ibis-project.org/
[ivy]: https://www.dmulholl.com/docs/ivy/dev/
[sdxjs]: @root/sdxjs/
[sdxjs_templates]: @root/sdxjs/page-templates/
