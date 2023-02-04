---
title: "Spelling, Fairness, and JavaScript"
date: 2011-08-18 10:18:46
year: 2011
---
My daughter has been sounding out words for a while now, and in the last couple of weeks has gone from c-a-t to "B-os-ton" (as in "Boston Pizza").  A couple of days ago, she was struggling with a new word: eff, are, eye, ee, en, dee—we've taught her that when two vowels are together, the first one says its name, so she pronounced it to rhyme with "blind".  "Close," I told her. "It's 'friend'—in this word, the <em>second</em> vowel says its name." She wrinkled her nose and said, "That's not fair."

She's right: the "rules" of English spelling aren't fair. Neither, unfortunately, are the rules of many programming languages. For example, suppose I tell you that:
<pre>4 * "5" =&gt; 20</pre>
i.e., that using '*' on the integer 4 with the string containing digit '5' is the integer 20, because the string is automatically converted to a number. What would you guess the result of:
<pre>4 + "5"</pre>
to be? I asked four people in my office yesterday; three said "the number 9", and one said, "It's not allowed" (clearly recognizing that it must be a trick question). No-one said, "The string '45'," but that's the answer in JavaScript.  Just for comparison, here are the answers in two other languages:
<table class="centered">
<tbody>
<tr>
<td></td>
<td> Perl</td>
<td> Python</td>
</tr>
<tr>
<td>4 * "5"</td>
<td> 20</td>
<td> "5555"</td>
</tr>
<tr>
<td>4 + "5"</td>
<td> 9</td>
<td> illegal</td>
</tr>
</tbody>
</table>
Surprisingly, given its reputation, Perl is the most consistent. Python is just as bad as JavaScript: while I occasionally still do construct a row of dashes by multiplying "-" by 80, it's a rare enough case that I think the language would have done well to say, "You can't combine strings and numbers without explicitly converting one to the other."  That would have made both operations illegal, which would have been easier to remember.

That's really what we mean by "fair" or "unfair" in this context: how easy is it to remember the rule(s) and predict what's going to happen in new situations. Several tons of cognitive science research have shown that people are pattern matchers, not memorizers; our brains perform much better when applying a small number of general (i.e., consistent) rules than when trying to figure out which of a larger set of rules to use. Putting it another way, the shallower the decision tree, the faster and more correctly we solve problems.

This is why we switched from Perl to Python in the early days of the <a href="https://software-carpentry.org">Software Carpentry</a> course. Back in 1998-99, Python was still very much a niche language: going by Amazon.com book rankings, we figured it had about a tenth of the user base of Perl. But every single page of the O'Reilly pocket guide to Perl contained one or more of the words "except", "unless", or "however", which meant that when we taught it, we kept having to say, "It's usually like this, but sometimes like that." Python was more regular, so material that had taken three days to cover in Perl only took two days in Python, and retention was higher (both immediately afterward and six months later).

And this is why I will continue to dislike JavaScript. Its inconsistencies impose extra <em>and unnecessary</em> cognitive burdens on users. Yes, I will eventually internalize its rules, just as I've learned to pronounce "friend" properly. But if the research is right, even then those inconsistencies will slow me down and increase my error rates–perhaps only a little, once I immerse myself in it, but the effect will persist. Building the future is hard enough; I think it's fair to grumble a bit about tools that make it even harder.
