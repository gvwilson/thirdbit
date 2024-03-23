import cProfile
import sys

from invperc_single import main  # noqa: F401

sys.argv = ["invperc_single.py", "profile.json"]
cProfile.run("main()", sort="tottime")
