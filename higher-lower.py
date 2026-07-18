#!/usr/bin/env python3

i = 0
prev = int(input())
cur = 0

while i < 5:
   n = int(input())
   cur = n
   if cur < prev:
      print("lower")
   elif cur > prev:
      print("higher")
   elif cur == prev:
      print("equal")
   prev = cur
   i = i + 1
