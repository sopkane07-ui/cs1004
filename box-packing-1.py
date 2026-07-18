#!/usr/bin/env python3

n = int(input())
total = 0
count = 0
while total + n <= 1000:
   total = total + n
   n = int(input())
   count = count + 1
print(count)
