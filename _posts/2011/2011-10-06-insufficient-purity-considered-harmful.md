---
title: "Insufficient Purity Considered Harmful"
date: 2011-10-06 00:39:32
year: 2011
---
Joseph Hellerstein, a professor in the Computer Science department at UC Berkeley, posted an article on his blog a couple of weeks ago titled, "<a href="http://databeta.wordpress.com/2011/09/15/is-teaching-mapreduce-healthy-for-students/">Is Teaching MapReduce Healthy for Students?</a>" His conclusion?
<blockquote><em>I have begun to think that Google's MapReduce model is not healthy for beginning students. The basic issue is that Google's narrow MapReduce API conflates logical semantics (define a function over all items in a collection) with an expensive physical implementation (utilize a parallel barrier).</em></blockquote>
I had reached the opposite conclusion, so I forwarded the link to a colleague who runs training at a supercomputing center. His response (edited only to fix autocorrect-induced typos) was:
<blockquote>See, this is why by the time students get to me, they have no knowledge of even the most rudimentary concepts of parallelism; existing solutions are insufficiently pure for CS profs. (And yet what they end up learning is Java!? How did we find ourselves in a position where Java is the default, and any attempt to add other things to the curriculum is killed dead because of lack of conceptual purity? We're raising a generation of CS students who think the world of programming starts and end with a JVM, or for really well-rounded students, some C++...)

I'm not a huge fan of Hadoop, or even MapReduce as a model, but it works really well for a lot of things, and it's a completely different mental model. Different models which work well in some sufficiently large domain should presumably be Good Things. I'm sorry its runtime semantics cause this guy to cry inside and everything, but life is tough.

If we're waiting for perfect languages in some domain before teaching them to students (again: Java?) then we're basically asking those people who task is to eventually <em>build</em> those perfect languages to do so without having any grounding what's come before. And we're living the inevitable outcome–endless wheel re-invention, endless grinding gears.</blockquote>
