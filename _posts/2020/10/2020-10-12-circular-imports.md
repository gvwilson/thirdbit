---
title: "Circular Imports"
date: 2020-10-12
---

I am struggling to find a readable explanation of how circular imports are handled
in Python and JavaScript (more specifically, by the `require` function used for CommonJS modules).
Here's a short example in Python:

<table>
  <tr>
    <th><code>a.py</code></th>
    <th><code>b.py</code></th>
  </tr> 
  <tr>
    <td valign="top">
<pre>
import b

def P():
    print("P")
    b.Q()

def R():
    print("R")
</pre>
    </td>
    <td valign="top">
<pre>
import a

def Q():
    print("Q")
    a.R()
</pre>
    </td>
  </tr>
</table>

If we run this in the interpreter, the functions call each other as desired:

```
>>> import a
>>> a.P()
P
Q
R
```

And if we change `a.py` to call `P()` *as the file is being loaded*, it still works:

<table>
  <tr>
    <th><code>a.py</code></th>
    <th><code>b.py</code></th>
  </tr> 
  <tr>
    <td valign="top">
<pre>
import b

def P():
    print("P")
    b.Q()

def R():
    print("R")

P() # ADDED
</pre>
    </td>
    <td valign="top">
<pre>
import a

def Q():
    print("Q")
    a.R()
</pre>
    </td>
  </tr>
</table>

```
>>> import a
P
Q
R
```

But if we run `a.py` directly from the command line, it fails:

```
$ python a.py
P
Traceback (most recent call last):
  File "a.py", line 1, in <module>
    import b
  File "/home/gvwilson/example/b.py", line 1, in <module>
    import a
  File "/home/gvwilson/example/a.py", line 10, in <module>
    P()
  File "/home/gvwilson/example/a.py", line 5, in P
    b.Q()
AttributeError: module 'b' has no attribute 'Q'
```

Node is more consistent.
Suppose I have two JavaScript files `a.js` and `b.js`:

<table>
  <tr>
    <th><code>a.js</code></th>
    <th><code>b.js</code></th>
  </tr>
  <tr>
    <td valign="top">
<pre>
const {Q} = require('./b')

const P = () => {
  console.log('P')
  Q()
}

const R = () => {
  console.log('R')
}

module.exports = {P, R}
</pre>
    </td>
    <td valign="top">
<pre>
const {R} = require('./a')

const Q = () => {
  console.log('Q')
  R()
}

module.exports = {Q}
</pre>
    </td>
  </tr>
</table>

Running inside the interpreter fails during loading:

```
> const {P} = require('./a')
undefined
> (node:1756) Warning: Accessing non-existent property 'R' of module exports inside circular dependency
(Use `node --trace-warnings ...` to show where the warning was created)
> P()
P
Q
Uncaught TypeError: R is not a function
    at Q (/home/gvwilson/example/b.js:5:3)
    at P (/home/gvwilson/example/a.js:5:3) 
```

and we get a similar error if we modify `a.js` to call `P()` at the top level as the file is loading.
It also fails if we use a bundler like Parcel.
Our HTML file is:

```
<html>
  <head>
    <script src="./a.js"></script>
  </head>
  <body>
    <p>Hello</p>
  </body>
</html>
```

and we run with:

```
$ parcel test.html
Server running at http://localhost:234
    Build in 0.124s.
```

When we look in the browser console, we see an uncaught error because `R` is not a function.

Does this mean that circular imports simply don't work?
That seems to be the case for JavaScript,
but not necessarily for Python.
My questions now are:

1.  Why do they work sometimes for Python but not always?
1.  Do they really not work in JavaScript without extra developer effort
    (e.g., creating a module initialization function so that loading and initializing are separated)?
1.  Most importantly, where can I find tutorials that explain how things like this work---not just for these two languages
    but in general?
    Where are the compare-and-contrasts for up-and-coming software engineers
    (and older ones like myself who know a lot less than we think we do)?
    Why are books like Levine's *[Linkers and Loaders](https://www.elsevier.com/books/linkers-and-loaders/levine/978-0-08-051031-6)*
    and Pearson's *[Software Build Systems](http://catalogue.pearsoned.ca/educator/product/Software-Build-Systems-Principles-and-Experience/9780321717283.page)*
    so rare?
