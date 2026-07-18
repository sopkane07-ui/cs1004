#!/usr/bin/env python3

s = input()
i = 0
t = ""

while i < len(s):
   if "a" <= s[i] and s[i] <= "z":
      o = ord(s[i]) - 32
      t = t + chr(o)
   else:
      t = t + s[i]
   i = i + 1
print(t)
