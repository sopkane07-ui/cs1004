#!/usr/bin/env python3

n = int(input())
i = 0
while i < n:
   s = input()
   j = 0
   if s[j] == s[j + 1]:
      print(s)
   i = i + 1
