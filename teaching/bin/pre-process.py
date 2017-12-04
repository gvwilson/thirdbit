#!/usr/bin/env python

import sys
import re

DIRECTIVES = r'<!--\|\s+([^-]+)\s+\|-->'

def directives(match):
    latex = match.group(1)
    return latex

data = sys.stdin.read()
data = re.sub(DIRECTIVES, directives, data, re.DOTALL)
sys.stdout.write(data)
