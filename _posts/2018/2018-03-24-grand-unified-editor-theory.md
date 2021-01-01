---
title: "Grand Unified Editor Theory"
date: 2018-03-24 03:30
year: 2018
---

It's a sad fact that you can't get a PhD in Computer Science simply by building an innovative piece of software.
That's partly due to a double standard among academic computer scientists,
who insist that their discipline isn't just about coding
but are happy to let students and their parents believe that a CS degree is the key to a well-paid coding job,
but it's also a failure on the part of practitioners,
who have still not developed a serious critical theory or vocabulary
like those found in architecture and industrial design.
(The fact that a more rigorous successor to *[The Architecture of Open Source Applications](http://aosabook.org)*
isn't a standard part of the undergraduate curriculum is a sign of how far we still have to go.)

But if building novel software was a path to doctoralhood,
I know one of the things I'd want someone to build.
On the one hand we have version control systems like CVS, Subversion, and Git,
with which people asynchronously edit private copies of sets of documents,
then merge their changes,
resolving any conflicts that have arisen.
On the other hand we have online concurrent editors like Google Docs, Etherpad, and ProseMirror,
with which people synchronously edit a shared public copy of a single document.
These systems use some variation of [operational transformation](https://en.wikipedia.org/wiki/Operational_transformation) (OT)
to merge fine-grained edits as they occur
rather than delaying merges until users are satisfied with a set of changes
and then having to deal with larger-grained conflicts.

I want a system that unifies these two models.
If people are editing a shared master copy online,
the editor would combine their changes in real time using OT.
However,
they could also choose to fork a copy of the document (or set of documents) and make modifications offline.
Those modifications would be recorded as a stream of transformations
that could be replayed when it was time to merge,
which I suspect would be a sounder approach than that ad hoc methods used by today's version control systems.

This tool would instantly be useful,
since it would allow people to move smoothly between "let's all make small changes together",
"I'm going to make a few changes on my laptop while the network is down",
and "let me go try this out on my own for a while and then share the results".
It would be even more useful if it supported editing of non-textual documents such as images and spreadsheets,
but that could come later.
The best thing,
though,
is that there's enough algebra (to prove that the operational transforms were sound)
and performance measurement (to demonstrate practicability)
that someone actually *could* get a PhD out of it.

If this tool already exists, I'd be grateful for a pointer.
Otherwise…any takers?
