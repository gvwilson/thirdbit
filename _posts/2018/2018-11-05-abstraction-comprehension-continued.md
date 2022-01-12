---
date: 2018-11-05 03:35
year: 2018
title: "Abstraction and Comprehension Continued"
---

In response to [my previous post]({{site.github.url}}/2018/11/03/abstraction-comprehension.html),
[Mark Guzdial](https://www.si.umich.edu/people/mark-guzdial)
[tweeted this](https://twitter.com/guzdial/status/1059260901105303552):

> There's an assumption in the third solution: that Solution E is within the
> novice's Zone of Proximal Development.  If not, then it won't be helpful to
> explain Solution E in terms of primitives of Solution N.

The [Zone of Proximal Development](https://en.wikipedia.org/wiki/Zone_of_proximal_development)
(ZPD) is the region between what the learner can do without help and what they can't do at all,
or equivalently,
a region in which someone will learn if they're guided by someone more knowledgeable than themselves.
What Mark is pointing out is that some experts' solutions cannot be comprehensibly expressed
in terms of the operations that novices understand.
This means that the "third lesson" explaining Solution E to a novice
might in practice have to start by turning the novice into an expert
(which is rather like saying that it's easy to get to the top of Mount Everest:
just climb the first few thousand meters,
then do the last hundred).

The key here is "*comprehensibly* expressed".
For me,
the `map`-based fragment of code I presented:

```
hosts <- links.map(a => a.href.split(':')[1].split('/')[0]).unique()
```

contains seven operations:
`map`, get `href`, split on colon, take the second element,
split on slash, take the first element, and uniquify.
On the other hand,
the loop-based solution:

```
hosts <- []
for (each a in links) do
  temp <- attr(a, 'href').split(':')[1].split('/')[0]
  if (not (temp in hosts)) do
    hosts.append(temp)
  end
end
```

has at least twelve operations,
and maybe as many as fourteen or fifteen,
depending on what's in the reader's [notional machine]({{site.github.url}}/2018/04/12/notional-machine-for-python.html).
My mind automatically compresses those lower-level operations because they conform to patterns I've seen before:
to me,
for example,
"if not in, then append" instantly translates to "keep unique values".
Since by definition novices don't have those patterns,
expanding the high-level solution automatically won't help them:
they'll understand the individual steps,
but the cognitive load of assembling those steps will defeat them.

What I've realized while writing this is that there's a connection between
[Caulfield's Chorus of Explanations](https://hapgood.us/2016/05/13/choral-explanations/)
and one of my favorite teaching techniques:
[proofs and refutations](https://www.amazon.com/Proofs-Refutations-Mathematical-Discovery-Philosophy/dp/1107534054).
I often teach by presenting a simple solution to a simple problem,
then adding a bit of complexity to the problem and showing why the simple solution no longer serves
in order to motivate a solution that's more powerful but more complex.
(I once spend an entire hour showing a class
how to count things in files.)
Caulfield's Chorus serves groups of mixed ability in which some learners know enough to skip directly to the more complex solution;
the terse, highly abstract solutions in the chorus work for readers who are fluent with patterns,
but who have also seen the refutations of the simpler solutions
that motivate the complexity or compression of the more abstract.

If this is correct,
then automatically mapping explanations from one level to another is a dead end
because the people who need the less abstract explanation won't be able to digest
the inch-by-inch version of the more abstract solution.
What *might* work is designing lessons not as a sequence of ideas introduced,
but as a sequence of refutations overcome.
This,
I think,
lies in my own ZPD,
so I'd be grateful for pointers to examples.

Footnote: over half of the contributors to *[AOSA](http://aosabook.org)*
explained the architecture of their software by recapitulating its history.
Over and over again they said,
"The only way to understand why it looks the way it does is to understand how we got here."
To the best of my knowledge,
no programming language has an "or else" clause
that lets programmers say, in code,
"Do it this way *or else* this bad thing will happen."
Unit tests don't quite serve that purpose,
since they don't record the code that fails;
if anyone knows of a system that does,
I'd be grateful for pointers to that as well.
