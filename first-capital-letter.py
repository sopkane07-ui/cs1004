#!/usr/bin/env python3

s = input()
i = 0
count = 0
while "a" <= s[i] and s[i] <= "z" or s[i] == " ":
   i = i + 1
if "A" <= s[i] and s[i] <= "Z":
   print(i)
