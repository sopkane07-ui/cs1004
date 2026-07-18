#!/usr/bin/env python3

s = input()
a = []
i = 1
while s != "end":
   a.append(int(s))
   s = input()
   smallest = a[0]
while i < len(a):
   if a[i] < smallest:
      smallest = a[i]
   i = i + 1
print(smallest)
