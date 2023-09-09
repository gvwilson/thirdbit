---
title: "An Approach to Motivating Coding"
date: 2023-09-09
year: 2023
---

One of the many challenges when teaching programming to adults is
to find motivating examples.
There's not a lot people do in real life
that you can do in five or ten lines of Python,
and the things you *can* do (like Scratch-style graphics)
aren't things most people with jobs and families have time to care about.

Data analysis is an exception.
I'm increasingly convinced that analytics-first
is the best way to convince most adults that lessons will pay off,
but R and Python both have unfortunate quirks.
[Tidyblocks][tidyblocks] was an attempt to build something Scratch-like
as a bridge between spreadsheets and textual coding,
but foundered on the inability of click-together blocks to express joins
(and on the fact that nobody would fund further work).
I'm now wondering whether some combination of click-together blocks
and block-and-connector dataflow would work better,
and whether we could use the question, "How does a spreadsheet work?"
as a running example.
A possible teaching sequence would be:

<ul>
  <li>
    A single input cell and a single output cell
    with a block in the middle that does <code>out := 2 * in</code>.
  </li>
  <li>
    Three such cell pairs, each with the same formula.
    clearly we don't want to have to do this N times.
  </li>
  <li>
    Two columns of three cells each to teach <code>in[i]</code> and <code>out[i]</code>,
    with subscripting represented as two-blocks (name and index expression).
  </li>
  <li>
    The same input and output columns but a loop block: <code>for i in 1..length(in)</code>.
  </li>
</ul>

<img src="{{'/files/2023/block-column-transform.svg' | relative_url}}" alt="example">

<ul>
  <li>
    Attach a simple inspector showing (i, val) as an (x, y) bar plot to visualize while single-stepping.
  </li>
  <li>
    Introduce a conditional block: <code>for... if in[i] >= 0</code>,
    then point out that holes (NA) appear in the output.
    (The watch plot shows special markers for missing values.)
  </li>
  <li>
    Introduce solution #1: the <code>else</code> clause
    (and watch what it does by single-stepping).
  </li>
  <li>
    Introduce solution #2: <code>for... if... append(out, value)</code> and show the output column growing.
    The final output column is a different length than the input.
  </li>
  <li>
    Next, add two columns of the same length.
  </li>
  <li>
    And then ask what happens if the input columns have different lengths? Options are:
    <ul>
      <li>Fail with an out-of-bounds error.</li>
      <li>Use the shorter length.</li>
      <li>Append NAs to the output.</li>
    </ul>
  </li>
  <li>
    We can now do things like sum the values in a column.
    <ul>
      <li>Create a scalar variable (visually like a column, but indexing not required).</li>
      <li>Add values in column into that scalar.</li>
      <li>Attach a watch plot that visualizes changes to the scalar's value.</li>
    </ul>
  </li>
</ul>

I know this isn't how spreadsheets actually work (mumble mumble observer/observable, mumble mumble),
but what I *don't* know is if anyone has ever used calculations on columns
to motivate basic programming for adult learners?
I think it would be easy to extend this:
for example,
the next step could be "how to create a function that operates on an arbitrary column",
which opens up all sorts of interesting learning possibilities.
If anyone has done this,
I'd be very grateful for pointers.

[tidyblocks]: {{'/2021/07/22/whatever-happened-to-tidyblocks/' | relative_url}}
