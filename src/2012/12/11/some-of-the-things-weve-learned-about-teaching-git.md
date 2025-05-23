---
title: Some of the Things We've Learned About Teaching Git
date: 2012-12-11
original: swc
---
<p>We've tried teaching Git six or seven times now; here's what some of the instructors have learned.</p>
<ul>
  <li><strong>Instructor #1</strong>
    <ul>
      <li>I spent too much time explaining the "stage." It's an important concept that sets git apart from other VCSes, but for beginning students it's probably too advanced.</li>
      <li>I wish I had used a more realistic project with several files and a history of logs. Creating a new project live is useful in teaching how to set up a git repository, but then I'm limited to working with a small history.</li>
      <li>I left the GitHub discussion until the end, and because we were tight for time I was not able to really get into it. I wish I had started to talk about GitHub early on, maybe as soon as their first commit.</li>
    </ul>
  </li>
  <li><strong>Instructor #2</strong>
    <ul>
      <li>I should have left out the part where folks set up their Git SSH keys. It's just not worth the confusion and only helps folks by letting them avoid typing in their passwords. Since more people understand passwords than SSH keys, just skip the SSH key set up part.</li>
      <li>Also, I think I could have crammed in more content if the examples early on had been better/more time efficient. I would have liked to cover "git commit -amend," "git reset", "git merge --no-ff", various workflows, the importance of keeping your main branches clean and working in side branches, etc.</li>
      <li>I also would have liked to end the whole thing with a more elaborate (though straightforward, ideally) exercise that folks work on by themselves, encounter conflicts, etc. As it stands in my notes, they only really encounter a conflict once.</li>
      <li>Talking about local version control all the way through branches was good for me, but, as Instructor #1 suggests, it was helpful to introduce github immediately after branches and <em>as soon as</em> remotes come up.</li>
    </ul>
  </li>
  <li><strong>Instructor #3</strong>
    <ul>
      <li>Don't pretend it's SVN or anything, just teach git as Git.</li>
      <li>Use lots and lots of graphics and demonstrations, especially demonstrations of opposing cases, e.g., here's a pull where everything went great, here's a pull with a conflict, or here's a push that goes smoothly, and here's what happens when your local copy is out of date.</li>
    </ul>
  </li>
</ul>
