---
title: "Ways to Explain Code"
date: 2023-01-01
year: 2023
---

- [Bloom's Two Sigma][bloom-two-sigma]: we don't know how good things *could* be, but we can compare common practice with the best thing we actually have

- Baseline is alternating blocks of code and prose

- Aspirational is Bret Victor's work (e.g., [Inventing on Principle][victor-inventing], which I think is the other [mother of all demos][mother-demos]) is out of reach of most instructors with today's tools
- [Glamorous Toolkit][glamorous] might free us from the tyranny of the punchcard,
  but we still have to decide what kinds of representations we want

- Recordings of interactive sessions (e.g., [Lorgat's SVG recordings][svg-screencast]), possibly with voiceover (e.g., [Scrimba][scrimba])
  - And these don't transfer to print or ebook, which is still important
  - Requires learners to [handle the third dimension][teaching-3d] themselves (recap this argument)

> ### Honorable Mentions
>
> [RxMarbles](https://rxmarbles.com/) and [finite state machine][fsm] representations of regular expressions
> are useful but not general.

## Text

- Callouts (numbers in the code with explanations there or in the main body)

- Generated explanations like [explainshell.com](https://explainshell.com/) and [regexr.com](https://regexr.com/)
  - Will ML chat tools make these more useful?

- Gradual mutation with changes highlighted (temporal diff)

- Skeleton that is filled in step by step (top-down diff)

- Problem is authoring
  - Maintaining the source as the lesson evolves is a nightmare
  - Many people have invented systems for keeping everything together
    (see [Hillel Wayne's][wayne-metafiles] or [Robert Nystrom's][nystrom-crafting],
    and I've written a couple over the years)
    but requires the author to keep track of the third dimension
    (like looking through a stack of transparencies and trying to make sense of individual sheets)

## Diagrams of Program State

- Ad-hoc diagrams of data structures, HTML/CSS layout, etc.

- Memory diagrams: more accurate but not necessarily more intelligible

- Program's execution state is a data structure (see [Loupe][loupe] depiction of JavaScript event loop)

> ### Who Are You Willing to Leave Out?
>
> The more we use diagrams, the less accessible our teaching materials are.
> We can add text descriptions,
> but that gets us right back to the textual explanations discussed in the previous section.

## Diagrams of Program Activity

- Sequence diagrams

- Use-case maps

- Dataflow diagrams (including Git branch-and-merge diagrams)

[bloom-two-sigma]: https://en.wikipedia.org/wiki/Bloom%27s_2_sigma_problem
[fsm]: https://en.wikipedia.org/wiki/Finite-state_machine
[glamorous]: https://gtoolkit.com/
[loupe]: http://latentflip.com/loupe/
[mother-demos]: https://en.wikipedia.org/wiki/The_Mother_of_All_Demos
[nystrom-crafting]: http://journal.stuffwithstuff.com/2020/04/05/crafting-crafting-interpreters/
[scrimba]: https://scrimba.com/
[svg-screencast]: https://wasimlorgat.com/tils/how-to-share-terminal-demos-as-razor-sharp-animated-svg.html
[teaching-3d]: {{'/2022/12/14/teaching-in-the-third-dimension/' | relative_url}}
[victor-inventing]: https://www.youtube.com/watch?v=PUv66718DII
[wayne-metafiles]: https://buttondown.email/hillelwayne/archive/on-metafiles/
