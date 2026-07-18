#!/usr/bin/env python3

s = input()
while s != "end":
   b = s.split()
   s = input()
   a = int(b[0])
   if a == 3:
      print(" ".join(b[0:]))
