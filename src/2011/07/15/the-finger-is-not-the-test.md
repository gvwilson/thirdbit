---
title: "The Finger Is Not The Test"
date: 2011-07-15
---
When Buddhists want to remind themselves that scripture is a guide, not a goal, they say, "The finger pointing at the moon is not the moon." I think we need a similar metaphor to explain what testing is really about to junior developers. When I say, "Don't check in code until all the tests pass," I do <em>not</em> mean:
<ul>
  <li>comment out test cases that are failing, then check in, or</li>
  <li>take failing assertions out of your methods, then check in, or</li>
  <li>throw away features whose tests are failing, then check in.</li>
</ul>
The purpose of testing is not to get all tests to pass. The purpose of testing is <em>to tell you what state your software is in</em>, and your goal should always be to gather as much useful information as you can (as economically as you can, but that's a topic for another post).  If you don't have any automated tests, then all you really know about the software comes from the interactive testing you've done since you last made a change. No other knowledge is reliable, not even the things you tried out 30 seconds before you made those changes.

If you do have automated tests, and some of them are failing, but you know why, that's OK (temporarily). Right now, for example, I know we're not creating a link object to connect A and B, because we decided we would do that implicitly rather than explicitly in this one special case, and I haven't implemented that code yet, so test #1234 is failing <em>as expected</em>, and that shouldn't stop me from checking in the code that makes test #5678 pass.  I shouldn't let very many failing tests pile up, but leaving them in the failing state to remind me (and the rest of the team) that some things aren't working yet is a lot better than taking them out just to get a green light.  The latter reduces how much I know about my program; the former may not be good for morale ("Jeez, we still have <em>that</em> to do, don't we?"), but it's more honest, and more useful.
