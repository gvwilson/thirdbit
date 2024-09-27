---
title: "Software Design by Example in Python 1: Introduction"
date: 2024-04-01
---

In the early 2000s,
the University of Toronto asked me to teach an undergraduate course on software architecture.
After three runs I told the university to cancel it because of a lack of material:
I'd bought a dozen textbooks on the subject,
but between them,
they devoted a total of less than 30 pages to describing the designs of actual systems.

Frustrated by that,
Andy Oram and I persuaded some well-known programmers to contribute chapters
to a book called [*Beautiful Code*][bc].
Entries described everything from figuring out whether three points are on a line
to the ground station software for the Mars Rover,
but the breadth that made them fun to read
also meant they weren't particularly useful for teaching.

Amy Brown, Tavish Armstrong, Mike Dibernardo, and I
then edited a four-book series called [*The Architecture of Open Source Applications*][aosa]
in which the creators of various open source projects described their systems' designs.
These books were closer to what a junior programmer would need,
but each author used the programming language of their choice
and most people still wouldn't be familiar with most of the problem domains.

So last year I published
[*Software Design by Example: A Tool-Based Introduction with JavaScript*][sdxjs],
which I think is finally the book I needed twenty years ago.
This year I'm proud to announce the sequel:
[*Software Design by Example: A Tool-Based Introduction with Python*][sdxpy].
In it,
I build tiny versions of Git, pytest, the Python VM, and other tools
to show how they work
and how experienced programmers think about software design.

I had two [learner personas][t3_personas] in mind as I wrote this book.
The first is a student:

> *Maya has a master's degree in genomics.
> She knows enough Python to analyze data from her experiments,
> but struggles to write code other people can use.
> These lessons will show her how to design, build, and test large programs
> in less time and with less pain.*
> {: .continue}

The other is the instructor I was twenty years ago:

> *Yim teaches two college courses on software development.
> They are frustrated that so many books talk about details but not about design
> and use examples that their students can't relate to.
> This book will give them material they can use in class
> and starting points for course projects.*
> {: .continue}

As with its predecessor,
all the material from *SDXPY* is available under open licenses,
and all royalties from book sales go to support the [Red Door Family Shelter][red_door] in Toronto.

I hope to blog about one chapter each day for the next few weeks.
Feedback is always welcome;
while I've had to disable comments on this blog because of trolls,
you can file issues in [in the book's GitHub repository][book_repo].
I hope you find the material useful,
and I'm happy to answer questions [by email](mailto:gvwilson@third-bit.com).

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

I am grateful to the creators of [diagrams.net][diagrams_net],
[Black][black],
[Emacs][emacs],
[flake8][flake8],
[Glosario][glosario],
[GNU Make][gnu_make],
[isort][isort],
[LaTeX][latex],
[pip][pip],
[Python][python],
[Remark][remark],
[WAVE][webaim_wave],
and all the other open source tools used in creating these lessons:
if we all give a little,
we all get a lot.
I would also like to thank everyone who took part in last year's beta testing for early and ongoing feedback,
especially [Alberto Bacchelli][bacchelli_alberto] and his students.
Any errors, omissions, or misunderstandings that remain are entirely my fault.

[aosa]: https://aosabook.org/
[ark]: https://www.dmulholl.com/docs/ark/main/
[bacchelli_alberto]: https://sback.it/
[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[black]: https://black.readthedocs.io/
[book_repo]: https://github.com/gvwilson/sdxpy/
[diagrams_net]: https://www.diagrams.net/
[emacs]: https://www.gnu.org/software/emacs/
[flake8]: https://flake8.pycqa.org/
[glosario]: https://github.com/carpentries/glosario
[gnu_make]: https://www.gnu.org/software/make/
[isort]: https://pycqa.github.io/isort/
[latex]: https://www.latex-project.org/
[pip]: https://pip.pypa.io/
[python]: https://www.python.org/
[red_door]: https://www.reddoorshelter.ca/
[remark]: https://remarkjs.com/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[t3_personas]: https://teachtogether.tech/en/index.html#s:process-personas
[third_bit]: @root/
[webaim_wave]: https://wave.webaim.org/
