#!/usr/bin/env python3


# run through the sentence and keep all the letters and store it somewhere
# (you are discarding all punchation
#once all punchation is removed it compares the list to its reverse

import sys
#s = sys.stdin.readlines()

def palindrome(s):
   s = s.lower()
   keep = []
   for c in s:
      if c.isalnum():
         keep.append(c)
   return keep == keep[::-1]

for line in sys.stdin:
   print(palindrome(line.strip()))

#dir(str) lists all the methods i can evoke on a string
#str.isalnum
#help(str.isalnum)
