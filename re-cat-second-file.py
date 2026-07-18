#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file) as f:
   t = f.readline()
t = t.strip()
with open(t) as g:
   print(g.read().strip())
