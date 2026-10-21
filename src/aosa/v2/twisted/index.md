---
title: "Twisted"
template: "page"
---

*by Jessica McKellar*

Twisted is an event-driven networking engine in Python. It was born in the early 2000s, when the writers of networked games had few scalable and no cross-platform libraries, in any language, at their disposal. The authors of Twisted tried to develop games in the existing networking landscape, struggled, saw a clear need for a scalable, event-driven, cross-platform networking framework and decided to make one happen, learning from the mistakes and hardships of past game and networked application writers.

Twisted supports many common transport and application layer protocols, including TCP, UDP, SSL/TLS, HTTP, IMAP, SSH, IRC, and FTP. Like the language in which it is written, it is "batteries-included"; Twisted comes with client and server implementations for all of its protocols, as well as utilities that make it easy to configure and deploy production-grade Twisted applications from the command line.

## Why Twisted?

In 2000, glyph, the creator of Twisted, was working on a text-based multiplayer game called Twisted Reality. It was a big mess of threads, 3 per connection, in Java. There was a thread for input that would block on reads, a thread for output that would block on some kind of write, and a "logic" thread that would sleep while waiting for timers to expire or events to queue. As players moved through the virtual landscape and interacted, threads were deadlocking, caches were getting corrupted, and the locking logic was never quite right---the use of threads had made the software complicated, buggy, and hard to scale.

Seeking alternatives, he discovered Python, and in particular Python's `select` module for multiplexing I/O from stream objects like sockets and pipes[^1]; at the time, Java didn't expose the operating system's `select` interface or any other asynchronous I/O API[^2]. A quick prototype of the game in Python using `select` immediately proved less complex and more reliable than the threaded version.

An instant convert to Python, `select`, and event-driven programming, glyph wrote a client and server for the game in Python using the `select` API. But then he wanted to do more. Fundamentally, he wanted to be able to turn network activity into method calls on objects in the game. What if you could receive email in the game, like the Nethack mailer daemon? What if every player in the game had a home page? Glyph found himself needing good Python IMAP and HTTP clients and servers that used `select`.

He first turned to Medusa, a platform developed in the mid-'90s for writing networking servers in Python based on the `asyncore` module[^3]. `asyncore` is an asynchronous socket handler that builds a dispatcher and callback interface on top of the operating system's `select` API.

This was an inspiring find for glyph, but Medusa had two drawbacks:

1.  It was on its way towards being unmaintained by 2001 when glyph started working on Twisted Reality.

2.  `asyncore` is such a thin wrapper around sockets that application programmers are still required to manipulate sockets directly. This means portability is still the responsibility of the programmer. Additionally, at the time, `asyncore`'s Windows support was buggy, and glyph knew that he wanted to run a GUI client on Windows.

Glyph was facing the prospect of implementing a networking platform himself and realized that Twisted Reality had opened the door to a problem that was just as interesting as his game.

Over time, Twisted Reality the game became Twisted the networking platform, which would do what existing networking platforms in Python didn't:

- Use event-driven programming instead of multi-threaded programming.

- Be cross-platform: provide a uniform interface to the event notification systems exposed by major operating systems.

- Be "batteries-included": provide implementations of popular application-layer protocols out of the box, so that Twisted is immediately useful to developers.

- Conform to RFCs, and prove conformance with a robust test suite.

- Make it easy to use multiple networking protocols together.

- Be extensible.

## The Architecture of Twisted

Twisted is an event-driven networking engine. Event-driven programming is so integral to Twisted's design philosophy that it is worth taking a moment to review what exactly event-driven programming means.

Event-driven programming is a programming paradigm in which program flow is determined by external events. It is characterized by an event loop and the use of callbacks to trigger actions when events happen. Two other common programming paradigms are (single-threaded) synchronous and multi-threaded programming.

![Figure 1: Threading models](threading_models.png)

Let's compare and contrast single-threaded, multi-threaded, and event-driven programming models with an example. Figure 1 shows the work done by a program over time under these three models. The program has three tasks to complete, each of which blocks while waiting for I/O to finish. Time spent blocking on I/O is greyed out.

In the single-threaded synchronous version of the program, tasks are performed serially. If one task blocks for a while on I/O, all of the other tasks have to wait until it finishes and they are executed in turn. This definite order and serial processing are easy to reason about, but the program is unnecessarily slow if the tasks don't depend on each other, yet still have to wait for each other.

In the threaded version of the program, the three tasks that block while doing work are performed in separate threads of control. These threads are managed by the operating system and may run concurrently on multiple processors or interleaved on a single processor. This allows progress to be made by some threads while others are blocking on resources. This is often more time-efficient than the analogous synchronous program, but one has to write code to protect shared resources that could be accessed concurrently from multiple threads. Multi-threaded programs can be harder to reason about because one now has to worry about thread safety via process serialization (locking), reentrancy, thread-local storage, or other mechanisms, which when implemented improperly can lead to subtle and painful bugs.

The event-driven version of the program interleaves the execution of the three tasks, but in a single thread of control. When performing I/O or other expensive operations, a callback is registered with an event loop, and then execution continues while the I/O completes. The callback describes how to handle an event once it has completed. The event loop polls for events and dispatches them as they arrive, to the callbacks that are waiting for them. This allows the program to make progress when it can without the use of additional threads. Event-driven programs can be easier to reason about than multi-threaded programs because the programmer doesn't have to worry about thread safety.

The event-driven model is often a good choice when there are:

1.  many tasks, that are...

2.  largely independent (so they don't have to communicate with or wait on each other), and...

3.  some of these tasks block while waiting on events.

It is also a good choice when an application has to share mutable data between tasks, because no synchronization has to be performed.

Networking applications often have exactly these properties, which is what makes them such a good fit for the event-driven programming model.

### Reusing Existing Applications

Many popular clients and servers for various networking protocols already existed when Twisted was created. Why did glyph not just use Apache, IRCd, BIND, OpenSSH, or any of the other pre-existing applications whose clients and servers would have to get re-implemented from scratch for Twisted?

The problem is that all of these server implementations have networking code written from scratch, typically in C, with application code coupled directly to the networking layer. This makes them very difficult to use as libraries. They have to be treated as black boxes when used together, giving a developer no chance to reuse code if he or she wanted to expose the same data over multiple protocols. Additionally, the server and client implementations are often separate applications that don't share code. Extending these applications and maintaining cross-platform client-server compatibility is harder than it needs to be.

With Twisted, the clients and servers are written in Python using a consistent interface. This makes it is easy to write new clients and servers, to share code between clients and servers, to share application logic between protocols, and to test one's code.

### The Reactor

Twisted implements the *reactor* design pattern, which describes demultiplexing and dispatching events from multiple sources to their handlers in a single-threaded environment.

The core of Twisted is the reactor event loop. The reactor knows about network, file system, and timer events. It waits on and then handles these events, abstracting away platform-specific behavior and presenting interfaces to make responding to events anywhere in the network stack easy.

The reactor essentially accomplishes:

    while True:
        timeout = time_until_next_timed_event()
        events = wait_for_events(timeout)
        events += timed_events_until(now())
        for event in events:
            event.process()

A reactor based on the `poll` API[^4] is the current default on all platforms. Twisted additionally supports a number of platform-specific high-volume multiplexing APIs. Platform-specific reactors include the KQueue reactor based on FreeBSD's `kqueue` mechanism, an `epoll`-based reactor for systems supporting the `epoll` interface (currently Linux 2.6), and an IOCP reactor based on Windows Input/Output Completion Ports.

Examples of polling implementation-dependent details that Twisted takes care of include:

- Network and filesystem limits.

- Buffering behavior.

- How to detect a dropped connection.

- The values returned in error cases.

Twisted's reactor implementation also takes care of using the underlying non-blocking APIs correctly and handling obscure edge cases correctly. Python doesn't expose the IOCP API at all, so Twisted maintains its own implementation.

### Managing Callback Chains

Callbacks are a fundamental part of event-driven programming and are the way that the reactor indicates to an application that events have completed. As event-driven programs grow, handling both the success and error cases for the events in one's application becomes increasingly complex. Failing to register an appropriate callback can leave a program blocking on event processing that will never happen, and errors might have to propagate up a chain of callbacks from the networking stack through the layers of an application.

Let's examine some of the pitfalls of event-driven programs by comparing synchronous and asynchronous versions of a toy URL fetching utility in Python-like pseudo-code:


<p>Synchronous URL fetcher:</p>
<pre><code>import getPage


def processPage(page):
    print page

def logError(error):
    print error

def finishProcessing(value):
    print &quot;Shutting down...&quot;
    exit(0)

url = &quot;http://google.com&quot;
try:
    page = getPage(url)
    processPage(page)
except Error, e:
    logError(error)
finally:
    finishProcessing()</code></pre>
<p>Asynchronous URL fetcher:</p>
<pre><code>from twisted.internet import reactor
import getPage

def processPage(page):
    print page
    finishProcessing()

def logError(error):
    print error
    finishProcessing()

def finishProcessing(value):
    print &quot;Shutting down...&quot;
    reactor.stop()

url = &quot;http://google.com&quot;
# getPage takes: url, 
#    success callback, error callback
getPage(url, processPage, logError)

reactor.run()</code></pre>


In the asynchronous URL fetcher, `reactor.run()` starts the reactor event loop. In both the synchronous and asynchronous versions, a hypothetical `getPage` function does the work of page retrieval. `processPage` is invoked if the retrieval is successful, and `logError` is invoked if an `Exception` is raised while attempting to retrieve the page. In either case, `finishProcessing` is called afterwards.

The callback to `logError` in the asynchronous version mirrors the `except` part of the `try/except` block in the synchronous version. The callback to `processPage` mirrors `else`, and the unconditional callback to `finishProcessing` mirrors `finally`.

In the synchronous version, by virtue of the structure of a `try/except` block exactly one of `logError` and `processPage` is called, and `finishProcessing` is always called once; in the asynchronous version it is the programmer's responsibility to invoke the correct chain of success and error callbacks. If, through programming error, the call to `finishProcessing` were left out of `processPage` or `logError` along their respective callback chains, the reactor would never get stopped and the program would run forever.

This toy example hints at the complexity frustrating programmers during the first few years of Twisted's development. Twisted responded to this complexity by growing an object called a `Deferred`.

#### Deferreds {#deferreds .unnumbered}

The `Deferred` object is an abstraction of the idea of a result that doesn't exist yet. It also helps manage the callback chains for this result. When returned by a function, a `Deferred` is a promise that the function will have a result *at some point*. That single returned `Deferred` contains references to all of the callbacks registered for an event, so only this one object needs to be passed between functions, which is much simpler to keep track of than managing callbacks individually.

`Deferred`s have a pair of callback chains, one for success (callbacks) and one for errors (errbacks). `Deferred`s start out with two empty chains. One adds pairs of callbacks and errbacks to handle successes and failures at each point in the event processing. When an asynchronous result arrives, the `Deferred` is "fired" and the appropriate callbacks or errbacks are invoked in the order in which they were added.

Here is a version of the asynchronous URL fetcher pseudo-code which uses `Deferred`s:

    from twisted.internet import reactor
    import getPage

    def processPage(page):
        print page

    def logError(error):
        print error

    def finishProcessing(value):
        print "Shutting down..."
        reactor.stop()

    url = "http://google.com"
    deferred = getPage(url) # getPage returns a Deferred
    deferred.addCallbacks(processPage, logError)
    deferred.addBoth(finishProcessing)

    reactor.run()

In this version, the same event handlers are invoked, but they are all registered with a single `Deferred` object instead of spread out in the code and passed as arguments to `getPage`.

The `Deferred` is created with two stages of callbacks. First, `addCallbacks` adds the `processPage` callback and `logError` errback to the first stage of their respective chains. Then `addBoth` adds `finishProcessing` to the second stage of both chains. Diagrammatically, the callback chains look like Figure 2.

![Figure 2: Callback chains](deferred.png)

`Deferred`s can only be fired once; attempting to re-fire them will raise an `Exception`. This gives `Deferred`s semantics closer to those of the `try/except` blocks of their synchronous cousins, which makes processing the asynchronous events easier to reason about and avoids subtle bugs caused by callbacks being invoked more or less than once for a single event.

Understanding `Deferred`s is an important part of understanding the flow of Twisted programs. However, when using the high-level abstractions Twisted provides for networking protocols, one often doesn't have to use `Deferred`s directly at all.

The `Deferred` abstraction is powerful and has been borrowed by many other event-driven platforms, including jQuery, Dojo, and Mochikit.

### Transports

Transports represent the connection between two endpoints communicating over a network. Transports are responsible for describing connection details, like being stream- or datagram-oriented, flow control, and reliability. TCP, UDP, and Unix sockets are examples of transports. They are designed to be "minimally functional units that are maximally reusable" and are decoupled from protocol implementations, allowing for many protocols to utilize the same type of transport. Transports implement the `ITransport` interface, which has the following methods:

  ------------------ -------------------------------------------------------------------------------------
  `write`            Write some data to the physical connection, in sequence, in a non-blocking fashion.
  `writeSequence`    Write a list of strings to the physical connection.
  `loseConnection`   Write all pending data and then close the connection.
  `getPeer`          Get the remote address of this connection.
  `getHost`          Get the address of this side of the connection.
  ------------------ -------------------------------------------------------------------------------------

Decoupling transports from procotols also makes testing the two layers easier. A mock transport can simply write data to a string for inspection.

### Protocols

Procotols describe how to process network events asynchronously. HTTP, DNS, and IMAP are examples of application protocols. Protocols implement the `IProtocol` interface, which has the following methods:

  ------------------ ------------------------------------------------
  `makeConnection`   Make a connection to a transport and a server.
  `connectionMade`   Called when a connection is made.
  `dataReceived`     Called whenever data is received.
  `connectionLost`   Called when the connection is shut down.
  ------------------ ------------------------------------------------

The relationship between the reactor, protocols, and transports is best illustrated with an example. Here are complete implementations of an echo server and client, first the server:

    from twisted.internet import protocol, reactor

    class Echo(protocol.Protocol):
        def dataReceived(self, data):
            # As soon as any data is received, write it back
            self.transport.write(data)

    class EchoFactory(protocol.Factory):
        def buildProtocol(self, addr):
            return Echo()

    reactor.listenTCP(8000, EchoFactory())
    reactor.run()

And the client:

    from twisted.internet import reactor, protocol

    class EchoClient(protocol.Protocol):
       def connectionMade(self):
           self.transport.write("hello, world!")

       def dataReceived(self, data):
           print "Server said:", data
           self.transport.loseConnection()

       def connectionLost(self, reason):
           print "connection lost"

    class EchoFactory(protocol.ClientFactory):
       def buildProtocol(self, addr):
           return EchoClient()

       def clientConnectionFailed(self, connector, reason):
           print "Connection failed - goodbye!"
           reactor.stop()

       def clientConnectionLost(self, connector, reason):
           print "Connection lost - goodbye!"
           reactor.stop()

    reactor.connectTCP("localhost", 8000, EchoFactory())
    reactor.run()

Running the server script starts a TCP server listening for connections on port 8000. The server uses the `Echo` protocol, and data is written out over a TCP transport. Running the client makes a TCP connection to the server, echoes the server response, and then terminates the connection and stops the reactor. Factories are used to produce instances of protocols for both sides of the connection. The communication is asynchronous on both sides; `connectTCP` takes care of registering callbacks with the reactor to get notified when data is available to read from a socket.

### Applications

Twisted is an engine for producing scalable, cross-platform network servers and clients. Making it easy to deploy these applications in a standardized fashion in production environments is an important part of a platform like this getting wide-scale adoption.

To that end, Twisted developed the Twisted application infrastructure, a re-usable and configurable way to deploy a Twisted application. It allows a programmer to avoid boilerplate code by hooking an application into existing tools for customizing the way it is run, including daemonization, logging, using a custom reactor, profiling code, and more.

The application infrastructure has four main parts: Services, Applications, configuration management (via TAC files and plugins), and the `twistd` command-line utility. To illustrate this infrastructure, we'll turn the echo server from the previous section into an Application.

#### Service {#service .unnumbered}

A Service is anything that can be started and stopped and which adheres to the `IService` interface. Twisted comes with service implementations for TCP, FTP, HTTP, SSH, DNS, and many other protocols. Many Services can register with a single application.

The core of the `IService` interface is:

  ---------------- --------------------------------------------------------------------------------------------------------------------------------
  `startService`   Start the service. This might include loading configuration data, setting up database connections, or listening on a port.
  `stopService`    Shut down the service. This might include saving state to disk, closing database connections, or stopping listening on a port.
  ---------------- --------------------------------------------------------------------------------------------------------------------------------

Our echo service uses TCP, so we can use Twisted's default `TCPServer` implementation of this `IService` interface.

#### Application {#application .unnumbered}

An Application is the top-level service that represents the entire Twisted application. Services register themselves with an Application, and the `twistd` deployment utility described below searches for and runs Applications.

We'll create an echo Application with which the echo Service can register.

#### TAC Files {#tac-files .unnumbered}

When managing Twisted applications in a regular Python file, the developer is responsible for writing code to start and stop the reactor and to configure the application. Under the Twisted application infrastructure, protocol implementations live in a module, Services using those protocols are registered in a Twisted Application Configuration (TAC) file, and the reactor and configuration are managed by an external utility.

To turn our echo server into an echo application, we can follow a simple algorithm:

1.  Move the Protocol parts of the echo server into their own module.

2.  Inside a TAC file:

    1.  Create an echo Application.

    2.  Create an instance of the `TCPServer` Service which will use our `EchoFactory`, and register it with the Application.

The code for managing the reactor will be taken care of by `twistd`, discussed below. The application code ends up looking like this:

The `echo.py` file:

    from twisted.internet import protocol, reactor

    class Echo(protocol.Protocol):
        def dataReceived(self, data):
            self.transport.write(data)

    class EchoFactory(protocol.Factory):
        def buildProtocol(self, addr):
            return Echo()

The `echo_server.tac` file:

    from twisted.application import internet, service
    from echo import EchoFactory

    application = service.Application("echo")
    echoService = internet.TCPServer(8000, EchoFactory())
    echoService.setServiceParent(application)

#### twistd {#twistd .unnumbered}

`twistd` (pronounced "twist-dee") is a cross-platform utility for deploying Twisted applications. It runs TAC files and handles starting and stopping an application. As part of Twisted's batteries-included approach to network programming, `twistd` comes with a number of useful configuration flags, including daemonizing the application, the location of log files, dropping privileges, running in a chroot, running under a non-default reactor, or even running the application under a profiler.

We can run our echo server Application with:

    $ twistd -y echo_server.tac

In this simplest case, `twistd` starts a daemonized instance of the application, logging to `twistd.log`. After starting and stopping the application, the log looks like this:

    2011-11-19 22:23:07-0500 [-] Log opened.
    2011-11-19 22:23:07-0500 [-] twistd 11.0.0 (/usr/bin/python 2.7.1) starting up.
    2011-11-19 22:23:07-0500 [-] reactor class: twisted.internet.selectreactor.SelectReactor.
    2011-11-19 22:23:07-0500 [-] echo.EchoFactory starting on 8000
    2011-11-19 22:23:07-0500 [-] Starting factory <echo.EchoFactory instance at 0x12d8670>
    2011-11-19 22:23:20-0500 [-] Received SIGTERM, shutting down.
    2011-11-19 22:23:20-0500 [-] (TCP Port 8000 Closed)
    2011-11-19 22:23:20-0500 [-] Stopping factory <echo.EchoFactory instance at 0x12d8670>
    2011-11-19 22:23:20-0500 [-] Main loop terminated.
    2011-11-19 22:23:20-0500 [-] Server Shut Down.

Running a service using the Twisted application infrastructure allows developers to skip writing boilerplate code for common service functionalities like logging and daemonization. It also establishes a standard command line interface for deploying applications.

#### Plugins {#plugins .unnumbered}

An alternative to the TAC-based system for running Twisted applications is the plugin system. While the TAC system makes it easy to register simple hierarchies of pre-defined services within an application configuration file, the plugin system makes it easy to register custom services as subcommands of the `twistd` utility, and to extend the command-line interface to an application.

Using this system:

1.  Only the plugin API is required to remain stable, which makes it easy for third-party developers to extend the software.

2.  Plugin discoverability is codified. Plugins can be loaded and saved when a program is first run, re-discovered each time the program starts up, or polled for repeatedly at runtime, allowing the discovery of new plugins installed after the program has started.

To extend a program using the Twisted plugin system, all one has to do is create objects which implement the `IPlugin` interface and put them in a particular location where the plugin system knows to look for them.

Having already converted our echo server to a Twisted application, transformation into a Twisted plugin is straightforward. Alongside the `echo` module from before, which contains the `Echo` protocol and `EchoFactory` definitions, we add a directory called `twisted`, containing a subdirectory called `plugins`, containing our echo plugin definition. This plugin will allow us to start an echo server and specify the port to use as arguments to the `twistd` utility:

    from zope.interface import implements

    from twisted.python import usage
    from twisted.plugin import IPlugin
    from twisted.application.service import IServiceMaker
    from twisted.application import internet

    from echo import EchoFactory

    class Options(usage.Options):
        optParameters = [["port", "p", 8000, "The port number to listen on."]]

    class EchoServiceMaker(object):
        implements(IServiceMaker, IPlugin)
        tapname = "echo"
        description = "A TCP-based echo server."
        options = Options

        def makeService(self, options):
            """
            Construct a TCPServer from a factory defined in myproject.
            """
            return internet.TCPServer(int(options["port"]), EchoFactory())

    serviceMaker = EchoServiceMaker()

Our echo server will now show up as a server option in the output of `twistd --help`, and running `twistd echo --port=1235` will start an echo server on port 1235.

Twisted comes with a pluggable authentication system for servers called `twisted.cred`, and a common use of the plugin system is to add an authentication pattern to an application. One can use `twisted.cred AuthOptionMixin` to add command-line support for various kinds of authentication off the shelf, or to add a new kind. For example, one could add authentication via a local Unix password database or an LDAP server using the plugin system.

`twistd` comes with plugins for many of Twisted's supported protocols, which turns the work of spinning up a server into a single command. Here are some examples of `twistd` servers that ship with Twisted:

::: description
`twistd web --port 8080 --path .`\
Run an HTTP server on port 8080, serving both static and dynamic content out of the current working directory.

`twistd dns -p 5553 --hosts-file=hosts`\
Run a DNS server on port 5553, resolving domains out of a file called `hosts` in the format of `/etc/hosts`.

`sudo twistd conch -p tcp:2222`\
Run an ssh server on port 2222. ssh keys must be set up independently.

`twistd mail -E -H localhost -d localhost=emails`\
Run an ESMTP POP3 server, accepting email for localhost and saving it to the `emails` directory.
:::

`twistd` makes it easy to spin up a server for testing clients, but it is also pluggable, production-grade code.

In that respect, Twisted's application deployment mechanisms via TAC files, plugins, and `twistd` have been a success. However, anecdotally, most large Twisted deployments end up having to rewrite some of these management and monitoring facilities; the architecture does not quite expose what system administrators need. This is a reflection of the fact that Twisted has not historically had much architectural input from system administrators---the people who are experts at deploying and maintaining applications.

Twisted would be well-served to more aggressively solicit feedback from expert end users when making future architectural decisions in this space.

## Retrospective and Lessons Learned

Twisted recently celebrated its 10th anniversary. Since its inception, inspired by the networked game landscape of the early 2000s, it has largely achieved its goal of being an extensible, cross-platform, event-driven networking engine. Twisted is used in production environments at companies from Google and Lucasfilm to Justin.TV and the Launchpad software collaboration platform. Server implementations in Twisted are the core of numerous other open source applications, including BuildBot, BitTorrent, and Tahoe-LAFS.

Twisted has had few major architectural changes since its initial development. The one crucial addition was `Deferred`, as discussed above, for managing pending results and their callback chains.

There was one important removal, which has almost no footprint in the current implementation: Twisted Application Persistence.

### Twisted Application Persistence

Twisted Application Persistence (TAP) was a way of keeping an application's configuration and state in a pickle. Running an application using this scheme was a two-step process:

1.  Create the pickle that represents an Application, using the now defunct `mktap` utility.

2.  Use `twistd` to unpickle and run the Application.

This process was inspired by Smalltalk images, an aversion to the proliferation of seemingly ad hoc configuration languages that were hard to script, and a desire to express configuration details in Python.

TAP files immediately introduced unwanted complexity. Classes would change in Twisted without instances of those classes getting changed in the pickle. Trying to use class methods or attributes from a newer version of Twisted on the pickled object would crash the application. The notion of "upgraders" that would upgrade pickles to new API versions was introduced, but then a matrix of upgraders, pickle versions, and unit tests had to be maintained to cover all possible upgrade paths, and comprehensively accounting for all interface changes was still hard and error-prone.

TAPs and their associated utilities were abandoned and then eventually removed from Twisted and replaced with TAC files and plugins. TAP was backronymed to Twisted Application Plugin, and few traces of the failed pickling system exist in Twisted today.

The lesson learned from the TAP fiasco was that to have reasonable maintainability, persistent data needs an explicit schema. More generally, it was a lesson about adding complexity to a project: when considering introducing a novel system for solving a problem, make sure the complexity of that solution is well understood and tested and that the benefits are clearly worth the added complexity before committing the project to it.

### web2: a lesson on rewrites

While not primarily an architectural decision, a project management decision about rewriting the Twisted Web implementation has had long-term ramifications for Twisted's image and the maintainers' ability to make architectural improvements to other parts of the code base, and it deserves a short discussion.

In the mid-2000s, the Twisted developers decided to do a full rewrite of the `twisted.web` APIs as a separate project in the Twisted code base called `web2`. `web2` would contain numerous improvements over `twisted.web`, including full HTTP 1.1 support and a streaming data API.

`web2` was labelled as experimental, but ended up getting used by major projects anyway and was even accidentally released and packaged by Debian. Development on `web` and `web2` continued concurrently for years, and new users were perennially frustrated by the side-by-side existence of both projects and a lack of clear messaging about which project to use. The switchover to `web2` never happened, and in 2011 `web2` was finally removed from the code base and the website. Some of the improvements from `web2` are slowly getting ported back to `web`.

Partially because of `web2`, Twisted developed a reputation for being hard to navigate and structurally confusing to newcomers. Years later, the Twisted community still works hard to combat this image.

The lesson learned from `web2` was that rewriting a project from scratch is often a bad idea, but if it has to happen make sure that the developer community understands the long-term plan, and that the user community has one clear choice of implementation to use during the rewrite.

If Twisted could go back and do `web2` again, the developers would have done a series of backwards-compatible changes and deprecations to `twisted.web` instead of a rewrite.

### Keeping Up with the Internet

The way that we use the Internet continues to evolve. The decision to implement many protocols as part of the core software burdens Twisted with maintaining code for all of those protocols. Implementations have to evolve with changing standards and the adoption of new protocols while maintaining a strict backwards-compatibility policy.

Twisted is primarily a volunteer-driven project, and the limiting factor for development is not community enthusiasm, but rather volunteer time. For example, RFC 2616 defining HTTP 1.1 was released in 1999, work began on adding HTTP 1.1 support to Twisted's HTTP protocol implementations in 2005, and the work was completed in 2009. Support for IPv6, defined in RFC 2460 in 1998, is in progress but unmerged as of 2011.

Implementations also have to evolve as the interfaces exposed by supported operating systems change. For example, the `epoll` event notification facility was added to Linux 2.5.44 in 2002, and Twisted grew an `epoll`-based reactor to take advantage of this new API. In 2007, Apple released OS 10.5 Leopard with a `poll` implementation that didn't support devices, which was buggy enough behavior for Apple to not expose `select.poll` in its build of Python[^5]. Twisted has had to work around this issue and document it for users ever since.

Sometimes, Twisted development doesn't keep up with the changing networking landscape, and enhancements are moved to libraries outside of the core software. For example, the Wokkel project[^6], a collection of enhancements to Twisted's Jabber/XMPP support, has lived as a to-be-merged independent project for years without a champion to oversee the merge. An attempt was made to add WebSockets to Twisted as browsers began to adopt support for the new protocol in 2009, but development moved to external projects after a decision not to include the protocol until it moved from an IETF draft to a standard.

All of this being said, the proliferation of libraries and add-ons is a testament to Twisted's flexibility and extensibility. A strict test-driven development policy and accompanying documentation and coding standards help the project avoid regressions and preserve backwards compatibility while maintaining a large matrix of supported protocols and platforms. It is a mature, stable project that continues to have very active development and adoption.

Twisted looks forward to being the engine of your Internet for another ten years.

[^1]: The Single UNIX Specification, Version 3 (SUSv3) describes the `select` API.

[^2]: The `java.nio` package for non-blocking I/O was added in J2SE 1.4, released in 2002.

[^3]: <http://www.nightmare.com/medusa/>

[^4]: The Single UNIX Specification, Version 3 (SUSv3) describes the `poll` API.

[^5]: <http://twistedmatrix.com/trac/ticket/4173>

[^6]: <http://wokkel.ik.nu/>
