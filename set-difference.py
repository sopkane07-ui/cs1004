#!/usr/bin/env python3

files = {}

with open("b.txt") as b:
   lineb = b.readlines()

i = 0
while i < len(lineb):
   lineb[i] = lineb[i].rstrip()
   files[lineb[i]] = 1
   i = i + 1


with open("a.txt") as a:
   linea = a.readlines()

i = 0
while i < len(linea):
   linea[i] = linea[i].rstrip()
   if linea[i] not in files:
      print(linea[i])
   i = i + 1
