---
title: Rationalizing the Command Line
date: 2026-11-12
category: programming
---

The Unix command line is the most successful user interface ever built, and
also the worst one we are stuck with. It was assembled over half a century, one
tool at a time, by people optimizing for their own fingers at a teletype. As a
result, it is full of overlapping responsibilities, inconsistent flags, and
names that mean nothing to anyone who was not there when they were invented.
That mattered little when the only consumer was a person who had memorized the
quirks. It matters a great deal now that the principal consumer is an LLM
assembling commands from a prompt, because an LLM has none of that inherited
lore to fall back on—it can only read the surface, and the surface is a mess.

This post proposes a coherent replacement for the conventional toolset: a set
of command-line tools with one verb per tool, one flag meaning per tool, and
output that a machine can parse without guessing. It is a design exercise, not
a working system. I will describe the principles, catalogue what we are
replacing, present the replacement set, and end with what PowerShell and
Nushell got right and wrong.

## Three principles

1.  **One verb per tool.** Each tool does one thing, and each thing is done by
    exactly one tool. If two commands can answer the same question, one of them
    disappears.

2.  **One flag, one meaning.** A flag means the same thing everywhere it
    appears. `--reverse` never changes to mean "recursive" on some other tool,
    because "recursive" is always spelled `--recursive`.

3.  **Legible output.** Default output is one record per line, in a fixed
    order, with no columns that change shape based on terminal width. A tool
    that might be scripted offers `--json`; a tool that must remain plain text
    keeps its fields in a stable, documented order.

## What is wrong today

The problems come in three flavors.

**Overlap.** Several responsibilities are split across multiple commands, and
several commands do more than one thing. `cat`, `head`, `tail`, and `less` all
print file content and differ only in *how much*. `grep`, `sed`, and `awk`
overlap so thoroughly that "should I use grep or sed for this?" is a permanent
thread. `du` and `df` both report disk numbers but from opposite directions.
`sort` and `uniq` are almost always used as a pair. `tar` bundles files *and*
invokes a compressor, while `zip` does both in one binary.

**Inconsistent flags.** The same letter means different things depending on
which tool you are holding:

| flag | means in one tool | means in another |
|------|-------------------|------------------|
| `-c` | bytes in `head`/`tail`/`wc` | "check" in `sort` |
| `-r` | reverse order in `sort` | recursive in `grep`/`cp`/`rm` |
| `-n` | line count in `head`/`tail` | numeric order in `sort` |
| `-L` | follow symlinks in `ls` | longest line in `wc` |

Worse, some tools use short flags only (`ls -l`), some support long flags
(`grep --ignore-case`), and some define short and long flags that do not
actually correspond (`head -n` is `--lines`, not `--number`). An LLM cannot
safely infer that `-i` is "interactive" in one place and "ignore case" in
another; it has to look each one up.

**Cryptic names.** `awk` (the authors' initials), `sed` (stream editor), `grep`
(global/regular expression/print), `du` (disk usage), `df` (disk free), `dd`,
`tr`. These are not discoverable; they are memorized. Abbreviations saved a
person two keystrokes and cost every future reader a lookup.

## The catalogue

The tools being replaced, grouped by responsibility:

- **Navigation:** `cd`, `pwd`, `ls`
- **Files and directories:** `cp`, `mv`, `rm`, `rmdir`, `mkdir`, `touch`, `ln`,
  `stat`, `find`
- **Content:** `cat`, `head`, `tail`, `less`, `more`, `wc`, `sort`, `uniq`,
  `cut`, `paste`, `diff`, `cmp`, `file`
- **Search and transform:** `grep`, `egrep`, `fgrep`, `sed`, `awk`, `tr`
- **Processes:** `ps`, `top`, `kill`, `killall`
- **System:** `uname`, `hostname`, `whoami`, `id`, `date`, `env`, `echo`,
  `man`, `apropos`, `which`
- **Disk:** `du`, `df`
- **Network:** `curl`, `wget`, `ssh`, `scp`, `ping`
- **Archive:** `tar`, `gzip`, `gunzip`, `zip`, `unzip`

## The replacement set

Every tool is a single lowercase verb. Every flag is `--long-form`. A small set
of flags is shared across all tools and always means the same thing:
`--recursive`, `--ignore-case`, `--reverse`, `--human`, `--quiet`, `--force`,
`--interactive`, `--json`, `--help`, `--version`. Exit codes are fixed: `0`
success, `1` "nothing found" (used by search and find), `2` usage error.

### Navigation

- `list [path]` — list directory entries. `--long` for detail, `--human` for
  sizes, `--recursive` to descend. Replaces `ls` and the "just enumerate"
  subset of `find`.
- `go [path]` — change directory. Replaces `cd`.
- `where` — print the current path. Replaces `pwd`.

### Files and directories

- `copy`, `move`, `remove`, `link` — the four verbs, unchanged in meaning, with
  `--recursive` and `--force` spelled out. `remove` also handles empty
  directories (replacing `rmdir`).
- `create path` — make an empty file, or a directory with `--directory`.
  Replaces `touch` and `mkdir`.
- `info path` — file metadata (type, size, ownership, timestamps). Replaces
  `stat` and the verbose half of `ls -l`.
- `find path --pattern …` — locate files by predicate. Replaces `find` and
  `locate`.

### Content

- `read path` — print file content. `--lines N` takes the first N lines (was
  `head`), `--from N` the tail (was `tail`), `--from A --to B` a range. With no
  flags it prints everything (was `cat`). Replaces four tools with one verb and
  three flags.
- `count` — count lines, words, characters, or bytes, selected by
  `--lines`, `--words`, `--chars`, `--bytes`. Replaces `wc`.
- `sort` — sort lines. `--reverse`, `--numeric`, `--unique` (folding in `uniq`),
  `--ignore-case`.
- `field` — select or reorder columns by delimiter. Replaces `cut` and `paste`
  (join is `field` with a join mode, not a separate verb).
- `compare left right` — show differences. Replaces `diff` and `cmp`.
- `identify path` — report content type. Replaces `file`.

### Search and transform

- `search pattern [files…]` — print matching lines. `--ignore-case`,
  `--invert`, `--count`, `--recursive`, `--fixed` (literal, replacing `fgrep`),
  `--extended` (replacing `egrep`). One verb, five flags, three tools gone.
- `replace pattern replacement [files…]` — substitute text. Replaces `sed`'s
  `s///` and `tr`.
- `transform program [files…]` — field-based computation, the structured-text
  escape hatch that `awk` currently occupies. `awk` is a small language bolted
  onto a filter; `transform` keeps the idea but the name says what it is.

### Processes

- `processes` — list processes. Replaces `ps`.
- `signal pid` — send a signal, `--force` for `SIGKILL`. Replaces `kill` and
  `killall`.
- `monitor` — live process view. Replaces `top`.

### System and environment

- `system` — machine identity. Replaces `uname`.
- `user` — current user and groups. Replaces `whoami` and `id`.
- `host` — host name. Replaces `hostname`.
- `time` — current date and time. Replaces `date`.
- `environment` — read or set variables. Replaces `env` and `export`.
- `echo`, `help` — `help` replaces `man` and `apropos`.

### Disk

- `usage path` — space used by a path. Replaces `du`.
- `space` — free space on filesystems. Replaces `df`.

### Network

- `fetch url` — transfer over HTTP(S). Replaces `curl` and `wget` (one verb;
  `curl`'s three dozen flags collapse into a handful).
- `connect host` — remote shell. Replaces `ssh`.
- `send local remote` — copy over SSH. Replaces `scp`.
- `reach host` — connectivity probe. Replaces `ping`.

### Archive and compression

- `archive path` — bundle files. `--create`, `--extract`, `--list` replace the
  tar subcommands *and* the zip/unzip split. Compression is `--compress`, but
  it calls a separate tool rather than doing two jobs.
- `compress path` / `expand path` — compress and decompress. Replaces `gzip`,
  `gunzip`, `zip`, `unzip` with a single symmetric pair.

## Old to new

| today | becomes | note |
|-------|---------|------|
| `ls -la` | `list --long --all` | |
| `cd` | `go` | |
| `pwd` | `where` | |
| `cp -r` / `rm -rf` | `copy --recursive` / `remove --recursive --force` | |
| `mkdir` / `touch` | `create --directory` / `create` | |
| `stat` | `info` | |
| `cat` / `head -n` / `tail -n` | `read` / `read --lines N` / `read --from N` | |
| `wc -l` | `count --lines` | |
| `sort -u` | `sort --unique` | |
| `cut` / `paste` | `field` | |
| `diff` | `compare` | |
| `grep -ri` | `search --recursive --ignore-case` | |
| `sed 's/x/y/'` / `tr` | `replace x y` | |
| `awk` | `transform` | |
| `ps` / `kill -9` | `processes` / `signal --force` | |
| `uname -a` / `whoami` | `system` / `user` | |
| `date` / `env` | `time` / `environment` | |
| `du -sh` / `df -h` | `usage --human` / `space --human` | |
| `curl` / `wget` | `fetch` | |
| `tar czf` / `unzip` | `archive --create --compress` / `archive --extract` | |
| `gzip` / `gunzip` | `compress` / `expand` | |

## What PowerShell and Nushell got right and wrong

PowerShell's contribution is its **noun-verb naming** (`Get-Content`,
`Get-ChildItem`) and its **object pipeline**: commands pass .NET objects, not
text, so there is no parsing step to get wrong. That is the right instinct for
legibility, and this design borrows it in spirit. But PowerShell's names are
verbose to the point of noise for an LLM, its common parameters
(`-ErrorAction`, `-WhatIf`) are a separate vocabulary bolted on, and it
inherits the very same overlapping commands under new names.

Nushell's contribution is **typed, structured output**: `ls` returns a table,
and pipelines carry records that later commands can select and sort by field
name rather than by column position. That is the single most important idea
for LLM legibility, and a real implementation of this proposal would adopt it:
`list`, `processes`, and `search` should emit structured records by default,
with `--json` for serialization and a plain-text rendering only for humans.
Nushell's mistake is keeping the legacy command names (`ls`, `cd`, `rm`) and
their inherited flags, so the structure is clean but the surface is not.

This design is the synthesis: PowerShell's one-verb discipline, Nushell's
structured output, and neither system's legacy baggage.

## What this does not solve

The proposal deliberately stays at the level of naming, flags, and
responsibilities. It does not define a new shell grammar, decide how pipelines
carry structured data between `transform` and `search`, or specify how a tool
declares its schema so an LLM can discover it. Those are the hard parts—the
kind that turn a blog post into a project—and they are exactly the parts a
working system would have to get right. If you want the whole thing, that is
the book, and like everything else worth writing, it is still on the shelf.
