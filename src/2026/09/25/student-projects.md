---
title: "Student Projects"
date: 2026-09-25
category: education
---
Autumn always makes me feel like I ought to be back in school,
either to learn or to teach.
In turn,
that makes me think about student projects I would like to run.

## Tools

Bram
:   [Bram][bram] ("Bram runs agents mindfully") is a desktop app that embeds
    Claude Code and Codex in a GUI that provides structured, audited workflows.
    This project will add several new features, including support for other
    families of models such as DeepSeek.

A Little WYSIWYG Editor
:   [*Web Browser Engineering*][wbe] builds a small but fully functional web
    browser step by step to show students how real ones work. The aim of this
    project is to build an equally simple desktop WYSIWYG editor in Python that
    supports both styled text and embedded sketching.

A Little Program Verifier
:   Where the previous project would build a simple editor, this project would
    build a verifier for a very simple programming language in order to teach
    people how those tools work. (See [here][frml] for preliminary work.)

XKCD Charts
:   [Chart.xkcd][chart.xkcd] creates charts in the hand-drawn style of
    [XKCD][xkcd].  This project will fix outstanding issues, add new features
    such as axis limits and stable coloring schemes, and create wrappers in one
    or both of [Gleam][gleam] or [Dafny][dafny].

Distributed Systems Simulators
:   [*Software Design by Example in Python*][sdxpy] deliberately ignored
    concurrency, partial failure, and everything else associated with modern
    distributed applications. The draft appendices are fixing that by building
    scale models of distributed protocols and systems from TCP to BitTorrent and
    load-balancing tools using [asimpy][asimpy]; this project will fill those in
    and extend them.

An I/O Library for Dafny
:   I want to translate [*Software Design by Example in Python*][sdxpy] into
    [Dafny][dafny] to see and show how verifiability changes the way we build
    software tools, but Dafny's I/O and systems programming libraries don't
    offer what the examples need. This project will build those libraries,
    starting with what's listed in [this blog post][dafny-io].

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

[asimpy]: https://asimpy.readthedocs.io/
[bram]: https://github.com/judell/bram
[chart.xkcd]: https://github.com/gvwilson/chart.xkcd/
[dafny]: https://dafny.org/
[dafny-io]: @root/2026/09/20/io-for-sd/
[frml]: https://github.com/gvwilson/frml/
[gleam]: https://gleam.run/
[sdxpy]: @root/sdxpy/
[tower-defense]: https://en.wikipedia.org/wiki/Tower_defense
[wbe]: https://browser.engineering/
[xkcd]: https://xkcd.com/
