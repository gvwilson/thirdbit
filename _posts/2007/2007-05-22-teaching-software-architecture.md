---
title: "Teaching Software Architecture"
date: 2007-05-22 08:46:34
year: 2007
---
<a href="http://www.cs.toronto.edu">Our department</a> has had a fourth-year course called "CSC407: Software Architecture" for several years. I taught it for the first time last summer, and had a lot of trouble figuring out what to put in front of students. Design patterns and basic queueing theory were no-brainers, but everything beyond that---everything that people point to when they say "software architecture"---seemed too ethereal for students. Take <a href="http://www.win.tue.nl/~mchaudro/sa2004/Kruchten4+1.pdf">Kruchten's 4+1</a> views, for example: it's a very useful way to think about software systems, but if you've never had to find your way around a really large application, the motivation and ideas are bound to seem a little abstract.

I taught the course for the second time in the fall; I was a little happier with it (thanks in large part to books like [<a href="http://www.amazon.com/Software-Architecture-Primer-John-Reekie/dp/0646458418">1</a>] and [<a href="http://www.amazon.com/Essential-Software-Architecture-Ian-Gorton/dp/3540287132">2</a>]), but only a little. This winter, though, I found something that seemed to work well. I asked students to compare and contrast the architectures of two competing open source applications: two editors, two racing games, two peer-to-peer file sharing systems, and so on. Students worked in pairs; a little over half of the teams divided the work by application, while the rest divided the work by topic (i.e., one person wrote most or all of each of the required papers). Several pairs gave me permission to post their work to show what they accomplished; I've put links to one series of submissions below, and will get others up when I have time.

Students enjoyed the exercise; most of them put a fair bit of effort into it, and appreciated the chance to learn some more about open source applications. More importantly (to me, at least), they seemed to learn a fair bit about software architecture as well. I'd be very interested in hearing from anyone else who has tried something like this.

Exercise 1
<ul>
  <li>domain.pdf: a one-page summary of the problem(s) your applications are intended to solve.</li>
  <li>differences.pdf: a one-page summary of the major differences between the features of the two applications.</li>
  <li>organization.pdf: a four-page description of the layout of the applications' code. If the application relies on configuration or data files at runtime, you must describe those as well.</li>
</ul>
Exercise 2
<ul>
  <li>conceptual.pdf: the conceptual architectures of the two applications.</li>
  <li>implementation.pdf: the applications' implementation architectures.</li>
  <li>execution.pdf: the execution architectures of the two applications.</li>
  <li>useful.pdf: which of these three views is the most useful in understand the applications, and the differences between them?</li>
</ul>
Exercise 3
<ul>
  <li>critique.pdf: a short critique of the architectures of the applications.</li>
  <li>extension.pdf: design an extension to the applications.</li>
</ul>
