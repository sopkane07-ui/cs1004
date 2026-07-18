#!/usr/bin/env python3

s = input()
while s != "end":
   i = 0
   while i < len(s):
      j = i
      while j < len(s) and s[j] != " ":
         j = j + 1
      word = s[i:j]
      k = 1
      while k < len(word) and word[k - 1] <= word[k]:
         k = k + 1
      if k == len(word):
         print(word)
      i = j + 1
   s = input()
