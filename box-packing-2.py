#!/usr/bin/env python3

n = int(input())
total = 0
count = 0
while n != 0:
   if total + n < 1000:
      total = total + n
      n = int(input())
   else:
      total = 0
      count = count + 1
print(count)
