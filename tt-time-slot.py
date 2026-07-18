#!/usr/bin/env python3

s = input()
while s != "end":
   b = s.split()
   s = input()
   end = (int(b[2]) + int(b[1]) - 1)
   print(b[0], b[1].lstrip("0") + ":00", str(end) + ":50", " ".join(b[3:]))
