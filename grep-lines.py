#!/usr/bin/env python3

import sys
grep = sys.argv[1]

s = input()
while s != "end":
   i = 0
   while i < len(s) and s[i:i + len(grep)] != grep:
      i = i + 1
   if i < len(s):
      print(s)
   s = input()
