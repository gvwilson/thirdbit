---
layout: teaching
permalink: /teaching/memory.html
title: "How to Teach Programming (and Other Things): Expertise and Memory"
---

# Expertise and Memory
<!--: \label{memory} :-->

> **Objectives**
>
> * Learners can define expertise and explain its operation using
>   a graph metaphor for cognition.
> * Learners can explain the difference between repetition and
>   deliberate practice.
> * Learners can define and construct concept maps, and explain
>   the benefits of externalizing cognition.
> * Learners can differentiate long-term and short-term  memory,
>   describe the capacity limits of the latter, and explain the
>   the impact of these limits on teaching.

The previous chapter looked at what distinguishes novices from
competent practitioners.  Here, we will look at expertise: what it is,
how people acquire it, and how it can be harmful as well as helpful.
We will then see how concept maps can be used to figure out how to
turn knowledge into lessons.

To start, what do we mean when we say someone is an expert?  The usual
response is that they can solve problems much faster than people who
are "merely competent", or that they can recognize and deal with the
cases where the normal rules don't apply.  They also somehow make this
look effortless: in most cases, they just know what the right answer
is.

What makes someone an expert? The answer isn't just that they know
more facts: competent practitioners can memorize a lot of trivia
without any noticeable improvement to their performance.  Instead,
imagine for a moment that we store knowledge as a graph in which facts
are nodes and relationships are arcs. (This is emphatically *not* how
our brains work, but it's a useful metaphor.) The key difference
between experts and people who are "merely competent" is that experts
have many more connections, i.e., their mental models are much more
densely connected.

This metaphor helps explain many observed aspects of expert behavior:

*   Experts can jump directly from a problem to its solution because
    there actually is a direct link between the two in their mind.
    Where a competent practitioner would have to reason "A, B, C, D,
    E", the expert can go from A to E in a single step. We call
    this *intuition*, and it isn't always a good thing: when asked
    to explain their reasoning, experts often can't, because they didn't
    actually reason their way to the solution–they just recognized it.

*   Experts are frequently so familiar with their subject that they can
    no longer imagine what it's like to *not* see the world that
    way. As a result, they are often less good at teaching the subject
    than people with less expertise who still remember what it's like
    to have to learn the things. This phenomenon is called _[expert
    blind spot](gloss.html#expert-blind-spot)_, and
    while it can be overcome with training, it's part of why there is
    no correlation between how good someone is at doing research in an
    area and how good they are at teaching it
    [[Marsh2002](biblio.html#marsh-hattie-teaching)].

*   Densely-connected knowledge graphs are also the basis for experts'
    _[fluid representations](gloss.html#fluid-representation)_, i.e.,
    their ability to switch back and forth between different views of
    a problem [[Petre2016](biblio.html#petre-expertise)].  For example,
    when trying to solve a problem in mathematics, we might switch
    between tackling it geometrically and representing it as a set of
    equations to be solved.

*   Finally, this metaphor also explains why experts are better at
    diagnosis than competent practitioners: more linkages between facts
    makes it easier to reason backward from symptoms to causes. (And
    this in turn is why asking programmers to debug during job
    interviews gives a more accurate impression of their ability than
    asking them to program.)

> **The J Word**
>
> Experts often betray their blind spot by using the word "just" in
> explanations, as in, "Oh, it's easy, you just fire up a new virtual
> machine and then you just install these four patches to Ubuntu and
> then you just re-write your entire program in a pure functional
> language." As we discuss later in [Motivation](motivation.html), the J word
> (also sometimes called the passive dismissive adjective) should be
> banned from classrooms, primarily because using it gives learners the
> very clear signal that the instructor thinks their problem is trivial
> and that they therefore must be stupid.

The graph model of knowledge explains why helping learners make
connections is as important as introducing them to facts.  To use
another analogy, the more people you know in a group, the more likely
you are to remain part of that group.  Similarly, the more connections
a fact has to other facts, the more likely the fact is to be
remembered.

## Repetition vs. Deliberate Practice

The idea that ten thousand hours of practice will make someone an
expert in some field is widely quoted, but reality is more complex.
Doing exactly the same thing over and over again is much more likely
to solidify bad habits than perfect performance.  What actually works
is _[deliberate practice](gloss.html#deliberate-practice)_ (also
sometimes called _[reflective
practice](gloss.html#reflective-practice)_), which is doing similar but
subtly different things, paying attention to what works and what
doesn't, and then changing behavior in response to that feedback to
get cumulatively better.

A common progression is for people to go through three stages:

1.  They *learn how to do something given feedback from others*.
    For example, they might write an essay about what they did on their
    summer holiday, and get feedback from a teacher telling them how to
    improve it.

2.  They *learn how to give feedback*.  For example, they might
    write an essay about character development in *The Catcher in
    the Rye*, and get feedback on their critique from a teacher.

3.  They *apply what they've learned about feedback to themselves*.
    At some point, they start critiquing their own work in real time
    (or nearly so) using the critical skills they have now built up.
    Doing this is so much faster than waiting for feedback from others
    that proficiency suddenly starts to take off.

A meta-study conducted in 2014
[[Macnamara2014](biblio.html#macnamara-deliberate)] found that
"…deliberate practice explained 26% of the variance in performance for
games, 21% for music, 18% for sports, 4% for education, and less than
1% for professions." One explanation for this variation is that
deliberate practice works best when the rules for evaluating success
are very stable, but is less effective when there are more factors at
play (i.e., when it's harder to connect cause to effect).

## Concept Maps

Our tool of choice to represent a knowledge graph (expert or
otherwise) is a _[concept map](gloss.html#concept-map)_.  A concept map
is simply a picture of someone's mental model of a domain: facts are
bubbles, and connections are labelled arcs. It is important that they
are labelled: saying "X and Y are related" is only helpful if we
explain what the relationship *is*. (And yes, one person's fact may be
another person's connection, but one of the benefits of concept
mapping is that it makes those differences explicit.)  The figure
below reproduces a concept map taken from the [IHMC CMap site][ihmc-cmap]
showing why the Earth has seasons.

![Concept Map for Seasons](fig/seasons.png)

<!-- http://cmap.ihmc.us/docs/images/Theory/Fig5CmapSeasons-large.png -->

<!--: \newpage :-->

To show what concept maps look like, consider this simple `for`
loop in Python:

~~~
for letter in "abc":
      print('*' + letter)
~~~

<!--: \noindent :-->
whose output is:

~~~
*a
*b
*c
~~~

<!--: \noindent :-->
The three key "things" in this loop are shown in the first part
of this concept map:

![Concept Map](fig/for-loop-concepts.png)

This is only half the story, though, and arguably the less important
half.  An expanded concept map shows the *relationships* between those
things, which are as important as the concepts themselves.

<!--: \newpage :-->

Concept maps can be used in many ways:

1.  Concept maps aid design of a lesson by helping authors figure out
    what they're trying to teach. Crucially, a concept map separates
    content from order: in our experience, people rarely wind up
    teaching things in the order in which they first drew them.

2.  They also aid communication between lesson designers. Instructors
    with very different ideas of what they're trying to teach are likely
    to pull their learners in different directions. Drawing and sharing
    concept maps isn't guaranteed to prevent this, but it certainly
    helps.

3.  Concept maps also aid communication with learners. While it's
    possible to give learners a pre-drawn map at the start of a lesson
    for them to annotate, it's better to draw it piece by piece while
    teaching to reinforce the ties between what's in the map and what
    the instructor said. (We will return to this idea when we discuss
    Mayer's work on multimedia learning in [Cognitive Load](load.html)).

4.  Concept maps are also a useful for assessment: having learners
    draw concept maps of what they think they just heard shows the
    instructor what was missed and what was mis-understood.  However,
    reviewing learners' concept maps is too time-consuming for use in
    class, but very useful in weekly lectures *once learners are
    familiar with the technique*.  The qualification is necessary
    because any new way of doing things initially slows people down–if
    a student is trying to make sense of basic programming, asking
    them to figure out how to draw their thoughts at the same time is
    an unfair load.  Finally, some instructors are skeptical of
    whether novices can effectively map their understanding, since
    introspection and explanation of understanding are generally more
    advanced skills than understanding itself.

> **Externalizing Cognition**
> 
> Concept maps are just one way to represent our understanding of a
> subject.  For example, Andrew Abela's decision tree
> [[Abela2009](biblio.html#abela-chart)] presents a mental model of how
> to choose the right kind of chart for different kinds of questions
> and data.  Maps, flowcharts, and blueprints can also be useful in
> some contexts.  What each does is _[externalize
> cognition](gloss.html#externalized-cognition)_, i.e., make thought
> processes and mental models visible so that they can be compared,
> contrasted, and combined.

<!-- comment needed to separate blockquotes -->

> **Meetings, Meetings, Meetings**
> 
> The next time you have a team meeting, give everyone a sheet of paper
> and have them spend a few minutes drawing a concept map of the project
> you're all working on–separately. On the count of three, have
> everyone reveal their concept maps simultaneously. The discussion that
> follows everyone's realization of how different their mental models of
> the project's aims and organization are is always interesting…

## Seven Plus or Minus Two

The graph model of knowledge is wrong but useful, but another simple
model has a sound physical basis.  As a rough approximation, human
memory can be divided into two distinct layers. The first is called
_[long-term](gloss.html#long-term-memory)_ or _[persistent
memory](gloss.html#persistent-memory)_. It is where we store things
like our password, our home address, and what the clown did at our
eighth birthday party that scared us so much. It is essentially
unbounded: barring injury or disease, we will die before it fills up.
However, it is also slow to access–too slow to help us handle hungry
lions and disgruntled family members.

Evolution has therefore given us a second system called
_[short-term](gloss.html#short-term-memory)_ or _[working
memory](gloss.html#working-memory)_. It is much faster, but also much
smaller: in 1956, Miller estimated that the average adult's working
memory could hold 7±2 items for a few seconds before things started to
drop out.  This is [why phone numbers are typically 7 or 8 digits
long][bell-phone]: back when phones had dials instead of keypads, that
was the longest string of numbers most adults could remember
accurately for as long as it took the dial to go around and
around. It's also why sports teams tend to have about half a dozen
members, or be broken down into smaller groups (such as the forwards
and backs in rugby).

> **Chunking**
> 
> Our minds can store larger numbers of facts in short-term memory by
> creating _[chunks](gloss.html#chunking)_. For example, most of us
> will remember a word we read as a single item, rather than as a
> sequence of letters.  Similarly, the pattern made by five spots on
> cards or dice is remembered as a whole rather than as five separate
> pieces of information.
>
> Chunks allow us to manage larger problems, but can also mislead us
> if we mis-identify something, i.e., see it as something it isn't.
> We will discuss this in more detail
> [later](load.html#pattern-recognition).  Recent estimates have
> suggested that the size of short-term memory might be as low as 4±1
> [[Didau2016](biblio.html#didau-teachers-psych)] which means that
> effective chunking (discussed below) is even more important than
> first thought.

7±2 is probably the most important number in programming. When
someone is trying to write the next line of a program, or understand
what's already there, she needs to keep a bunch of arbitrary facts
straight in her head: what does this variable represent, what value
does it currently hold, etc. If the number of facts grows too large,
her mental model of the program comes crashing down (something we have
all experienced).

7±2 is also the most important number in teaching. An instructor
cannot push information directly into a learner's long-term
memory. Instead, whatever she presents is first represented in the
learner's short-term memory, and is only transferred to long-term
memory after it has been held there and rehearsed. If we present too
much information too quickly, the new will displace the old before it
has a chance to consolidate in long-term memory.

This is one of the reasons to create a concept map for a lesson before
teaching it: an instructor needs to identify how many pieces of
separate information will need to be "stored" in memory as part of the
lesson.  In practice, it's common to draw a concept map, realize that
there's far too much in it to teach in a single pass, and then carve
out tightly-connected sub-sections to divide the overall lesson into
teachable episodes.

> **Building Concept Maps Together**
> 
> Concept maps can be used as a classroom discussion exercise. Put
> learners in small groups (2-4 people each), give each group some sticky
> notes on which a few key concepts are written, and have them build a
> concept map on a whiteboard by placing those sticky notes, connecting
> them with labelled arcs, and adding any other concepts they think they
> need.

## Six Strategies

The [Learning Scientists][learning-scientists] have catalogued six
strategies for effective learning, which are summarized in [these
downloadable posters][six-strategies]:

1.  *Spaced practice*: creating a study schedule that spreads study
    activities over time.
    <br/>
    Block off 30 minutes to study each day rather than trying to cram
    everything in the night before an exam.

2.  *Retrieval practice*: bringing learned information to mind
    from long-term  memory.
    <br/>
    Take practice tests, or practice summarizing the details of a
    topic from memory.

3.  *Interleaving*: creating a study schedule that mixes different
    kinds of problems, or different content subjects within one study
    session.
    <br/>
    Solve practice problems A-B-C-A-B-C-A-B-C rather than
    A-A-A-B-B-B-C-C-C.

4.  *Elaboration*: asking and explaining why things work.
    <br/>
    Follow up each practice answer with an explanation of why that
    answer is correct.

5.  *Concrete examples*: illustrating abstract concepts with specific
    real-life examples.
    <br/>
    Follow each statement of a general principle with one or more
    examples, or each particular problem with a statement of the
    general principles it embodies.

6.  *Dual coding*: combining words with visuals.
    <br/>
    Draw or label diagrams while explaining things or working through
    problems.

Teaching these strategies to students, and mentioning them by name
when you use them in class, can help them learn how to learn faster
and better.

## Challenges

### Concept Mapping (30 minutes)

Create a hand drawn concept map for something you would teach in five
minutes.  (If possible, do it for the same subject that created a
multiple choice question for earlier.) Trade with a partner, and
critique each other's maps. Do they present concepts or surface
detail? Which of the relationships in your partner's map do you
consider concepts and vice versa?

### Learning Strategies (20 minutes)

1.  Which of the [learning strategies](#six-strategies) discussed
    above do you regularly use?  Which ones do you not?
2.  Write down three general concepts that you want your learners to
    master, and then give two specific examples of each.  (This uses
    practice #5).
3.  For each of those concepts, work backward from one of your
    examples to explain how the concept explains it.  (This uses
    practice #4).

### The Cost of Multi-Tasking (10 minutes)

[This post][switching] from the Learning Scientists describes a simple
experiment you can do without preparation or equipment (other than a
timer) to demonstrate the mental cost of multi-tasking.  Try the
activity in pairs, and then report your results to the group.

[bell-phone]: https://www.quora.com/Why-did-Bell-Labs-create-phone-numbers-of-7-digits-10-digits-Is-there-a-reason-that-dashes-and-brackets-are-used
[ihmc-cmap]: https://cmap.ihmc.us/
[learning-scientists]: http://www.learningscientists.org/
[six-strategies]: http://www.learningscientists.org/downloadable-materials
[switching]: http://www.learningscientists.org/blog/2017/7/28-1
