---
date: 2012-02-13
original: swc
title: Formatting Revisited
---
<p><a href="http://dseifried.wordpress.com/">David Seifreid</a> has been working for the past week to combine <a href="http://imakewebthings.github.com/deck.js/">deck.js</a>, a Javascript-plus-CSS slideshow package, with the <a href="https://github.com/dz0ny/AudioJS">AudioJS</a> audio player, so that we can re-do slides as pure HTML5 (instead of using PNGs exported from PowerPoint). At the same time, I'm trying to turn the course notes into long-form prose (what used to be called a "book") for people who prefer reading at leisure. How should all this content be managed? My previous post on 21st Century teaching formats described what I'd eventually like, but the tool I want doesn't exist yet, so what can be done now?</p>
<p>We will have:</p>
<ol>
<li><em>metadata</em>, such as keywords and topic guides;</li>
<li><em>slides</em>containing
<ul>
<li>vector diagrams,</li>
<li>raster images,</li>
<li>point-form text, and</li>
<li>code samples</li>
</ul>
</li>
<li><em>audio narration</em> synced with the slides;</li>
<li><em>tranascripts</em> of the narration; and</li>
<li><em>prose</em> (the "book" stuff), which may include the same code samples and figures.</li>
</ol>
<p>I know from experience that the transcripts of the audio will be a starting point for the book-form material, but the latter will be longer. We'll therefore have four parallel streams of data: slides, audio, narration (as text), and the book. That suggests something like this (using the topic/concept distinction I discussed a couple of weeks ago):</p>
<pre>&lt;section class="topic"&gt;
  &lt;section class="metadata"&gt;
    keywords, notes to instructors, etc.
  &lt;/section&gt;

  &lt;audio src="…" /&gt;

  &lt;section class="concept"&gt;

    &lt;section class="slide" popcorn-slideshow="start time in seconds"&gt;
      Slide (or several slides if we're using progressive highlighting on a single logical slide).
    &lt;/section&gt;

    &lt;section class="transcript"&gt;
      Text transcript of the slide (or group of closely-related slides).
    &lt;/section&gt;

    &lt;section class="book"&gt;
      Long-form prose discussion of the same concept.
    &lt;/section&gt;

  &lt;/section&gt;

  &lt;section class="concept"&gt;
    …as above…
  &lt;/section&gt;
&lt;/section&gt;</pre>
<p>Diagrams and images will be stored in external files and <code>href</code>'d in–I've played with putting the SVG directly in the document, but in practice, people are going to use different tools to edit the two anyway. I'd like to use inclusions for code fragments, so that they don't have to be duplicated in the slide and book sections, but there's no standard way to do text inclusion in HTML (which is odd when you think about it, given that other media are usually included by reference instead of by value).</p>
<p>The advantages of this format that I see are:</p>
<ol>
<li>Anyone can edit it without special tools.</li>
<li>It's mergeable: provided people stick to a few rules about indentation and the like, it'll be a simple text merge (which is a <em>lot</em> easier than merging PowerPoint slides or the like).</li>
<li>We can re-skin it using CSS and a bit of Javascript. (For example, the default web view won't show the transcript or book form, just the slides and audio.)</li>
<li>It's accessible to people with visual handicaps (since related content is side-by-side and complete).</li>
<li>We can compile it to produce web-only or print-only versions using XSLT or the like if we want to.</li>
</ol>
<p>Things I don't like:</p>
<ol>
<li>I really would like to store code snippets in external files and <code>href</code> them as if they were diagrams or images. We can do that with a simple script, but then what you're editing and what you're looking at in your previewer (browser) will be separated by a compilation step, which in my experience always results in headaches.</li>
<li>Different authors' HTML editing tools will indent things differently, so we'll need to provide some sort of normalizer for them to run before doing an update or commit. It's not a big deal, but again, experience teaches that it will lead to a constant background annoyance level ("Whoops, sorry, I forgot to clean up before I committed that change").</li>
</ol>
<p>We <em>could</em> use a wiki-like syntax for notes, and rely on something like <a href="http://sphinx.pocoo.org/">Sphinx</a> to convert that to what we need. This is the route the authors of <a href="http://scipy-lectures.github.com/">these SciPy lectures</a> have taken, and while it's intriguing, I don't see how to support the parallel streams we want without some serious hackage. It would also tie any processing tools we build to an idiosyncratic format (reStructuredText); HTML5 might be more typing, but it can also be crunched by almost any language people are likely to use straight out of the box.</p>
<p>Thoughts?</p>
