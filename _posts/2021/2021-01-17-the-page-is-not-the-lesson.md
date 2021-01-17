---
title: "The Page Is Not The Lesson"
date: 2021-01-17
year: 2021
---

> *The finger pointing at the moon is not the moon.*
>
> --- variously attributed

I [tweeted yesterday](https://twitter.com/gvwilson/status/1350419811080269824)
about using static website generator templates for lessons:

1.  Programmers follow many conventions to make code repos more usable,
    from having `README`, `LICENSE`, and `CONDUCT1 files in the root directory
    to naming conventions, package structure, and having `make test` or `npm run test` do something useful.

1.  Every time I see an aggregation like this,
    I wish we had similar interoperability/discoverability conventions for tutorials.
    That doesn't mean "one template to rule them all"
    any more than it means every software project must have exactly the same structure, but…

1.  …imagine a world in which every tutorial had a GLOSSARY file beside its README and LICENSE files
    so that you could easily find out what terms that lesson defined
    (which in turn would tell you what it was about)?
    Or a convention for structuring exercises…

1.  …similar to the conventions that programming languages have for structuring tests
    (where they are, what they're called, etc.).
    There are standards for creating and packaging learning objects for use with learning management systems,
    but…

1.  …they are much too burdensome for most free-range teaching—it's as if our only options were chaos or Enterprise Java.
    I hope some day that creating a lesson on GitHub is as easy
    (i.e., as well supported both technically and socially)
    as creating a Node project.

1.  One way forward could start with a change of perspective:
    instead of thinking a package as "code with some docs",
    think about it as "docs with some supporting code".
    What would we have to add to turn a site like <https://readthedocs.org> into a lesson hub?

1.  Auto-grading is a distraction in this context—it's certainly not a must-have,
    not even for coding lessons.
    (Proof: textbooks have been around and useful for centuries without auto-grading.)
    But think about things like…

1.  …consistent numbering of exercises and figures *across multiple source documents*.
    Think about learning objectives that can be put in each individual lesson,
    but extracted and collated as a summary.
    All of these things…

1.  …can be done with existing tools,
    but they're all harder and more fragile than documenting the parameters to a method
    or cross-referencing classes and their ancestors/decendants.
    (If your "solution" requires people to indent their YAML, it's not a solution.)

1.  And yes, the analogy with reusing code is flawed—the [Reusability Paradox](http://opencontent.org/docs/paradox.html)
    is very real—but I believe *discoverability* and *interoperability* are worthwhile, achievable goals.

1.  How can I tell at a glance that a site or repo is a lesson rather than [noun]?
    What about the (human) language it's in?
    Ditto its major topics.
    We're done this part when I can search for "lesson in Spanish about JavaScript callbacks" with high signal-to-noise.

1.  This is part of why we wrote <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008469>
    (see also <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007854>):
    we should listen to librarians & teachers before we create more templates
    (but then, I think the world would be a better place if we all listened to librarians and teachers more…)

Much of the discussion that followed on Twitter and by email took the form,
"If we build a good enough template, people will adopt it."
With respect,
I think that if better templates were the solution,
they would have worked by now.
I have written several myself,
including the first version of [the Carpentries template](https://github.com/carpentries/styles/);
I've used several others,
and a search on GitHub turns up dozens of others.

The problem is that templates help *present* the lesson but don't help *write* it.
For example,
all of the templates I've looked at allow authors to write whatever they want for learning objectives.
They don't help connect those objectives together
or check that the objectives are still consistent with the lesson's content:
"still" because lessons evolve over time,
and people forget to check and update objectives
just as they forget to check and update documentation and installation instructions for code.
Just as UML [doesn't help developers solve the hard parts of their problems](http://oro.open.ac.uk/35805/8/UML%20in%20practice%208.pdf),
static website frameworks don't help teachers any more than a Microsoft Word or Google Doc template.

> That's a slight exaggeration:
> templates *do* help keep common values like the author's email address consistent.
> However, the cost is very high:
> installing Jekyll or Hugo,
> writing YAML to configure them,
> and getting the right plugins in place (never mind keeping them up to date)
> is a hell of a cover charge.
> The payoff seems small,
> particularly if you aren't already steeped in the technology,
> so on any given Thursday,
> most teachers really are better off using Word or Docs.

The Glosario project ([site](https://glosario.carpentries.org/), [repo](https://github.com/carpentries/glosario))
is an experiment to see if we can do better.
Suppose you're writing a lesson about data science using Markdown.
Instead of using **bold** or `[an arbitrary link](http://somewhere/#term)` to highlight a definition,
you either:

1.  refer to `[the online glossary](https://glosario.carpentries.org/en/#term)` (in your preferred language), or

1.  call an inline function like `gloss('key', 'inline text')` to generate that text and link
    (if you're using something like R Markdown).

In both cases,
tools can now tell which terms a particular lesson defines.
Those terms can then be put in the `<head>` of a web page,
stuffed in a database,
or added to a summary page for the course as a whole.
Doing this accomplishes two things:

1.  It makes the lessons more discoverable.

1.  It allows to build another tool for stitching lessons together.
    People will not manually highlight all of the terms they use in a lesson that they don't define:
    it's too much work,
    and requires too much re-work as the glossary evolves.
    However,
    it would be relatively straightforward to compare the text of a lesson against a glossary
    to determine what terms it depends on
    so that we can say, "You probably want to look at lessons X and Y before tackling lesson Z."

No templating engine I know of will do this right now.
Most of them won't even do simpler but equally necessary things
like create two-part IDs for the figures within chapters
and then fill in references with `chapter.figure`.

> Yes, I've used [GitBook](https://www.gitbook.com/),
> [Bookdown](https://www.bookdown.org/),
> and [JupyterBook](https://jupyterbook.org/).
> No, they are not solutions for the 99.9% of our species
> that can't or won't spend their afternoons messing with Pandoc templates,
> LaTeX packages,
> and conflicts between multiple YAML configuration files.

So here's what I'd like,
and yes,
I *do* think this would be a great project for someone doing a PhD in HCI:
finish the tooling for [Glosario](https://glosario.carpentries.org/),
fold it into lessons written with the template of your choice,
and tell us what you've learned about how to build it
and about whether authors, instructors, and learners actually find it useful.
It may seem like a small thing,
but I bet it's harder than it looks,
and I bet we'll learn a lot more from doing it than we expect.
Most importantly,
I think it would a good first step toward shifting our attention from the page to the lesson.
