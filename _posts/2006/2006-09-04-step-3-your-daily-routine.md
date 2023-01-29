---
title: "Step 3: Your Daily Routine"
date: 2006-09-04 18:17:50
year: 2006
---
OK, your project is up and running: you know what you're supposed to be building, and you have a schedule for producing it.  Now what? "Code 'til your fingers bleed" is a lousy strategy for individual work; it's almost certain to fail on team projects.  Instead, you should invest a little time in getting your day-to-day operations right.

First, <strong>learn how to run meetings.</strong> I blogged my rules last autumn, and believe them even more strongly today.

Second, <strong>read Stephanie Ludi's <a href="http://www.csc.calpoly.edu/~sludi/SEmanual/TableOfContents.html">guide to student software projects</a></strong>, and pay particular attention to the section titled "<a href="http://www.csc.calpoly.edu/~sludi/SEmanual/Part4.html">Student Project Myths</a>".  If you have time, you should also dip into Karl Fogel's excellent book <a href="http://www.amazon.com/Producing-Open-Source-Software-Successful/dp/0596007590"><cite>Producing Open Source Software</cite></a>, which is available <a href="http://producingoss.com/">online</a>.  Both have a lot of good advice about communication and respect; I'll talk about both issues in a future post.

Third, <strong>set up a development environment</strong> that includes version control, a bug tracker, a wiki, and a mailing list with a searchable archive.  These will greatly improve your chances of meeting your schedule without <a href="http://www.igda.org/articles/erobinson_crunch.php">burning out</a>.  If your instructor hasn't installed something like DrProject for you, and you can't set up things like <a href="http://subversion.tigris.org">Subversion</a> and <a href="http://trac.edgewall.org/">Trac</a> on your university's machines, buying a hosted domain and install <a href="http://buildix.thoughtworks.com/">Buildix</a>.  It'll cost less than pizza for six people, and when your project is over, you can show the domain off in job interviews—I know at least one Web 2.0 company that won't even interview anyone who doesn't have their own domain.

<strong>Make sure everyone is using the same tools</strong>.  This is just as important as setting up a development environment in the first place.  If some team members are using Make from the command line, while others are building inside an IDE, or if one person is automating tests with shell scripts, while another is using Python, you will lose precious time to duplication and contradiction.

You'll know you have it right when your working day looks something like this:
<ul>
  <li>3:00 p.m.: you sit down to spend two hours working on project. Launch <a href="http://www.eclipse.org">Eclipse</a> and do a <a href="http://subversion.tigris.org">Subversion</a> update. Hm… your teammates have checked in 17 sets of changes since the meeting two days ago.</li>
  <li>3:05 p.m.: you log in to DrProject and look at the event log.  Five tickets have been closed, but eight new ones have been created, three of which are assigned to you.  Looks like the file parser you wrote last week doesn't handle all of the new examples the prof put on the web on Monday.  You start writing unit tests to check the things that are breaking.</li>
  <li>3:25 p.m.: you have added twelve new file parsing tests to the project's test suite.  Eleven currently fail the way you expected; the twelfth triggers an assertion in a data structure one of your teammates built.  You file a ticket with a pointer to the test case, check them all in, and start fixing your code.</li>
  <li>4:00 p.m.: the eleven tests whose failure was your fault now pass, so you check in your fixes and close the tickets.  You're careful to refer to the changeset that contains the fix in your comments when you close the tickets, and to the tickets in the comment on your changeset; it only takes a second to type in this information, and it makes it much easier for your teammates to keep track of what you've done.  You then take a five-minute break to check email; when you're done, you close your mail client (since you've learned the hard way that you can't resist looking at new messages if you know they're there).</li>
  <li>Now you can start work on the new feature you want to add (which translates part of the program's internal data structure into a blob of XML to send to a web server).  You have an hour less to do this than you originally planned, but that's OK: by fixing bugs first, you've avoided the all-too-common situation of only half the code working when the project is "done".  As with bug fixes, you start by writing some test cases, which help you think through the details of the two new interfaces and five new classes you're going to add.</li>
  <li>4:20 p.m.: after rewriting your test cases a couple of times, you're happy with the API for the new feature.  Time to start coding? Not quite: with only 40 minutes to go, you know you won't finish it today.  Instead, you decide to write the two interfaces in full, along with their JavaDoc, to capture the thinking you've just done.  You will then write stubs of the new classes that implement those interfaces, all of whose methods will return 0 or <code>null</code>. These placeholders let you add calls to the classes, and check that everything still compiles, and that none of the tests that used to work now fail.</li>
  <li>4:45 p.m.: having checked everything in, you send a short email to the project list to tell your teammates what you've done.  You then reward yourself by checking email and reading a couple of blog postings about how bad the Maple Leafs' offensive lineup is this year.</li>
</ul>
Three sessions like that a week, from each person on the project, plus a single one-hour team meeting, and you'll be in great shape.
<ul>
  <li>Part 1</li>
  <li>Part 2</li>
</ul>
