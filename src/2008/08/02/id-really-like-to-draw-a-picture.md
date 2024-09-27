---
title: "I'd Really Like To Draw A Picture…"
date: 2008-08-02
---
I'd like to draw a picture—I really would. It wouldn't exactly be an entity-relationship diagram, or a database schema, but it would combine elements of both, and it would help me explain the model underlying the app I'm currently working on to the whole team (myself included).  But I'm not going to bother, because experience has taught me that it will cost too much to maintain:
<ol>
  <li>There isn't a decent lightweight open source cross-platform drawing tool for this kind of thing: Inkscape and Dia just don't measure up to Visio and Omnigraffle.</li>
  <li>There aren't tools to check those diagrams against actual schemas, or vice versa. Well, OK, there are, but all the ones I have found can only check drawings they've created (i.e., they conflate drawing with checking), and none of them talk directly to ORM code like SQLAlchemy or Hibernate.</li>
  <li>Most importantly, version control systems don't know how to handle diagrams, even ones stored in SVG or other pseudo-text-based formats. I want "svn diff" to be able to tell me what's change between the last version of the diagram and this one; I <em>hate</em> launching two versions of a drawing application side by side and playing "spot the change".  I want merge, too—if Jeff and I are both working on a complex design, I don't want our tools to make the job even more complex.</li>
</ol>
So here I am, doodling in my notebook instead of creating something I can actually share with my fellow developers. Pfah.
