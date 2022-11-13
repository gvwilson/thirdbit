---
title: "The Notebook Not Taken"
date: 2022-11-13
year: 2022
---

I had the pleasure of seeing [Alison Hill](https://www.apreshill.com/)
talk about computational notebooks last week.
[Jupyter](https://jupyter.org/),
[Quarto](https://quarto.org/),
[Wolfram Notebooks](https://www.wolfram.com/notebooks/),
and the like are now many scientists' preferred way to think in code.
Having used several,
I can't help but wonder if there's a universe out there
in which we took a different path.
Instead of starting with Markdown and slowly edging toward a full-featured editor,
did someone on Earth-978 write a plugin for [LibreOffice](https://www.libreoffice.org/)
to run code and insert its output into the document?
It's technically feasible:
there's no reason something like the [Jupyer protocol](https://jupyter-protocol.readthedocs.io/)
couldn't have been invented with a WYSIWYG editor as the first front end
instead of a browser.

Earth-977's history took yet another path.
There,
Microsoft included what they called a "computational bridge" in Office 2007.
It was designed to help people create automated reports,
but scientists almost immediately adopted it as well:
most of them were already using Word and Excel,
and found that learning a bit of VB.NET to push around their dataframes
was a lot easier than shifting to an entirely new suite of tools.
By the time Google Docs appeared,
active code blocks were as normal (and as expected) as drawings and tables.
A few holdouts continued to use Python, R, and plaintext editors,
but once a consortium sponsored by Microsoft, Google, and Apple
implemented diff and merge for office documents,
the battle was effectively over.

I suspect [our universe](https://marvel.fandom.com/wiki/Earth-1218) unfolded differently
for two reasons:

1.  Most computational scientists don't know Java or .NET.

2.  Most programmers look down on WYSIWYG editors.
    As a result,
    auxiliary tools from `grep` to Git can't handle things
    that aren't backward-compatible with punchcards.

I believe the LibreOffice path is still viable in our universe.
The [unseen 99%](https://www.hanselman.com/blog/dark-matter-developers-the-unseen-99)
of scientists (data or otherwise)
don't yet use computational notebooks of any kind.
With the distinction between desktop and cloud growing ever blurrier,
and with so many of the pieces needed for this approach already available,
I think a startup could make a compelling case that
accountants, marketing executives, and others
would prefer something evolutionary
over a browser-based dashboarding tool
or something as alien as today's notebooks.

*Note: this post was inspired in part by my move from Twitter to
[Mastodon](https://mastodon.social/@gvwilson).
The differences between the two have got me thinking about
how chancy and evitable our technologies are,
and about how many alternatives we have yet to explore.*
