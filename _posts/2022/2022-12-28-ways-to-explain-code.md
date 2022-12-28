---
title: "Ways to Explain Code"
date: 2022-12-28
year: 2022
---

In the mid-1980s, Benjamin Bloom reported that
students tutored one-to-one performed two standard deviations better than
students lectured to in a class of 30.
That difference is now referred to as [Bloom's Two Sigma][bloom-two-sigma],
and serves as a measure for teaching techniques:
we don't know how good things *could* be,
but we can compare new ideas with the best thing we know.

I think about this when I think about different ways to explain programs.
The baseline is alternating static blocks of prose and code:
a bit of explanation,
a bit of software,
and so on
at scales ranging from a few lines to a few pages of each.
This format was the easiest (often only) one that could be implemented at scale
well into the 1990s,
but [as I described a few days ago][teaching-3d],
it requires both teachers and learners to do much more work
than they do when they're actually programming.
Can we do better?

When I asked that question online
several people pointed me at Bret Victor's work
(e.g., [Inventing on Principle][victor-inventing],
which I think is the other [mother of all demos][mother-demos]).
Things like the [Glamorous Toolkit][glamorous] might help us build things like
by finally freeing us from the tyranny of the punchcard,
but (a) we still have to decide what kinds of representations we want
and (b) there's not much evidence that teaching this way would actually be better.
The latter is plausible,
but I've learned the hard way that [plausible and widely believed aren't the same as true][nwit-tdd].
And even if it's true,
it's not much help today:
the overwhelming majority of instructors simply don't have time to build things like this
with today's tools.

But lots of intermediate are within reach.
One is mouseover-highlight explanations like [explainshell.com][explainshell] and [regexr.com][regexr];
I haven't seen something like this for entire programs,
but it should be buildable (at least for small pieces of code),
and I wonder if ML chat tools will make these more useful.

Another interesting intermediate is recordings of interactive sessions
(e.g., [Lorgat's SVG recordings][svg-screencast]),
possibly with voiceover (e.g., [Scrimba][scrimba]).
With a bit more work (OK, [a *lot* more work][sessioncasting])
these could turn into something approximating Victor's work,
but they still wouldn't transfer to print or ebook,
which I think is still important,
and they would still require learners to [handle the third dimension][teaching-3d] themselves.
So where does that leave us?

## Text

If we stick to textual representations of programs,
teachers and learners currently use at least four pedagogical tools:

1. Interleaved prose and code (described above).

2. Callouts, e.g., numbers in the code with explanations beside them.
   The numbers can be sequential from top to bottom,
   arranged in order of explanation (typically high-level structure then low-level details)
   or reflect execution order (e.g., 1 happens first, 2 happens next, etc.).

3. Temporal differencing in which a small piece of code is presented
   and then changed, changed, and changed again,
   with each change being shown in context.
   This method looks like interleaved prose and code but is fundamentally different:
   the instructor isn't presenting a finished program piece by piece,
   but rather growing it from a seed.

4. Incremental reveal in which the skeleton of the overall program is presented
   and then parts are filled in piece by piece.
   Again, this looks like interleaved prose and code,
   but the ordering and effect is quite different.

The biggiest problem with all of these approaches is that
maintaining the source as the lesson evolves is a nightmare.
Many people have invented systems for keeping all the variations of the code in one file
(see [Hillel Wayne's][wayne-metafiles] or [Robert Nystrom's][nystrom-crafting]),
but having written three such tools myself over the years,
using them is like looking through a stack of transparencies and trying to make sense of individual sheets.
And no,
version control tools aren't actually much help here:
trying to keep thirty or forty slight variations of a single program consistent simultaneously
isn't the use case they were designed for.

## Diagrams

We don't have to stick to text, of course.
The Unified Modeling Language failed to live up to the hype of the 1990s and early 2000s
(see [Laurence Tratt's analysis][uml-downfall] or [Marian Petre's award-winning study][nwit-uml])
but most instructors and learners still doodle to help them understand things.
Some of their notations only apply to specific use cases
(e.g., [RxMarbles](https://rxmarbles.com/) and [finite state machine][fsm] representations of regular expressions),
but many others are widely applicable:

1. Ad-hoc diagrams of data structures, HTML/CSS layout, and so on are probably the most common
   but the hardest to support with anything more than a general-purpose drawing tool.

2. Memory diagrams showing the stack and inter-object references
   as in Guo et al's [PythonTutor][pythontutor]
   are more accurate but not necessarily more useful:
   without interactive control over level of detail
   they quickly become so cluttered as to be unintelligible.

3. When the program's execution state is the data structure of interest,
   visualizations like [Loupe][loupe]'s depiction of the JavaScript event loop are wonderful.

4. UML sequence diagrams and [use-case maps][use-case-map]
   showing the exchange of messages between objects or micro-services are helpful too,
   as are dataflow diagrams showing things like operations on dataframes
   or branches and merges in Git.

Unfortunately,
diagrams of all sorts have just as many maintenance problems as evolving text:
on at least three occasions,
despite very careful proofreading,
I've published books in which the diagram had fallen out of step with the code it was supposed to explain.
And no,
tools like [Graphviz][graphviz] and [Mermaid][mermaid] don't help:
they don't eliminate the consistency and maintenance issues,
but add the extra complexity of having to compile diagrams and then tweak the layout over and over again
until the layout algorithm does approximately what you want
or you give up and tell yourself it's not actually *that* bad.

More importantly,
the use of diagrams to teach programming raises a moral question:
who are you willing to leave out?
The more we use diagrams, the less accessible our teaching materials are.
We can add text descriptions,
but if those descriptions are truly useful,
they have to solve all the problems discussed in the previous section.

## Conclusion

A lot of things have gotten better since I wrote my first program in the fall of 1980:
garbage collection,
[Stack Overflow][stack-overflow],
and meaningful action on inclusivity
have all made it easier for people to teach and learn programming.
But as I go into the last lap of my career,
I'm disappointed that our tools are indistinguishable from those
that were already widespread in that long-ago autumn classroom.
If you use others that I haven't mentioned,
I'd be grateful for pointers.

[bloom-two-sigma]: https://en.wikipedia.org/wiki/Bloom%27s_2_sigma_problem
[explainshell]: https://explainshell.com/
[fsm]: https://en.wikipedia.org/wiki/Finite-state_machine
[glamorous]: https://gtoolkit.com/
[graphviz]: https://graphviz.org/
[loupe]: http://latentflip.com/loupe/
[mermaid]: https://mermaid.js.org/
[mother-demos]: https://en.wikipedia.org/wiki/The_Mother_of_All_Demos
[nwit-tdd]: https://neverworkintheory.org/2021/09/16/analyzing-the-effects-of-tdd-in-github.html
[nystrom-crafting]: http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/
[nwit-uml]: https://neverworkintheory.org/2013/06/13/uml-in-practice-2.html
[pythontutor]: https://pythontutor.com/
[regexr]: https://regexr.com/
[scrimba]: https://scrimba.com/
[sessioncasting]: {{'/2022/12/18/sessioncasting/' | relative_url}}
[stack-overflow]: https://stackoverflow.com/
[svg-screencast]: https://wasimlorgat.com/tils/how-to-share-terminal-demos-as-razor-sharp-animated-svg.html
[t3-exercises]: https://teachtogether.tech/en/index.html#s:exercises
[teaching-3d]: {{'/2022/12/14/teaching-in-the-third-dimension/' | relative_url}}
[use-case-map]: {{'/2018/12/27/use-case-maps/' | relative_url}}
[victor-inventing]: https://www.youtube.com/watch?v=PUv66718DII
[uml-downfall]: https://tratt.net/laurie/blog/2022/uml_my_part_in_its_downfall.html
[wayne-metafiles]: https://buttondown.email/hillelwayne/archive/on-metafiles/
