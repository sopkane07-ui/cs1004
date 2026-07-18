#!/usr/bin/env python3

s = input()
count = 0
while s != "end":
   b = s.split()
   s = input()
   hour = int(b[2])
   count = count + hour
print(count)
