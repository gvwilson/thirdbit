---
title: "Software Design by Example 1: Introduction"
date: 2023-01-01
year: 2023
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

To fix that,
Amy Brown and I
(and later Tavish Armstrong and Mike DiBernardo)
edited a four-book series called [*The Architecture of Open Source Applications*][aosa].
In the first two volumes,
the creators of fifty open source projects described their systems' designs;
the third book explored the performance of those systems,
while contributors to the fourth built scale models of common tools
to demonstrate how real ones worked.

These books were closer to what an instructor would need for an undergrad class on software design,
but still not quite right.
Students wouldn't be familiar with most of the problem domains,
and since each author used the programming language of their choice,
most students wouldn't be able to read most examples.
"They'll get the sense of it" misses the point:
discussion and critique of design often hinges on small details,
so anything that distracts readers from seeing those details inhibits learning.

So here we are in 2023,
and I think I've finally created what I wanted twenty years ago.
[*Software Design by Example: A Tool-Based Introduction with JavaScript*][sdxjs]
builds tiny versions of Git, Mocha, the JavaScript VM, and other tools
in order to show how they work,
but more importantly,
to show how experienced programmers think about software design.
All the material is available under open licenses,
and all royalties from book sales go to support the [Red Door Family Shelter][red_door] in Toronto.

I had three [learner personas][t3_personas] in mind as I wrote:

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

I hope to blog about one chapter each week day in January.
Feedback is always welcome;
while I've had to disable comments on this blog
(see the explanation in the footer of [my site's home page][third_bit]),
you can file issues in [in the book's GitHub repository][book_repo].
I hope you find the material useful,
and I'm happy to answer questions [by email][contact].

<div align="center">
  <img src="{{'/sdxjs/sdxjs-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="40%" />
</div>

> I am grateful to the creators of [diagrams.net][diagrams_net],
> [Emacs][emacs],
> [ESLint][eslint],
> [Glosario][glosario],
> [GNU Make][gnu_make],
> [LaTeX][latex],
> [Node][nodejs],
> [NPM][npm],
> [Standard JS][standard_js],
> [SVG Screenshot][svg_screenshot],
> [WAVE][webaim_wave],
> and all the other open source tools used in creating these lessons:
> if we all give a little,
> we all get a lot.
> I would also like to thank Darren McElligott, Evan Schultz, and [Juanan Pereira][pereira_juanan]
> for early and ongoing feedback;
> any errors, omissions, or misunderstandings that remain are entirely my fault.

Notes:

1.  Each post in this series contains a list of the terms defined in the corresponding chapter.
    In my experience, a list like this is the quickest way to get a reliable overview
    of what a lesson is about.
    You can find the corresponding definitions in [the book's glossary][sdxjs_glossary].

2.  I'm translating this book into Python, and adding a few more examples along the way.
    If you'd like to give early feedback on that material, please [reach out][contact].

[aosa]: https://aosabook.org/
[bc]: https://www.oreilly.com/library/view/beautiful-code/9780596510046/
[book_repo]: https://github.com/gvwilson/sdxjs/
[contact]: mailto:{{site.author.email}}
[diagrams_net]: https://www.diagrams.net/
[emacs]: https://www.gnu.org/software/emacs/
[eslint]: https://eslint.org/
[glosario]: https://github.com/carpentries/glosario
[gnu_make]: https://www.gnu.org/software/make/
[ivy]: https://www.dmulholl.com/docs/ivy/dev/
[latex]: https://www.latex-project.org/
[nodejs]: https://nodejs.org/en/
[npm]: https://www.npmjs.com/
[pereira_juanan]: https://ikasten.io/
[red_door]: https://www.reddoorshelter.ca/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_glossary]: {{'/sdxjs/glossary/' | relative_url}}
[standard_js]: https://standardjs.com/
[svg_screenshot]: https://chrome.google.com/webstore/detail/svg-screenshot/nfakpcpmhhilkdpphcjgnokknpbpdllg
[t3_personas]: https://teachtogether.tech/en/index.html#s:process-personas
[third_bit]: {{'/' | relative_url}}
[webaim_wave]: https://wave.webaim.org/
