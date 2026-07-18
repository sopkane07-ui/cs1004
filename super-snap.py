#!/usr/bin/env python3

import sys
word = sys.stdin.readline().rstrip()
snap = {}
stop = 0

while 0 < len(word) and stop != 1:
   if word not in snap:
      snap[word] = + 1
   elif word in snap:
      print("snap:", word)
      stop = 1
   if stop != 1:
      word = sys.stdin.readline().rstrip()
