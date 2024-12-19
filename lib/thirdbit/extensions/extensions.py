import ark
from pathlib import Path
from shutil import copyfile
import yaml


@ark.events.register(ark.events.Event.INIT_BUILD)
def load_data():
    """Load data files."""
    ark.site.config["_data"] = {}
    for filename in Path(ark.site.home(), "data").glob("*.yml"):
        with open(filename, "r") as reader:
            ark.site.config["_data"][filename.stem] = yaml.safe_load(reader)


@ark.filters.register(ark.filters.Filter.BUILD_NODE)
def decide_to_build(value, node):
    """Only build index.html for files, not directories."""
    return Path(node.filepath).is_file()


@ark.events.register(ark.events.Event.EXIT_BUILD)
def copy_files():
    """Copy files from source directories."""
    for pat in ark.site.config["copy"]:
        src_dir = ark.site.src()
        out_dir = ark.site.out()
        for src_file in Path(src_dir).rglob(f"**/{pat}"):
            out_file = str(src_file).replace(src_dir, out_dir)
            Path(out_file).parent.mkdir(exist_ok=True, parents=True)
            copyfile(src_file, out_file)


@ark.filters.register(ark.filters.Filter.LOAD_NODE_FILE)
def translate_file(value, path):
    """Only process .md Markdown files."""
    return path.suffix == ".md"
