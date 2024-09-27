---
title: "Java Ecosystems for Python Programmers"
date: 2007-06-06
---
(Posted on behalf of Miles Thibault, a former CSC49X student now working in London, England.)

I have a problem: I'm a Python programmer.  That's not the problem. My problem is that I'm starting a Java project and I don't really know what experienced Java developers do when they build software.

I know I want things like version control, an IDE, unit tests and logging; but I don't know which specific tools and libraries I should be using, nor how to best utilize them.

There are myriad books on the Java programming language proper, but I'm having a tough time finding anything that says: "If you're going to build Java software, here are some popular/pragmatic tools that most people use because they like building quality code and they don't like wasting their own time."

I've spoken to a few Java hackers and here's what I've come up with so far (thanks Bill, Sean, and Greg).  I'd be interested in hearing what else <em>you</em> use.
<table class="centered">
<tr>
<td>Version control</td>
<td>Subversion (included for completeness—I already use version control)</td>
</tr>
<tr>
<td>IDE</td>
<td>Eclipse (tough one for a Textmate fanboy)</td>
</tr>
<tr>
<td>Debugger</td>
<td>built into Eclipse.</td>
</tr>
<tr>
<td>Build</td>
<td>Ant</td>
</tr>
<tr>
<td>Deploy</td>
<td>Ant</td>
</tr>
<tr>
<td>Unit tests</td>
<td>Testng</td>
</tr>
<tr>
<td>Logging</td>
<td>Log4j</td>
</tr>
<tr>
<td>Docs</td>
<td>Javadoc</td>
</tr>
<tr>
<td>Lint</td>
<td>Findbugs</td>
</tr>
<tr>
<td>Coverage</td>
<td>Clover</td>
</tr>
<tr>
<td>Style</td>
<td>Checkstyle</td>
</tr>
<tr>
<td>Continuos integration</td>
<td>Cruisecontrol</td>
</tr>
<tr>
<td>Monitoring</td>
<td>Nagios (included for completeness)</td>
</tr>
<tr>
<td>Postmortem debugging</td>
<td>does Java do core files?</td>
</tr>
<tr>
<td>Performance testing</td>
<td>Jmeter</td>
</tr>
<tr>
<td>Profiling</td>
<td>PerformaSure?</td>
</tr>
</table>
