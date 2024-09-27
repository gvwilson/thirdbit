---
title: "Computational Science Education (1996 edition)"
date: 2019-08-05
---

Once upon a time,
my job was to make scientists' software run
on a supercomputer that (like me) lived in the basement of a building in Edinburgh.
A new faculty member in astronomy came to my office one day
and asked if I could help him with his program.
It was about a hundred thousand lines of Fortran,
all in one file,
but to my relief it was broken up into lots and lots of functions.

It took me a lunch hour to realize that those functions were the bits of code he was no longer using.
His actual simulation was in the top half of the file;
every time he wanted to make a change
he would take a chunk of code,
move it into a function (with a meaningful name) at the bottom of the file,
and *never call it*.
He was using functions as a version control mechanism
because no-one had ever shown him a better way to do it.

[Software Carpentry](http://carpentries.org) didn't start then,
but the seed was planted.
It bore fruit five years later when I organized a short series of articles
about what computer science ought to teach physical scientists and engineers,
which led directly to the first classes that [Brent Gorda](https://www.linkedin.com/in/bgorda/) and I
taught at [Los Alamos National Laboratory](https://lanl.gov/) in the summer of 1998.
I dug out a copy of those original articles today,
and have [put them online](@root/files/2019/08/cse-education-1996.pdf)
in case anyone would like to see what has changed and what hasn't.
The design started with some user stories;
the week-long course included:

-   the Unix shell
-   editing (which the Carpentries never taught, but [others have](http://practicalcomputing.org/))
-   browing the web and writing HTML (which were pretty new back then)
-   LaTeX
-   Make
-   Perl (for lack of something better at the time)
-   Revision management (which is what we called version control back then)
-   Debugging (sure, we can cover that in a couple of hours…)
-   Profiling and tuning
-   Software testing

What's most interesting,
though,
is the replies from Rubin Landau (a computational scientist),
Steve McConnell (a software engineer),
Elizabeth Jessup and Roscoe Giles (both of whom were also computational scientists),
Dave McQueeney (who didn't think any one-week course would be useful),
and Tom Issaevitch (who worked at Wolfram Research and thought we should just teach everyone Mathematica).
I have a lot more sympathy for all but the last two of these viewpoints today than I had back then,
and wonder sometimes how things might have played out if we'd stuck with a one-week format
and tried to include a bit more of science with our computing.

And since we're strolling down memory lane,
here are the participants in our first two workshops.
I hope we helped;
I know we had fun.

<img src="@root/files/swc/lanl-1998-09.jpg" class="centered">

<img src="@root/files/swc/lanl-1998-07.jpg" class="centered">
