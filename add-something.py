#!/usr/bin/env python3

a = []
n = input()
i = 0
while n != "end":
   a.append(int(n))
   n = input()

m = int(input())
while i < len(a):
   print(m + a[i])
   i = i + 1
