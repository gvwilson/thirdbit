---
title: "Software Design by Example 5: File Backup"
date: 2023-01-05
year: 2023
---

The chapter explaining [how hash-based version control systems work][sdxjs_file_backup]
was one of the three starting points for this book.
The others were [how a browser lays out a page][sdxjs_layout_engine] and [how a debugger works][sdxjs_debugger];
I tackled this one first because of [Mary Rose Cook's][cook_mary_rose] excellent [Gitlet][gitlet] project,
though if I'd known about Panchekha and Harrelson's equally inspiring [*Browser Engineering*][browser_engineering]
I might have begun with the layout engine.
(I *wish* that starting with the debugger example had been an option,
but I've been [complaining][not_on_the_shelves] for 25 years about the fact that
nobody has ever written a good book on the subject.)

By the time it was done,
this chapter introduced two of the most important ideas in practical computing:
hashing and mock objects.
The former struck me as magical when I first encountered it—how could
a deterministic algorithm possibly produce output that was indistinguishable from random noise?
And how could randomness be so useful?
As for mock objects,
my first languages were Fortran, Pascal, C, Occam, and C++ in that order.
Dynamic introspection wasn't available in any of them;
the closest I came to it before learning Java in the late 1990s
was using function pointers and virtual methods,
but neither made me feel like my program was making itself up as it went along.

The running example in this chapter does far less than Git, Mercurial, or their siblings.
In particular it doesn't allow for branching and merging,
whose design deserve a chapter of their own.
I also think a lot could be learned from comparing a Git-inspired tool like this one
with a system inspired by [Fossil][fossil],
in the same way that comparing the implementation of undo/redo in Emacs and Vim
can show just how large the space of possible designs actually is.

<figure id="file-backup-storage">
  <img src="{{'/sdxjs/file-backup/storage.svg' | relative_url}}" alt="Backup file storage"/>
  <figcaption markdown="1">Figure 5.3: Organization of backup file storage.</figcaption>
</figure>

> Terms defined: Application Programming Interface, collision, comma-separated values, Coordinated Universal Time, cryptographic hash function, data migration, handler, hash code, hash function, JavaScript Object Notation, mock object, pipe, race condition, SHA-1 hash, stream, streaming API, Time of check/time of use, timestamp, version control system.

[browser_engineering: https://browser.engineering/
[fossil]: https://www2.fossil-scm.org/
[not_on_the_shelves]: {{'/not-on-the-shelves/' | relative_url}}
[sdxjs_debugger]: {{'/sdxjs/debugger/' | relative_url}}
[sdxjs_file_backup]: {{'/sdxjs/file-backup/' | relative_url}}
[sdxjs_layout_engine]: {{'/sdxjs/layout-engine/' | relative_url}}
