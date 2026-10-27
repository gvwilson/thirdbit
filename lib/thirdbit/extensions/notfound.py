import re

import ark


@ark.filters.register(ark.filters.Filter.OUTPUT_FILEPATH)
def notfound_output_path(filepath, node):
    """Write the root-level 404 node to docs/404.html."""
    if node.path == ["404"]:
        return ark.site.out("404.html")
    return filepath


@ark.filters.register(ark.filters.Filter.PAGE_HTML)
def notfound_absolute_urls(html, page_data):
    """Make URLs absolute, since 404.html is served at any depth."""
    if page_data["node"].path != ["404"]:
        return html
    html = html.replace('"@root/', '"/')
    return re.sub(r'(href|src)="(?![/#]|[a-z][a-z0-9+.-]*:)', r'\1="/', html)
