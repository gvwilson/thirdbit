---
title: "Using Jekyll for Lessons"
date: 2015-06-24
original: swc
---
<p>
  A recurring complaint about our lesson template
  is that it requires authors to commit generated HTML files to their repositories
  as well as their Markdown source files.
  This is necessary because we use <a href="http://pandoc.org">Pandoc</a> to convert Markdown to HTML,
  but GitHub will only run <a href="http://jekyllrb.com/">Jekyll</a>.
</p>
<p>
  There were a bunch of reasons for using Pandoc instead of Jekyll,
  but it is now clear that the simplicity of only committing Markdown–i.e.,
  of using GitHub pages the way they're meant to be used–is more important.
  We have therefore created a prototype of a Jekyll-based template.
  The most important changes are:
</p>
<ul>
  <li>
    <p>
      Only the source Markdown files go into the repository's <code>gh-pages</code> branch,
      <em>not</em> the generated HTML
    </p>
  </li>
  <li>
    <p>
      The lesson's title, repository URL, and other values are defined once
      in a configuration file called <code>_config.yml</code>.
    </p>
  </li>
  <li>
    <p>
      Blockquotes are styled like this:
    </p>
<pre>
> ## Title
>
> body
{: .style}
</pre>
    <p>
      instead of like this:
    </p>
<pre>
> ## Title {.style}
>
> body
</pre>
    <p>
      Code blocks are styled similarly,
      i.e.,
      with the style <em>after</em> the block instead of at the top.
    </p>
  </li>
</ul>
<p>
  People using source formats other than Markdown,
  such as R Markdown or Jupyter Notebooks,
  will still need to convert their files to plain old Markdown
  (styled as shown above)
  in order for them to be rendered properly by Jekyll.
  And we'll need to upgrade the format checking script,
  which means finding a Kramdown-compatible parser in Python
  (or getting Kramdown to spit out its AST as a data structure
  that a Python program can consume).
  But most of these things have to be done anyway,
  and it seems that most of our contributors think they're a price worth paying
  for a "real" GitHub Pages experience.
</p>
<p>
  If you think the change is worth making,
  please say so in <strike>the comments below</strike>
  this GitHub issue.
  If you think we should stick with our existing tools,
  please say that too.
</p>
<p>
  Postscript:
  many people have said they want the change,
  largly because it brings us in line with the standard GitHub Pages workflow
  (which Data Carpentry is using).
  Several others have counter-arguments,
  some of which are in 
  this thread
  from our discussion list.
  In particular,
  please read:
</p>
<ul>
  <li>
    <p>
      this post
      from John Blischak about us having come full circle,
      and about us putting time into tooling that we should be putting into creating lesson content;
    </p>
  </li>
  <li>
    <p>
      this one
      from Doug Latornell about re-mixing our current Pandoc-based workflow; and
    </p>
  </li>
  <li>
    <p>
      this one
      from Carl Boettiger about Markdown syntax.
    </p>
  </li>
</ul>
<p>
  <em>
    We are grateful to <a href="http://brittanyhemming.com/">Brittany Hemming</a>
    for her work on the CSS for this prototype,
    and to <a href="http://www.mat.univie.ac.at/~leitner/">Thomas Leitner</a>
    for advice on Kramdown's Markdown parsing.
  </em>
</p>
