---
title: "IO for Software Design"
date: 2026-09-20
category: education technical-writing
---
Last winter I wrote [a discrete event simulation framework][asimpy] in Python
to keep myself busy,
have something to put on my CV,
experiment with LLM-assisted coding,
and learn how `async` and `await` actually work.
Over the summer,
for similar reasons,
I played around a bit with [Lean][lean] and [Gleam][gleam],
thinking that I might translate the *Software Design by Example* books
from [JavaScript][sdxjs] and [Python][sdxpy] into one or the other.
Lean defeated me,
and I quickly grew frustrated with the gaps in Gleam's standard library,
but my noodling around left me wanting to learn more about formal verification of programs.

After poking around a bit I decided to give [Dafny][dafny] a try,
only to find that its standard library has gaps too.
Depending on whether or not I'm able to [find work][unemployed],
I might try to recruit some undergrads to fill those in.
What follows is a spec for what I would need them to build
in order to be able to replicate the examples in the existing books.

In brief:
Dafny's standard library provides only whole-file I/O (`Std.FileIO`) and JSON (`Std.JSON`).
`Std.FileIO` reads or writes an entire file in a single call;
there are no functions to open and close file handles and no streaming reads.
It also has no networking, hashing, SQLite, CSV/YAML, temporary-file, or path-manipulation support.

-   Standard streams
    -   `sys.stdin`: missing
    -   `sys.stdout` exists (kind of: `print` writes to standard output)
    -   `sys.stderr`: missing
-   File operations
    -   `open(path, mode)` with text and binary modes (`"r"`, `"w"`, `"rb"`): missing
    -   `file.close()`: (obviously) also missing
    -   `file.read()` to read a whole file exists:
	    `Std.FileIO.ReadUTF8FromFile` (text) or `Std.FileIO.ReadBytesFromFile` (bytes)
    -   `file.read(n)` to read fixed-size blocks: missing
    -   `file.readlines()` to read content as lines: missing
    -   `file.write(text)` to save data to file exists:
        `Std.FileIO.WriteUTF8ToFile` (text) or `Std.FileIO.WriteBytesToFile` (bytes)
-   Path manipulation
    -   `Path(...)` (string to path): missing (paths are plain `string`s passed to `Std.FileIO`)
    -   `Path.read_text()`: use `Std.FileIO.ReadUTF8FromFile`
    -   `Path.write_text()`: use `Std.FileIO.WriteUTF8ToFile`
    -   `Path.mkdir()` (including `parents=True, exist_ok=True`):
        partial: `Std.FileIO.WriteUTF8ToFile`/`WriteBytesToFile` create nonexistent parent directories,
        but there is no standalone `mkdir`
    -   missing: `Path.cwd()`,  `Path.joinpath()`,  `Path.parent`,  `Path.stem`,  `Path.suffix`,  `Path.name`,  `Path.exists()`,  `Path.is_file()`,  `Path.touch()`,  `Path.unlink()`,  `Path.rmdir()`,  `Path.rename()`,  `Path.iterdir()`,  `Path.glob()` / `Path.rglob()`, 
-   Temporary files and directories
    -   `tempfile.TemporaryDirectory()`: missing
    -   `tempfile.NamedTemporaryFile(...)`: missing
-   JSON
    -   `json.load()` exists: `Std.JSON.API.Deserialize` (from `seq<byte>`, not from a file or string)
    -   `json.dump()` exists: `Std.JSON.API.Serialize` (to `seq<byte>`; `SerializeAlloc` returns an `array<byte>`)
-   CSV
    -   `csv.reader()` missing
    -   `csv.writerow()` missing
    -   `csv.writerows()` missing
    -   `csv.DictReader()` missing
-   YAML
    -   `yaml.load()`: missing
-   Binary records
    -   `struct.pack()`: missing
    -   `struct.unpack()`: missing
    -   `struct.calcsize()`: missing
-   Hashing
    -   `hashlib.sha256().hexdigest()`: missing (the standard library has `Std.Base64`, but no SHA/MD5)
    -   `hashlib.md5()` with `.update()` for streaming hash: missing
-   SQLite
    -   `sqlite3.connect()`: missing
    -   `connection.execute()`: missing
    -   `connection.fetchall()`: missing
    -   `connection.commit()`: missing
-   TCP sockets
    -   `socket.socket()`: missing
    -   `socket.gethostbyname()`: missing
	-   Missing from client side: `.connect()`, `.send()`, `.sendall()`, `.recv()`, `.close()`
	-   Missing from server side: `.bind()`, `.listen()`, `.accept()`, `.recv()`, `.send()`, `.close()`
-   TCP server framework
    -   A way to create a TCP server (e.g., a base class)
	-   And then `self.request.recv()`, `self.request.sendall()`, `self.client_address`, `server.serve_forever()`
-   HTTP server
    -   A way to create an HTTP server
    -   And then `do_GET()` (with `self.path` and `self.command`), `self.send_response()`, `self.send_header()`, `self.end_headers()`, `self.wfile.write(body)`, `HTTPStatus` enum
-   HTTP client
    -   `requests.get()` (or a similar workhorse) with `req.add_header()`
    -   And then a response with `.status_code`, `.headers[]`, `.text`, `.read()`

[asimpy]: https://gvwilson.github.io/asimpy/
[dafny]: https://dafny.org/
[gleam]: https://gleam.run/
[lean]: https://lean-lang.org/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
[unemployed]: @root/2026/09/08/looking-for-work/
