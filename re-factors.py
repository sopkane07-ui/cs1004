#!/usr/bin/env python3

import sys
p = sys.argv[1:]
a = []
i = 0
j = 0

s = sys.stdin.read().split()

while j < len(p):
   while i < len(s):
      l = int(s[i])
      command = int(p[j])
      if l % command == 0:
         a.append(l)
      i = i + 1
   j = j + 1


i = 0
while i < len(a):
   print(a[i])
   i = i + 1
