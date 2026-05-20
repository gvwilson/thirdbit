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
    "linkedin": "https://www.linkedin.com/in/gvwilson/",
    "youtube": "https://www.youtube.com/channel/UCbDQ7FIeYB3FHRADAjUjfrg",
}

today = date.today()
now = datetime.now().isoformat()

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

prior_entries = [
    {
        "title": "The Carpentries",
        "url": "https://carpentries.org",
        "description": "A non-profit organization teaching basic software and data skills to researchers world-wide (1998–present).",
    },
    {
        "title": "It Will Never Work in Theory",
        "url": "http://neverworkintheory.org",
        "description": "Brief reviews for working programmers of empirical results in software engineering (2011–2023).",
    },
    {
        "title": "Software Design by Example in Python",
        "url": "@root/sdxpy/",
        "description": "Two dozen worked examples that teach software design by showing how to build the tools that programmers use every day using Python (2024).",
        "image": {"src": "@root/sdxpy/_static/sdxpy-cover.png", "alt": "Software Design by Example in Python"},
    },
    {
        "title": "Software Design by Example in JavaScript",
        "url": "@root/sdxjs/",
        "description": "Twenty worked examples that teach software design by showing how to build the tools that programmers use every day using JavaScript (2022).",
        "image": {"src": "@root/sdxjs/_static/sdxjs-cover.png", "alt": "Software Design by Example in JavaScript"},
    },
    {
        "title": "Research Software Engineering with Python",
        "url": "@root/py-rse/",
        "description": "A textbook on building research software and running research software projects (2021).",
        "image": {"src": "@root/files/bib/py-rse.png", "alt": "Research Software Engineering with Python"},
    },
    {
        "title": "JavaScript for Data Science",
        "url": "@root/js4ds/",
        "description": "An introduction to JavaScript and web programming for data scientists (2020).",
        "image": {"src": "@root/files/bib/js4ds.jpg", "alt": "JavaScript for Data Scientists"},
    },
    {
        "title": "Teaching Tech Together",
        "url": "http://teachtogether.tech",
        "description": "An introduction to evidence-based teaching for people with technical backgrounds (2019).",
        "image": {"src": "@root/files/bib/t3.jpg", "alt": "Teaching Tech Together"},
    },
    {
        "title": "The Architecture of Open Source Applications",
        "url": "https://aosabook.org/",
        "description": "A collection of essays describing the architectures of fifty open source projects (2011–12).",
        "image": {"src": "@root/files/bib/aosa-1.jpg", "alt": "Architecture of Open Source Applications"},
    },
    {
        "title": "Organizational Change",
        "url": "@root/change",
        "description": "This workshop is a short introduction to organizational change for people with backgrounds in research.",
    },
    {
        "title": "Closing Time",
        "url": "@root/closure",
        "description": "This workshop is a short introduction to winding down research and software projects, either deliberately or on short notice.",
    },
    {
        "title": "Introduction to SQL",
        "url": "@root/sql",
        "description": "A one-day introduction to the basics of SQL.",
    },
    {
        "title": "Distributed Systems Design by Example",
        "url": "@root/dsdx",
        "description": "Thirteen worked examples of distributed systems in Python (beta).",
        "beta": True,
    },
    {
        "title": "Unbreaking Software",
        "url": "@root/unbreak",
        "description": "An example-driven tutorial on finding and fixing bugs in software (beta).",
        "beta": True,
    },
    {
        "title": "Learning Web Programming with LLMs",
        "url": "@root/webllm",
        "description": "A short introduction to web programming using LLMs as a teaching aid (alpha).",
        "beta": True,
    },
    {
        "title": "Learning Data Science with LLMs",
        "url": "@root/dsllm",
        "description": "A short introduction to data science using LLMs as a teaching aid (alpha).",
        "beta": True,
    },
    {
        "title": "Research Software Testing by Example",
        "url": "@root/rstx",
        "description": "Thirty-one short examples that explore how to test research software (alpha).",
        "beta": True,
    },
    {
        "title": "Managing Research Software Projects",
        "url": "@root/mrsp",
        "description": "The ideas and tools you need to manage a team of research software developers (alpha).",
        "beta": True,
    },
    {
        "title": "How to Not Be Wrong About AI",
        "url": "@root/notwrong",
        "description": "What software engineers need to understand to tell good studies from bad ones (alpha).",
        "beta": True,
    },
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
