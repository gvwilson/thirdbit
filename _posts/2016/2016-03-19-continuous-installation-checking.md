---
title: "Continuous Installation Checking"
date: 2016-03-19 05:00
year: 2016
---
<p>
  This one started with me
  <a href="http://stackoverflow.com/questions/36088231/unable-to-install-bioperl-on-mac-os-x">trying and failing to install some bioinformatics software on my Mac</a>,
  then turned into <a href="https://twitter.com/gvwilson/status/710950558207774722">a Twitter rant</a>:
</p>
<ul>
  <li>Everyone: please start doing installation-driven development. Not test-driven, not feature-driven: installation-driven.</li>
  <li>Best possible use of AI: a program that simulates a naive user trying to install your software. "Reads" docs, follows steps...</li>
  <li>...gets lost, makes mistakes... we could feed traces from actual install attempts into a Markov chain generator, then couple it to...</li>
  <li>...Travis-CI or something like that so that "user can install" becomes part of the pre-commit check and the world's a better place</li>
</ul>
<p>
  But I'm serious.
  (I'm <em>always</em> serious.)
  Given how formulaic installation instructions tend to be,
  could a graduate student or startup build:
</p>
<ol>
  <li>an <a href="https://en.wikipedia.org/wiki/Natural_language_processing">NLP</a> tool to extract actions from installation and configuration instructions,</li>
  <li>a monitor to gather traces of the steps taken by actual users (<em>not</em> professional sys admins or package authors) as they try to install the software, and</li>
  <li>some sort of Markov chain generator to follow the steps found in #1 while making mistakes similar to those detected by #2?</li>
</ol>
<p>
  I don't think this would be easy:
  the first two parts are each worthy of a thesis (though I suspect the third will be relatively straightforward by comparison).
  But imagine how useful this would be.
  Imagine what it would be like if Travis-CI or other continuous integration tools could fire up a lightweight VM
  and go through your installation instructions
  <em>every time you committed a change</em>
  and say,
  "Nope, sorry, it looks like you've missed a step,
  and that bit there,
  the one we've been telling you about for the last three months?
  Most people are still going to find it confusing,
  so how about you try explaining it differently?"
</p>
