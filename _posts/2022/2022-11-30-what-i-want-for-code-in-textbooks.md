---
title: "What I Want for Code in Textbooks"
date: 2022-11-30
year: 2022
---

Regular readers will know that
I find the tools we have for authoring long-form explanations of code
very frustrating.
I've used LaTeX (both desktop and online), RMarkdown, Jupyter Notebooks, Microsoft Word, Google Docs,
and a variety of lesser-known Markdown-based tools,
and they all make simple things hard.

For example,
suppose I want to include a snippet of code in an explanation—not an entire class or function,
but just a few lines or a method.
I can't do this with computational notebooks:
so far as I can tell,
they all require cells to be runnable as-is,
which means I can't have just a few key lines from the middle of a function
or one method from the middle of a class.
Similarly,
suppose I want to show a class with placeholder ellipses instead of the method bodies
so that readers can get an overview of what's where
before we dive into specifics.
Again,
the tools that let me run code in situ don't allow this.

<img src="{{'/files/2022/code-inclusions.svg' | relative_url}}" alt="code inclusions" class="centered">

Authors therefore wind up hacking together code scrapers
that (for example) look for markers and directives in source code files
and copy ranges of code during document compilation.
This approach leads to code like that shown below,
which is unpleasant to read
if you're trying to single-step through it in a debugger,
and which is usually made even more complicated by extra directives
to suppress warning messages from linting tools:

```
# [range key="class" elide=true]
class Example:
    MARKERS = {"[", "]"}

    def __init__(self, filler):
        self._filler = filler

    # [range key="revise"]
    def revise(self, contents):
        end = None
        for (i, val) in enumerate(contents):
            if self.spans(val):
                if (end is None) or (i > end):
                    end = i
        return end
    # [/range]

    def spans(self, value):
        return self._filler(value) in self.MARKERS
# [/range]
```

So what do I want?

1.  I want a plugin for [pick your favorite IDE—I'll switch to it if you offer this feature]
    that allows me to select a range of lines in a source code file
    and add an annotation on them
    that is stored outside the source file
    in the same way that reviewers' comments in Microsoft Word or Google Docs
    are stored beside the main text.

2.  I also want a counterpart plugin for the IDE
    that allows me to put a marker in a text file that says,
    "Find the annotation with this label
    and display the selected range of lines right here, right now."
    I don't want to have to go through a compilation step in order to see those lines
    (not even one that runs continuously in the background);
    I want actual fragment transclusion in real time.

3.  And yes,
    users should be able to jump from the transcluded fragment
    to the original source file
    and run things,
    or better yet,
    click a button to open the entire runnable program
    beside the text that displays the fragment
    so that they can step through that bit of code
    with the explanatory text beside it.

Once we have that,
I want to be able to apply it to diagrams
to transclude a portion of a larger diagram
so that I can explain parts of the whole
without trying to keep half-a-dozen SVG's in sync with each other.
Before then,
though,
I'd like to be able to drive this in the opposite direction.
If I'm viewing the code,
whatever's displaying it should automatically point to the relevant explanations,
because that's what I'd do if I was coding in a classroom
with some explanations on slides on another screen
or some diagrams on a whiteboard beside me:

<img src="{{'/files/2022/code-references.svg' | relative_url}}" alt="code references" class="centered">

It's all technically feasible,
particularly if someone wants to leverage an existing platform like VSCode.
I don't expect to see it in my working lifetime,
but I do still hope that programming will some day free itself
from backward compatibility with punchcards
and all the misery that antiquated constraint causes.
