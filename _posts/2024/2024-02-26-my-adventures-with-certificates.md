---
title: "My Adventures with Certificates"
date: 2024-02-26
year: 2024
---

> Update: thanks to the generosity of [Matt Panaro][panaro-matt],
> I now have [a working example][https-example].
> I don't fully understand it yet,
> but it runs on Ubuntu and macOS.

I'm putting together a tutorial on safe computing for data scientists.
As part of that,
I want to show learners how HTTPS actually works:
I hope most of them will never have to manage this stuff on their own,
but going through a couple of exercises will give them a better understanding of
what the terms mean.

It's been more than two decades since I touched this stuff,
so I'm basically (re-)learning it from scratch myself.
What I've found so far is:

1.  Three quarters of the articles returned by online searches
    are cribbed from each other.
    They present exactly the same examples,
    in exactly the same order,
    with (almost) exactly the same prose around them.
    I knew things were getting bad,
    but I hadn't realized it was *this* bad.

2.  The material that doesn't fall into category #1
    is riddled with circular dependencies.
    In order to do X, you must understand Y,
    but Y requires an understanding of Z,
    which in turn depends on X
    (and W, and μυστήριο, and the fine structure constant, and…).
    I knew going into this that public key infrastructure was riddled with
    [inessential weirdness][inessential],
    but saints and their mercies,
    this stuff makes Git and Emacs look elegant.

Here's where I got to yesterday.
First,
I ran `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 1000 -nodes`
to create a self-signed certificate and key file in `cert.pem` and `key.pem` respectively.
(Note: I may be using all of this terminology incorrectly—that's part of my struggle.)

Second,
I used Python's `http.server` module and a few other bits and pieces
to create a simple file server that I can run on my laptop.
I tested the part that serves files *without* HTTPS and it works as expected.
To get it to serve over HTTPS, I do this:

```py
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import ssl
import sys

if __name__ == "__main__":
    server_address = ("", 1443)
    sandbox = sys.argv[1]
    certfile = sys.argv[2]
    keyfile = sys.argv[3]

    # Move into working directory to serve files from.
    os.chdir(sandbox)

    # Use the certificate and key files for secure connections.
    # If check_hostname is True, only the hostname that matches the certificate
    # will be accepted.
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.check_hostname = False
    ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)

    # Now serve files.
    server = HTTPServer(server_address, RequestHandler)
    server.socket = ssl_context.wrap_socket(server.socket, server_side=True)
    print(f"serving at {server_address} in {os.getcwd()}...")
    server.serve_forever()
```

If I put `cert.pem` and `key.pem` in a directory called `site` along with a file `test.txt`
and then run my Python program using `python file_server_secure.py site cert.pem key.pem`,
I can point my browser at `https://localhost:1443/test.txt`.
The browser complains that I'm doing something unsafe,
but once I tell it to trust the certificate
it displays the content of `test.txt` as desired.

Now for the hard part.
I want to connect to this server using the `requests` module.
My first attempt is `requests.get("https://localhost:1443/test.txt")`,
which produces:

```
ERROR: HTTPSConnectionPool(host='localhost', port=1443):
Max retries exceeded with url: /test.txt
(Caused by SSLError(SSLCertVerificationError(1,
'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:1000)')))
```

OK, that's fair:
`requests` shouldn't trust my self-signed certificate unless I tell it to.
I can turn off checking entirely by passing `verify=False` to `requests.get`,
but I'm not going to teach people to do that.
Instead,
I try this:

```py
requests.get("https://localhost:1443/test.txt", verify="cert.pem")
```

which gives me a different error:

```
ERROR: HTTPSConnectionPool(host='localhost', port=1443):
Max retries exceeded with url: /test.txt
(Caused by SSLError(SSLCertVerificationError(1,
"[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:
Hostname mismatch, certificate is not valid for 'localhost'. (_ssl.c:1000)")))
```

A bit of poking around leads me to the [`certifi`][certifi] module;
calling `certifi.where()` gives me:

```
/Users/gvwilson/anaconda3/envs/safety/lib/python3.12/site-packages/certifi/cacert.pem
```

That `cacert.pem` contains 147 trusted certificates, so…
I'm not quite how to finish that sentence.
What should someone who's working through their first tutorial on PKI do at this point?

1.  Append their `cert.pem` file to `certifi`'s global `cacert.pem`?
    That feels like an accident waiting to happen (and not waiting patiently).

2.  Or is there a way for learners (and me) to sign our own certificates
    using one of the certificates in `cacert.pem`
    so that `requests` will trust it?
    That also feels unsafe:
    what's to stop me generating and signing certificates that claim to belong to
    the Government of Canada?

3.  What about having learners create their own certificate authority?
    Some of what I'm reading online seems to suggest that,
    and [Stefan Arentz][arentz-stefan] kindly pointed me at [this article][cloudflare],
    but it feels like a lot of work and confusion
    for what's meant to be one 10-minute exercise in a day-long tutorial.

What's the best answer?
Remember,
I'm not trying to set up public key infrastructure for a real site:
I'm trying to give first-timers a feeling for what's involved in doing that.
If you have taught these concepts,
what did you do and how well did it work?
Please add thoughts and comments to [this GitHub issue][issue],
and thank you in advance.

[arentz-stefan]: https://www.linkedin.com/in/stefanarentz/
[certifi]: https://pypi.org/project/certifi/
[cloudflare]: https://technedigitale.com/archives/639
[https-example]: https://github.com/gvwilson/https_example
[inessential]: https://www.harihareswara.net/posts/2014/inessential-weirdnesses-in-open-source/
[issue]: https://github.com/gvwilson/sys-tutorial/issues/7
[panaro-matt]: https://github.com/panarom
