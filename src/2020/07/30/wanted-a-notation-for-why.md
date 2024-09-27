---
title: "Wanted: A Notation for 'Why'"
date: 2020-07-30
---

We've been working on the next version of TidyBlocks,
which means I've been programming again after a hiatus of several months.
I enjoy it,
much as I imagine my mother enjoyed knitting,
but the older I get,
the more frustrated I am by our tools.
For example,
the `Program` class has a `Map` called `waiting` from sets of strings to runnable pipelines,
each of which can depend on zero or more other pipelines.
As a pipeline runs,
it can call `Program.notify(label)` to say,
"Tell anything that depends on `label` that the result it needs to run is now available."
Once all of a pipeline's dependencies are ready,
it is removed from `waiting` and added to the runnable queue (called `queue`).
The code looks like this:

```js
/**
 * Notify the manager that a named pipeline has finished running.
 * This enqueues pipeline functions to run if their dependencies are satisfied.
 * @param {string} label Name of the result that was just produced.
 */
notify (label) {
  util.check(label && (typeof label === 'string'),
             `Cannot notify with empty label`)
  util.check(this.env instanceof Env,
             `Program must have non-null environment when notifying`)
  const toRemove = []
  this.waiting.forEach((dependencies, pipeline) => {
    dependencies.delete(label)
    if (dependencies.size === 0) {
      this.queue.push(pipeline)
      toRemove.push(pipeline)
    }
  })
  toRemove.forEach(pipeline => this.waiting.delete(pipeline))
}
```

But why does this method build a list called `toRemove` while it's checking dependencies,
then go back and remove the pipelines in that list from `waiting`?
Why doesn't it just called `this.waiting.delete(pipeline)` inside the first `forEach`?
The reason is that it's not safe to remove items from a `Map` while iterating over it:
doing so can result in items being missed or in the wrong item being removed.

That's not what annoys me, though.
What annoys me is that I don't have any better way to explain why two `forEach`es are needed
than a sentence or two of plain text.
Modeling notations like UML can show what I'm doing (sort of),
and with enough work I could write something in a rigorous specification language like [TLA+](https://en.wikipedia.org/wiki/TLA%2B)
that would allow the computer to warn me if I *did* try to delete items inside the main `forEach`,
but neither of those is the "why" that the next human being needs.

All of which has me thinking about [dplyr](https://dplyr.tidyverse.org/) pipelines
and about whether every verb should have an optional `inOrderTo` parameter
so that I can write pipelines like this:

```r
infant_hiv %>%
  filter(estimate != 0.95,
         inOrderTo="Get rid of markers used by field workers to indicate unreliable data") %>%
  filter((0.5 <= low) & (high <= 0.7),
         inOrderTo="Select estimates in the 50-70% range") %>%
  group_by(year,
           inOrderTo="Look at annual averages in this band") %>%
  summarize(ave_range = mean(high - low),
            inOrderTo="Look at how the actual range in this band changes over time")
```

I know I can do this with comments,
but this would encourage authors to explain specific steps more precisely.
The next step would be to come up with a (restricted, checkable) vocabulary
like that used in [Gherkin](https://cucumber.io/docs/gherkin/reference/)…

…or something equally nebulous.
I'm not a data scientist,
so I don't know exactly what would be most useful in practice,
but as I help a colleague figure out why Booleans are showing up as strings,
what I *do* know is that there has to be a better way.
