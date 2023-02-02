---
title: "REST APIs for Batch Operations"
date: 2008-09-15 14:30:21
year: 2008
---
I have a question about the "right" way to design a REST API, and am hoping someone out there on the Interweb will point me in the right direction.  The short version of the question is, "How should batch operations be structured?"  The long version goes something like this:

Suppose your web application has to keep track of fruit flies.  Each fruit fly has a unique (system-assigned) integer ID, a name (hey, even flies can be cuddly), and a genome (represented as a string of characters).  If you only had to work with one fly at a time, the API might look something like this (with the data values formatted as XML, JSON, or what have you):
<table>
<tr>
<td><strong>Operation</strong></td>
<td><strong>URL</strong></td>
<td><strong>HTTP Verb</strong></td>
<td><strong>Request Data</strong></td>
<td><strong>Response Code(s)</strong></td>
<td><strong>Response Data</strong></td>
</tr>
<tr>
<td>Find out what flies exist</td>
<td>/api/fly</td>
<td>GET</td>
<td>—</td>
<td>200</td>
<td>{id, id, …}</td>
</tr>
<tr>
<td>Get a fly's record</td>
<td>/api/fly/id</td>
<td>GET</td>
<td>—</td>
<td>200</td>
<td>{id, name, genome}</td>
</tr>
<tr>
<td>Create a fly in the database</td>
<td>/api/fly</td>
<td>POST</td>
<td>{name, genome}</td>
<td>200</td>
<td>{id}</td>
</tr>
<tr>
<td>Update a fly's record</td>
<td>/api/fly/id</td>
<td>PUT</td>
<td>{new name and/or genome}</td>
<td>200</td>
<td>{id}</td>
</tr>
<tr>
<td>Delete a fly's record</td>
<td>/api/fly/id</td>
<td>DELETE</td>
<td>—</td>
<td>200</td>
<td>{id}</td>
</tr>
</table>
I've left out error cases because they aren't relevant to my question—at least, I don't think they are.

But now suppose that you want to do batch operations, i.e., that you want to create, read, update, or delete hundreds or thousands of flies at once.  Your client (which may be a desktop application or something else that isn't a browser) can POST data for lots of flies at once, but you do <em>not</em> want to handle the set of values like this:
<pre>
result = OK

for chunk_of_data in HTTP_Request:

    start_database_transaction

    result = result and process(chunk_of_data)

    end_database_transaction

return result</pre>
The first reason you don't want to do this is that it's not atomic: if anything goes wrong partway through, you could have five hundred flies updated, and five hundred not.  The second reason is that the <code>process</code> function is actually very slow: if you call it five hundred times, there's a real risk of taking so long that the web server will time out the request.  (Note: in reality, a lot more is going on inside <code>process</code> than just a few SQL queries—files are being opened, parsed, and closed, log entries are being created, etc., so "get a faster web server" is <em>not</em> a valid solution.)

The solution I've come up with is to make batch operations fundamental to the REST API, and to define the single-fly operations in terms of them.  This leads to API entries like this:
<table>
<tr>
<td><strong>Operation</strong></td>
<td><strong>URL</strong></td>
<td><strong>HTTP Verb</strong></td>
<td><strong>Request Data</strong></td>
<td><strong>Response Code(s)</strong></td>
<td><strong>Response Data</strong></td>
</tr>
<tr>
<td>Update flies' records</td>
<td>/api/fly</td>
<td>PUT</td>
<td>{ {id_0, name_0, genome_0}, {id_1, name_1, genome_1}, …}</td>
<td>200</td>
<td>number_of_updates</td>
</tr>
</table>
with the obvious definition of a PUT to <code>/api/fly/<em>id</em></code> as a multi-fly PUT with only one fly.

This doesn't feel right, but I'm not sure where I've gone wrong.  My performance constraints (i.e., the need to support batch operations) isn't going to go away, but the whole point of REST seems to be a fundamental one-to-one mapping between URLs and entities, which the batch API seems to violate.  So, how do other people (or APIs) do this?  And why?
