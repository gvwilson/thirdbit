---
title: "Browsercast Revisited"
date: 2024-10-13
---

Shakespeare wrote sonnets;
we write PowerPoint
A lot of people blame it for bad presentations,
but that's like blaming fountain pens for bad poetry.
The real problem with tools like PowerPoint is that they aren't web-friendly.
When you export a slideshow to present on the web,
what you actually get is a bunch of images.
There's no text,
just pixels arranged in the shapes of letters;
no hyperlinks;
and nothing search engines or disability aids can read.
What's worse,
if you want something people can replay,
you have to make a screencast.
These are just as opaque to search engines and disability aids,
and probably several times larger than the original slides.

A decade ago,
we built a solution called Browsercast
that played audio in sync with an HTML slideshow.
"View Source", links, CSS, screen readers, and search worked as they should
because everything was web-native HTML.
And since it was just text and audio,
it was a fraction of the size of a video,
which made it ideal for mobile devices.

Browsercast never caught on,
but I'm hoping [this new version][browsercast-site] will.
It's just 5kb of JavaScript and 1.5kb of CSS,
and,
like its predecessor,
is available under the MIT License.
However,
there's still a lot to do:

1.  The first challenge is to find a better way to manage replay.
    If the `audio` element on the first slide doesn't display controls,
    browsers refuse to play any of the sound clips
    because the user hasn't interacted with the page.
    (Try removing `control=true` from the first `audio` element
    and then check the error messages in browser's console log to confirm this.)
    This behavior prevents pop-up audio ads,
    but in this case it makes for a poor user experience.

2.  Second, we need a better way to manage the audio clips themselves.
    It's easiest for a person to record their presentation as a single audio file,
    but the `audio` elements in the slides would then need start and end time markers,
    which are annoying to find and copy into the browsercast file.
    On the other hand,
    splitting one file into a couple of dozens short clips
    or recording the presentation in a couple of dozen bursts
    is equally annoying.

3.  This prototype replays narration every time a slide comes into view,
    which means the audience hears a clip repeated
    when the presenter backs up to a previous slide.
    The JavaScript could keep track of which clips have already played
    and not replay them unless asked to,
    but should that be controlled by hot keys?
    Or should the audio control on the first slide be repeated on subsequent slides?
    Or should we approach this problem in some other way entirely?

4.  The [snap-scroll technique][snap-scroll] for presenting slides
    does not behave gracefully when a slide is too tall to fit on the screen.
    We would like to clip slides to fit the viewport
    and to report clipped slides to authors as they are developing slideshows,
    but need ways to implement and present this.

5.  Finally [sic],
    we need to think about captioning and internationalization.
    Transcripts in different languages can easily be added to slides in hidden elements;
    how should the accompanying audio clips be added,
    and how should users indicate which set of clips they want to hear?

My thanks to David Seifried,
Jeremy Banks,
David Wolever,
Gabriel Ivanica,
and Rémi Emonet for their work on Version 1,
and to Yihui Xie for inventing the [snap-scroll technique][snap-scroll].

[browsercast-site]: https://gvwilson.github.io/browsercast/
[snap-scroll]: https://yihui.org/en/2023/09/snap-slides/
