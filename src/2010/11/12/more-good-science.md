---
title: "More Good Science"
date: 2010-11-12
---
We're starting to get feedback on <a href="http://oreilly.com/catalog/9780596808303"><em>Making Software</em></a>, most of it positive (but some of it grumpy: "how dare your evidence contradict my cherished belief!"). Here are two recent papers that aren't in the book, but will give you a taste of what is:

Rossbach, Hofmann, and Witchel: "Is Transactional Programming Actually Easier?" In <em>Proc. 15th ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming</em>. The question they set out to answer is, does software transactional memory (STM) make parallel programming easier or not? From their abstract:
<blockquote>In this paper, we describe a user-study in which 147 undergraduate students in an operating systems course implemented the same programs using coarse and fine-grain locks, monitors, and transactions. We surveyed the students after the assignment, and examined their code to determine the types and frequency of programming errors for each synchronization technique. Inexperienced programmers found baroque syntax a barrier to entry for transactional programming. On average, subjective evaluation showed that students found transactions harder to use than coarse-grain locks, but slightly easier to use than fine-grained locks. Detailed examination of synchronization errors in the students' code tells a rather different story. Overwhelmingly, the number and types of programming errors the students made was much lower for transactions than for locks. On a similar programming problem, over 70% of students made errors with fine-grained locking, while less than 10% made errors with transactions.</blockquote>
In other words, students did better, but thought they did worse. This is interesting for a whole bunch of reasons (not least that for highlighting how flaky subjective self-assessment is).

Bird, Nagappan, Murphy, Gall, and Devanbu: "An Analysis of the Effect of Code Ownership on Software Quality across Windows, Eclipse, and Firefox."

From their abstract:
<blockquote>We examine the relationship between different ownership measures and software faults/failures in three large software projects drawn from different process domains: Windows Vista, the Eclipse Java IDE, and the Firefox Web Browser. We find that in all cases, measures of ownership such as the number of low-expertise developers, and the proportion of ownership for the top owner have a relationship with both pre-release faults and post-release failures. However, we find that the strength of the effects is related to the development process used. Vista shows the strongest relationship with ownership level, followed by Eclipse, and then Firefox, suggesting that the more that a project uses an open source style process, the more that team sizes rather than ownership levels affect failures. We also find reasons that low-expertise developers make changes to components and show that the removal of low-expertise contributions dramatically decreases the performance of contribution-based defect prediction.</blockquote>
They are painstaking in defining what they mean by "ownership", and how they measure it, so that other people can (and should!) replicate their work. Drilling down, their conclusions are:
<ul>
  <li>Vista:
<ol>
  <li>The number of minor contributors has a strong positive relationship with both pre- and post-release failures even when controlling for metrics such as size, churn, and complexity.</li>
  <li>Higher levels of ownership for the top contributor to a component results in fewer failures when controlling for the same metrics, but the effect is smaller than the number of minor contributors.</li>
  <li>Ownership has a stronger relationship with pre-release failures than post-release failures.</li>
</ol>
</li>
  <li>Eclipse:
<ol>
  <li>Both MINOR and TOTAL (defined in the paper) have a positive relationship with pre- and post-release defects. However, neither is consistently a better indicator, and the effect is weaker than in Vista.</li>
  <li>Higher levels of Ownership sometimes have a positive relationship with pre- and post-release quality, but the effect is small when it is statistically significant.</li>
  <li>Ownership measures have a slightly larger effect on pre-release failures than post-release failures.</li>
</ol>
</li>
  <li>Firefox:
<ol>
  <li>Team size has a stronger relationship with defects than ownership levels.</li>
  <li>Team size and ownership metrics have a much stronger relationship with pre-release defects than post-release defects.</li>
</ol>
</li>
</ul>
This is cool: we can measure important things, we can see how they relate to other important things, and (crucially) we can <em>act</em> on what we see. I'm looking forward to seeing what both groups do next.
