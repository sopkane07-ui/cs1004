#!/usr/bin/env python3

import sys

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0
src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

words = {}
while i < len(src):
   words[src[i]] = dst[i]
   i = i + 1


s = sys.stdin.readline().strip()
while 0 < len(s):
   i = 0
   a = ""
   while i < len(s):
      if s[i] in words:
         a = a + words[s[i]]
      if s[i] not in words:
         a = a + s[i]
      i = i + 1
   s = sys.stdin.readline().rstrip()
   b = "".join(a)
   print(b)
