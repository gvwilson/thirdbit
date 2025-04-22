---
title: Lazy Loading a Data Package
date: 2025-04-21
---

*Later: see the bottom of this post for a much less frightening solution.*

R has the notion of a "data package",
which looks and feels like a code package
except its primary purpose is to provide a dataset.
One of the key features of such packages is that the data isn't loaded into memory
unless and until it's needed,
which is known as *lazy loading*.
The code below shows my attempt to do this in Python;
I'd [be grateful](mailto:gvwilson@third-bit.com) for pointers to prior art
and advice on how to simplify it.

## Desired Outcome

Importing the package does *not* load the data.
Instead,
each dataset in the package is loaded into memory the first time it is referenced.

```python
import example                # data not loaded
print(example.machines)       # 'machines' data loaded here
print(example.persons)        # 'persons' data loaded here
```

## What the Package Author Writes

The programmer who wants to provide the data package must:

1.  define a class derived from `BaseDatasetLoader`
    with a zero-argument method for each dataset;

1.  mark those methods as [cached properties](https://docs.python.org/3/library/functools.html#functools.cached_property);

1.  call their classes' `install` method with their module's name as an argument;
    and

1.  put their data files in a directory called `data` in the top level of their project.

For example,
the package `example` that provides persons and machines would be structured like this:

```
.
├── data
│   ├── machines.csv
│   └── persons.csv
├── example
│   └── __init__.py
└── pyproject.toml
```

Here's the code in `__init__.py`:

```python
from functools import cached_property
from datapkg.package import BaseDatasetLoader

class _Loader(BaseDatasetLoader):
    """Example dataset loader."""

    @cached_property
    def machines(self):
        return self.load_csv("machines.csv")
    
    @cached_property
    def persons(self):
        return self.load_csv("persons.csv")

# Set up lazy loading - automatically discovers cached properties
_Loader.install(__name__)
```

I'd like to find a way to automate the installation step
so that programmers only have to define the class,
but I haven't figured out a way yet.

## Behind the Curtain

The `datapkg` library defines three things,
two of which programmers (hopefully) won't need to know about.
The thing they *do* need to be aware of is
the base class from which their data loader classes are derived.
For demo purposes,
`BaseDatasetLoader` assumes (i.e., requires) that data lives in a `data` directory
beside the package source code directory
and that there is a cached property in the user-defined class derived from `BaseDatasetLoader`
corresponding to each of the datasets:

```python
class BaseDatasetLoader:
    """Base class for dataset loaders."""

    # Where datasets are located.
    DATA_DIR = "data"
        
    @classmethod
    def discover_cached_properties(cls):
        """Discover all cached_property attributes in this class (i.e., datasets)."""

        return [
            name for name, attr in inspect.getmembers(cls)
            if (not name.startswith("_")) and isinstance(attr, cached_property)
        ]
    
    @classmethod
    def install(cls, package_name):
        """Set up lazy loading for a data package."""

        loader_instance = cls()
        exported_names = cls.discover_cached_properties()
        create_lazy_package(package_name, loader_instance, exported_names)
    
    def load_csv(self, filename):
        """Load data from a CSV file."""

        with resources.files(BaseDatasetLoader.DATA_DIR).joinpath(filename).open("r") as stream:
            return [r for r in csv.reader(stream)]
```

`BaseDatasetLoader` relies on `create_lazy_package`,
which looks up a module and replaces it with a lazy-loading module,
copying over the attributes of the original model along the way
and then exporting all the module's names:

```python
def create_lazy_package(package_name, loader, names=None):
    """Set up lazy loading for a data package."""

    original_module = sys.modules[package_name]
    lazy_module = LazyModule(package_name, loader)
    lazy_module.__dict__.update(original_module.__dict__)
    sys.modules[package_name] = lazy_module
    lazy_module.__all__ = [] if names is None else names
```

Finally,
`LazyModule` intercepts attempts to get the module's attributes
and defers them to the user-defined class derived from `BaseDatasetLoader`:

```python
class LazyModule(types.ModuleType):
    """A module that lazily loads datasets when attributes are accessed."""
    
    def __init__(self, name, loader):
        """Initialize a lazy module."""

        super().__init__(name)
        self._loader = loader
    
    def __getattr__(self, name):
        """Get an attribute from the loader when not found in the module."""

        try:
            return getattr(self._loader, name)
        except AttributeError as exc:
            raise AttributeError(f"Module '{self.__name__}' has no attribute '{name}'") from exc
```

## Building the Package

Life's not complete these days without a `pyproject.toml` file:

```python
[project]
name = "example"
version = "0.1.0"
description = "An example data package"
dependencies = []
requires-python = ">=3.11"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["datapkg"]

[tool.hatch.build.force-include]
"data" = "data"
```

The trick is that last line,
which forces the build system to include the contents of the `data` directory in the package.
(And yes, both uses of the word `data` in that line must be quoted:
it's TOML's way of defining a key-value table.
I miss my `package.json` files every day…)

## The Simpler Version

The solution described above is very complex,
and it would be unreasonable to expect most data scientists to debug subtle mistakes.
If we are willing to use:

```python
from datapkg import datapkg
print(datapkg.machines)
```

then the `pyproject.toml` file stays as it is and the Python becomes:

```python
import csv
from functools import cached_property
from importlib import resources

DATA_DIR = "data"

class _loader:

    @cached_property
    def machines(self):
        return _load_csv("machines.csv")

    @cached_property
    def persons(self):
        return _load_csv("persons.csv")

    
def _load_csv(filename):
    """Load data from a CSV file."""
    print(f"loading {filename}")
    with resources.files(DATA_DIR).joinpath(filename).open("r") as stream:
        return [r for r in csv.reader(stream)]

datapkg = _loader()

__all__ = ["datapkg"]
```

## The Even Simpler Version

Nat Knight suggested an even simpler approach:
use [a module-level `__getattr__` function][pep-0562].
I didn't even know these existed,
but they make the code _much_ easier to understand:

```python
import csv
from importlib import resources

DATA_DIR = "data"
AVAILABLE = {
    "machines": {"filename": "machines.csv", "cached": None},
    "persons": {"filename": "persons.csv", "cached": None},
}


def __getattr__(name):
    if name not in AVAILABLE:
        raise AttributeError(f"{__name__} does not have {name}")
    entry = AVAILABLE[name]
    if entry["cached"] is None:
        entry["cached"] = _load_csv(entry["filename"])
    return entry["cached"]

    
def _load_csv(filename):
    with resources.files(DATA_DIR).joinpath(filename).open("r") as stream:
        return [r for r in csv.reader(stream)]
```

Thanks, Nat—this is what I'm going with.
But also:
damn,
I remember when Python was a small enough language that I actually understood it…

[pep-0562]: https://peps.python.org/pep-0562/
