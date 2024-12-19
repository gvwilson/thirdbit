import ark
from pathlib import Path
from shutil import copyfile


@ark.events.register(ark.events.Event.INIT_BUILD)
def load_projects():
    """Load project snippets."""
    for section, keys in ark.site.config["projects"].items():
        ark.site.config["projects"][section] = {
            key: Path(ark.site.home(), "projects", f"{key}.html").read_text()
            for key in keys
        }


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
