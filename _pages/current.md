---
permalink: /current/
title: "Current Activities"
layout: single
---

<h2>Projects</h2>

<p class="paper-details">
{% for p in site.projects %}
<strong><a href="{{p.url}}">{{p.title}}</a></strong>: {{p.details}}
{% unless forloop.last %}<br/>{% endunless %}
{% endfor %}
</p>

<h2>Writing</h2>

<div align="center">
<p>
  {% for b in site.books %}
  <a href="{{b.url}}"><img src="{{b.cover | prepend: '/files/' | relative_url}}" alt="{{b.title}}" class="book-cover" /></a>
  {% endfor %}
</p>
</div>

<p class="paper-details">
{% for p in site.papers %}
{{p.authors}}: "<a href="{{p.url}}">{{p.title}}</a>"
{% unless forloop.last %}<br/>{% endunless %}
{% endfor %}
</p>
