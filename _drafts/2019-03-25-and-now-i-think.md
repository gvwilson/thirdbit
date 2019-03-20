---
layout: post
date: 2019-03-25 07:31
title: "And Now I Think"
---

Years ago, I stumbled across a book called
*[I Used to Think... And Now I Think...](https://www.amazon.com/Used-Think-Now-Leading-Educatiors/dp/1934742856/)*,
in which twenty leading educators looked back and reflected on their efforts to reform schooling.
Some of the writing was self-congratulatory,
but several of the contributors were quite blunt about how naive their younger selves had been.
In that spirit,
I'd like to try to summarize what I currently think about building lessons together
and delivering them effectively.
I expect---and hope---that my thinking will continue to evolve,
but I hope a snapshot will be useful.

## Lessons Are Not Like Software Packages

A good software package is a self-contained black box:
you can install it and use it
without knowing what it depends on or how it works.
Lessons aren't like that---not good ones, anyway.
The [Reusability Paradox](https://opencontent.org/blog/archives/3854) states that,
"The pedagogical effectiveness of a learning object and its potential for reuse are completely at odds with one another".
Good lessons help learners build a mental model that includes lots of long-range links
so that they can retrieve and apply what they've learned in lots of different contexts.
However,
the more long-range links a lesson has,
the harder it is to re-use.

I can only see three responses to this:

1.  Invest in highly contextualized resources that are pedagogically effective,
    knowing that they will be harder to re-use.
2.  Encourage sharing of fine-grained decontextualized resources that are highly reusable
    but don't connect with other lessons or with specific audiences.
    Exercise banks and graphics that illustrate specific points particularly well
    fall into this category;
    we can support re-use here by choosing open licenses
    and by making things findable (discussed below),
    but teachers will still have to assemble lessons themselves (also discussed below).
3.  The mediocre middle.
    In my experience,
    "skinning" lessons (e.g., swapping one data set for another but leaving most of the description the same)
    falls into this category.

## Lessons Are Not Like Stack Overflow

Mike Caulfield's notion of [choral explanations](https://hapgood.us/2016/05/13/choral-explanations/)
completely changed the way I think about lessons,
and for a while I thought that something like "Lesson Overflow" could solve the Reusability Paradox.
In my mind,
people would post motivating questions and curate explanations at differing levels of complexity;
a lesson would then be a guided tour through a series of questions and answers selected by an instructor.

I still think a "guided tour" would be an interesting pedagogical experiment,
but I now believe there would either be a lack of continuity (case #2 above)
or that creators would have to post a coordinated sequence of questions,
which would be just as much work as writing a conventional lesson (case #1).
For example,
if the answer to the question, "How do I change the limits to the X and Y axes in a plot?"
used economic time series data as an illustration,
but the answer to the next question, "How do I change the markers used in a scatterplot?"
used medical data,
novices would be distracted by the superficial differences
because they wouldn't yet have a mental model that included and supported generalization.

## Findability Beats Aggregation

David Wiley and others have said that
nobody should ever build another lesson repository
because thirty years of experience show that they don't work.
Instead, people should focus on making lessons findable.
Doing that well requires a bit of training in SEO,
particularly in how to tag pieces of existing lessons rather than lessons as a whole.
I don't know yet how helpful tools like [hypothes.is](http://hypothes.is) will be
for improving findability post facto,
but I think it would be another worthwhile experiment.

## Both Styles Work

After co-teaching a class with me this week,
a colleague said, "You're playing jazz and I'm playing classical music."
They're right:
I improvise a lot around any teaching outline or slide deck I start with,
where many other people stick more closely to the plan.
For years,
I've been pushing people to adopt my style by emphasizing the benefits of live coding
and telling them that there's no point reading a script
because then you're "just" competing with video (for some value of "just").

I now believe that I've been wrong.
I don't know of any literature on the interaction between a teacher's personality
and what style of instruction they can deliver most effectively,
but I'd be surprised if there wasn't one.
Some people are organized and some are messy;
some prefer predictability and others like surprises,
and I think that people are more likely to do well if they're doing things they're comfortable with.

That said,
the idea that people have different learning styles (visual, auditory, or kinesthetic)
[turned out to be wrong](https://www.theatlantic.com/science/archive/2018/04/the-myth-of-learning-styles/557687/),
so it could well be that people prefer to teach in different ways
but it makes no difference to outcomes.
Still,
if saying that this is OK helps teachers' motivation,
it's worth doing.

## Hybrid Vigor

My experiences with MOOCs left a bad taste in my mouth,
but I now believe that my distaste led me to overlook ways in which the web ought to be used for teaching.
Like most people,
I long assumed that each person learning on the web would do it on their own time,
and that collaboration would therefore primarily happen through asynchronous media like bulletin boards
or semi-synchronous media like chat rooms.
That's how a lot of distributed companies work,
and it's very different from the classroom-and-lecture model of education that I grew up with,
where everyone is receiving the lesson at the same time
and able to interact conversationally with their peers.

But while it's easy to compare and contrast extremes,
there's no guarantee that they are optimal.
I now believe that a hybrid of the two models described above
is more effective at scale than either on its own:

1.  A single instructor teaches a live in-person audience of a dozen to twenty people
    so that the instructor gets the immediate-presence feedback
    (eye contact, puzzled expressions, etc.)
    needed to make this more than a live MOOC.

2.  The instructor is supported at her location by two people:
    a TA who helps on-site learners with technical problems
    and an A/V technician responsible for broadcasting audio and video in real time.
    (With a bit of practice and setup I believe the A/V technician can be dispensed with.)

3.  Remote learners congregate in 2-4 rooms,
    each of which also holds a dozen to twenty people.
    The stream from the instructor’s site is projected in real time
    so that remote learners can see and hear the instructor.
    Crucially, they can also interact with each other (e.g., by working in pairs)
    and with a local TA.
    The peer interaction helps motivation and engagement,
    while the local TA gets them unstuck whenever they have issues
    (and again, makes this more than a live MOOC).

4.  The remote-site TAs are responsible for managing their A/V
    (which in practice means connecting a projector and speakers to a spare laptop and dialing into a web conferencing session).
    They are also responsible for fielding questions asked by learners in their rooms.
    If they don’t know the answer,
    or if they think the question is sufficiently interesting,
    they either relay it to the instructor (e.g., via text chat)
    or pass a microphone to the learner so that she can ask it directly.

This model requires learners to learn together,
but that's pedagogically more effective than having them learn on their own.
I would *really* like to try this model with a bit of clicker-style support
for [peer instruction](https://en.wikipedia.org/wiki/Peer_instruction)
to see whether the latter's benefits scale across sites.

## Help Teachers First

Finally,
I now believe that the best way to help the majority of students is not to create more self-study materials,
because that's subject to the [Matthew Effect](https://en.wikipedia.org/wiki/Matthew_effect)
(the rich get richer and the poor get poorer).
Instead,
the best way is to support teachers who are already helping those groups.
Quoting [Mike Caulfield](https://hapgood.us/2018/12/02/empower-teachers-first/),
it's like the advice they give you on planes:
in event of sudden decompression,
put on your own mask first,
then help the person beside you.
Showing instructors how to create better lessons and deliver them more effectively is a first step.
Teaching them how to make those lessons more findable is the next,
and if the hybrid teaching model described above turns out to be an improvement over alternatives,

## Final Thoughts

I'd like to close with a quote from
*[The Big Picture: Education is Everyone's Business](http://www.amazon.com/The-Big-Picture-Education-Everyones/dp/0871209713/)*:

> If poor inner-city children consistently outscored children from wealthy suburban homes on standardized tests,
> is anyone naive enough to believe that we would still insist on using these tests as indicators of success?
>
> -- Kenneth Wesson

I have focused on the neuroscience of learning for most of the past ten years
because it's the easiest part of education to discuss.
Who gets taught and who decides what they're taught are bigger and harder questions,
and I think their answers will change my thinking about everything else in this post.
As Pablo Casals said, "I think I am still making progress."
