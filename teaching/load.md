---
layout: teaching
permalink: /teaching/load.html
title: "How to Teach Programming (and Other Things): Cognitive Load"
---

# Cognitive Load

**Objectives**

* **Learners can define cognitive load and explain how consideration
  of it can be used to shape instruction.**
* **Learners can explain what faded examples are and construct faded
  examples for use in programming workshops.**
* **Learners can explain what Parsons Problems are and construct
  Parsons Problems for use in programming workshops.**
* **Learners can describe ways they differ from their own students and
  what effect those differences have on instruction.**

In 2006, Kirschner, Sweller, and Clark published a paper titled "Why
Minimal Guidance During Instruction Does Not Work: An Analysis of the
Failure of Constructivist, Discovery, Problem-Based, Experiential, and
Inquiry-Based Teaching"
[[Kirschner2006](biblio.html#kirschner-minimal)]. Its abstract says:

> Although unguided or minimally guided instructional approaches are
> very popular and intuitively appealing…these approaches ignore both
> the structures that constitute human cognitive architecture and
> evidence from empirical studies over the past half-century that
> consistently indicate that minimally guided instruction is less
> effective and less efficient than instructional approaches that
> place a strong emphasis on guidance of the student learning
> process. The advantage of guidance begins to recede only when
> learners have sufficiently high prior knowledge to provide
> "internal" guidance.

The paper set off a minor academic firestorm, because beneath the
jargon the authors were claiming that _[inquiry-based
learning](gloss.html#inquiry-based-learning)_ doesn't actually work
very well.  Inquiry-based learning is the practice of allowing
learners to ask their own questions, set their own goals, and find
their own path through a subject, just as they would when solving
problems in real life.  It is intuitively appealing, but Kirschner
argued that it overloads learners, since it requires them to
simultaneously master both a domain's factual content and its
problem-solving strategies.

More specifically, _[cognitive load
theory](gloss.html#cognitive-load-theory)_ posits that people have to
deal with three things when they're learning:

1.  *Intrinsic* load is what people have to keep in mind in order to
    carry out a learning task.  In a programming class, this might be
    understanding what a variable is, or understanding how assignment in
    a programming language is different from creating a reference to a
    cell in a spreadsheet.

2.  *Germane* load is the (desirable) mental effort required to create
    linkages between new information and old, which is one of the
    things that distinguishes learning from memorization.  An example
    might be learning how to loop through a collection in Python.

3.  *Extraneous* load is everything else that distracts or gets in
    the way, such as knowing that tabs look like multiple characters but
    only count as one when indenting Python code.

According to this theory, searching for a solution strategy is an
extra burden on top of applying that strategy. We can therefore
accelerate learning by giving learners worked examples that show them
a problem and a detailed step-by-step solution, followed by a series
of _[faded examples](gloss.html#faded-example)_. The first of these
presents a nearly-complete use of the same problem-solving strategy
just demonstrated, but with a small number of blanks for the learner
to fill in. The next problem is also of the same type, but has more
blanks, and so on until the learner is asked to solve the entire
problem.  (The material that *isn't* blank is often referred to as
_[scaffolding](gloss.html#scaffolding)_, since it serves the same
purpose as the scaffolding set up temporarily at a building site.)

For example, someone teaching Python might start by explaining this:

~~~
# total_length(["red", "green", "blue"]) => 12
def total_length(words):
      total = 0
      for word in words:
          total += len(word)
      return total
~~~

<!--| \noindent |-->
then ask learners to fill in the blanks in:

~~~
# word_lengths(["red", "green", "blue"]) => [3, 5, 4]
def word_lengths(words):
      lengths = ____
      for word in words:
          lengths ____
      return lengths
~~~

<!--| \newpage |-->
<!--| \noindent |-->
The next problem might be:

~~~
# join_all(["red", "green", "blue"]) => "redgreenblue"
def join_all(words):
      result = ____
      for ____ in ____:
          ____
      return result
~~~

<!--| \noindent |-->
and learners would finally be asked to tackle:

~~~
# acronymize(["red", "green", "blue"]) => "RGB"
def acronymize(words):
      ____
~~~

Faded examples work because they introduce the problem-solving
strategy piece by piece. At each step, learners have one new problem
to tackle.  As [discussed later](practices.html#never-a-blank-page),
this is less intimidating than a blank screen or a blank sheet of
paper.  It also encourages learners to think about the similarities
and differences between various approaches, which helps create the
linkages in the mental model that instructors want them to form.

The key to constructing a good faded example is to think about the
problem-solving strategy or solution pattern that it is meant to
teach.  For example, the series of problems are all examples of the
*accumulator pattern*, in which the results of processing items
from a collection are repeatedly added to a single variable in some way
to create the final result.

Cognitive load theory has been criticized as being
[unfalsifiable][cognitive-load-unfalsifiable]: since there's no way to
tell in advance of an experiment whether something is germane or not,
any result can be justified after the fact by labelling things that
hurt performance as "extraneous" and things that don't "germane''.
However, there is no doubt that faded examples are effective.

> **Split Attention**
> 
> Research by Mayer and colleagues on the [split-attention
> effect][wikipedia-split-attention] is closely related to cognitive
> load theory [[Mayer2003](biblio.html#mayer-nine-ways)].  Linguistic and
> visual input are processed by different parts of the human brain,
> and linguistic and visual memories are stored separately as
> well. This means that correlating linguistic, auditory, and visual
> streams of information takes cognitive effort: when someone reads
> something while hearing it spoken aloud, their brain can't help but
> check that it's getting the same information on both channels.
> 
> Learning is therefore more effective when redundant information is
> *not* presented simultaneously in two different channels. For
> example, people find it harder to learn from a video that has both
> narration and on-screen captions than from one that has either the
> narration or the captions but not both.
> 
> The key word in the previous paragraph is "redundant".  It turns out
> that it's more effective to draw a diagram piece by piece while
> teaching rather than to present the whole thing at once.  If parts
> of the diagram appear at the same time as things are being said, the
> two will be correlated in the learner's memory.  Pointing at part of
> the diagram later is then more likely to trigger recall of what was
> being said when that part was being drawn.

Another way to use cognitive load theory to construct exercises is
called a _[Parsons Problem](gloss.html#parsons-problem)_.  If you are
teaching someone to speak a new language, you could ask them a
question, and then give them the words they need to answer the
question, but in jumbled order.  Their task is to put the words in the
right order to answer the question grammatically, which frees them
from having to think simultaneously about what to say *and* how to say
it.

Similarly, when teaching people to program, you can give them the
lines of code they need to solve a problem, and ask them to put them
in the right order.  This allows them to concentrate on control flow
and data dependencies, i.e., on what has to happen before what,
without being distracted by variable naming or trying to remember what
functions to call.

## Pattern Recognition

[An earlier section](memory.html#seven-plus-or-minus-two) described how
people chunk related or correlated information together so that they
can fit more into short-term memory.  One key finding in cognition
research is that experts have more and larger chunks than non-experts,
i.e., experts "see" larger patterns, and have more patterns to match
things against.  This allows them to reason at a higher level, and
to search for information more quickly and more accurately.

It is therefore tempting to try to teach patterns directly–in fact,
supporting this is one of the reasons programmers have been so
enthusiastic about [design patterns][wikipedia-design-patterns].  In
practice, though, pattern catalogs are too large to flick through and
too dry to memorize directly.  Giving names to a small number of
patterns, though, does seem to help with teaching, primarily by giving
the learners a richer vocabulary to think and communicate with
[[Kuittinen2004](biblio.html#kuittinen-patterns)].

## You Are Not Your Learners

People learn best when they care about the topic and believe they can
master it. Neither fact is particularly surprising, but their
practical implications have a lot of impact on what we teach, and the
order in which we teach it.

First, as noted in [Motivation](motivation.html), most people don't
actually want to program: they want to build a website or check on
zoning regulations, and programming is just a tax they have to pay
along the way. They don't care how hash tables work, or even that hash
tables exist; they just want to know how to process data faster. We
therefore have to make sure that everything we teach is useful right
away, and conversely that we don't teach anything just because it's
"fundamental".

Second, believing that something will be hard to learn is a
self-fulfilling prophecy. This is why it's important not to say that
something is easy: if someone who has been told that tries it, and it
doesn't work, they are more likely to become discouraged.

It's also why installing and configuring software is a much bigger
problem for us than experienced programmers like to acknowledge. It
isn't just the time we lose at the start of boot camps as we try to
get a Unix shell working on Windows, or set up a version control
client on some idiosyncratic Linux distribution.

It isn't even the unfairness of asking students to debug things that
depend on precisely the knowledge they have come to learn, but which
they don't yet have. The real problem is that every such failure
reinforces the belief that computing is hard, and that they'd have a
better chance of making next Thursday's deadline at work if they kept
doing things the way they always have. For these reasons, we have
adopted a "teach most immediately useful first" approach described
in [Motivation](motivation.html).

## Challenges

### Create a Faded Example (30 minutes)

It's very common for programs to count how many things fall into
different categories: for example, how many times different colors
appear in an image, or how many times different words appear in a
paragraph of text.

1.  Create a short example (no more than 10 lines of code) that shows
    people how to do this, and then create a second example that solves
    a similar problem in a similar way, but has a couple of blanks for
    learners to fill in.  How did you decide what to fade out?  What
    would the next example in the series be?

1.  Define the audience for your examples. For example, are these
    beginners who only know some basics programming concepts? Or are
    these learners with some experience in programming but not in
    Python?

1.  Show your example to a partner, but do *not* tell them what
    level it is intended for.  Once they have filled in the blanks, ask
    them what level they think it is for.

If there are people among the trainees who don't program at all, make
sure that they are in separate groups and ask to the groups to work
with that person as a learner to help identify different loads.

### Create a Parsons Problem (20 minutes)

Write five or six lines of code that does something useful, jumble
them, and ask your partner to put them in order.  If you are using an
indentation-based language like Python, do not indent any of the
lines; if you are using a curly-brace language like Java, do not
include any of the curly braces.

[cognitive-load-unfalsifiable]: https://edtechdev.wordpress.com/2009/11/16/cognitive-load-theory-failure/
[wikipedia-design-patterns]: https://en.wikipedia.org/wiki/Software_design_pattern
[wikipedia-split-attention]: https://en.wikipedia.org/wiki/Split_attention_effect
