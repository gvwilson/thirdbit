---
date: 2019-03-10 11:59
title: "The Tool I Want"
---

We talk about "programming" as if there was just one kind,
but in the past three months I have:

1.  written, refactored, and tested tools
    that will be used by people I've never met
    in situations I haven't envisaged;

2.  explored complex data
    by extending and revising a mixture of prose and code,
    guided at each step by what I've learned from what I've done so far;
    and

3.  created tutorials that present both small self-contained programs
    and fragments from several revisions of larger ones.

We've had good solutions for the first use case for decades,
and dynamic documents like [R Markdown](https://rmarkdown.rstudio.com/),
the [Jupyter Notebook](https://jupyter.org/),
and [Stencila](https://stenci.la/)
have pretty much taken care of the second,
at least for desktop-scale work.

But what about the third case?
Dynamic documents are great for showing short pieces of code and their output,
and all of the tools listed above can generate slides with a little extra work,
but I'm still not satisfied:

1.  I often want to have the full runnable code in the document,
    but elide sections when displaying it.
    For example,
    the runnable version of this code is about 40 lines long,
    but what I want to display for tutorial purposes is:

    ```js
    // ...as before...

    app.use((req, res, next) => {
      const actual = path.join(root, req.url)
      if (actual.endsWith('.json')) {
        // ...parse file and set content type before returning...
      }
      else {
        // ...read file and return directly...
      }
    })
    ```

    The gotcha is that I also want to display different fragments of the same piece of code in sequence,
    so that (for example)
    I can expand the second elision above to show the body of the `if`:

    ```js
      if (actual.endsWith('.json')) {
        const data = fs.readFileSync(actual, 'utf-8')
        const json = JSON.parse(data)
        res.setHeader('Content-Type', 'application/json')
        res.status(200).send(json)
      }
    ```

    I really, really don't want to duplicate any of this code;
    instead,
    I want to slice and dice one copy of the code in different ways
    at different points in my exposition.
    Knuth's [original description of literate programming](http://www.literateprogramming.com/knuthweb.pdf)
    allowed for partial and out-of-order exposition,
    but today's systems don't,
    since it's mostly not needed for production code or analysis.

2.  Dynamic documents provide excellent support for charts
    (by which I mean programmatically-generated data visualizations),
    but they provide no support at all for diagrams
    (by which I meant explanatory graphics created manually).
    You can create these by switching to another tool,
    drawing what you want,
    and linking to that image file,
    but that's a pretty awkward workflow---awkward enough that
    most people either create fewer diagrams than cognitive science tells us we should
    or create their presentations with slideshow tools like Keynote and PowerPoint
    that put drawing and writing on a more equal footing.
    Given that all of the dynamic document tools I mentioned earlier can display images inline,
    it would be a simple matter of programming [tm] to embed or launch something like [draw.io](https://www.draw.io/)
    for editing in situ.
    This wouldn't do everything that slideshow tools can do,
    but it would still be a big step in the right direction.

3.  I've been ranting for years about the fact that
    version control tools can't diff and merge any format except lines of text,
    which makes them effectively useless for managing spreadsheets,
    images,
    rich text documents,
    PDFs,
    and everything else that programmers have created to make everyone's life easier.
    I won't repeat that rant now,
    but bloody hell, folks,
    it's 2019!
    Surely we can---sorry,
    sorry,
    you're right,
    I said I wouldn't.
    (I'm not yet at the point of advocating widespread re-adoption of ASCII art
    as a solution for this one and the one above,
    but the thought *has* crossed my mind.)

Years ago,
I said that programmers' tools hadn't changed since I was a grad student.
[Peggy Storey](http://margaretstorey.com/) corrected me:
Stack Overflow and other Q&A sites have changed the act of programming in fundamental ways.
Dynamic documents have had a similar impact on data analysis;
I think that with a few enhancements,
they could do the same for teaching,
and that's a pretty exciting idea.
Now we just have to figure out how to combine them with blocks-based programming...
