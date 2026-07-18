#!/usr/bin/env python3

n = int(input())
tp = 0
tn = 0

while n != 0:
   if n < 1:
      tn = tn + n
   else:
      tp = tp + n
   n = int(input())
print(tn, tp)
