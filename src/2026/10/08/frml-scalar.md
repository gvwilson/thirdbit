---
title: "Scalar Code in Frml"
date: 2026-10-08
category: education software-engineering
---
The [first post][frml-intro] in this series introduced [Frml][frml],
a little procedural language I created
so that I could learn how program verification works.
This post explains how Frml checks `scalar`-level programs
that have straight-line and branching code over scalar values
with no function calls, contracts, loops, or quantifiers.

## The Prover's Data Model

The prover tracks a program point with a `State` object.
`State.vars` holds the symbolic values of scalar variables,
and `State.path` holds every fact assumed to hold so far.
The prover never stores concrete numbers in variables;
it stores [Z3][z3] formulas about numbers.
For example,
`x` might hold the symbolic integer `x!1` rather than the number 5,
where `x!1` means "the first fresh symbol named `x`".

An `Obligation` records one claim to prove.
Its `kind` can be `assert` or `division` at this level,
its `description` is the human readable text of the claim,
`hyp` is the list of hypothesis terms,
`goal` is the goal term,
and `pos` is the source position of the claim
(shown in `--trace` output).

## Fresh Names

The prover keeps a counter and calls `_fresh(name)`
to get `name!N` with an increasing `N`,
so `x!1`, `x!2`, and `x!3` are different symbols
even though they all relate to the source variable `x`.
This matters because when `x` is reassigned,
the old `x!1` is not overwritten;
the new value becomes a new symbol such as `x!5`,
which keeps the symbolic execution correct.
For example, after the statement:

```
x = x + 1;
```

the state maps `x` to the term `x!1 + 1`, not to a number.

## Operation

The prover works in two phases:
it generates obligations by walking the AST and collecting `Obligation` objects,
then checks them by handing each obligation to Z3 and turning the answers into outcomes.
`verify()` is the generation phase for the whole program:

```python
def verify(self):
    results = []
    for fn in self.program.functions:
        self.obligations = []
        self.current_fn = fn
        self.verify_function(fn)
        results.append(ProverResult(fn.name, self.obligations))
    self.obligations = []
    return results
```

`verify` verifies one function at a time in source order;
`self.obligations` is reset per function so obligations stay grouped by function.
`verify_function()` handles one function:

```python
def verify_function(self, fn):
    state = State()

    # Entry state: fresh constants for the parameters.
    for p in fn.params:
        state.vars[p.name] = self._fresh_scalar(p.type, p.name)

    # Snapshot for `old(...)` (unused at this level; higher levels read it).
    state.old_vars = dict(state.vars)

    self._assume_spec(fn, state)

    # Run the body.  Surviving states reached the end without `return`; for
    # a value-returning function that is an error.
    end_states = self.exec_stmt_seq(fn.body, state)
    if fn.return_type is not None:
        if end_states:
            raise FrmlVerificationError(
                f"function {fn.name!r} has a path that does not return", fn.pos
            )
    else:
        for s in end_states:
            self._check_ensures(fn, s, None)
```

`_assume_spec` and `_check_ensures` do nothing at this language level
because there are no `requires`, `ensures`, or `decreases` clauses,
so the entry path is empty and the body's fall-through is simply checked.
`exec_stmt_seq` returns the states of paths that fell off the end of the body.
A `return` produces no end state (see below),
so if a value-returning function has any end state,
some path never returned,
which is an error.

## Statements

Statements are handled by three related methods:

```python
def exec_stmt_seq(self, stmts, state):
    states = [state]
    for stmt in stmts:
        new_states = []
        for s in states:
            new_states.extend(self.exec_stmt(stmt, s))
        states = new_states
        if not states:
            break
    return states


def exec_block(self, stmts, state):
    before_vars = set(state.vars)
    states = self.exec_stmt_seq(stmts, state)
    for s in states:
        for name in list(s.vars):
            if name not in before_vars:
                del s.vars[name]
    return states


def exec_stmt(self, stmt, state):
    return stmt.accept(self, state)
```

In `exec_stmt_seq`, `states` is the set of live paths,
starting with the single entry state,
and each statement maps every live state to zero or more successor states (see below).
`exec_stmt` calls `stmt.accept(self, state)`,
which dispatches to `visit_StmtAssign`, `visit_StmtIf`, `visit_StmtLet`, and so on.
The "zero or more" matters because of `return`:

```python
def visit_StmtReturn(self, stmt, state):
    value, state = self.eval_rhs(stmt.expr, state)
    self._check_ensures(self.current_fn, state, value)
    return []
```

A `return` returns the empty list.
`new_states.extend([])` adds nothing,
so that path is dropped from `states`;
execution stops there, exactly as it does at run time.
This is also what makes the `verify_function` fall-through check work,
since only paths that reach the end of the body survive in `end_states`.

`exec_block` is `exec_stmt_seq` plus scoping.
After a nested block (i.e., an `if` body) runs,
any variables introduced inside it are deleted from the resulting states,
so local declarations do not leak outward.

## Expressions

Expressions use the same visitor pattern as statements:

```python
def eval_expr(self, expr, state, *, use_old=False, result_term=None):
    return expr.accept(self, state, use_old=use_old, result_term=result_term)
```

`expr.accept(...)` calls `visit_ExprBinary`, `visit_ExprVar`, and so on.
Each visitor returns a Z3 term.
`eval_expr` never actually computes anything;
as noted above,
it translates a Frml expression into the Z3 formula that describes it
using the current symbolic state.

## A Complete Trace

Let's trace a complete verification:

```
fn main() -> Int
{
  let x: Int = 3;
  assert x > 0;
  return 0;
}
```

1.  `verify_program` builds the `ScalarProver` and calls `verify()`.
1.  `verify()` sets `current_fn = main` and calls `verify_function(main)`.
1.  `verify_function` builds the entry state: `state.vars` is empty (no
    parameters), and the path is empty.
1.  `exec_stmt_seq([let, assert, return], state)` starts with `states = [state]`.
1.  `let x: Int = 3;` evaluates the literal `3` and stores it in
    `state.vars["x"]` as the Z3 integer `3` (not a fresh symbol).
1.  At `assert x > 0;`, the prover evaluates the assertion expression:
    -   `x` looks up the stored term `3`.
    -   `>` builds the Z3 term `3 > 0`.
1.  The prover emits one obligation:
    -   kind: `assert`
    -   description: `assert (x > 0)`
    -   hypotheses: the current path (empty here)
    -   goal: `3 > 0`
1.  `return 0` drops the path, so `end_states` is empty and no error is raised.
1.  `verify()` records `ProverResult("main", [the one obligation])`.
1.  `verify_program` hands the obligation to `check_obligations`, which builds
    the claim `not (True => 3 > 0)` and asks Z3 to satisfy it (see "The Z3 check
    loop" below).
1.  Z3 finds no assignment that makes `not (3 > 0)` true, so it returns `unsat`,
    and the obligation is `VERIFIED`.

`uv run frml check --trace examples/scalar/ex01_assign_then_assert.frml` prints:

```
fn main
--- assert:4:3: assert (x > 0)
    prove: (> 3 0)
    => VERIFIED
VERIFIED
```

## Translating expressions to Z3

`eval_expr` maps each Frml expression node to a Z3 term.

-   Literals:
    `42` becomes `z3.IntVal(42)`,
    `true` becomes `z3.BoolVal(True)`,
    and `"hi"` becomes `z3.StringVal("hi")`.
-   Variables:
    the variable `x` becomes the term currently stored in `state.vars["x"]`.
-   Operators:
    `a and b` becomes `z3.And(a, b)` and so on for other unary and binary operators.

Division by zero is undefined,
the verifier turns it into another proof obligation.
n the prover evaluates `a / b` or `a % b`, it first emits:

```
hypotheses:  current path
goal:        b != 0
```

and then returns the Z3 division or modulo term. For example:

```
fn main() -> Int
{
  let x: Int = 10;
  let y: Int = 2;
  if y != 0 {
    assert x / y == 5;
  }
  return 0;
}
```

The `if y != 0` guard puts `y != 0` on the path before the division. The
division emits `y != 0`, which the path already contains, so Z3 proves it
immediately.

## Branching

A conditional statement forks the symbolic execution.
The condition is evaluated once,
then the `then` branch continues with the condition added to the path,
while the `else` branch continues with `not condition` added to the path.
(If there is no `else`, the fall-through branch still gets `not condition`.)

The prover tracks a *list* of states, one per path through the code.
Here is the code that does the forking:

```python
def visit_StmtIf(self, stmt, state):
    cond, state = self.eval_rhs(stmt.cond, state)
    then_state = state.copy()
    then_state.path.append(cond)
    then_ends = self.exec_block(stmt.then, then_state)
    ends = list(then_ends)
    if stmt.else_ is not None:
        else_state = state.copy()
        else_state.path.append(z3.Not(cond))
        ends.extend(self.exec_block(stmt.else_, else_state))
    else:
        else_state = state.copy()
        else_state.path.append(z3.Not(cond))
        ends.append(else_state)
    return ends
```

## `assert`

An `assert` statement produces a goal from the current path:

```
assert 1 < 2;
```

The prover evaluates the condition, emits an obligation with the current path
as hypotheses and the condition as goal, and if Z3 proves it, execution
continues with the fact now guaranteed.

> The prover does not add the assertion to the path after checking
> because `assert` is a check, not an assumption.
> The programmer asserts what should already be true,
> so the verifier must prove it from what came before.

## The Z3 Check Loop

`check_obligations` is where Z3 is actually called:

```python
solver = z3.Solver()
solver.set(timeout=timeout_ms)

for ob in obligations:
    solver.push()
    hyp = z3.And(*ob.hyp) if ob.hyp else z3.BoolVal(True)
    solver.add(z3.Not(z3.Implies(hyp, ob.goal)))
    result = solver.check()

    if result == z3.unsat:
        -> VERIFIED
    elif result == z3.sat:
        -> FAILED with the counterexample model
    else:
        -> UNKNOWN

    solver.pop()
```

Each obligation gets a fresh solver context via `push` and `pop`.
The empty hypothesis list becomes `True`.
With no hypotheses, the claim is `goal` alone, i.e. `True => goal`.
The code writes `z3.BoolVal(True)` so `z3.And(*ob.hyp)` always has a value,
because Z3's `And()` is not defined over an empty argument list.
Z3 is asked to satisfy `not (hyp => goal)`.
`unsat` means the claim holds,
`sat` means a counterexample exists,
and anything else is `unknown`.

[frml]: https://gvwilson.github.io/frml
[frml-intro]: @root/2026/10/05/frml-intro/
[z3]: https://github.com/Z3Prover/z3
