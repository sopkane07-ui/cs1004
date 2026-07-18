#!/usr/bin/env python3


s = input()
while s != "end":
   if s[0] == s[1]:
      print(s)
      s = "end"
   else:
      s = input()
