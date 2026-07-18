#!/usr/bin/env python3

n = int(input())
if n == 2 or n == 3:
   print("prime")
elif n % n == 0 and n >= 2 and n % 2 != 0 and n % 3 != 0:
   print("prime")
else:
   print("not prime")
