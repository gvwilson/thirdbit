---
title: "Technical Writing Decisions"
date: 2005-02-20 12:26:16
year: 2005
---
<p>The <a href="http://www.python.org/psf">Python Software
Foundation</a> has given me a grant to open source my course on
software engineering for scientists and engineers.  I've been
consulting with several people on what the course's exact content
should be; the other issue I have to sort out before I start work is
its format.  The course will include:</p>

<ul>
<li>point-form lecture notes that:
  <ul>
  <li>lecturers can use in class</li>
  <li>students can skim through when they already know something about
  a topic
  </ul>
</li>
<li>full-text explanations for people who ''don't'' know the topic,
and won't be able to figure it out from point-form notes</li>
<li>images
  <ul>
  <li>line drawings</li>
  <li>screen shots</li>
  </ul>
</li>
<li>programs
  <ul>
  <li>The lecture notes and text will need to be able to refer to
  specific sections, either by callout (O'Reilly style—cleaner look,
  harder to engineer) or by line number</li>
</ul>
<li>sample data files</li>
<li>"generated" files (e.g. program output)
  <ul>
  <li>Must be able to re-generate all program output
  automatically</li>
  <li>Must also get a report if/when any of it changes, so that I can
  check back against the text</li>
  </ul>
</li>
<li>supporting code
  <ul>
  <li>Makefiles (or the equivalent, if I use <a href="http://www.scons.org">SCons</a> or some other system)</li>
  <li>libraries and other big (often platform-specific) things</li>
  </ul>
</li>
</ul>

<p>The question is, how to prepare, store, transform, and present all
of this?  I bring this up here because my students face many of the
same challenges every time they have to write a final report.  While
they don't need to mix slide content and prose side-by-side, they do
have to manage images, code fragments, and so on.</p>

<p>Lots of systems already exist that do some or all of what I want,
and new ones are appearing all the time.  (For example, <a href="http://www.meyerweb.com/eric/tools/s5">S5</a>, the Simple
Standards-Based Slide Show System, uses XHTML and JavaScript to create
a simple slide show.)  The problem I have is that I've used all of the
ones described below, and haven't been happy with any of them:</li>

<ul>
<li>A (modified?) form of Wiki text as the source (so that it's easy
to edit and diff)
  <ul>
  <li>Generate slides and prose programmatically</li>
  <li>Use a simple CGI system to display pages in a browser while
  editing in order to check formatting</li>
  <li>Transform generated HTML/XML to create printable copy</li>
  </ul>
</li>
<li>LaTeX
  <ul>
  <li>Already has grown-up production tools (don't need to invent any
  wheels!)</li>
  <li>Editing and diffing is harder than Wiki text (comparable to
  XML)</li>
  <li>Expressing formatting right (e.g. indentation of code samples in
  slide bullet points) is easier than with Wiki text</li>
  </ul>
</li>
<li>HTML
  <ul>
  <li>Can view exactly what I'm writing...</li>
  <li>...except I don't want to: included code, point form vs. prose,
  etc.</li>
  <li>Can CSS take care of some of the display/view problems?</li>
  </ul>
</li>
<li>XML (home grown)
  <ul>
  <li>Can provide exactly as much information as I need to</li>
  <li>Transformation is relatively straightforward</li>
  <li>Do I really want to build up my own tagset?</li>
  </ul>
</li>
<li>XML (borrowed from the Pragmatic Programmers)
  <ul>
  <li>Don't know if they'd let me</li>
  <li>Doesn't handle slides</li>
  </ul>
</li>
<li>XML (DocBook or other)
  <ul>
  <li>Overkill (esp. from an editing point of view)</li>
  <li>Don't know if it handles slides or not</li>
  </ul>
</li>
<li>WYSIWYG (Word, OpenOffice, etc.)
  <ul>
  <li>Hard to process (e.g. extract slides to one fileset, prose to
  another, or insert/check code samples)</li>
  </ul>
</li>
</ul>

<p>What else is there?  What have you used that helped make you
productive?</p>
