#!/usr/bin/env python3

import sys
words = {}

s = sys.stdin.readlines()
i = 0
while i < len(s):
   s[i] = s[i].rstrip()
   if s[i] not in words:
      words[s[i]] = 1
   elif s[i] in words:
      words[s[i]] = 2
   i = i + 1

for b in words:
   if words[b] == 1:
      print(b)
