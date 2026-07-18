#!/usr/bin/env python3

s = input()
total = ""
s = int(s)
while s != 0:
   total = total + (s % 2)
   s = s // 2
print(total)
