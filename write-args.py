#!/usr/bin/env python3

import sys

file = sys.argv[1]
count = sys.argv[2:]

with open(file, "w") as f:
   i = 0
   while i < len(count):
      f.write(count[i] + "\n")
      i = i + 1
