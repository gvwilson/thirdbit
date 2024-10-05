import ark
from pathlib import Path

@ark.filters.register(ark.filters.Filter.BUILD_NODE)
def decide_to_build(value, node):
    """Only build index.html for files, not directories."""
    return Path(node.filepath).is_file()
