#!/usr/env/bin python3

import sys

lines = sys.stdin.readlines()

for line in lines:
   chopped = (line.strip()[1:len(line) - 2])
   if chopped:
      print(chopped)


