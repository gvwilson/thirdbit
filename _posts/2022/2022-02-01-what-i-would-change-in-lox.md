---
title: "What I Would Change in Lox for Teaching"
date: 2022-02-01
year: 2022
---

I spent a couple of weeks last year noodling around with Lox,
the little language that Bob Nystrom created for his wonderful book
*[Crafting Interpreters](https://craftinginterpreters.com/)*.
As [I said then]({{'/2021/12/26/effort-estimation/' | relative_url}}),
languages like Python and JavaScript are larger than they used to be,
so I'm looking for something smaller for teaching [software design]({{'/sdxjs/' | relative_url}})
(say, about the same size as Pascal was in 1980).
I don't have time to make all the changes I'd like to Lox,
but I hope that writing them down and explaining why will spark ideas in someone else:

1.  *Add array and hash values* so that `x = [1, 2, 3]` and `y = {"a": 1, "b": 2}` work.
    I'd like to add sets as well—I think they're under-rated and under-used—but
    I'm trying to budget complexity.

2.  *Add modules* and some kind of import mechanism
    so that learners can see how to break problems down into reusable pieces
    and manage the namespaces that come from doing so.

3.  *Add an infix string conversion operator* so that `print("We need " # x # " balls of yarn.")` works.
    If the thing being stringified has the right method,
    the operator should call that
    (which turned out to be trickier to implement in Lox than I expected).
    This isn't just about making `print` easier to use without adding varargs to the language:
    showing learners how to hook into a language's runtime can be mindblowing.

4.  *Replace Lox's C-style `for` loops with iterators*
    and implement a Python-style iterator protocol so that programs can loop over user-level classes.
    Again, the main purpose for doing this is to explore the design possibilities it opens up.

5.  *Make function definition an expression* rather than a statement
    so that users can define little functions on the fly.
    The idea that functions are just another kind of data is one of the most powerful in programming,
    and I'd like to make it as frictionless to use (and teach) as possible.

6.  *Add fibers* or some other lightweight concurrency mechanism
    (but *not* JS-style callbacks or promises, because brr...).
    Lox's predecessor [Wren](https://wren.io/) provides fibers for co-operative multitasking;
    combined with [`libuv`](http://libuv.org/) it would allow lessons on asynchronous I/O,
    which I believe is as important to learn now as `stdio`-based pipes were for my generation.

7.  *Add reflection*.
    Going back to point #5, treating code as data is a tremendously powerful idea,
    and everything from testing harnesses to object-relational mappers rely on it.

The one other thing I really want to add that isn't on this list is
the hooks needed for a breakpointing debugger and for coverage/profiling tools.
I think the debugger hooks are the most important,
but there's no point adding them without also providing a debugger;
that said,
a 1970s-style command-line interface would work,
and once again would open a lot of teaching doors.
(For example, I'd really like to be able to show students
how to write scripts to control debugging sessions
because boy howdy is that powerful once you have it.)

My guess is that there's about 100 hours of work on the bullet list
and another 100 for the runtime hooks and debugger,
but I think the result would be a very nice little teaching language.
If only the days were longer...
