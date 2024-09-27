---
title: "For Each, Replace"
date: 2008-05-23
---
My greatest weakness as a programmer (other than impatience) is how little I know about relational databases. I know how it happened—I spent my twenties working in high-performance scientific computing, before very large scientific databases became common, and there was always somebody else to worry about that side of things for the projects I was on in my thirties—but it trips me up with ever-increasing frequency.

So, having told my students many times not to be ashamed of not knowing things, I figure I should set a good example and parade my own ignorance in public. The entries in this blog are stored in a PostgreSQL database as chunks of text. I've discovered that different entries represent characters in different ways: the long dash, for example, is usually a triple dash "—", but is also sometimes represented as either a two-byte or three-byte sequence (depending, I presume, on what machine I was on the day I wrote the entry—I sometimes compose in a regular editor, then paste the entry into the blog). I'd like to clean up these inconsistencies, which means doing search/replace on approximately 1450 database entries. As I see it, my options are:
<ol>
  <li>Write a shell script that uses the command-line PostgreSQL client to pull entries in turn, run them through sed(1), and push the results back into the database.</li>
  <li>Write a Python script that connects to the database, pulls the entries, does string substitution, and pushes the results.</li>
  <li>Learn a little more SQL and do this with a query of some kind.</li>
</ol>
#3 is where I'm stuck. I know how to find the offending entries: "select entry from table where  entry like chars". I even think I know how to do string substitution. My question is, how do I push the results back into the table? I clearly want to replace each entry with the update of itself; is there a way to do this, or do I insert a new bunch of rows into the table, then delete the old rows? How? And why?
