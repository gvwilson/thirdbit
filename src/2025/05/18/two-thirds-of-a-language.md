---
title: Two Thirds of a Language
date: 2025-05-18
---

Inspired in part by posts online about this year's PyCon,
I started to wonder how much of the language I actually use.
To answer the question,
I counted how many different types of nodes are provided by [Python's `ast` module][ast]
and how many of those show up in the code I wrote for
[*Software Design by Example*][sdxpy].
The answer appears to be 60%,
i.e.,
I use a bit less than two-thirds of what Python 3.12 offers.
Other measures would give other answers—for example,
I expect that I use much, much less than 60% of Python's standard library—but still,
it's kind of interesting.

I hope everyone's having fun in Pittsburgh…

**The Code**

```python
import ast
from pathlib import Path
import sys

ast_dict = {name: getattr(ast, name) for name in dir(ast)}
available = {val for name, val in ast_dict.items() if isinstance(val, type) and not name.startswith("_")}

used = set()
for filename in sys.argv[1:]:
    try:
        tree = ast.parse(Path(filename).read_text())
        used |= {type(node) for node in ast.walk(tree)}
    except SyntaxError:
        pass

print(f"available: {len(available)}")
print(f"used: {len(used)}")
print(f"percentage: {(100*len(used)/len(available)):.1f}")
unused = {n.__name__ for n in available - used}
for n in sorted(unused):
    print(n)
```

**The Output**

```
available: 136
used: 81
percentage: 59.6
```

[ast]: https://docs.python.org/3/library/ast.html
[sdxpy]: @root/sdxpy/
