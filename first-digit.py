#!/usr/bin/env python3


s = input()
i = 0
t = " "
while s[i] < "0" or "9" < s[i]:
   print("")
if "0" <= s[i] and s[i] <= "9":
   print(s[i])
   i = i + 1
