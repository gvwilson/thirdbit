---
title: "Static Lesson Generators"
date: 2020-09-13
year: 2020
---

Yesterday I tweeted:

> Somewhere out there, in a timeline very close to ours,
> there are as many static site generators for lessons and courses as there are for blogs,
> and that design space has been as well explored.

and:

> And somewhere, in an even better timeline,
> it's normal and valued for grad students in software engineering to write
> detailed, theoretically-well-founded compare-and-contrast analyses of those design spaces.

I'm not going to attempt the latter here—doing it properly
would take several months of research and careful thought—but
after trying and failing for years to build a usable framework for lessons using [Jekyll](https://jekyllrb.com/),
I hope a sketch of how I think about static site generators
and what I'd want from a lesson generator might be useful.
To set the stage:

1.  In the beginning we wrote web pages by hand and put them in our `htdocs` directory
    so that our web server could share them with the world.

1.  We quickly realized that some content needed to be generated on the fly,
    so we created content management systems (CMSes) to parse the user's HTTP request,
    look things up on disk or in a database,
    and generate HTML right then and there.

1.  But it turned out that a lot of sites didn't need just-in-timeness,
    and that creating pages once and serving them many times put less load on the server
    and enabled caching,
    so we created static site generators (SSGs).

Every SSG I've used is built around templates that define how pages are laid out.
These templates combine plain old HTML (which is copied verbatim)
and code fragments that repeat some chunks,
conditionally include other chunks,
and/or insert data values into the generated pages.
The SSG reads files containing content
and configuration files containing commonly-used values like the site's contact address
and combines that information with the templates to produce the static pages making up the site.

I think any tool that does what's described in the previous paragraph is an SSG
in the same way that anything with feathers and a beak is a bird,
but it's a very large design space:

-   Most SSGs allow files to include other files
    so that things like headers and footers will be consistent.

-   Most SSGs allow some in-page processing of data,
    such as converting file paths to absolute URLs,
    formatting dates,
    or filtering lists.

-   Most can load data files (typically formatted as YAML)
    and then use that data to drive page generation.

-   Most can hand off processing of specialized files to other tools:
    for example, most will turn SASS into pure CSS automatically.

The paradigm of SSGs is a blog
(where I used the word "paradigm" in the sense of something that serves as a defining exemplar).
I have used them to create tutorial websites,
but:

-   SSGs don't support specialized forms of cross-referencing
    that have been around for centuries,
    such as bibliographic citations or glossary references.
    You can do these by hand (which is error-prone)
    or write little include snippets that parse parameters and generate the HTML you want
    (which is cumbersome, but at least gives you error messages).

-   SSGs don't support numbered cross-references like `Exercise 3.4` or `Figure 5.6`
    (where `3.4` is generated on the fly).
    I realize numbering pages isn't how the web works,
    but when you have a dozen tutorials,
    each with a dozen of these entities,
    you really do want meaningful short labels.
    You particularly want them when you're generating a printable PDF,
    because hyperlinking text like "this figure" doesn't work on paper.
    (And yes, print still matters…)

-   And speaking of exercises,
    their implicit semantics is at least as rich as that of blog posts:
    where the latter have excerpts, slugs, and tags,
    the former have things like hints and solutions.
    You can build these inline with nested `div`s,
    but what if you want the exercise in one place and the solution in another?
    The solutions I've seen are:

    1.  Manage it by hand (which in practice quickly means
        "build a little script to check consistency").

    2.  Put every exercise in a sub-directory that has files with fixed names
        like `exercise.md`, `solution.md`, `hint-01.md`, and so on,
        then use templates to load these snippets in the right places.

    3.  Write each exercise, its solution, and what-not as YAML,
        which is basically the same as #2 except everything's in one file.

    All of these work, but none are anywhere near as smooth an experience
    as writing a blog post.

-   When I'm presenting code I frequently want to show a simple solution to something,
    explain why it's inadequate,
    and then present a replacement for part of it without repeating the rest.
    I don't know _any_ tool that does this:
    I've seen and built solutions that rely on `#include`-style processing
    and specially-formatted comments to select or exclude variant chunks in a single file,
    but the rest of my programming tools don't understand them,
    so I've just traded one kind of pain for another.

-   Finally, lessons themselves also have some implicit semantics
    that SSGs designed for blogging don't support.
    In our upcoming book
    *[Research Software Engineering with Python]({{'/py-rse/' | relative_url}})*,
    each chapter starts with learning objectives and ends with a summary of key points.
    The former and latter also appear in appendices for easy reference,
    so we've put each set in its own includable file.
    That information *should* live in each chapter's YAML header,
    but the tool we're using doesn't provide a way for one page to access another's header data.
    Again, we could put that information in a single YAML file
    and have each chapter look up its portion,
    but that's like putting the code in one file and its documentation in another:
    experience shows that keeping them side by side makes maintenance and consistency a lot easier.

At this point you may be thinking, "But LaTeX! Or Bookdown!"
In practice,
they make some things easier but other things harder.
But this blog post isn't about designing a better static lesson generator.
What I really want is an in-depth, peer-reviewed analysis of this design space.
What are the paradigmatic needs that define "this design space"?
What approaches have been taken in the past?
What workarounds or shims have people evolved to handle needs that *aren't* core?

And most importantly,
why aren't analyses like these a standard part of a software engineer's education?
The architects who live across the street from me have a shelf full of books
that analyze buildings of differents and styles,
from medieval cathedrals to modern Scandinavian bus shelters
(which appear to have undergone the same kind of adaptive radiation as Darwin's finches).
They started to learn what had come before,
why it was built the way it was,
and how to think about it when they were 18 or 19.
Fifteen years after *Beautiful Code*,
I still struggle to find examples of software architects discussing software architecture
with the same level of insight I would expect in an undergrad architect's term paper on Union Station
or an undergrad music student's analysis of Gershwin's "Rhapsody in Blue".

Stroustrup's *[Design and Evolution of C++](https://www.stroustrup.com/dne.html)*
Ierusalimschy et al's "[Implemenation of Lua 5.0](https://www.lua.org/doc/sblp2005.pdf)",
and Cooks [Gitlet](http://gitlet.maryrosecook.com/)
are proof that discussion of this kind is both possible and valuable at several levels;
(Go ahead: spend half an hour with [this page](http://gitlet.maryrosecook.com/docs/gitlet.html)—you
can thank me later.)
If I really had any influence on software engineering education,
every undergrad would read a couple of dozens essays like this in a third-year course
and write at least two.
As it is,
I'm just going to keep ranting from the sidelines and hope that some day,
somewhere,
better becomes normal.
