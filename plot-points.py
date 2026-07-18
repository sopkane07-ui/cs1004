#!/usr/bin/env python3

import sys

points = {}
x = [] * 20
y = [] * 20
s = sys.stdin.readline().rstrip()
while len(s) > 0:
   tokens = s.split()
   x[tokens[0]] = tokens[0]
   s = sys.stdin.readline().rstrip()

print(x, y)
