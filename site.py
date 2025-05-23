from datetime import datetime, date

theme = "thirdbit"
title = "The Third Bit"
tagline = "Start where you are, use what you have, help who you can."
url = "https://third-bit.com"
author = {
    "name": "Greg Wilson",
    "url": "third-bit.com",
    "email": "gvwilson@third-bit.com",
    "calendly": "https://calendly.com/gvwilson",
    "github": "https://github.com/gvwilson",
    "mastodon": "https://mastodon.social/@gvwilson",
    "linkedin": "https://www.linkedin.com/in/greg-wilson-a26510b6/",
    "youtube": "https://www.youtube.com/channel/UCbDQ7FIeYB3FHRADAjUjfrg",
}

today = date.today()
now = datetime.now().isoformat()

projects = {
    "ongoing": [
        "browsercast",
        "marimo-h5p",
    ],
    "programming": [
        "execution-order",
        "narwhals",
        "markdown-dom",
        "dragnet",
        "wysiwyg-editor",
        "xkcd-charts",
        "extending-lox",
        "testing-rse",
        "parallel-marimo",
        "tidyblocks",
        "wysiwyg-notebook",
        "code-selectors",
        "session-recording",
        "tower-support",
    ],
    "tutorials": [
        "web-tutorial",
        "generative-art",
        "sdx-gleam",
        "des-sim",
        "sdx-security",
        "sdx-everyone",
        "unbreaking",
        "sdx-performance",
    ],
    "research": [
        "undergrad-textbooks",
        "variable-roles",
        "code-review",
        "claim-validity",
        "understanding-ethics",
        "missing-lessons",
        "slide-text",
        "tooling-effort",
        "developer-discussions",
        "ide-adoption",
        "ghost-engineers",
        # "hoye-test",
        # "altruism",
    ]
}

papers = [
    {
        "author": "Wilson et al",
        "title": "Experience Report: It Will Never Work in Theory",
        "url": "https://www.computer.org/csdl/magazine/so/5555/01/10424425/1Ulj1Qa8tJ6",
        "year": 2024,
    },
    {
        "author": "Haberman & Wilson",
        "title": "Ten simple rules for writing a technical book",
        "url": "https://doi.org/10.1371/journal.pcbi.1011305",
        "year": 2023,
    },
    {
        "author": "Wilson",
        "title": "Twelve quick tips for software design",
        "url": "https://doi.org/10.1371/journal.pcbi.1009809",
        "year": 2022,
    },
    {
        "author": "Smalls & Wilson",
        "title": "Ten quick tips for staying safe online",
        "url": "https://doi.org/10.1371/journal.pcbi.1008563",
        "year": 2021,
    },
    {
        "author": "Lin et al",
        "title": "Ten quick tips for making things findable",
        "url": "https://doi.org/10.1371/journal.pcbi.1008469",
        "year": 2020,
    }
]

src_dir = "src"
out_dir = "docs"
extension = "/"
dir_nodes = False
markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
copy = [
    "*.gif",
    "*.jpeg",
    "*.jpg",
    "*.js",
    "*.json",
    "*.pdf",
    "*.png",
    "*.svg",
    "*.webp",
]
