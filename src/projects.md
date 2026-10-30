---
title: "Student Projects"
template: "page"
---
I have always enjoyed supervising undergraduate capstone projects.
If you're interested in doing any of these,
or have students who would be,
please [get in touch][email].

## Tools

Bram
:   [Bram][bram] ("Bram runs agents mindfully") is a desktop app that embeds
    Claude Code and Codex in a GUI that provides structured, audited workflows.
    This project will add several new features, such as better support for
    design recovery and data analysis.

A Little Program Verifier
:   This project will extend [a verifier for a very simple programming language][frml]
    with basic concurrency features in order to teach people how those tools work.

A Little Program Analyzer
:   [Jorma][jorma] uses a combination of static and dynamic analysis to identify
    the roles of variables using Sajaniemi et al's taxonomy. This project will
    extend the dynamic analysis capabilities and test it on a larger set of programs

XKCD Charts
:   [Chart.xkcd][chart.xkcd] creates charts in the hand-drawn style of
    [XKCD][xkcd].  This project will fix outstanding issues, add new features
    such as axis limits and stable coloring schemes, and create wrappers in one
    or both of [Gleam][gleam] or [Dafny][dafny].

An I/O Library for Dafny
:   I want to translate [*Software Design by Example in Python*][sdxpy] into
    [Dafny][dafny] to see and show how verifiability changes the way we build
    software tools, but Dafny's I/O and systems programming libraries don't
    offer what the examples need. This project will build those libraries,
    starting with what's listed in [this blog post][dafny-io].

*A Software Development Simulator (filled for Winter 2027)*
:   I created [asimpy][asimpy] so that I could build simulations of software
    development teams similar to [these ones][curious-duck]. The goal of this
    project is to build those simulations and use them to explore the impact
    of AI tooling on the software lifecycle.

## Games

Rewind
:   A first-person shooter with a science-fiction theme in which each player has
    a limited "temporal battery" that can be spent to reverse the flow of time
    by a few seconds. If you just got shot, rewind and take cover instead; if
    you missed a shot, rewind and aim lower. The twist is that your opponent
    knows you can do this, turning every rewind into a battle of wits.

Save the Humans!
:   The zombies have attacked.  The people at the zoo have panicked, and it's up
    to the animals to save them in this tongue-in-cheek game. The tiger can
    chase people away from danger, but they might run straight into the arms of
    the ravenous horde. The bunny is so cute that people will chase *it*, but if
    they catch it they'll just stand there petting it until they're eaten, and
    so on.

Tower Support Game
:   A [tower defense game][tower-defense] is one in which the player builds
    fixed defenses against incoming waves of attackers. The objective of this
    game is to prototype a simple tower *support* game, in which the player
    builds bridges, first aid stations, and so on to help travelers reach their
    destination.

*Stardew Valley Murders (filled for Winter 2027)*
:   A mod that turns [Stardew Valley][stardew] into a murder mystery game.
    Grow vegetables, then trade them for gossip and clues until you figure out
    who murdered Clint and why.

[asimpy]: https://asimpy.readthedocs.io/
[bram]: https://github.com/judell/bram
[chart.xkcd]: https://github.com/gvwilson/chart.xkcd/
[curious-duck]: https://sim.curiousduck.io/
[dafny]: https://dafny.org/
[dafny-io]: @root/2026/09/20/io-for-sd/
[email]: mailto:gvwilson@third-bit.com
[frml]: https://github.com/gvwilson/frml/
[gleam]: https://gleam.run/
[jorma]: https://github.com/gvwilson/jorma
[sdxpy]: @root/sdxpy/
[stardew]: https://www.stardewvalley.net/
[tower-defense]: https://en.wikipedia.org/wiki/Tower_defense
[wbe]: https://browser.engineering/
[xkcd]: https://xkcd.com/
