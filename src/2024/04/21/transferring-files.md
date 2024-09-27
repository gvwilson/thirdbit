---
title: "Software Design by Example in Python 21: Transferring Files"
date: 2024-04-21
---

[A week ago][layout_post] I wrote that
learning how to write a web browser
will teach you more about modern computer systems
than learning how to write a compiler.
One reason for that is that almost modern application relies on networks,
so understanding how they work is at least as important as
understanding register allocation.

[Chapter 21: Transferring Files][sdxpy_ftp] therefore has three parts:

1.  How to transfer a file using TCP/IP.
2.  How to break large transfers into chunks.
3.  How to write unit tests when multiple processes are involved.

Of these,
I think the third is the hardest and therefore the most important.
My approach in this chapter is to stub out the client when testing the server and vice versa;
it reduces the fidelity of the tests,
but it's one of the few times I haven't felt uncomfortable using multiple inheritance.

<img class="centered" src="@root/sdxpy/ftp/concept_map.svg" alt="Concept map for transferring files"/>

> Terms defined: client, deadlock, Domain Name System, Internet Protocol, IP address, port, server, socket, test fidelity, Transmission Control Protocol.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="@root/sdxpy/sdxpy-cover.png" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[layout_post]: @root/2024/04/14/page-layout/
[sdxpy_ftp]: @root/sdxpy/ftp/
