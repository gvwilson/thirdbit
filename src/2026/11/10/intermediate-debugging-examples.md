---
title: "Intermediate Debugging Examples"
date: 2026-11-10
category: education software-engineering
---
I'm thinking about extending [this set of debugging examples][unbreak]
with the more complex examples described below.
I'd be very grateful for feedback:
would they be useful?
Would they be useful *to you*?
What other examples could be included,
or should be included instead of some of the ones I've outlined?

## Log Ingestion Pipeline

A command-line Python tool that reads application log files, normalizes each
line, extracts structured fields, and loads them into SQLite for later querying.

- What it does: walks a directory of log files, parses each line with a regex,
  converts the timestamp, extracts level/component/message, and inserts a row
  per line into a `logs` table.

- Components: a scanner, a parser/normalizer, a loader, and a query/report
  module that runs after loading.

- The bug: the normalizer converts timestamps to UTC and stores them as naive
  datetimes, while the query layer assumes local time and compares against naive
  `datetime.now()`. Reports are shifted by the local UTC offset. Secondarily,
  the regex silently drops lines it doesn't match, but the loader reports "N
  lines loaded" from the file's own count, so missing events are invisible.

- What it teaches: the wrong rows are *present and plausible*; nothing raises.
  The two timezone assumptions live in different files, and the dropped-line bug
  only shows up as a *shortfall* the learner has to notice rather than an error.

## Concurrent Web Crawler

A Python crawler using `httpx` with a thread or `asyncio` worker pool that
fetches pages, normalizes URLs, deduplicates by content hash, and records pages
and links in SQLite.

- What it does: starts from seed URLs, fetches pages concurrently, extracts
  links, and stores each page body plus a `pages`/`links` relationship in
  SQLite.

- Components: a frontier/queue, a fetcher pool, a link extractor, a URL
  normalizer, and a storage layer.

- The bug: the "have I seen this URL?" check and the subsequent insert are not
  atomic, so two workers can both pass the check and fetch/store the same page
  (duplicate rows, double work). Separately, URL normalization (stripping
  trailing slashes, fragments, and normalizing case) is applied in the fetch
  path but not in the link-extraction path, so the *same* page is keyed under
  two URLs.

- What it teaches: it is a race, so it reproduces intermittently and only under
  concurrency. The normalization mismatch produces near-duplicate rows that look
  like different records at a glance.

## Library Lending API

A FastAPI application with SQLite persistence and an htmx front end for a small
library: books, members, loans, and holds.

- What it does: serves pages listing books and loans, and endpoints to check a
  book out to a member, return it, and place holds. htmx renders table rows and
  status fragments server-side.

- Components: route handlers, a data-access layer, SQLite models, htmx
  templates, and a small availability helper used by both listing and checkout.

- The bug: checkout/return is not wrapped in a transaction, so the copy count is
  decremented, then a later `INSERT` (the loan row) fails, leaving the count
  wrong. The loan list also issues one query per row (N+1), which is fine until
  the table grows. Availability is derived from loans in the listing path but
  from a cached copy count in the checkout path, and the two drift.

- What it teaches: the transaction bug corrupts state that looks consistent
  until a specific failure; the N+1 only bites under load; the availability
  discrepancy is a disagreement between two places that each look individually
  correct.

## Job Queue with Retries

A Python worker pool backed by a SQLite `jobs` table that claims, runs, and
marks jobs done, with retry and exponential backoff.

- What it does: producers insert jobs; N workers poll for pending jobs, claim
  one, run it, and update its status; failures are retried with backoff up to a
  maximum attempt count.

- Components: an enqueue function, a claim loop, a runner, and a retry/settle
  routine.

- The bug: claiming is a `SELECT` followed by a separate `UPDATE ... WHERE
  status='pending'`, not an atomic claim, so two workers can claim the same job.
  The retry logic also treats permanent failures (a job that always raises the
  same way) as retryable until the cap, then marks them "failed", while a
  transient timeout path re-enqueues a job that was in fact already completed.

- What it teaches: duplicate execution and dropped jobs both manifest as *count*
  mismatches across a run, and the two bugs interact: retries resurface jobs the
  duplicate-claim bug already ran.

## Checkout Wizard

A multi-step checkout workflow where an Alpine.js front end holds state across
steps and a FastAPI backend validates and submits the order.

- What it does: the client advances through steps, applying a discount code and
  stock availability checks as it goes; the final submit posts the whole order
  to the server, which re-validates.

- Components: Alpine components per step, a client-side cart/discount store, and
  FastAPI endpoints for validation and order submission.

- The bug: client-side validation and server-side validation disagree: the
  discount is applied client-side for display but not re-applied server-side,
  and an out-of-stock item passes the client check (the client's stock number is
  stale) and only fails at submit. Alpine state is not reset when the user
  navigates back and starts a new order, so a stale discount or address leaks
  in.

- What it teaches: the UI *shows* a valid-looking order that the server rejects,
  and the leak is state the learner can't see in the markup. The two validation
  layers are in different languages and files.

## Report Generator

A Python command-line tool that reads SQLite, groups records into day/week/month
buckets, and emits CSV or HTML.

- What it does: runs aggregation queries with a chosen granularity, formats
  bucket labels, and writes the result to a report file.

- Components: a query builder, a bucket/label formatter, and an output writer.

- The bug: the aggregation query uses inclusive/exclusive boundaries or naive
  vs. UTC datetimes differently from the label formatter, so records landing
  exactly on a boundary are double-counted in one bucket and omitted from the
  next, and the label's date is off by one. The two bucket definitions live in
  separate functions.

- What it teaches: totals look plausible but don't sum to the source row count,
  and the error only appears for records on exact boundaries (a small,
  intermittent-looking slice of the data).

## Incremental Backup Tool

A Python command-line tool that walks a source tree, content-hashes files,
deduplicates, and copies changed files into a backup directory while recording a
manifest in SQLite.

- What it does: scans the tree, hashes each file, compares against the manifest,
  and copies new/changed files, updating the manifest.

- Components: a walker/scanner, a hasher, a differ, and a copier/manifest
  updater.

- The bug: the tool scans, then copies, with no snapshot in between, so a file
  changed between the scan and the copy is copied in a torn state or missed
  entirely. The dedup key is the content hash alone, while the manifest records
  path + mtime, so an empty file (or a file that became empty) is treated as
  unchanged because "missing" and "empty" collide.

- What it teaches: the race is timing-dependent and only affects files touched
  during the backup; the empty-vs-missing collision silently skips a file the
  learner expected to be copied.

## Legacy Data Migration ETL

A Python script that reads a legacy SQLite schema and writes a normalized schema
for the same data.

- What it does: reads rows from several legacy tables and inserts them into new
  tables with foreign keys, `NOT NULL` constraints, and unique indexes.

- Components: a reader per legacy table, a transformer, and a writer with
  constraint handling.

- The bug: insert ordering isn't respected (child rows are inserted before their
  parents, violating foreign keys) and legacy rows contain empty strings and
  duplicates that violate the new schema's `NOT NULL` and unique constraints, so
  the load fails partway and leaves a half-migrated database.

- What it teaches: the failure is a constraint violation deep in a bulk load,
  far from the code that read the offending row, and the partial state makes
  rerunning the migration unsafe without cleanup.

## Notification Dispatcher

A Python daemon that polls a SQLite `outbox` table, sends each pending message
(email or HTTP), and marks it sent.

- What it does: a loop selects unsent rows, sends them, and updates their
  status; on send failure it leaves the row pending for retry.

- Components: a poller, a sender (SMTP/HTTP), and a status updater.

- The bug: send-then-mark is not atomic, so a crash or timeout after the send
  but before the `UPDATE` leaves the row pending, and the message is sent again
  on the next poll. There is no idempotency key on the receiving side, so a slow
  or duplicated request produces duplicate deliveries.

- What it teaches: the duplicated side effect (an extra email) happens outside
  the process, on the recipient's side, and the learner sees a "pending" row
  that looks like it was never sent.

## Plugin-Based CLI

A Python command-line tool (argparse or typer) that loads plugins from a
directory; plugins register subcommands and share a config object.

- What it does: discovers plugin modules, imports them, collects the subcommands
  each registers, and dispatches a chosen subcommand.

- Components: a plugin loader, a registry, a shared config object, and the
  dispatch/argument parser.

- The bug: the shared config is a mutable dict aliased into every plugin; one
  plugin mutates it and another reads the mutated value, so behavior depends on
  plugin registration order. A plugin that registers a subcommand whose name
  collides with an existing one silently overwrites the earlier registration.

- What it teaches: the bug moves with load order and only appears when a
  specific combination of plugins is installed; the overwrite leaves no error,
  just a missing command.

## Metrics Dashboard

A dashboard where htmx polls a FastAPI endpoint for JSON and Alpine.js renders
charts, backed by SQLite sample storage.

- What it does: a collector writes samples to SQLite; a FastAPI endpoint returns
  the latest samples as JSON; an htmx-triggered poll fetches them and Alpine
  components render the charts.

- Components: a sample collector, a query endpoint, htmx polling markup, and
  Alpine chart components.

- The bug: timestamp comparison uses the browser's wall clock against server/DB
  timestamps, so clock skew makes samples appear duplicated or missing at the
  boundary. An htmx poll response can arrive out of order and update the DOM
  *after* a newer response, overwriting fresh data with stale data.

- What it teaches: both bugs are timing/ordering problems that don't reproduce
  deterministically, and the symptom (a chart briefly showing old values) looks
  like a rendering glitch.

## Session & Auth Service

A FastAPI application with SQLite and an htmx front end that logs users in,
issues a session token, validates it in middleware, and invalidates it on
logout.

- What it does: login verifies credentials and issues a token (stored in a
  sessions table); middleware validates the token on each request; logout marks
  the session invalid.

- Components: login/logout routes, session/token storage, validation middleware,
  and a refresh path.

- The bug: token expiry is checked in the middleware, but the refresh path
  extends a *different* record (or logout invalidates the session row without
  invalidating already-issued tokens), so a session that should be expired or
  logged out still authenticates. A race between the expiry check and request
  handling lets a request past just as the token lapses.

- What it teaches: the security-sensitive behavior only fails at the exact
  expiry/logout boundary, and the invalid state lives in a different table or
  code path from the check, so both sides look correct in isolation.

[unbreak]: @root/unbreak/
