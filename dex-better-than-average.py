#!/usr/bin/env python3

import sys
i = 0
s = sys.stdin.readlines()
count = len(s)
total = 0

while i < count:
   total = total + int(s[i].split()[2])
   i = i + 1
print(total)
