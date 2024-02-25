---
title: "Community Norms"
date: 2024-02-25
year: 2024
---

I just wrapped up [a poll on Mastodon][mastodon-poll];
since I don't know how long it will persist there,
I'm saving the question and the results for future use.

<blockquote>
<p>
Q: team A creates a package called XYZ on PyPI.
It only has a few users, but it <em>is</em> used and under active development.
Team B shows up and wants to use the same name.
They called their package XYZ-toolkit, but when installed it creates a module called XYZ,
so people can't use it and the original in the same project without low-level manual grief.
Team B is aware of the conflict, but has many more users and isn't willing to change name.
Has Team B:
</p>

<table>
  <tr><td>broken an actual rule (if so, which one)</td><td align="right"> 7%</td></tr>
  <tr><td>violated community norms but not broken a rule</td><td align="right">80%</td></tr>
  <tr><td>neither of the above</td><td align="right">12%</td></tr>
  <tr><td>total respondents</td><td align="right">137</td></tr>
</table>
</blockquote>

Now that the poll is over,
the packages in question are [Ibis][pypi-ibis] (first released October 20, 2014)
and [the Ibis Framework][pypi-ibis-framework] (July 20, 2015).
I tripped over this because [the static site generator][ark] I use to produce my books
relies on the original Ibis,
and installing Ibis-for-dataframes in the same environment to use in a lesson broke my build.
It's the first time I've run into something like this in the 25 years I've been using Python.

[ark]: https://www.dmulholl.com/docs/ark/main/
[mastodon-poll]: https://mastodon.social/deck/@gvwilson/111974909759293702
[pypi-ibis]: https://pypi.org/project/ibis/
[pypi-ibis-framework]: https://pypi.org/project/ibis-framework/
