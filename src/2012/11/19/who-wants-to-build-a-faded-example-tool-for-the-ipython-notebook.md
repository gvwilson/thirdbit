---
title: Who Wants To Build a Faded Example Tool for the IPython Notebook?
date: 2012-11-19
original: swc
---
<p>While I'm asking people to write code for me, here's a small addition to the IPython Notebook that someone should be able to knock off in an hour. The starting points are <a href="http://en.wikipedia.org/wiki/Cognitive_load">cognitive load theory</a> and the idea of faded examples: long story short, one good way to teach is to show learners one example in detail, then ask them to fill in the ever-larger blanks in a series of similar partly-worked-out examples. Here's one that <a href="http://ethanwhite.org">Ethan White</a> did for our online study group:</p>
<pre>def get_word_lengths(words):
    word_lengths = []
    for item in words:
        word_lengths.append(len(item))
    return word_lengths</pre>
<p>This function creates and returns a list containing the lengths of a series of character strings. The list of character strings is passed in as the argument <code>words</code>, and the local variable <code>word_lengths</code> is initialized to an empty list. The loop iterates over each character string in the list. Each loop iteration determines the length of a single character string using the function <code>len()</code> and then appends that length to the list <code>word_lengths</code>. The final <code>word_lengths</code> list is returned by the function. An example of using it is:</p>
<pre>&gt;&gt;&gt; print word_lengths(['hello', 'world'])
<em>[2, 2]</em></pre>
<p>Given that, we would ask learners to fill in the blanks to make this verison work:</p>
<pre>def word_lengths(words):
    word_lengths = ____
    for item in range(len(____)):
        word_lengths.append(len(____))
    return word_lengths</pre>
<p>and work up to:</p>
<pre> def word_lengths(words):
    return [____ for ____ in ____]</pre>
<p>I'd like to be able to put exercises like this into the IPython Notebook. In particular, I'd like a two-by-two display:</p>
<table class="centered">
<tbody>
<tr>
<td align="center">code with blanks
(read-only)</td>
<td align="center">user's code
(editable)</td>
<td align="center">[reset]</td>
</tr>
<tr>
<td align="center">expected output
(read-only)</td>
<td align="center">actual output
(colorized)</td>
<td align="center">[run]</td>
</tr>
</tbody>
</table>
<p>The column on the left is read-only. Whenever the user clicks the "reset" button, the code with blanks is copied over to the right column. Whenever the user clicks "run", the code is re-run, and the actual output is compared to the expected output (and if it's textual, differences are colorized to draw the eye).</p>

<p>I <em>think</em> this is "just" a bit of Javascript–anyone want to take a crack at it and let me know?</p>
