---
title: "Punchcards Considered Harmful"
date: 2021-01-17
year: 2021
---

<img src="{{ '/files/2021/punchcard.jpg' | relative_url }}" alt="punchcard" class="centered">

Most people programming today have never punched a card,
but all programming editors still treat code as lines of text—in other words,
as if it still might have to fit onto punchcards.
As I've been <strike>saying</strike> ranting [for a while now](https://queue.acm.org/detail.cfm?id=1039534),
this is holding us back in ways we can barely recognize.

One example is YAML,
or rather,
the insistence that people must write complex nested data structures as indented lines of text.
The rules are well-defined and simple cases are simple,
but as anyone who has spent an hour wrestling with a Jekyll or Bookdown configuration file can attest,
any complex case is an unproductive nightmare waiting to escape its cage.

So here's a thought experiment.
Imagine that every editor from [Notepad](https://en.wikipedia.org/wiki/Microsoft_Notepad)
to [Vim](https://www.vim.org/)
to [VS Code](https://code.visualstudio.com/)
automatically displayed CSV files as editable tables.
Instead of editing this:

```
book_filename: "r4de"
language:
  label:
    fig: "Figure "
    tab: "Table "
  ui:
    chapter_name: "Chapter "
output_dir: "docs"
delete_merged_file: false
new_session: true
rmd_files:
  - index.Rmd
  - basics.Rmd
  - tidyverse.Rmd
  - rmarkdown.Rmd
  - package.Rmd
  - references.Rmd
```

people would read and edit something like this:

<table class="centered">
<tr>	<td> book_filename </td>	<td> "r4de" </td>		<td> </td>		<td> </td></tr>
<tr>	<td> language </td>		<td> </td>			<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> label </td>		<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td>  </td>			<td> fig </td>		<td> "Figure " </td></tr>
<tr>	<td>  </td>			<td>  </td>			<td> tab </td>		<td> "Table " </td></tr>
<tr>	<td>  </td>			<td> ui </td>			<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td>  </td>			<td> chapter_name </td>	<td> "Chapter " </td></tr>
<tr>	<td> output_dir </td>		<td> "docs" </td>		<td> </td>		<td> </td></tr>
<tr>	<td> delete_merged_file </td>	<td> false </td>		<td> </td>		<td> </td></tr>
<tr>	<td> new_session </td>		<td> true </td>			<td> </td>		<td> </td></tr>
<tr>	<td> rmd_files </td>		<td> </td>			<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> index.Rmd </td>		<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> basics.Rmd </td>		<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> tidyverse.Rmd </td>	<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> rmarkdown.Rmd </td>	<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> package.Rmd </td>		<td> </td>		<td> </td></tr>
<tr>	<td>  </td>			<td> references.Rmd </td>	<td> </td>		<td> </td></tr>
</table>

The file might actually be *stored* like this:

```
book_filename,"r4de"
language
,label
,,fig,"Figure "
,,tab,"Table "
,ui
,,chapter_name,"Chapter "
output_dir,"docs"
delete_merged_file,false
new_session,true
rmd_files
,index.Rmd
,basics.Rmd
,tidyverse.Rmd
,rmarkdown.Rmd
,package.Rmd
,references.Rmd
```

but if programmers could trust everyone's favorite editor
to render rows and columns as rows and columns,
I believe that:

1.  most people would choose to use it instead of JSON, YAML, TOML, and STUMBL
    (OK, I made that last one up, but you weren't sure, were you?) because

1.  they would find it easier to read and write nested structures
    if their editor gave them even this little bit of help and guidance.

But I don't have any evidence for my second claim,
which is where you (the ambitious grad student looking for a project) come in.
Is there a difference in frustration quotient between YAML-in-a-text-editor
and the same data in a table editor?
Do people like the experience better if the table editor lives inside their usual editor?
And can people find bugs faster or more reliably
if nested structures are presented as tables rather than as indented text?
My bet is "yes" for all three,
but I don't want you to trust me
because I don't want you to trust people—I want you to trust *data*.

And of course once this is working,
the next experiment would be to add a tree editing widget to several common programming editors
and see if it's better, worse, or the same.
I use `[ a | b ]` is my way of showing two editable cells side by side,
and for fairness' sake I think it's essential to add these widgets to existing editors:
many programmers will change operating system, citizenship, and gender
before abandoning Emacs.

```
├──[ book_filename | "r4de" ]
├──language
│   ├──label
│   │  ├──[ fig | "Figure " ]
│   │  └──[ tab | "Table " ]
│   └──ui
│      └──[ chapter_name | "Chapter " ]
├──[ output_dir | "docs" ]
├──[ delete_merged_file | false ]
├──[ new_session | true ]
└──rmd_files
   ├──index.Rmd
   ├──basics.Rmd
   ├──tidyverse.Rmd
   ├──rmarkdown.Rmd
   ├──package.Rmd
   └──references.Rmd
```

I don't think "the other 99%" of humanity will
[use static site generators to write lessons]({{ '/2021/01/17/the-page-is-not-the-lesson/' | relative_url }})
unless we make them much (much) more approachable.
Making configuration easier is just one part of that,
but:

1.  it's a part that can be used in many other places, and

1.  it's a step toward finally ending the long, tyrannical reign of the punchcard.
