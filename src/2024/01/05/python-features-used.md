---
title: "What Features of Python Do I Use?"
date: 2024-01-05
---

It's easy to answer the question in this post's title
for the Python version [*Software Design by Example*][sdxpy]
using Python's `ast` module:

```py
import ast
import sys
from collections import Counter

def main():
    seen = Counter()
    for filename in sys.argv[1:]:
        scrape(filename, seen)
    for count, name in sorted(seen.items(), key=lambda x: x[1], reverse=True):
        print(name, count)

def scrape(filename, seen):
    with open(filename, "r") as reader:
        tree = ast.parse(reader.read(), filename=filename)
        for node in ast.walk(tree):
            seen[node.__class__.__name__] += 1

if __name__ == "__main__":
    main()
```

The results shown below reveal that
the book uses a rather small subset of Python's features.
These tables is misleading, though,
since things like decorators and `else` don't show up.
Still,
I think these numbers show that:

1.  I'm pretty conservative in my Python coding.
2.  It's possible to teach a lot about design without using a lot of language features.
3.  Which implies that it's possible do a lot of design with a fairly small language.

As I wrote [a couple of days ago][other-examples],
I'm not going to write another programming book.
If I had it all to do over again,
though,
I'd think very seriously about doing just one volume in [Lua][lua]:
Roberto Ierusalimschy and his team have done us all a service
in resisting the bloat that almost every other language has succumbed to.

| Count | Name           | Comment     |
| ----: | :------------- | :---------- |
| 11619 | Load           | Read a value |
|  9667 | Name           | Variable or function name |
|  3874 | Constant       | Constant number or string |
|  3437 | Call           | Call a function or method |
|  2579 | Attribute      | Reference an object attribute with `.` notation |
|  2048 | Store          | Write a value (17% as common as reading) |
|  1416 | Assign         | Assignment (which includes updating as well as initial definition) |
|  1103 | FunctionDef    | I define a lot of little functions… |
|   803 | Subscript      | `[…]` element reference |
|   526 | Return         | Huh: only about half of my functions actually return something explicitly |
|   469 | Eq             | Value equality |
|   371 | List           | Defining a new list |
|   327 | If             | `elif` and `else` don't show up separately |
|   276 | JoinedStr      | A bunch of f-strings |
|   214 | ImportFrom     | My example programs import things from each other a lot |
|   213 | Tuple          | Tuple definition |
|   173 | For            | Loops |
|   163 | Dict           | Explicit dictionaries |
|   150 | ClassDef       | I define many fewer classes than functions in this book |
|   148 | Import         | Mostly standard libraries |
|    79 | Slice          | A lot of these are `sys.argv[1:]`… |
|    72 | AugAssign      | `+=` and its friends |
|    68 | ListComp       | I still prefer loops to list comprehensions |
|    40 | With           | I use `with` statements primarily for file I/O and mock objects in tests |
|    35 | Starred        | Spreading lists |
|    33 | Pass           | Mostly placeholders as I'm developing code in stages during a tutorial |
|    32 | Raise          | I probably should have included more about exception handling… |
|    29 | While          | 17% as many `while` loops as `for` loops |
|    24 | ExceptHandler  | See note above about exceptions |
|    22 | DictComp       | I could have written more of these, but the code can be hard to read |
|    18 | Try            | See note above about exceptions |
|    12 | Set            | Turns out constant sets are pretty rare |
|    11 | SetComp        | See above |
|    11 | Continue       | Surprised that there are more `continue` than `break` |
|    11 | Lambda         | Almost all as `key` arguments to sorting |
|     7 | Break          | See note above about `continue` |
|     1 | Del            | Removing a breakpoint from a dictionary |
|     1 | Global         | I could (and should) get rid of this… |

And here are the uninteresting bits
(e.g., intermediate nodes in the parse tree or specific arithmetic operators):

| Count | Name           | Count | Name          | Count | Name          |
| ----: | :------------- | ----: | :------------ | ----: | :------------ |
|   961 | Expr           |    57 | In            |     8 | BitOr         |
|   698 | Compare        |    55 | USub          |     7 | BitAnd        |
|   485 | Assert         |    41 | Lt            |     7 | Div           |
|   296 | FormattedValue |    40 | Sub           |     7 | IsNot         |
|   248 | Module         |    37 | NotEq         |     4 | Or            |
|   217 | BinOp          |    36 | LtE           |     4 | RShift        |
|   113 | UnaryOp        |    31 | Gt            |     3 | NamedExpr     |
|    26 | GeneratorExp   |    28 | NotIn         |     3 | GtE           |
|    21 | BoolOp         |    17 | And           |     2 | FloorDiv      |
|    20 | IfExp          |    14 | Pow           |     2 | LShift        |
|   136 | Add            |    12 | Is            |     1 | Invert        |
|    58 | Mult           |    11 | Mod           |     1 | Delete        |
|    57 | Not            |       |               |       |               |

---

Update: in memory of Niklaus Wirth,
Dana Sibera has reproduced the classic Apple Pascal poster (see below).
Like I said,
I'm not going to write another programming book,
but if I *did*,
I'd want to use a language whose grammer is no more complicated than this.

<div class="center">
  <img src="@root/files/2024/PascalPosterV1.svg" alt="Apple Pascal poster redrawn by Dana Sibera"/>
</div>

[lua]: https://www.lua.org/
[other-examples]: @root/2024/01/03/the-other-examples/
[sdxpy]: @root/sdxpy/
