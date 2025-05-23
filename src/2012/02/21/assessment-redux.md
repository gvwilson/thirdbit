---
date: 2012-02-21
original: swc
title: Assessment Redux
---
<p>The single biggest challenge Software Carpentry faces right now is how to tell what impact it's having. This is only partly to satisfy funders–as I said back in December, if we don't know how to tell if we succeeded, we're going to fail. It would be (relatively) easy to put together a multiple-choice quiz to see how much people have learned about basic shell commands, the syntax of Python, and so on, but that would only address the shallowest aspects of learning. We're trying to impart some fundamental principles, and what we need is questions that will tell us whether people have internalized them. (As many studies have shown, it's possible to get a decent score on a quiz without actually understanding the subject matter.)</p>
<p>For example, consider this question about Subversion:</p>
<blockquote><p>Emmy wants to see what has changed in her working copy since revision 120. The command she should run is:</p>
<ol>
<li><code>svn log -r 120</code></li>
<li><code>svn diff -r 120</code></li>
<li><code>svn revert -r 120</code></li>
<li><code>None of the above</code></li>
</ol>
</blockquote>
<p>It addresses Q05 ("How can I keep track of what I've done?") fairly directly, but not R02 ("Use a version control system"), R03 ("Automate repetitive tasks"), or <em>any</em> of the basic principles. Open-ended answers might do the latter, but it's hard to come up with ones that don't lead the witness: asking, "When would you use a version control system?" isn't going to give us much insight into what people actually think. We could combine a few multiple-choice with a few open-ended, but realistically, if it takes more than 10-15 minutes for people to answer, many (most?) won't. If anyone can see a way to square this circle, I'd welcome ideas.</p>
