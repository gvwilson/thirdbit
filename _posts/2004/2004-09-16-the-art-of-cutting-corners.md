---
title: "The Art of Cutting Corners"
date: 2004-09-16 14:11:38
year: 2004
---
<p>According to one of my students, I tell the same jokes, the same way, every time I lecture.  I apparently make them sound fresh each time, though, so I guess that's OK.</p>

<p>I give the same introductory lectures to each new group of students as well.  In contrast with my jokes, that isn't because I can't think of anything new to say.  Instead, to paraphrase <a href="http://www.quotationspage.com/quote/27719.html">Tolstoy</a>, it's because all successful projects are alike, while all failures fail in their own way.  If you want to deliver usable software on time, without burning out, there are a few things you simply have to do, so I figure I might as well explain them at the start of each term.</p>

<p>The first thing I explain is how to run a meeting.  Circulate the agenda in advance by email, or write it up on the whiteboard; circulate minutes and action items afterward; and be polite (which in practice means "give everyone else a chance to speak too").  It isn't rocket science, but right now, out there, a room full of supposedly intelligent people are wasting an hour of their lives because they aren't following these simple rules.</p>

<p>The second thing I explain is what schedules are for.  Contrary to popular belief, a schedule's primary purpose is <em>not</em> to tell you what you're supposed to be doing on any given day.  Instead, its purpose is to tell you when you should start cutting corners.  Suppose, for example, that you have ten weeks in order to accomplish some task.  Five weeks after you start, you've only done the first four weeks' worth of work.  What are your options?</p>

<ol>

<li>Denial.  This is very popular, but doesn't actually solve the problem.</li>

<li>Tell yourself that you'll just have to work harder, and start putting in evenings and weekends.  This is also very popular, but ultimately self-defeating.  When you're tired, the quality of your work goes down; any ground you gain by working 'til three a.m. you lose again to extra debugging and rewriting.</li>

<li>Ask for more time.  Groups working in industry often do this (usually in combination with the previous solution), but it usually isn't an option in an academic setting.  Instructors have to submit marks at the end of the term; as far as the university is concerned, whatever hasn't been done by then might as well not be done at all.</li>

<li>Cut corners, either by doing less testing (which is quickly self-defeating), or by updating the schedule to reflect the rate at which you're <em>actually</em> working, and dropping features that you already know you won't be able to finish in time.</li>

</ol>

<p>Let's return to the earlier example.  At the start of the project, you believed it would take ten weeks.  You're now half-way through, and you've done 4/5 of the work you were supposed to.  Looking at it another way, your estimates for how long sub-tasks would take were too optimistic by about a quarter.  You should therefore go back to your schedule and add 1/4 to each task's estimate.  That inevitably means that some of the things you originally planned to do now spill off the end of your ten-week window.  That's OK; it's a shame you won't get to them, but at least you know it now, and can start taking action (like lowering your customer's expectations) well in advance of delivery.</p>

<p>But how do you decide what to cut out?  The Nevex group I work(ed) with used a very simple procedure, which previous undergraduate teams I've supervised have adopted as well.  When the project starts, make up a list of the features you intend to implement.  Rank each feature High, Medium, or Low on two different scales: how important you think it is, and how long you think it will take to implement.  That gives you a three-by-three grid, which you then use to make decisions.  Things which are quick to do, and important, are scheduled first; things which will take a long time, and are unimportant, aren't scheduled at all; and things which are on the diagonal in between are put on the back end of the schedule.  That way, when the time comes to cut corners, the things that fall off the wagon either aren't very important, or couldn't be done in the remaining time anyway.</p>

<p>The only hard step in this process is coming up with time estimates for particular tasks.  The first time you have to do this, it is very frustrating.  "How can I possibly guess how long it will take to write a database persistence layer for some Java classes?  I've never used a persistence layer before!"  Well, yes, that's true, but you've had to learn other new technologies before, and then apply them in courses.  A guess based on that experience might be off by a factor of two or three, but it probably won't be off by a factor of ten, and even if it is, it's better than no guess at all.  Plus, everyone in the Nevex group discovered that the more estimating they did, the better they got at doing it.  We had to add several completely new things every time we released a major version of our product, but in four and a half years, our worst schedule slippage was only six weeks on a year-long development cycle, with only a handful of late nights (where "late" means "work until 9:00 p.m. once a week").</p>

<p>Taking scheduling seriously is one of the things that distinguishes good software development teams from bad ones.  It's unfortunate that you'll only get to do it once during this course, since you only really see the benefits the second time around, but I hope that even once will be enough to convince you that it's worth doing.</p>
