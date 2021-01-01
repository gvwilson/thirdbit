---
title: "What We've Learned"
date: 2010-03-02 09:18:08
year: 2010
---
My talk at <a href="http://us.pycon.org/2010">PyCon 2010</a> was titled "What We've Learned From Building Basie (and lots of other software using student labor over the course of eight years)".  The <a href="http://www.slideshare.net/gvwilson/what-weve-learned-from-building-basie-3241279">slides</a> are up on Slideshare, and there's <a href="http://blip.tv/file/3260995">video</a> of the talk itself on blip.tv, but I thought readers of this blog might be interested in a summary.

My starting point is Joel Spolsky's <a href="http://joelonsoftware.com/items/2009/10/26.html&lt;/p&gt; &lt;p&gt;">comment</a> that, "...student projects, while laudatory, frequently fail to deliver anything useful."  Respectfully, I beg to differ: About a quarter of the student projects I've helped supervise since 2002 have delivered software that clients actually used, and the rest have produced something even more useful: experience.  (And when I say "about a quarter", I'm talking about a quarter of 368 people from 35 countries of origin working on 136 projects.)

To make a long story short, undergraduate students <em>can</em> build great software if:
<ol>
	<li>you have realistic expectations,</li>
	<li>you're patient, and</li>
	<li>you realize that "how" matters more than "what".</li>
</ol>
Let's take those in order.

<strong>Realistic Expectations.</strong> Most undergrads are doing five courses at once, which leaves them only 8-10 hours/week per course.  Putting it another way, 13 weeks of student time is equivalent to 3 weeks of full-time work.  When you're planning projects, you therefore have to ask yourself how much you would expect a new (junior) hire to do in their first three weeks on the job, particularly if (as is often the case with students) they'd never used the tools or worked in the application domain before.

It's equally important to have realistic expectations of faculty, most of whom are working even harder than their students.  A colleague of mine once summed up professorial life by saying, "We're here to do research, they pay us to teach, and we spend our time on admin."  Keep in mind that computer science professors care about computer science, which is emphatically <em>not</em> the same thing as programming.  Computer science is the scientific study of what computers can do; a computer scientist's job is to invent (or discover, depending on your philosophical point of view) new knowledge.  That sometimes involves writing code, but that's like saying that mathematics sometimes involves doing integrals.

It took me a long time to understand this, and <a href="http://mail.python.org/pipermail/edu-sig/2006-September/007031.html">I'm not the only one</a> to misunderstand this.  I believe very strongly that being a better programmer can help someone be a better computer scientist, but if you want any traction in academa at all, you have to remember that programming really is just a means to an end.

<strong>Patience.</strong> Your project may be the first time students have written something that isn't just going to be marked and thrown away.  It may also be the first time they've been in a situation where 90% right is a failure rather than an A.  You <em>must not</em> make students feel like failures for working the way the educational system has trained them to, even (or especially) if those ways are wrong.

Aside #1: one of the best students I've ever had explained to me several years ago why she always left her assignments until the last possible moment.  "If I start early," she said, "I'm the one who has to ask the prof all the questions to clear up what the assignment actually means.  And if I start early, the odds are good that one of the prof's answers will mean I have to re-do something.  On the other hand, if I leave it 'til the night before, I can be sure that I have a stable spec."

Aside #2: People often ask why schools don't  teach students Git, or Haskell, or GPU programming, or mobile devlopment, or whatever else is currently cool.  The answer is that <em>the curriculum is full</em>.  4 years × 2 terms/year × 13 weeks is 4800 hours, and every single one of those hours is spoken for.  Do you want to add functional programming?  Cool!  What are you going to take out: operating systems or B-trees?

<strong>How Matters More Than What.</strong> When I ask alumni of my project courses what the most valuable thing they learned was, none of them name a particular technology---none.  Instead, they talk about teamwork, presentation skills, code reviews, time management, prioritization, communication, negotiating real requirements with real users, and building their network and portfolio.  This is why I think that efforts to <a href="http://teachingopensource.org">teach open source</a> are slightly mis-aimed: in my experience, students don't care if the code is open or closed nearly as much as they care about how to build complex things.  It just happens that the various open source communities are both good at that, and able to talk <a href="http://producingoss.com">publicly and in detail</a> about the mechanics.

My colleagues and I at the <a href="http://www.cs.utoronto.ca">University of Toronto</a> have learned a lot of other things about running student projects, including:
<ul>
	<li>How to run meetings</li>
	<li>How to teach students how to do code reviews</li>
	<li>What level of tooling is appropriate/feasible</li>
	<li>Accountability</li>
	<li>How to accelerate ramp-up</li>
	<li>Carry-overs from previous terms</li>
	<li>Importance of full-time summer work (yay <a href="http://code.google.com/soc/">GSoC</a>!)</li>
	<li>Industry support</li>
	<li>Presentations, presentations, presentations</li>
	<li>Scoping and re-scoping deliverables</li>
	<li>Recruiting students and faculty</li>
	<li>How to grade one-of-a-kind projects</li>
</ul>
We're now scaling up what we've learned in <a href="http://ucosp.wordpress.com">UCOSP</a>, a set of undergraduate capstone projects in which students from 14 universities work together in distributed teams.  If you're interested in taking part, we'd <a href="mailto:gvwilson@cs.utoronto.ca">like to hear from you</a>.
