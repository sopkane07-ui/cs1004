#!/usr/bin/env python3

import sys
vowels = {
   "a": True,
   "e": True,
   "o": True,
   "u": True,
   "i": True,
   "A": True,
   "E": True,
   "I": True,
   "O": True,
   "U": True,
}

s = sys.stdin.readlines()
i = 0
count = 0

while i < len(s):
   j = 0
   while j < len(s[i]):
      if s[i][j] in vowels:
         count = count + 1
      j = j + 1
   i = i + 1
print(count)
