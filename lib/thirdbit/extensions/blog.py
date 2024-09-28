import ark
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

@ark.events.register(ark.events.Event.INIT_BUILD)
def collect_files():
    """Collect blog posts."""
    posts = []
    years = set()
    def _visitor(node):
        if (node.ext == "md") and node.path and (node.path[0].startswith("20")):
            posts.append(node)
            years.add(node.meta["date"].year)

    ark.nodes.root().walk(_visitor)

    posts.sort(key=lambda node: node.meta["date"])
    ark.site.config["_posts"] = posts
    ark.site.config["_years"] = list(sorted(years))

    for i, post in enumerate(posts):
        post["date"] = post.meta["date"]
        if i > 0:
            post["prev"] = posts[i-1]
        if i < len(posts) - 1:
            post["next"] = posts[i+1]


@ark.events.register(ark.events.Event.EXIT_BUILD)
def generate_feed():
    """Generate atom.xml feed."""
    env = Environment(
        loader=FileSystemLoader(Path(ark.site.home(), "lib", ark.site.config["theme"], "templates")),
    )
    template = env.get_template("atom.jinja")
    updated = max(post.meta["date"] for post in ark.site.config["_posts"])
    text = template.render(site=ark.site.config, updated=updated)
    text = text.replace("@root", ark.site.config["url"])
    Path(ark.site.home(), ark.site.config["out_dir"], "atom.xml").write_text(text)
