import ark

@ark.filters.register(ark.filters.Filter.LOAD_NODE_FILE)
def translate_file(value, path):
    """Only process .md Markdown files."""
    return path.suffix == ".md"
