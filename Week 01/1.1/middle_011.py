#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
   line = line.rstrip()
   if len(line) % 2 == 1:
      position = (len(line) // 2)
      print(line[position])
   else:
      print("No middle character!")

