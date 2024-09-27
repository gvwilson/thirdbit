---
title: "Converting PowerPoint to SVG: Help Needed"
date: 2012-02-22
---
Software Carpentry has 110 PowerPoint files, each containing between 20 and 120 slides–call it 5000 slides in total. I'd like to convert them to HTML5 for use with <a href="https://github.com/dseif/slide-drive">Slide Drive</a>, the <a href="http://imakewebthings.github.com/deck.js/">deck.js</a>+audio slideshow tool that <a href="http://dseifried.wordpress.com/">David Seifried</a> is building. Here's the breakdown:
<ul>
  <li>A few bugs in the slide decks need to be fixed–it's a fairly small job.</li>
  <li>I already have audio recordings narrating the slides. A few will need to be redone to sync with bug fixes in the slides, but that's a fairly small job.</li>
  <li>I also have transcripts of those recordings. They'll need corresponding edits, and reformatting, but again, that's fairly small.</li>
  <li>I <em>don't</em> have time-marks synchronizing the audio with the slides. I'm sure that information is embedded in the Camtasia project files I created when making the current videos, but I don't know how to get it out (yet).</li>
  <li>Exporting the main text in the slides (the bullet points) is straightforward, though a fair bit of manual touch-up will be needed to reformat it.</li>
  <li>Ditto for the code samples (which don't show up with the main text, since they're in separate text objects).</li>
</ul>
And then there are the diagrams… Roughly a third of the slides have diagrams of some kind, which makes about 1500 in all. That's too many to redraw, and anyway, I shouldn't have to: they're stored in PowerPoint in some kind of vector format, so I should be able to "export as SVG" or the moral equivalent thereof.

But "should" and "can" aren't the same thing. I can save my PowerPoint in a lot of different raster image formats, but not in a vector format like SVG. However, I <em>can</em> select elements of a diagram, copy them, and then paste them into a vector drawing tool like <a href="http://inkscape.org/">Inkscape</a>, which indicates that something in Windows understands how to do the required format conversion.

Doing that 1500 times would be very tedious, though. What I really want is a way to automate that process, i.e., save each slide in a deck as a separate SVG that I can later open and edit. Googling turns up a couple of possibilities, but:
<ul>
  <li>The <a href="http://www.verydoc.com/doc-to-any/powerpoint-to-svg.html">VeryDOC Powerpoint-to-SVG convert</a> completely drops the embedded text (i.e., the captions).</li>
  <li>Ditto <a href="http://www.openoffice.org/product/impress.html">OpenOffice.org Impress</a>–slides must be saved one at a time, and only the graphical elements come out (not the captions).</li>
  <li><a href="http://www.davisor.com/transformations/ppt-to-svg-java.html">Davisor Publishor</a> doesn't even export all the graphics.</li>
  <li><a href="http://www.docx4java.org/trac/docx4j">docx4j</a>'s pptx4j sounds like it ought to do the job, but (a) it's a library, not a tool, so some Java would have to be written to create an actual converter, and (b) it's not clear that it <em>does</em> actually do the job.</li>
</ul>
Please tell me I missed something…

<em>Later: in response to a suggestion, I downloaded a Windows clipboard viewer and copied a diagram out of PowerPoint. The display looked like this (click the image for full-sized):</em>

<img alt="Capture" src="@root/files/2012/02/Capture-300x156.png" width="300" height="156" class="centered">

<em>It appears to be a reference into the source file, rather than an actual representation of my boxes, arrows, and text.</em>
