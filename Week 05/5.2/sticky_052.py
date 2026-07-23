#!/usr/bin/env python3

import sys

def find_sticky_keys(typed, shown):
   sticky = set()

   i = 0  # index for typed
   j = 0  # index for shown

   while i < len(typed) and j < len(shown):
      if j + 1 < len(shown) and shown[j] == shown[j + 1] and shown[j] == typed[i]:
         sticky.add(typed[i])
         i += 1
         j += 2
      elif shown[j] == typed[i]:
         i += 1
         j += 1
      else:
         # If input is valid according to the problem,
         # this case should not occur.
         j += 1

   return "".join(sorted(sticky))

typed = sys.stdin.readline().rstrip("\n")
shown = sys.stdin.readline().rstrip("\n")

print(find_sticky_keys(typed, shown))



'''
words = []
sticky = {}

typed = sys.stdin.readline().strip()
words.append(typed)
print(words)

for output in sys.stdin:
   output = output.strip()
   for char in output:
      if char in words:
      #   words.replace(char, 1, ' ')
print(words)
'''
