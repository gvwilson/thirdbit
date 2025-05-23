---
title: "Questions, Answers, and Lessons"
date: 2016-04-24
original: swc
---
<p>
  While working on an outline of
  a new lesson on Python,
  I began thinking about the overall coherence of what we teach.
  In particular,
  I started to worry that we might be teaching some things because we teach them,
  i.e.,
  that the curriculum might lose its connection to researchers' actual issues.
</p>
<p>
  One method for keeping things grounded in the other field I still occasionally work in
  (empirical software engineering)
  is called <a href="https://en.wikipedia.org/wiki/GQM">Goal, Question, Metric</a>.
  As the name suggests,
  it defines three questions:
  what are you trying achieve,
  what questions do you need answered in order to achieve it,
  and what metrics will you accept as answers to those questions.
  An educational equivalent is Question, Answer, Lesson:
  what questions do novices have,
  what answers do competent practitioners give them,
  and what lessons are needed to teach those answers.
  (The "do novices have" modifier is crucial:
  in order for our workshops to be appealing,
  they must answer the questions that novices actually have,
  not the ones we wish they would ask.)
</p>
<p>
  Here's what I've come up with so far:
</p>
<table class="centered">
  <tr>
    <th>Questions</th>
    <th>Answers</th>
    <th>Lessons</th>
  </tr>
  <tr>
    <td>
      How can I choose what tool to use?
      <br>
      How can I get help/fix this?
      <br>
      How can I get started?
      <br>
      How can I work in a team?
      <br>
      How can I make my software more useful?
      <br>
      How can I get my software to do more?
      <br>
      How can I make my work reproducible?
      <br>
      How can I get the right answer?
      <br>
      How can I understand the project I've inherited?
    </td>
    <td>
      Automate tasks and analyses.
      <br>
      Avoid duplication.
      <br>
      Be welcoming.
      <br>
      Choose the right visualization.
      <br>
      Program defensively.
      <br>
      Document intention not implementation.
      <br>
      Use the experimental method.
      <br>
      Modularize software.
      <br>
      Normalize data.
      <br>
      Be open by default.
      <br>
      Organize projects consistently.
      <br>
      Do pre-commit reviews.
      <br>
      Publish software and data.
      <br>
      Reduce, re-use, recycle.
      <br>
      Create re-runnable tests.
      <br>
      Search the web.
      <br>
      Store raw data as it arrived.
      <br>
      Tune programs.
      <br>
      Understand data formats.
      <br>
      Understand error messages.
      <br>
      Understand how programs run.
      <br>
      Use checklists and to-do lists.
      <br>
      Use configuration files.
      <br>
      Use more hardware.
      <br>
      Use version control.
    </td>
    <td>
      Collaboration
      <br>
      Data Management
      <br>
      Make
      <br>
      Managing Software
      <br>
      Performance
      <br>
      Programming
      <br>
      Authoring and Publishing
      <br>
      Quality Assurance
      <br>
      Unix Shell
      <br>
      Version Control
      <br>
      Visualization
    </td>
  </tr>
</table>
<p>
  But by themselves,
  these three lists aren't very useful.
  What really matters is the connections between them:
  which answers address which questions,
  and which lessons teach the ideas used in those answers?
  The obvious way to represent this is as a graph,
  since both relationships are many-to-many.
  So far,
  though,
  I haven't produced anything better than this:
</p>
<p>
  <a href="@root/files/2016/04/design-01.svg"><img src="@root/files/2016/04/design-01.svg" width="80%" alt="Questions, Answers, and Lessons" class="centered"></a>
</p>
<p>
  (You can click on the image to see the full thing,
  or <a href="@root/files/2016/04/design-01.gv">look here</a> for the GraphViz source:
  run <code>dot -Tsvg design-01.gv &gt; design-01.svg</code> to regenerate the SVG.
  Note that I've added a fourth column to the graph to show the half-day modules within each lesson,
  primarily to give a sense of how much time would be devoted to what.)
</p>
<p>
  Drawing up these lists has already helped me figure out what we might teach in a two-week Carpentry-style class
  (a long-standing dream of mine),
  but:
</p>
<ol>
  <li>
    I'm pretty sure these still aren't the questions novices actually have, and
  </li>
  <li>
    as presently drawn, the graph is unreadable.
  </li>
</ol>
<p>
  The first is more important right now than the second,
  so I would be grateful for feedback to go with that I've already received from
  Jackie Kazil, Noam Ross, Karen Cranston, and Andromeda Yelton.
  Please add comments to this post about which questions you'd add, delete, or change,
  and what you think the answers should be.
</p>
