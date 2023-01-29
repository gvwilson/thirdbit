---
title: "State of DrProject"
date: 2006-02-21 15:27:21
year: 2006
---
In the wake of  at <a href="http://barcamp.pbwiki.com/TorCampDemoCamp3">DemoCamp 3</a> last night, we had another on-line meeting this morning about the state of DrProject.  Our original aim was to release it at the end of January; we're now looking at the first week of March, and it may slip again.  Here's the current to-do list:
<ol>
  <li>Our <a href="http://kid.lesscode.org/">Kid</a> templates are too slow: 2-3 seconds per page.  This is only partly Kid's fault—as Chris Lenz pointed out, our current wiki formatter is creating HTML, which Kid then tries to validate.  We hope to fix this with a two-pronged attack: writing a new wiki formatting engine (which we really want to do anyway), and getting Kid's maintainers to add a "don't bother to validate" flag.</li>
  <li>The mail subsystem still isn't hooked up.  <a href="http://www.exim.org">Exim</a> vs. <a href="http://www.sendmail.org">Sendmail</a> is part of the problem, but so is the code that was written last summer.</li>
  <li>We still don't have any screencasts (which have quickly become one of the things that separates the pros from the amateurs).  Pat Smith has tried various tools, but none of the free ones generate Flash <em>and</em> record audio at the same time.  The latest beta of <a href="http://www.debugmode.com/wink/">Wink</a> is next on his list; if that doesn't work by week's end, we'll spring for <a href="http://www.techsmith.com/camtasia.asp">Camtasia</a>.</li>
  <li>We haven't figured out what to do about RSS authentication (but then, neither has anyone else).  We <em>must</em> use the user accounts on the underlying Unix system, rather than doing our own provisioning, so we either figure out a secure way to get a dozen different blog readers to pass user IDs and passwords to us (unlikely), or place a bet on one of the open source identity management "standards" being bruited about.  You can probably hear the lack of enthusiasm in my voice...</li>
  <li>Documentation.  The user guide isn't done, the installation notes are incomplete, the scripting examples don't exist—in short, we're looking like a typical open source project.</li>
  <li>Finally, there are a bunch of smaller issues: modifying the CSS style sheets so that pages printed from Firefox aren't squeezed into a two-centimeter column, making the logo display properly in IE, and so on.</li>
</ol>
None of this detracts from the fact that we've come a long way in a very short time: DrProject is very usable, and impressed a lot of people last night who aren't particularly easy to impress.

Onward!
