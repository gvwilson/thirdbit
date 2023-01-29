---
title: "Problems with Pandoc"
date: 2013-06-13 18:48:09
year: 2013
---
People have been asking me to write the Software Carpentry instructor's guide in Markdown instead of HTML, mostly so that it will be easier for other people to review and contribute. I was initially against the idea because standard Markdown lacks so many features that I'd basically be writing HTML with back quotes instead of &lt;code&gt; tags, but it turns out that Pandoc's variation on Markdown provides a lot of what I want–a lot, but not all. After converting the section on databases, I've come up against the following.

1) Pandoc won't number figures and insert those numbers in references. I can do this by inserting \label{...}'s and \ref{...}'s if my target format is LaTeX, but I want HTML.

2) There's no way to attach a CSS class to a table. I can do this to a heading by writing:

```
### Heading Title {.some-style}
```

but the curly-brace syntax doesn't work with tables. I want to do this so that I can display the output of SQL queries as HTML tables, but style them in a particular way.

3) I can't put styling information inside a pre-formatted code block. I frequently want to show a snippet of code, then show it again with some minor changes highlighted. Using HTML, I do this as:

```
the original &lt;span class="highlight"&gt;and the changes&lt;/span&gt;
```

but if I do that inside an indented (pre-formatted) block, it's rendered literally.

4) Most of the major sections in each chapter open with instructors' notes. As pure HTML, this looks like:

```
&lt;section&gt;
  &lt;h2&gt;Section Heading&lt;/h2&gt;

  &lt;div class="guide"&gt;
    &lt;h3&gt;For Instructors&lt;/h3&gt;
    &lt;p&gt;A hundred lines of guidance go here...&lt;/p&gt;
  &lt;/div&gt;

  &lt;p&gt;...and several hundred lines of lesson go here.&lt;/p&gt;
&lt;/section&gt;
```

Now, if I use the `--section-divs` flag, Pandoc will guess where sections begin and end based on uses of `h1`, `h2`, etc., and wrap them in `div`'s (which is good). However, if I give it this:

```
## Section Heading

### For Instructors

A hundred lines of guidance go here...

...and several hundred lines of lesson go here.
```

it (quite naturally) guesses wrong about where the `div`'s should go. For now, I'm putting the instructors' material in a quotation block, but I'd rather do this properly if I can.

I can get around all of these problems by writing raw HTML instead of Markdown, but the result isn't any more readable to me than pure HTML. I'd welcome other suggestions, or offers of help.
