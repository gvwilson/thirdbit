---
layout: teaching
permalink: /teaching/novice.html
title: "How to Teach Programming (and Other Things): Helping Novices Build Mental Models"
---

# Helping Novices Build Mental Models

**Objectives**

* **Learners can explain the cognitive differences between novices
  and competent practitioners in terms of mental models, and
  explain the implications of these differences for teaching.**
* **Learners can define and differentiate formative and summative
  assessment.**
* **Learners can construct multiple-choice questions with
  plausible distractors that have diagnostic power.**

The first task in teaching is to figure out who your learners are and
how best to help them.  Our approach is based on the [Dreyfus model of
skill acquisition][wikipedia-dreyfus], and more specifically on the
work of researchers like Patricia Benner, who studied how nurses
progress from being novices to being experts
[[Benner2000](biblio.html#benner-expertise)].  Benner identified five
stages of cognitive development that most people go through in a
fairly consistent way.  (We say "most" and "fairly" because human
beings are variable, and there will always be outliers.  However, that
shouldn't prevent us from making strong statements about what's true
for the majority.)

For our purposes, we simplify the five stages to three:

1.  A _[novice](gloss.html#novice)_ is someone who doesn't know what
    they don't know, i.e., they don't yet know what the key ideas in
    the domain are or how they relate. They reason by analogy and
    guesswork, borrowing bits and pieces of their mental models of
    other domains which seem superficially similar.

2.  A _[competent practitioner](gloss.html#competent-practitioner)_
    is someone who has a mental model that's good enough for everyday
    purposes: they can do normal tasks with normal effort under normal
    circumstances. This model does not have to be completely accurate
    in order to be useful: for example, the average driver's mental
    model of how a car works probably doesn't include most of the
    complexities that a mechanical engineer would be concerned with.

3.  An _[expert](gloss.html#expert)_ is someone who can easily handle
    situations that are out of the ordinary, diagnose the causes of
    problems, and so on. We will discuss expertise in more detail in
    [Memory](memory.html).

One sign that someone is a novice is that the things they say aren't
even wrong, e.g., they think there's a difference between programs
they type in character by character and identical ones that they have
copied and pasted.  As we will discuss [later](motivation.html), it is
very important not to shame novices for this.

One example of a mental model is the ball-and-spring model of
molecules that most of us encountered in high school chemistry. Atoms
aren't actually balls, and their bonds aren't actually springs, but
the model does a good job of helping people reason about chemical
compounds and their reactions.  Another model of an atom has a small
central ball (the nucleus) surrounded by orbiting electrons.  Again,
this model is wrong, but useful for many purposes.

Novices, competent practitioners, and experts need to be taught
differently.  In particular, presenting novices with a pile of facts
early on is counter-productive, because they don't yet have a model to
fit those facts into.  In fact, presenting too many facts too soon can
actually reinforce the incorrect mental model they've cobbled
together.  As Derek Muller wrote about this
[[Muller2011](biblio.html#muller-videos)] in the context of video
instruction for science students:

> Students have existing ideas about scientific phenomena before
> viewing a video. If the video presents scientific concepts in a
> clear, well illustrated way, students believe they are learning but
> they do not engage with the media on a deep enough level to realize
> that what was is presented differs from their prior knowledge.
>
> There is hope, however. Presenting students' common misconceptions
> in a video alongside the scientific concepts has been shown to
> increase learning by increasing the amount of mental effort students
> expend while watching it.

The goal with novices is therefore *to help them construct a working
mental model* so that they have somewhere to put facts.  As an example
of what this means in practice, Software Carpentry's [lesson on the
Unix shell][swc-unix] introduces fifteen commands in three
hours. Twelve minutes per command may seem glacially slow, but the
lesson's real purpose isn't to teach those fifteen commands: it's to
teach learners about paths, history, tab completion, wildcards, pipes
and filters, command-line arguments, redirection, and all the other
big ideas that the shell depends on.  Once they understand those
concepts, people can quickly learn a repertoire of commands.  What's
more, later lessons on how to build functions in a programming
language can refer back to pipes and filters, which helps solidify
both ideas.

> **Different Kinds of Lessons**
> 
> The cognitive differences between novices and competent
> practitioners underpin the differences between two kinds of teaching
> materials. A tutorial's purpose is to help newcomers to a field
> build a mental model; a manual's role, on the other hand, is to help
> competent practitioners fill in the gaps in their
> knowledge. Tutorials frustrate competent practitioners because they
> move too slowly and say things that are obvious (though of course
> they are anything but to newcomers). Equally, manuals frustrate
> novices because they use jargon and *don't* explain things. One of
> the reasons Unix and C became popular is that Kernighan et al's
> trilogy [[Kernighan1982](biblio.html#kernighan-plauger-elements)],
> [[Kernighan1984](biblio.html#kernighan-pike-upe)],
> [[Kernighan1988](biblio.html#kernighan-ritchie-c)] somehow managed to be
> good tutorials *and* good manuals at the same time. Ray and Ray's
> book on Unix [[Ray2014](biblio.html#ray-ray-unix)] and Fehily's
> introduction to SQL [[Fehily2008](biblio.html#fehily-sql)] are among the
> very few other books in computing that have accomplished this.

One of the challenges in building a mental model is to clear away
things that *don't* belong.  As Mark Twain said, "It ain't what
you don't know that gets you into trouble. It's what you know for sure
that just ain't so."

Broadly speaking, learners' misconceptions fall into three categories:

1.  Simple *factual errors*, such as believing that Vancouver is the
    capital of British Columbia (it's Victoria). These are simple to
    correct, but getting the facts right is not enough on its own.

2.  *Broken models*, such as believing that motion and acceleration
    must be in the same direction. We can address these by having them
    reason through examples to see contradictions.

3.  *Fundamental beliefs*, such as "the world is only a few thousand
    years old" or "some kinds of people are just naturally better at
    programming than others"
    [[Patitsas2016](biblio.html#patitsas-cs-grades)].  These are often
    deeply connected to the learner's social identity, and so are
    resistant to evidence and cannot be reasoned away in class.

## Formative Assessment

Teaching is most effective when instructors have a way to identify and
clear up learners' misconceptions *while they are teaching*.  The
technical term for this is _[formative
assessment](gloss.html#formative-assessment)_, which is assessment
that takes place during the lesson in order to form or shape it.
Learners don't pass or fail formative assessments; instead, its main
purpose is to tell both the instructor and the learner how the learner
is doing, and what to focus on next.  For example, a music teacher
might ask a student to play a scale very slowly in order to see
whether she is breathing correctly, and if she is not, what she should
change.

The counterpoint to formative assessment is _[summative
assessment](gloss.html#summative-assessment)_, which is used at the end
of the lesson to tell whether the desired learning took place and
whether the learner is ready to move on.  One example is a driving
exam, which reassures the rest of society that someone can safely be
allowed on the road.

> *When the cook tastes the soup, that's formative.
> when the guests taste the soup, that’s summative.  
> - Michael Scriven, as quoted by Debra Dirksen.

<!-- comment needed to separate blockquotes -->

> **Connecting Formative and Summative Assessment**
> 
> One rule to use when designing lessons is that formative assessments
> should prepare people for summative assessments: no one should ever
> encounter a question on an exam for which the teaching did not
> prepare them.  This doesn't mean that novel problems should not
> appear, but that if they do, learners should have had practice with
> and feedback on tackling novel problems beforehand.

In order to be useful during teaching, a formative assessment has to
be quick to administer and give an unambiguous result. The most widely
used kind of formative assessment is probably the multiple choice
question (MCQ). When designed well, these can do much more than just
tell whether someone knows something or not. For example, suppose we
are teaching children multi-digit addition. A well-designed MCQ would
be:

> Q: what is 27 + 15 ?
>
> 1.  42
> 1.  32
> 1.  312
> 1.  33

The correct answer is 42, but each of the other answers provides
valuable insight:

*   If the child answers 32, she is throwing away the carry completely.

*   If she answers 312, she knows that she can't just discard the
    carried 1, but doesn't understand that it's actually a ten and needs
    to be added into the next column. In other words, she is treating
    each column of numbers as unconnected to its neighbors.

*   If she answers 33 then she knows she has to carry the 1, but is
    carrying it back into the same column it came from.

Each of these incorrect answers is a _[plausible
distractor](gloss.html#plausible-distractor)_ with _[diagnostic
power](gloss.html#diagnostic-power)_.  "Plausible" means that it looks
like it could be right, while "diagnostic power" means that each of
the distractors helps the instructor figure out what to explain to
that particular learner next.

A good MCQ tests for conceptual misunderstanding rather than simple
factual knowledge. If you are having a hard time coming up with
diagnostic distractors, then either you need to think more about your
learners' mental models, or your question simply isn't a good starting
point for an MCQ.

When you are trying to come up with distractors, think about questions
that learners asked or problems they had the last time you taught this
subject. If you haven't taught it before, think about your own
misconceptions or ask colleagues about their experiences.  You can
also ask open-ended questions in one class to collect misconceptions
about material to be covered in a later class.

> **Humor**
>
> Instructors will often put supposedly-silly answers like "a fish!"
> on MCQs, particularly ones intended for younger learners.  However,
> they don't provide any insight into learners' misconceptions, and
> most learners don't actually find them funny.

Instructors should use MCQs or some other kind of formative assessment
every 10-15 minutes in order to make sure that the class is actually
learning.  That way, if a significant number of people have fallen
behind, only a short portion of the lesson will have to be repeated.
Additionally, most learners can only focus intensely for roughly this
long, so using formative assessments this frequently also helps them
re-focus.

Formative assessments can also be used preemptively: if you start a
class with an MCQ and everyone can answer it correctly, then you can
safely skip the part of the lecture in which you were going to explain
something that your learners already know. Doing this also helps show
learners that the instructor cares about how much they are learning,
and respects their time enough not to waste it.

But what should you do if most of the class votes for one of the wrong
answers? What if the votes are evenly spread between options?  The
answer is, "It depends."  If the majority of the class votes for a
single wrong answer, you should go back and work on correcting that
particular misconception. If answers are pretty evenly split between
options, learners are probably guessing randomly and it's a good idea
to go back to a point where everyone was on the same page.

If most of the class votes for the right answer, but a few vote for
wrong ones, you have to decide whether you should spend time getting
the minority caught up, or whether it's more important to keep the
majority engaged.  This is just one example of one of the most
important rules of teaching: no matter how hard you work, or what
teaching practices you use, you won't always be able to give everyone
the help they need.

> **Concept Inventories**
>
> Given enough data, MCQs can be made surprisingly precise.  The
> best-known example is the [Force Concept Inventory][wikipedia-fci],
> which gauges understanding of basic Newtonian mechanics. By
> interviewing a large number of respondents, correlating their
> misconceptions with patterns of right and wrong answers to
> questions, and then improving the questions, its creators
> constructed a diagnostic tool to pinpoint specific misconceptions.
> However, it's very costly to do this, and students' ability to
> search for answers on the internet is an ever-increasing threat to
> the validity of tools like this.

Designing an MCQ with plausible distractors is useful even if it is
never used in class because it forces the instructor to think about
the learners' mental models and how they might be broken–in short,
to put themselves into the learners' heads and see the topic from
their point of view.

> **Why Not MOOCs**
>
> Massive open online courses (MOOCs) in which students watch videos
> instead of attending lectures, and then do assignments that are
> (usually) robo-graded, were a hot topic a few years ago.  Now that
> the hype has worn off, though, it's clear that they aren't as
> effective as their more enthusiastic proponents claimed they would
> be [[Ubell2017](biblio.html#ubell-moocs)].
>
> Recorded content is ineffective for most novices learners because it
> cannot intervene to clear up specific learners' misconceptions. Some
> people happen to already have the right conceptual categories for a
> subject, or happen to form them correctly early on; these are the
> ones who stick with most massive online courses, but many
> discussions of the effectiveness of such courses ignore this
> survivor bias.
>
> *If you use robots to teach, you teach people to be robots.*  
> – variously attributed

## Teaching Practices

If you haven't done so already, you should start using these three
teaching practices in your instructor training workshop:

*   [Use sticky notes as status flags](practices.html#sticky-notes-as-status-flags)
    so that you can quickly see who needs help, who has questions,
    and who's ready to move on.

*   [Use sticky notes to distribute attention](practices.html#sticky-notes-to-distribute-attention)
    so that everyone gets a fair share of the instructor's time.

*   [Use sticky notes as minute cards](practices.html#minute-cards) to
    encourage learners to reflect on what they've just learned and to
    give instructors actionable feedback while they are still in a
    position to act on it.

## Challenges

### Your Mental Models (5 minutes)

What is one mental model you use to frame and understand your work?
Write a few sentences describing it in the shared notes, and give
feedback on other learners' contributions.

### Symptoms of Being a Novice (5 minutes)

What are the symptoms of being a novice?  I.e., what does someone do
or say that leads you to classify them as a novice in some domain?

### Modelling Novice Mental Models (20 minutes)

Create a multiple choice question related to a topic you intend to teach
and explain the diagnostic power of each its distractors (i.e., what
misconception each distractor is meant to identify).

When you are done, give your MCQ to a partner, and have a look at
theirs.  Is the question ambiguous?  Are the misconceptions plausible?
Do the distractors actually test for them?  Are any likely
misconceptions *not* tested for?

### Other Kinds of Formative Assessment (20 minutes)

A good formative assessment requires people to think through a
problem.  For example, consider this question from
[[Epstein2002](biblio.html#epstein-thinking-physics)].  Imagine that you
have placed a cake of ice in a bathtub and then filled the tub to the
rim with water. When the ice melts, does the water level go up (so
that the tub overflows), go down, or stay the same?

The correct answer is that the level stays the same: the ice displaces
its own weight in water, so it exactly fills the "hole" it has made
when it melts.  Figuring this out why helps people build a model of
the relationship between weight, volume, and density.

Describe another kind of formative assessment you have seen or used and
explain how it helps both the instructor and the learner figure out
where they are and what they need to do next.

### A Different Progression (15 minutes)

Another progression often used to describe the path from novice to expert is
the [four stages of competence][four-competence]:

* Unconscious incompetence: the person doesn't know what they don't know.
* Conscious incompetence: the person realizes that they don't know something.
* Conscious competence: the person has learned how to do something, but can
  only do it while concentrating, and may still need to break things down into
  steps.
* Unconscious competence: the skill has become second nature, and the person
  can do it reflexively.

Describe one or more subjects related to programming for which you are
at each of these levels.

[four-competence]: https://en.wikipedia.org/wiki/Four_stages_of_competence
[swc-unix]: http://swcarpentry.github.io/shell-novice/
[wikipedia-dreyfus]: https://en.wikipedia.org/wiki/Dreyfus_model_of_skill_acquisition
[wikipedia-fci]: https://en.wikipedia.org/wiki/Force_Concept_Inventory
[wikipedia-peer-instruction]: https://en.wikipedia.org/wiki/Peer_instruction
