#!/usr/bin/env python3

s = input()
a = []
b = []
while s != "end":
   a.append(s)
   s = input()
n = input()
while n != "end":
   b.append(n)
   n = input()
c = a + b
print(c)
