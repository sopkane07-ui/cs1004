#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
for line in lines:
   line = line.strip().split()
   first, second = line
   if first.lower() in second.lower():
      print("True")
   else:
      print("False")


