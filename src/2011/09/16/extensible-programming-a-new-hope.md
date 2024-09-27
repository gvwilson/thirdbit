---
title: "Extensible Programming: A New Hope"
date: 2011-09-16
---
Back in 2004, I wrote an article for <a href="http://queue.acm.org"><cite>ACM Queue</cite></a> titled "<a href="http://queue.acm.org/detail.cfm?id=1039534">Extensible Programming for the 21st Century</a>". In it, I argued that it was time for programming languages to break free from their textual shackles–that we should separate models (the program's content) from views and controllers (how that content is displayed), just as we have with CAD systems, word processors, and other tools that work with rich, highly-structured content. Before I look at some recent signs of progress, let me back up and explain both the problem and why I think model-view separation is the solution. What I want is a programming "language" that can be extended in a wide variety of ways. That's pretty conventional–every modern language lets people define new functions, create new types, overload operators, etc.–but I think that's much too limited. I want to be able to embed a table in a program as a first-class object, so that instead of:
<pre>if x:
    if y:
        z == 0
    else:
        z == 1
else:
    if y:
        z == 2
    else:
        z == 3</pre>
I can write
<table class="centered">
<tbody>
<tr>
<td valign="center">z</td>
<td valign="center">=</td>
<td>
<table class="centered">
<tbody>
<tr>
<td colspan="2"></td>
<td colspan="2" align="center" valign="center">y</td>
</tr>
<tr>
<td colspan="2"></td>
<td align="center" valign="center">True</td>
<td align="center" valign="center">False</td>
</tr>
<tr>
<td rowspan="2" align="center" valign="center">x</td>
<td align="center" valign="center">True</td>
<td align="center" valign="center">0</td>
<td align="center" valign="center">1</td>
</tr>
<tr>
<td align="center" valign="center">False</td>
<td align="center" valign="center">2</td>
<td align="center" valign="center">3</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
Actually, scrap that: what I want is to be able to embed a full-blown spreadsheet in amongst other statements so that I can write:
<table class="centered">
<tbody>
<tr>
<td colspan="3">def func(a, b):</td>
</tr>
<tr>
<td></td>
<td>x =</td>
<td>a &gt; b</td>
</tr>
<tr>
<td></td>
<td>y =</td>
<td>something(a, b)</td>
</tr>
<tr>
<td></td>
<td>z =</td>
<td>
<table class="centered">
<tbody>
<tr>
<td>
<table class="centered">
<tbody>
<tr>
<td colspan="2"></td>
<td colspan="2" align="center" valign="center">y</td>
</tr>
<tr>
<td colspan="2"></td>
<td align="center" valign="center">True</td>
<td align="center" valign="center">False</td>
</tr>
<tr>
<td rowspan="2" align="center" valign="center">x</td>
<td align="center" valign="center">True</td>
<td align="center" valign="center">a + 1</td>
<td align="center" valign="center">b + 1</td>
</tr>
<tr>
<td align="center" valign="center">False</td>
<td align="center" valign="center">(a + b) - 1</td>
<td align="center" valign="center">a + b</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
I want to be able to embed other things as well: bubble-and-arrow diagrams of finite state machines, before-and-after diagrams of data structures, and everything else that appears in programming textbooks. I can do this if I'm writing in Word or LibreOffice, or giving a lecture in front of a whiteboard. Why can't I do it when I'm programming?

The standard answer is, "Because programs are text." To which I can only reply, "No: that's a <em>storage format</em> for programs–a very limited (and limiting) one." I don't know how LibreOffice stores documents, or how SQLite stores a database, and I don't care. In fact, I <em>shouldn't</em> care unless something goes wrong (about which more later). In every domain except programming, programmers accept that there should be a division between:
<ol>
  <li>models (the things that make up whatever we're working with)</li>
  <li>views and controllers (how we display and interact with those things)</li>
  <li>storage formats (how we store things on disk)</li>
</ol>
The only place where we don't do this is when we're building things for ourselves. We insist that programs be stored as text streams because that's what Emacs, Vi, and the Unix command-line tools know how to work with, and what our compilers know how to process, but it doesn't have to be like that. We could store programs as XML documents, blobs of JSON, serialized Python data structures, whatever your favorite database uses, or something else entirely, then teach our controllers and views (i.e., our editors), and our processing tools (compilers and interpreters) to display that however we wanted and let us manipulate it in whatever way made the most sense for the content.

I thought at the time that doing this would require us to combine three specific technologies:
<ol>
  <li>Programming languages that allow programmers to extend their syntax.</li>
  <li>Compilers, linkers, debuggers, and other tools that are frameworks for plug-ins, rather than monolithic applications.</li>
  <li>Programs that are stored as XML documents, so programmers can represent and process data and meta-data uniformly.</li>
</ol>
Looking back seven years later:
<ol>
  <li>#1 was the goal of the exercise, so long as "extending syntax" is understood to mean "with entirely new displays with associated processing rules". Scheme's hygienic macros and Python's operator overloading are great, but they still require you to squeeze your thoughts into a single display form. You don't have to do that on a whiteboard, when authoring a textbook, or when writing a plugin for Firefox (though in each case, what you're building will be more comprehensible if it rhymes with things users already understand); why should you have to do it with programs?</li>
  <li>#2 is a corollary of #1: if I'm going to add X to my language, I need a way to tell tools how to handle X. The compiler or interpreter needs to know how to translate it into primitives; the optimizer might need special rules for making it fast; the debugger needs to know how to display its operation or internals, my coverage tool probably needs something as well, and so on. This is straightforward engineering: every new "thing" should be a bundle that respects various tools' APIs, and each tool should provide an API so that people can plug things into it.</li>
  <li>I was wrong about #3, partly because I still hadn't escaped the "storage format equals model" trap, and partly because I thought that XML processing tools like XSLT would catch on and become the basis for a new generation of pipe-and-filter tools to replace the venerable Unix toolset. What I'd say today is, "Programs are stored in some format that's amenable to low-level inspection by people who are developing new plugin forms, in the same way that SVG diagrams can be viewed as angle-bracketed text if absolutely necessary."</li>
</ol>
So, how has reality measured up? Well, as Bill Gates once said, "We always overestimate the change that will occur in the next two years and underestimate the change that will occur in the next ten." There has been renewed interest in programming language design in the last few years, mostly focused around the meme of functional languages being the only way to cope with massive parallelism (they aren't, but that's a different post). Unfortunately, all of these languages have remained trapped in the textual tarpit: whether it's Scala, Clojure, Haskell, or something more esoteric, their authors all take for granted that a program has to be a stream of characters that can be edited by Pico or Notepad. There are, however, a few signs of progress:
<ul>
  <li>Something–no one is quite sure what–is happening at Charles Simonyi's company Intentional Software. <a href="http://msdn.microsoft.com/en-us/data/dd727740.aspx">This talk</a> seems to show a working implementation of many of the ideas discussed above, focused on letting business people build things for themselves. That will fail unless someone teaches those business people the principles of <a href="http://blog.jonudell.net/2011/01/24/seven-ways-to-think-like-the-web/">computational</a> <a href="https://software-carpentry.org/4_0/softeng/principles/">thinking</a>, but the tool itself shows a lot of promise.</li>
  <li>Mathematica's <a href="http://www.wolfram.com/news/cdf-computable-document-format-released.html">Computable Document Format</a> doesn't provide the extensibility, but I still think it's worth watching. As I said in the original article, the biggest obstacle to getting from here to there is that everything has to change at once: editors, compilers, the language, etc. Vendors who own the whole toolchain, like Wolfram (Mathematica), The MathWorks (MATLAB), and Microsoft (.NET) can do this more easily than systems with distributed ownership (the C/Linux/Vi-or-Emacs/GCC toolchain). In that light, Microsoft's <a href="http://www.techworld.com.au/article/401071/microsoft_previews_compiler-as-a-service_software/">compiler-as-a-service</a> project is very interesting as well…</li>
  <li>Steve Witten's <a href="http://acko.net/blog/on-termkit">TermKit</a> is also interesting: he's replacing the plain text streams that classic Unix tools use to communicate with streams of JSON and a rich display. This grassroots, bottom-up approach is an interesting complement to the corporate, top-down approaches above.</li>
</ul>
But the project that has me really excited is Geoffrey French's <a href="https://sites.google.com/site/larchenv/">Larch</a>, which leverages Python and Jython to give people a forward migration path. The <a href="https://sites.google.com/site/larchenv/video-tutorials">tutorial videos</a> don't really do Larch justice, and you have to remember that it's really a proof of concept, but I'm still very excited. If nothing else, it could finally bring software visualization into the mainstream: as several studies have showed, visualizations are more useful and powerful if people create their own, but existing IDEs and languages make this hard. By making "draw this" a natural part of programming, Larch or something like it could be the next big step forward in programming.
