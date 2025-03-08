---
title: What We Mean by Software Design
date: 2025-03-08
---

Suppose you are building a static site generator that turns a bunch of Markdown files into HTML pages.
The Markdown files include links to external sites;
to ensure these are consistent between pages,
you have decided to do the following:

1.  All links to external sites are written as `[text][some_key]`.

2.  The keys and their associated URLs are stored in a YAML file like this:
    ```
    - key: first
      url: https://first.site
    - key: second
      url: https://second.site
    ```

3.  The static site generator reads the YAML file and converts the content to a block of text
    like the one shown below,
    then appends that text to each Markdown file in memory before translating to HTML:
    ```
    [first]: https://first.site
    [second]: https://second.site
    ```

Now comes the hard part.
Your static site generator includes a linting tool that checks for common mistakes,
such as improperly-nested headings or undefined bibliography references.
You want to check that every link reference corresponds to an entry in the YAML file
and that everyone entry in the YAML file is used at least once.
Your first attempt uses a regular expression to find patterns of the form `[some][url]` in the Markdown,
then does the obvious two-sided check with the URLs.
However,
your Markdown files also include snippets of Python code;
these may contain chained subscripts like `grid[x][y]`,
which cause your linter to produce spurious error reports.
What should you do?

1.  Implement some sort of "known problem" list to suppress the spurious error messages.

2.  Use regular expressions to erase code chunks from your Markdown files before searching for link references.

3.  Wait until the Markdown has been converted to HTML,
    then walk the DOM tree and check all the text that isn't in code chunks.

Solution #1 requires users to do extra work (and re-work as their content changes),
so let's set it aside.
It's easier to implement a first version of Solution #2 than of Solution #3,
but Solution #2 turns out to be surprisingly tricky to get right:
Markdown allows for indented code blocks,
and inline code sections might be marked with `<code>…</code>` rather than with single backticks.

I'm sure there are other solutions,
some of which may be better than the ones I've outlined,
but the point of this post is that when I say "software design",
what I mean is "answers to questions like these and the justifications behind them".
I wish there were more worked examples that discussed the pros and cons of possible solutions—I feel like
I still have a lot to learn.

[sdxpy]: https://third-bit.com/sdxpy/
