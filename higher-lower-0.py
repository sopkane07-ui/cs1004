#!/usr/bin/env python3

prev = int(input())
while prev != 0:
   cur = int(input())
   if cur == 0:
      prev = 0
   elif prev < cur:
      print("higher")
   elif prev > cur:
      print("lower")
   elif prev == cur:
      print("equal")
   prev = cur
