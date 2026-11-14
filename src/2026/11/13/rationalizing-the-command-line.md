---
title: Rationalizing the Command Line
date: 2026-11-13
category: programming
---

The Unix command line is the most successful user interface ever built, and also
the worst one we are stuck with. It was assembled over half a century, one tool
at a time, by people optimizing for their own fingers on a keyboard. The result
is overlapping responsibilities, inconsistent flags, and names that mean nothing
to anyone who was not there when they were invented.  That didn't matter when
the only consumers were people willing to memorize its quirks; it matters a
great deal now that the principal consumers are people trying to understand what
an LLM is doing on their behalf.

This post is a thought exercise: what a set of replacement tools that have more
readable names and more consistent (and therefore more learnable) flags look
like? This wouldn't make any difference to the LLMs; the aim would be to make
their actions more legible to users who aren't command-line nerds.

One core design decision is to stop treating everything as a stream of bytes,
which forces every tool to re-derive structure.  Two modern shells have already
done this.  [PowerShell][powershell] built a pipeline that carries .NET objects,
not text. A command like `Get-Process` produces a stream of process objects; the
next command reads their typed properties instead of parsing columns. PowerShell
draws a hard line between data and display: `ConvertTo-Json` and `ConvertTo-Csv`
turn objects into data, while `Format-Table` and `Format-List` format objects
for the screen and are display-only: they must be the last command in a
pipeline, and piping their output into a data command produces garbage.
PowerShell also standardizes a set of common parameters (`-Verbose`,
`-ErrorAction`, `-WhatIf`, `-Confirm`) shared by every command. Its flaws are
the verbose `Verb-Noun` names, the case-insensitive abbreviable parameters, and
awkward gotchas like `ConvertTo-Json` defaulting to `-Depth 2` and silently
flattening anything deeper.

[Nushell][nushell] goes further by making typed tables the standard.  `ls`
returns a table of records; `where`, `select`, and `sort-by` reshape it by field
name; `to json` and `to csv` serialize it; `from json` and `from csv` parse it
back; `into int` and `into string` convert types, and so on. A pipeline like
`ls | where size > 10mb | sort-by modified | to json` therefore never has to
parse a text column.  Nushell's weakness is that it keeps the legacy command
names and their inherited flags, so the surface is still cluttered even though
the data is clean.

The design below is the synthesis: Nushell's typed tables, PowerShell's
separation of data from display, neither system's legacy names, and a standard
way to interrogate tools to get their output schema.

## Principles

Typed data, not text.
:   Commands pass tables (lists of records with named fields) and scalars, never
    ad-hoc text. Text is a rendering.

One verb per tool.
:   Each tool does one thing; each thing is done by one tool.

One flag, one meaning.
:   A flag means the same thing everywhere. Shared flags include `--recursive`,
    `--ignore-case`, `--reverse`, `--human`, `--quiet`, `--force`,
    `--interactive`, `--help`, `--version`.

Data and display are separate.
:   Serialization is an explicit, final step (`to json`), never a mode hidden
    inside a data command.

Schemas are declared.
:   Every producer documents the fields it emits, so other tools (not just LLMs)
    can discover what a table contains.

Three types of commands.
:   Every command is one of three things: a producer (emits typed data), a
    transformer (reshapes typed data), or a serializer (turns typed data into
    text). Pipelines run producers into transformers into a serializer.

## Producers

| tool | emits | replaces |
|------|-------|----------|
| `list path` | `{name, type, size, modified, mode, owner, group}` | `ls`, `stat` |
| `find path` | `{path, type, size, modified}` | `find`, `locate` |
| `resolve path` | `{path, canonical, target}` | `realpath`, `readlink` |
| `read path` | the file as a list of line records, or a string | `cat`, `head`, `tail`, `tac`, `less`, `zcat` |
| `search pattern` | `{file, line, column, text}` | `grep`, `egrep`, `fgrep`, `zgrep` |
| `processes` | `{pid, ppid, user, cpu, mem, command}` | `ps` |
| `usage path` | `{path, size, files}` | `du` |
| `space` | `{filesystem, size, used, available, mount}` | `df` |
| `system` | `{os, kernel, hostname, arch, uptime}` | `uname`, `hostname` |
| `user` | `{name, uid, gid, groups}` | `whoami`, `id`, `groups` |
| `time` | `{now, utc, epoch}` | `date` |
| `environment` | `{name, value}` | `env`, `printenv`, `set` |
| `interfaces` | `{name, address, mac, state}` | `ifconfig`, `ip addr` |
| `connections` | `{protocol, local, remote, state}` | `netstat`, `ss` |
| `mounts` | `{device, mountpoint, fstype, options}` | `mount`, `df` |
| `logged-in` | `{user, tty, host, since}` | `who`, `w`, `last` |
| `checksum path` | `{path, algorithm, digest}` | `md5sum`, `sha256sum`, `cksum` |

## Transformers

These are the heart of the design. They work on any table and are the
replacement for a large fraction of the text tooling.

| tool | what it does | replaces |
|------|--------------|----------|
| `select field…` | keep named columns | `cut`, PowerShell `Select-Object` |
| `filter predicate` | keep rows matching a predicate | `awk` on columns, Nushell `where` |
| `sort field…` | sort by named fields | `sort -k`, `sort -t` |
| `unique field…` | drop duplicate rows | `uniq`, `sort -u` |
| `group field` | group rows by a field | `awk` grouping |
| `join right --on field` | relational join of two tables | `join`, `comm` |
| `count` | count rows (or a field's values) | `wc -l`, `uniq -c` |
| `sum`, `mean`, `min`, `max field` | aggregate a numeric field | `awk '{s+=$1}END{print s}'` |
| `map expression` | compute a new field | `awk '{print ...}'` |
| `head N`, `tail N` | take first or last N rows | `head`, `tail` |
| `replace pattern replacement` | substitute text in a field | `sed 's///'`, `tr` |
| `flatten` | unnest a nested field | `jq flatten` |

`filter` and `map` need a small expression language. The design keeps it
deliberately tiny—field access, comparison, arithmetic, and boolean
combinators—because a full programming language bolted onto a filter is how
`awk` happened.

## Serializers

| tool | output | replaces |
|------|--------|----------|
| `to table` | aligned text table for humans | `column`, `fmt` |
| `to json` | JSON | `jq`, `ConvertTo-Json` |
| `to csv` | CSV | `ConvertTo-Csv` |
| `to plain` | one field per line, for text pipelines | implicit text |

## Others

### File and directory operations

| new | old |
|-----|-----|
| `go` | `cd` |
| `copy` | `cp` |
| `move` | `mv` |
| `remove` | `rm`,`rmdir` |
| `create` | `touch`, `mkdir` with `--directory`, `mktemp` with `--temporary` |
| `link` | `ln` |
| `permit` | `chmod`, `chown`, `chgrp` via `--mode`, `--owner`, `--group` |

### Processes

| new | old |
|-----|-----|
| `signal` | `kill`, `killall`, `pkill` |
| `monitor` | `top` |
| `run` | `nice`, `timeout`, `nohup` |

### System

| new | old |
|-----|-----|
| `help` | `man`, `apropos`, `whatis` |
| `which` | `which`, `whereis`, `type` |

### Network

| new | old |
|-----|-----|
| `fetch` | `curl`, `wget` |
| `connect` | `ssh` |
| `send` | `scp`, `sftp`, `rsync` |
| `reach` | `ping` |
| `trace` | `traceroute` |
| `lookup` | `dig`, `nslookup`, `host` |

### Archive and compression

| new | old |
|-----|-----|
| `archive` | `tar`, `cpio`, `zip` via `--create`, `--extract`, `--list` |
| `compress` and `expand` | `gzip`, `bzip2`, `xz`, `zip`, `unzip` |

### Miscellaneous

`calc` (and `bc`),
`echo`,
`expr`,
`false`,
`seq`,
`sleep`,
`test`,
and `true`.

## Examples

| today | becomes |
|-------|---------|
| `ls -la` | `list --long` |
| `du -sh *` | `usage --human` |
| `ps aux` | `processes` |
| `cat f | grep x | wc -l` | `search x f | count` |
| `cut -d, -f1,3` | `select name, amount` |
| `sort -t, -k3 -n` | `sort score --numeric` |
| `awk '$3 > 100 {print $1}'` | `filter score > 100 | select name` |
| `grep -ri foo .` | `search foo --recursive --ignore-case` |
| `find . -name '*.py'` | `find . --name '*.py'` |
| `curl -s url` | `fetch url` |
| `tar czf x.tgz dir` | `archive dir --create --compress` |
| `sha256sum f` | `checksum f --algorithm sha256` |
| `jq '.items[]' f` | `read f | from json | flatten` |

## Declaring a Schema

Every producer has a shared option `--schema`, which makes it emit a table that
describes the fields it produces. `list --schema`, for example, returns:

| field | type | description |
|-------|------|-------------|
| `name` | path | file or directory name |
| `type` | string | `file`, `directory`, or `symlink` |
| `size` | bytes | size in bytes |
| `modified` | timestamp | time of last modification |
| `mode` | string | permission bits |
| `owner` | string | owning user |
| `group` | string | owning group |

Because a schema is itself a table, the ordinary transformers and serializers
apply to it: `list --schema | select field, type | to json` yields the compact
machine-readable form, while `list --schema` alone renders it for a person.  As
a result, a reader can learn what a command will emit before running it, using
the same vocabulary as any other data.

## Further Reading

-   The [Nushell book][nushell-book] and [command reference][nushell-command]
-   The PowerShell documentation for [ConvertTo-Json][powershell-json] and [CommonParameters][powershell-params]

[nushell]: https://www.nushell.sh/
[nushell-book]: https://www.nushell.sh/book/
[nushell-command]: https://www.nushell.sh/commands/
[powershell]: https://www.microsoft.com/powershell
[powershell-json]: https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/convertto-json
[powershell-params]: https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_commonparameters
