---
title: "Creating Tables in DrProject"
date: 2007-01-18
---
Courtesy of David Scannell, here's a quick rundown of how to create a new table in DrProject's database.  (Yes, I know, we should convert to <a href="http://www.sqlobject.org/">SQLObject</a> or <a href="http://www.sqlalchemy.org/">SQLAlchemy</a>; if you have time to do the work, please let me know…)

Suppose I want to create a table called <code>Demo</code> with three fields:
<ul>
  <li><code>Named</code>: string</li>
  <li><code>ID</code>: integer (primary key)</li>
  <li><code>TicketID</code>: Integer (foreign key)</li>
</ul>
We'll assume that all work is being done in a <code>drproject/demo</code> directory, that you have <code>__init__.py</code> set up, and you have modified <code>setup.py</code> file to recognize the new package.
<h2>Step 1: Create the Model</h2>
A. Create a file call <code>model.py</code>.

B. Import the following:
<pre>from drproject.db.record import *         # Base for all database modelling</pre>
<pre>from drproject.ticket.model import Ticket # Because we want a foreign key</pre>
C. Create a new subclass for record.
<pre>Class Demo(Record):</pre>
D. Associated this model with a database table (by default the table it gets associated with is the same as the name of the class):
<pre>Class Demo(Record):   _table='demo_table'</pre>
E. Now add the columns to the table:
<pre>Class Demo(Record):</pre>
<pre>_table='demo_table'</pre>
<pre>id = IdColumn()                # Creates a self-incrementing id</pre>
<pre>name = TextColumn()            # String column</pre>
<pre>ticket_id = ForeignKey(Ticket) # Makes this a foreign key to the Ticket Table</pre>
F. Make the ID column our primary key:
<pre>Class Demo(Record):</pre>
<pre>_table='demo_table'</pre>
<pre>id = IdColumn()</pre>
<pre>name = TextColumn()</pre>
<pre>ticket_id = ForeignKey(Ticket)</pre>
<pre>_key = (id,)</pre>
Done.
<h2>Step 2: Create the System</h2>
A. Create a file called <code>api.py</code>.

B. Import the following:
<pre>from drproject.core import *</pre>
<pre>from drproject.env import EnvironmentSetupParticipant # For database creation</pre>
<pre>from drproject.demo.model import *                    # Our database model</pre>
C. Create our <code>EnviromentSetupParticipant</code> subclass.
<pre>Class DemoSystem(EnvironmentSetupParticipant):</pre>
D. Associate the table that this new system will work with. In our case, it is the demo table.
<pre>Class DemoSystem(EnvironmentSetupParticipant):</pre>
<pre>database_tables = (Demo,)</pre>
E. Give our system a name and version number:
<pre>Class DemoSystem(EnvironmentSetupParticipant):</pre>
<pre>database_tables = (Demo,)</pre>
<pre>version_propery = 'demo_system'</pre>
<pre>version = 1</pre>
Done.
<h2>Step 3: Finishing Off</h2>
Now, when we create a new environment, DrProject will go over all the <code>EnvironmentSetupParticipant</code> objects, and create all the database tables each one is associated with. Process occurs in the method <code>__init__</code> of the class <code>Environment</code> in the file <code>drproject/env.py</code>.
