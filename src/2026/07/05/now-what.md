---
title: "Now What? A Workshop on Error Handling"
date: 2026-07-05
category: education proposal software-engineering
---
I finally have time to flesh out ideas for lessons that I've wanted for years.
However,
if I can't find a way to send them back to 2006,
there's no point writing them:
very few people read long-form tutorials about software these days.
I'd still be interested in comments, though—figuring out what I would teach
always helps me learn.

## Overview

**Topic**: Error handling.

**Audience**: Senior undergraduates who are
comfortable writing programs in Python and JavaScript that are hundred of lines long,
know how to raise and catch exceptions,
and are familiar with SQL, C, and the Unix shell,
but have no experience building production-robust programs.

**Format**: seven 45-minute lessons with exercises.

## 1) What Can Go Wrong

-   Taxonomy of errors
    -   Logic errors: bugs in the program itself
    -   Runtime errors: null dereference, division by zero, index out of bounds
    -   External errors: file not found, network timeout, database constraint violation
    -   Human errors: bad input, misconfiguration, wrong file format
    -   Environmental errors: disk full, out of memory, clock skew
-   Failure modes
    -   Fail-fast vs. fail-slow: silent corruption is harder to debug than an early crash
    -   Silent failures: errors ignored, wrong results returned without warning
    -   Cascading failures: one component's error triggering failures in others
-   C-style error signaling
    -   Return codes: functions return -1, NULL, or 0 on failure
    -   `errno`: a global (thread-local) integer set by system calls
        -   Read with `perror()` or `strerror()`
    -   Sentinel values: EOF (-1), invalid index, or a special out-of-band value
    -   Advantages: explicit control flow, no hidden jumps, zero runtime overhead
    -   Disadvantages: easy to ignore, verbose, callers must check every call, no stack information
    -   Common pitfalls:
        -   Not checking return values
        -   Reading `errno` after another call has overwritten it
        -   `errno` not being set on success
-   Philosophy: errors are not exceptional, they are expected
    -   The happy path is one of many paths
    -   Spectrum of responses: ignore vs. crash vs. recover vs. degrade gracefully
    -   Choosing a response requires knowing the context and the cost of each option

Taxonomy drill
:   Given six short programs in Python, JavaScript, and C,
    each containing a different type of error,
    classify each error using the taxonomy above
    and explain whether the program's response (crash, wrong output, hang, silent skip)
    is appropriate for a production context.

`errno` pitfall hunt
:   A short C function uses `fopen`, `fread`, and `fclose` and checks `errno` after each call.
    The function contains three bugs related to C-style error handling
    (e.g., ignoring a return value, checking `errno` too late, not distinguishing error from end-of-file).
    Identify each bug and propose a fix.

Failure brainstorm
:   Given a brief description of a web form that accepts a user's name, email, and a file upload,
    then stores the data in a database,
    list every error that could occur,
    including errors the user causes,
    errors the network causes,
    errors the OS causes,
    and errors the program itself could cause.
    Compare lists with a partner and identify any category you missed.

## 2) Error Propagation and Recovery

-   Options when an error is detected
    -   Crash/abort: call `abort()`, `panic`, or let the process die
        -   Appropriate when the program is in an unrecoverable state or an invariant is violated
    -   Return an error value: C-style return codes, Go-style `(value, error)` pairs, Rust-style `Result<T, E>`
    -   Raise an exception: hands control to the caller's handler
    -   Log and continue: almost always wrong
        -   Hides failures and corrupts program state
    -   Retry: attempt the operation again (only safe for transient, idempotent operations)
    -   Use a fallback value: return a default, a cached result, or a degraded response
    -   Partial success: complete what you can, report what failed
    -   Compensating action: undo work already done before propagating the error
-   Propagating errors without losing information
    -   Re-raise: pass the error up unchanged
    -   Wrap/chain: add context while preserving the original cause (Python `raise X from Y`, Java `initCause`)
    -   Translate: convert a low-level error into a domain-level error
        (e.g., from `OSError` to `ConfigurationError`)
    -   Anti-pattern: catching an exception and throwing a new one that discards the original
-   Adding context as errors propagate
    -   Include what was being attempted and with what inputs (sanitized)
    -   Each layer adds the context it has
    -   Callers should not have to guess
-   C-style propagation patterns
    -   Check every return value, every time: a missed check is a latent bug
    -   Passing error information up via out-parameters or a shared error struct
    -   `goto cleanup` pattern for resource cleanup on multiple error paths
    -   Comparing C-style propagation to exception propagation: explicitness vs. verbosity
-   Retry logic
    -   Distinguish transient errors (timeout, temporary unavailability)
        from permanent errors (permission denied, not found)
    -   Exponential backoff: double the wait time between retries
    -   Add jitter (random variation) to prevent thundering herd
    -   Set a maximum number of retries and a total timeout
    -   Only retry idempotent operations
        -   Retrying a non-idempotent operation can cause duplicate side effects

Propagation rewrite
:   A Python function reads a configuration file,
    connects to a database using values from that file,
    and runs a query.
    The function is given with no error handling.
    Rewrite it so that errors at each stage are wrapped with context and propagated appropriately,
    then rewrite the equivalent in C using return codes, noting what is harder and easier in each style.

Swallowed exceptions
:   A code snippet contains three `except: pass` or equivalent constructs.
    For each, explain what failure is being hidden,
    what could go wrong as a result,
    and what the correct handling would be.
    At least one case should be a place where logging-and-continuing is wrong even though it feels safe.

Retry with backoff
:   Implement a `retry` decorator (Python) or higher-order function (JavaScript) that wraps a function call,
    retries up to N times on specified exception types,
    uses exponential backoff with jitter,
    and raises the last exception if all retries fail.
    Test it against a stub that fails a configurable number of times before succeeding.
    Discuss which HTTP status codes should trigger a retry and which should not.

## 3) Error Communication

-   Errors have multiple audiences with different needs
    -   End users: need to know what happened and what they can do about it
    -   API callers: need structured, machine-readable information to handle programmatically
    -   Operators and on-call engineers: need enough detail to diagnose and fix the problem
-   User-facing error messages
    -   State what went wrong in plain language
    -   Tell the user what to do next (retry, contact support, correct their input)
    -   Avoid technical jargon, stack traces, and internal identifiers
    -   Do not blame the user
    -   Provide a reference (request ID, error code) they can give to support without revealing internals
    -   Distinguish "you did something wrong" (4xx) from "we did something wrong" (5xx)
-   API error responses
    -   HTTP status codes: 4xx for client errors, 5xx for server errors
        -   Use specific codes (400, 401, 403, 404, 409, 422, 429, 503) rather than always returning 400 or 500
    -   Error response body: include `type`, `message`, `detail`, and `request_id` fields
    -   RFC 7807 (Problem Details for HTTP APIs): a standard format worth knowing
    -   Consistent schema across all endpoints
        -   Callers should not have to handle different shapes
    -   Validation errors: return all field errors at once, not just the first one
-   Security considerations in error communication
    -   Information leakage:
        stack traces, SQL queries, file paths, and internal service names in error messages help attackers
    -   User enumeration: "user not found" vs. "wrong password" reveals whether an account exists
        -   Use "invalid credentials" instead
    -   Timing side-channels: if "user not found" returns in 1ms and "wrong password" returns in 200ms
        (due to password hashing),
         an attacker can enumerate accounts by timing
        -   Always perform the same operations regardless of the error branch
    -   Error messages as reconnaissance:
        the more specific the error, the more an attacker learns about your system
    -   Rule of thumb:
        the user-facing message and the internal log entry should contain different levels of detail
-   Correlation IDs
    -   Generate a unique ID per request
        -   Include it in all logs and in the user-visible error response
    -   Allows an operator to find all logs related to a specific error report
    -   Pass the ID through every internal service call in a distributed system

Message rewrite
:   Five error messages from real or realistic applications are provided
    (e.g., a raw Python traceback shown in a web UI,
    a message reading "MySQL error 1045 for user 'admin'@'localhost'",
    a message reading "Your session token has expired and cannot be refreshed").
    For each,
    write a user-appropriate replacement that is informative without leaking internals,
    and write a separate message suitable for the internal log.

API error schema design
:   Design the error response body for a REST endpoint that registers a new user.
    The schema must handle missing required fields,
    fields that fail validation (email format, password length),
    a duplicate username,
    and an unexpected server failure.
    Show example JSON for each case.

Login timing attack
:   A login function is provided that queries the database first
    and returns "User not found" immediately if the user does not exist,
    or hashes the password and compares it (taking ~200ms) if the user does exist.
    Explain the timing side-channel,
    fix it so both branches take the same time,
    and discuss whether this fix is always necessary or whether it depends on the threat model.

## 4) Logging and Observability

-   Why logging matters for error handling
    -   Errors that are caught and handled still need to be visible to operators
    -   Post-mortem debugging requires a record of what happened
    -   Trends in error rates reveal systemic problems before they become outages
-   Log levels and when to use each
    -   `DEBUG`: detailed internal state, useful during development, not in production by default
    -   `INFO`: normal significant events (startup, shutdown, completed request)
    -   `WARNING`: unexpected but handled conditions that may indicate a problem
    -   `ERROR`: a failure that was caught but means something did not complete successfully
    -   `CRITICAL`: system is in a severely degraded or unrecoverable state
    -   Common mistake: logging every caught exception at `ERROR` regardless of severity
-   Structured logging
    -   Free-text logs are hard to query: key-value pairs (or JSON) are machine-parseable
    -   Standard fields: `timestamp`, `level`, `message`, `request_id`, `user_id`, `error_type`, `duration_ms`
    -   Log the event, not a sentence:
        `{"event": "db_query_failed", "table": "users", "error": "timeout"}`
        rather than `"Failed to query users table due to timeout"`
-   What to include in an error log entry
    -   What was being attempted and with what parameters (sanitized)
    -   The error: type, message, and stack trace for unexpected errors (not for expected/handled errors)
    -   The outcome: did the system recover, degrade, or fail?
    -   Correlation ID to link this entry to the request and to other services
-   What NOT to log
    -   Passwords, API keys, session tokens, OAuth codes: not even partial values or hashes
    -   Personally identifiable information (PII): names, emails, government IDs
        -   Check compliance requirements (GDPR, HIPAA)
    -   Full request/response bodies if they may contain credentials or sensitive data
    -   Stack traces in user-facing API responses (they belong in the internal log only)
-   Audit logs vs. diagnostic logs
    -   Diagnostic logs: help engineers debug problems (mutable, short retention, lower protection)
    -   Audit logs: immutable record of security-relevant actions
        (who authenticated, what data was accessed, what was changed)
        -   Long retention, tamper-evident, access-controlled
    -   Not the same stream: conflating them causes both compliance and debugging problems
-   The observability triad
    -   Logs: record of individual events
    -   Metrics: aggregated numerical measurements (error rate, latency percentiles, queue depth)
    -   Traces: end-to-end path of a request through multiple services
    -   Correlation IDs connect all three (errors visible in metrics can be traced to specific log entries)

Logging retrofit
:   A function that processes uploaded CSV files
    is given with a single `except Exception as e: print(e)` handler.
    Add structured logging using Python's `logging` module (or a JavaScript equivalent).
    Include appropriate log levels for different error conditions,
    add relevant context fields,
    distinguish expected errors (bad CSV format) from unexpected errors (disk full),
    and identify what was unobservable before your changes.

Security audit of log output
:   Three log excerpts are provided,
    each containing at least one security violation
    (e.g., a plaintext password,
    a full stack trace that reveals an internal file path and SQL query,
    or a user ID that allows enumeration of account existence).
    Identify each violation, explain what risk it creates, and show the corrected log entry.

Logging strategy design
:   A data pipeline reads records from an API, transforms them, and writes results to a database.
    The pipeline processes records in batches.
    Design a logging strategy: what events are logged at each stage,
    what fields each entry includes,
    what constitutes a loggable error vs. a metric,
    and how an operator would diagnose a job that completed without crashing
    but produced fewer output records than expected.

## 5) External Systems

-   Why external systems are the primary source of production errors
    -   Code you write can be tested exhaustively
    -   Systems you depend on cannot be controlled
    -   External systems fail in ways that are partial, delayed, and inconsistent
-   File system errors
    -   Not found, permission denied, disk full, file locked by another process, corrupted data
    -   Always close files: use context managers (`with` in Python, `using` in C#, RAII in C++)
    -   Atomic writes: write to a temporary file, then rename
        -   Rename is atomic on POSIX systems
        -   Direct writes leave a window where the file is partially written
    -   Handling partial reads and partial writes explicitly
-   Database errors
    -   Connection failure: the database is unreachable (transient, so retry with backoff)
    -   Timeout: query took too long (may or may not have committed, so check before retrying)
    -   Constraint violation: duplicate key, foreign key failure, not-null violation (permanent, so do not retry)
    -   Deadlock: two transactions are waiting on each other (transient, so retry the whole transaction)
    -   Serialization failure (in serializable isolation):
        transaction conflicted with a concurrent one (transient, so retry)
    -   Connection pool exhaustion: all connections are in use (application-level backpressure needed)
    -   Distinguishing transient from permanent errors using error codes, not message strings
-   Network and HTTP errors
    -   Every external call must have a timeout: separate connect timeout and read/total timeout
    -   Retrying safely:
        only retry if the operation is idempotent or the error occurred before the request was received
    -   HTTP status codes that indicate retrying is safe: 429 (with `Retry-After`), 503, 504
    -   HTTP status codes that should not be retried: 400, 401, 403, 404, 409, 422
    -   Exponential backoff with jitter (review from Lesson 2, now applied to real HTTP clients)
    -   Handling rate limiting: respect `Retry-After` headers, implement client-side rate limiting
-   Parsing external data
    -   Never assume the schema of data from an external source
    -   Validate presence and type of required fields before using them
    -   Handle missing optional fields explicitly rather than letting a `KeyError` or `undefined` propagate
    -   Version skew: the API changed its schema (your parser must detect and report this)
    -   Fail loudly on unexpected schema changes rather than silently producing wrong results

Error handling retrofit for a pipeline
:   A script that downloads a JSON file from an HTTP endpoint,
    parses it,
    and inserts records into a SQLite database is given.
    It has no error handling.
    Add appropriate handling for
    HTTP errors (including distinguishing retryable from non-retryable),
    JSON parse failures,
    missing required fields,
    and database constraint violations.
    For each error type, decide whether to abort, skip the record, or retry, and justify the choice.

Transaction retry
:   A function executes a multi-statement database transaction and fails with a deadlock error.
    Implement retry logic that retries the entire transaction on deadlock,
    does not retry on constraint violations,
    limits total retries,
    and logs each retry attempt.
    Discuss why retrying only the failed statement, rather than the whole transaction, is wrong.

Atomic file write
:   A function saves user settings to a JSON file by opening the file,
    serializing the settings,
    and writing directly.
    Demonstrate two failure scenarios where this approach corrupts the file:
    interrupted write,
    and crash between open and close.
    Implement the temp-file-then-rename pattern and explain why it is safe
    even if the process is killed mid-write.

## 6) Concurrency and Async Errors

-   Why concurrency changes error handling
    -   An error in a thread or task may not propagate to the code that started it
    -   Operations may be partially complete when an error occurs, leaving shared state inconsistent
    -   Some errors (race conditions, deadlocks) only appear under concurrency and are hard to reproduce
-   Errors in threads
    -   Python: an uncaught exception in a `Thread` prints a traceback
        but does not crash the main thread or propagate to the caller
        -    Errors are silently lost unless explicitly collected
    -   Thread pools (`concurrent.futures.ThreadPoolExecutor`):
        exceptions are stored and re-raised when `future.result()` is called
        -   But only if you call it
    -   Always collect results from thread pools
        -   Never fire-and-forget threads that could fail silently
    -   Setting a global thread exception handler (`threading.excepthook`) as a backstop
-   Async/await errors (Python and JavaScript)
    -   Python: an unawaited coroutine silently does nothing (forgetting `await` is a silent bug)
    -   Python: an unhandled exception in a `Task` is reported when the task is garbage-collected
        -   Too late to be useful
        -   Always await tasks or attach `.add_done_callback`
    -   JavaScript: an unhandled promise rejection crashes Node.js in recent versions
        -   In older versions (and some browsers) it is silently swallowed
    -   Always handle rejections: `.catch()`, `try/await/catch`, or `process.on('unhandledRejection')`
    -   Forgetting `await` in a loop:
        tasks are created but not awaited, the loop exits, and all tasks are cancelled
-   Parallel operations and partial failure
    -   `Promise.all`: fails fast
        -   If any promise rejects, the whole thing rejects and other results are lost
    -   `Promise.allSettled`: waits for all promises regardless of outcome
        -   Returns an array of `{status, value/reason}`
        -   Use when you want partial results
    -   Python `asyncio.gather(return_exceptions=True)`:
        returns exceptions as values instead of raising them
        -   Allows processing partial results
    -   Decision: whether to fail fast or collect all results depends on whether partial results are useful
-   Structured concurrency
    -   The problem: a task that spawns subtasks and then throws has left orphaned subtasks running
    -   Python `asyncio.TaskGroup` (3.11+):
        all tasks in the group are cancelled if any raises an exception
        -   The group does not exit until all tasks are done
    -   Structured concurrency ensures the lifetime of every subtask is bounded by the scope that created it
    -   Cancellation propagation:
        when a task is cancelled, it receives a `CancelledError` (Python) or `AbortError` (JS)
        -   Cleanup must happen in `finally` or `try/catch` around `await`
-   Shared state and locks in error paths
    -   A lock must always be released, even if an error occurs
    -   Use `try/finally` or a context manager
    -   If an error occurs while holding a lock after modifying shared state,
        the state may be inconsistent when the lock is released
        -   Decide if the modification needs to be rolled back before releasing
    -   Deadlock: two threads each hold a lock the other needs
        -   Prevent via lock ordering (always acquire locks in the same order) or via timeouts

Silent thread failures
:   A Python script spawns ten threads,
    each of which downloads a file and writes it to disk.
    When a download fails,
    the exception is printed to stderr but the main thread sees all tasks as complete.
    Rewrite using `ThreadPoolExecutor`,
    collect all futures,
    and report which downloads succeeded and which failed,
    then introduce a deliberate failure in two of the threads
    and verify the errors are caught and reported correctly.

Promise.all to Promise.allSettled
:   A JavaScript function fetches data from five independent APIs using `Promise.all`.
    The whole function fails if any one API is unavailable.
    Rewrite it using `Promise.allSettled` so that
    results from available APIs are returned and failures are reported per-API.
    When is `Promise.all`'s fail-fast behavior preferable?

Deadlock identification and fix
:   A function managing a shared cache acquires `cache_lock` and then `stats_lock` in that order.
    Another function acquires the same locks in the opposite order.
    Trace through a scenario where both functions run concurrently and deadlock.
    Fix the bug using lock ordering.
    As a second fix,
    add a timeout to the lock acquisition and show how to handle the case where the timeout expires.

## 7) Resilience Patterns and Production Practices

-   The goal: systems that degrade gracefully rather than fail catastrophically
    -   "Fail safe" vs. "fail secure" vs. "fail operational"
    -   No system achieves zero errors: the goal is bounded, predictable failure
-   Circuit breaker pattern
    -   Closed state: requests pass through normally
    -   Open state: requests fail immediately without attempting the operation
        (protecting a downstream that is already failing)
    -   Half-open state: a probe request is allowed through
        -   If it succeeds, the breaker closes
        -   If not, it stays open
    -   Thresholds: open after N failures in a time window
        -   Reset after a timeout
    -   Use case:
        preventing cascading failures when a slow or failing dependency causes your thread pool to fill up
-   Bulkhead pattern
    -   Isolate resources (thread pools, connection pools, processes)
        so that a failure in one area does not exhaust resources for another
    -   Example: use separate HTTP connection pools for critical and non-critical external services
    -   Trade-off: resource isolation requires over-provisioning in aggregate
-   Timeout patterns
    -   Every call to an external system must have a timeout
        -   A call without a timeout can block forever
    -   Cascading timeouts:
        internal timeouts should be shorter than the external deadline so the caller still gets a response
    -   Distinguishing timeout-on-connect from timeout-on-read
-   Graceful degradation
    -   Serve stale cached data rather than failing when the data source is unavailable
    -   Disable non-critical features (recommendations, analytics) when load is high or dependencies are down
    -   Return partial results rather than failing when some data is unavailable
    -   Read-only mode: allow reads but reject writes when the system cannot safely persist data
-   Testing for failure
    -   Happy-path tests verify normal behavior
        -   Error-path tests verify that errors are handled correctly
    -   Fault injection: deliberately introduce failures (network errors, corrupt data, slow responses) in tests
    -   Property-based testing (Hypothesis, fast-check): generate unexpected inputs to find unhandled edge cases
    -   Chaos engineering: inject controlled failures in production
        to find weaknesses before an actual incident does
-   Error budgets and SLOs
    -   Service Level Indicator (SLI): a measurement of reliability (e.g., fraction of requests that succeed)
    -   Service Level Objective (SLO): the target (e.g., 99.9% success over 30 days)
    -   Error budget: the allowed failure rate (e.g., 0.1% of requests, or about 43 minutes of downtime per month)
    -   If the error budget is exhausted, new features stop and reliability work takes priority
-   Post-mortems
    -   Document what happened, what the impact was, and why it happened
    -   Blameless culture: focus on systemic causes, not individual mistakes
    -   Five Whys: ask "why" repeatedly to find the root cause rather than the proximate cause
    -   Action items must be concrete, assigned, and time-bound

Circuit breaker implementation
:   Implement a `CircuitBreaker` class in Python or JavaScript that wraps a function.
    It should track consecutive failures,
    open after a configurable threshold,
    fail fast while open,
    and attempt recovery after a timeout.
    Write tests that simulate a dependency that fails, recovers, and fails again,
    verifying the breaker transitions through all three states correctly.

Single points of failure analysis
:   A diagram shows a web application with a load balancer,
    two application servers,
    one database,
    and one external payment API.
    Each component can fail independently.
    Identify the single points of failure,
    propose bulkhead and timeout strategies to limit the blast radius of each failure,
    and discuss the cost (infrastructure, complexity) of each mitigation.
    At what point does additional resilience add more complexity than it is worth?

Error path test coverage
:   A small data processing function is provided,
    along with a test suite with 100% line coverage on the happy path.
    Enumerate all error paths in the function
    (e.g., invalid input, missing file, network failure, and malformed response).
    Write tests for each error path using fault injection (i.e., mock the failing component).
    Measure what fraction of error paths were untested before,
    and explain why line coverage is a misleading metric for error-handling code.

## Appendix: Exceptions

-   Exception hierarchies
    -   Python: `BaseException` vs. `Exception` vs. specific types
        -   `KeyboardInterrupt` and `SystemExit` inherit from `BaseException`, not `Exception`
    -   JavaScript: `Error` base class plus built-in subtypes (`TypeError`, `RangeError`, `SyntaxError`, etc.)
    -   Catching a parent class catches all subclasses
        -   `except Exception` in Python does not catch `KeyboardInterrupt`
-   Custom exception types
    -   Subclass the appropriate base: add fields for structured error data
    -   Use custom exceptions to distinguish your errors from library errors
        and to allow callers to catch specifically
    -   Name exceptions as nouns describing the condition,
        not the action (`ConfigurationError`, not `FailedToLoadConfig`)
-   Exception chaining
    -   Python: `raise NewException("context") from original_exception` preserves the original traceback
    -   Python: `raise NewException("context")` inside an `except` block implicitly chains
        (visible as "During handling of the above exception, another exception occurred")
    -   Java: pass the original exception to the constructor of the new one (`new RuntimeException("msg", cause)`)
-   Cleanup with `finally` and context managers
    -   `finally` runs whether or not an exception was raised
        -   Use for resource cleanup (closing files, releasing locks)
    -   Context managers (`with` statement) encapsulate the `try/finally` pattern
        -   Prefer them for resource management
    -   `__exit__` receives exception information and can suppress the exception by returning `True`
        -   Do this rarely and intentionally
-   Anti-patterns
    -   `except Exception: pass`: silently discards all errors
    -   `except Exception as e: print(e)`: visible but unactionable
        -   Provides no context and does not propagate
    -   Catching overly broad types: bare `except:` in Python catches `KeyboardInterrupt` and `SystemExit`
    -   Raising `Exception` directly instead of a specific type: callers cannot catch it selectively
-   Checked vs. unchecked exceptions (Java)
    -   Checked exceptions must be declared or caught
        -   Unchecked (`RuntimeException` subclasses) need not be
    -   Checked exceptions enforce handling at compile time
        but lead to verbose, often-ignored `throws` declarations
    -   Most modern languages (Python, C#, Kotlin, Swift) do not have checked exceptions
