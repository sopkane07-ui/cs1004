#!/usr/bin/env python3

s = input()

while s != "end":
   b = s.split()
   s = input()
   c = int(b[2])
   if c > 1:
      print(" ".join(b))
