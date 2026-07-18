#!/usr/bin/env python3

i = 0
while i < 10:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j = j + 1
   ls = s[:j]
   rs = s[j + 1:]
   print(int(ls) + int(rs))
   i = i + 1
