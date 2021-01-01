---
date: 2019-05-26 03:22
year: 2019
title: "LaTeX, Biber, and Pandoc"
---

I'm trying to get *[Teaching Tech Together](http://teachtogether.tech)* ready for publication.
The PDF is looking OK, but I'm struggling to get an HTML that I'm happy with, and I'm hoping someone can help.
My LaTeX file contains this:

```
\usepackage[backend=biber,style=alphabetic,sorting=nyt,maxbibnames=99]{biblatex}
\addbibresource{book.bib}
```

My BibTeX file contains entries like:

```
@inproceedings{Bacc2013,
  author = {Alberto Bacchelli and Christian Bird},
  title = {Expectations, Outcomes, and Challenges of Modern Code Review},
  booktitle = {2013 International Conference on Software Engineering ({ICSE'13})},
  year = {2013},
  month = {5},
  local = {bacchelli-2013-code-review.pdf},
  note = {A summary of work on code review.}
}
```

and I compile everything with:

```
$ pdflatex book.tex
$ biber book
$ pdflatex book.tex
$ pdflatex book.tex
```

Citations in the body of the PDF use the BibTeX key as the citation key:

```
Debugging depends on being able to read code, which multiple studies have
shown is the single most effective way to find bugs [Basi1987; Keme2009;
Bacc2013]. The code quality rubric developed in [Steg2014; Steg2016a], which is
online at [Steg2016b], is a good checklist of things to look for, though it is best
presented in chunks rather than all at once.
```

The bibliography uses the citation key as well, and includes the `note` field.
(I would rather it came after the date, but I'm trying not to ask for the moon.)

```
[Bacc2013] Alberto Bacchelli and Christian Bird. "Expectations, Outcomes, and
    Challenges of Modern Code Review". In: 2013 International Conference on
    Software Engineering (ICSE’13). A summary of work on code review. May 2013.
```

How can I replicate this with Pandoc?
My command line is:

```
$ pandoc -s --css=assets/bootstrap.css --css=assets/book.css --toc --toc-depth=2 \
  --template=template.html --bibliography=book.bib \
  -o index.html book.tex
```

where `template.html` is a copy of Pandoc's default HTML template lightly tweaked to use Bootstrap CSS.
I would like the resulting HTML to use the BibTeX citation key in both the body and the bibliography.
(I would also like citations to hyperlink to the bibliography entry,
and bibliography entries to include the note field, but one step at a time...)
What is the magic I'm looking for?

Note: source available in <https://github.com/gvwilson/teachtogether.tech/>
