#!/usr/bin/env python3

s = input()
i = 0
total = 0
while i < len(s):
   if "A" <= s[i] and s[i] <= "Z":
      total = total + 1
   i = i + 1
print(total)
