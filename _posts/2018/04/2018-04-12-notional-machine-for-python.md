---
title: "Is This a Notional Machine for Python?"
date: 2018-04-12 01:30
---

[Mark Guzdial](http://computinged.wordpress.com) was kind enough
to take [a few](https://twitter.com/gvwilson/status/982233353125376000)
[tweets](https://twitter.com/guzdial/status/982293974131007489) last week
to try to explain the idea of a "notional machine" to me.
If I understand correctly,
it's a competent practitioner's mental representation
of how programs in a particular language are executed,
which sounds like a mental model–except Mark tells me it's not.
That leaves me wondering if the term is like "computational thinking",
i.e.,
everyone agrees it's important but no-one agrees what it means.

I thought that writing down my notional machine for Python might help clarify discussion
(or at least my thinking).
I'm leaving out modules and objects until I know if I'm on the right track;
I'd be grateful for feedback.

1. A running program has a call stack and a heap.

1. Memory for data is always allocated from the heap.

1. Every piece of data is stored in a two-part box:
   the first part says what type the data is,
   and the second part is the actual value.

1. Atomic data like Booleans, numbers, and character strings are stored directly in the second part.
   These values are never modified after they are created.

1. The scaffolding for collections like lists and sets are also stored in the second part,
   but they store references to user-visible data values
   rather than storing those values directly.
   The scaffolding may be modified after it is created,
   e.g.,
   a list may be extended or new key/value pairs may be added to a dictionary.

1. When code is loaded,
   Python parses it and converts it to a sequence of instructions
   that are stored in heap-allocated memory just like any other data.

1. When code is executed,
   Python steps through the instructions,
   doing what each tells it to in turn.

1. Some instructions make Python read data,
   operate on it,
   and create new data.

1. Other instructions make Python jump to other instructions
   instead of executing the next one in sequence;
   this is how conditionals and loops work.

1. Yet another instruction tells Python to call a function,
   which basically means temporarily switching from one blob of instructions to another.

1. We make programs easier to understand by writing functions,
   which are recipes that give a name to a series of calculations.

1. When a function is called,
   a new stack frame is pushed on the call stack.

1. When a variable is used,
   Python looks for it in the top stack frame.
   If it isn't there,
   it looks in the base (global) frame.

1. When the function completes or returns,
   Python switches from its blob of instructions
   back to the code it was executing beforehand.
   If there isn't a "beforehand",
   the program has finished.

So:

1. Is this a notional machine?
1. If so, how does it differ from yours?
1. If not, why not?
