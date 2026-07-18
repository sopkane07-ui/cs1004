#!/usr/bin/env python3

i = 0
j = 0
a = []
p = 0
s = input()

while s != "end":
   a.append(int(s))
   s = input()

while i < len(a):
   smallest = a[i]
   while j != len(a):
      if smallest < a[j]:
         j = j + 1
      else:
         smallest = a[j]
         p = j
         j = j + 1
   a[p] = a[i]
   a[i] = smallest
   i = i + 1
   p = i
   j = i
i = 0
while i < len(a):
   print(a[i])
   i = i + 1
