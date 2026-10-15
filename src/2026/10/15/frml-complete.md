---
title: "Frml: Next Steps"
date: 2026-10-15
category: education software-engineering
---
Previous posts in this series [introduced Frml][frml-intro],
explained [how it checks simplar scalar code][frml-scalar]
and handles [contracts between functions][frml-contracts],
and then discussed how it [deals with loops][frml-loops],
[checks arrays][frml-arrays],
and [checks built-in functions][frml-builtins].
The final language level, `complete`,
doesn't add any new features.
Instead,
it serves as a placeholder in case we want to extend the language further.
I'm not going to do this myself,
but if you are a student (or a professor looking for projects for students)
please [get in touch][email].

## Algebraic Data Types and Pattern Matching

Add `enum` sum types and a `match` expression
to teach structural induction over data and Z3's datatype theory.
A sample program would be:

```
enum Option<T> { None, Some(T) }

fn get_or(a: Option<Int>, d: Int) -> Int
  ensures result == d or result != d
{
  match a {
    None => d,
    Some(v) => v,
  }
}
```

Frml currently proves things about numbers and arrays
but never about the shape of a value.
Lists, options, and trees are where induction over data structures becomes real,
and the classic proofs
(list length, `append` associativity, `map` distributes over `append`)
are exactly what separates "checked the arithmetic" from "verified a data structure".
Z3 has a native datatype sort,
so this is more a type-checker and visitor addition than new solver machinery.
It would sit as a `datatype` level above `contracts`,
and recursive types would reuse the existing `decreases` machinery.

## Explicit Frame Clauses (`modifies` / `reads`)

Frml already infers `written_params`,
but the language gives the programmer no way to state what a call may touch.
An explicit, checked clause makes that contract visible:

```
fn increment_first(a: Array<Int>)
  modifies a
  ensures a[0] == old(a[0]) + 1
```

This would teach the frame problem, modular verification, and information hiding.
The pedagogical payoff is the frame problem:
proving that a call does not change everything else.
A student who writes `modifies a` and then has the verifier flag an unlisted write
learns why modularity fails without framing,
and why "what may this function change?" is a first-class specification question
rather than an implementation detail.
It also becomes the bridge to the hardest topics:
aliasing and separation logic,
which the current "arrays are references but aliasing is forbidden" design
deliberately sidesteps.

## Machine Integers (Bit Vectors) vs. Mathematical Integers

Frml's `Int` is an unbounded mathematical integer,
so `x + 1 > x` is always true.
If we add a bounded type or a `--int-model bitvector` switch,
that theorem quietly breaks:

```
fn add_one(x: Int32) -> Bool
  ensures x + 1 > x   // false when x == Int32.max
```

This is arguably the most important caveat in applied verification:
the model is not the machine.
It teaches why SMT solvers are split into theories,
why overflow is a real bug class,
and why a verified program can still be wrong if the verification model diverges from the runtime.
It also gives a natural way to discuss the tradeoff,
since bit-vector reasoning is harder for the solver than integer arithmetic.

## Ghost Code and Lemmas

The final idea is to extend the language
so that programmers can introduce names and functions that exist only in specifications:

```
ghost var count: Int = 0;

lemma append_len(a: List<Int>, b: List<Int>)
  ensures length(a ++ b) == length(a) + length(b);
```

These *ghost variables* are the classic trick for proving properties
that the running program has no reason to record,
and lemmas are how a verified fact gets packaged and reused across functions
instead of being re-derived inline.
Together they teach that a proof is a structure of its own
that can be layered on top of,
but kept separate from,
the executable program,
and they unlock the "mathematical library" style of verification
that makes large programs tractable.
This composes naturally with the first feature idea,
since inductive lemmas over data types are the standard way to prove list properties.

[email]: mailto:gvwilson@third-bit.com
[frml]: https://gvwilson.github.io/frml
[frml-arrays]: @root/2026/10/13/frml-arrays/
[frml-builtins]: @root/2026/10/14/frml-builtin/
[frml-contracts]: @root/2026/10/10/frml-contracts/
[frml-intro]: @root/2026/10/05/frml-intro/
[frml-loops]: @root/2026/10/12/frml-loops/
[frml-scalar]: @root/2026/10/08/frml-scalar/
