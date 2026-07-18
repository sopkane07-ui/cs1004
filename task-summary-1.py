#!/usr/bin/env python3

import sys

files = {}

s = sys.stdin.readline().rstrip()

while 0 < len(s):
   tokens = s.split(".")
   files[tokens[0]] = tokens[2]
   print(files)
   s = sys.stdin.readline().rstrip()

for words in files:
   if files[words] == "correct":
      print(words + "." + tokens[1])
      print(files[words])
