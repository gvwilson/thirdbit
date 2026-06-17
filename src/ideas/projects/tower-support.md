# Project Proposal: Tower Support Game

## Background Information

-   Sponsor: Greg Wilson, independent educator and software engineering author
-   Domain: game development, software design education
-   Tower defense is a well-established game genre
-   This project inverts the conventional mechanic: goal is to *help* the travelers, not destroy them

## Project Description

-   Build a prototype browser-based "tower support" game
-   Inversion of the tower defense genre:
    -   Instead of building defenses against attackers, the player places infrastructure (bridges, first aid stations, supply depots, etc.) to help travelers safely reach their destination
-   Travelers follow paths through a map: they are slowed, blocked, or harmed by terrain and hazards
-   Player deploys limited support structures strategically to keep travelers alive and moving
-   Score: how many travelers reach their destination

## Project Scope

-   Game framework selection and justification (e.g., Pygame, Godot, Phaser.js)
-   Tile- or graph-based map representation
-   Traveler agent AI: pathfinding around obstacles and toward exits
-   Minimum support structure types:
    -   Bridges (cross gaps)
    -   First aid stations (restore health)
    -   Shelters (pause travelers safely)
    -   Guards (fend off wolves and bandits)
-   Resource/economy system:
    -   Player earns points when travelers reach their destination
    -   Spends points to place structures
-   At least 3 distinct levels with increasing complexity
-   Basic UI: map view, resource counter, traveler status, win/lose screen
-   Save/load and level-select functionality
-   Unit and integration tests for core game logic (pathfinding, resource management, win condition)
-   Stretch goals:
    -   Procedural level generation
    -   Additional structure types (food stations, signal towers, wizards)
    -   Simple level editor

## Project Challenges

-   Pathfinding:
    -   Travelers must dynamically recompute routes as structures are placed
    -   Efficient re-evaluation is non-trivial
-   Balancing: tuning the game so it is neither trivial nor frustrating requires iterative playtesting
-   Emergent complexity: interactions between structures, terrain, and traveler behavior is hard to predict/test
-   Non-technical:
    -   Clear, intuitive UI for structure placement without a tutorial
    -   Game feel (timing, feedback) affects playability significantly
-   Scope management: distinguishing a playable prototype from a complete game is a challenge for the team

## Number of Students

-   3-4 students preferred

## Sponsor-Provided Hardware and Software

-   None: all required tools are freely available (open-source game engines, Python, JavaScript)
-   Sponsor will act as project manager, run standups, and playtest

## Project Search Keywords

-   "tower defense"
-   "browser game"

## Department of Software Engineering Required Deliverables

-   Standard departmental deliverables as listed by RIT SE

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
