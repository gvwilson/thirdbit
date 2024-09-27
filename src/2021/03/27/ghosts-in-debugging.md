---
title: "The Ghosts in the Debugging"
date: 2021-03-27
---

A couple of days ago I tweeted:

> I would trade my left nostril for a decent book on debugging.
> (I realize that's not much of an incentive for potential authors, but I hope it'll be taken as a sign of how desperate I am.)

An hour or so later I followed up with:

> My apologies to people who *have* written good books on debugging - there are several, and I shouldn't have implied there weren't.
> What I should have written was "another dozen good books on debugging" and specified what I meant by "good". My bad.

Before I go on to the main point of this post
I'd like to reiterate that apology and point at the books I know of:

- Andreas Zeller: *[Why Programs Fail](https://isbndb.com/book/9780123745156)*
- David J. Agans: *[Debugging](https://isbndb.com/book/9780814474570)*
- Diomidis Spinellis: *[Effective Debugging](https://isbndb.com/book/9780134394886)*
- Adam Barr: *[Find the Bug](https://isbndb.com/book/9780321223913)*

I reviewed all four of these for *[Doctor Dobb's Journal](https://www.drdobbs.com/)* when they first came out;
I apologize again to their authors.
But these books are all more than a decade old;
I don't know of anything useful that's appeared more recently
except for *[The Fuzzing Book](https://www.fuzzingbook.org/)* and *[The Debugging Book](https://www.debuggingbook.org/)*
(both of which are works in progress from Andreas Zeller and colleagues).
A quick check on an online bookstore tells me that
in the time it's taken our profession to write six books on debugging,
we have written over a hundred on compilers
and a roughly equal number on operating systems.
Again on Twitter:

> I used to think the reason there are several hundred books on parsers and compilers in print
> but only a handful on debugging stems in part from the fact that debugging doesn't have a mathematical foundation
> (i.e., there are no theorems to prove).
> But I no longer think that's the case - there are lots of good books on the practical aspects of operating systems and network stacks, for example.
> My current theory is that debugging is mostly about verbs rather than nouns, and we're just not very good at teaching verbs.
> We do a much better job of teaching code than teaching coding:
> for example, there are a gajillion tools for checking style,
> but I don't know of any that watch the order in which you write things and says,
> "Maybe you should have written *this* before *that*."

Mark Guzdial replied:

> I have a hypothesis that we can't teach debugging.
> We can teach a debugging process as rules ("When you see this, do that"), but we can't teach [students] to be successful debuggers.
> Debugging is a process of looking at a situation, noting that it's wrong, and developing a theory for why…
> You have to know enough patterns/situations to see what's wrong and to match to a known pattern,
> re: [Marton's Variation Theory](https://math4teaching.com/what-is-variation-theory-of-learning/).
> The more you know, the more you realize what can go wrong, and better you are debugging…
> You become better at debugging by knowing more ways to do things and learning more ways that things can go wrong.
> So we become better at debugging by developing more domain knowledge, not by studying debugging.

While I'm reluctant to disagree with Mark (who knows more about education than I ever will),
I've helped people debug systems in languages I didn't speak and in domains I'd never worked in,
so I think there is some useful generic skill there.
I've also seen people teach others how to analyze chess positions or criticize a literary work;
rather than enunciating rules,
they carefully select interesting cases and draw attention to features of interest.
They're not trying to pass on algorithm:
they're training the neural network between the student's ears.

The best example of this approach I know of in computing is Jeff Johnson's wonderful book
*[GUI Bloopers](https://isbndb.com/book/9780123706430)*.
Rather than trying to teach user interface design directly,
Johnson thinks through the shortcomings of some real-world interface elements
(e.g., the font selection dialog in Microsoft Word)
and shows readers what he would do instead.
Of the debugging books I mentioned earlier,
only Barr's *[Find the Bug](https://isbndb.com/book/9780321223913)* makes this approach central:
with apologies for the generalization,
the other books use examples to illustrate big ideas,
while Johnson and Barr derive big ideas from examples.

All of which brings us to [a great blog post from Vicki Boykis](https://veekaybee.github.io/2021/03/26/data-ghosts/)
about the difference between implicit and explicit knowledge
and about what she calls "ghost knowledge":
the implicit knowledge that nobody in your field ever writes down.
Her focus is data science,
but what she says applies to debugging as well.
I believe that indiviual practitioners know a lot that *could* be taught explicitly—they
just don't write it down.
More specifically, I hypothesize that:

1.  The more domain knowledge you have the more effectively you can debug,
    but there is a domain-independent "how to find and fix the problem" skill
    and people can learn it.

2.  The best way to teach that skill is to think aloud through carefully-selected case studies.
    Learners can only apply general rules about debugging
    *after* seeing a large number of case studies.
    (I say "apply" rather than "understand" because I think it's possible to understand something in the abstract
    but not know how to use it in the concrete.)

3.  Debugging is not taught in most college and university computer science programs
    because case-based instructions feels like [stamp collecting](https://www.goodreads.com/quotes/275894-all-science-is-either-physics-or-stamp-collecting)
    to people who aren't used to it
    and whose discipline looks to mathematics rather than medicine for pedagogical inspiration.

The first two are testable
(I'm exploring the first one with some colleagues right now).
I think, or at least I hope, that the third is fixable,
which is part of why I'm reading everything I can find on
[implementation science](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4573926/)
and [its application to higher education](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7644597/).
I'll let you know what I find…
