---
title: "How Do You Want to See Source Code?"
date: 2005-12-02 09:54:14
year: 2005
---
I ran a post-mortem for this term's run of the <a href="https://carpentries.org/">Software Carpentry</a> course on Monday.  Students gave me a lot of useful feedback, which I'll post as soon as I find my notes ;-).  One comment that's got me thinking was about the way sample programs are presented in the notes.  Right now, I include the finished code in a monochrome fixed-width font.  Adding syntax highlighting won't be difficult; the more interesting suggestion was to write the code "live", while talking aloud.  The main benefit would be that it would prevent the instructor from racing by something that students need time to absorb.  It would also force (or at least encourage) the instructor to think aloud about what the code was doing, how it was structured, etc.

The problem is that I want the notes to be usable on their own, without an instructor, both on-line and when printed.  That suggests some Powerpoint-style animation trickery to reveal successively larger versions of the code sample one after the other, accompanied by comments.  I'm envisioning something like this:
<table class="centered">
<tr>
<td colspan="3">
<table class="centered">
<tr>
<td><code> </code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
</table>
</td>
</tr>
<tr>
<td colspan="3"><em>Invert a dictionary without losing any data.</em></td>
</tr>
<tr>
<td align="center">1</td>
<td align="center">2</td>
<td align="center">3</td>
</tr>
</table>
becoming this:
<table class="centered">
<tr>
<td colspan="3">
<table class="centered">
<tr>
<td><code><font color="blue">def</font> invert(d):</code></td>
</tr>
<tr>
<td><code>  result = {}</code></td>
</tr>
<tr>
<td><code>  <em>…invert d into result…</em></code></td>
</tr>
<tr>
<td><code>  <font color="blue">return</font> result</code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
</table>
</td>
</tr>
<tr>
<td colspan="3"><em>Step 1: signature and skeleton.</em></td>
</tr>
<tr>
<td align="center"><strong><em>1</em></strong></td>
<td align="center">2</td>
<td align="center">3</td>
</tr>
</table>
then this:
<table class="centered">
<tr>
<td colspan="3">
<table class="centered">
<tr>
<td><code><font color="blue">def</font> invert(d):</code></td>
</tr>
<tr>
<td><code>  result = {}</code></td>
</tr>
<tr>
<td><code>  <font color="blue">for</font> (k, v) <font color="blue">in</font> d.items():</code></td>
</tr>
<tr>
<td><code>    result[v] = result.get(v, []).append(k)</code></td>
</tr>
<tr>
<td><code>  <font color="blue">return</font> result</code></td>
</tr>
<tr>
<td><code> </code></td>
</tr>
</table>
</td>
</tr>
<tr>
<td colspan="3"><em>Step 2: use a list for values, so that collisions aren't fatal.</em></td>
</tr>
<tr>
<td align="center">1</td>
<td align="center"><strong><em>2</em></strong></td>
<td align="center">3</td>
</tr>
</table>
and then this:
<table class="centered">
<tr>
<td colspan="3">
<table class="centered">
<tr>
<td><code><font color="blue">def</font> invert(d):</code></td>
</tr>
<tr>
<td><code>  <font color="green">'''Invert a dictionary, keeping colliders.'''</font></code></td>
</tr>
<tr>
<td><code>  result = {}</code></td>
</tr>
<tr>
<td><code>  <font color="blue">for</font> (k, v) <font color="blue">in</font> d.items():</code></td>
</tr>
<tr>
<td><code>    result[v] = result.get(v, []).append(k)</code></td>
</tr>
<tr>
<td><code>  <font color="blue">return</font> result</code></td>
</tr>
</table>
</td>
</tr>
<tr>
<td colspan="3"><em>Step 3: remember, always document your code.</em></td>
</tr>
<tr>
<td align="center">1</td>
<td align="center">2</td>
<td align="center"><strong><em>3</em></strong></td>
</tr>
</table>
My questions are:
<ol>
  <li>Is there a better way to do this?</li>
  <li>If not, is there a tool out there (presumably written in JavaScript) that'll do this?</li>
  <li>If so, what happens in the print version?  I'd rather not display the same lines of code several times—some kind of callout or highlighting would be best—but I want to be able to do everything from a single source representation.</li>
</ol>
Answers <a href="mailto:{{site.author.email}}">to me</a>, please; best response wins an all-expenses-paid trip to the nearest Tim Horton's.
