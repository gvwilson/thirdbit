---
title: "All I Want for Christmas is a Pull Request…"
date: 2014-12-18 06:00:00
year: 2014
original: swc
---
<p>
  As we said back in October,
  we're splitting the existing lesson repository
  into smaller and more manageable pieces.
  To do that,
  we have defined
  a new template for lessons,
  and have been extracting the history of the existing material from the current repository.
  (We wanted to get the entire history of each lesson
  so that people would receive credit for the work they've done.)
  The second step has taken longer than planned,
  but we now have all of the core novice lessons in repositories of their own:
</p>
<table class="table table-striped">
  <tr>
    <th>Repository</th>
    <th>Title/website</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>shell-novice</td>
    <td>Introduction to the Unix shell.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>git-novice</td>
    <td>Introduction to Git.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>hg-novice</td>
    <td>Introduction to Mercurial.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>sql-novice-survey</td>
    <td>Introduction to SQL using Antarctic survey data.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>python-novice-inflammation</td>
    <td>Introduction to Python using inflammation data.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>r-novice-inflammation</td>
    <td>Introduction to R using inflammation data.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>matlab-novice-inflammation</td>
    <td>Introduction to MATLAB using inflammation data.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>capstone-novice-spreadsheet-biblio</td>
    <td>A short capstone that gets a bibliography out of a spreadsheet and into a more usable form.</td>
    <td>beta</td>
  </tr>
  <tr>
    <td>instructor-training</td>
    <td>Software Carpentry instructor training course.</td>
    <td>alpha</td>
  </tr>
  <tr>
    <td>python-novice-turtles</td>
    <td>Introduction to Python using turtle graphics.</td>
    <td>alpha</td>
  </tr>
</table>
<p>
  There's still a lot to be done:
</p>
<ul>
  <li>
    <p>
      The CSS used to style the new template needs a major overhaul.
    </p>
  </li>
  <li>
    <p>
      The validation tool
      used to check the format of lessons against the new template needs more work.
    </p>
  </li>
  <li>
    <p>
      The challenge exercises all need titles
      (right now, most are titled "FIXME").
    </p>
  </li>
  <li>
    <p>
      We need a 3-minute motivational slide deck for each lesson.
      (See this page for
      a preview of the tool we're going to use to record these.)
    </p>
  </li>
  <li>
    <p>
      Glossary entries need to be brought over from
      the old repository.
    </p>
  </li>
  <li>
    <p>
      The intermediate lessons
      need to be extracted from the old repository
      and merged with the new lesson template.
    </p>
  </li>
  <li>
    <p>
      Learning objectives for each lesson need to be rewritten to be more concrete.
    </p>
  </li>
  <li>
    <p>
      Data files in
      the novice R lesson
      need to be
      moved into the <code>data</code> sub-directory
      and paths in the source updated accordingly.
    </p>
  </li>
  <li>
    <p>
      The outstanding pull requests
      against the <code>master</code> branch of the shell lesson need to be merged or discarded
      so that we can close that branch and start doing everything against <code>gh-pages</code>.
    </p>
  </li>
  <li>
    <p>
      The "images" produced by ipythonblocks
      in the novice Python lesson
      need to be regenerated as PNGs (rather than as HTML tables),
      saved,
      and linked in.
    </p>
  </li>
  <li>
    <p>
      …and a hundred and one other things,
      because lessons are like theses:
      they're never done,
      they're just delivered.
    </p>
  </li>
</ul>
<p>
  One thing you'll notice is that we're now using Markdown for everything
  instead of IPython Notebooks.
  We still <em>teach</em> with notebooks when we're in front of a class,
  but our contributors have found diffing and merging them difficult enough
  that we're switching back to plain old text for the notes
  until something like nbdiff is ready for prime time.
</p>
<p>
  Another thing you might notice is a new capstone lesson
  showing people how to use the shell, Python, SQL, and Git
  to extract authors' names from a bibliography stored in a spreadsheet
  and answer questions like, "Who has co-authored papers with whom?"
  This lesson is meant to be useful in its own right,
  but also to serve as an example for others of its kind.
  If you have something short and accessible that you'd like to share,
  please let us know:
  we'd be happy to work with you to bring it to a wider audience.
</p>
<p>
  What we need most, though, is polish:
  all of the points listed above need to be addressed
  before we can put these lessons on the website
  instead of the ones stored in the old repository.
  If you have 15 minutes,
  please dive into one of these lessons,
  proof-read one section,
  and file some issues.
  Or better yet,
  send us a pull request that fixes something–anything at all–so that
  we can hit the ground running in 2015.
</p>
