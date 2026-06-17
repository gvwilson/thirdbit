# Project Proposal: Save the Humans!

## Background Information

-   Sponsor: Greg Wilson, independent educator and software engineering author
-   Domain: game development, crowd simulation, AI behavior design
-   Tongue-in-cheek premise: a zombie outbreak at a zoo where the animals must rescue panicked human visitors

## Project Description

-   Build a prototype browser-based game in which the player controls zoo animals to save human visitors from a zombie horde
-   Humans panic and behave irrationally
    -   Zombies pursue humans
    -   Animals have unique abilities to redirect, distract, or protect humans
-   Examples of animal abilities
    -   Tiger: chases humans away from danger, but humans may run in a wrong direction (into zombies' arms)
    -   Bunny: so cute that humans chase it, but humans who catch it stop moving (and may be eaten while distracted)
-   Player must use animal abilities in combination to herd humans to safety before zombies reach them
-   Game score: how many humans escape

## Project Scope

-   Game framework selection and justification (e.g., Godot, Pygame, Phaser.js)
-   Tile- or grid-based map (zoo layout with enclosures, paths, exits)
-   Human crowd simulation: panic state, attraction/repulsion behaviors, basic pathfinding
-   Zombie AI: pursuit of nearest human, simple spreading horde behavior
-   At least 2 playable animal types (tiger + bunny minimum) with distinct player-controlled abilities
-   At least 3 levels with distinct zoo layouts and escalating difficulty
-   UI: map view, human/zombie counts, win/lose screen
-   Unit and integration tests for AI behaviors and win/loss conditions
-   Stretch goals:
    -   Additional animal types (elephant stampede, parrot that repeats commands to redirect groups, etc.)
    -   Environmental hazards (enclosures that open, water hazards)
    -   Simple level editor

## Project Challenges

-   Crowd simulation:
    -   Modeling realistic (or entertainingly unrealistic) panic behavior without full physics simulation
    -   Tuning attraction/repulsion radii is non-trivial
-   Emergent behavior:
    -   Combining multiple animal abilities can produce unexpected outcomes that are hard to test exhaustively
-   Balancing double-edged mechanics:
    -   Abilities must be useful but not trivially so
-   Pathfinding under dynamic conditions:
    -   Humans, zombies, and animals all move simultaneously
    -   efficient multi-agent pathfinding is a known hard problem
-   Non-technical:
    -   Communicating animal abilities clearly to players without lengthy tutorials
    -   Humor and tone must be consistent across art, text, and mechanics

## Number of Students

-   3-4 students preferred

## Sponsor-Provided Hardware and Software

-   None: all required tools are freely available (open-source engines)
-   Sponsor will act as project manager, run standups, and playtest

## Project Search Keywords

-   "zombies"
-   "humorous games"
-   "browser games"

## Department of Software Engineering Required Deliverables

-   Standard departmental deliverables as listed by RIT

## Sponsor and Project Specific Deliverables

-   Playable prototype: runnable game with at least 3 levels and 2 animal types
-   Source code in a public Git repository under an open-source license (MIT preferred)
    -   Game assets (e.g., artwork and sound effects) must be ethically sourced
-   Technical design document: agent behavior models, AI architecture, map/level format
-   User guide: how to install, run, and play
-   Playtesting report: results from at least two rounds of external playtesting
    -   Including documented adjustments to game balance
-   2-minute gameplay video highlighting animal mechanics

## Proprietary Information

-   No aspect of this project is proprietary

## Availability

-   Sponsor available for weekly 30-minute video calls; flexible on day and time; prefers morning slots (ET)
-   Responsive by email within 24 hours on weekdays

## Project Agreements and Assignment of Rights

-   Open-source agreement required: code is published publicly
-   Sponsor confirms all necessary clearances to use RIT standard open-source project agreement unmodified
