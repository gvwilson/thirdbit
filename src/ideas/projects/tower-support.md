# Project Proposal: Tower Support Game

## Background Information

Tower defense is a well-established video game genre in which players build static defenses to destroy waves of enemies before they reach a protected point. This proposal inverts that familiar mechanic to create something pedagogically and mechanically novel: a game in which the goal is cooperation and assistance rather than destruction.

## Mentor

Greg Wilson is an independent educator and software engineering author who has spent decades teaching software development skills and designing learning materials for developers at all stages of their careers. 

## Project Description

The goal of this project is to build a browser-based "tower support" game that inverts the conventional tower defense genre. Rather than deploying weapons to halt attackers, the player places infrastructure such as bridges, first aid stations, supply depots, and guards to help travelers safely reach their destination despite threats and obstacles. Travelers follow paths through a map and are slowed, blocked, or harmed by terrain features and hazards they encounter along the way. The player's task is to deploy a limited set of supports strategically, managing resources to keep as many travelers alive and moving as possible. The game score is determined by how many travelers successfully reach their destination.

This project will appeal to students interested in game AI, agent-based simulation, and interactive software design. It requires them to tackle authentic engineering challenges in a domain that is immediately engaging and testable through play. The prosocial game mechanic is both a distinguishing feature and a design constraint: structures must visibly benefit travelers without removing all challenge from the game.

## Project Scope

The team will select and justify a game framework appropriate for browser-based development, with candidate options including Godot, Phaser.js, and Pygame. The selection decision should be documented and driven by factors such as language familiarity, asset pipeline support, and browser deployment requirements.

The map representation will use either a tile- or graph-based approach, and the team will design and implement at least three distinct levels of increasing complexity. Each level must be expressible in a documented data format that can be loaded at runtime, laying the groundwork for the stretch goal of a simple level editor.

Traveler agents require an AI subsystem capable of pathfinding around obstacles and toward exits, with the ability to dynamically recompute routes as the player places new structures. The team will implement at minimum four support structure types: bridges (which allow travelers to cross gaps in the terrain), first aid stations (which restore traveler health), shelters (which pause travelers in a protected state), and guards (which defend travelers from wolves, bandits, or other hazards encountered on the map). Additional structure types are listed as stretch goals below.

The game economy gives players points when travelers reach their destination; those points are spent to place new structures. This feedback loop is central to the game's strategic depth and must be balanced carefully through iterative playtesting.

The user interface must display the map view, the player's current resource total, the status of travelers in the field, and appropriate win/lose screens. The game must support save/load functionality and a level-select screen. The team will write unit and integration tests for all core game logic, including the pathfinding subsystem, the resource management system, and the win/loss condition evaluation.

The broad scope of the project, with framework selection, AI design, game balance, UI implementation, data persistence, and testing, is designed to provide an authentic full-cycle software engineering experience in which students develop requirements, design, and test documentation as a natural part of building a working product. Stretch goals may include procedural level generation, additional structure types such as food stations, signal towers, or wizards, and a simple in-game level editor.

## Project Challenges

The largest challenge in this project is game balance. Tuning the game so that it is neither trivially easy nor frustratingly difficult requires iterative playtesting with external users, not just the development team. The team must build this testing time into their schedule and treat balance adjustments as first-class engineering work rather than an afterthought. This is particularly important because emergent complexity arises from interactions between structures, terrain types, and traveler behavior. A combination of structures that seems straightforward in isolation may produce unexpected results when travelers interact with several of them in sequence, and exhaustive automated testing of such interactions is difficult by nature.

A purely technical challenge is the pathfinding subsystem. Travelers (and mobile threats) must dynamically recompute routes whenever the player places a new structure, and this recomputation must be fast enough not to disrupt gameplay. Naive re-evaluation strategies are unlikely to be acceptable, and the team will need to evaluate incremental or event-driven approaches.

On the non-technical side, the user interface must make structure placement intuitive without requiring a lengthy tutorial. Game feel significantly affects playability, but is difficult to specify in advance. Finally, the team must exercise scope discipline, clearly distinguishing the deliverables of a playable prototype from the aspirations of a complete commercial game.

## Number of Students

3-4 students preferred.

## Sponsor-Provided Hardware and Software

No special hardware or software is required. All tools needed to complete this project are freely available as open-source software, including game engines, language runtimes, and development environments. The sponsor will act as project manager, participate in weekly standups, and serve as an external playtester throughout development.

## Project Search Keywords

- tower defense
- browser game
- game AI
- agent pathfinding
- cooperative game mechanics

## Department of Software Engineering Required Deliverables

Standard departmental deliverables as listed by the RIT Department of Software Engineering.

## Sponsor and Project Specific Deliverables

- Playable prototype: a runnable game with at least 3 levels and at least 2 distinct traveler types, hosted in a browser
- Source code in a public Git repository under an open-source license (MIT preferred); all game assets must be ethically sourced and licensed for reuse
- Technical design document covering agent behavior models, AI architecture, and the map/level data format
- User guide explaining how to install, run, and play the game
- Playtesting report documenting results from at least two rounds of external playtesting, including the adjustments made to game balance based on tester feedback
- A 2-minute gameplay video highlighting the traveler and support structure mechanics

## Proprietary Information

No aspect of this project is proprietary. The project will be developed and published openly, and team members are free to discuss all aspects of their work with potential employers or graduate programs.

## Availability

The sponsor is available for weekly 30-minute video calls and is flexible on the day and time, with a preference for morning slots (Eastern Time). The sponsor responds to email within 24 hours on weekdays.

## Project Agreements and Assignment of Rights

The sponsor requires the open-source project agreement: all code will be published publicly under an open-source license. The sponsor confirms that all necessary internal clearances have been obtained to use the RIT standard open-source project agreement unmodified.
