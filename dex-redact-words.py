#!/usr/bin/env python3

import sys
i = 0

words = sys.argv[1:]

s = sys.stdin.read().split()


while i < len(s):
   word = s[i]
   if word in words:
      print("*" * len(word))
   else:
      print(word)
   i = i + 1
