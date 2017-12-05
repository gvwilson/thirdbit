#!/usr/bin/env python

import sys
import re

dir_pat = re.compile(r'<!--:\s+([^:]+)\s+:-->')

def dir_func(m):
    text = m.group(1)
    return text

data = sys.stdin.read()
data = dir_pat.sub(dir_func, data)
sys.stdout.write(data)
