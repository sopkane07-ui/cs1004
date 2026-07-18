#!/usr/bin/env python3

n = int(input())
add = 0
ans = 1
i = 0

while i < n:
   print(add)
   old_ans = ans
   ans = ans + add
   add = old_ans
   i = i + 1
