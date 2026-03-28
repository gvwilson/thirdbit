---
title: "An E-Bike for the Mind"
date: 2026-03-28
---

As I wrote [a couple of days ago][feasible],
Sajaniemi et al's work on [roles of variables][roles]
identified and named ten patterns in the way variables are used in novice programs.
These roles aren't just a way to analyze code.
They're also useful for explaining code,
because they provide a vocabulary to capture *intent*
in a way that's complementary to type information like `int` or `Person`.

| Role | Description |
|---|---|
| Fixed value | Initialized once and not changed thereafter. |
| Stepper | Steps through a systematic, predictable succession of values (e.g., a loop counter). |
| Walker | Traverses a data structure element by element, where each new value depends on the previous position. |
| Follower | Always receives the previous value of some other variable (e.g., `prev = current` before `current` is updated). |
| Most-recent holder | Holds the latest value encountered in an unpredictable series, typically successive inputs. |
| Most-wanted holder | Holds the best value found so far (e.g., maximum or minimum). |
| Gatherer | Accumulates the combined effect of individual values (e.g., running sum or count). |
| One-way flag | A two-valued variable that, once changed from its initial value, never reverts (e.g., an error flag set to `True` and never reset). |
| Temporary | Holds a value for a very short time only, most commonly in a swap operation. |
| Organizer | A collection used only to rearrange its elements (e.g., sorted in place), never to add or remove them. |
| Container | A collection whose elements are added and/or removed during the computation. |

It occurred to me during a workshop this week that
variable roles might help when we are using LLMs in teaching.
In order to understand a piece of software,
I need to understand the purpose of each of its parts.
Pattern names like Observer or Singleton help me do this
because they compress complex chunks of code down to single concepts,
which helps prevent cognitive overload.
However,
the classic design patterns are still too big for novices;
would Sajaniemi's roles be more helpful?
I.e.,
can we prompt the LLM to explain things in terms of these roles
while simultaneously teaching newcomers to think in terms of them,
and if so,
does it help?
And if the answers are "yes",
are there other roles that Sajaniemi and his colleagues didn't identify
that are worth adding to the table above?
(I work with data scientists
so the first that comes to mind is "Dataframe",
but that's not a role: that's a data type.)

> One way to think about roles is that types tell you about the variable's state at rest
> while roles tell you about the variable's state in motion.
> This duality is similar to the one Kerievsky described
> in his under-appreciated book [*Refactoring to Patterns*][refactoring],
> which explored the duality between design patterns (code at rest)
> and refactorings (code in motion).

In order to explore these ideas,
I spent about three and a half hours prompting Claude to build [jorma][jorma],
a small Python package that uses static and dynamic analysis
to identify variables' roles.
At the time of writing it is about 1000 lines of Python (not including tests)
and is able to process 145 source files taken from [*Software Design by Example*][sdxpy].
I made a few small edits to the code manually,
but almost all of what's in `src` and `tests` was written by Claude.
I think it would have taken me four or five days of full-time work and frustration
to get this far on my own,
which means that I probably wouldn't have done it.

That realization is what led to this post's title:
if a computer is a bicycle for the mind,
then LLMs are like e-bikes.
They let a lot of people go distances and tackle hills that they couldn't before,
and they're better for all of us than cars,
but they're a menace to both pedestrians and traditional cyclists,
more harmful to the environment than what they're replacing,
and have given companies yet another way to hollow out local businesses.
(Neighborhood restaurants know that cheap delivery services are killing them slowly,
but if they don't play,
they'll just die more quickly.)

I wish I could write a tidy conclusion for this post,
but I don't have one.
Experiments like [jorma][jorma] have convinced me that
telling people not to use LLMs
is going to be just as ineffective as telling teenagers not to have sex or use social media.
I hope that this week's court decisions to hold Meta accountable for the harm it has caused
is a first step toward dealing with [cognitive pollution][pollution] in general,
for the same reason that I hope Toronto and other places will figure out
how to make e-bikes a normal part of everyday life.
Until then,
if you'd like to help me improve [jorma][jorma],
please try it out or [get in touch][email].

[email]: mailto:gvwilson@third-bit.com
[feasible]: @root/2026/03/26/feasible/
[jorma]: https://github.com/gvwilson/jorma
[pollution]: @root/2026/03/08/cognitive-pollution/
[refactoring]: https://isbnsearch.org/isbn/9780321630018
[roles]: https://www.ppig.org/files/2005-PPIG-17th-sajaniemi.pdf
[sdxpy]: @root/sdxpy/
