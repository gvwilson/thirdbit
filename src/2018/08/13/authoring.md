---
date: 2018-08-13
title: "Authoring"
category: favorite
---

In the beginning was the finger, and paint, and the wall of the cave.
Whoever painted the first pictures this way could create whatever they wanted—the medium
allowed them to create anything they could imagine.
So did pens and paper:
pictures and text could be arranged on the page
however the author wanted.

The first printing presses didn't change this.
They made impressions from woodblock carvings,
which still allowed authors to put whatever they wanted wherever they wanted it.
But then,
around 1370,
craftsmen in Korea invented movable type.
It spread like wildfire after Gutenberg and others reinvented it in the 1440s,
and humanity's long fall from written grace began.

While movable type allowed printers to set pages
many times more quickly than carvers could produce woodblocks,
the cost was flexibility:
where scribes could draw anywhere on the page,
typesetters had to put letters of uniform size in rows.
And while diagrams were still possible,
the lowered cost of words made them relatively many times more expensive than they had been.

The typewriter (invented in the 1860s) put "printing" in millions of middle-class hands.
Mechanical, electrical, and then electronic computers all re-used typewriter technology
to print their output.
When the first pen plotters appeared in the 1950s,
they were too slow and too expensive to displace line printers.
What's more,
the two technologies didn't work well together:
it's possible to draw pictures using ASCII art,
or to write letters with a pen plotter,
but neither is particularly attractive.

One sign of this gap between tools meant for words and tools meant for pictures
was the development of separate languages for controlling them.
Plotters were typically controlled by *drawing languages* that had commands to say,
"Pen up,
move to this (x,y) location,
pen down,
and move again."

~~~
PU;
PA200,150;
PD;
PA250,250;
~~~

*Typesetting languages* for line printers,
on the other hand,
let authors tell the computer to lay out a phrase as a second-level heading
or set certain words in italics,
but it was then the computer's job to determine
where things would go and what they would look like:

~~~
.t2 Section Heading

Empty lines separate
.it paragraphs
and lines starting with '.' are commands.
~~~

A third kind of language emerged in this period as well,
one meant to describe the *content* of a document rather than its *appearance*.
Doctors and lawyers wanted to be able to search patient histories and precedents,
but the computers of the time weren't powerful enough to handle natural language.
Instead,
companies like IBM developed *markup languages*
so that people could make the meaning, or *semantics*, of their documents explicit:

~~~
<person>Derstmann</person> still questions the importance of <chemical>methane</chemical> release
in <event>the Fukuyama disaster</event>.
~~~

These worlds collided after the invention of the laser printer in the 1970s,
and that tension was only magnified by high-resolution computer screens in the 1980s
and the World Wide Web in the 1990s.
On the one hand,
most people simply want to write—to put these words here and those words there,
or make some of them green and others italic.
WYSIWIG (what you see is what you get) editors like MacWrite and Microsoft Word fill this need,
but documents produced this way have two shortcomings:

1.  They are *rigid*.
    If someone lays things out manually,
    then changes the size of the page,
    their hard work must be re-done.

2.  They are *opaque*.
    Telling the computer to display something in italics
    doesn't tell it whether that phrase is a book title,
    in a foreign language,
    or defining a new term.

Typesetting and markup languages address both problems.
Instead of saying what things should look like and where they should go on the page,
authors are supposed to tell the computer what kinds of things they are,
e.g., a title or a new term.
The computer is then supposed to decide what it should look like and where it should go.
Separating semantics and appearance in this way also allows people to switch styles easily and consistently
by telling the computer,
"Typeset all second-level headings in 16-point Garamond, left-aligned."

But this approach also has shortcomings:

1.  Computers don't always lay out text the way human beings would
    because they don't understand it.
    People have therefore always insisted on being able to override the computer's choices,
    even though it re-introduces rigidity.

2.  Specifying their documents' semantics seems alien to most people,
    and much more work than just enlarging the title a few times.

3.  Interpreting what the user typed in and figuring out what to display takes the computer time.
    Figuring out why the document doesn't look like it ought to takes the person even more time;
    it's exactly like debugging a program,
    and debugging is frustrating.

No-one has invented something that avoids all of these problems,
so today's researchers have a confusing variety of choices when it comes to writing their reports:

1.  A desktop WYSIWYG tool like Microsoft Word or LibreOffice (both of which work with the `.docx` format).
    This is by far the easiest way to create simple things like letters,
    but it is rigid and opaque,
    has poor support for laying out equations,
    and doesn't work well with version control systems (discussed below).

2.  A web-based WYSIWYG tool like Google Docs.
    This has the immediacy of Word or LibreOffice,
    and makes collaboration easier
    (since everyone shares one copy of the document).
    It is still rigid and opaque,
    though,
    and a growing number of people are uncomfortable with putting all their eggs
    in an unaccountable private company's basket.

3.  LaTeX on the desktop.
    This powerful typesetting language has excellent support for equations and bibliographies.
    It also works well with version control,
    since documents are written as plain text.
    However,
    it is by far the most complex to learn,
    and getting things laid out exactly as desired can take many painful hours.

4.  Web-based tools like Authorea and Overleaf
    offer users a WYSIWYG editing interface
    but store documents as LaTeX
    and re-display them in real time as changes are typed in.
    Like all WYSIWYG-on-a-substrate approaches, this works as long as you are careful to stay inside the sandbox.

5.  HTML.
    The native language of the web is much simpler than LaTeX,
    but also does much less:
    even simple things like footnotes, bibliographic references, and numbered sections aren't directly supported.
    It can also be quite verbose,
    and CSS
    (the language used to tell browsers how to display HTML)
    is famously quirky.

6.  Markdown was created as a simple alternative to HTML.
    It uses the conventions of plain-text email:
    blank lines separate paragraphs,
    putting something in `*asterisks*` makes it italic,
    and so on.
    It does less than HTML,
    but also requires less typing.
    Unfortunately,
    though,
    almost every implementation adds its own features,
    so "standard Markdown" is an oxymoron.

The division between WYSIWYG on the one hand and typesetting and markup on the other
has more to do with tools than formats.
A `.docx` file actually contains a mix of typesetting commands and text,
just like a LaTeX, HTML, or Markdown file.
The difference is that the commands in the latter are stored as human-readable text,
which means that the standard Unix command-line utilities can process them
(though as [this comment on Stack Overflow][html-regexp] indicates,
there are limits to how much they can actually do).
In contrast,
the formatting instructions embedded in Microsoft Word and LibreOffice
are created by and for specific special-purpose programs,
so plain-text tools like `grep` can't handle them.

The same is true of Google Docs:
formatting instructions are embedded in the document,
then executed by Javascript running in the user's browser
to create the rendered page that the user interacts with.
Authorea and Overleaf do the same thing,
except their storage format is LaTeX.

Hard-core programmers may sneer at WYSIWYG tools and their non-textual formats,
but their feet are made of clay.
Microsoft Word has been around for three decades;
its document format has changed several times in those years,
but there has still been plenty of time for command-line aficionados
to adapt their favored tools to handle it.
That hasn't happened, though,
which means that most version control systems still can't handle
the most widely-used documents formats in the world:
when confronted with two different version of a Microsoft Word file,
all Git and its kin can say is, "Difference detected."
The net effect is that
anyone who wants to adopt version control
has to abandon the tools that they and their colleagues have used productively for years
in the hope of greater productivity at some future date.

The discussion above has assumed that authors are creating letters and papers,
but researchers also frequently need to create posters and slides to present their work.
PowerPoint is the undisputed queen of presentation tools;
while many people have critiqued it,
blaming PowerPoint for bad presentations is like blaming fountain pens for bad poetry.
PowerPoint and its imitators make it easy for people to use their computer's screen as if it was a whiteboard.
Yes,
they can create mind-numbing pages of bullet-point lists if they choose,
but they can also freely *and easily* mix images, diagrams, and text.
LaTeX and HTML can do this,
but neither makes it easy.
In fact,
it's so hard in both that most people don't bother.
Even when they do,
the graphical elements are external foreign inserts
rather than integral parts of the document.

All this leaves me in an uncomfortable situation
as I try to write a lesson on how to write up research in the early 21st Century.
On the one hand,
papers and presentations are integral parts of research projects,
and should be tracked and shared just like code and data.
On the other hand,
as Stephen Turner said:

> …try to explain the notion of compiling a document to an overworked physician you collaborate with.
> Oh, but before that, you have to explain the difference between plain text and word processing.
> And text editors.
> And Markdown/LaTeX compilers.
> And BiBTeX.
> And Git.
> And GitHub. Etc.
> Meanwhile he/she is getting paged from the OR…
>
> …as much as we want to convince ourselves otherwise,
> when you have to collaborate with those outside the scientific computing bubble,
> the barrier to collaborating on papers in this framework is simply too high to overcome.
> Good intentions aside,
> it always comes down to "just give me a Word document with tracked changes," or similar.
{: .quotation}

For the foreseeable future,
many researchers will therefore continue to use WYSIWYG editors
(and their associated formats)
rather than switch to pure-text typesetting tools.
Hybrid systems like Authorea and Overleaf may turn this cliff into a ramp,
but until programmers have the decency to handle the document formats that the other 99% of the human race prefers,
we have to choose between small things being simple and big things being possible.

Personally,
I use Markdown for websites and blogs,
HTML when I need more control (for example, to create a complex table),
and LaTeX for manuscripts.
I rely on GitHub Pages to translate Markdown into something people can read online,
and Pandoc to turn it into something worth printing.
Since I've never made the time to master Pandoc templating,
I usually wind up writing a couple of pre- and post-processing scripts in Python
to clean up what I'm feeding it
and then clean up its output.
(Why *does* it insist on putting `<span>` tags in odd places?)
It works,
but only in the sense that English has grammar
or markets are efficient.
One day,
I hope,
I'll have something better to teach.

[html-regexp]: https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454
