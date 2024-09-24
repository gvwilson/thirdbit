---
title: "Who Are We?"
date: 2014-12-15
original: swc
---
<p>
  For the last three years,
  I've been storing information about instructors, workshops, and other things
  in a small SQLite database
  so that I can look things up and generate statistics when I need to.
  I can't publish it,
  since it contains personal identifying information,
  but since I had to write a script to migrate the data to
  the tool we're building to manage workshops,
  it only took another few minutes to create a partly-redacted version of the data.
  ("Partly" because someone who was really keen could work backward workshop URLs to instructors' names,
  cross-reference,
  and recover the names of some fraction of our instructors.
  Since that information is all public anyway,
  though,
  I don't think I've introduced any new risks.)
</p>
<p>
  The SQL source for the database is here;
  with it,
  you can regenerate the database using:
</p>

```
$ sqlite3 swc.db < swc-db-2014-12-14.sql
```

<p>
  You can then ask lots of questions–some examples are included below.
  If you'd like a little end-of-year procrastination,
  what else can you find in this data that's interesting?
</p>
<pre>
-- How many sites have had how many events?  
select count(*), c
from (select count(*) as c
      from site join event
      on site.id=event.site_id
      group by site.id)
group by c
order by c desc;
</pre>
<table class="centered">
<tr><th>number</th>
<th>count</th>
</tr>
<tr><td>2</td>
<td>8</td>
</tr>
<tr><td>2</td>
<td>7</td>
</tr>
<tr><td>2</td>
<td>6</td>
</tr>
<tr><td>3</td>
<td>5</td>
</tr>
<tr><td>4</td>
<td>4</td>
</tr>
<tr><td>8</td>
<td>3</td>
</tr>
<tr><td>36</td>
<td>2</td>
</tr>
<tr><td>117</td>
<td>1</td>
</tr>
<tr><td></td>
</tr>
</table>

```
-- How many people have taught?
select count(distinct person_id)
from person join task join role
on person.id=task.person_id and task.role_id=role.id
where role.name='instructor';
```

<table class="centered">
<tr><th>number</th>
</tr>
<tr><td>281</td>
</tr>
</table>

```
-- How many people started as learners or helpers and became instructors?
```

<table class="centered">
<tr><th>number</th>
</tr>
<tr><td>123</td>
</tr>
</table>

```
-- How often have people taught?
from (select count(*) as c
      from person join task join role
      on person.id=task.person_id and task.role_id=role.id
      where role.name='instructor'
      group by person_id)
group by c
order by c desc;
```

<table class="centered">
<tr><th># instructors</th>
<th># workshops</th>
</tr>
<tr><td>1</td>
<td>43</td>
</tr>
<tr><td>1</td>
<td>14</td>
</tr>
<tr><td>3</td>
<td>12</td>
</tr>
<tr><td>2</td>
<td>11</td>
</tr>
<tr><td>2</td>
<td>10</td>
</tr>
<tr><td>5</td>
<td>9</td>
</tr>
<tr><td>5</td>
<td>8</td>
</tr>
<tr><td>4</td>
<td>7</td>
</tr>
<tr><td>5</td>
<td>6</td>
</tr>
<tr><td>16</td>
<td>5</td>
</tr>
<tr><td>17</td>
<td>4</td>
</tr>
<tr><td>32</td>
<td>3</td>
</tr>
<tr><td>50</td>
<td>2</td>
</tr>
<tr><td>138</td>
<td>1</td>
</tr>
</table>

```
-- How has each training cohort done?
select cohort.name, count(*), round((100.0 * sum(trainee.complete)) / count(*), 1)
from trainee join cohort
on trainee.cohort_id=cohort.id
where cohort.qualifies
group by cohort_id;
```

<table class="centered">
<tr><th>name</th>
<th>enrolled</th>
<th>completion %age</th>
</tr>
<tr><td>2012-08-26-online</td>
<td>20</td>
<td>55.0</td>
</tr>
<tr><td>2012-10-11-online</td>
<td>25</td>
<td>44.0</td>
</tr>
<tr><td>2013-01-06-online</td>
<td>12</td>
<td>16.7</td>
</tr>
<tr><td>2013-03-12-online</td>
<td>27</td>
<td>48.1</td>
</tr>
<tr><td>2013-05-12-online</td>
<td>45</td>
<td>26.7</td>
</tr>
<tr><td>2013-08-12-online</td>
<td>41</td>
<td>43.9</td>
</tr>
<tr><td>2013-09-30-online</td>
<td>57</td>
<td>31.6</td>
</tr>
<tr><td>2014-01-16-online</td>
<td>67</td>
<td>22.4</td>
</tr>
<tr><td>2014-04-24-online</td>
<td>58</td>
<td>31.0</td>
</tr>
<tr><td>2014-04-28-mozilla</td>
<td>43</td>
<td>65.1</td>
</tr>
<tr><td>2014-06-05-online</td>
<td>29</td>
<td>10.3</td>
</tr>
<tr><td>2014-06-11-online</td>
<td>59</td>
<td>27.1</td>
</tr>
<tr><td>2014-09-10-online</td>
<td>81</td>
<td>29.6</td>
</tr>
<tr><td>2014-09-22-uva</td>
<td>31</td>
<td>22.6</td>
</tr>
<tr><td>2014-10-22-tgac</td>
<td>41</td>
<td>26.8</td>
</tr>
<tr><td>2014-11-12-washington</td>
<td>20</td>
<td></td>
</tr>
<tr><td>2015-01-01-online</td>
<td>135</td>
<td></td>
</tr>
<tr><td>2015-01-06-ucdavis</td>
<td>4</td>
<td></td>
</tr>
<tr><td>2015-05-01-online</td>
<td>113</td>
<td></td>
</tr>
</table>
