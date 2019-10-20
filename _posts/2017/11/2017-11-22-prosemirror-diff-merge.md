---
title: "Diff and Merge for ProseMirror"
date: 2017-11-22 03:00:00
---

[ProseMirror][prosemirror] is one of the most interesting projects I've come across this year.
As its blurb says:

> An ideal content editor produces structured, semantically meaningful
> documents, but does so in a way that is easy for users to
> understand. ProseMirror tries to bridge the gap between Markdown
> text editing and classical WYSIWYG editors.
>
> It does this by implementing a WYSIWYG-style editing interface for
> documents more constrained and structured than plain HTML. You can
> customize the shape and structure of the documents your editor
> creates, and tailor them to your application's needs.

More specifically,
ProseMirror stores a document as JSON,
and allows the creators of custom editors to provide templates
to specify what's allowed where.
For example,
you can say that a page like this one has to have
a header with three fields called `layout`, `title`, and `date`,
a body consisting of paragraphs and block quotes,
and a list of URLs at the end.

ProseMirror is designed for real-time collaborative editing:
its author even says that [its model is useless][prosemirror-useless].
Respectfully,
I disagree:
[Jupyter Notebooks][jupyter] are stored as JSON,
[Tavish Armstrong][tavish] and his colleagues
implemented [diff and merge for them][nbdiff] back in 2014 as an undergraduate honors project,
and [nbdime][nbdime] now provides a full suite of diff and merge tools.
I think it would be really exciting to implement a general JSON-based diff-and-merge for ProseMirror
that leveraged the structural information in the schemas
in the way that [Compare++][compare] and [SemanticMerge][semantic] do syntax-aware merging for code.
"Slide moved" is just the beginning:
once there's a schema for tables,
there's the possibility of diffing rows and columns instead of the markup used to represent them,
and if anyone ever gets around to creating a diagram plugin for ProseMirror
(using a JSON encoding of SVG as a store)
we might finally get the diff tool for diagrams that I've been yearning for.

I've been advocating [extensible programming systems][xps]
(and more generally, extensible authoring systems) for years.
A few tools, like [Proxima][proxima], [Larch][larch], [MPS][mps], and [Xtext]
showed what could be done,
but the idea never caught on.
I've also been arguing that [merging is the magic that makes collaboration at scale possible][merging],
and asking (or begging) developers to implement diff and merge in LibreOffice
so that the 99% of humanity who *aren't* willing to dumb everything down to ASCII text
can use this powerful idea with the tools and formats they're already using.
Diff and merge for ProseMirror wouldn't be everything I want,
but it would be a big step in the right direction.

[compare]: http://cmpp.coodesoft.com/
[jupyter]: https://jupyter.org/
[larch]: {{site.github.url}}/2011/09/16/extensible-programming-a-new-hope.html
[merging]: {{site.github.url}}/2013/05/01/merging-is-the-real-revolution.html
[mps]: https://www.jetbrains.com/mps/
[nbdiff]: http://tavisharmstrong.com/2014/04/06/nbdiff-a-diffing-and-merging-tool-for-the-ipython-notebook/
[nbdime]: https://github.com/jupyter/nbdime
[prosemirror]: https://prosemirror.net/
[prosemirror-useless]: http://marijnhaverbeke.nl/blog/collaborative-editing.html#offline-work
[proxima]: http://foswiki.cs.uu.nl/foswiki/Proxima/WebHome
[semantic]: https://www.semanticmerge.com/
[tavish]: http://tavisharmstrong.com/
[xps]: http://queue.acm.org/detail.cfm?id=1039534
[xtext]: https://www.eclipse.org/Xtext/
