#!/usr/bin/env python3

i = 0
tp = 0
tn = 0

while i < 5:
   n = int(input())
   if n < 1:
      tn = tn + n
   else:
      tp = tp + n
   i = i + 1
print(tn, tp)
