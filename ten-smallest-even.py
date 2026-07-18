#!/usr/bin/env python3

i = 0
N = 10
smallest = int(input())

while i < N - 1:
   n = int(input())
   if n % 2 == 0 and n < smallest:
      smallest = n
   i = i + 1
print(smallest)
