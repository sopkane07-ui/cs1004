#!/usr/bin/env python3

s = input()
a = []
i = 0
while s != "end":
   b = s.split()
   c = int(b[0])
   a.append(b)
   s = input()
n = input()
while i < len(a):
   if a[i][0] == n:
      print(" ".join(a[i]))
   i = i + 1
