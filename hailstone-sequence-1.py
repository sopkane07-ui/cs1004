#!/usr/bin/env python3

n = int(input())
m = int(input())
a = 0
i = 0
while i < n:
   a = m
   print(a)
   if m % 2 == 0:
      a = m // 2
   else:
      a = (m * 3) + 1
   m = a
   i = i + 1
