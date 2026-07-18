#!/usr/bin/env python3

s = input()
i = 0
total = 0

while i < len(s):
   r = s[::-1]
   if r[i] == "1":
      total = total + (1 * (2 ** i))
   i = i + 1
print(total)
