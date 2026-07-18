#!/usr/bin/env python3

i = 0
ans = 0
while ans != 1000:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j = j + 1
   ls = s[:j]
   rs = s[j + 1:]
   ans = (int(ls) + int(rs))
   print(ans)
   i = i + 1
