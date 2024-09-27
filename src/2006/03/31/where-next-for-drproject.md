---
title: "Where Next for DrProject?"
date: 2006-03-31
---
It's time to start thinking about what to add to DrProject this summer. Please <a href="mailto:gvwilson@third-bit.com?subject=drproject-vote">vote</a> for any <em>two</em> of the following; I'll collate and re-post.
<ol>
  <li>web-based administration interface</li>
  <li>user-oriented pages</li>
  <li>status dashboard</li>
  <li>manual RSS feeds</li>
  <li>continuous integration</li>
  <li>pluggable authentication</li>
  <li>web services</li>
  <li>shared bookmarks</li>
  <li>calendaring</li>
</ol>
<strong>1. Web-Based Administration Interface</strong>

Instructors and TAs should be able to do simple things (like add a user to a project) through a web interface.  Jeff Okawa prototyped an admin interface in Fall 2005; we'll need to update that, extend it, and add it in.

<strong>2. User-Oriented Pages</strong>

This page would show a user all the tickets and timeline entries for all of the projects she belongs to, so that she doesn't have to cycle through three or four separate views to get a picture of what she's supposed to be doing.  Raheel Ashraf prototyped something like this in Fall 2005; we'd have to re-design from the ground up.

<strong>3. Status Dashboard</strong>

This is Maria's work from last summer—one form is a graphical display of what's in the timeline view for a single project, a second is a graphical display of the user-oriented page (#2), and a third (aimed at instructors) summarizes the status of all the projects in the system, so that problems can be spotted early.

<strong>4. Manual RSS Feeds</strong>

Right now, each project automatically generates an RSS feed of timeline items; there's no way for users to inject hand-written entries (like, "W00t!  We did it!").  The plan is to have a second RSS feed per project containing the hand-written entries, which would also show up in the timeline RSS; that way, when the latter is disabled (as it usually will be for student projects, because of the authentication problems we've discussed before), groups can still feed out selected information.

<strong>5. Continuous Integration</strong>

CI is the practice of rebuilding the software, and rerunning the tests, every time someone checks something in.  It's hard to do in the general case (how many different ways to build, and report build status, can you think of?), but if we can handle simple Ant and Make cases, that's probably enough…?

<strong>6. Pluggable Authentication</strong>

We decided a year ago to make the underlying Linux system responsible for user provisioning (i.e., accounts and passwords).  That's now proving awkward: in order to get the Foodbank project collaborators access to the source code and tickets, for example, we have to set them up with guest accounts on CDF.  A pluggable auth system would allow us to add our own accounts as needed (but would open up a big can of very squiggly worms).

<strong>7. Web Services</strong>

Providing either a REST or SOAP API to DrProject, so that it can be scripted remotely, should be relatively straightforward.  Throttling usage, so that students don't do silly things, will be more of a challenge…

<strong>8. Shared Bookmarks</strong>

A del.icio.us-style bookmarking system would allow students working on parallel projects to save useful links (pointers to relevant parts of the Java API, for example).  Dunno how much students would actually use it…

<strong>9. Calendaring</strong>

Finding times to meet, and keeping track of due dates, is one of the most tedious parts of student team projects.  A simple calendaring system that would let students mark off when they're available, and when assignments are due, would be useful—I question, though, how much they'd actually use it.
