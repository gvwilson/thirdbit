---
title: "Old Dogs Are Suspicious of New Tricks"
date: 2008-03-30
---
There was a brief flurry of email on the DrProject list this week about using <a href="http://www.json.org/">JSON</a> instead of XML for communication between clients (in our case, browsers and the occasional client-side script) and servers.  The younger members of the team were excited about the advantages: less typing, easier to read, faster to convert to/from data structures, and shiny newness.  I said "no" because of the disadvantages: every implementation works slightly differently (XML may be broken, but at least it's broken the same way everywhere), and it introduces a serious security risk [1]—I might not be able to think of a way to exploit it if all connections are HTTPS, but I'm just one guy, and I'd rather not require DrP's users to bet that I'm smarter than all the villains in the world.

The whole discussion was an interesting reminder of how my priorities have shifted over the last ten years. I would have been on the juniors' side in the mid-1990s; hell, back then, I still toyed with the idea of teaching people Scheme as a first language.  I guess part of growing old as a technologist is caring more about not stepping on traps than about missed opportunities…

[1] There are two ways to process JSON: use eval(), or parse it. If you're using eval(), you are taking the risk that someone has embedded function calls in the "data" they're sending you, in which case you just handed them the keys.  If you're parsing, then what's the advantage over XML, for which there are many well-tested out-of-the-box parsers?
