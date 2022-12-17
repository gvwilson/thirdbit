---
title: "The Compassionate Programmer"
date: 2022-12-17
year: 2022
---

> I'd like the next best-seller to be
> "The Compassionate Programmer: Programming as if People Mattered"
> because I think being pragmatic hasn't played out so well.
>
> – me on Mastodon earlier today

The idea for this book first came to me while I was supervising undergrads' senior projects
in computer science at the University of Toronto.
I routinely pointed students at *The Pragmatic Programmer*,
but the more often I did,
the less satisfied I was:

1.  It had a lot to say about software design,
    but like most books on the subject,
    it made very few references to specific systems.
    ([*Beautiful Code*][beautiful-code] and [*The Architecture of Open Source Applications*][aosa]
    were inspired by this frustration.)

2.  Few of its pronouncements were backed up by empirical evidence.
    After reading Glass's *Facts and Fallacies of Software Engineering*,
    I realized that (a) we actually knew a lot about how programs and programming actually work
    and (b) many of the things I believed were either wrong or unproven.
    ([*Making Software*][making-software] and [*It Will Never Work in Theory*][nwit]
    were attempts to address this.)

3.  It left out things that mattered to me as a working programmer.
    Well into my thirties I chose not to notice
    how our industry excludes people
    who aren't affluent, white or Asian, straight, physically able, and male.
    Once I acknowledged that,
    it became impossible to read anything about teamwork or management in tech
    without asking what it said about fairness or employees' rights.

4.  While it had a lot to say about software design,
    it left out security, privacy, accessibility, and how to *not* amplify hate online.
    These can't be sprinkled onto a program after Version 1 ships,
    so I think they need to be taught just as early as design patterns or the SOLID principles.

The twentieth anniversary edition of *PP* didn't fix these shortcomings,
but neither have other books of its type.
For example,
I have eight recent books on how to be a software engineering manager on my tablet right now;
only two of them mention tech's history of discrimination and exclusion,
and none of them talk about employment rights
or what to do if your boss asks you to add an option to a wayfinding application
that will avoid police checkpoints.
(Which user persona did you think of first:
a drunk driver in Manitoba
or someone on their way home from a political protest in Tunisia?)

Hence, *The Compassionate Programmer*
(or possibly *Building Tech Together*—I dither over titles).
What would we teach young programmers about how to be better at their craft
if our starting point was the belief that people matter?
Extensible, testable designs?
Absolutely: tidying up the kitchen
so that the next person who wants to cook
doesn't have to work around your dirty dishes
is a sign of a compassionate roommate.
Version control and issue triage?
Ditto.
Debugging strategies?
Absolutely—showing a young programmer how to use a breakpointing debugger effectively
is one of the kindest things you can do for them.

But I'd include just as much on intellectual property
(because a lot of companies say or do things that aren't actually legally enforceable),
how to run a meeting so that everyone has a fair chance to be heard
([slides][meeting-slides]), [video][meeting-video]),
[danger signs in interviews][iq-personality-tests],
and [what to do if you're unfairly fired][being-fired],
because the title says "programmer" not "programming".
I'd explain [why "just tell the truth" is bullshit][radical-candor]
so that people wouldn't blame themselves for toxic management.
And I'd reference every relevant empirical study I could find
because we know a lot more than most people realize,
and because the more working programmers know about research,
the more likely they are to ask researchers to start tackling
[problems that practitioners actually care about][nwit-questions].

There's no way all of that could fit in a single book,
but here's the thing:
every book embodies its author's priorities.
When we say, "If you're going to read one thing about programming, read this,"
and the book we recommend talks about the Visitor pattern
but not about algorithmic bias,
we're telling people the former is more important than the latter.
I no longer believe that's true;
I no longer believe it's possible to excel at a craft
if we exclude how it's used and abused from our thinking about how we build it.

I've tried to write this book twice and given up both times.
I think that doing it properly would require a year of full-time work;
so far I haven't found a company or foundation willing to support that,
but even if I could,
I think it's time for fresh eyes on the problem and fresh voices on the airwaves.
If you ever take this on,
please let me know.

[aosa]: https://aosabook.org/
[beautiful-code]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[being-fired]: {{'/advice/#being-fired' | relative_url}}
[iq-personality-tests]: {{'/2021/09/13/iq-and-personality-tests/' | relative_url}}
[making-software]: https://www.amazon.com/Making-Software-Really-Works-Believe/dp/0596808321
[meeting-video]: https://www.youtube.com/watch?v=K77Mi7pysGM
[meeting-slides]: https://docs.google.com/presentation/d/1HSdgVQjq0d3UYh-aA4uWHXxYYpySn_xXwfn_M4Ms8Ts/
[nwit]: https://neverworkintheory.org/
[nwit-questions]: https://neverworkintheory.org/2022/08/30/software-engineering-research-questions.html
[radical-candor]: {{'/2018/11/24/afraid-of-change/' | relative_url}}
[sdxjs]: {{'/sdxjs/' | relative_url}}
