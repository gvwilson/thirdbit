---
title: "Three Paradigms (or, Why LLC Should Teach Javascript)"
date: 2011-08-25
---
Mark Guzdial recently posted another <a href="http://computinged.wordpress.com/2011/08/23/why-we-ought-to-teach-java-computing-education-and-social-practice/">thought-provoking piece</a> on computing education that has some direct implications for a project here in Toronto called <a href="http://ladieslearningcode.tumblr.com/">Ladies Learning Code</a> (and for other projects Software Carpentry). In his post, Mark summarizes a 1996 paper by Greeno, Collins, and Resnick that summarizes three views of education:
<ol>
  <li>Behaviorist: education is a matter of stimulus and response.</li>
  <li>Cognitive: education is about building and applying knowledge structures.</li>
  <li>Situated: education is about making people more successful members of a community of practice.</li>
</ol>
All three views are valid: they all provoke useful questions, make testable predictions, and so on. #2 (which is associated with people like Piaget) is probably the dominant paradigm today, but Mark's point is that #3 is equally important. Real-world problems are rarely solved by hermits working in complete isolation; instead, we go through apprenticeships, share sub-problems with colleagues, and hang out on Stack Overflow.

So what's this got to do with LLC? Well, if you're going to teach people to program, you have to pick a programming language. As a computer scientist, I'm drawn to elegant little languages like Scheme–but that's paradigm #2 talking. "We must use language X, so that we can focus on fundamental principles that students will use for the rest of their lives" <em>isn't useful</em> if those students are going to be interacting with people who speak a different language, just as teaching the fundamental principles of grammar and composition in Latin isn't useful if people are going to work in English or Mandarin.

Mark knows better than anyone that Java is a bad language to use with novice programmers–he and his group have been studying the broader question for years. Despite that, he accepts that computer science students have to learn Java at some point in order to take part in the community of practice that is professional programming. It's an echo of Joel Spolsky's argument that every serious programmer has to learn C: other than examples in class, I haven't written any C (or C++) in almost ten years, but I simply couldn't take part in some discussions with my peers without knowing what structs and pointers are.

I personally think that Javascript is a less-than-ideal language for teaching novices: it violates the <a href="http://en.wikipedia.org/wiki/Principle_of_least_astonishment">Principle of Least Astonishment</a> almost as often as Inglish speling. Despite that, I think it's the only sensible choice for something like LLC: like it or not, it's the lingua franca of the web. If the goal of LLC is to get participants to the point where they can bootstrap themselves in the time they can actually spare for this (remember, they all have jobs and families–they're doing this on the side), then Javascript's flaws are less significant than its community and utility.

This still leaves a lot of questions, of course. Should it be taught language-first, or should libraries like jQuery be introduced right from the start? What about things like Processing.js: after all, Guzdial's research shows that a media-first approach attracts and retains a wider range of people. I think trial and error is the only solution, but even the "errors" will be useful and fun, and how often can you say <em>that</em> with a straight face?
