# Project Proposal: Save the Humans!

## Background Information

This project is situated at the intersection of game development, crowd simulation, and AI behavior design. The premise is deliberately tongue-in-cheek: a zombie outbreak has occurred at a city zoo, and the animals, rather than the zookeepers, must rescue the panicked human visitors before the horde reaches them. This satirical inversion gives the project a distinctive identity while posing genuine and substantive technical challenges in agent-based simulation and interactive software design.

## Mentor

Greg Wilson is an independent educator and software engineering author who has spent decades teaching software development skills and designing learning materials for developers at all stages of their careers. 

## Project Description

The goal of the project is to build a browser-based game in which the player controls zoo animals to save human visitors from a zombie horde. Humans in the game panic and behave irrationally: rather than following optimal paths to the exits, they respond to nearby activity in counter-productive ways. Zombies pursue the nearest human, spreading as a horde through the zoo map. The player's zoo animals each have a distinct ability that can attract, repel, protect, redirect, or temporarily immobilize humans, and the player must use these abilities in combination to herd humans to safety before the zombies reach them.

Two initial animal types illustrate the double-edged nature of the mechanics. A tiger chases humans away from danger, but frightened humans may run in an unexpected direction and stumble toward the zombies rather than away from them. A bunny is so appealing that humans chase it, giving the player a way to draw crowds toward exits, but humans who catch the bunny stop moving entirely, leaving them vulnerable to any zombie that wanders past. The tension between each ability's upside and its downside is the core strategic challenge of the game. The game score is determined by how many humans escape through the exits before the horde overwhelms the remaining visitors.

This project will appeal to students interested in crowd simulation, game AI, and interactive software design. It provides authentic engineering challenges in a setting that is immediately legible and testable through play, and the humor of the premise gives the team creative latitude in designing levels, characters, and feedback.

## Project Scope

The team will select and justify a game framework appropriate for browser-based development, with candidate options including Godot, Phaser.js, and Pygame. The selection should be documented and driven by concrete criteria such as language familiarity, asset pipeline capabilities, and the ease of deploying a playable build to a browser environment.

The map will use a tile- or grid-based map for the zoo, with paths, enclosures, and clearly marked exits. At least three distinct levels must be designed and implemented, with escalating difficulty. Each level must be defined in a documented data format that can be loaded at runtime, laying the groundwork for the stretch goal of a simple in-game level editor.

The human crowd simulation is the most technically demanding component of the core scope. Human agents must implement a panic state that affects their movement decisions, a response system that models attraction toward friendly stimuli (such as the bunny) and repulsion from threatening ones (such as the tiger or a nearby zombie), and basic pathfinding toward exits when not overridden by a stronger immediate stimulus. The zombie AI must implement pursuit of the nearest human and simple horde-spreading behavior that creates escalating pressure as the level progresses. All AI behaviors must be unit tested to confirm that they behave correctly in isolation before integration testing is used to confirm that combined behaviors interact as expected.

The team will implement at least two distinct player-controlled animal types (tiger and bunny), each with a clearly distinct ability and documented tradeoffs that the player must learn to use strategically. The user interface must display a map view showing all agents in the field, counters for the current human and zombie populations, and appropriate win and lose screens. The game must support save/load functionality and a level-select screen.

Stretch goals to be pursued if core scope is completed ahead of schedule include additional animal types (such as an elephant with a stampede ability, or a parrot that mimics commands to redirect groups of humans), environmental hazards such as enclosures that open unexpectedly or water features that block movement, and a simple in-game level editor.

## Project Challenges

The crowd simulation is the project's most demanding technical challenge. Modeling entertaining and strategically interesting panic behavior without a full physics simulation requires the team to design and tune attraction and repulsion radii, movement response functions, and state transition thresholds carefully. Small changes in these parameters can shift the game from trivially easy to unplayably chaotic, and this tuning can only be validated through playtesting rather than automated tests alone. The team must treat balance work as a first-class engineering activity and schedule time for it accordingly.

Emergent behavior arises naturally from combining multiple animal abilities with a crowd of human agents and a pursuing zombie horde. The tiger's repulsion effect and the bunny's attraction effect can interact in ways that neither the developers nor the player fully anticipate, producing outcomes that are difficult to test exhaustively. The team should treat emergent interactions as a feature to be documented and balanced rather than a bug to be eliminated.

The double-edged mechanics require careful balance work. Each animal ability must be useful enough that a player will deploy it deliberately, but not so powerful that a single ability trivially solves every level. Achieving this balance requires iterative playtesting with users outside the development team, and the team must schedule and document at least two formal playtesting rounds as part of their project plan.

Multi-agent pathfinding under dynamic conditions is a known hard problem. Humans, zombies, and animals all move simultaneously, and each agent's movement affects the stimuli experienced by neighboring agents. The team should investigate efficient approximations appropriate for a real-time game context (e.g., steering behaviors, flow fields, or simplified influence maps) rather than attempting to implement optimal multi-agent planning algorithms.

On the non-technical side, animal abilities must be communicated to players intuitively without requiring lengthy tutorials, and the humor and tone of the game must remain consistent across artwork, text, and mechanics. Both of these constraints affect the user interface and level design as much as the underlying code, and the team should treat them as explicit design requirements rather than afterthoughts.

## Number of Students

3-4 students preferred.

## Sponsor-Provided Hardware and Software

No special hardware or software is required. All tools needed to complete this project are freely available as open-source software, including game engines, language runtimes, and development environments. The sponsor will act as project manager, participate in weekly standups, and serve as an external playtester throughout development.

## Project Search Keywords

- zombie game
- crowd simulation
- browser game
- humorous game design
- multi-agent AI

## Department of Software Engineering Required Deliverables

Standard departmental deliverables as listed by the RIT Department of Software Engineering.

## Sponsor and Project Specific Deliverables

- Playable prototype: a runnable game with at least 3 levels and at least 2 distinct animal types, hosted in a browser
- Source code in a public Git repository under an open-source license (MIT preferred); all game assets must be ethically sourced and licensed for reuse
- Technical design document covering agent behavior models, AI architecture, and the map/level data format
- User guide explaining how to install, run, and play the game
- Playtesting report documenting results from at least two rounds of external playtesting, including the adjustments made to game balance based on tester feedback
- A 2-minute gameplay video highlighting the animal ability mechanics and crowd behavior

## Proprietary Information

No aspect of this project is proprietary. The project will be developed and published openly, and team members are free to discuss all aspects of their work with potential employers or graduate programs.

## Availability

The sponsor is available for weekly 30-minute video calls and is flexible on the day and time, with a preference for morning slots (Eastern Time). The sponsor responds to email within 24 hours on weekdays.

## Project Agreements and Assignment of Rights

The sponsor requires the open-source project agreement: all code will be published publicly under an open-source license. The sponsor confirms that all necessary internal clearances have been obtained to use the RIT standard open-source project agreement unmodified.
