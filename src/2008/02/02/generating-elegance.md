---
title: "Generating Elegance"
date: 2008-02-02
---
There was a moment on Friday that sums up why I like to teach.  As part of preparing for <a href="http://us.pycon.org/2008/about/">PyCon'08</a>, <a href="http://blog.codekills.net/">David Wolever</a> is tidying up DrProject's database schema.  One task is to rationalize the handling of enumerations such as ticket states: at present, these are variously represented as:
<ul>
  <li>string columns in the database;</li>
  <li>integer columns that index into tables that store the corresponding human-readable string; and</li>
  <li>integer columns that are translated into strings in the code.</li>
</ul>
The cleaned-up version is to have one table that stores all enumerated values:
<ul>
  <li>whatfor (string): name of enumeration</li>
  <li>name (string): name of enumeration elements</li>
  <li>value (string): integer value of that element (for sorting and cross-referencing)</li>
</ul>
which gives:
<table class="centered">
<tr>
<th>whatfor</th>
<th>name</th>
<th>value</th>
</tr>
<tr>
<td>'ticket_type'</td>
<td>'bug'</td>
<td>0</td>
</tr>
<tr>
<td>'ticket_type'</td>
<td>'enhancement'</td>
<td>1</td>
</tr>
<tr>
<td>'ticket_type'</td>
<td>'task'</td>
<td>2</td>
</tr>
<tr>
<td>'user_state'</td>
<td>'pending_confirmation'</td>
<td>0</td>
</tr>
<tr>
<td>'user_state'</td>
<td>'registered'</td>
<td>1</td>
</tr>
<tr>
<td>…</td>
<td>…</td>
<td>…</td>
</tr>
</table>
Using <a href="http://www.sqlalchemy.org/">SQLAlchemy</a> and <a href="http://elixir.ematia.de/trac/wiki">Elixir</a>, this schema is:
<pre>
class Enum(Entity):

    has_field('whatfor', Unicode(), primary_key = True)

    has_field('name', Unicode(), primary_key = True)

    has_field('value', Integer())

    using_options(tablename='enums', order_by=['value'])class Ticket(Entity):

    belongs_to('status', of_kind='Enum')</pre>
The problem is, we also want to define default values for the fields <code>whatfor</code> and <code>name</code> when declaring those columns.  Normally, this would be done like this:
<pre>
belongs_to(

    'status',

    of_kind='Enum',

    column_kwargs = {'default': lambda 'some_default'}

)</pre>
But that doesn't work in this case, because there are two fields in the primary key of <code>Enum</code> (and they both get assigned <code>'some_value'</code>).  In the long run, there doesn't seem to be any reason why we shouldn't be able to specify per-column settings when the primary key spans multiple fields, like this:
<pre>
belongs_to(

    'status',

    of_kind='Enum',

    per_column_kwargs = {

        'whatfor' : { 'default' : 'foo'},

        'value'   : { 'default' : 'bar'}

    }

)</pre>
But that doesn't work yet, so <a href="http://blog.codekills.net/">David</a> came up with this:
<pre>
def enum_default(whatfor, value):

    def _enum_generator(whatfor, value):

        yield whatfor

        yield value</pre>
<pre>    return _enum_generator(whatfor, value).next

belongs_to(

    'status',

    of_kind='Enum',

    column_kwargs = {

        'default': enum_default('foo', 'bar')

    }

)</pre>
It took me a moment to figure it out, but when I did, I thought it was actually rather elegant.  I wonder what I'll learn from my students next week?
