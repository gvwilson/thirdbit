---
title: "Software Design by Example in Python 12: A Template Expander"
date: 2024-04-12
year: 2024
---

When I was [outlining the content][outline] for [*Software Design by Example*][sdxpy],
there were two natural follow-ons to [the HTML checker][sdxpy_check].
One was a [template expander][sdxpy_template] of the sort used in static site generators
like the one that created the page you'r reading right now.
I chose to tackle it first because it calls back to
[the simple interpreter][sdxpy_interp] built earlier
with its variables, loops, and conditionals.
As this chapter says,
there are basically three approaches to HTML templating:

> 1.  Mix commands in an existing language such as JavaScript with the HTML or Markdown
>     using some kind of marker to indicate which parts are commands
>     and which parts are to be taken as-is.
>
> 2.  Create a mini-language with its own commands like Jekyll.
>     Mini-languages are appealing because they are smaller and safer than general-purpose languages,
>     but eventually they acquire most of the features of a general-purpose language.
>
> 3.  Put directives in specially-named attributes in the HTML.
>     This approach is the least popular,
>     but it eliminates the need for a special parser.

I chose #3 to avoid having to write, test, debug, and explain another parser.
The resulting syntax isn't something I'd want to use:

```
<ul z-loop="item:names">
  <li><span z-var="item"/></li>
</ul>
```

but it does the job well enough.

<img class="centered" src="{{'/sdxpy/template/concept_map.svg' | relative_url}}" alt="Concept map for a template expander"/>

> Terms defined: abstract class, abstract method, Application Programming Interface, Boolean expression, static site generator, truthy.

<a href="https://www.routledge.com/Software-Design-by-Example-A-Tool-Based-Introduction-with-Python/Wilson/p/book/9781032725215"><img src="{{'/sdxpy/sdxpy-cover.png' | relative_url}}" alt="Cover of 'Software Design by Example'" width="20%" class="centered">
</a>

[outline]: {{'/sdxpy/intro/#intro-syllabus' | relative_url}}
[sdxpy]: {{'/sdxpy/' | relative_url}}
[sdxpy_check]: {{'/sdxpy/check/' | relative_url}}
[sdxpy_interp]: {{'/sdxpy/interp/' | relative_url}}
[sdxpy_template]: {{'/sdxpy/template/' | relative_url}}
