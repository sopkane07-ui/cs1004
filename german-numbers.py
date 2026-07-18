#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
i = 0
trans = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

while i < len(words):
   word = words[i]
   if word in trans:
      print(trans[word])
   i = i + 1
