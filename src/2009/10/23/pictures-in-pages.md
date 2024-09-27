---
title: "Pictures in Pages"
date: 2009-10-23
---
It's still a lot harder than it should be to add pictures to web pages. I know, you think it's easy, but let's do a comparison:
<table class="centered">
<tbody>
<tr>
<td>Modern desktop WYSIWYG editor</td>
<td>WordPress (and most other tools)</td>
</tr>
<tr>
<td>
<ol>
  <li>click on the drawing palette</li>
  <li>draw</li>
</ol>
</td>
<td>
<ol>
  <li>fire up a separate drawing application</li>
  <li>create the image</li>
  <li>upload it</li>
  <li>add an &lt;img&gt; tag to link to it</li>
</ol>
</td>
</tr>
</tbody></table>
Not too bad so far, but what happens when someone wants to update the image?
<table class="centered">
<tbody>
<tr>
<td>Modern desktop WYSIWYG editor</td>
<td>WordPress (and most other tools)</td>
</tr>
<tr>
<td>
<ol>
  <li>click on the picture</li>
  <li>draw</li>
</ol>
</td>
<td>
<ol>
  <li>download the image</li>
  <li>fire up a separate drawing application</li>
  <li>update the image</li>
  <li>upload it again</li>
</ol>
</td>
</tr>
</tbody></table>
The former feels more wiki-like, and I suspect that if sketching in web pages was as easy as sketching in Word or OpenOffice, a lot more developers would draw pictures of what's going on in their applications.

I can see two ways forward: create drawing tools that rely on the &lt;canvas&gt; element that are as easy to incorporate into web pages as the Javascript WYSIWYG HTML editor I'm using right now in WordPress, or hack around the problem. Right now, it looks like the latter is winning.  For example, check out Jordi Cabot's list of <a href="http://modeling-languages.com/content/uml-tools#textual">text-based UML tools</a>: all of the entries translate text like
<pre>@startuml
Alice -&gt; Bob: Authentication Request
Bob --&gt; Alice: Authentication Response
@enduml</pre>
into a picture like:

<img src="@root/files/2009/10/diagram.png" alt="diagram" width="210" height="153" class="centered">

just as a wiki engine takes <code>//ohmigod!//</code> and turns it into <em>ohmigod!</em>. (Example taken from <a href="http://plantuml.sourceforge.net/">PlantUML</a>.)

Now, part of me wants to weep at the prospect of ASCII art's continued survival. On the other hand, it's a pretty creative way to work around the continuing backwardness of web interfaces, and if people actually start using it to explain what their code is doing and how it works, we'll all be better off.
