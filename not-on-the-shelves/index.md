---
layout: page
title: "Not on the Shelves"
---

*From the introduction to the [first version](./1997/):*

I was watching *Field of Dreams* a couple of nights ago.
When the ghostly voice whispered,
"If you build it, they will come,"
I thought,
"That's it!
If I write reviews of the books I'd most like to read,
maybe someone will write the books!"

As I was nursing my hangover the next morning
I explained my plan to a friend.
She took the icepack off her forehead long enough to explain
[sympathetic magic][magic] to me.
According to her,
there's a tribe whose land is occasionally stricken by drought.
When the rain fails,
the elders plow the soil anyway
in the hope that doing so will force the rain to come.

After reviewing dozens of computer-related books,
I'd happily sacrifice a rooster to get someone to write something *different*.
I'm constantly amazed by how few books there actually are:
my local bookstore has eight shelves of Java books,
but if you did a set-union on their contents,
you'd be left with only two or three.
What's worse,
a lot of things I really want to know wouldn't be there at all.

These reviews are my attempt to point out the gaps in the computing literature,
and indirectly,
the gaps in most programmers' education (including my own).
Over the years,
they have inspired
[*Beautiful Code*][bc],
[*Making Software*][ms],
[*The Architecture of Open Source Applications*][aosa],
[*Research Software Engineering with Python*][rsepy],
and [*Software Design by Example*][sdxjs].
If you know of other books that match these descriptions,
please give me a shout;
if you'd like to write one,
please get in touch as well---I'd be happy to help if I can.

Past Versions:
<a href="./2017/">2017</a>
&middot;
<a href="./2014/">2014</a>
&middot;
<a href="./2009/">2009</a>
&middot;
<a href="./2003/">2003</a>
&middot;
<a href="./1997/">1997</a>

<hr/>

Please also see the discussion of
[*Sex and Drugs and Guns and Code*]({{'/ideas/sdgc/' | relative_url}})
and [*Software Engineering: Compassion, Evidence, Process, and Tools*]({{'/ideas/secept/' | relative_url}}).

## *How to Keep a Tech Company Going*

There are hundreds of books and thousands of talks about how to do a startup,
but English doesn't even have a word for a "keep going"---for
a company that is as big as it needs to be
and can continue quite happily at that size as long as people do things right.
This book describes that:
how to shift to new business areas as the world changes,
how to replace staff who move on,
and how to keep legacy code going through years of updates.

## *How to End a Tech Company*

Just as there aren't books about how to keep tech companies going,
there aren't any about how to _end_ a tech company.
This isn't another Musk/Twitter joke:
most startups don't make it,
so this book shares advice on how to take care of staff,
get investors what they're owed,
make sure useful software isn't lost,
grieve, reflect, and move on.
(See also [this talk]({{'/talks/#late-night-thoughts' | relative_url}}).)

## *Managing Research Software Projects*

Your graduate degree is in ecology,
but now you're running a three-person team responsible for building and maintaining a hundred thousand lines of code?
This book is an overview of everything you absolutely, positively need to know
*after* you know how to program:
[marketing](https://www.amazon.com/Marketing-Scientists-Shine-Tough-Times/dp/1597269948/),
[community management](http://producingoss.com),
[leading a lab](https://www.amazon.com/At-Helm-Leading-Laboratory-Second/dp/0879698667/),
and [basic finance](http://ecampus.oregonstate.edu/soc/ecatalog/downloadsyllabus.htm?docid=2641&subject=PSM&cn=565).
We've [made a start]({{'/mrsp/' | relative_url}}),
but there's a lot still to be done.

## *Computing and the Law: A Guide for the Perplexed*

The legal aspects of software have always been complicated;
the web has done nothing to make them simpler.
This book seeks to help programmers understand the rules (or lack thereof)
they have to live with
by tracing the historical development of patents, copyrights, privacy, and professional liability
from the Industrial Revolution to the present day.
Aimed squarely at people with no prior exposure to legal terminology,
it explains concepts clearly and provides examples for each.

## *Now What? A Practitioner's Guide to Error Handling*

Programs can fail in a hundred different ways,
but most programmers either ignore the possibility of failure
or deal with it by printing a log message.
This book presents examples of what they could do instead,
from data structure repair to automatically restarting servers.
Along the way,
it catalogs the kinds of errors that programmers may encounter
and shows how they can be prevented as well as managed.

## *Concurrent Design by Example*

[*Software Design by Example*]({{'/sdxjs/' | relative_url}}) described
small versions of single-threaded command-line tools,
but most of today's tools are concurrent and distributed.
This book looks at the design of such systems,
from message queues to overlapping I/O and user interfaces.
Along the way it touches on some of the same ideas as *Now What?*,
but shows how to use things like file locking and retry protocols
to prevent or ameliorate faults.

## *300 Lines of Science*

Can you write a climate simulator in less than 500 lines of Python?
What about constructing phylogenetic trees in less than 500 lines of R?
This collection would show readers how science is turned into code across a broad range of disciplines.
Each entry is less than 300 lines of code in the style of *[500 Lines or Less](http://aosabook.org/en/index.html#500lines)
or [*Software Design by Example*]({{'/sdxjs/' | relative_url}}),
supplemented by an equal-sized chunk showing how to test what has been written.

## *A Practical Introduction to Debugging*

Most programmers spend a large part of their time debugging,
but most books only show working code,
and never discuss how to prevent, diagnose, and fix errors.
[Most](http://www.amazon.com/Debugging-Indispensable-Software-Hardware-Problems/dp/0814474578/)
[books](http://www.amazon.com/Debugging-Thinking-Multidisciplinary-Approach-Technologies/dp/1555583075/)
[ostensibly](http://www.amazon.com/Debug-It-Prevent-Pragmatic-Programmers/dp/193435628X/)
[about](http://www.amazon.com/The-Developers-Guide-Debugging-Edition/dp/1470185520/)
[debugging](http://www.amazon.com/The-Art-Debugging-GDB-Eclipse/dp/1593271743/)
are either high-level handwaving ("Make sure you're solving the right problem"),
user's guides for particular debugging tools,
or [out of date](http://www.amazon.com/Find-Bug-Book-Incorrect-Programs/dp/0321223918/).
The one notable exception,
Zeller's *[Why Programs Fail](http://www.amazon.com/Why-Programs-Fail-Second-Edition/dp/0123745152/)*,
is an excellent read,
but too advanced for most undergraduates.
This book fills that gap by combining an exploration of how debugging tools actually work
with dozens of case studies showing how to apply them to real-world problems.
And while the author only occasionally makes this explicit,
the book also shows how to write programs that are easier to fix.

## *Performance Tuning*

In the spirit of Jon Louis Bentley's *[Writing Efficient Programs](https://www.amazon.com/Writing-Efficient-Programs-Prentice-Hall-Software/dp/013970244X/)*,
this book shows readers how to model, analyze, and improve the performance of their programs.
Written for undergraduates who already have a basic understanding of computer architecture, compilers, operating systems, and networks,
it can be used in a capstone course that unifies ideas from these subjects.

## *Difference Engines*

Modern version control systems handle text well,
but are much clumsier when it comes to images, MP3s, spreadsheets, and other so-called "binary" files.
The reason is simple:
those formats are supported by tools for reading and writing,
but not for differencing and merging.
This survey describes a collection of open source libraries
(the "engines" of the title)
that can handle many of those formats in a more-or-less uniform way.
Readers will enjoy the combination of theory
(such as proofs of some algorithms' performance characteristics)
and practice
(the design and implementation of the tools themselves).

[aosa]: http://aosabook.org/
[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[magic]: http://en.wikipedia.org/wiki/Sympathetic_magic
[ms]: https://www.oreilly.com/library/view/making-software/9780596808310/
[rsepy]: https://www.taylorfrancis.com/books/mono/10.1201/9781003143482/research-software-engineering-python-damien-irving-kate-hertweck-luke-johnston-joel-ostblom-charlotte-wickham-greg-wilson
[sdxjs]: https://www.taylorfrancis.com/books/mono/10.1201/9781003317807/software-design-example-greg-wilson
