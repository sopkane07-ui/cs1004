#!/usr/bin/env python3

s = input()
while s != "end":
   b = s.split()
   s = input()
   print(" ".join(b[5:]))
