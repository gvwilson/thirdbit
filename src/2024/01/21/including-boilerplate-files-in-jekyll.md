---
date: 2024-01-20
title: "Including Boilerplate Files in Jekyll"
---

I use [Ark][ark] to format my books[^1]
but [Jekyll][jekyll] (the default for GitHub Pages) for my other sites[^2].
Each of those sites has a license,
a contributor guide,
and a code of conduct in its root directory.
I don't want to put YAML headers in them
because GitHub renders all of their content when they're viewed online,
but I also don't want to duplicate the content in other files
for rendering on GitHub Pages.
My solution is to create a parallel file called (for example) `license_.md`
(with a trailing underscore)
that contains this:

```
---
title: License
permalink: /license/
---

{% include boilerplate.md filename='LICENSE.md' %}
```

and then put this in `_includes/boilerplate.md`:

```
{% capture other %}{% include_relative {{include.filename}} %}{% endcapture %}
{{ other | markdownify | split: "</h1>" | last }}
```

It only works correctly if the file being included has exactly one `h1` header,
but well-formed pages shouldn't have more (or none).
I hope it's useful.

*This post motivated in part by a reading of Crichton and Krishnamurthi's recent paper "[A Core Calculus for Documents][paper]".*

[^1]: See [this post][building] for details.
[^2]: Despite the perpetual low-level annoyance of managing its toolchain.

[ark]: https://www.dmulholl.com/docs/ark/main/
[building]: https://third-bit.com/2023/03/12/building-a-book/
[jekyll]: https://jekyllrb.com/
[paper]: https://arxiv.org/abs/2310.04368
