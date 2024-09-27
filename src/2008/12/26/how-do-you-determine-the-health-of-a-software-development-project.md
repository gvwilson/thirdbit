---
title: "How Do You Determine the Health of a Software Development Project?"
date: 2008-12-26
---
This one has come up before, but with a near year dawning, I think it's worth revisiting.  Suppose you had been asked to audit a medium-sized software development project—something with a couple of dozen people, split between two or three sites, with a couple of hundred thousand lines of moderately complex code already written.  What would you do to determine how healthy the it was? Obvious things include:
<ol>
  <li>Ask the team how positive they feel about what they're doing. (Happy teams aren't always productive, but unhappy teams almost never are.)</li>
  <li>Compare their actual development practices against some kind of checklist.  (Version control? Yup.  Test-driven development?  No, but most people still don't actually do that.  <em>Some</em> testing, with continuous build on the back-end, is a more reasonable expectation…)</li>
  <li>Read their code.  In my experience, this is a lot more work than the previous two options, primarily because most projects don't have a useful architectural overview.</li>
  <li>Help them out for a few days (e.g., do some testing).</li>
</ol>
What else? What would you do, and why?

Now put your answer aside, and answer a slightly different question. What would you do if you were faced with a dozen teams, each with four to six people and roughly ten thousand lines of code?  This is the situation hundreds of lecturers like me face every term when teaching project-based software engineering classes to undergraduates, and all of the strategies above fail:
<ol>
  <li>By definition, student teams are composed of novices who don't (yet) know how to work productively in teams, so asking them how they think they're doing is sort of like asking a random number generator.</li>
  <li>Comparing their development practices against a checklist fails because you either publish the checklist or you don't. If you do, students work to that whether they believe in it or not. If you don't, you're playing "I've got a secret and I won't tell", which doesn't do a lot for morale.</li>
  <li>Reading their code has the same problem; it also measures what they produce, rather than how they produce it, and the latter is really what we ought to be teaching.</li>
  <li>Helping them out for a few days (or sitting in on team meetings) would be the best method, but there simply aren't enough hours in the week.</li>
</ol>
Pious hopes and protestations notwithstanding, students mostly learn what's assessed.  This is partly an economic decision (given a choice between putting hours into something that will show up on their transcript, and something that won't, the former is the rational strategy), but it's also true that if we grade one thing and not another, we're sending a pretty clear signal that we think the first is more important than the second. I therefore believe that if we can't come up with robust, affordable ways to give students marks for how they build software, we will continue to produce graduates who know how to write legal Java or Python, but not how to build real-world applications without heroic effort. I'd welcome your proposals…
