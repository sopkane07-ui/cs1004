#!/usr/bin/env python3

a = []
s = input()
i = 0
total = 0
while s != "end":
   a.append(s)
   s = input()
total = total + len(a)
while i < len(a):
   print(i, total, a[i])
   i = i + 1
