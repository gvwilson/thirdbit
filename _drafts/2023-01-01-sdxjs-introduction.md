---
title: "Introduction"
date: 2023-01-01
year: 2023
---

In the early 2000s,
the University of Toronto asked me to teach an undergraduate course on software architecture.
After delivering the course three times I told the university to cancel it
because of a lack of material:
I'd bought a dozen textbooks on the subject,
but between them,
they devoted a total of less than 30 pages to describing the designs of actual systems.

Frustrated by that,
Andy Oram and I persuaded some well-known programmers to contribute chapters
to a book called [*Beautiful Code*][bc].
Entries in the book described everything from figuring out whether three points are on a line
to core components of Linux
and the software for the Mars Rover,
but the breadth that made them fun to read
also meant they weren't particularly useful for teaching.

To fix that,
Amy Brown,
Tavish Armstrong,
Mike DiBernardo, and I
edited a four-book series between 2011 and 2016 called [*The Architecture of Open Source Applications*][aosa].
In the first two volumes,
the creators of fifty open source projects described their systems' designs;
the third book explored the performance of those systems,
while in the fourth volume contributors built scale models of common tools
as a way of demonstrating how those tools worked.
These books were closer to what an instructor would need for an undergraduate class on software design,
but still not quite right:

1.  Students would probably not be familiar with most of the problem domains,
    which would create a double cognitive burden.

2.  Since each author used the programming language of their choice,
    most students wouldn't be able to read most examples
    without even more work.

Twenty years on,
I think I've finally created what I wish I'd had then.
[*Software Design by Example: A Tool-Based Introduction with JavaScript*][sdxjs]
builds tiny versions of things like Git, Mocha, and the JavaScript VM
as a way of showing how experienced programmers think.
All the material is available under open licenses,
and all royalties from book sales go to support the [Red Door Family Shelter][red_door] in Toronto.

So who is this book for?

-   **Aïsha** started writing VB macros for Excel in an accounting course and never looked back.
    After spending three years doing front-end JavaScript work
    she now wants to learn how to build back-end applications.
    *SDXJS* will fill in some gaps in her programming knowledge
    and teach her some common design patterns.

-   **Rupinder** is studying computer science at college.
    He has learned a lot about the theory of algorithms,
    and while he uses Git and unit testing tools in his assignments,
    he doesn't feel he understands how they work.
    *SDXJS* will give him a better understanding of those tools
    and of how to design new ones.

-   **Yim** builds mobile apps for a living
    but also teaches two college courses:
    one on full-stack web development using JavaScript and Node
    and another titled "Software Design".
    They are happy with the former,
    but frustrated that so many books about the latter subject talk about it in the abstract
    and use examples that their students can't relate to.
    *SDXJS* will fill those gaps
    and give them starting points for a wide variety of course assignments.

I'm planning to blog about one chapter each week day during the month of January.
Feedback would be welcome;
while I've had to disable comments on this blog
(see the explanation in the footer of [my site's home page][third_bit]),
issues in [in the book's GitHub repository][book_repo] are always welcome.
I hope you find the material useful.

I am grateful to the creators of [diagrams.net][diagrams_net],
[Emacs][emacs],
[ESLint][eslint],
[Glosario][glosario],
[GNU Make][gnu_make],
[LaTeX][latex],
[Node][nodejs],
[NPM][npm],
[Standard JS][standard_js],
[SVG Screenshot][svg_screenshot],
[WAVE][webaim_wave],
and all the other open source tools used in creating these lessons:
if we all give a little,
we all get a lot.
I would also like to thank Darren McElligott, Evan Schultz, and [Juanan Pereira][pereira_juanan]
for their feedback;
any errors, omissions, or misunderstandings that remain are entirely my fault.

<div align="center">
  <img src="{{'/files/bib/sdxjs-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="40%" />
</div>

[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[ivy]: https://www.dmulholl.com/docs/ivy/dev/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[third_bit]: {{'/' | relative_url}}
[pereira_juanan]: https://ikasten.io/
[aosa]: https://aosabook.org/
[book_repo]: https://github.com/gvwilson/sdxjs/
[red_door]: https://www.reddoorshelter.ca/
[diagrams_net]: https://www.diagrams.net/
[emacs]: https://www.gnu.org/software/emacs/
[eslint]: https://eslint.org/
[glosario]: https://github.com/carpentries/glosario
[gnu_make]: https://www.gnu.org/software/make/
[latex]: https://www.latex-project.org/
[nodejs]: https://nodejs.org/en/
[npm]: https://www.npmjs.com/
[standard_js]: https://standardjs.com/
[svg_screenshot]: https://chrome.google.com/webstore/detail/svg-screenshot/nfakpcpmhhilkdpphcjgnokknpbpdllg
[webaim_wave]: https://wave.webaim.org/
