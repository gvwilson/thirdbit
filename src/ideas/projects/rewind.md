# Project Proposal: Rewind

## Background Information

First-person shooters are one of the most popular genres in games, and time manipulation has appeared in pouplar games such as *Prince of Persia: The Sands of Time*. This proposal combines the two in a way that has not been fully explored: a multiplayer FPS in which every player has access to a limited time-rewind ability, and every tactical decision is shadowed by the knowledge that the opponent can undo it. The resulting gameplay is less about reflexes than about strategic reasoning.

## Mentor

Greg Wilson is an independent educator and software engineering author who has spent decades teaching software development skills and designing learning materials for developers at all stages of their careers.

## Project Description

The goal of this project is to build a browser-playable first-person shooter with a science-fiction theme in which each player carries a temporal battery. At any point during play, a player may press a rewind key to reverse the flow of time by a few seconds, undoing recent events including incoming fire, missed shots, and movement decisions. Rewinding consumes battery charge, and the battery only recharges slowly (or can be topped up by collecting power-ups scattered around the level).

The core strategic tension is recursive. If a player rewinds after being shot, they now know where the shot came from and can respond differently. But their opponent also knows that the player can rewind, so the opponent will themselves do something different in the replayed interval. The result is a layered bluffing game in which the optimal play depends not just on the current state of the match but on a stack of assumptions about what each player expects the other to do in a replay. The game rewards players who can reason one or two levels deeper than their opponent.

This project will appeal to students interested in game engine architecture, real-time state management, and the design of novel mechanics that are easy to explain but produce complex emergent behavior. The time-rewind mechanic is technically demanding to implement correctly, and the design challenges around communicating the mechanic to players and balancing battery costs against rewind benefit are substantial.

## Project Scope

The team will select and justify a game framework appropriate for browser-based development, with candidate options including Godot (exported to web), Babylon.js, and Three.js. The selection should be documented and driven by criteria such as language familiarity, the ease of implementing a first-person controller, asset pipeline support, and browser deployment constraints.

The game's most important technical component is the state recording and replay system. At every game tick, the engine must snapshot all relevant state: player positions, orientations, velocities, projectile positions, and health values. When a player rewinds, the engine restores the recorded state from the appropriate tick and resumes play from that point. The snapshot system must be efficient enough to run continuously without degrading frame rate, and the team must decide how many seconds of history to retain and at what granularity. This decision involves a space-time tradeoff that should be documented and justified.

A second technical challenge arises from the game's multiplayer nature. When one player rewinds, the server must coordinate the rewind across all connected clients so that each player sees a consistent game state. The team should begin with a single-player mode against AI opponents and treat networked multiplayer as a stretch goal, implementing it only after the core mechanics are stable and tested in the single-player context.

The temporal battery must be clear in the user interface. Players need to see their current charge level at a glance and understand the cost of a rewind before committing to it. The team will implement at minimum a heads-up display showing remaining charge, a visual effect that signals to both the rewinding player and observers that a rewind is in progress, and a brief cooldown after a rewind to prevent players from holding the rewind key continuously.

The map must be designed with the rewind mechanic in mind. Cover positions, sight lines, and the placement of battery recharge pickups all affect the strategic value of rewinding, and these elements should be tuned through playtesting. The team will design and implement at least two distinct arena maps, each defined in a documented data format that can be loaded at runtime.

## Project Challenges

The state recording system is the project's central technical challenge. Naive approaches that record the full game state at every tick will consume too much memory; approaches that record only deltas require a reliable way to reconstruct any past state by replaying forward from an earlier snapshot. The team must investigate and benchmark at least two approaches before committing to an implementation, and the choice must be documented with measurements.

Reproducing game state after a rewind is harder than it appears. Events that are partly completed when a rewind begins must either be rolled back cleanly or the system must be designed so that all state changes are atomic and invertible. The team must enumerate the categories of game events that can occur and confirm that each is handled correctly by the replay system.

Game balance is the project's central design challenge. If the battery is too large, players can rewind freely and the game degenerates into whoever rewinds last. If the battery is too small, rewinding feels pointless and players ignore the mechanic. Tuning the battery capacity, recharge rate, rewind cost, and pickup placement requires iterative playtesting with external testers, and the team must schedule and document at least two formal playtesting rounds.

Communicating the mechanic to new players is non-trivial. Players unfamiliar with time-rewind games may not realize that their opponent can also rewind, or may not grasp that their own behavior in the replayed interval is visible to the opponent. The tutorial and onboarding experience must convey these ideas quickly and without a lengthy text explanation, and the team should treat the tutorial as a first-class deliverable rather than an afterthought.

## Number of Students

2-3 students preferred.

## Sponsor-Provided Hardware and Software

No special hardware or software is required. All tools needed to complete this project are freely available as open-source software, including game engines, language runtimes, and development environments. The sponsor will act as project manager, participate in weekly standups, and serve as an external playtester throughout development.

## Project Search Keywords

- first-person shooter
- time rewind mechanic
- game state replay
- browser game
- game AI

## Sponsor and Project Specific Deliverables

- Playable prototype: a runnable single-player game with at least 2 arena maps and at least one AI opponent, hosted in a browser
- Source code in a public Git repository under an open-source license (MIT preferred); all game assets must be ethically sourced and licensed for reuse
- Technical design document covering the state recording system, battery balance parameters, and the map data format
- User guide explaining how to install, run, and play the game, including an explanation of the rewind mechanic
- Playtesting report documenting results from at least two rounds of external playtesting, including the adjustments made to balance based on tester feedback
- A 2-minute gameplay video demonstrating the rewind mechanic and its strategic implications

## Proprietary Information

No aspect of this project is proprietary. The project will be developed and published openly, and team members are free to discuss all aspects of their work with potential employers or graduate programs.

## Availability

The sponsor is available for weekly 30-minute video calls and is flexible on the day and time, with a preference for morning slots (Eastern Time). The sponsor responds to email within 24 hours on weekdays.
