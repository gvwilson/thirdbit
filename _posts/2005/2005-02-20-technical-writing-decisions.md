---
title: "Technical Writing Decisions"
date: 2005-02-20 12:26:16
year: 2005
---
The <a href="http://www.python.org/psf">Python Software
Foundation</a> has given me a grant to open source my course on
software engineering for scientists and engineers.  I've been
consulting with several people on what the course's exact content
should be; the other issue I have to sort out before I start work is
its format.  The course will include:

-   point-form lecture notes that:
    -   lecturers can use in class
    -   students can skim through when they already know something about a topic
-   full-text explanations for people who ''don't'' know the topic, and won't be able to figure it out from point-form notes
-   images
    -   line drawings
    -   screen shots
-   programs
    -   The lecture notes and text will need to be able to refer to specific sections, either by callout (O'Reilly style—cleaner look, harder to engineer) or by line number
-   sample data files
-   "generated" files (e.g. program output)
    -   Must be able to re-generate all program output automatically
    -   Must also get a report if/when any of it changes, so that I can check back against the text
-   supporting code
    -   Makefiles (or the equivalent, if I use <a href="http://www.scons.org">SCons</a> or some other system)
    -   libraries and other big (often platform-specific) things

The question is, how to prepare, store, transform, and present all
of this?  I bring this up here because my students face many of the
same challenges every time they have to write a final report.  While
they don't need to mix slide content and prose side-by-side, they do
have to manage images, code fragments, and so on.

Lots of systems already exist that do some or all of what I want,
and new ones are appearing all the time.  (For example, <a href="http://www.meyerweb.com/eric/tools/s5">S5</a>, the Simple
Standards-Based Slide Show System, uses XHTML and JavaScript to create
a simple slide show.)  The problem I have is that I've used all of the
ones described below, and haven't been happy with any of them:

-   A (modified?) form of Wiki text as the source (so that it's easy to edit and diff)
    -   Generate slides and prose programmatically
    -   Use a simple CGI system to display pages in a browser while editing in order to check formatting
    -   Transform generated HTML/XML to create printable copy
-   LaTeX
    -   Already has grown-up production tools (don't need to invent any wheels!)
    -   Editing and diffing is harder than Wiki text (comparable to XML)
    -   Expressing formatting right (e.g. indentation of code samples in slide bullet points) is easier than with Wiki text
-   HTML
    -   Can view exactly what I'm writing…
    -   …except I don't want to: included code, point form vs. prose, etc.
    -   Can CSS take care of some of the display/view problems?
-   XML (home grown)
    -   Can provide exactly as much information as I need to
    -   Transformation is relatively straightforward
    -   Do I really want to build up my own tagset?
-   XML (borrowed from the Pragmatic Programmers)
    -   Don't know if they'd let me
    -   Doesn't handle slides
-   XML (DocBook or other)
    -   Overkill (esp. from an editing point of view)
    -   Don't know if it handles slides or not
-   WYSIWYG (Word, OpenOffice, etc.)
    -   Hard to process (e.g. extract slides to one fileset, prose to another, or insert/check code samples)

What else is there?  What have you used that helped make you productive?
