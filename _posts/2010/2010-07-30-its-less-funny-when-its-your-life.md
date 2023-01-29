---
title: "It's Less Funny When It's Your Life"
date: 2010-07-30 12:22:37
year: 2010
---
A couple of days ago, Steve Yegge posted a <a href="http://steve-yegge.blogspot.com/2010/07/wikileaks-to-leak-5000-open-source-java.html">sort-of funny piece</a> to his blog about Wikileaks leaking the source code of 5000 open source Java projects by making all modifiers 'public' and all classes and members non-'final'.  One mock-quote in it was:
<blockquote>If people could keep using the older, more convenient APIs I made for them, then why...would they use my newer, ridiculously complicated ones? It boggles the imagination.</blockquote>
In response, a friend of mine who works for a major bank said that he just had to explain to a new Java programmer why:
<ol>
  <li>In Java, you have to use <code>java.util.Date</code> and <code>java.util.Calendar</code> and <code>java.sql.Date</code></li>
  <li><code>java.util.Date</code> has a <code>getYear()</code> which needs you to add 1900 to the year (because that was reasonable to somebody)</li>
  <li>Months are 0 based, but days of the month are not.</li>
  <li><code>Calendar.get()</code> uses <code>YEAR</code>, <code>MONTH</code> and <code>DATE</code> to get year month and day. Because you know, I always think of describing the date with dates. It's recursive. Or circular. It's something.</li>
  <li>Even with all three dates, you'll still end up getting nothing done, because you can't compare dates. So go just download this open source library instead.</li>
  <li>And finally, now you have opensource, so fill out this security deviation form for the bank.</li>
</ol>
