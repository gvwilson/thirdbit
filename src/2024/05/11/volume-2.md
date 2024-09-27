---
title: "Volume Two"
date: 2024-05-11
---

I don't think there will ever be a second volume of [*Software Design by Example in Python*][sdxpy],
but if there is,
I'd like it to include the examples listed below.
What I'd like even more is if a handful of software engineering professors
used some chapters from the existing book in their course,
then assigned one of these topics to their students as a final project
and share the results with me.
I'd be very happy to combine and edit the results,
and I think that having a chapter with their name on it in a published book
would be a pretty cool achievement for an undergrad.

1.  A *file compressor*
    because compression algorithms are both important and cool.

1.  A *fuzz tester*.
    If you haven't read [*The Fuzzing Book*][fuzzing-book] yet, you really should.

1.  A *discrete event simulator* like [SimPy][simpy] (but much simpler),
    mostly to show how co-operative multi-tasking works.

1.  An *object-relational mapper* that targets a very simple subset of SQL
    (but which does show how to implement foreign key relationships).

1.  *Dynamic autocompletion*.
    Showing possible continuations of what's been typed so far is straightforward;
    showing how to update the tree of possibilities as new things are typed is a lot more fun.

1.  A simple *search engine*.
    I'd like something more sophisticated than [TF-IDF][tf-idf],
    but I don't know what that would be.

1.  A *continuous integration system* that runs jobs and reports results on each commit to version control.
    Its real purpose would be to show people how to manage processes,
    e.g.,
    how to interrupt a job if another commit occurs before the job completes
    and how to limit the time each job is allowed.

1.  An *issue tracker* with authentication and workflow management.
    (The issues are just there to motivate authentication and workflow as objects.)

1.  Speaking of authentication, [OAuth][oauth].

1.  A *message queue* like [Celery][celery] or [ZeroMQ][zeromq].

1.  A *fault-tolerant virtual machine* like [BEAM][beam].
    (The existing book has a simple VM; perhaps this could extend it?)

1.  *[TCP][tcp]*,
    because the lack of networking in the [current book][sdxpy] is its biggest weakness.

1.  *[DNS][dns]*,
    for the same reason
    (though I doubt I could make anything as fun as [Julia Evans][evans-julia]'s [Mess With DNS][mess-with-dns]).

1.  A scale model of *[Docker Compose][docker-compose] or [Kubernetes][kubernetes]*,
    which wouldn't have to be much more complicated than
    [this tool for running concurrent examples][concurrent].

1.  A *[VPN][vpn]*.
    (Remember, these are scale models with only a fraction of the functionality of the real thing.)

[beam]: https://en.wikipedia.org/wiki/BEAM_(Erlang_virtual_machine)
[celery]: https://docs.celeryq.dev/
[concurrent]: @root/2024/02/17/concurrent-examples/
[dns]: https://en.wikipedia.org/wiki/Domain_Name_System
[docker-compose]: https://docs.docker.com/compose/
[evans-julia]: https://jvns.ca/
[fuzzing-book]: https://www.fuzzingbook.org/
[kubernetes]: https://kubernetes.io/
[mess-with-dns]: https://messwithdns.net/
[oauth]: https://en.wikipedia.org/wiki/OAuth
[sdxpy]: @root/sdxpy/
[simpy]: https://simpy.readthedocs.io/
[tcp]: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
[tf-idf]: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
[vpn]: https://en.wikipedia.org/wiki/Virtual_private_network
[zeromq]: https://zeromq.org/
