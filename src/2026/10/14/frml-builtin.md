---
title: "Built-in Functions in Frml"
date: 2026-10-14
category: education software-engineering
---
Previous posts in this series [introduced Frml][frml-intro],
then explained [how it checks simplar scalar code][frml-scalar],
handles [contracts between functions][frml-contracts],
[deals with loops][frml-loops],
and [checks arrays][frml-arrays].
This post shows how Frml handles built-in functions like `push` and `pop`.
Here's an example program to motivate the discussion:

```
fn main() -> Int
{
  let a: Array<Int> = [1];
  push(a, 2);
  assert length(a) == 2;
  return 0;
}
```

## Built-in Functions

Frml's built-in functions live in `frml/builtins.py`:

-   `read(path: String) -> String` returns the contents of a file
-   `write(path: String, text: String)` writes text to a file
-   `print(text: String)` writes text to standard output
-   `split(text: String, sep: String) -> Array<String>` splits text on a separator
-   `args() -> Array<String>` returns the command-line arguments
-   `push(array, value)` appends a value to an array
-   `pop(array) -> value` removes and returns the last element

`TypeChecker.check_call` first looks the name up in `BUILTINS`.
For a non-polymorphic built-in,
it checks the argument count and each argument type against the recorded signature,
then checks that a value-returning built-in is not used as a statement.
The same path is reached whether the built-in appears as a statement or as an expression.

`push` and `pop` are marked `poly=True`
because their signatures depend on the element type of the array argument:
`_check_poly_builtin` resolves them.
`push(a, v)` requires `a` to be an array variable and `v` to have `a`'s element type;
since it is a procedure, it returns no value.
`pop(a)` requires `a` to be an array variable,
returns `a`'s element type,
and cannot be used as a statement.
Both are also rejected inside specifications,
because a specification must describe a function without mutating arrays.

## Verifying Built-Ins

The prover models most built-ins as uninterpreted values:
`read` becomes a fresh string,
`split` and `args` become fresh arrays of strings,
and `print` and `write` evaluate their arguments and then have no further effect.
The verifier can therefore prove nothing about a built-in's contents,
which is sound because file contents and command-line arguments are external to the program.

`push` and `pop` are the only built-ins that mutate a program array,
so the prover treats them specially.
The prover models `push(a, v)` as appending `v` at the current length:

```
a = Store(a, length(a), v)
length(a) = length(a) + 1
```

There is no bounds obligation: appending is always legal.
The array variable is rebound to the new `ArrayVal`.

The prover models `pop(a)` as removing the last element:

```
result = a[length(a) - 1]
length(a) = length(a) - 1
```

Unlike `push`, `pop` emits an obligation that the array is non-empty:

```
hypotheses:  current path
goal:        0 < length(a)
```

Popping an empty array is therefore a failed verification condition
rather than a runtime error.

### Resizing in Loops

A loop that calls `push` or `pop` changes an array's length,
so loop havoc must forget both the contents and the length.
A scalar assignment havocs the scalar's value,
a fixed-size array assignment havocs the array's contents but keeps its length,
and an array changed by `push` or `pop` havocs the contents and the length.
This is the same induction soundness argument as in the loop and array tutorials:
the invariant is the only information that survives the havoc.

### Resizing Across Function Calls

The builtin prover also tracks which array parameters a callee resizes.
`written_params` contains the array parameters the callee writes,
and `resized_params` is the subset of `written_params` that the callee resizes with `push` or `pop`.
At a call site,
a written-but-not-resized array parameter gets a fresh post-array with the same length,
while a resized array parameter gets a fresh post-array with a fresh,
unknown length,
and the prover assumes that length is non-negative.

## So How Do I Feel About This?

The short answer is "unsatisfied".
I didn't want to handle `push` and `pop` as special cases,
and I hoped to build some sort of effects system for I/O,
but this project is already larger than I originally intended it to be.
If some students want to take this on,
please [reach out][email].

[email]: mailto:gvwilson@third-bit.com
[frml]: https://gvwilson.github.io/frml
[frml-arrays]: @root/2026/10/13/frml-arrays/
[frml-contracts]: @root/2026/10/10/frml-contracts/
[frml-intro]: @root/2026/10/05/frml-intro/
[frml-loops]: @root/2026/10/12/frml-loops/
[frml-scalar]: @root/2026/10/08/frml-scalar/
