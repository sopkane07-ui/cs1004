#!/usr/bin/env python3

odd = []
i = 0
n = input()

while n != "end":
   if int(n) % 2 == 0:
      print(n)
   else:
      odd.append(n)
   n = input()

while i < len(odd):
   print(odd[i])
   i = i + 1
