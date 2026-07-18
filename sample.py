#!/usr/bin/env python3

import sys
minimum = 100

a = int(input())
b = int(input())

if a < minimum or b < minimum:
   print("a and b must both be at least", minimum)
   #
   # sys.exit() causes the script to exit immediately.
   #
   sys.exit(1)

while 0 < b:
   r = a % b
   a = b
   b = r
   print(a, b)

print(a)
