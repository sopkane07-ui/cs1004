#!/usr/bin/env python3

i = 0
s = input()
store = 0
while i < len(s):
   while i < len(s) and s[i] != ",":
      i = i + 1
   word = s[store:i]
   print(word)
   i = i + 1
   store = i
