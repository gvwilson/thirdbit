---
title: Rationalizing the Command Line
date: 2026-11-12
category: programming
---

The Unix command line is the most successful user interface ever built, and
also the worst one we are stuck with. It was assembled over half a century, one
tool at a time, by people optimizing for their own fingers at a teletype. The
result is overlapping responsibilities, inconsistent flags, and names that mean
nothing to anyone who was not there when they were invented. That mattered
little when the only consumer was a person who had memorized the quirks. It
matters a great deal now that the principal consumer is an LLM assembling
commands from a prompt, because an LLM has none of that inherited lore—it can
only read the surface, and the surface is a mess.

This post proposes a coherent replacement for the conventional toolset. Unlike
an earlier draft of this argument, which mostly renamed the existing commands,
this one treats the *data* as the thing to fix: commands should pass typed
tables and records between each other, not lines of text, and should only
render that data as text at the very last moment. It is a design exercise, not
a working system.

## The problem is text, not names

The names and the flags are symptoms. The disease is that the Unix command
line treats everything as a stream of bytes and forces every tool to re-derive
structure from it. `ls` knows it is printing files but flattens them into
whitespace-aligned columns. `ps` knows it is printing processes but pads and
truncates them to fit the current terminal width. The next tool in the pipe
receives that text and has to guess where one field ends and the next begins.
`awk` exists because the columns are not labelled. `cut` and `sed` exist to
re-derive fields that a tool discarded one step earlier. `sort -k 3` and
`uniq -f 1` exist because "the third field" and "skip one field" are the only
way to talk about columns that were never given names.

Every one of those tools is a workaround for the same missing thing: *the
structure was thrown away.* The single most important fix is to stop throwing
it away. Pass typed tables and records between tools, and render them as text
only at the boundary where a human—or a file—actually needs text.

## What two shells already figured out

Two modern shells have already made this move, and the design below borrows
from both.

**PowerShell** built a pipeline that carries .NET *objects*, not text. A
command like `Get-Process` produces a stream of process objects; the next
command reads their typed properties instead of parsing columns. PowerShell
draws a hard line between data and display: `ConvertTo-Json` and
`ConvertTo-Csv` turn objects into data, while `Format-Table` and `Format-List`
turn objects into *screen formatting* and are display-only—they must be the
last command in a pipeline, and piping their output into a data command
produces garbage. That split is exactly right and this design adopts it.
PowerShell also standardizes a set of common parameters (`-Verbose`,
`-ErrorAction`, `-WhatIf`, `-Confirm`) shared by every cmdlet. Its flaws are
the verbose `Verb-Noun` names, the case-insensitive abbreviable parameters, and
awkward gotchas like `ConvertTo-Json` defaulting to `-Depth 2` and silently
flattening anything deeper.

**Nushell** goes further and makes *typed tables* the currency of the shell.
`ls` returns a table of records; `where`, `select`, and `sort-by` reshape it by
field name; `to json` and `to csv` serialize it; `from json` and `from csv`
parse it back; `into int` and `into string` convert types. A pipeline like
`ls | where size > 10mb | sort-by modified | to json` never parses a text
column, because there are no text columns to parse. Nushell's weakness is that
it keeps the legacy command names and their inherited flags, so the *surface*
is still cluttered even though the *data* is clean.

The design below is the synthesis: Nushell's typed tables, PowerShell's hard
separation of data from display, and neither system's legacy names.

## Principles

1. **Typed data, not text.** Commands pass tables (lists of records with named
   fields) and scalars, never ad-hoc text. Text is a rendering.

2. **One verb per tool.** Each tool does one thing; each thing is done by one
   tool.

3. **One flag, one meaning.** A flag means the same thing everywhere. Shared
   flags include `--recursive`, `--ignore-case`, `--reverse`, `--human`,
   `--quiet`, `--force`, `--interactive`, `--help`, `--version`.

4. **Data and display are separate.** Serialization is an explicit, final step
   (`to json`), never a mode hidden inside a data command.

5. **Schemas are declared.** Every producer documents the fields it emits, so
   an LLM can discover what a table contains without running it.

## The design

Every command is one of three things: a **producer** (emits typed data), a
**transformer** (reshapes typed data), or a **serializer** (turns typed data
into text). Pipelines run producers into transformers into a serializer.

```
list | filter type == "file" | sort size --reverse | to json
```

### Producers

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

### Transformers

These are the heart of the design. They work on *any* table and are the
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

### Serializers

| tool | output | replaces |
|------|--------|----------|
| `to table` | aligned text table for humans | `column`, `fmt` |
| `to json` | JSON | `jq`, `ConvertTo-Json` |
| `to csv` | CSV | `ConvertTo-Csv` |
| `to plain` | one field per line, for text pipelines | implicit text |

### The remaining verbs

#### File and directory operations

| `go` | `cd` |
| `copy` | `cp` |
| `move` | `mv` |
| `remove` | `rm`,`rmdir` |
| `create` | `touch`, `mkdir` with `--directory`, `mktemp` with `--temporary` |
| `link` | `ln` |
| `permit` | `chmod`, `chown`, `chgrp` via `--mode`, `--owner`, `--group` |

#### Processes

| `signal` | `kill`, `killall`, `pkill` |
| `monitor` | `top` |
| `run` | `nice`, `timeout`, `nohup` |

#### System

| `help` | `man`, `apropos`, `whatis` |
| `which` | `which`, `whereis`, `type` |

#### Network

| `fetch` | `curl`, `wget` |
| `connect` | `ssh` |
| `send` | `scp`, `sftp`, `rsync` |
| `reach` | `ping` |
| `trace` | `traceroute` |
| `lookup` | `dig`, `nslookup`, `host` |

#### Archive and compression

| `archive` | `tar`, `cpio`, `zip` via `--create`, `--extract`, `--list` |
| `compress` and `expand` | `gzip`, `bzip2`, `xz`, `zip`, `unzip` |

#### Miscellaneous

`calc` (and `bc`),
`echo`,
`expr`,
`false`,
`seq`,
`sleep`,
`test`,
`true`,
`yes`

## The catalogue

The full mapping, grouped, covers roughly a hundred legacy commands.

### Files and directories

`ls`, `stat` → `list`;
`cd` → `go`;
`pwd` → `where`;
`cp`, `install` → `copy`;
`mv` → `move`;
`rm`, `rmdir` → `remove`;
`mkdir`, `touch`, `mktemp` → `create`;
`ln` → `link`;
`readlink`, `realpath` → `resolve`;
`find`, `locate` → `find`;
`file` → `identify`;
`chmod`, `chown`, `chgrp`, `umask` → `permit`.

### Content

`cat`, `tac`, `head`, `tail`, `less`, `more` → `read`;
`wc` → `count`;
`sort` → `sort`;
`uniq` → `unique`;
`cut` → `select`;
`paste`, `join` → `join`;
`comm` → `join` with set modes;
`tr`, `sed` → `replace`;
`awk` → `filter`, `map`, and the aggregates;
`grep`, `egrep`, `fgrep` → `search`;
`tee` → `branch`;
`fold`, `fmt`, `column` → `to table`;
`nl` → `read --numbered`;
`split`, `csplit` → `split`;
`od`, `hexdump` → `hex`;
`strings` → `strings`;
`rev` → `replace` with `--reverse`;
`xargs` → `each`.

### Checksums and encoding

`cksum`, `md5sum`, `sha1sum`, `sha256sum`, `shasum` → `checksum --algorithm`;
`base64` → `encode`/`decode`.

### Processes

`ps` → `processes`;
`top`, `htop` → `monitor`;
`kill`, `killall`, `pkill` → `signal`;
`pgrep` → `processes` then `filter`;
`nice`, `renice`, `nohup`, `timeout` → `run`;
`jobs`, `fg`, `bg` → `jobs`, `foreground`, `background`;
`time` → `time`.

### System

`uname`, `hostname`, `uptime` → `system`;
`whoami`, `id`, `groups` → `user`;
`who`, `w`, `last` → `logged-in`;
`date` → `time`;
`cal` → `calendar`;
`env`, `printenv`, `set`, `export`, `unset` → `environment`;
`echo`, `printf` → `echo` and `format`;
`man`, `apropos`, `whatis`, `info` → `help`;
`which`, `whereis`, `type`, `command` → `which`;
`bc`, `expr` → `calc`;
`test`, `[` → `test`;
`clear`, `tty` → unchanged.

### Disk and filesystems

`du` → `usage`;
`df` → `space`;
`mount`, `umount` → `mount`, `unmount`;
`fsck` → `check`;
`mkfs` → `format`.

### Network

`curl`, `wget`, `ftp` → `fetch`;
`ssh` → `connect`;
`scp`, `sftp`, `rsync` → `send`;
`ping` → `reach`;
`traceroute` → `trace`;
`dig`, `nslookup`, `host` → `lookup`;
`ifconfig`, `ip` → `interfaces`;
`netstat`, `ss` → `connections`;
`nc`, `telnet` → `talk`.

## Archive and compression

`tar`, `cpio`, `zip`, `unzip` → `archive`;
`gzip`, `gunzip`, `bzip2`, `bunzip2`, `xz`, `unxz`, `zip`, `unzip` → `compress`, `expand`.

## Old to new

A representative slice:

| today | becomes |
|-------|---------|
| `ls -la` | `list --long` |
| `du -sh *` | `usage --human` |
| `ps aux` | `processes` |
| `cat f \| grep x \| wc -l` | `search x f \| count` |
| `cut -d, -f1,3` | `select name, amount` |
| `sort -t, -k3 -n` | `sort score --numeric` |
| `awk '$3 > 100 {print $1}'` | `filter score > 100 \| select name` |
| `grep -ri foo .` | `search foo --recursive --ignore-case` |
| `find . -name '*.py'` | `find . --name '*.py'` |
| `curl -s url` | `fetch url` |
| `tar czf x.tgz dir` | `archive dir --create --compress` |
| `sha256sum f` | `checksum f --algorithm sha256` |
| `jq '.items[]' f` | `read f \| from json \| flatten` |

## Why this helps an LLM

An LLM composes tools it can *predict*, and the text-line model defeats
prediction at every step. A table with named fields can be filtered and sorted
without guessing delimiters, quoting rules, or which column is which. A
declared schema means the model can discover what a command produces before it
runs it. A hard separation of data from display means there is no `-l`, `-h`,
or `-p` flag whose meaning changes depending on whether output is going to a
terminal or a pipe. And a single consistent flag vocabulary removes the
per-tool lookup that currently consumes most of an agent's attention.

The goal is not fewer keystrokes. It is a command line whose surface tells the
truth about its data.

## What this does not solve

The proposal stops at the shape of the tools. It does not define how a tool
*declares* its schema so an LLM can read it, how the pipeline carries typed
values across the boundary to legacy programs, or what the `filter`/`map`
expression language looks like in full. Those are the hard parts—the kind that
turn a blog post into a project. PowerShell and Nushell have each answered them
differently and incompletely, which is the strongest argument that the next
shell, whoever builds it, should treat the answers as the interesting part
rather than the afterthought.

*Sources: the [Nushell book](https://www.nushell.sh/book/) and
[command reference](https://www.nushell.sh/commands/), and the PowerShell
documentation for
[ConvertTo-Json](https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/convertto-json)
and
[about_CommonParameters](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_commonparameters).*
