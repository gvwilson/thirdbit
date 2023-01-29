---
title: "More Thoughts on Document Compilers"
date: 2021-09-23
year: 2021
---

I let fly with some half-baked complaints about the state of document compilers on Twitter yesterday,
so I'd like to try to get some more organized thoughts down before I'm distracted again.

1. By now we should all be using WYSIWYG tools.
   We don't because version control tools refuse to diff and merge them.
   I've ranted about this [before]({{'/2011/09/16/extensible-programming-a-new-hope/' | relative_url}});
   I no longer believe it's going to be fixed in my working lifetime,
   so I'll move on.

1. Jamstack's list of open source static site generators (SSGs) currently has
   [over 300 entries](https://jamstack.com/generators/).
   Most of them are designed with blogging in mind,
   which means they don't meet a lot of other authorial needs out of the box:

   - Numbering chapters, sections, and subsections consecutively across files (e.g., across chapters).
   - Numbering figures, tables, examples, exercises, and everything else an author might want.
     (No matter what counters you provide, people are going to need another one—for example,
     did you notice that "theorems" wasn't in the previous sentence's list?)
   - *Not* requiring document names in cross-references,
     because content often moves between files.
   - *Not* requiring manual numbering (e.g., an order number or weight in each chapter) because ditto.
   - Handling bibliographic citations, glossary references, index references, and a bunch of other things
     without requiring a lot of typing.

   Most SSGs are extensible *if you speak the language* (more on this below),
   but many insist on a page-at-a-time processing model
   so that (for example) consecutive sequential numbering of figures *across* rather than *within* chapters
   simply isn't doable without external processing.

1. There are layers on top of SSGs that handle some of these things,
   but in my experience they're very fragile.
   (Go ahead, try to figure out which of Bookdown's several configuration files you need to modify
   to change the way pages are numbered.)
   A large part of that fragility comes from reliance on LaTeX and/or Pandoc.
   These are both powerful tools,
   but like FORTRAN,
   the startup costs for casual users are prohibitive
   and the number of expert users is slowly but steadily dwindling.
   (Try to get the LaTeX templates of any of the major publishers to work nicely with the SSG of your choice
   and tell me how long it took you.
   Now go to someone who hasn't used LaTeX as long as you have and see how long it takes them.)

1. "Everybody should use the right tool for the job" isn't a solution for the people I want to help,
   any more than "everybody should use the right programming language for the job,"
   because most people don't have the free time I had in my twenties to master obscure technologies.
   If you don't agree,
   we're probably thinking about different audiences.

One thing yesterday's Twitter exchange helped me realize is that
I think user-level in-tool extensibility is a must-have.
For all its quirks,
most people can build the customizations they want for LaTeX *in the tool itself*.
If you want to extend Pandoc you have to write in—well,
you get to pick,
which means that someone else who wants to use your extension has to install that language's toolchain.
(Have fun.)
You also have to work at the parse tree level rather than by slinging bits of text around;
I recognize that the former is more general,
but so is assembly code.

At this point I'd like to put forward a proposal that solves all these problems at once,
but I don't have one.
"Simple things are easy and hard things can be approached gradually without switching paradigms"
is what every tool builder aspires to,
but that doesn't mean it's always achievable.
I think that LaTeX-style text splicing is enough for a lot of common cases,
but a Turing-complete extension language is needed for more complex things,
and that language should be one that people use anyway instead of (for example)
the bastardized Ruby that things like Jekyll provide.
I've played with some SSGs that use JavaScript as the extension language,
and liked them,
but they don't provide a simpler mechanism equivalent to LaTeX's `\newcommand`
with a couple of string parameters.

And of course my perspective is heavily biased by my background
and I might completely misunderstand the problems that most people face.
If anyone knows of a comparative usability study of different document compilers
(something more than just one person's drive-by based on misreading those tools' home pages),
I'd be grateful for a pointer.
