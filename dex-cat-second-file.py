#!/usr/bin/env python3

import sys

args = sys.argv[1]

with open(args) as f:
   t = f.readline().strip()

with open(t) as g:
   m = g.read().strip()
print(m)
