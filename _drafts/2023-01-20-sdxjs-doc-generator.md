---
title: "Software Design by Example 16: Documentation Generator"
date: 2023-01-20
year: 2023
---

Many programmers believe they're more likely to write documentation and keep it up to date
if it is close to the code.
Tools that extract specially-formatted comments from code and turn them into documentation
have been around since at least the 1980s;
[Chapter 16][sdxjs_doc] of [*Software Design by Example*][sdxjs]
builds on discussion in earlier chapters of [turning code into a data structure][sdxjs_checker]
to extract Markdown from comments and turn it into HTML.

<figure id="doc-generator-mapping">
  <img src="{{'/sdxjs/doc-generator/mapping.svg' | relative_url}}" alt="Mapping comments to documentation"/>
  <figcaption>Figure 16.2: How comments in code map to documentation in HTML.</figcaption>
</figure>

While tools like this are useful,
I wish they didn't need to exist.
Instead,
I wish our languages would allow us to write things like:

```
const name = (args) => {
    ...do things...
}
with documentation {
    Lorem ipsum dolor sit amet,
    [[consectetur]] adipiscing elit,
    sed do eiusmod tempor incididunt ut labore
    et dolore magna aliqua.
}
```

where the names of parameters and other functions are automatically cross-linked
and `[[...]]` or some similar syntax creates an external link and so on.
[doctest][doctest]-style tests could be put in another block,
and I'm sure people would find other uses for this as well.
In a better world than this…

> Terms defined: accumulator, block comment, deprecation, doc comment, line comment, slug.

And in answer to a question online,
no,
I didn't draw UML diagrams anywhere in this book:
there wasn't a single case where one of the standard diagram forms
felt like the best way to present what I wanted to convey.
I don't think it's because my programs are too small—there are
lots of places in the book where I wish I'd drawn more,
but I was wearied by the thought of having to maintain them.
I've grumbled about this in [[1][explain_code], [2][memory_diagram], [3][code_textbooks], [4][tools_exist]],
and frankly,
I'll start believing Silicon Valley is serious about being desperate for more programmers
when I see companies putting some real resources behind tools to help teach them better.

[code_textbooks]: {{'/2022/11/30/what-i-want-for-code-in-textbooks/' | relative_url}}
[doctest]: https://docs.python.org/3/library/doctest.html
[explain_code]: {{'/2022/12/28/ways-to-explain-code/' | relative_url}}
[memory_diagram]: {{'/2022/12/04/i-want-a-memory-diagram-generator/' | relative_url}}
[sdxjs]: {{'/sdxjs/' | relative_url}}
[sdxjs_checker]: {{'/sdxjs/style-checker/' | relative_url}}
[sdxjs_doc]: {{'/sdxjs/doc-generator/' | relative_url}}
[tools_exist]: {{'/2023/01/14/do-these-tools-exist/' | relative_url}}
