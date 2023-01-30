---
title: "Issue Tracking Systems"
date: 2004-08-30 10:01:41
year: 2004
---
One of the students who's going to be working on Hippo this fall sent a message to the group asking for everyone's MSN IDs, so that the team could set up group chats.  That got me thinking about how many different ways there are to communicate electronically these days, and about how to use them to manage a small, part-time software development team.

First, some definitions.  <em>Targeted</em> communication is aimed at a particular receiver, or set of receivers, while <em>untargeted</em> just puts content in a well-known place for anyone to read.  Email and instant messaging are generally targeted, while newsgroups and wiki pages are untargeted; an always-on IRC channel is somewhere in between.  <em>Archived</em> communication "sticks around", i.e. can be re-read or searched at a later date, while <em>transient</em> communiation evaporates.  As with the previous category, the dividing line is not a clear one—newsgroups feel archived, but most servers throw away old articles after a time.  Similarly, instant messaging feels transient, but many IM clients now allow you to record conversations.  Finally, content that is <em>pushed</em> reaches the recipients without the recipients having to do anything; email is once again the classic example, but weblogs are becoming popular as well.  In the <em>pull</em> model, readers have to go out of their way to get messages, i.e. go to a particular web site to read new messages in a forum.

Now, small software development teams want to be able to:
<ol>
  <li>ask teammates for help, or request feedback on ideas;</li>
  <li>report progress, or share things you've discovered;</li>
  <li>schedule meetings;</li>
  <li>hold meetings (rather than getting together face-to-face); and</li>
  <li>socialize,</li>
  <li>all without being flooded.</li>
</ol>
#1 wants to be targeted to team members, archived, and pushed.  (Requests for help don't actually need to be archived, but answers do.)  #2 is similar, though it's OK for progress reports to be pulled rather than pushed, so long as everyone pulls them eventually.

#3 can be transient, but should be pushed to everyone you want in the meeting.  #4 is just a bad idea—the Winter 2003 students found that IM is a very inefficient way to hold meetings.  (Check with them if you don't believe me.)  On the other hand, IM is great for #5 (although as Joel Spolsky says, running an IM client at all times is guaranteed to lower your productivity).  As for #6, that comes down to the project admins putting spam protection in place, and project members playing nice.

So, with that lengthy preamble out of the way, how <em>should</em> team communicate?
<ul>
  <li>Use the email lists for questions and short answers, especially when they are time-critical (i.e. someone needs to know how to do XYZ <em>right now</em>).</li>
  <li>Add content to the project web site for progress reports, longer answers, discoveries, FAQs, how-to's, and so on, but post a note (including a URL) to the project mailing list to let people know when new content is available.</li>
  <li>By all means use IM for socializing, but if you spent ten minutes on IM explaining XYZ to someone, please, copy the conversation, paste it into a page in the project's web folder, and let everyone know it's there.</li>
</ul>
Hm… I've left something out here.  In fact, I've left out the most important point of all:
<blockquote>USE YOUR PROJECT'S ISSUE TRACKING SYSTEM.</blockquote>
(Yes, I actually <em>do</em> think it deserves capital letters.)  An issue tracking system is a project's shared to-do list; it's used to record bugs, features that need implementing, action items (such as "prepare a note for students on how to communicate"), and so on.  What's more, it records them in a <em>structured</em> way, and that's what makes issue tracking systems so useful.  Email, wikis, blogs, and so on are the "goto" statements of electronic communication: since you can put/send data just about anywhere, there's no inherent rhyme or reason to traffic and content.  An issue tracking system, on the other hand, imposes rules on format, state transitions, and so on, just as "for" loops and "if/else" statements impose order on goto's.

Experience (mine, anyway) shows that imposing order at the outset is more efficient, and more helpful, than trying to reverse engineer it after the fact by building ultra-smart search engines.  Experience also shows that if teams start using an issue tracking system early in the project lifecycle, when deadline pressure is low, they're more likely to use it well by the time deadline pressure intensifies—i.e., by the time they really need it.
