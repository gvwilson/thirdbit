---
title: "Introducing Frml"
date: 2026-10-05
category: education software-engineering
---
A few months ago I set out to learn how program verification works.
I tried [Lean][lean] and [Dafny][dafny],
but kept wondering how verification actually worked.
To find out,
DeepSeek and I built [Frml][frml],
which is a very simple imperative language with its own verifier.

This post walks through the Frml verification engine, explaining how a Frml
program becomes Boolean logic that the [Z3][z3] solver can check, and what Z3 does
with that logic.
The language and its verifier are layered: the `scalar` level
handles straight-line and branching code with no functions or loops,
while successive levels add features one by one.

Frml is aimed at experienced programmers: you should understand basic
Boolean logic (`and`, `or`, `not`, implication) and already know what a lexer,
parser, and abstract syntax tree (AST) are, but you need no prior background in
formal verification.

## The big picture

Frml's lexer and parser turn program text into an AST, and the typechecker rejects
programs with type errors. The prover then turns the AST into *verification
conditions* of the form:

```
hypotheses => goal
```

The prover asks Z3 to confirm every verification condition, and if Z3 confirms
all of them, the program is verified.

OK, so what's a verifier?
To start,
a *proof obligation* is a claim:

```
from these hypotheses, this goal always follows
```

Symbolically:

```
h1 and h2 and ... and hn  =>  goal
```

The `h1 ... hn` are facts known at some point in the program, and `goal` is a
fact that must hold at that point. Example claims from a real program are
"knowing `x >= 0`, prove `0 <= x`", "knowing `i < n`, prove `i + 1 <= n`", and
"knowing nothing, prove `x > x`", where the last one is false. The prover's job
is to produce claims in this shape.

## What Z3 is and what it does

Z3 is an *SMT solver*, where SMT means Satisfiability Modulo Theories. It knows
the theory of integers, arrays, strings, and Boolean logic. A formula is
*satisfiable* when some assignment of values to its variables makes it true.
Given a formula, Z3 returns one of three answers: `sat`, meaning a satisfying
assignment exists and Z3 can show you one; `unsat`, meaning no satisfying
assignment exists; or `unknown`, meaning Z3 gave up or timed out. An example
that can be satisfied:

```
formula:  x > 3 and x < 5
answer:   sat          (x = 4 works)
```

An example that cannot:

```
formula:  x > 3 and x < 4
answer:   unsat        (no integer fits)
```

## From "is it valid?" to "is it unsatisfiable?"

The prover wants to prove that `hypotheses => goal` is *valid*, meaning true
for every possible assignment of the variables. Z3 does not directly check
validity; it checks *satisfiability*. The two are connected, because `A => B`
is valid exactly when `not (A => B)` is unsatisfiable. So the prover asks Z3
about:

```
not (hypotheses => goal)
```

If Z3 says `unsat`, then no counterexample exists, so the goal is proved. If Z3
says `sat`, it found a counterexample, so the goal is false. If Z3 says
`unknown`, the proof is inconclusive. That is the entire proof mechanism, and
everything else is just building the hypotheses and goals, for a rather large
value of "just".

## Z3 in Python

The [package manager lesson][sdxpy-pack] in [*Software Design by Example*][sdxpy]
used Z3 to find compatible versions of packages.
Here's a simple example of its use:

```python
from z3 import Bool, Solver

A = Bool("A")
B = Bool("B")
C = Bool("C")
```

`A`, `B`, and `C` do not have specific values. Each instead represents the set
of possible Boolean values, so we can specify constraints like `A == B`.

```python
solver = Solver()
solver.add(A == B)
solver.add(B == C)
report("A == B & B == C", solver.check())
```

We can then ask Z3 to find a *model* that satisfies those constraints:

```
A == B & B == C: sat
A False
B False
C False
```

To see unsatisfiability, require `A` to equal `B` and `B` to equal `C` but `A`
and `C` to be unequal:

```python
A = Bool("A")
B = Bool("B")
C = Bool("C")
solver = Solver()
solver.add(A == B)
solver.add(B == C)
solver.add(A != C)
report("A == B & B == C & B != C", solver.check())
```

```
A == B & B == C & B != C: unsat
```

The next post in this series will show how Frml builds proof obligations
for simple programs that manipulate scalar variables without loops or conditionals.

[dafny]: https://dafny.org/
[frml]: https://gvwilson.github.io/frml
[lean]: https://lean-lang.org/
[sdxpy]: https://third-bit.com/sdxpy/
[sdxpy-pack]: https://third-bit.com/sdxpy/pack/
[z3]: https://github.com/Z3Prover/z3
