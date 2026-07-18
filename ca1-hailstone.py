#!/usr/bin/env python3

a = int(input())
b = int(input())

if a % 2 == 0:
   if a // 2 == b:
      print("yes")
   else:
      print("no")
elif a % 2 != 0:
   if (a * 3) + 1 == b:
      print("yes")
   else:
      print("no")
