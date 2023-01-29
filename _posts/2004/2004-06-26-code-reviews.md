---
title: "Code Reviews"
date: 2004-06-26 17:32:37
year: 2004
---
<p>People talk about code reviews far more often than they do them, despite the fact that everyone (reviewers and coders alike) seems to get a lot out of them.  We've been talking about implementing code reviews in my real job for almost four years, but have never actually gotten around to doing it.</p>

<p>So, I marked up 48 pages of Helium on the way back from Montreal last Sunday, and spent a couple of hours going over it with the team Monday morning.  We covered everything from low-level formatting and out-of-date JavaDoc, to <a href="#1">asymmetrical class design</a> and
<a href="#2">poor choice of data structures</a>.  I learned a lot about why the code is structured the way it is—in particular, about some of the restrictions and requirements associated with <a href="http://www.hibernate.org">Hibernate</a>—while the team came away with a much better idea of what they're actually expected to do.  Three and a half hours of reading, two hours of talking—I think it was a good investment.</p>

<p>I'd really like to get code reviews into the undergraduate curriculum. The major obstacle is the chicken-and-egg problem: most instructors and TAs have never been subjected to a code review, so how can they teach students how to do them? <a>Reading Code</a>, by Diomidis Spinellis, is a start, but (a) it's very C-oriented, (b) it's more about reading code than reviewing it, and (c) who has time to read several hundred pages in order to put together a lecture or two?</p>

<p>One possibility (which some study group members are investigating) is to use code metrics to identify suspicious code segments, and focus on reviewing those. For an example of a metrics-driven review process, see <a href="http://blogs.msdn.com/mswanson/articles/154460.aspx">this article</a> by Michael Swanson.  It's also worth reading the <a href="http://www.mozilla.org/hacking/code-review-faq.html">Mozilla Code Review FAQ</a> to get an idea of how a large open source project handles this.</p>

<p>[<a name="1">1</a>] Asymmetrical class design means that two classes that seem to do similar things do them differently; in Helium's case, this is required by our object/relational mapping layer, <a href="http://www.hibernate.org">Hibernate</a>.</p>

<p>[<a name="2">2</a>] Helium's data model contains users, user groups (which are sets of users or other user groups), projects (which are organized in a tree), and memberships (each of which represents a single user or user group's association with a single project). Right now, each <code>UserGroup</code> stores its members in a <code>Set</code>.  This allows fast lookup, but only if you already have the object you're looking for.  In most cases, the code actually iterates through the set's members, comparing a user's name with the name recorded in the set entry.  A cleverer data structure would allow lookup either by object identity or by name, but would require more work to maintain consistency.  I've told team members not to worry about it for now, since we're not going to bump into performance problems for a long, long time...</p>
