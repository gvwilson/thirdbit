"""Ark configuration file."""

title = "Snail Percolation"
data_dir = "../../data/assays"

theme = "snails"
src_dir = "src"
out_dir = "docs"
extension = "/"

markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
