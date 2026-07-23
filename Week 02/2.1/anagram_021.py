#!/usr/bin/env python3

import sys

for line in sys.stdin:
   line = line.strip().split()
   first, second = line
   for char in first:
      if char in second:
         first = first.replace(char, '', 1)
         second = second.replace(char, '', 1)
   if len(first) == 0 and len(second) == 0:
      print('True')
   else:
      print('False')


'''
def anagram(line):
   ag = line.strip().split()
   first, second = ag
   for letter in first:
      if letter in second:
         second = second.replace(letter, '', 1)
         first = first.replace(letter, '', 1)
   if len(second) == 0 and len(first) == 0:
      print("True")
   else:
      print("False")

anagrams = sys.stdin.read().strip().splitlines()
for line in anagrams:
   anagram(line)
'''




"""
for c in left:
   if c not in right:
      return false
   right = right.replace(c, '', 1)
return not right

for line in lines:
   left, right = line.strip().lower().split()
"""
