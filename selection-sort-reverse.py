#!/usr/bin/env python3

i = 0
j = 0
p = 0
s = input()
a = []

while s != "end":
   a.append(int(s))
   s = input()

while i < len(a):
   smallest = a[i]
   while j != len(a):
      if smallest < a[j]:
         j = j + 1
      else:
         p = j
         smallest = a[p]
         j = j + 1
   a[p] = a[i]
   a[i] = smallest
   i = i + 1
   p = i
   j = i

b = a[i::-1]
i = 0
while i < len(a):
   print(b[i])
   i = i + 1
