---
title: "Our Experiences Switching to Python"
date: 2009-08-25 08:49:11
year: 2009
---
In response to a question about what it's been like switching to Python as a first-year programming language, <a href="http://www.cs.utoronto.ca/~pgries">Paul Gries</a> wrote the following.  It might be of interest to other instructors who are thinking of changing over.

And in related news, we're compiling errata and solutions to even-numbered exercises for a fresh printing of <em><a href="http://pragprog.com/titles/gwpy/practical-programming">Practical Programming</a></em>. We're pleased with how well it's doing; in particular, we've been pleasantly surprised by the number of inquiries we've had from people who are home schooling. If you have questions, suggestions, or experiences to share, we'd love to hear from you.

<hr />The switch to Python was quite smooth, except for the following items:
<ul>
  <li>We decided to write a textbook because we didn't think we could live with the options at the time.</li>
  <li>We decided to use Mark Guzdial's excellent multimedia approach, but ended up almost completely rewriting his media module to use standard Python instead of Jython and had many issues with his development environment.  Mark had a proof of concept that we worked from, but it used Java naming conventions and since it was designed and written by undergrads it needed a lot of cleaning up.  You can find installation instructions for all of the packages that we use at <a href="http://www.cdf.utoronto.ca/~pgries/pybook/"></a>. A team of about 4 people worked roughly 1 day a week throughout the summer in 2007 to put together the lectures, assignments, labs, and tests, and we've been refining that since then.</li>
</ul>
We love most of Python, especially the clean, readable, minimal syntax.  However, there are several Python gotchas, and we were bitten by almost all of them.  Here are some of the major ones that confused either students or instructors:
<ul>
  <li>There are no good GUI packages; Swing was at least teachable, but Tkinter has lots of warts and none of the others (e.g., wxPython, PyQt) seem to be usable on all three major OSes.  We've dropped Tkinter this fall in favour of EasyGUI, which has major limitations but is much more teachable.</li>
  <li>It's hard to know when to stop.  List comprehensions, for example, are really cool and natural, but they make a surprising number of problems too easy and allow students to avoid writing loops.  We show them toward the end of our intro course but don't require the students to use them.</li>
  <li>Aliasing is surprising and comes up naturally and even accidentally, especially in lists.  This is not necessarily Python-specific, but it sure comes up more in Python than it did in Java.</li>
  <li>Default values for parameters are created once.  Students (and some instructors) hate this.</li>
  <li>Simple classes are harder to teach than in Java.  Also, "self" confuses a large subset of the students.  Since dictionaries are so accessible they do whatever they can to avoid using and understanding classes.</li>
  <li>Global scope is hard to explain: it's actually module scope and not global, and in the three examples below there are different behaviours; the last example in particular really confuses students. They do all of these things naturally, so we can't prevent them getting confused.
<table class="center">
<tbody>
<tr>
<td valign="top">
<pre># Example 1
i = 1
def f():
    print i

f()
print i</pre>
</td>
<td valign="top">
<pre># Example 2
i = 1
def g():
    i = 2
    print i

g()
print i</pre>
</td>
<td valign="top">
<pre># Example 3
i = 1
def h():
    print i
    i = 2
    print i

h()
print i</pre>
</td>
</tr>
</tbody></table>
</li>
  <li>More scope: nested functions baffle students.

On the positive side, some students LOVE putting functions into dictionaries and getting rid of huge if/else statements.  They also find passing functions as parameters to be natural; we introduce this idea to write a timing function that returns how long its argument runs.  This is a lovely thing to do when we get to searching and sorting.

In CS2, we're struggling with how much information hiding to do; we're conflicted about whether __var plus set_ and get_ helpers is what we should do or if we should get into properties.  We're leaning toward the former, but we're not certain.</li>
</ul>
