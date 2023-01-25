---
title: "Miscellaneous Projects"
date: 2015-11-15 07:00:00
year: 2015
original: swc
---
<p>
  This post is a bit of a
  <a href="http://www.theguardian.com/science/brain-flapping/2014/sep/10/wild-extrapolation-classification-system-science-media-scepticism">link fest</a>,
  but after talking about how to contribute
  at yesterday's instructor retreat,
  I thought it might be useful to post a few additions to
  our projects page.

<ul>
  <li>
    <p>
      In a "Parsons Problem",
      you are given the pieces of the solution and asked to arrange them in the correct order.
      For example,
      given the words "cat", "eating", "quietly", "is", and "the",
      you could be asked to construct a grammatically correct sentence that explains what the cat is doing.
      <a href="http://js-parsons.github.io/">js-parsons is a Javascript library
      for building Parsons Problems for programming.
      It would be cool to incorporate it into our lessons
      (and to see whether it's easier to auto-grade solutions to such exercises
      than solutions written from scratch).
    </p>
  </li>
  <li>
    <p>
      A growing number of programmers are
      <a href="https://medium.com/backchannel/the-strange-appeal-of-watching-coders-code-5c677b2c34ec">coding live online</a>
      so that people can see what they do and hear how they think.
      (My favorite is <a href="http://mikeconley.ca/blog/2015/10/04/the-joy-of-coding-eps-23-29/">Mike Conley hacking on Firefox</a>.)
      I would really like to see some Carpentry instructors livecast some data analysis and coding sessions–volunteers?
    </p>
  </li>
  <li>
    <p>
      daff
      is an R package that can find difference in values between data.frames,
      store this difference,
      render it,
      and apply this difference to patch a data.frame.
      It can also merge two versions of a data.frame having a common parent.
      I've been saying for years that better support for diffing and merging things
      would make it a lot easier for scientists (and everyone else) to adopt version control;
      is daff a step toward this?
      If so,
      should we teach it in our workshops?
    
  </li>
  <li>
    <p>
      I really like our lesson on SQL,
      but as non-relational databases become more popular,
      I wonder if it's time for us to cover them as well.
      Setup wouldn't be as big an obstacle as it once was,
      thanks to libraries like <a href="https://pypi.python.org/pypi/tinydb">tinydb</a>.
      And hey,
      we can even <a href="https://github.com/harelba/q">run SQL queries directly on CSV files</a>.
    </p>
  </li>
  <li>
    <p>
      It would also be useful to integrate
      <a href="https://github.com/agiliq/notebooks/blob/master/sql-equivalents.ipynb">this comparison of SQL and Pandas</a>
      into our lessons.
      (Of course,
      we'd have to integrate Pandas first...)
      There's also this <a href="http://mathesaurus.sourceforge.net/r-numpy.html">NumPy for R</a> guide,
      <a href="http://sebastianraschka.com/Articles/2014_matrix_cheatsheet_table.html">this matrix cheatsheet</a>,
      and I'm sure we can find others.
    </p>
  </li>
  <li>
    <p>
      And speaking of lessons,
      it would be great to have more people contribute to Fiona Tweedie's
      lesson on natural language processing
      (possibly incorporating material from Allison Parrish).
      I don't know if this should be combined with
      a user-friendly replacement for our old lesson on regular expressions,
      but it should definitely include
      this example
      of the problems with manually-entered data.
    </p>
  </li>
  <li>
    <p>
      I think our learners would also like a couple of hours on image processing
      (the Version 4 lesson on multimedia
      is woefully out of date,
      and was never particularly well organized)...
    </p>
  </li>
  <li>
    <p>
      ...but most of all I want a lesson on
      how to write and publish in the early 21st Century.
      Word or LibreOffice?
      Version control can't handle them.
      Markdown or LaTeX?
      A lot of scientists are simply never going to adopt them,
      even with <a href="http://thomaspark.co/2015/01/pubcss-formatting-academic-publications-in-html-css/">help like this</a>.
      Are Authorea or Google Docs the happy medium?
      We might not be able to offer a single best solution,
      but we should at least be able to explain the tradeoffs.
      And that's just authoring:
      if we really want to help,
      we should also explain <a href="http://depsy.org/">Depsy</a>,
      <a href="https://hypothes.is/">Hypothes.is</a>,
      <a href="https://zenodo.org/">Zenodo</a>,
      <a href="http://blog.impactstory.org/ten-things-you-need-to-know-about-orcid-right-now/">ORCID</a>,
      new <a href="https://peerj.com/">publishing</a> <a href="http://f1000research.com/">models</a>,
      and all the other cool things that the one percenters of open science now take for granted
      but their colleagues have never used.
    </p>
  </li>
  <li>
    <p>
      OK, I wasn't done with lesson ideas.
      I think Abela's <a href="http://extremepresentation.typepad.com/blog/2006/09/choosing_a_good.html">chart chooser</a>
      (adapted from Zelazny's <em>Saying It With Charts</em>)
      would be a brilliant way to organize a lesson on data visualization:
      it's a useful medium between Tufte's high-level pontificating
      (I never know what to <em>do</em> after reading his books)
      teaching people how to center labels under the ticks on the X axis,
      and scientific publishers would be very grateful if more authors followed these rules.
      Bonus marks for integrating Heer's <a href="http://homes.cs.washington.edu/~jheer//files/zoo/">tour of the visualization zoo</a>
      into the lesson as well.
    </p>
  </li>
  <li>
    <p>
      The errors and exceptions topic
      in our standard Python lesson is really useful:
      programmers at all levels spend much (or most) of their time trying to diagnose and correct errors,
      but most textbooks and courses give the topic short shrift.
      (If you want a <em>really</em> cool project,
      create a new programming language with easy-to-understand errors as the most important design criterion.)
      I'd like to incorporate things like <a href="https://github.com/dhellmann/whatthewhat">What the What</a>,
      <a href="http://explainshell.com/">explainshell</a>,
      and similar tools into our teaching.
      (I'd also like to add something like Sumana Harihareswara's
      "<a href="http://www.harihareswara.net/sumana/2014/08/10/1">Inessential Weirdnesses in Open Source</a>",
      just so that learners know this stuff really is harder than it needs to be.)
    </p>
  </li>
  <li>
    <p>
      Would anyone like to go through
      <a href="https://nsfbiobuzz.wordpress.com/2015/10/16/dmp_guidance/">the latest recommendations for data management plans</a>,
      compare what they're asking for with what we teach,
      and file issues to fill in the gaps?
      Because one useful goal of our workshops would be
      to give attendees the understanding needed to write <em>and critique</em> data management or software sustainability plans.
      DataONE's <a href="https://www.dataone.org/sites/all/documents/DataONE-PPSR-DataManagementGuide.pdf">Data Management Guide for Public Participation in Scientific Research</a> might also figure into this.
    </p>
  </li>
  <li>
    <p>
      We'd like to rebuild our web site using the same "Feeling Responsive" theme
      that the Data Carpentry site uses.
      We've made good progress,
      but there's a lot left to do.
      If you have good CSS and web design skills,
      or if you're up for a bit of Python hacking,
      this is the job for you.
    </p>
  </li>
</ul>
