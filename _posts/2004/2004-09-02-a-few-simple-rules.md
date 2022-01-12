---
title: "A Few Simple Rules"
date: 2004-09-02 16:29:47
year: 2004
---
<p>We held the post-mortem
for Helium this
morning.  Lots of things went wrong, but many more went right---it was
a fun, productive summer.</p>

<p>Lots of things contributed to the fun, but much of the productivity
can be attributed to one thing: everyone learned to use modern tools,
and adopted good working practices.  Many projects stumble or fail
because programmers aren't willing to do this---far too many, young as
well as old, still insist on using Vim, Emacs, and other legacy tools.
This doesn't just make <em>them</em> less productive; it also
handicaps the rest of the team, since it prevents people learning from
each other, sharing resources (such as useful keyboard macros),
doubling up to debug hard problems, and so on.</p>

<p>So, with that, the post-mortem,
and the <a href="http://www.joelonsoftware.com/articles/fog0000000043.html">Joel
Test</a> in hand, here are the rules by which this fall's projects
will be run:</p>

<table>

  <tr>
    <td align="right" valign="top">1.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Everything important is versioned.</b>
      Source code, web pages... anything and everything that you need
      to build, install, or debug the project goes into the Subversion
      repository.
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">2.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Everyone uses Eclipse.</b>
      And Ant.  And JUnit.  And all the
      <a href="http://pyre.third-bit.com/helium/docs/tools_and_technologies.html">other
      tools</a>
      that are part of the environment.  If you don't, you are slowing
      down your teammates, and making extra work for them.
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">3.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>The build is automated.</b>
      And all tests are re-run by default every time the project is
      built (which will be every 30 minutes, round the clock).
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">4.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Anything that isn't done immediately goes into the issue
      tracker.</b>
      Why?  Because even if you would remember it a month from now,
      teammates who weren't sitting with you when you slapped your
      forehead and said, "D'oh!" won't.
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">5.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Everyone writes tests,</b>
      preferably <em>before</em> they write the code itself.
      Take a look at Helium's
      <a href="http://pyre.third-bit.com/helium/#progress">progress
      chart</a>; one of the reasons the team go that far, that fast,
      was that they tested early, and tested often.  You owe it to
      your successors to do the same.
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">6.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Everyone fixes bugs.</b>
      Code is done when it's all typed in; code is done when it
      works, and "working" means "working for everyone, everywhere,
      every time".  (Yes, this means that most software is never
      done...)  When your tests turn up bugs, file 'em and fix 'em
      before implementing more features.  Experience shows that this
      will make your work faster, since you won't constantly be
      doubling back to shore up the foundations.
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">7.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Every large piece of work is sanity checked <em>before</em>
      code is written.</b>
      Thinking of reorganizing some of the data model classes?
      About to write forty new classes to handle threading of
      email conversations?  Grab a teammate and a whiteboard, and
      explain what you're about to do, or send email to the list,
      or fire up IM.  Anything, just as long as someone else gets
      a chance to tell you when you should switch back to decaf...
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">8.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Every meeting start with an agenda, and ends with minutes and
      an action list.</b>
      Where possible, the agenda should be circulated before the
      meeting begins; the minutes and actions <em>must</em> be
      circulated soon after it's over (and added to the project web
      site).
    </td>
  </tr>

  <tr>
    <td align="right" valign="top">9.</td>
    <td>&nbsp;&nbsp;</td>
    <td valign="top">
      <b>Have fun.</b>
      This is the most important rule of all.  ("Floggings will
      continue until morale improves...")  Your project isn't just
      about marks---it's about learning new things, making new
      friends, and building something you can be proud of.  Most of
      the students who've done projects in the past have had a lot
      of fun---we hope you will too.
    </td>
  </tr>

</table>
