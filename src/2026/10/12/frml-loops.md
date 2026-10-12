---
title: "Loops in Frml"
date: 2026-10-12
category: education software-engineering
---
The first three posts in this series [introduced Frml][frml-intro],
then explained [how it checks simplar scalar code][frml-scalar]
and [contracts between functions][frml-contracts].
This post shows how Frml handles `while` loops
with invariants and termination measures.

## What It Does

Here's a minimal program with a loop:

```
fn main() -> Int
{
  let i: Int = 0;
  while i < 3
    invariant 0 <= i
    invariant i <= 3
    decreases 3 - i
  {
    i = i + 1;
  }
  return i;
}
```

The loop type checker adds one visitor to the existing code called `visit_StmtWhile`,
and the loop prover adds the same visitor plus the logic that turns a loop into obligations.
`visit_StmtWhile` checks four things:
the loop condition must have type `Bool`,
every `invariant` must have type `Bool`,
the `decreases` expression when present must have type `Int`,
and the loop body is type-checked in a fresh scope.

```python
def visit_StmtWhile(self, stmt, ret):
    self.check_expr(stmt.cond, expected=BOOL, allow_old=False, result_type=None)
    self.in_spec = True
    try:
        for inv in stmt.invariants:
            self.check_expr(inv, expected=BOOL, allow_old=False, result_type=None)
        if stmt.decreases is not None:
            self.check_expr(
                stmt.decreases, expected=INT, allow_old=False, result_type=None
            )
    finally:
        self.in_spec = False
    self._push_scope()
    for s in stmt.body:
        self.check_stmt(s, ret)
    self._pop_scope()
```

The `in_spec` flag is set while checking the loop's specifications,
just as the contracts checker does for `requires`, `ensures`, and `decreases` clauses.
It has no effect on scalar loops,
but the loop checker keeps the pattern so that subsequent levels will inherit
the same behavior.
The body gets its own scope,
so variables declared inside the loop do not leak out of it.

## Why Loops Are Hard

A loop runs an unknown number of times,
and the prover cannot execute the loop symbolically "until it ends".
It therefore reasons about the loop inductively using invariants.
A loop invariant is a fact that is true before the first iteration and after every iteration;
if both hold,
the invariant is also true immediately after the loop exits.
The prover generates one obligation for each of those two moments,
plus a post-loop exit state for whatever code follows the loop.

The invariant tells the prover what is true at those moments,
but it does not say what value each variable has.
That is a real problem:
a loop that assigns to a variable may run any number of times,
so there is no single value the prover can hand to the rest of the proof.
The prover's answer is to deliberately forget those values
as explained in the next section.

## Causing Havoc

To *havoc* a variable is to replace its value with a fresh, unknown symbol,
deliberately forgetting everything the prover previously knew about it.
This is how the prover stays sound when a value is genuinely unknown:
rather than pretending to know the final value of an assigned variable,
it admits that it does not.

This is necessary and sound because a loop may run any number of times,
so we cannot know the exact final value of an assigned variable;
we only know what the invariant tells us about it.
The invariant is the only bridge from before the loop to after it.

Before checking the inductive step,
the prover scans the loop body and applies havoc to every scalar variable the body assigns.
A `ScalarWriterCollector` walks the body
and records every name that appears on the left of an assignment,
including assignments inside nested `if` and `while` statements.
It deliberately ignores `let` declarations inside the loop body,
because those names are local to a single iteration
and do not exist before the loop.
Each recorded name that already exists in the state is replaced with
a fresh symbol of the same Z3 sort:

```python
def _fresh_from_term(self, term, name):
    if z3.is_bool(term):
        return z3.Bool(self._fresh(name))
    if z3.is_string(term):
        return z3.String(self._fresh(name))
    return z3.Int(self._fresh(name))
```

## An Example

Let's take a look at an example:

```
fn count(n: Int) -> Int
  requires n >= 0
  ensures result == n
{
  let i: Int = 0;

  while i < n
    invariant 0 <= i
    invariant i <= n
    decreases n - i
  {
    i = i + 1;
  }

  return i;
}
```

Verifying `count` emits seven obligations:
two initialization,
two preservation,
two termination,
and one final postcondition.

### Initialization Obligations

Every invariant must hold before the first iteration.
With `i = 0`,
`0 <= i` becomes `0 <= 0`
and `i <= n` becomes `0 <= n`,
proved from `requires n >= 0`.
The prover evaluates each invariant in the state that reaches the `while` and emits:

```
hypotheses:  current path
goal:        invariant
```

### Preservation Obligations

This is the inductive step,
which checks an arbitrary loop iteration,
not just the first one.

1.  Havoc every scalar variable the loop body assigns:
    `i` becomes a fresh, unknown symbol such as `i!2`,
    which forgets whatever value `i` had on entry so the check is about an arbitrary iteration.
1.  Assume the invariants and the loop condition, `0 <= i`, `i <= n`, and `i < n`.
1.  Run the loop body once symbolically, so `i = i + 1` becomes `i + 1`.
1.  Prove each invariant again for the after-body value.

For `count`, the two preservation obligations are:

```
(0 <= i and i <= n and i < n) => 0 <= i + 1
(0 <= i and i <= n and i < n) => i + 1 <= n
```

The second one uses `i < n` to prove `i + 1 <= n`.

### Exit State

After the loop,
the prover must continue with a state that satisfies the invariant and the negated loop condition.
It havocs the modified variables again,
assumes the invariants,
and assumes `not condition`.
For `count`,
after the loop, `i` becomes a fresh symbol such as `i!3`,
and the path gains `0 <= i`, `i <= n`, and `not (i < n)`, so `i >= n`.
Together these force `i == n`,
and the following `return i` proves `ensures result == n`.
The body's final value is deliberately *not* connected to the exit value;
the invariant is the only information that survives.

## Termination with `decreases`

A `decreases` clause proves that a loop terminates.
It produces two obligations.

### Before the Loop

Before the loop, the measure must be non-negative:

```
decreases >= 0
```

### After the Body

After the body, the measure must strictly decrease:

```
new_decreases < old_decreases
```

For `count`, the measure is `n - i`.
On entry, `n - 0 >= 0`, proved from `requires n >= 0`.
After the body,
with the havoced `i` and the invariant and condition facts assumed,
`n - (i + 1) < n - i` simplifies to `-1 < 0`.
The strict-decrease check uses the same havoced `i` as the preservation check.

A loop without `decreases` is still accepted;
the verifier then proves partial correctness only.
It cannot prove the loop terminates.

## A Broken Loop Invariant

A loop invariant must hold before the first iteration
*and* survive every execution of the loop body.
The example below survives the first iteration but not the second.

```
fn bad() -> Bool
{
  let i: Int = 0;
  while i < 3
    invariant i <= 2
  {
    i = i + 1;
  }
  return true;
}
```

The initialization obligation is `0 <= 2`, which holds.
The preservation obligation is built exactly like the preservation step in `count`:
havoc `i` into an arbitrary fresh symbol,
assume the invariant `i <= 2` and the loop condition `i < 3`,
run the body `i = i + 1` once to get the after-body value `i + 1`,
and prove `i + 1 <= 2`.
That gives the obligation:

```
(i <= 2 and i < 3) => i + 1 <= 2
```

Z3 finds a counterexample with `i = 2`.
Since `2 <= 2` is true,
the invariant holds before the iteration,
and since `2 < 3` is true,
the loop condition says to run another iteration,
but `2 + 1 <= 2` is false,
so the invariant is broken after the iteration.
The prover does not iterate the loop from `0` to `3`;
the preservation check symbolically executes the body once on an arbitrary `i`,
and the counterexample `i = 2` picks the arbitrary iteration
where that one step breaks the invariant.
The correct upper bound is `i <= 3`, because `i` reaches `3` before the loop exits.

[frml]: https://gvwilson.github.io/frml
[frml-contracts]: @root/2026/10/10/frml-contracts/
[frml-intro]: @root/2026/10/05/frml-intro/
[frml-scalar]: @root/2026/10/08/frml-scalar/
