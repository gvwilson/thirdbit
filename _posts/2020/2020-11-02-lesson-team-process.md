---
title: "A Lightweight Process for Lesson Teams"
date: 2020-11-02
year: 2020
---

Over the course of my last several jobs,
I've been trying to develop a lightweight process for small teams who are developing lessons together.
Version control and a standard template are the "what",
and while there's a lot of room to improve the templates,
the "how" needs even more attention.
Here's my current best guess
for a team of half a dozen technically-skilled people who are building a large-ish set of tutorials,
and who are already familiar with the topic.
(If the team isn't already comfortable with what they're going to teach,
please read *[Teaching What You Don't Know](https://www.hup.harvard.edu/catalog.php?isbn=9780674066175)*
and then tell me what process you come up with.)

1.  Spend a few hours brainstorming the overall structure of the curriculum.
    I like [concept maps](https://github.com/gvwilson/concept-maps/) for this,
    but what's important is coming up with a rough decomposition of material into lessons.
    The details will change once you start work---probably more than you think---but
    this decomposition allows team members to work in parallel.

2.  Pick an editor---the human kind, not the Emacs-or-Word kind.
    Their job is to keep the big picture in mind
    and check everyone's rough first draft for gaps, overlaps, and inconsistencies.
    This is the point at which lessons are moved and/or refactored;
    like the editor of a medium-sized newspaper or magazine,
    they decide "is this worth finishing?"

3.  The authors' first task is to give the editor something to edit.
    Again, I like drawing concept maps,
    but a point-form outline with roughly one bullet per spoken minute can serve just as well.
    The most important thing,
    though,
    is to *include working code*.
    It doesn't matter what I'm teaching or how often I've taught it:
    as soon as I actually have to write code
    I discover that I've left out some important details that will take time to cover.
    Writing code at this stage also helps the editor:
    "explain anchors in regular expressions" is soothing but much more ambiguous
    than three lines of Python.

4.  Authors should also describe the lessons' [formative assessments](http://teachtogether.tech/en/index.html#s:models)
    at this point.
    I *don't* recommend completing them---writing auto-grading code is a lot of work
    that might need to be redone several times as material moves around---but
    a sentence or three outlining a multiple-choice question,
    fill-in-the-blanks coding exercise,
    or [Parsons Problem](http://teachtogether.tech/en/index.html#s:architecture-load)
    is a good reality check on how feasible the lesson is.

5.  If the team is using a plain-text format (e.g., Markdown) and GitHub,
    the author submits the draft as a pull request for the editor to review.
    The author then incorporates the editor's big-picture changes and
    re-works the outline,
    goes on to write the prose, draw the diagrams, and fill in the exercises, or
    hands it off to someone else,
    who ought to be able to fill it in more or less the way the outliner would have.
    (Handoffs like this are a good way to bring new team members on board.)

Nothing in this process is revolutionary,
but it seems to work reasonably well.
I'd be grateful for feedback on what other people have come up with and how well it's working.
