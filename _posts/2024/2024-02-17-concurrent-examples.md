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

Later,
[Jean-Marc Saffroy][saffroy-jean-marc] provided this script,
which uses `lsof` to wait until servers start listening on ports
before launching clients:

```sh
#!/usr/bin/env bash

# First argument is a set of TCP ports.
# This is followed by one command per server listening to those ports
# and then by client commands, e.g.
# e.g: ./runner.sh "8081 8082" "servercmd 8081" "servercmd 8082" "client1" "client2" ...

PORTS="$1"
shift

CHILDREN=

# Wait for a port to be available.
await_port_free() {
    PORTNUM=$1
    while lsof -n -iTCP:${PORTNUM} ; do
        sleep 0.5
        # printf "*"
    done
    # printf "\nport $PORTNUM free\n"
}

# Wait for a port to be in the listening state.
await_port_listen() {
    PORTNUM=$1
    while ! lsof -n -iTCP:${PORTNUM}|grep -qw LISTEN ; do
        sleep 0.5
        # printf "*"
    done
    # printf "\nport $PORTNUM in LISTEN state\n"
}

# Kill all child processes (suppressing messages so as not to clutter output).
on_exit(){
    # disable trap
    trap - exit int
    # gently kill every child
    kill -INT $CHILDREN &>/dev/null
    sleep 1
    # thorough cleanup
    pkill -TERM -g 0
}

# exiting or ^C runs on_exit
trap on_exit exit int

# Launch the servers as their ports become available, and wait until each one
# has started listening before starting the next one.
for PORT in $PORTS; do
    await_port_free $PORT

    CMD="$1"
    shift
    $CMD &
    CHILDREN="$CHILDREN $!"

    await_port_listen $PORT
done

# Launch all of the clients.
for CMD in "$@"; do
    $CMD &
    CHILDREN="$CHILDREN $!"
done

# Wait until any child process exits
while true; do
    for CHILD in $CHILDREN; do
        if ! kill -0 $CHILD &>/dev/null; then
            exit # to on_exit
        fi
    done
    sleep 0.5
done
```

Is there a better way?
I feel like there must be—I'm hardly the first person to wrestle with these issues—but
it has been decades (literally) since I programmed at this level.
One possibility is to borrow some code from [VCR.py][vcrpy]
and run everything in a single process
after replacing the underlying socket library with something that captures and forwards messages.
That would have the advantage of being reproducible—I'm going to use this
to re-run examples for a tutorial,
and while I don't care what the order of messages is,
I do care that it's the same each time—but this kind of mocking will only work if everything is in Python.
If you have another solution you can share,
please [reach out](mailto:{{site.author.email}}).

[kern-robert]: https://www.enthought.com/team/robert-kern/
[saffroy-jean-marc]: https://github.com/saffroy
[sql-tutorial]: https://gvwilson.github.io/sql-tutorial/
[vcrpy]: https://vcrpy.readthedocs.io/
