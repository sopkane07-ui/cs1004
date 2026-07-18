#!/usr/bin/env python3

s = input()
i = 0
t = ""

while i < len(s):
   if "a" <= s[i] and s[i] <= "z":
      u = ord(s[i]) - 32
      t = t + chr(u)
   elif "A" <= s[i] and s[i] <= "Z":
      l = ord(s[i]) + 32
      t = t + chr(l)
   i = i + 1
print(t)
