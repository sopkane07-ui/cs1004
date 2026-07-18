#!/usr/bin/env python3

p = int(input())
c = int(input())
t1 = 0
t2 = 0

if (p % 2 == 0 and c == p // 2) or (p % 2 == 1 and c == p * 3 + 1):
   t1 = p
   t2 = c

print(t1, t2)
