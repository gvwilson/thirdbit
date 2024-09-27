---
title: "When I Said 'The Last Twenty Years…'"
date: 2009-11-16
---
<p>Last week, in response to Google's announcement of a new programming language called Go, I said:</p>

<blockquote>I'm underwhelmed: it's as if the last 20 years of programming language research hadn't happened.</blockquote>

<p>Turns out I was being generous: read <a href="http://www.cowlark.com/2009-11-15-go/">this post</a> from start to finish, and you'll see what I mean.</p>

<p>So what <em>should</em> a new programming language do to get my attention? First, just as applications should be designed for testability, languages should be too. That means choosing constructs to make the lives of static and dynamic analysis tools better. Building such tools after the fact is like trying to add security to an app after it has been deployed; I think we'd do better to treat the capabilities of today's leading-edge program analysis tools as hard (but not unbreakable) constraints on what's allowed to go into a language, and see how far it gets us. I suspect this will push us toward strongly typed and mostly functional languages.</p>

<p>Second, user testing of language features. The folks at CWI did this with <a href="http://homepages.cwi.nl/~steven/abc/">ABC</a> (a precursor of Python); Steven Clarke has done excellent work on API usability at Microsoft (see for example <a href="http://www.ddj.com/windows/184405654">this DDJ article</a> from 2004), and there's lots of other prior art—hell, I did a little myself nine years ago for Python (see these messages for details). I'm not suggesting design by committee [1], but checking to see how comprehensible or surprising feature XYZ is going to be to the average programmer before it's put into the language just seems like common sense. I suspect this will push us <em>away</em> from pure functional languages: monads are just plain hard, and while <a href="http://www.amazon.com/Purely-Functional-Structures-Chris-Okasaki/dp/0521663504">purely functional data structures</a> are possible, they're hardly intuitive.</p>

<p>Third, a new language should explicitly be designed to make the expression of common design patterns as straightforward as possible. Languages (of all kinds, not just programming languages) evolve by formalizing the common usages of the day: idiomatic uses of goto statements become for loops, structs with function pointers become objects, and so on. There's a tremendous literature on design patterns at several scales; why not treat them as something akin to use cases?</p>

<p>Of course it's never too late—if someone has the time and energy, they could apply these three criteria to Go (or any other language) right now. Hm… sounds like an interesting thesis topic…</p>

<p>[1] Which gets an unfairly bad rap—both the American Constitution and the King James version of the Bible were produced by committees.</p>
