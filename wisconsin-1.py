#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while i < len(s) and s[i] != ",":
      i = i + 1
   city = s[i + 1] + s[i + 2]
   if city == "WI":
      print(s[:i])
   s = input()
