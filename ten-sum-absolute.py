#!/usr/bin/env python3

N = 10
i = 0
total = 0

while i < N:
   n = int(input())
   if n < 0:
      n = n * -1
   i = i + 1
   total = total + n
print(total)
