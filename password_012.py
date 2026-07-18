#!/usr/bin/env python3

import sys

for line in sys.stdin:
   line = line.strip()
   has_digit = False
   has_upper = False
   has_lower = False
   has_hash = False
   for char in line:
      if char.isupper():
         has_upper = True
      elif char.islower():
         has_lower = True
      elif char.isdigit():
         has_digit = True
      else:
         has_hash = True
   print(sum([has_lower, has_digit, has_upper, has_hash]))
