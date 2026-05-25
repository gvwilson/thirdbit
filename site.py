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
    {
        "title": "Lean for Python Programmers",
        "url": "@root/l4py",
        "description": "An introduction to Lean for Python programmers (pre-alpha).",
        "beta": True,
    },
]

talks_entries = [
    {
        "title": "Twelve Ways to Be Wrong About AI-Assisted Coding",
        "description": "Outlines twelve common methodological errors in studies claiming to measure the productivity impact of AI coding tools.",
        "updated": "May 2026",
        "links": [
            {"text": "HTML", "url": "@root/talks/12ways/"},
        ],
    },
    {
        "title": "Thirty Years of Python",
        "description": "A personal look at how Python has evolved over three decades and what that evolution has cost in learnability.",
        "updated": "February 2026",
        "links": [
            {"text": "HTML", "url": "@root/talks/py30/"},
        ],
    },
    {
        "title": "Cocaine and Conway's Law",
        "description": "Outlines what a course for programmers on civics and society might contain and how it ought to be presented.",
        "updated": "October 2025",
        "links": [
            {"text": "HTML", "url": "@root/talks/sdgc/"},
            {"text": "video", "url": "https://youtu.be/f86KBeJ7e2M"},
        ],
    },
    {
        "title": "Giving a Tech Talk That Doesn't Suck",
        "description": "A few simple rules (or questions) for giving technical presentations.",
        "updated": "July 2025",
        "links": [
            {"text": "HTML", "url": "@root/talks/tech-talk/"},
        ],
    },
    {
        "title": "Software Engineering's Greatest Hits",
        "description": "Software engineering is turning itself into an evidence-based discipline. This talk describes how, why it matters, and a few interesting findings.",
        "updated": "May 2023",
        "links": [
            {"text": "HTML", "url": "@root/talks/greatest-hits/"},
            {"text": "video", "url": "https://www.youtube.com/watch?v=HrVtA-ue-x0"},
        ],
    },
    {
        "title": "Writing a Technical Book",
        "description": "I've written several technical books and edited several others. This talk summarizes what I've learned that first-time authors might find useful.",
        "updated": "November 2022",
        "links": [
            {"text": "HTML", "url": "@root/talks/writing-book/"},
        ],
    },
    {
        "title": "Software Design for Data Scientists",
        "description": "Many data scientists are self-taught programmers and have never been shown how to think about design in the large. This talk presents ten different approaches, each of which gives different insights.",
        "updated": "July 2021",
        "links": [
            {"text": "HTML", "url": "@root/talks/sd4ds/"},
        ],
    },
    {
        "title": "Teaching Tech Together",
        "description": "Having tried to cram a dozen books about teaching into a two-day course, I have now tried to cram key ideas from that course into this one-hour talk.",
        "updated": "July 2021",
        "links": [
            {"text": "OpenOffice", "url": "@root/files/talks/teaching-learning.odp"},
            {"text": "Google Slides", "url": "https://docs.google.com/presentation/d/1INHfSJzkNpdKonzqYzNlIq6D-H5dyKqs57qoVCAYxB0/"},
            {"text": "video", "url": "https://www.youtube.com/watch?v=ewXvFQByRqY"},
        ],
    },
    {
        "title": "How to Run a Meeting",
        "description": "A few simple rules that can make everyone's life run a little more smoothly.",
        "updated": "July 2020",
        "links": [
            {"text": "OpenOffice", "url": "@root/files/talks/meeting.odp"},
            {"text": "Google Slides", "url": "https://docs.google.com/presentation/d/1HSdgVQjq0d3UYh-aA4uWHXxYYpySn_xXwfn_M4Ms8Ts/"},
            {"text": "video", "url": "https://www.youtube.com/watch?v=5f3-q9SzkeE"},
        ],
    },
    {
        "title": "Late Night Thoughts on Listening to Ike Quebec",
        "description": "Keynote at CarpentryCon 2018 in Dublin.",
        "updated": "May 2018",
        "links": [
            {"text": "HTML", "url": "@root/talks/late-night/"},
            {"text": "video", "url": "https://www.youtube.com/watch?v=7xR50ty5DZ0"},
        ],
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
