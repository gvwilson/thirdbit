---
title: "Publishing, Metadata, and Being Ahead of the Curve"
date: 2015-08-12
original: swc
---
<p>
  As described in earlier
  posts,
  we are publishing our Version 5.3 lessons through <a href="https://zenodo.org/">Zenodo</a>
  to make it easier for people to cite them.
  We're getting closer,
  but there are still a few bumps in front of us,
  and we would like our readers to help us figure out what to do next.
</p>
<p>
  Uploading a ZIP of the lesson's source corresponding to the version tagged "5.3" was straightforward.
  The next step was (and is) to figure out what metadata to provide.
  Zenodo kindly added Lesson as a type
  (to go along with Publication and Presentation, neither of which were quite right for us),
  so categorizing is easy.
  Some of the lessons have contributions of wildly varying size from dozens of people,
  so we decided to list each lesson's maintainers as its editors,
  which would give us something like this:
</p>
<pre>Daisie Huang and Ivan Gonzalez (eds): "Software Carpentry: Version Control with Git."
Version 5.3, May 2015, 10.5281/zenodo.23544.</pre>
<p>
  We can then add all of the people who contributed as–well, that's the first pair of problems:
</p>
<ol>
  <li>
    <p>
      Zenodo won't let us create a record that doesn't have an Author field.
      After some discussion with Elizabeth Wickes (a data curation specialist at the University of Illinois),
      we decided to use an institutional author for now,
      i.e.,
      to list "Software Carpentry Foundation" as the author.
      This offers a lot of discoverability benefits,
      and also keeps the citation short.
    </p>
  </li>
  <li>
    <p>
      The only options for other kinds of contributor are "Contact person", "Data collector",
      "Data curator", "Data manager", "Editor", "Researcher", "Rights holder", "Sponsor", and "Other".
      We're already using Editor for the lesson maintainers,
      and none of the others feels right.
      ("Contributor" isn't available as a type of contributor.)
    </p>
  </li>
</ol>
<p>
  Setting those issues aside for now,
  let's have a look at what Zenodo exports for citation.
  The BibTeX they suggest is:
</p>
<pre>@misc{software_carpentry_foundation_2015_23544,
  author       = {Software Carpentry Foundation},
  title        = {Software Carpentry: Version Control with Git},
  month        = may,
  year         = 2015,
  doi          = {10.5281/zenodo.23544},
  url          = {http://dx.doi.org/10.5281/zenodo.23544}
}</pre>
<p>
  but that doesn't produce the plaintext citation shown earlier.
  In fact,
  it appears that <em>none</em> of the standard BibTeX entries will do exactly what we want:
  <code>@misc</code> doesn't allow <code>editor</code> as a field,
  while if we use <code>@incollection</code> (which requires a book title and author)
  we'll wind up with a "collection" that has the same author but different editors for each entry
  (which is the reverse of normal practice).
</p>
<p>
  After a bit of external inspection, Elizabeth believes that:
</p>
<blockquote>
  <p>
    …the problem is that
    data citation formats are still being sorted out and there is no single formula that is the "one true way" to make them…
    The problem that you're encountering,
    that Creators cannot be tagged with types like Contributors,
    is a problem within every schema I've encountered.
    You cannot express a creator as editor in DataCite,
    and therefore any system built with DataCite as a backend will have this limitation.
  </p>
  <p>
    …
  </p>
  <p>
    In the end,
    as with all metadata discussions,
    we tend to get lost in the weeds and need to take a step back and ask what we're really after here.
    Pretty much the DOI, right?
    Zenodo is not an authoritative source on who was involved in the project.
    No repository is.
    So leave that to your own documentation.
    The type of work you're trying to describe doesn't fit neatly into any of the schemas that are available.
    This means you'll never find a system that will perfectly generate what you're trying to achieve.
    You may just have to provide a suggested citation within the description areas, documentation, and SWC pages
    and leave it at that for now.
  </p>
  <p>
    Sorry, metadata emails never have happy endings.
  </p>
</blockquote>
<p>
  Stepping back,
  the underlying problem is that what we're doing is kind of new:
  if it wasn't,
  there would (probably) already be a BibTeX citation template we could pick up and use.
  Even the idea of version numbers for citable artifacts is still being sorted out–quoting
  Elizabeth again,
  "Looks like [Zenodo is] pulling the version number out of github and placing it within the &lt;title&gt; string value.
  Hacky, but not an incorrect way of accomplishing the task.
  Given this intel,
  placing the version number in the title would allow you to canonically match how Zenodo is using them
  (compare the full XML DataCite record here
  <a href="http://data.datacite.org/10.5281/zenodo.18910">http://data.datacite.org/10.5281/zenodo.18910</a>
  against the Zenodo record <a href="http://zenodo.org/record/18910">http://zenodo.org/record/18910</a>)."
</p>
<p>
  With all that as backdrop,
  my questions are:
</p>
<ol>
  <li>
    <p>
      Should we list all the contributors as authors,
      rather than having an institutional author?
      (We can do this in the electronic record,
      but still provide a citation for copying and pasting
      that lists the maintainers as editors.)
    </p>
  </li>
  <li>
    <p>
      What other changes (if any) should we make to our entry on Zenodo?
    </p>
  </li>
  <li>
    <p>
      What should the BibTeX for our lessons look like?
      (And for bonus points, what should citations in other formats look like as well?)
    </p>
  </li>
</ol>
<p>
  Please add your answers as comments on this blog post–we'll all learn something,
  and it'll all feed into the lesson we're planning on
  how to write, publish, and review scientific papers in the early 21st Century.
</p>
<hr/>
<blockquote>
  <p>
    Update on 2015-08-17:
    we have experimented with adding all of the contributors to the Git lesson
    as contributors in the Zenodo record,
    but we've had to list them as "Other",
    because (ironically) "Contributor" isn't available as a kind of contributor.
    This doesn't feel right,
    so we may revisit listing them all as authors (alphabetically by surname),
    rather than listing "Software Carpentry Foundation" as the author,
    and then having the standard citation list only the editors (as above).
    But we still need to figure out how to jam that citation into things like BibTeX…
  </p>
</blockquote>
