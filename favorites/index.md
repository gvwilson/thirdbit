---
layout: page
title: Favorites
---

<div class="posts">
  {% for post in site.posts %}
  {% if post.favorite %}
  <h4><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h4>
  <time datetime="{{ post.date | date_to_xmlschema }}" class="post-date">{{ post.date | date: "%Y-%m-%d" }}</time>
  {% endif %}
  {% endfor %}
</div>
