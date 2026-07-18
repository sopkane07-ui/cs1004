#!/usr/bin/env python3

N = 10
i = 0
largest = int(input())

while i < N - 1:
   n = int(input())
   if n > largest:
      largest = n
   i = i + 1
print(largest)
