---
title: Where We Are (More or Less)
date: 2013-05-24
original: swc
---
<p>
In January 2012,
John Cook posted <a href="http://blog.codekills.net/">this</a> to his widely-read blog:
</p>
<blockquote>
  In a review of linear programming solvers from 1987 to 2002,
  Bob Bixby says that solvers benefited as much from algorithm improvements as from Moore's law:
  "Three orders of magnitude in machine speed
  and three orders of magnitude in algorithmic speed add up to six orders of magnitude in solving power.
  A model that might have taken a year to solve 10 years ago can now solve in less than 30 seconds."
</blockquote>
<p>
  A million-fold speedup is pretty impressive,
  but faster hardware and better algorithms are only two sides to the triangle.
  The third is development time,
  and while it has improved since 1987,
  the speedup is measured in small percentages,
  not orders of magnitude.
  For most scientists,
  getting the code to do the right thing
  is now a bigger bottleneck than its running time.
</p>
<p>
  That's where Software Carpentry comes in.
  We teach scientists
  (usually grad students, since they have both the need and the time)
  what they ought to know
  <em>before</em> they start working on large programs,
  creating web services,
  or any other leading-edge work.
  Our hope is that if we give people basic skills,
  they'll be better able to take advantage of more sophisticated things.
</p>
<p>
  Between January 2012 and July 2013,
  over 100 volunteers will have run 92 two-day workshops for over 3000 scientists.
  A typical two-day curriculum is:
</p>
<ul>
  <li>
    <strong>Day 1 morning</strong>:
    Introduction to Unix shell.
    We show participants a dozen basic commands,
    but the real aim is to introduce them to pipes,
    loops and history (to automate repetitive tasks),
    and the idea of scripting.
  </li>
  <li>
    <strong>Day 1 afternoon</strong>:
    Version control,
    with an emphasis on collaboration and reproducibility.
    If time permits,
    we also give them a quick intro to regular expressions
    or something else that's relatively easy.
  </li>
  <li>
    <strong>Day 2 morning</strong>:
    An introduction to Python,
    the real goal of which is to show them
    when and why to develop code as a set of comprehensible,
    reusable functions.
    Some bootcamps use R instead,
    and we expect that to become more common.
  </li>
  <li>
    <strong>Day 2 afternoon</strong>:
    Testing,
    focusing on the idea of tests
    as a way to specify what a program is supposed to do,
    and how to structure unit tests using an xUnit-style library.
    This is probably the weakest part of our standard two days:
    we've got the "how" down cold,
    but the "what" for scientific software is still very much up in the air.
  </li>
  <li>
    <strong>Day 2 afternoon</strong>:
    Number crunching using NumPy,
    basic SQL,
    or some other "beyond mere programming" topic that suits the audience.
  </li>
</ul>
<p>
  As the comments above suggest,
  our real aim isn't to teach Python, Git, or any other specific tool:
  it's to teach <em>computational competence</em>.
  What we've found,
  though,
  is that we can't do this in the abstract:
  people won't show up,
  and if they do,
  they won't understand.
  We try hard to start with the particular,
  and to show them that yes,
  this stuff actually is useful,
  and then bring in more general stuff.
</p>
<p>
  We nominally aim for 40 people per workshop,
  and are always grateful for local helpers
  to wander the room and answer questions during practicals.
  We find workshops go a lot better if people come in groups,
  e.g., 4-5 people from one lab,
  half a dozen from another department or institute,
  etc.,
  so that they are less inhibited about asking questions,
  and can support each other afterward.
  (It also produces much higher turnout from groups
  that are usually under-represented in computing,
  such as women and minority students.)
  We use live coding rather than slides:
  it's more convincing,
  there's more lateral knowledge transfer
  (i.e., people learn more than we realized we were teaching them by watching us work),
  and it makes instruction a lot more responsive.
</p>
<p>
  Our instructors are all volunteers,
  so the only cost to host sites is travel and accommodation.
  All but a handful of our instructors are working scientists themselves;
  that,
  plus live coding instead of slides,
  ensures that attendees get lots of "how"
  as well as "what".
</p>
<p>
  We also run an online training course
  for would-be instructors.
  It takes 2-4 hours/week of their time for 12 weeks,
  and introduces them to the basics of educational psychology,
  instructional design,
  and how these things apply to teaching programming.
  It's necessarily very shallow,
  but it's still more than most university faculty ever get…
</p>
<p>
  Results have been very good:
  we had two independent evaluations done last spring
  (one by Prof. Julie Libarkin at Michigan State University,
  the other by Dr. Jorge Aranda at the University of Victoria),
  and both found that people actually are learning useful things.
  What we're struggling with now is
  showing that this translates into them doing more and/or better science
  (the holy trinity of "novelty, efficiency, and trust").
</p>
<p>
  Here's what else isn't working (or isn't working well):
</p>
<ul>
  <li>
    Our "host site pays costs" model
    makes us nearly self-sustaining financially,
    but only if you exclude the costs of
    1.5 people in the middle of things doing coordination.
    Since I'm the 1.0 of that 1.5,
    I'd like to find a way to regularize that size of things…
  </li>
  <li>
    Learners come to us with a very wide range of prior knowledge and abilities,
    and as a result,
    we figure that 20% are bored and 20% are lost at any time.
    We'd like to start offering separate bootcamps for complete novices
    and can-already-kind-of-program people,
    but we can't rely on them to self-assess their ability
    (they don't know what they don't know),
    and if we give them any kind of proficiency test,
    it scares away the ones with weaker skills who need us most.
  </li>
  <li>
    We need to start teaching data management
    and how to use the web to do science better;
    the hard part is to figure out what.
    We can talk generalities about data management,
    but they want tools and procedures.
    As for web programming,
    all we can show them in half a day is
    how to create security holes…
  </li>
  <li>
    We need to persuade the powers that be–funding agencies,
    departmental chairs, etc.–that this stuff deserves institutional backing.
    Many believe it's important;
    what's hard is persuading them that it's <em>more</em> important than
    things that are already in the curriculum,
    and that have passionate defenders.
    (As a chemist once said to us in frustration,
    "What do we take out of the undergrad curriculum to make room for this:
    thermodynamics or quantum mechanics?")
    One thing we're trying is a "driver's license" exam
    for the DiRAC supercomputing facility in the UK;
    once it's implemented,
    grad students who want to use it
    have to show they have at least basic computational competence.
  </li>
</ul>
<p>
  We're pausing to catch our breath from mid-July to the end of August this year,
  during which time we'll clean up our GitHub repositories,
  finish the instructors' guide,
  and generally get ready for another round of bootcamps in the fall.
  Before then,
  though,
  we will have some exciting news to announce,
  so please keep an eye on this blog–we think you'll like what you see.
</p>
