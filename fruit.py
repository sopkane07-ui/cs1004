#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()

fruit = {
   "apple": True,
   "pear": True,
   "cherry": True,
   "banana": True,
   "orange": True,
}

i = 0
while i < len(words):
   word = words[i]
   if word in fruit:
      print(word)
   i = i + 1
