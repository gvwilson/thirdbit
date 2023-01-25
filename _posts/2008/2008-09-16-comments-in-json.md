---
title: "Comments in JSON?"
date: 2008-09-16 08:09:30
year: 2008
---
Some of my students have discovered that JSON doesn't support comments—they're not in the syntax diagram on the <a href="http://www.json.org">json.org</a> home page or <a href="http://www.ietf.org/rfc/rfc4627.txt?number=4627">the RFC</a>, and various <a href="http://bytes.com/forum/thread641975.html">discussion threads</a> bemoan their absence.  We'd like to use JSON both for data interchange and for specifying test fixtures; we could live without comments for the former if we had to, but it's a real pain to (for example) have the encrypted version of a password in a test fixture, but not the plaintext password it was derived from.  One possibility is to add a "comment" field to every data type that needs commenting (e.g., the dictionary that represents a User object would have "comment" as one of its keys), but then the mapping from JSON to object or database entry is no longer 1-1.  How are other people dealing with this?
