---
title: "Building a Ramp"
date: 2023-10-22
year: 2023
---

I've written, co-written, or edited [15 books][bib] over 32 years,
and have used a different authoring and publication pipeline each time.
My latest two books
(the [JavaScript][sdxjs] and [Python][sdxpy] versions of *Software Design by Example*)
use variations of the following:

1.  One sub-directory for each chapter.
2.  An `index.md` Markdown file in each sub-directory with the chapter's prose.
3.  Source code for examples (including tests and sample data) in multiple files in each sub-directory.
4.  Custom shortcodes in the Markdown files to include source files
    *or sections of source files* (about which more in a moment).
5.  [Ark][ark] to turn the whole mess into HTML.
6.  Some Python scripts to convert the HTML to LaTeX,
    from which I generate the PDF.

I really wanted to use [Jupyter notebooks][jupyter] or [Quarto][quarto],
but the emphasized part of point #4 defeated me.
If I write a class with a dozen methods,
I don't want to show the whole class at once.
I want to show a skeleton and then introduce the methods one by one or in small batches
with explanations interleaved,
but there doesn't appear to be a way to do this with today's notebooks.

Ideally,
I would put the entire class in a cell
and label that cell with a directive meaning,
"Show a skeleton instead of the entire code."
Other cells would be labeled with a pointer to the authoritative cell (e.g., its unique name)
and something indicating which portion of the cell to display
(preferably some kind of logical selector like `ClassName.MethodName` rather than line numbers,
because the latter *always* break as you're editing and revising).
The source would look something like this:

```
~~~{lang=python name=actual outline=true}
class Example:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self_name
~~~

The code in the cell above is hidden but runs when the file is run.
We can then have cells like this:

~~~{ref=actual selector=Example.__init__}
~~~

and this:

~~~{ref=actual selector=Example.get_name}
~~~

which are <strong>not</strong> run, but which are displayed.
```

and the rendered version would look something like this:

<blockquote>
<pre><code>
class Example:
    …__init__…
    …get_name…
</code></pre>

<p>
The code in the cell above is hidden but runs when the file is run.
We can then have cells like this:
</p>

<pre><code>
    def __init__(self, name):
        self._name = name
</code></pre>

<p>
and this:
</p>

<pre><code>
    def get_name(self):
        return self_name
</code></pre>

<p>
which are <em>not</em> run, but which are displayed.
</p>
</blockquote>

What I've done instead is put the runnable copy of the code in an external file
and use the aforementioned shortcodes to select the chunks I want.
This works,
but is a perpetual source of friction when doing updates.
It also perpetuates an either/or distinction between noodling around in a notebook
and building a robust application.
I think a system like the one sketched above would solve both problems:
the runnable code and its accompanying explanation would be in one file,
and authors could freely mix the kind of exploratory code notebooks are best at
with longer-form application code.

[ark]: https://www.dmulholl.com/docs/ark/main/
[bib]: {{'/bib/' | relative_url}}
[jupyter]: https://jupyter.org/
[quarto]: https://quarto.org/
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxpy]: {{'/sdxpy/' | relative_url}}
