---
title: "Software Engineering Education"
date: 2020-04-30
---

I was surprised and honored to be given
[ACM SIGSOFT's Influential Educator Award]({{site.github.url}}/2020/03/30/sigsoft-educator.html)
for 2020.
Now that I've had a chance to digest the news,
I have a few thoughts about software engineering education that I'd like to share.
None of them will be new to regular readers of this blog,
but I hope they'll make more sense if they're all in one place.

1.  **Stop asking students to follow a process when they can't.**
    Many software engineering courses put students into project teams
    and ask them to do all the things they'd do if they were building a product:
    gather requirements, architect a solution, test it, and so on.
    That's great,
    except that these courses also often ask them to follow some name-brand process like Scrum
    when they actually can't:
    most of them are taking four, five, or six courses concurrently,
    and since their instructors don't coordinate homework deadlines,
    students simply can't work in the steady, focused fashion that brand-name processes assume.

2.  **Don't spend more than a lecture on UML.**
    In the 25 years since its creation
    I've only met one programmer who actually used it,
    and he was a Russian mathematician who'd read up on knot theory before tying his shoes.
    My friend and mentor [Marian Petre](http://www.open.ac.uk/people/mp8)
    won an award for [her paper](http://oro.open.ac.uk/35805/)
    analyzing why developers mostly ignore it;
    given that we have better ways to model software (discussed below),
    I think that forcing it on today's students
    is about as useful as requiring doctors to learn Latin.

But if not this, then what?

1.  **Teach software architecture by example.**
    I taught a senior software architecture course three times in 2006–07,
    then told the university they should cancel it.
    The reason was a lack of meaningful material:
    the eight books I had with "Software Architecture" in their titles
    told readers how to gather architectural requirements
    and how to document architectures,
    but between them devoted a grand total of 20 pages
    to describing the actual architectures of actual systems.

    *[Beautiful Code](http://shop.oreilly.com/product/9780596510046.do)*
    and *[Architecture of Open Source Applications](http://aosabook.org)*
    were attempts to create the raw material I wished I'd had.
    I believe more strongly than ever that this is the right approach—that
    we should teach students how to read and reason about the source of medium-to-large applications.
    The assignments in such a course would include
    building working models of those applications
    like [Matt Brubeck's browser engine](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
    and [Conor Stack's little database](https://cstack.github.io/db_tutorial/),
    or comparing and contrasting things like the undo/redo stacks in Emacs and Vim
    or the data structures beneath Git and Mercurial.
    I expect graduates of such a course would be much better able
    to contribute to complex real-world applications,
    and would know enough about prior art
    to avoid making *all* of their predecessors' mistakes.

2.  **Teach data science for software engineering.**
    Can we predict whether or not a bug will be fixed
    based on how quickly someone first responds to it?
    What is the best indicator of when we'll be ready to release a package:
    the number of outstanding bugs or the rate at which new bugs are being found?
    And are commits on Friday afternoon more or less likely to contain bugs
    than commits made at other times?
    Other engineering disciplines tackle their equivalents of these questions
    by collecting data and analyzing it statistically.

    We should do the same.
    We should teach software engineers how to collect, clean, analyze, and present
    data from and about their own products and processes.
    Conferences like [Mining Software Repositories](http://www.msrconf.org/)
    have made a lot of raw material available
    and produced some fascinating results for students to replicate (or refute).
    It's culturally defensible—no one ever got fired
    for saying that computer science students ought to learn more math—and
    given how hot data science is right now,
    students would flock to a course with that title.
    I expect graduates of such a course would be more skeptical of
    the bandwagons that roll through Silicon Valley every couple of years,
    and (from a professorial point of view)
    would be much better prepared to tackle interesting problems in grad school
    than most of today's students.

3.  **Teach rigorous modeling.**
    Teach students [TLA+](https://www.apress.com/us/book/9781484238288)
    and [Alloy](https://alloytools.org/).
    Their user interfaces are awful,
    but if enough young programmers are exposed to the joy of rigor,
    one of them will eventually create a tool that's usable as well as powerful.

Changing the curriculum is always hard,
but trying to do things the right way when your situation won't let you is harder,
and having to pass exams on things you know you'll never use is harder still.
I think we owe it to our students to change as well as teach;
I hope I can use whatever influence I have to push us in that direction,
and if you'd like to help,
please [get in touch](mailto:gvwilson@third-bit.com).
