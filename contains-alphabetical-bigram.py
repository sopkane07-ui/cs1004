#!/usr/bin/env python3

import sys

s = sys.stdin.read().split()
i = 0

while i < len(s):
   char = list(s[i])
   j = 0
   order = False
   while j < len(char) - 1:
      if ord(char[j]) == ord(char[j + 1]) - 1:
         order = True
      j = j + 1
   if order is True:
      print("".join(char))
   i = i + 1
