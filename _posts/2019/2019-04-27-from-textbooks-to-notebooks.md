---
date: 2019-04-27 08:33
year: 2019
title: "From Textbooks to Notebooks and Back"
---

I just converted [my introduction to R for Python programmers][tidynomicon]
from Jekyll to [bookdown][bookdown],
partly because I wanted to learn how bookdown works
but also because I think that computational notebooks are one of the futures of programming.
(We're a pretty big field, so I think we're going to have more than one.)

My question is, what kind of notebook would be best suited to teaching?
I think we can answer that by looking at how existing textbooks present code,
at what else they present,
and at what else people use when teaching.
Here are a few things I've done that I can't easily do with either R Markdown or Jupyter Notebooks:

1.  *Placeholders.*
    I often want to present the skeleton of a class with `...` markers for methods,
    then present those methods one by one with discussion interleaved.
    Knuth's original vision of literate programming supported this,
    but today's notebooks don't.

2.  *Incremental development.*
    So far as I know,
    I can't split the body of a single function across multiple code blocks in existing notebooks,
    but when I present code in something like *[JavaScript versus Data Science][js-vs-ds]*
    I often want to write a few lines of a function,
    explain what's going on,
    then write the next few lines and so on.

3.  *Diagrams*.
    Yeah, I know, I can draw something with an external tool,
    save the file,
    then link to that file in my notebook,
    but seriously:
    how long are we going to communicating with our multimedia supercomputers via punch cards?
    Good teaching materials use a wide variety of graphics,
    everyone else's tools allow drawings to be created and previewed in situ---let's have some of that in our notebooks.

4.  *Highlighting*.
    I can highlight <span style="background-color: #ffff33">this text</span> with three clicks in a WYSIWYG editor,
    or with 46 keystrokes in HTML.
    Highlighting a section of code in a notebook that I also want to run is painful;
    circling parts of the program and adding callouts *while leaving it runnable* is even worse,
    but these are things that good textbooks frequently do.

But I'm not asking for these features---not yet.
What I want now is for some enterprising graduate student to go through
a couple of  dozen highly-rated programming textbooks
and compile a list of how frequently different kinds of things are used.
This was part of what led me to [propose][sets-pep] that sets be added to Python:
I noticed that they were used over and over again in algorithms books
but weren't a first-class citizen of any major programming language.
Such a list could also help us compare notebooks and steer their future development.
If you're interested in taking this on,
please give me a shout---I'd welcome a chance to talk.

*By the way,
I think we ought to start calling computational notebooks "knuths"
in honor of the inventor of literate programming.
If anyone in our field deserves to have their name become a common noun,
I think he does.*

[bookdown]: https://bookdown.org/
[js-vs-ds]: https://software-tools-in-javascript.github.io/js-vs-ds/
[sets-pep]: https://www.python.org/dev/peps/pep-0218/
[tidynomicon]: https://gvwilson.github.io/tidynomicon/
