#!/usr/bin/env python3

i = 0
total = 0
n = int(input())

while n != 0:
   if n < 1:
      n = n * -1
   total = total + n
   n = int(input())
   i = i + 1
print(total)
