# Project Proposal: ClickFlow

## Background Information

-   Sponsor: Greg Wilson, independent educator and software engineering author
-   Domain: visual programming, dataflow systems, JavaScript library development
-   Dataflow diagram tools appear across many industries
    -   LabVIEW (National Instruments) lets scientists wire instruments together
    -   Apache NiFi and Node-RED let systems integrators route and transform data streams between services and APIs
    -   Blender's shader and geometry node editors let 3D artists compose visual effects
-   Scratch uses a click-together block interface to make sequential programming accessible to beginners
    -   But it does not support the fan-in/fan-out patterns that arise in dataflow problems
-   No open-source JavaScript library lets developers mix both paradigms

## Project Description

-   Build a JavaScript library that lets users construct dataflow applications by combining two visual paradigms:
    1.  Scratch-style Snap-together blocks
    2.  Dataflow-style port connections
-   The two paradigms are complementary:
    -   A chain of snapped blocks is itself a node that can appear in a dataflow graph and expose ports
    -   Ports and connectors make it easy to represent complex dataflow relationships such as joins
-   The project includes a custom block API that lets developers define new block types by declaring:
    -   ports
    -   configuration fields that the end user can set using dropdown menus, radio buttons, or text entry boxes
    -   The library renders those fields inside the block without the developer writing any rendering code

## Project Scope

-   Canvas engine: an SVG-based (or Canvas-based) workspace that supports:
    -   Drag-and-drop placement and movement of blocks
    -   Snap detection and attachment for sequential (Scratch-style) connections
    -   Port hit-testing and bezier-curve line drawing for dataflow connections
    -   Zoom and pan
    -   Cycle prevention
-   Data model including block configuration, position, and connection
-   A custom block API that allows programmers to define new block types
-   Serialization to and from JSON
-   Built-in standard library of blocks demonstrating the API:
    -   Control flow: Sequence (implicit in snap), If/Else, Repeat N Times, While
    -   Data routing: Join, Broadcast, Route (conditional fan-out based on a field value)
    -   Utility: Constant, Log/Debug (prints to a panel)
-   Demo application: a standalone HTML page that loads the library and lets the user assemble a simple data pipeline, run it, and observe output
-   Automated tests:
    -   Unit tests for the graph data model
    -   Unit tests for the custom block API
    -   Integration tests that programmatically build a graph, execute it, and check its results
-   Stretch goals:
    -   Integrate a simple charting library

## Project Challenges

-   Mixed-paradigm UX:
    -   Users must understand intuitively when to snap blocks versus when to draw port connections
    -   Deciding where the boundary between the two paradigms lies
-   Unified execution semantics:
    -   Snap connections imply a strict execution order while port connections imply a reactive or event-driven model
    -   Combining them in a single runtime without surprising the user (e.g., a loop in a snapped chain that feeds data into a join node) requires a clearly specified execution model
    -   Cycles in the port-connection graph must be prevented
-   Custom block API ergonomics:
    -   The extension and registration APIs must be simple enough for the developers to have used *before* they started the project
-   Testing a visual, interactive system is always a challenge

## Number of Students

-   3-4 students preferred

## Sponsor-Provided Hardware and Software

-   None: all required tools are freely available
-   Sponsor will act as project manager, run standups, and participate in UX review sessions

## Project Search Keywords

-   "visual programming"
-   "dataflow diagrams"
-   "block-based programming"
-   "JavaScript library"
-   "no-code tools"

## Department of Software Engineering Required Deliverables

-   Standard departmental deliverables as listed by RIT SE

## Sponsor and Project Specific Deliverables

-   Published package containing the library with no required external dependencies beyond a modern browser
-   Source code in a public Git repository under an open-source license (MIT preferred)
-   Demo application (standalone HTML page) demonstrating all capabilities
-   Technical design document: architecture, data model, execution semantics, serialization format, and design rationale
-   Custom block API reference showing how to define blocks with various field types
-   Test suite covering the graph model, serialization, and API registration paths
-   Usability report: results from at least two rounds of user testing
    -   Including documented changes made in response to feedback

## Proprietary Information

-   No aspect of this project is proprietary

## Availability

-   Sponsor available for weekly 30-minute video calls; flexible on day and time; prefers morning slots (ET)
-   Responsive by email within 24 hours on weekdays

## Project Agreements and Assignment of Rights

-   Open-source agreement required: code is published publicly
-   Sponsor confirms all necessary clearances to use RIT standard open-source project agreement unmodified
