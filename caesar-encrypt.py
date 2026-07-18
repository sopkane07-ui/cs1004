#!/usr/bin/env python3

import sys

i = 0
word = []

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]
letters = {}

while i < len(src):
  letters[src[i]] = dst[i]
  i = i + 1

i = 0
s = sys.stdin.read().strip()
while i < len(s):
  if s[i] in letters:
    word.append(letters[s[i]])
  else:
    word.append(s[i])
  i = i + 1
word = "".join(word)
word = word.rstrip()
print(word)
