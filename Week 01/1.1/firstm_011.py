#!/usr/bin/env python3

import sys

for line in sys.stdin:
   i = 0
   line = line.strip()
   while i < len(line) and line[i] != "m":
      i = i + 1
   if i < len(line):
      print(line[:i] + "M" + line[i + 1:])
   else:
      print(line)






"""
import sys
n = sys.stdin.read().strip()

a = []
i = 0
while n[i] != "m" and i < len(n):
   a.append(n[i])
   i = i + 1
a.append("M")
i = i + 1
while i < len(n):
   a.append(n[i])
   i = i + 1
result = "".join(a)
print(result)
"""
