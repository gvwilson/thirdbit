---
title: Wrapping Up
---

In most courses you never have to work on an assignment again once you submit
it.  Most project courses are different:

1.  Assignments are cumulative, i.e., each one builds on the ones before it.

1.  Projects may roll forward from one term to the next, so the end of one team's
    involvement isn't necessarily the end of the project.

1.  These courses are meant to simulate real life, where delivery of a
    particular version is just another step in the product lifecycle.

This chapter describes some things you might be asked to do when wrapping up.
Even if they aren't required, doing them is good practice for working in the
real world.

## What to Deliver

At a minimum, your finished project should have:

1.  A home page with an elevator pitch and a few paragraphs or bullet lists to
    help newcomers orient themselves.

1.  An architectural overview, including a block diagram of the major components
    and a walkthrough of how it behaves.  (I prefer the use-case maps[%i "use-case
    map" %] introduced in [%x design %] for this.)

1.  An installation guide.

1.  An up-to-date set of issues[%i "issue tracker!as course
    deliverable" %]. If the work has been done, the issue should be
    closed; if not, it should describe the state of the bug (or enhancement, or
    question) well enough for someone to know where to start work.

Another possible deliverable is a package[%i "package!as course
deliverable" %] that other people can download and install
([%x design %]). It isn't an either/or choice: every good package has a home page,
installation instructions, and so on.

<div class="callout" markdown="1">
## Bugs

It's OK to have bugs in your code when you finish your project—after all,
almost all products do. This isn't because developers are lazy or careless;
instead, it's a matter of economics.  If you're near the end of the development
cycle, it may be riskier to fix a minor bug (and introduce new bugs in doing so)
than to document its existence and provide a workaround.
</div>

Depending on the structure of your course, you may be asked to figure out how
much you would charge for the software you have produced.  The answer is out of
scope for this book, but [%b Davidson2009 %] is a good short introduction
to the topic.

You may also be asked to do some [%g marketing "marketing" %][%i "marketing" %],
which is the process of figuring out how to tell
the people you're trying to help how you can help them. This doesn't mean
spamming people with discount coupons; instead, it means explaining the problem
that the product will solve in ways that will reach the intended users.  I have
seen more startups fail because of poor marketing than because of poor
programming; it is also out of scope for this book, but [%b Jackson2017 %]
is a good introduction.

## Version Numbers

If your project is like most, you're going to submit your work several times
over the course of the term. That means it's important for you to keep track of
exactly what version you're working on at any time, where it came from, and
where it's going.

The usual way to do this is with [%g version_number "version numbers" %][%i "version numbers" %].  Most projects these days use
[%g semantic_versioning "semantic versioning" %][%i "semantic versioning" "version numbers!semantic versioning" %];
when you see a number like "6.2.3.1407"
attached to a piece of software, it generally means:

-   major version 6

-   minor version 2

-   patch 3

-   build 1407

The major version
number[%i "major version number" "version numbers!major" %] is only incremented when significant changes are made. In
practice, "significant" means "changes that make it impossible for older
versions to read the new version's data or configuration files". In practice,
major version numbers are often under the control of the marketing
department—if a competitor releases a new major version, we'd pretty much have
to as well.

Minor version
numbers[%i "version numbers!minor" "minor version number" %] are what most people think of as releases. If you've added a few
new features, changed part of the GUI, etc., you increment the minor version
number so that your customers can talk intelligently about which version they
have.

[%g patch "Patches" %][%i "patch (software)" "software patch" "version numbers!patch" %] don't have their own installers. If, for example,
you need to change one HTML form, or one DLL, you will often just mail that out
to customers, along with instructions about where to put it, rather than
creating a new installer. You should still give it a number, though, and make an
entry in your release log.

The [%g build_number "build number" %][%i "build number" "version numbers!build" %] is incremented every time you create a new version of the product
for QA to test. Build numbers are never reset, i.e. you don't go from 5.2.2.1001
to 6.0.0.0, but from 5.2.2.1001 to 6.0.0.1002, and so on. Build numbers are what
developers care about: they're often only matched up with version numbers after
the fact (i.e. you create build #1017, QA says, "It looks good," so you say,
"All right, this'll be 6.1.0," and voila, you have 6.1.0.1017.)

Finally, groups will sometimes identify pre-releases as "beta 1", "beta 2", and
so on, as in "6.2 beta 2". Again, this label is usually attached to a particular
build after the fact—you wait until QA (or whoever) says that build #1017 is
good enough to send out to customers, then tag it in version control.

A four-part numbering scheme is more than you need for an undergraduate
course. You can probably get away with just one: the assignment the software was
submitted for.

Most programs can report a version number, either through an "About…" menu item
or through a command-line option like `--version`.  It helps a lot when people are
reporting bugs.

## The Final Report

The other thing student projects usually have to deliver is some kind of final report[%i "final report" %]. Most students short-change this part of
the course, in part because it comes at the end, but also because they think, "I
want to write code, not a novel." However, [%b Fogel2005 %] had this to
say:

> The ability to write clearly is perhaps the most important skill one can have in
> an open source environment. In the long run it matters more than programming
> talent. A great programmer with lousy communication skills can only get one
> thing done at a time, and even then may have trouble convincing others to pay
> attention. But a lousy programmer with good communication skills can coordinate
> and persuade many people to do many different things, and thereby have a
> significant effect on a project's direction and momentum.

Final reports can range from half a dozen to fifty pages, depending on the
course's structure and the instructor's whims.  Regardless of their size, they
will usually include the following:

Title page, abstract, and table of contents.
:   The first identifies the document; the second summarizes it in three or four
    sentences, so that busy people can decide whether they ought to read the
    whole thing; and the third helps people navigate.

An introduction that orients the reader.
:   This explains what problem the team set out to solve, and summarizes any
    background knowledge needed to understand the team's solution.  It shouldn't
    state the obvious: there's no need to tell readers what the Internet is, or
    how a parser works. Instead, it should cover whatever general knowledge the
    *next* team will need in order to continue the project.

A summary of what was accomplished.
:   This should not just summarize the analysis & estimation
    ([%x process %]), although that's a good place to start. Instead, it should
    describe the system's architecture, any features of its data formats, class
    structure, or UI that won't immediately make sense to a knowledgeable
    observer, and so on ([%x "design" %]). As with the introduction, the
    target audience is the next team to work on the project.

A summary of the current state of the project.
:   This should include high-level criticism ("The persistence layer works fine,
    but in retrospect, our concurrency control mechanism was a bad choice") and
    pointers to specifics ("Issue 213 should be addressed before any further
    work is done on user preferences").

An evaluation of the project.
:   What did the team learn about teamwork? What went well? What should they
    never do again?  Don't bother including generic statements about the
    importance of version control; instead, conduct a proper post mortem (as
    described below) and present as honest a summary of its findings as
    possible.  (The checklists in [%x eval-project %] and
    [%x eval-personal %] may be useful starting points.)

References.
:   Include books, papers, and links the team found helpful so that whoever
    inherits the project doesn't have to search for them again.

This report is neither a user's guide nor maintenance documentation. Instead, it
is like the end-of-contract reports I prepare when I'm consulting.  What have I
done to earn my customers' money? What should the next person (who might not be
me) do? What can I tell them that would save them time?

So much for what the final report should include; how should you actually go
about writing it? It will probably include:

-   paragraphs of text;

-   equations;

-   source code;

-   vector graphics (such as graphs and line drawings); and

-   raster graphics (such as screen shots).

Lots of tools exist that will handle these, but they all have shortcomings.  You
can create your report as a set of wiki pages or Google Docs, but they don't
flag conflicts between concurrent authors.  On the other end of the spectrum are
WYSIWYG editors like Microsoft Word[%i "Microsoft Word" %] and LibreOffice[%i "LibreOffice" %]. Unfortunately, these get in the way at least
as much as they help:

1.  They store documents in non-text formats that version control systems can't
    diff or merge[%i "version
    control!inability to handle office documents" %].

2.  It's hard to write scripts to process these documents, so inclusions (such
    as code fragments) have to be done manually.

3.  Neither one handles equations very well (although both are getting better).

4.  It's very easy to format things using low-level primitives ("make this
    italic") rather than logical styles ("making this a book title"), which
    makes it difficult to keep the document consistent over time.

For these reasons, most teams format their reports as a set of Markdown[%i "Markdown!for final report" %] pages under version control and
use a static site generator[%i "static site generator" %]
([%x communicate %]) to turn them into a report. That solves the problem of
multiple authors (Markdown is a text format, so diff and merge will work), and
if you know a little CSS, you can make it look as pretty as you want. Diagrams
and screenshots work well, and you can embed [MathML][mathml][%i "MathML" %] for equations if you need to.  The downside
is that you can't actually see what your document is going to look like until
you compile it, and doing that breaks your flow[%i "flow" %].

<div class="callout" markdown="1">
### LaTeX

LaTeX[%i "LaTeX" %] is a markup language that's much more sophisticated
than HTML and has literally thousands of add-on packages for equations, code
formatting, and just about everything else you could want. Like HTML, LaTeX is a
text format, so it plays nicely with version control.  However, its power comes
at a steep price: LaTeX is as hard to master as a programming language. It also
has a frustratingly slow formatting cycle, since documents have to be compiled
several times to resolve cross-references.
</div>

## The Post Mortem

The most valuable part of your project isn't the software you write, or the
grade you're given: it's the [%g post_mortem "post mortem" %][%i "post mortem" %]. Literally, this is an examination of a deceased person; in a
software project, it's a look back at what went right and what went wrong.

The aim of a post mortem is to help the team and its members do better next time
by giving everyone a chance to reflect on what they've just accomplished. It is
*not* to shame people, but it can be hard to critique someone's work without
them taking it personally, so post mortems add a few extra rules to the ones
introduced for meetings[%i "meetings!extra rules for post mortems" %]
in [%x important %]:

Get a moderator who wasn't part of the project.
:   Someone who doesn't have a stake in the project should run the meeting.
    Otherwise, the meeting will either go in circles, or focus on only a subset
    of important topics. In the case of student projects, this moderator might
    be the course instructor, or (if the course is too large) a TA.  You can
    have another student as moderator, but since they are probably friends with
    some team members, it may be hard for them to be objective.

Set aside an hour, and *only* an hour.
:   In my experience, nothing useful is said in the first ten minutes of anyone's
    first post mortem, since people are naturally a bit shy about praising or
    damning their own work. Equally, nothing useful is said after the first
    hour: if you're still talking, it's probably because one or two people have
    a *lot* they want to get off their chests.

Require attendance.
:   Everyone who was part of the project ought to be in the room for the post
    mortem. This is more important than you might think: the people who have the
    most to learn from the post mortem are often least likely to show up if the
    meeting is optional.

Make two lists.
:   Put the headings "Keep" and "Change" on the board, then do a lap around the
    room and ask every person to give me one item that hasn't already been
    mentioned for each list.  The "hasn't already been mentioned" part is
    important: after the first few safe responses are up on the board, people
    have to start saying the more difficult things that really matter.

Comment on actions rather than individuals.
:   Don't let tension between teammates sidetrack the meeting: if someone has a
    specific complaint about another member of the team, require them to
    criticize a particular event or decision. "They had a bad attitude" does
    *not* help anyone improve their game.

Once everyone's thoughts are out in the open, organize them somehow so that you
can make specific recommendations about what to do next time.  For example, here
are the recommendations that came out of one post mortem I did with students:

1.  Do a better job of tracking actual progress, rather than reported progress.
    Maybe require a one-minute demo every time a feature is marked "complete"?

2.  Teams should find one block of 2--3 hours per week when they can work side
    by side: IM meetings and email resulted in a lot of dropped balls.

3.  Having someone who worked on the project in the previous term come in to get
    the new team up to speed made a huge difference.

4.  Issue tracking system was too complicated for students' needs: really just
    want a shared online to-do list.

5.  Teams should have to report test coverage at every progress meeting to make
    sure that a lot of untested code doesn't pile up during the term.

<div class="callout" markdown="1">
### Pay it forward

Ask your instructor at the start of your course for copies of the post mortems
written by previous student teams.  Go through and pick out some common themes,
then use them as a list of things to do or avoid in your own project.  Sharing
what you've learned with those who come after you is the most compassionate
thing you can do.
</div>
