#!/usr/bin/env python3

filea = {}
disjoint = 0

with open("a.txt") as a:
   linea = a.readlines()

i = 0
while i < len(linea):
   linea[i] = linea[i].rstrip()
   filea[linea[i]] = 1
   i = i + 1

with open("b.txt") as b:
   lineb = b.readlines()

i = 0
while i < len(lineb):
   lineb[i] = lineb[i].rstrip()
   if lineb[i] not in filea:
      disjoint = disjoint + 1
   i = i + 1

if disjoint == len(lineb):
   print("disjoint")
else:
   print("intersecting")
