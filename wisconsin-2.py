#!/usr/bin/env python3

s = input()
count = 0
while s != "end":
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1
   city = s[i + 1] + s[i + 2]
   if city == "WI":
      count = count + 1
   i = i + 1
   s = input()
print(count)
