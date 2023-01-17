---
layout: page
title: Favorites
permalink: "/favorites/"
---

<table>
  {% for post in site.posts %}
  {% if post.favorite %}
  <tr><td>{{ post.date | date: "%Y-%m-%d" }}</td><td><a href="{{ post.url | relative_url }}">{{ post.title }}</a></td></tr>
  {% endif %}
  {% endfor %}
</table>
