#!/usr/bin/env python3

s = input()
i = 0
final = 0
while i < len(s):
   if "A" <= s[i] and s[i] <= "Z":
      final = final + 1
   i = i + 1
print(final)
