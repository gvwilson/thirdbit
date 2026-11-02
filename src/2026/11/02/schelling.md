---
title: "Testing the Schelling Segregation Model"
date: 2026-11-02
category: software-carpentry software-engineering
katex: true
---

In 1971,
economist Thomas Schelling asked whether mild individual preferences for similar neighbours
could produce large-scale residential segregation.
The answer is yes:
even when each agent requires only 30% of occupied neighbours to share its type,
the population self-organises into sharply segregated clusters.
The Schelling model is an example of an agent-based model:

-   Place two types of agents on a grid, leaving some cells empty.
-   At each step, identify dissatisfied agents and move each to a random empty cell.
-   Repeat until no agent moves, or for a fixed number of steps.

It's a landmark result in computational social science
because it shows that macro-level patterns can emerge from micro-level rules
without central coordination.
It's fairly easy to implement in Python,
but testing it is a challenge.

## Implementation

The grid is an $N \times N$ array.
Each cell holds one of three values:
0 (empty), 1 (red agent), or 2 (blue agent).
The Moore neighborhood of a cell is the set of adjacent cells horizontally, vertically, or diagonally,
and the same-neighbor fraction for an agent at position $(r, c)$ is:

<p>$$f(r,c) = \frac{\text{occupied neighbors of the same type}}{\text{total occupied neighbors}}$$</p>

An agent is *satisfied* when $f(r,c) \geq \theta$, where $\theta$ is the threshold.
An agent with no occupied neighbors is treated as satisfied ($f = 1$)
so that isolated agents do not drift endlessly across empty space.

We initialize the grid by placing equal numbers of red and blue agents at random
in a fraction $(1 - p_e)$ of cells, where $p_e$ is the empty fraction.
(Those empty cells provide the vacancies that dissatisfied agents move into.)
In each simulation step, we do the following:

-   All dissatisfied agents are identified first, then all empty cells.
-   Both lists are shuffled independently and paired in order.
-   Each dissatisfied agent moves to the corresponding empty cell if one exists.
-   Shuffling before pairing ensures no agent is systematically favored.

The satisfaction rate (i.e., the fraction of agents that meet the threshold)
rises as the grid segregates,
and reaches 1.0 when every agent is happy with its neighborhood.
This happens pretty quickly:

<img src="@root/files/2026/schelling-grid.svg">

## Testing

So how do we test this?
More specifically,
what do we get when we ask an LLM to generate tests for this?

1.  Grid shape and contents
    -   `make_grid` must produce a $(50 \times 50)$ array whose cells are all in $\{0, 1, 2\}$
2.  Balanced agent counts
    -   Red and blue agents are built as equal halves of the occupied pool,
        so their counts differ by at most 1
        (an off-by-one when the total number of agents is odd)
3.  Neighbor fractions
    -   An isolated agent (no occupied neighbors) must return 1.0,
        matching the convention that isolated agents are considered satisfied
    -   An agent surrounded entirely by the same type returns 1.0
    -   One surrounded entirely by the opposite type returns 0.0
4.  Stable segregated grid
    -   A $4 \times 4$ grid with red in the left two columns and blue in the right two columns
        is fully satisfied
    -   Border agents have $5/8 = 0.625$ same-type neighbors which exceeds the threshold of 0.3
    -   One step must leave the grid unchanged
5.  Satisfaction increases
    -   Starting from the random initial grid,
        the satisfaction rate after 20 steps must exceed the initial rate
        because agents self-organise into clusters

The first three items don't exercise the science at all.
That doesn't mean they're not important, but they feel a bit trivial.
The fourth and fifth items are more interesting,
but take a close look at the fifth one.
It is possible (though extremely unlikely) for a stochastic process to fail this test.
How should we handle that?
"Don't worry about it" might actually be the right answer:
as discussed [last year][some-testing-answers],
if the odds of a statistically-correct test failing are on par with
the odds of two Git hashes colliding,
we should turn our attention elsewhere.

The problem is that I don't know how to calculate those odds.
"It seems pretty unlikely to me" isn't satisfying,
particularly given how prone human beings are to confirmation bias.
As more and more scientists generate code with LLMs,
and use those same LLMs to generate tests,
I'd be very grateful for answers to these questions.

[some-testing-answers]: @root/2025/05/19/some-testing-answers/
