---
layout: teaching
permalink: /teaching/motivation.html
title: "How to Teach Programming (and Other Things): Motivation and Demotivation"
---

# Motivation and Demotivation

**Objectives**

* **Learners can name and describe the three principal ways in which
  they can demotivate their own learners.**
* **Learners can define impostor syndrome and stereotype threat, and
  describe ways in which to combat each.**
* **Learners can describe the difference between fixed and growth
  mindset and explain the importance of encouraging the latter.**
* **Learners can describe and enact at least three things they can
  do to make their programming workshops more accessible.**
* **Learners can describe and enact at least three things they can
  do to make their programming workshops more inclusive.**

Learners need encouragement to step out into unfamiliar terrain, so
this chapter discusses ways instructors can motivate them.  More
importantly, it discusses ways that we can accidentally *demotivate*
them, and how we can avoid doing that.

People learn best when they care about the topic and believe they can
master it. This presents us with a problem because most people don't
actually want to program: they want to make music or compare changes
to zoning laws with family incomes, and rightly regard programming as
a tax they have to pay in order to do so. In addition, their early
experiences with programming are often demoralizing, and believing
that something will be hard to learn is a self-fulfilling prophecy.

Imagine a grid whose axes are labelled "mean time to master" and
"usefulness once mastered". Everything that's quick to master, and
immediately useful should be taught first; things in the opposite corner
that are hard to learn and have little near-term application don't
belong in this course.

> **Actual Time**
> 
> Any useful estimate of how long something takes to master must take
> into account how frequent failures are and how much time is lost to
> them. For example, editing a text file seems like a simple task, but
> most graphical editors save things to the user's desktop or home
> directory.  If people need to run shell commands on the files they've
> edited, a substantial fraction won't be able to navigate to the right
> directory without help. If this seems like a small problem to you,
> please revisit the discussion of expert blind spot in
> [Memory](memory.html).

Many of the foundational concepts of computer science, such as
computability, inhabit the "useful but hard to learn" corner of the
grid described above. This doesn't mean that they aren't worth
learning, but if our aim is to convince people that they *can*
learn this stuff, and that doing so will help them do more science
faster, they are less compelling than things like automating
repetitive tasks.

We therefore recommend a "teach most immediately useful first"
approach.  Have learners do something that *they* think is useful
in their daily work within a few minutes of starting each lesson.
This not only motivates them, it also helps build their confidence in
us, so that if it takes longer to get to the payoff of a later topic,
they'll stick with us.

The best-studied use of this idea is the media computation approach
developed by Guzdial and Ericson at Georgia Tech
[[Guzdial2013](biblio.html#guzdial-mediacomp-retrospective)].  Instead of
printing "hello world" or summing the first ten integers, their
students' first program opens an image, resizes it to create a
thumbnail, and saves the result. This is an _[authentic
task](gloss.html#authentic-task)_, i.e., something that learners
believe they would actually do in real life. It is also has a
_[tangible artifact](gloss.html#tangible-artifact)_: if the image
comes out the wrong size, learners have a concrete starting point for
debugging.

> **Strategies for Motivating Learners**
> 
> [[Ambrose2010](biblio.html#ambrose-hlw)] contains a list of
> evidence-based methods to motivate learners.  None of them are
> surprising–it's hard to imagine someone saying that we *shouldn't*
> identify and reward what we value–but it's useful to check lessons
> against these points to make sure they're doing at least a few of
> these things.
> 
> What's missing from this list is strategies to motivate the
> *instructor*. Learners respond to an instructor's enthusiasm, and
> instructors need to care about a topic in order to keep teaching it,
> particularly when they are volunteers.

## Demotivation

> *Women aren't leaving computing because they don't know what it's
> like; they're leaving because they **do** know.*  
> – variously attributed

If you are teaching free-range learners, they are probably already
motivated–if they weren't, they wouldn't be in your classroom. The
challenge is therefore not to demotivate them.  Unfortunately, we can
do this by accident much more easily than you might think.

The three most powerful demotivators are *unpredictability*,
*indifference*, and *unfairness*.  Unpredictability demotivates people
because if there's no reliable connection between what they do and
what outcome they achieve, there's no reason for them to try to do
anything.  If learners believe that the instructor or the educational
system doesn't care about them or the lesson, they won't care
either. And if people believe the class is unfair, they will also be
demotivated, even if it is unfair in their favor (because consciously
or unconsciously they will worry that they will some day find
themselves in the group on the losing end
[[Wilkinson2011](biblio.html#wilkinson-pickett-spirit-level)]).  In
extreme situations, learners may develop [learned
helplessness](gloss.html#learned-helplessness): when repeatedly
subjected to negative feedback that they have no way to escape, they
may learn not to even try to escape when they could.

Here are some quick ways to demotivate your learners:

*   A "holier-than-thou" or contemptuous attitude from an instructor.

*   Tell learners they are rubbish because they use Excel and/or Word,
    don't modularize their code, etc.

*   Repeatedly make digs about Windows and praise Linux, e.g., say that
    the former is for amateurs.

*   Criticize GUI applications (and by implication their users) and
    describe command-line tools as the One True Way.

*   Dive into complex or detailed technical discussion with the one or
    two people in the audience who clearly don't actually need to be
    there.

*   Pretend to know more than you do. People will actually trust you
    more if you are frank about the limitations of your knowledge, and
    will be more likely to ask questions and seek help.

*   Use the J word ("just"). As discussed in [Memory](memory.html), this
    signals to the learner that the instructor thinks their problem is
    trivial and by extension that they therefore must be stupid for not
    being able to figure it out.

*   Feign surprise. Saying things like "I can't believe you don't know
    X" or "you've never heard of Y?" signals to the learner that they
    do not have some required pre-knowledge of the material you are
    teaching, that they are in the wrong place, and it may prevent them
    from asking questions in the future.

> **Code of Conduct Revisited**
> 
> As noted [at the start](index.html), we believe very strongly that
> classes should have a [Code of Conduct](conduct.html). Its details
> are important, but the most important thing about it is that it
> exists: knowing that we have rules tells people a great deal about
> our values and about what kind of learning experience they can
> expect.

<!-- comment needed to separate blockquotes -->

> **Never Learn Alone**
> 
> One way to support learners who have been subject to systematic
> exclusion or discrimination (overt or otherwise) is to have people
> sign up for workshops in small teams rather than as individuals. If
> an entire lab group comes, or if attendees are drawn from the same
> (or closely-related) disciplines, everyone in the room will know in
> advance that they will be with at least a few people they trust,
> which increases the chances of them actually coming. It also helps
> after the workshop: if people come with their friends or colleagues,
> they can work together to implement what they've learned.

## Impostor Syndrome

_[Impostor syndrome](gloss.html#impostor-syndrome)_ is the belief
that one is not good enough for a job or position, that one's
achievements are lucky flukes, and an accompanying fear of being
"found out". Impostor syndrome seems to be particularly common among
[high achievers who undertake publicly visible work][usenix-impostor].

Academic work is frequently undertaken alone or in small groups but
the results are shared and criticized publicly. In addition, we rarely
see the struggles of others, only their finished work, which can feed
the belief that everyone else finds it easy. Women and minority
groups who already feel additional pressure to prove themselves in
some settings may be particularly affected.

Two ways of dealing with your own impostor syndrome are:

1.  Ask for feedback from someone you respect and trust. Ask them for
    their honest thoughts on your strengths and achievements, and commit
    to believing them.

1.  Look for role models. Who do you know who presents as confident and
    capable? Think about how they conduct themselves. What lessons can
    you learn from them? What habits can you borrow? (Remember, they
    quite possibly also feel as if they are making it up as they go.)

As an instructor, you can help people with their impostor syndrome by
sharing stories of mistakes that you have made or things you struggled
to learn. This reassures the class that it's OK to find topics hard.
Being open with the group makes it easier to build trust and make
students confident to ask questions. (Live coding is great for this:
typos let the class see you're not superhuman.)

You can also emphasize that you want questions: you are not succeeding
as a teacher if no one can follow your class, so you're asking
students for their help to help you learn and improve. Remember, it's
much more important to *be* smart than to *look* smart.

The Ada Initiative has some excellent resources for teaching about and
dealing with imposter syndrome [[Ada2017](biblio.html#ada-imposter)].

## Stereotype Threat

Reminding people of negative stereotypes, even in subtle ways, makes
them anxious about the risk of confirming those stereotypes, which in
turn reduces their performance. This is called _[stereotype
threat](gloss.html#stereotype-threat)_, and the clearest examples in
computing are gender-related.  Depending on whose numbers you trust,
only 12-18% of programmers are women, and those figures have actually
been getting worse over the last 20 years. There are many reasons for
this (see [[Margolis2003](biblio.html#margolis-fisher-clubhouse)] and
[[Margolis2010](biblio.html#margolis-shallow)]), and
[[Steele2011](biblio.html#steele-vivaldi)] summarizes what we know about
stereotype threat in general and presents some strategies for
mitigating it in the classroom.

However, while there's lots of evidence that unwelcoming climates
demotivate members of under-represented groups, it's not clear that
stereotype threat is the underlying mechanism. Part of the problem is
that [the term has been used in many
ways][stereotype-threat-ambiguity]; another is [questions about the
replicability of key studies][stereotype-threat-replicability]. What
*is* clear is that we need to avoid thinking in terms of a deficit
model (i.e., we need to change the members of under-represented groups
because they have some deficit, such as lack of prior experience) and
instead use a systems approach (i.e., we need to change the system
because it produces these disparities).

A great example of how stereotypes work in general was presented in
Patitsas et al's "Evidence That Computer Science Grades Are Not
Bimodal" [[Patitsas2016](biblio.html#patitsas-cs-grades)].  This
thought-provoking paper showed that people see evidence for a "geek
gene" where none exists.  As the paper's abstract says:

> Although it has never been rigorously demonstrated, there is a
> common belief that CS grades are bimodal. We statistically analyzed
> 778 distributions of final course grades from a large research
> university, and found only 5.8% of the distributions passed tests
> of multimodality. We then devised a psychology experiment to
> understand why CS educators believe their grades to be bimodal. We
> showed 53 CS professors a series of histograms displaying ambiguous
> distributions and asked them to categorize the distributions. A
> random half of participants were primed to think about the fact that
> CS grades are commonly thought to be bimodal; these participants
> were more likely to label ambiguous distributions as "bimodal".
> Participants were also more likely to label distributions as bimodal
> if they believed that some students are innately predisposed to do
> better at CS. These results suggest that bimodal grades are
> instructional folklore in CS, caused by confirmation bias and
> instructor beliefs about their students.

It's easy to use language that suggests that some people are natural
programmers and others aren't, but Mark Guzdial has called this belief
[the biggest myth about teaching computer science](guzdial-myth).

## Mindset

Learners can be demotivated in subtler ways as well. For example,
Dweck and others have studied the differences of [fixed
mindset](gloss.html#fixed-mindset) and [growth
mindset](gloss.html#growth-mindset). If people believe that
competence in some area is intrinsic (i.e., that you either "have the
gene" for it or you don't), *everyone* does worse, including the
supposedly advantaged.  The reason is that if they don't get it at
first, they figure they just don't have that aptitude, which biases
future performance. On the other hand, if people believe that a skill
is learned and can be improved, they do better on average.

A person's mindset can be shaped by subtle cues. For example, if a
child is told, "You did a good job, you must be very smart," they are
likely to develop a fixed mindset. If on the other hand they are told,
"You did a good job, you must have worked very hard," they are likely
to develop a growth mindset, and subsequently achieve more. Studies
have also shown that the simple action of telling learners about the
different mindsets before a course can improve learning outcomes for
the whole group.

As with stereotype threat, [there are
concerns][growth-mindset-concerns] that research on grown mindset has
been oversold, or will be much more difficult to put into practice
than its more enthusiastic advocates have implied.  While some people
interpret this back and forth of claim and counter-claim as evidence
than education research isn't reliable, what it really shows is that
anything involving human subjects is both subtle and difficult.

## Accessibility

Not providing equal access to lessons and exercises is about as
demotivating as it gets. The older Software Carpentry lessons, for
example, the text beside the slides includes all of the narration–but
none of the Python source code.  Someone using a [screen
reader][wikipedia-screen-reader] would therefore be able to hear what
was being said about the program, but wouldn't know what the program
actually was.

While it may not be possible to accommodate everyone's needs, it
*is* possible to get a good working structure in place without any
specific knowledge of what specific disabilities people might have.
Having at least some accommodations prepared in advance also makes it
clear that hosts and instructors care enough to have thought about
problems in advance, and that any additional concerns are likely to be
addressed.

> **It Helps Everyone**
> 
> [Curb cuts][wikipedia-curb-cuts] (the small sloped ramps joining a
> sidewalk to the street) were originally created to make it easier
> for the physically disabled to move around, but proved to be equally
> helpful to people with strollers and grocery carts.  Similarly,
> steps taken to make lessons more accessible to people with various
> disabilities also help everyone else. Proper captioning of images,
> for example, doesn't just give screen readers something to say: it
> also makes the images more findable by exposing their content to
> search engines.

The first and most important step in making lessons accessible is to
*involve people with disabilities in decision-making*: the slogan
*[nihil de nobis, sine nobis][wikipedia-nihil]* (literally, "nothing
about us, without us") predates accessibility rights, but is always
the right place to start.  A few other recommendations are:

*   *Find out what you need to do.* The W3C Accessibility Initiative's
    checklist for presentations
    [[W3C2017](biblio.html#w3c-accessibility)] is a good starting point
    focused primarily on assisting the visually impaired, while Liz
    Henry's blog post about accessibility at conferences
    [[Henry2014](biblio.html#henry-accessibility)] has a good checklist
    for people with mobility issues, and this interview with Chad
    Taylor is a good introduction to issues faced by the hearing
    impaired [[Taylor2014](biblio.html#taylor-interview)].

*   *Know how well you're doing.* For example, sites like
    [WebAIM][webaim] allow you to check how accessible your online
    materials are to visually impaired users.

*   *Don't do everything at once.* We don't ask learners in our
    workshops to adopt all our best practices or tools in one go, but
    instead to work things in gradually at whatever rate they can
    manage.  Similarly, try to build in accessibility habits when
    preparing for workshops by adding something new each time.

*   *Do the easy things first.* There are plenty of ways to make
    workshops more accessible that are both easy and don't create extra
    cognitive load for anyone: font choices, general text size, checking
    in advance that your room is accessible via an elevator or ramp,
    etc.

## Inclusivity

_[Inclusivity](gloss.html#inclusivity)_ is a policy of including
people who might otherwise be excluded or marginalized. In computing,
it means making a positive effort to be more welcoming to women,
people of color, people with various sexual orientations, the elderly,
the physically challenged, the formerly incarcerated, the economically
disadvantaged, and everyone else who doesn't fit Silicon Valley's
white/Asian male demographic. Lee's paper "What can I do today to
create a more inclusive community in CS?"
[[Lee2017](biblio.html#lee-create-inclusive-community)] is a brief,
practical guide to doing that with references to the research
literature. These help learners who belong to one or more marginalized
or excluded groups, but help motivate everyone else as well; while
they are phrased in terms of term-long courses, many can be applied in
our workshops:

*   Ask learners to email you before the workshop to explain how they
    believe the training could help them achieve their goals.

*   Review notes to make sure they are free from gendered pronouns, that
    they include culturally diverse names, etc.

*   Emphasize that what matters is the rate at which they are learning,
    not the advantages or disadvantages they had when they started.

*   Encourage pair programming.

*   Actively mitigate behavior that some learners may find intimidating,
    e.g., use of jargon or "questions" that are actually asked to
    display knowledge.

## Challenges

### Authentic Tasks (15 minutes)

Think about something you did this week that uses one or more of the
skills you teach, (e.g., wrote a function, bulk downloaded data, did
some stats in R, forked a repo) and explain how you would use it (or a
simplified version of it) as an exercise or example in class.

Pair up with your neighbor and decide where this exercise fits on a
2x2 grid of "short/long time to master" and "low/high usefulness"?  In
the shared notes, write the task and where it fits on the grid. As a
group, discuss how these relate back to the "teach most immediately
useful first" approach.

### Implement One Strategy for Inclusivity (5 minutes)

Pick one activity or change in practice from Lee's paper
[[Lee2017](biblio.html#lee-create-inclusive-community)] that you would
like to work on.  Put a reminder in your calendar three months in the
future to self-check whether you have done something about it.

### Brainstorming Motivational Strategies (20 minutes)

1.  Think back to a programming course (or any other) that you took in
    the past, and identify one thing the instructor did that demotivated
    you, and describe what could have been done afterward to correct
    the situation.

2.  Pair up with your neighbor and discuss your stories, then add
    your comments to the shared notes.

3.  Review the comments in the shared notes as a group. Rather than
    read them all out loud, highlight and discuss a few of the things
    that could have been done differently. This will give everyone
    some confidence in how to handle these situations in the future.

### Demotivational Experiences (15 minutes)

Think back to a time when you demotivated a student (or when you were
demotivated as a student). Pair up with your neighbor and discuss what
you could have done differently in the situation, and then share the
story and what could have been done in the group notes.

### Walk the Route (15 minutes)

Find the nearest public transportation drop-off point to your building
and walk from there to your office and then to the nearest washroom,
making notes about things you think would be difficult for someone with
mobility issues. Now borrow a wheelchair and repeat the journey. How
complete was your list of challenges? And did you notice that the first
sentence in this challenge assumed you could actually walk?

### Who Decides? (15 minutes)

In [[Littky2004](biblio.html#littky-big-picture)], Kenneth Wesson wrote,
"If poor inner-city children consistently outscored children from
wealthy suburban homes on standardized tests, is anyone naive enough
to believe that we would still insist on using these tests as
indicators of success?" Read
[[Cottrill2016](biblio.html#cottrill-gifted)], and then describe an
example from your own experience of "objective" assessments that
reinforced the status quo.

[ada-resources]: http://adainitiative.org/continue-our-work/impostor-syndrome-training/
[growth-mindset-concerns]: http://www.learningspy.co.uk/psychology/growth-mindset-bollocks/
[guzdial-myth]: http://cacm.acm.org/blogs/blog-cacm/189498-top-10-myths-about-teaching-computer-science/fulltext
[stereotype-threat-ambiguity]: http://www.europhd.net/html/_onda02/07/PDF/20th_lab_materials/jane/shapiro_neuberg_2007.pdf
[stereotype-threat-replicability]: https://www.psychologytoday.com/blog/rabble-rouser/201512/is-stereotype-threat-overcooked-overstated-and-oversold
[swc-old-lessons]: http://swcarpentry.github.io/v4/python/flow.html
[usenix-impostor]: https://www.usenix.org/blog/impostor-syndrome-proof-yourself-and-your-community
[webaim]: http://webaim.org/
[wikipedia-curb-cuts]: https://en.wikipedia.org/wiki/Curb_cut
[wikipedia-learned-helplessness]: https://en.wikipedia.org/wiki/Learned_helplessness
[wikipedia-nihil]: https://en.wikipedia.org/wiki/Nothing_About_Us_Without_Us
[wikipedia-screen-reader]: https://en.wikipedia.org/wiki/Screen_reader
