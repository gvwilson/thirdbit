---
date: 2024-02-17
year: 2024
title: "Concurrent Examples"
---

I would like to write a short tutorial on web programming for data scientists.
I want to be able to re-run the examples and capture their output automatically,
but concurrency makes this much harder than it is for something like [this SQL tutorial][sql-tutorial].
I need to be able to:

1.  launch two or more processes (clients and servers);
2.  make sure clients don't try running before their servers are ready to accept requests;
    and
3.  capture the messages printed by these processes in the order in which they appear
    (rather than all of one process's output followed by all of another's).

[Robert Kern][kern-robert] kindly provided a predecessor for this script:

```sh
#!/usr/bin/env bash

# Save the process group ID of this script.
pgid=`ps -o pgid= $$`

# Trap a Ctrl-C SIGINT and kill everything running inside this script.
trap "pkill -KILL -g $pgid" INT

# 1. Redirect server stderr to stdout.
# 2. Prefix each line with 'server'.
# 3. Background the process.
($1 2>&1 | while read server; do echo 'S: ' ${server}; done) &

# Wait.
sleep 1

# 1. Redirect client stderr to stdout.
# 2. Prefix each line with 'client'.
$2 2>&1 | while read client; do echo 'c: ' ${client}; done

# Kill this script and its children (client and server) when client finishes.
pkill -KILL -g $pgid
```

When run like this:

```sh
run2.sh "python -m http.server -d site" "python simple_request.py" > output.txt
```

it launches a simple HTTP server,
sleeps for one second,
and then runs the client program `simple_request.py`.
The output from the server uses `S` as a prefix
while the output from the client uses `c`.

This script works,
but only sort of:

1.  The one-second delay before launching the client isn't always enough.
2.  When I'm using Python's `socket`, `socketserver`, and `ssl` modules,
    processes don't always relinquish sockets cleanly upon exit
    (particularly if there's a deliberate bug in the code to illustrate errors and error handling),
    which means I can't re-run the job for several seconds.

Is there a better way?
I feel like there must be—I'm hardly the first person to wrestle with these issues—but
it has been decades (literally) since I programmed at this level.
Using Python's `logging` module to capture output from multiple processes
might be more robust than the `while` loops in the script shown above,
but how do I manage startup and shutdown in examples that include three or four processes,
some of which might deliberately fail?
If you have a solution you can share,
please [reach out](mailto:{{site.author.email}}).

[kern-robert]: https://www.enthought.com/team/robert-kern/
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
