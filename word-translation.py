#!/usr/bin/env python3

import sys

file = "translation.txt"
i = 0
words = sys.stdin.read().split()

trans = {}
with open(file) as f:
   while i < len(file):
      t = f.readline().split()
      if t != []:
         trans[t[0]] = t[1]
      i = i + 1

i = 0
while i < len(words):
   word = words[i]
   if word in trans:
      print(trans[word])
   i = i + 1
