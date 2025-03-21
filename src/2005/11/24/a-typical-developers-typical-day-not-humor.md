---
title: "A Typical Developer's Typical Day (not humor)"
date: 2005-11-24
---
Jon Erickson, the editor-in-chief of <em><a href="http://www.ddj.com">Doctor Dobb's Journal</a></em>, asked me to write a couple of paragraphs about a typical developer's typical day.  As usual, I went a little overboard; unusually, I veered toward the bright side.

It's 9:30.  You've caught up on email from the contractors in India, skimmed a dozen blog postings, and finished your first cup of coffee: time to get to work.  Open <a href="http://www.eclipse.org">Eclipse</a>, and check your working copy against the repository.  Hm… Maria and Sukhmeet have checked in changes to the charting module.  Two clicks takes you to the web page that shows the results of the overnight build and smoke tests.  Total coverage has dropped slightly, but the new functionality <em>is</em> being tested, so you update and recompile.

Next, you flip over to the bug tracking web page, and re-read the description that Bin in QA filed against the password strength checker.  "Doesn't recognize digits immediately following non-Latin characters."  OK, that's probably a character encoding problem.  You write a unit test, copy and paste the Chinese character passwords Bin used to find the problem, set a couple of breakpoints, and dive in.

By 11:00, you know that the problem is something to do with the LDAP server not reporting encodings correctly.  You have to put it aside for a while, though, because there's a 1:00 meeting to review the schedule estimates for the new biometrics module, and you want to get forty minutes on the exercise bike downstairs before then.  You print the requirements doc, get a fresh cup of coffee, and settle in with your favorite red pen.

3:00.  The meeting ran well over time, but the pizza was good, and several important decisions were made.  The minutes won't be up on the project web site for checking until the end of the day, so you have at least a couple of hours to track down that encoding issue.  You're interrupted twice: once by the intern with a question about environment variables in <a href="http://ant.apache.org">Ant</a>, and one by a phone call from a field engineer in Calgary, whom you redirect to second-line support.  Despite that, you're able to figure out that the admin UI isn't setting the domain object properties correctly.  A one-line change, two new unit tests, and a three-line check-in comment later, it's 4:30, and you have half an hour in which to catch up with <a href="http://www.joelonsoftware.com/">Joel Spolsky</a>, <a href="http://weblog.infoworld.com/udell/">Jon Udell</a>, and the fine folks at <a href="http://www.artima.com/index.jsp">Artima</a> before catching the train home.
