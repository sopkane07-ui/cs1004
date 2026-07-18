#!/usr/bin/env python3

import sys

for email in sys.stdin:
   email = email.strip()
   names = email.split(".")
   second = names[1].split("@")
   i = 0
   while i < len(second[0]) and (second[0][i] < "0" or second[0][i] > "9"):
      i = i + 1
   print(names[0].capitalize() + " " + second[0][:i].capitalize())



"""
import sys

lines = sys.stdin.readlines()

for line in lines:
   second = line.split("@")
   #print(second)
   first = second[0].split(".")
   #print(first)
   name1, name2 = first
   print(name1)
   print(name2)
   hi = 2
   if hi.isdigit():
      print("yes")
   else:
      print("no")
   #first = line.strip().split(".")
   #print(first[0])"""
