---
title: "A Better Software Engineering Course"
date: 2014-10-02 21:00
year: 2014
---
<p>
  I've taught several university courses on software engineering over the years,
  and haven't been happy with any of them.
  Like most professors,
  I build these courses around team projects,
  and had students work in small groups to design, build, and test a sizeable (ish) piece of software.
  I realized after a couple of years,
  though,
  that students weren't actually learning what I wanted them to learn in these courses because:
</p>
<ol>
  <li>
    <em>We were putting them in impossible situations.</em>
    Having two bosses is hell;
    having five is–well, it's actually quite normal for students
    who are taking that many courses
    from faculty who don't consult with each other on workload and deadlines.
    As a result,
    students simply can't manage their time the way we tell them they should.
    All they can actually do is tell us what they think we want to hear
    about how and when they did things.
  </li>
  <li>
    <em>Process can't be taught: it has to be mentored.</em>
    Facts–nouns–are relatively easy to teach through lectures.
    Processes–verbs–aren't nearly as amenable to description:
    in my experience,
    the only way to convey them is by example,
    working side by side,
    but that doesn't scale beyond small classes without heroic effort,
    which is neither sustainable nor transferable.
  </li>
  <li>
    <em>The raw material is missing.</em>
    Lots of books have the words "software architecture" in the titles,
    but other than <a href="http://aosabook.org">the ones I helped create</a>
    (ironically, just as I was leaving academia),
    none of them actually describe the architectures of real applications.
    Similarly,
    while there are books on measuring and tuning performance–a
    core engineering activity if ever there was one–that
    material is almost never discussed in courses called "software engineering".
    And when it comes to measuring software development–not just
    talking about it, but <em>measuring</em> it–textbooks
    simply haven't kept pace with the changes I've seen at major conferences
    like <a href="http://www.icse-conferences.org/">ICSE</a>,
    where papers on new tools now routinely report
    empirical field studies of those tools' use.
  </li>
</ol>
<p>
  If I ever teach undergraduates software engineering again,
  I'll create a course that could have exercises like these:
</p>
<ol>
  <li>
    Describe and contrast the implementation of undo/redo in the Vim text editor
    with the implementation in the Inkscape vector graphics application.
    Explain the forces or constraints that led to the differences between the two.
  </li>
  <li>
    You have been asked to review a paper whose abstract reads:
    "We analyzed 17 pieces of software ranging in size from 18K to 110K lines,
    and calculated the density of design patterns using
    <em>D = (# uses of patterns) / (# classes)</em>.
    We compared this value to the error density:
    <em>E = (# errors found by customers) / (# classes)</em>.
    The correlation was -0.87,
    from which we conclude that using design patterns results in better code."
    Identify the ways in which this analysis is flawed or suspect.
  </li>
  <li>
    You have been given a database
    of all bug reports filed and closed during one release cycle for a medium-sized Java application,
    along with an archive of the version control history of that same application.
    By combining information from the two data sets,
    determine whether changes to large methods are more likely to contain bugs
    than changes to small methods.
  </li>
</ol>
<p>
  In order to tackle the last of these,
  students will need to figure out how to connect bug reports to commits,
  how to use code analysis tools to measure the sizes of methods,
  and how to operationalize "more likely"
  (does it mean "more likely per method",
  "more likely per line of code",
  or "more likely per commit"?).
  This knowledge,
  and the knowledge needed for the other questions,
  isn't more important than teamwork,
  but it's a lot more teachable in a standard classroom.
</p>
<p>
  And learning it will do a lot both to help students succeed on real projects,
  and to raise standards in industry.
  I've spent the last few years teaching scientists how to program;
  what I've learned is,
  programmers have a lot to learn from scientists about
  how to figure out what's working and what isn't.
  If we start teaching that,
  we might finally deserve to call what we do "software engineering".
</p>
