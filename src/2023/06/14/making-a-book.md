---
title: "Making a Book"
date: 2023-06-13
---

Mike Hoye recently [tooted][toot]:

> The most common thing I want to say to GitHub projects is "Please use Make".
>
> It's old as dirt and the syntax isn't great,
> but even in its simplest use being able to reduce a wall of shell copypasta
> to "make whatever" is such a breath of fresh air. 
>
> Get yourself to where "install", "install-devenv", "build",
> and "run all my tests" are all dead easy,
> zero chaff,
> no typos simple.
> And if you find yourself re-using some long command chain,
> add it to the makefile and you're done. It is so good.

I strongly agree:
every project I'm on puts all of the commands someone might need to repeat
in a Makefile, an [Earthfile][earthly], or something else
that allows people to re-run chained commands with a few keystrokes
in a reliable, repeatable way.
Every one of those files also has a `make help` command (or equivalent)
so that people can easily find out what they're able to do.
That command's output for my current book project is shown below,
and I can't even guess how many hours of work I've saved
by *not* having to figure out how to do these things
a second, third, or N<sup>th</sup> time.

```
style        check source code style
---          ---
commands     show available commands
build        rebuild site without running server
serve        build site and run server
pdf          create PDF version of material
---          ---
lint         check project structure
inclusions   compare inclusions in prose and slides
examples     re-run examples
fonts        check fonts in diagrams
spelling     check spelling against known words
wordlist     make a list of unknown and unused words
---          ---
html         create single-page HTML
latex        create LaTeX document
pdf-once     create PDF document with a single compilation
diagrams     convert diagrams from SVG to PDF
---          ---
github       make root pages for GitHub
check        check source code
fix          fix source code
profile      profile compilation
clean        clean up stray files
---          ---
status       status of chapters
valid        run html5validator on generated files
vars         show variables
```

[earthly]: https://earthly.dev/
[toot]: https://mastodon.social/@mhoye/110544320436786292
