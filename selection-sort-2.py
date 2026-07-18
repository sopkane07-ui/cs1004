#!/usr/bin/env python3

s = input()
a = []
i = 0
p = 0
while s != "end":
   a.append(int(s))
   s = input()

n = int(input())

i = n
smallest = a[n]
while i < len(a):
   if a[i] <= smallest:
      smallest = a[i]
      p = i
   i = i + 1
print(p)
