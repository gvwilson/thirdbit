---
title: "Getting Balls Rolling in the Real World"
date: 2004-06-25 12:18:26
year: 2004
---
<p>Many books describe how to get a project rolling.  Unfortunately, none of their descriptions match anything I've ever seen in the real world.  For example, Rosenberg and Scott's <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0201432897">Use Case Driven Object Modeling with UML</a> tells readers to write use cases (actor X does Y to achieve result Z), then extract system features from them. At the other end of the spectrum, Extreme Programming advocates pretty much the same approach; all that differs is how much you do in one go.</p>

<p>But how can you write use cases unless you know what the system is going to include?  We intended to start Helium by writing use cases, but quickly ran into sand.  Do we need a use case for "user joins user group"?  Well, that depends: does our system have user groups?  What about "administrator removes user from user group"—are there administrators? Mailing lists? Permissions?</p>

<p>What we actually wound up doing was stepping back and developing a conceptual model that specified Helium's major entities. It was frustrating, since we couldn't decide what to include until we knew what the system had to be able to do, but couldn't specify what the system could do until we knew what it contained.</p>

<p>I think the reason software process books don't emphasize this crucial stage is that there's really not a lot you can say about it. It's like asking an author, "Where do you get ideas for stories?"  Or a cyclist, "How do you ride a bike?"  I believe that you can <em>show</em> people how to do it, and coach them to help them improve, but descriptions are either banal abstractions ("Think outside the box!") or case studies ("So then we decided to separate roles from memberships").</p>

<p>I therefore think that one-on-one (or one-on-very-few) collaboration is as important in computing education as it is to music or swimming. Lectures and books can teach content, but not method, and twenty-five years of research have shown that method is what matters most.  Since schools can't afford to hire one instructor for every five or ten students (even for just a couple of courses), the best we can do is build tools that encourage students to do things the right way.  That's  Helium's real goal; we should know in a couple of years whether we've achieved it.</p>

<p>Quote of the day:</p>

<blockquote><p>
<em>
The fantasy element that explains the appeal of dungeon-clearing  games to many programmers is
neither the fire-breathing monsters nor  the milky-skinned, semi-clad sirens; it is the experience
of carrying  out a task from start to finish without user requirements changing.
</em>
<br />
 - Thomas L. Holaday
</p></blockquote>
