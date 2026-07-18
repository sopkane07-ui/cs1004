#!/usr/bin/env python3

s = input()
t = ""
i = 0

while i < len(s):
   if ("a" <= s[i] and s[i] <= "z") or ("1" <= s[i] and s[i] <= "9"):
      t = t + s[i]
   i = i + 1
print(t)
