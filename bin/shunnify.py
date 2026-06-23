#!/usr/bin/env python

"""Change header to what's required for Shunn formatting."""

import sys

NEW = """
title: "TITLE"
short_title: "TITLE"
author: "by Greg Wilson"
author_lastname: "Wilson"
contact_name: "Greg Wilson"
contact_address: "65 Highfield Road"
contact_city_state_zip: "Toronto, Ontario M4L 2T9"
contact_phone: "(416) 435-9779"
contact_email: "gvwilson@third-bit.com"
"""

assert len(sys.argv) == 4, "usage: shunnify title infile outfile"
title = sys.argv[1]
text = open(sys.argv[2], "r").read()
assert text.startswith("---")
_, _, body = text.split("---", 2)
header = NEW.strip().replace("TITLE", title)
body = body.lstrip()
result = f"---\n{header}\n---\n{body}"
open(sys.argv[3], "w").write(result)
