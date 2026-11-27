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

projects = [
    {
        "title": "The Carpentries",
        "url": "https://carpentries.org",
        "description": "A non-profit organization teaching basic software and data skills to researchers world-wide (1998–present).",
        "image": {"src": "@root/files/carpentries-hex.jpg", "alt": "Carpentries logo"},
    },
    {
        "title": "It Will Never Work in Theory",
        "url": "http://neverworkintheory.org",
        "description": "Brief reviews for working programmers of empirical results in software engineering (2011–2023).",
        "image": {"src": "@root/files/neverworkintheory.svg", "alt": "NWIT logo"},
    },
]

books = [
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
        "image": {"src": "@root/sdxjs/images/sdxjs-cover.png", "alt": "Software Design by Example in JavaScript"},
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
]

workshops = [
    {
        "title": "Organizational Change",
        "url": "@root/change",
        "description": "An introduction to organizational change for people with backgrounds in research.",
    },
    {
        "title": "Closing Time",
        "url": "@root/closure",
        "description": "How to wind down research and software projects, either deliberately or on short notice.",
    },
    {
        "title": "Teaching Tech Together",
        "url": "https://teachtogether.tech/",
        "description": "A one-day introduction to modern teaching practices for programmers and data scientists.",
    },
    {
        "title": "Managing Research Software Projects",
        "url": "@root/mrsp",
        "description": "Ideas and tools you need to manage a team of research software developers.",
    },
]

beta = [
    {
        "title": "Introduction to SQL",
        "url": "@root/sql",
        "description": "A one-day introduction to the basics of SQL.",
    },
    {
        "title": "Unbreaking Software",
        "url": "@root/unbreak",
        "description": "An example-driven tutorial on finding and fixing bugs in software.",
        "beta": True,
    },
    {
        "title": "Sex and Drugs and Guns and Code",
        "url": "@root/sdgc",
        "description": "A few things I think programmers should know about how the world actually works.",
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
