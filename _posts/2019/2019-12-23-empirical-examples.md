---
title: "Empirical Examples"
date: 2019-12-23 15:45:00
year: 2019
---

Back in July 2000,
I sent [these](http://mail.python.org/pipermail/python-dev/2000-July/006098.html)
[messages](http://mail.python.org/pipermail/python-dev/2000-July/006427.html)
to the Python developers' mailing list.
List comprehensions were still a new feature,
and I thought the best way to decide on a syntax was to try it out.
The idea didn't catch on,
but I still believe very strongly that
we ought to field-test language features and additions to libraries
*before* rolling them out,
and that such tests are much easier to do than most people believe.

## Message 1

**[July 11, 2000](http://mail.python.org/pipermail/python-dev/2000-July/006098.html)**

I sent the message below to the 11 developers here in the office this
morning.  They all have 10+ years experience with C, and 2-3 years with
C++, Java, or both.  None have used Python (I'm working on it :-), but two
have extensive Perl experience, and one worked on and with functional
languages in grad school.  The question was:

<div style="font-size:80%" markdown="1">
```
OK, folks, language question.  Given the statement:

    for x in [10, 20, 30]; y in [1, 2]:
        print x+y

(note that the second list is shorter than the first),
would you expect to see:

(A) 'x' and 'y' move forward at the same rate:

    11
    22

(B) 'y' goes through the second list once for each value of 'x':

    11
    12
    21
    22
    31
    32

(C) an error message because the two lists are not the same length?

Votes to me, please.

Thanks,
Greg
```
</div>

*Everyone* voted (B).  As useful as this capability is, I therefore think
the proposed syntax is likely to mislead.

Hope it's helpful,
Greg

## Message 2

**[July 13, 2000](https://mail.python.org/pipermail/python-dev/2000-July/006427.html)**

I gave 20+ grad students in computer engineering and computer science
(plus a couple of profs) the questionnaire below.
A summary of results is:

* Everyone understood the existing syntax (A).

* Most assumed that that the 'zip()' function version would yield
  cross-product iteration (B).  This surprised me a lot, particularly
  as I think we all agree that 'zip()' is the most suggestive possible
  name for this function.

* Versions (D), (F), and (H) show that semi-colon separated targets
  imply cross-product iteration, but 'and' and 'while' imply
  simultaneous iteration.

* Version (G) shows that using 'and' suggests that the sequences being
  iterated over must have the same length.

The questionnaire and a table of responses are included below (100 characters wide).

Greg

<div style="font-size:80%" markdown="1">
```
The single and double loop below print the output shown:

for x in [10, 20, 30]:          for x in [10, 20, 30]:
    print x                         for y in [1, 2, 3]:
                                        print x+y
10                              11
20                              12
30                              13
                                21
                                22
                                23
                                31
                                32
                                33

Match each of the following to its output.
(Note that several examples may print the same thing.)


                                                (1)     (2)     (3)     (4)     (5)     (6)

                                                11      11      11      11      error   ??
                                                22      12      22      12
                                                33      13              21
                                                        21              22
                                                        22              31
                                                        23              32
                                                        31
                                                        32
                                                        33

(A)
for (x, y) in [[10, 1], [20, 2], [30, 3]]:      11      0       0       0       0       0
    print x+y

(B)
for [x, y] in zip([10, 20, 30], [1, 2, 3]):     2       6       0       0       0       3
    print x+y

(C)
for [x, y] in zip([10, 20, 30], [1, 2]):        0       0       1       4       4       2
    print x+y

(D)
for x in [10, 20, 30]; y in [1, 2, 3]:          3       7       0       0       1       0
    print x+y

(E)
for x in [10, 20, 30]; y in [1, 2]:             1       0       2       6       2       0
    print x+y

(F)
for (x in [10, 20, 30]) and (y in [1, 2, 3]):   7       4       0       0       0       0
    print x+y

(G)
for (x in [10, 20, 30]) and (y in [1, 2]):      0       0       1       2       6       2
    print x+y

(H)
for x in [10, 20, 30] while y in [1, 2, 3]:     2       7       0       0       1       1
    print x+y

(I)
for x in [10, 20, 30] while y in [1, 2]:        0       1       0       7       2       1
    print x+y

(J)
for x; y in [10, 20, 30]; [1, 2, 3]:            2       3       0       1       3       2
    print x+y

(K)
for x; y in [10, 20, 30]; [1, 2]:               0       1       0       3       5       2
    print x+y
```
</div>
