---
date: 2019-01-26
title: "The Elements of Programming Writing Style"
---

Along with my [list of unwritten books](@root/2019/01/06/not-on-the-shelves-2019/) about programming,
I've kept a haphazard list of ones that have influenced the way I write about the subject.
Sometimes what I've learned from them is stylistic,
other times it's about how to shape content,
but I think they're all worth looking at if you're writing about code.

-   *[Software Tools in Pascal](https://www.amazon.com/Software-Tools-Pascal-Brian-Kernighan/dp/0201103427/)*
    by Kernighan and Plauger
    and *[The C Programming Language](https://www.amazon.com/Programming-Language-2nd-Brian-Kernighan/dp/0131103628/)*
    by Kernighan and Ritchie
    get everything right:
    the prose is so clear it's almost transparent,
    new ideas are introduced exactly as needed,
    and every example is something the reader would actually want to do.

-   Stroustrup's *[The Design and Evolution of C++](https://www.amazon.com/Design-Evolution-C-Bjarne-Stroustrup/dp/0201543303/)*
    is a bit more difficult to get through in places,
    but it's a great example of challenge-and-response exposition:
    here's an idea,
    here's why it's interesting,
    here are its shortcomings or the second-order problems that arise from its use,
    here's how to solve those,
    and so on and so on.
    I don't know if Stroustrup was inspired by
    Lakatos's *[Proofs and Refutations](https://www.amazon.com/Proofs-Refutations-Mathematical-Discovery-Philosophy/dp/1107534054/)*,
    but several of the best chapters in *[The Architecture of Open Source Applications](http://aosabook.org)*
    used this recapitulatory approach as well,
    and I think it's the best way to explain the design of any complex thing.

-   Johnson's *[GUI Bloopers](https://www.amazon.com/GUI-Bloopers-2-0-Interactive-Technologies/dp/0123706432/)*
    doesn't go from simple to complex,
    but from clumsy to elegant.
    Each small section (2--4 pages) analyzes a flaw in a specific user interface—the font selection
    dialog in Microsoft Word, for example—and then describes how it could be improved.
    This is much more effective than any direct exposition of high-level rules like "make use of negative space",
    since it allows the reader to build and test a mental model grounded in specifics.
    (In my experience, expounding on general rules is usually ineffective,
    since the reader must already more-or-less understand the subject in order to understand the rules.
    One of the few exceptions I've encountered is
    Bentley's *[Writing Efficient Programs](https://www.amazon.com/Efficient-Programs-Prentice-Hall-Software-1982-05-23/dp/B01N1WX781/)*.)

-   Kerievsky's *[Refactoring to Patterns](https://www.amazon.com/Refactoring-Patterns-Joshua-Kerievsky/dp/0321213351/)*
    is explicit where *GUI Bloopers* is implicit.
    In it,
    the author takes two big ideas—design patterns and refactoring—and shows how they are complements of one another.
    Design patterns are the resting states of software;
    refactorings are how to move software from one of those states to another.
    It's one of the few examples I know of effective big-picture exposition.

-   Rather than starting with something simple and adding well-motivated complexity,
    Olsen's *[Design Patterns in Ruby](https://www.amazon.com/Design-Patterns-Ruby-Russ-Olsen/dp/0321490452/)*
    presents what a naturalist would call type specimens:
    each design pattern is explained by showing examples of its use in the Ruby standard library.
    As with the books by Kernighan et al,
    this authenticity adds authority to the writing,
    and I would bet that in searching for examples,
    the author learned a great deal more about his chosen subject.

-   McConnell's *[Code Complete](https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/)*
    completely changed how I view programming and how I (try to) write about it.
    I'd been working for ten years, and had recently completed a PhD,
    and had absolutely no idea that there was this much evidence about software engineering.
    It's not an exciting read,
    but statement after claim after suggestion is backed up with references to empirical research.
    If nothing else
    it made me impatient with [other books](https://www.amazon.com/Pragmatic-Programmer-Journeyman-Master/dp/020161622X/)
    that make general claims based on anecdotes and personal experience.

-   Petzold's deep love for his subject shines through in every page of
    *[The Annotated Turing](https://www.amazon.com/Annotated-Turing-Through-Historic-Computability/dp/0470229055/)*.
    He doesn't gush,
    or tell us how important Turing's seminal paper on computability was;
    instead,
    he dissects it line by line and word by word,
    using everything from its typography to its method of proof
    as starting points for engrossing little excursions into the intellectual world of the 1930s
    and the ripples from it we still swim in today.
    Few books on any subject have been so quietly enjoyable.

There are a lot of other rewarding books about computing,
and quite a few whose reputation I struggle to understand,
but there are the ones that I think have had the most influence on *how* I write.

What struck me as I compiled this list is that the authors on it are all white and male.
I don't know how that has affected my writing style,
but the books I have enjoyed most in the past few years,
like Jemisin's *[Broken Earth](https://www.amazon.com/Broken-Earth-Trilogy-Season-Obelisk/dp/031652719X/)* trilogy
or Jahren's *[Lab Girl](https://www.amazon.com/Lab-Girl-Hope-Jahren/dp/1101873728/)*,
have made me wonder how many more exemplars of great writing we might have in computing
if we were to stop making most people feel unwelcome.
As someone who thinks that a well-crafted page is as close to paradise as I'm ever likely to get,
I think it's just one more reason to try to fix what's broken in our profession.
