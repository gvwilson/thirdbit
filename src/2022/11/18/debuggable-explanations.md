---
title: "Debuggable Explanations"
date: 2022-11-18
---

Jon Udell has written [a short post](https://blog.jonudell.net/2022/11/17/debuggable-explanations/)
about his experience working through [the Python version](@root/sdxpy/)
of [Software Design by Example](@root/sdxjs/).
He doesn't jus want to *read* prose and code:
he wants to be able to *run* the code in a debugger
so he can step through and build a mental model of how it works.
Downloading the samples
figuring out how to run them on their own without command-line arguments,
and arranging things for side-by-side viewing is doable,
but as he says,
"…the activation threshold is high enough
to thwart my best intention of repeating the steps for every chapter."

Tools like the Jupyter Notebook aren't much help here:
for example,
they don't provide a way
to have a cell containing just one method of a larger class
or just a few lines from a longer function
(which I frequently want to do for pedagogical reasons).
I did think about bundling a VSCode `launch.json` file with each chapter,
but that wouldn't do anything to put the code side-by-side with the explanation.

What's funny/not-funny is that these aren't niche needs.
While JavaDoc-style comments or Python's specially-formatted docstrings
are OK (but not great) for API documentation,
they're a clumsy way to write long-form tutorials.
I've been stumbling over this problem for over thirty years,
and today's solutions are only marginally better than what was available in 1989.
If you have one—one that will make authoring easier
while simultaneously allowing people like Jon to experience the lesson
in the IDE of their choice—please let me know.
