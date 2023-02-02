---
title: "Three Rules for Supervising Student Programming Projects"
date: 2010-08-25 18:01:09
year: 2010
---
<a href="http://jendodd.com">Jen Dodd</a> recently posted an article titled "<a href="http://jendodd.com/2010/08/16/3-rules-for-running-events/">3 rules for running events</a>", plus one metarule that I particularly appreciated: "Stop deluding yourself."  In the same spirit, I'd like to offer up three rules for running student programming projects.  To set the stage, here's the number of student programming projects I've organized, supervised, or otherwise been guilty of since <a href="http://en.wikipedia.org/wiki/David_Wallace_%28physicist%29">David Wallace</a> first asked me to look after a couple of summer interns in Edinburgh half a lifetime ago:
<div>

<img alt="students-supervised-per-year" src="{{'/files/2010/08/students-supervised-per-year.png' | relative_url}}" alt="Students Supervised per Year" width="525" height="291" class="centered">
<table class="centered">
<tbody>
<tr>
<td>Year</td>
<td>1987</td>
<td>1988</td>
<td>1989</td>
<td>1990</td>
<td>1991</td>
<td>2002</td>
<td>2003</td>
<td>2004</td>
<td>2005</td>
<td>2006</td>
<td>2007</td>
<td>2008</td>
<td>2009</td>
<td>2010</td>
</tr>
<tr>
<td>Number</td>
<td>2</td>
<td>4</td>
<td>12</td>
<td>14</td>
<td>26</td>
<td>7</td>
<td>13</td>
<td>35</td>
<td>42</td>
<td>34</td>
<td>38</td>
<td>78</td>
<td>110</td>
<td>49</td>
</tr>
</tbody>
</table>
</div>
Yes, the numbers for 2008 and 2009 are crazy, but those are the years I ran consulting projects at the <a href="http://www.utoronto.ca">University of Toronto</a> and started <a href="http://ucosp.ca">UCOSP</a>.  If you only count students I directly supervised, the numbers for 2008-09 drop back down to the high thirties–say, a dozen or so per term, three terms a year.

So what have I learned in those 23 years?
<h2>Rule 1: It's Not Thirteen Weeks, It's Three</h2>
This was the hardest one for me to learn, and it's almost always the hardest to get across to both students and their clients.  University terms may be thirteen weeks long, but students are usually juggling five courses, and many have part-time jobs as well.  That means they can only put eight hours a week into their project without sacrificing grades somewhere else.  If you figure a full-time work week is 35 hours, that means students actually spend 8×13/35 = a bit less than three weeks working for you.  In that time, they have to:
<ul>
  <li>figure out what problem they're actually going to solve,</li>
  <li>learn some new technologies,</li>
  <li>digest the existing code base,</li>
  <li>get to know their teammates,</li>
  <li>build something, and</li>
  <li>jump through whatever hoops are required for getting a grade, like writing a final report or some documentation that no-one will ever read.</li>
</ul>
That's an awful lot to squeeze into three weeks: very few open source projects expect their <a href="http://code.google.com/soc/">GSoC</a> students to start checking things in after three weeks of full-time work, but students in school are expected to be <em>done</em> in that time.  Prof. <a href="http://www.cs.utoronto.ca/~reid">Karen Reid</a> says that she usually divides the term into three pieces:
<blockquote>I find that I spend the first 3 weeks working hard to get the students up to speed and essentially demanding that they get something real done in the first 3 weeks.  In other words, my students are more successful if they push hard at the beginning. After that, they usually have a good idea of what they need to do for the remainder of the term and I can kind of let them set the pace.  Then I spend the last 3 weeks defining what it means to be done.</blockquote>
There's another catch lurking in here too.  The iron triangle of project management is scope, schedule, and resources.  In a student project, both the schedule and resources are fixed (13 weeks and N students respectively), so the only thing that can give is scope.  There are two ways to reduce it: lower quality, or fewer features.  Lowering quality is self-defeating–the students you want in a project course are the ones who take pride in their work and care about their grades (which aren't necessarily the same thing), and they're not going to like being told that the only way to pass a course is to produce crap.

That leaves the number and scope of features as the only free variable.  Problem is, neither students nor clients are going to be excited about fixing a couple of minor bugs or adding one small new feature.  If you want to get people on board, you have to aim higher, and be willing and able to reduce scope as the term goes on without making anyone feel like the project has failed–which brings us neatly to our second rule.
<h2>Rule 2: It's Not About Technology</h2>
It really isn't.  When I ask students I've supervised in the past what they learned in their project, they never mention technology–never.  They might have learned Ruby on Rails, or CUDA, or touch-screen interface design, or database performance optimization, but that's not what they remember afterward.  What sticks is how to run a project: how to run a progress meeting, review someone else's code, manage their time, present their work in five minutes or less, and negotiate scope with a client.

I've tried teaching these things in regular software engineering classes, but it has never worked.  (This is one of the reasons I have so little use for <a href="http://www.amazon.com/Software-Engineering-9th-Ian-Sommerville/dp/0137035152">standard</a> <a href="http://www.amazon.com/Software-Engineering-Practitioners-Roger-Pressman/dp/0073375977">undergrad</a> software engineering textbooks: you can talk about riding bicycles all you want, but the only way to learn how to do it is to <em>do it</em>.)  On the upside, once I students understand that I'm trying to teach them process, rather than technology, the problems I mentioned in the previous section are greatly reduced: cutting the set of features we're going to deliver, for example, becomes an exercise in scope negotiation rather than a failure on the students' part.

So what goes into a rational student-oriented development process?
<ol>
  <li>A weekly status meeting (face-to-face if possible, online if not).  Whoever is running it (me for the first few, one student in turn thereafter) is responsible for drawing up an agenda and posting a summary afterward.  They're also responsible for checking that the previous week's to-do items were completed, and for keeping the meeting on track (politely, but firmly).  The first meeting each term usually runs 90 minutes or so; by the end of term, we can do them in 45 minutes or less.</li>
  <li>Version control, ticketing, a blog, an archived mailing list, an IRC channel, and (most recently) <a href="http://www.reviewboard.org/">code review</a>–in short, the same infrastructure you'd use for a small open source project.  You'll note that "wiki" isn't on the list: we've set them up in the past, but no one has ever made much use of them.  You'll also note that five of these six items are about communication–all six, actually, if you think of version control as a way to share files.</li>
  <li>Demos and presentations.  I emphasize this less when project teams are distributed across several universities, but if they're collocated, I expect every team to present or demo weekly or every couple of weeks.  I usually don't give grades for each presentation or demo except to cure procrastination.</li>
</ol>
And that's about it.  On some projects, I'll ask students to draw up a plan for the term at the end of their second or third week (i.e., once they've learned something about the problem–if they have to do it at the start of term, waterfall-style, all they can do is write some science fiction and hope I won't hold them to it).  On others, there's some formality around handing off their code to their client, such as submitting it as a patch, doing a presentation at the client site, or showing off their work to all comers at a local pub.

Other people handle process differently, of course.  Andrew Ross, of Ingres, says:
<blockquote>I tend not to have regular weekly meetings with my teams. Instead, we have meetings as needed to discuss things that can't be covered acceptably in emails/IM's/IRC/calls. We do the latter constantly. The more important underlying concept is keeping students from drifting away and losing contact.</blockquote>
<h2>Rule 3: Steady Beats Smart Every Time</h2>
I once had three students working on separate projects during the same summer term.  Two had straight A's; the third was struggling to maintain a low 'B' average, but he's the only one I would have hired back, because he was the only one I could actually rely on.  One of the 'A' students had spent his whole life acing exams, and didn't know how to do anything else.  He panicked when asked, "What do you think we should do next?" Literally–you could see his pulse race and his mouth dry out.  The second had the same fatal flaw I had when I was twenty: he'd do the first three quarters of every job in record time, but getting the next 20% out of him was like pulling teeth, and the last 5% never got done all.

The third student, though, was as reliable as a grilled cheese sandwich.  If he told me on Monday that something was going to be done on Friday, it was done on Friday; when I asked him, "Where are you?" he always gave me a straight answer: no "almost done", no "just another couple of bugs" if he hadn't actually started.  It took me a couple of months to appreciate him, but once I did, I started looking for that same quality in every student I interviewed.

Of course, this isn't to say that every student with low grades is a gem waiting to be uncovered, or that everyone with an 'A' average is unreliable.  Far from it: grades <em>are</em> a fairly reliable indicator of ability and persistence, especially grades in courses that no one loves.  But the correlation is a lot weaker than I, a former 'A' student, once believed.

Keep in mind that even the steadiest students will doubt themselves sometimes.  Quoting <a href="http://www.cs.utoronto.ca/~reid">Karen Reid</a> again:
<blockquote>I find I spend a lot of time reassuring students who are climbing the learning curve.  Having different levels of expectations for students depending on their background is something I have to explain to students used to the same evaluation standards.</blockquote>
And "steady beats smart" applies to supervisors as well as students.  If you're unreliable–if you miss meetings, promise to do things but don't get around to them, or pretend to know more about technical matters than you actually do–your students will respond in kind.  If you can't or don't commit at least 3-4 high-quality hours a week for each project you're running, it would be better for everyone if you did something else.  (This is, by the way, one of the many reasons I prefer team projects to individual ones: the number of hours required per project grows only slowly with the team size, at least up to half a dozen students, so you can reach more students without sacrificing everything else.)

And finally, a metarule:
<h2>Have Fun</h2>
Students won't ever enjoy a project more than you do.  After all, they have to do all the hard work, like tracking down bugs, while you get to do the fun stuff like argue over what it's all supposed to do.  And if you're not having fun, they will quickly start to treat the project like just another course.  It's very hard to pull out of that downward spiral, so don't get into it: no matter what happens, grit your teeth and have some fun.  Go out for ice cream; borrow a projector and introduce them to <cite>Tron</cite>, <cite>WarGames</cite>, or <cite>Startup.com</cite>.  They'll remember that long after the course is over, too, and so will you.

<em>Later: a <a href="http://www.futurity.org/society-culture/what-makes-us-happy-can-make-us-sad/">recent study</a> confirmed what most of us probably knew already: what makes people happiest (or saddest) are group events and achievements, not individual accomplishments.  Maybe that's why students enjoy team projects, and come away appreciating most what they learned about teamwork rather than technology…</em>
