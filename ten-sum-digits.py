#!/usr/bin/env python3

i = 0
N = 10
total = 0
LSD = 0

while i < 10:
   n = int(input())
   if n < 0:
      n = n * -1
   LSD = n % 10
   total = total + LSD
   i = i + 1
print(total)
