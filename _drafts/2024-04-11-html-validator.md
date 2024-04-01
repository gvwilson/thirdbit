---
title: "Software Design by Example in Python 11: An HTML Validator"
date: 2024-04-11
year: 2024
---

[This book][sdxpy] teaches software design by building scale models of tools that programmers actually use.
It therefore seemed fitting to spend a chapter on a tool that I built for the book itself:
one that compares the structure of its HTML pages
to a specification of what elements are allowed and what attributes they can have.
I've written several such tools over the years
to check the output of various [static site generators][ssg].
Each time,
I've wished that I had started earlier and been more thorough,
both so that the generated pages actually match the CSS I've created for them
and so that HTML-to-LaTeX conversion will work correctly.

This chapter was also an opportunity to introduce the Visitor pattern.
It comes up several times later on,
but so much else is going on in each of those examples
that explaining visitors would push the content over the one-hour limit.
Once again I was struck by how much instructional design has in common with writing fiction:
if you want something ready for Act 3,
you need to figure out how to introduce it in Act 1 or Act 2
without being too obvious.

<img class="centered" src="{{'/sdxpy/check/concept_map.svg' | relative_url}}" alt="Concept map for an HTML validator"/>

> Terms defined: attribute, child (in a tree), closing tag, DOM, DOM tree, element (in HTML), HTML, node, opening tag, self-closing tag, tag (in HTML), tree, Visitor pattern.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[sdxpy]: {{'/sdxpy/' | relative_url}}
[ssg]: https://en.wikipedia.org/wiki/Static_site_generator
