# Project Proposal: JupyWord

## Background Information

-   Sponsor: Greg Wilson, independent educator and software engineering author
-   Domain: computational notebooks, office productivity software, plugin development
-   Tools like Jupyter and Marimo let users embed and run code cells inside a browser
    -   No equivalent exists for desktop word processors such as Microsoft Word or LibreOffice Writer

## Project Description

-   Build a plugin for Microsoft Word and/or LibreOffice Writer that lets users embed computational cells in desktop documents
    -   A computational cell is a block of code (e.g., Python) that the user can run from inside the document
    -   The output (text, tables, or charts) appears inline below the cell
-   The plugin communicates with a Jupyter-compatible kernel running locally so that cells in the same document share state
    -   I.e., a variable defined in one cell is available in later cells
-   When the document is saved, the source code of each cell and its most recent output are saved so that readers who do not run the plugin still see the last computed results
-   Target users are analysts, scientists, and educators who prefer to write reports, papers, or course notes in a familiar word processor rather than a browser-based notebook

## Project Scope

-   Plugin target: LibreOffice Writer is preferred (open-source, Python UNO API is publicly documented)
    -   Microsoft Word support via Office.js is a stretch goal
-   Kernel integration
    -   Connect to a local Jupyter kernel using the Jupyter messaging protocol (ZeroMQ)
    -   Start and stop the kernel from inside the plugin UI
-   Cell UI embedded in the document:
    -   Syntax-highlighted editable code area
    -   "Run" button and keyboard shortcut (e.g., Shift+Enter)
    -   Output area below the cell that displays plain text, error tracebacks, and images (e.g., charts)
-   Document persistence: serialize cell source and output into the document's native format
-   Session management: a sidebar or toolbar panel showing kernel status, interrupt, etc.
-   At least one complete worked example document with 5-10 cells shipped with the plugin
-   Unit and integration tests
-   Stretch goals:
    -   Microsoft Word support via Office.js add-in
    -   Additional output types: HTML tables, Markdown-rendered text
    -   Variable inspector panel showing the current kernel namespace
    -   Export document to a static HTML page with outputs frozen

## Project Challenges

-   Plugin APIs:
    -   LibreOffice's UNO API is powerful but sparsely documented
    -   And behavior differs across platforms (Linux, macOS, Windows)
-   Embedding a custom UI widget (the code cell) inside a Writer document without disrupting normal text flow is non-trivial
    -   Content controls or frames must be used carefully
-   Kernel lifecycle:
    -   Starting, monitoring, and stopping a kernel subprocess introduces process-management complexity
    -   Kernel crashes must be detected and reported without corrupting the document
-   Serialization:
    -   ODF and OOXML are XML formats
    -   Storing code and binary image output (e.g., base64 PNG) in a way that survives third-party editors (e.g., Google Docs opening a .docx) requires careful design
-   Security:
    -   Office documents that automatically run code are a known attack vector
    -   The plugin must require explicit user action (clicking Run) and must never auto-execute on open
-   Non-technical:
    -   The UX must feel native to word processor users who have never used a computational notebook
    -   Jupyter conventions (e.g., cell numbering, execution order) cannot be assumed

## Number of Students

-   3-4 students preferred

## Sponsor-Provided Hardware and Software

-   None:
    -   LibreOffice is open source and freely available
    -   The Jupyter kernel protocol is open and documented
    -   Python and required libraries are freely available
-   Sponsor will act as project manager, run standups, and test the plugin on realistic data analysis documents

## Project Search Keywords

-   "computational notebooks"
-   "office plugin"
-   "Jupyter kernel"
-   "literate programming"
-   "LibreOffice extension"

## Department of Software Engineering Required Deliverables

-   Standard departmental deliverables as listed by RIT SE

## Sponsor and Project Specific Deliverables

-   Working plugin installable in LibreOffice Writer (and optionally Microsoft Word) with no build steps for the end user
-   Source code in a public Git repository under an open-source license (MIT preferred)
-   Technical design document: plugin architecture, serialization format, security model, etc.
-   User guide
-   At least one complete example document that demonstrates the plugin's capabilities
-   Test suite covering core execution, rendering, and persistence paths
-   Usability report: at least two rounds of user testing with people who are not on the development team
    -   Including documented changes made in response to feedback

## Proprietary Information

-   No aspect of this project is proprietary

## Availability

-   Sponsor available for weekly 30-minute video calls; flexible on day and time; prefers morning slots (ET)
-   Responsive by email within 24 hours on weekdays

## Project Agreements and Assignment of Rights

-   Open-source agreement required: code is published publicly
-   Sponsor confirms all necessary clearances to use RIT standard open-source project agreement unmodified
