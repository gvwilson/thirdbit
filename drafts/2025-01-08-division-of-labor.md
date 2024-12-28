---
title: Division of Labor
date: 2025-01-08
---

All right, you've [formed a team][forming-teams]:
now what?
How do you decide who does what?
How do you make sure that everyone actually does what they're supposed to?
And most importantly, how do you do this fairly?

Some jobs have higher social status than others,
and what is or isn't considered important
usually reflects racial and gender divides within society—so much so that
sociologists use the phrase "[women's work][womens-work]" to describe the phenomenon.
It is also known as "[quarterback syndrome][quarterback-syndrome]":
two thirds of NFL players overall in the United States are Black,
but only 17% of quarterbacks,
which is the position on a team with the highest social status.

Among programmers,
writing operating systems or other software that is close to the hardware
has higher status than building user interfaces;
people doing the former are both paid more and more likely to be male
than people doing the latter,
regardless of ability or value delivered to the employer.
This creates a feedback loop:
white and Asian men pursue certain career paths because they have high status
(they want to be "real programmers"),
and the fact that they are pursuing those careers is what maintains their higher status.
It also creates a confirmation loop:
since women and people of color get fewer chances to do certain tasks,
they are less good at them,
which "confirms" the initial bias.

All of this starts in the classroom.
In mixed-gender teams,
for example,
female students are more likely to be given responsibility for taking notes,
writing documentation,
and other low-status tasks.
Some have experienced this so often that they have come to accept it as
the price they have to pay for being in tech.
Others protest, but those who do are often dismissed as being "difficult".
Many take a third path and decide to leave programming—after all,
why play a game that's unfair?

<div class="callout" markdown="1">
**In the beginning**

Programming was originally considered a female occupation,
but as it became more lucrative it came to be viewed as "naturally" male.
[[Abbate2012][Abbate2012]] and [[Ensmenger2012][Ensmenger2012]] describe how this happened,
while [[Hicks2018][Hicks2018]] looks at how Britain lost its early dominance in computing
by systematically discriminating against its most qualified workers:
women.
Some men become quite uncomfortable whenever this is brought up,
but we need to learn how to discuss our own history
if we want to be able to think clearly about how the things we're doing today
might change society tomorrow.
</div>

There are many ways to divide project work between team members,
but no matter how you do it,
the software you get will reflect the division of labor
(a phenomenon known as [Conway's Law][conways-law]
or socio-technical congruence [[Cataldo2008][Cataldo2008]]).
In a *modular decomposition*,
each person is responsible for one part of the program.
For example,
one person might design and build the GUI
while another writes the database interface
and a third implements the business rules.
Having people own parts of the code like this produces lower failure rates in industry [[Bird2011][Bird2011]],
but is generally a bad strategy in a course project:

1.  It leads to *big bang integration*
    in which all the components meet each other for the first time
    right at the end of the project.
    Big bang almost always fails.

2.  Each team member only really understands one aspect of the project,
    which often proves fragile.
    (Imagine what happens if someone gets sick or drops the course…)

3.  It increases the risk of people from marginalized groups being assigned lower-status work,
    since self-appointed alpha geeks will usually snag jobs like architecture and coding,
    leaving less appealing work to people who aren't as pushy, privileged, or self-confident.
    This tends to reinforce existing inequities;
    it also tends to lower the team's overall grade,
    since there's often little relationship between how outspoken people are
    and how well they work.

With *functional decomposition*,
each person is responsible for one type of task,
i.e.,
one person does the testing,
another handles the documentation,
a third does the bulk of the coding,
and the fourth takes care of build and deployment.
This strategy has the same drawbacks as modular decomposition.

I therefore recommend that student teams use *feature decomposition*:
instead of owning an entire subsystem for the life of the project,
each team member handles the design, coding, testing, and documentation of one feature.
There isn't as much need for close collaboration between students
as there is with the previous two strategies,
but feature decomposition is more robust and more equitable.

Any of these strategies is better than *chaotic decomposition*,
which unfortunately is the most common approach.
If people have different ideas about who's supposed to do what,
some things won't be done at all while others will be done several times over.
(You can tell if your decomposition is chaotic by counting how often people say,
"I thought *you* were doing that!" or "But I've already done that!")
All other decompositions tend toward chaos under pressure,
so it's important to establish rules early
and stick to them when the going is easy
so that the instinct to do the right thing will be there
when mid-terms other deadlines strike.

<div class="callout" markdown="1">
**Clarity**

No matter how you allocate work, make sure that everyone understands who is doing what, when.
As [[Barke2019][Barke2019]] found,
actual roles can be fluid;
what matters most is that team members understand and accept their responsibilities
and everyone else's at any particular moment.
</div>

[Abbate2012]: https://isbnsearch.org/isbn/9780262534536
[Barke2019]: https://peerj.com/articles/cs-241/
[Bird2011]: https://dl.acm.org/doi/10.1145/2025113.2025119
[Cataldo2008]: https://dl.acm.org/doi/10.1145/1414004.1414008
[Ensmenger2012]: https://isbnsearch.org/isbn/9780262517966
[Hicks2018]: https://isbnsearch.org/isbn/9780262535182
[conways-law]: https://en.wikipedia.org/wiki/Conway's_law
[forming-teams]: @root/2025/01/07/forming-teams/
[quarterback-syndrome]: https://en.wikipedia.org/wiki/Racial_issues_faced_by_black_quarterbacks
[womens-work]: https://en.wikipedia.org/wiki/Women%27s_work
