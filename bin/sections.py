import re
import sys

title = sys.argv[1]
SECTION = re.compile(r'<section\s+markdown="1">(.+?)</section>', re.DOTALL)
text = sys.stdin.read()
for i, section in enumerate(SECTION.findall(text)):
    with open(f"{title}-{i+1:02d}.md", "w") as writer:
        print(section.strip(), file=writer)
