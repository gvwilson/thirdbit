---
layout: post
date: 2018-10-24 01:15
title: "Two Columns"
---

I'm spending a few minutes every morning adding prose to the point-form notes in
[JavaScript versus Data Science](https://software-tools-in-javascript.github.io/js-vs-ds/en/).
My goal is to have a single document that contains both
the slides someone would use when teaching in a classroom
and the text that someone would read on their own,
all in step,
*without* duplicating code samples or images or the like.
It's proving frustrating,
because what I find I really want to do is this:

    +----------------------------------+
    |            diagram               |
    +---------------+------------------+
    | - point       | Paragraph saying |
    | - point       | the same things  |
    |   - sub-point | in sentences.    |
    +---------------+------------------+
    | ```js                            |
    | ...code...                       |
    | ```                              |
    +----------------------------------+
    | - point       | Paragraph saying |
    | - point       | the same things  |
    |   - sub-point | in sentences.    |
    +---------------+------------------+

I.e.,
I want to see the point-form notes and the paragraphs of text side by side *while I'm editing*,
with the diagrams and code fragments being described and discussed spanning both columns.
It seems like a simple thing,
but none of the editors I have will do this satisfactorily:
they will let me add classes to divs so that my Markdown or HTML *renders* like this,
or put the prose in the speaker's notes section of my reveal.js slides,
but a side-by-side view as I'm typing would make it much easier for me to keep things in sync
(just as putting documentation *in* code has made it easier for programmers to keep them in step with each other).

I could use tables or two-column mode in Word or Google Docs,
but they don't play nicely with version control,
which is a must-have for me.
It's frustrating that I can't easily style my editing interface
in the way that I would style a web page.
And yes,
I'm sure there's an Emacs mode for this,
but "you must use Emacs to edit this file" feels [rude](http://b.z19r.com/post/did-you-just-tell-me-to-go-fuck-myself).
