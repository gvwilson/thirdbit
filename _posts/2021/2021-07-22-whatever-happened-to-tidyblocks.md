---
title: "Whatever Happened to TidyBlocks?"
date: 2021-07-22
year: 2021
---

TidyBlocks is a Scratch-like tool for doing basic data science.
Originally built by [Maya Gans][gans-maya],
it was overhauled in 2020,
after which several volunteers translated its interface into several different (human) languages.
We were excited by its potential, but:

1.  We had reached the limits of what the [Blockly][blockly] toolkit could do
    without some serious extension work.
    (In particular,
    there's no comprehensible way to represent joins using the available styles of blocks.)

2.  Nobody was willing to fund further development.
    The overhaul in 2020 took about 300-400 hours of volunteer time;
    while I would have liked to continue,
    I didn't see a way forward without fixing #1 above,
    and that couldn't be done without financial support.

I still think the idea is a good one:
the user testing we did showed that the interface is immediately comprehensible
to anyone who has used Scratch
(which these days means most middle school kids and their teachers),
and after watching my daughter plod through their school's "data literacy" module,
I think we need something better.
I hope someone, some day, will find a way to make it happen.

<img src="{{'/files/2021/tidyblocks-screenshot.png' | relative_url}}" alt="TidyBlocks" />

[blockly]: https://developers.google.com/blockly/
[gans-maya]: https://maya.rbind.io/
