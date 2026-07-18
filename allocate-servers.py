#!/usr/bin/env python3

s = input()
a = []
n = 0

while s != "end":
   a.append(int(s))
   job = 0
   i = 0
   while i < len(a):
      if int(s) <= a[i] + 1000:
         job = job + 1
         if n < job:
            n = job
      i = i + 1
   s = input()
print(n)
