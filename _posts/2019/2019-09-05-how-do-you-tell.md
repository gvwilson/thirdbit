---
title: "How Do You Tell?"
date: 2019-09-05 03:16
year: 2019
---

I had another good conversation yesterday with [Prof. Sally Fincher](https://www.cs.kent.ac.uk/people/staff/saf/),
whose work was a big influence on [*Teaching Tech Together*](http://teachtogether.tech).
The subject was
[notional]({{'/2018/04/12/notional-machine-for-python.html' | relative_url}})
[machines]({{'/2019/07/15/notional-machine-for-r.html' | relative_url}}),
and in particular how to figure out as quickly as possible what someone's mental model of program execution includes.
For example:

> After the following code runs:
>
> ```
> A = 1
> B = A
> A = 99
> ```
>
> what is the value of `B`?

Someone who thinks in Excel will (quite fairly) say "99",
because the whole point of saying `B = A` is to make `B` equal to `A`,
while someone whose thinking is shaped by Java, Python, or the like will say that `B` is still 1.

Here's another:

> In what order are the words "before", "during", and "after" printed when this JavaScript runs?
>
> ```
> console.log('before')
> const text = fs.readFile('data.txt', (err, data) => {
>   console.log('during')
> })
> console.log('after')
> ```

The natural answer (for some very biased value of "natural") is before-during-after,
but in Callback Country,
the actual order is before-after-during.

And finally:

> In what order are "F" and "G" printed when this code runs in R?
>
> ```
> f <- function(x) {
>   print('F')
>   return (2*x)
> }
>
> g <- function(x) {
>   print('G')
>   return (2*x)
> }
>
> g(f(2))
> ```

The answer in most languages is F-G,
but the answer in R is G-F because of [lazy evaluation](https://gvwilson.github.io/tidynomicon/nse.html).

If you have short questions that you use to probe or classify people's mental models of program execution,
I'd enjoy hearing about them:
please [give me a shout](mailto:gvwilson@third-bit.com).

---

Tavish Armstrong sent this:

When a function A is defined,
and the result of a call to a function B is assigned to one of A's parameters as its default value,
many people expect B to be called each time A is called
rather than just once ag definition time:

```
def f(start=datetime.datetime.now()):
  print(start)

f() # prints 2019-09-05 15:47:20.976051
f() # also prints 2019-09-05 15:47:20.976051
f() # and again...
```

Possible causes are:

1.  Nested function definitions like `f(g())` *do* call the inner function each time they're run.
2.  Many people (including some quite experienced programmers)
    don't think of function definition as a thing programs do
    that is qualitatively the same as adding numbers.
