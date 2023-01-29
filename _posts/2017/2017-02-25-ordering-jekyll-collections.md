---
title: "Ordering Jekyll Collections"
date: 2017-02-25 05:00:00
year: 2017
---

Short version: I am offering a US$100 bounty for an implementation of
[ordering for Jekyll collections](https://github.com/jekyll/jekyll/issues/5754).
To qualify, an implementation must be an addition to Jekyll core,
not an extension or plugin.

Long version:

1.  [Jekyll](http://jekyllrb.com/) is a Ruby tool that creates static websites
    from HTML or Markdown source.

1.  A [collection](https://jekyllrb.com/docs/collections/) is a group of files
    that belong together, such as the individual tutorials making up a lesson.

1.  Jekyll orders the elements of collections alphabetically, so if someone
    wants to enforce a particular order, they have to use a naming scheme
    like `01-alpha.md`, `02-beta.md`, and so on.

1.  As a result, when authors want to re-order topics, they need to rename many files
    whose content often hasn't changed, which makes the version control log difficult
    to interpret.  They may also have to update internal links, since `/01-alpha/`
    may become `/02-alpha/`.

1.  It's possible to add a list to Jekyll's `_config.yml` configuration file to specify order:

    ~~~
    topic_order:
      - '/intro'
      - '/setup'
      - '/filter'
    ~~~

    and then using that loop and where to create the ordered list in the home page:

    ~~~
    {% raw %}<ul>{% endraw %}
    {% raw %}{% for ident in site.topic_order %}{% endraw %}
      {% raw %}{% assign topic = site.topics | where: "id", ident | first %}{% endraw %}
      {% raw %}<a href="{{topic.url}}">{{topic.title}}</a>{% endraw %}
      {% raw %}<li>{% endraw %}
    {% raw %}{% endfor %}{% endraw %}
    {% raw %}</ul>{% endraw %}
    ~~~

    However, his doesn't generate previous/next links to connect the topics.
    This can be done using a search loop inside each topic to find it within the `site.topics` list,
    but that means that building the site is O(N**2), since the search loop over N topics
    is run once for each topic.  That makes builds slow for large collections
    (e.g., 100 items).

1.  It would be straightforward to create a Ruby plugin for Jekyll that
    took care of this, but GitHub only runs stock Jekyll when generating
    GitHub Pages sites.

I would therefore like the following:

1.  Support an `order` key in the `_config.yml` metadata for each collection,
    whose value is the ordered list of IDs of collection members.
    Values in the list that don't correspond to collection members are errors;
    collection members that are not listed are an error, omitted, or added to
    the end of the collection in alphabetical order, depending on the value of
    a `missing` key in the collection metadata.

1.  Set previous and next links in the page for each collection item
    to respect this ordering.

I will pay US$100 for an implementation of this feature.  To qualify, work
must be submitted as a PR against the [Jekyll repository](https://github.com/jekyll/jekyll/)
on GitHub, and must include enough unit tests to satisfy Jekyll's maintainers.
The PR does *not* have to be merged in order to qualify (since that is
out of the author's control).  If you are interested, please
[email me](mailto:{{site.author.email}}) a few sentences describing how
you would deal with missing collection items.
