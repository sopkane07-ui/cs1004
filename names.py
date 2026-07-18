#!/usr/bin/env python3

import sys
boy = {}
girl = {}

with open("boys.txt") as f:
   t = f.readlines()

i = 0
while i < len(t):
   t[i] = t[i].rstrip()
   boy[t[i]] = "boy"
   i = i + 1

with open("girls.txt") as g:
   h = g.readlines()

i = 0
while i < len(h):
   h[i] = h[i].rstrip()
   girl[h[i]] = "girl"
   i = i + 1

s = sys.stdin.readline().strip()
i = 0
while 0 < len(s):
   if s in girl and s in boy:
      print(s, "either")
   elif s in girl:
      print(s, "girl")
   elif s not in girl:
      print(s, "boy")
   i = i + 1
   s = sys.stdin.readline().strip()
