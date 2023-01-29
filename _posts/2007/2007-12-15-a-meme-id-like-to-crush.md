---
title: "A Meme I'd Like To Crush"
date: 2007-12-15 10:47:24
year: 2007
---
Over on O'Reilly Radar, Nat Torkington recently <a href="http://radar.oreilly.com/archives/2007/12/amazon_simpledb.html">posted</a>:
<blockquote>According to a blog post by (update: a friend of) one of the developers, <a href="http://www.satine.org/archives/2007/12/13/amazon-simpledb/">Amazon's SimpleDB is built on Erlang</a>.  Cool!  Another datapoint for the trend we see towards parallel-capable languages like Erlang and Haskell.</blockquote>
"Parallel-capable"? I know the arguments—values in pure functional languages (PFLs) are immutable once created, so there can't be race conditions, so parallel programming is easier, and parallel programs will scale better—but I have yet to see any data to substantiate that oft-repeated meme. I <a href="http://mitpress.mit.edu/catalog/item/default.asp?ttype=2&tid=8185">wrote a book</a> about parallel programming in the early 90s, and have maintained a more-than-casual interest in the topic ever since (mostly through work with computational scientists).  I don't believe that PFLs make non-trivial parallel programs easier to write. I don't believe they make parallel programming harder, either, and the reason I don't is that I haven't seen any empirical studies of real programmers writing real programs that point either way. I hereby offer a very nice bottle of wine and/or all seven seasons of <a href="http://www.imdb.com/title/tt0118276/"><em>Buffy the Vampire Slayer</em></a> to the first person to conduct a study rigorous enough to be accepted as a senior undergraduate project in psychology—a standard which, sadly, most discussion of the merits of various programming languages, tools, and paradigms signally fails to meet.

Note: if you'd like to know what those standards are—i.e., what kind of evidence you should require someone who's pushing the software equivalent of a cure for baldness to give you—please have a look at:
B.A. Kitchenham, S.L. Pfleeger, L.M. Pickard, P.W. Jones, D.C. Hoaglin, K. El Emam, and J. Rosenberg: "Preliminary guidelines for empirical research in software engineering". <cite>IEEE Transactions on Software Engineering<cite>, 28(8), August 2002.</cite></cite>

Barbara A. Kitchenham, Tore Dyba, and Magne Jorgensen: "Evidence-Based Software Engineering". <cite>Proc. 26th International Conference on Software Engineering (ICSE'04)</cite>, 2004.
