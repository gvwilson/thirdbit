---
title: "What Else for the Sudonomicon?"
date: 2026-11-05
category: software-carpentry software-engineering
---
I started work last year on [an introduction to systems programming for data scientists][sudonomicon].
I assumed learners were comfortable with the material covered in the Carpentries workshops
on the Unix shell and Python:

-   Unix shell:
    -   `pwd`; `ls`; `cd`; `.` and `..`; `rm` and `rmdir`; `mkdir`; `touch`;
        `mv`; `cp`; `tree`; `cat`; `wc`; `head`; `tail`; `less`; `cut`; `echo`;
        `history`; `find`; `grep`; `zip`; `man`
    -   Current working directory; absolute and relative paths; naming files
    -   Standard input; standard output; standard error; redirection; pipes
    -   `*` and `?` wildcards; shell variable with `$` expansion; `for` loop
-   Python for command-line scripting
    -   Variables; numbers and strings; lists; dictionaries; `for` and `while` loops;
        `if`/`else`; `with`; defining and calling functions; `sys.argv`, `sys.stdin`,
        and `sys.stdout`; simple regular expressions.
    -   Create a virtual environment; activate it and install packages.

The topics I outlined then were:

-   filesystems (e.g., what's a symbolic link?)
-   processes and job control
-   the basics of the HTTP protocol
-   accounts, permissions, and SSH
-   shell variables
-   virtual environments (in the Python `.venv` sense)
-   the basics of networking (IP addresses, DNS lookup)
-   virtualization with Docker

Before I start fleshing out the existing material, I'd like to figure out what else ought to be included.
Possibilities include:

-   creating and managing certificates (which is still a lot harder than it should be)
-   concurrency and parallelism (threads versus processes, how to do this in Python)
-   observability and logging
-   resource management with tools like `top`, `ulimit`, and `nice`
-   serialization and binary file formats
-   web APIs and REST
-   compression, archives, and hashes
-   more SSH and remote access (e.g., port forwarding and tunnels)
-   firewalls and NAT
-   profiling (and why benchmarking is hard)
-   web security vulnerabilities (e.g., SQL injection, cross-site scripting, and cross-site request forgery)

I would be very grateful for guidance:
what do *you* think a (data) scientist who's starting to manage their own system needs to know?

[sudonomicon]: https://github.com/gvwilson/sudonomicon
