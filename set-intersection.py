#!/usr/bin/env python3

files = {}
seen = {}

with open("a.txt") as a:
   linea = a.readlines()

i = 0
while i < len(linea):
   linea[i] = linea[i].rstrip()
   files[linea[i]] = 1
   i = i + 1

with open("b.txt") as b:
   lineb = b.readlines()

i = 0
while i < len(lineb):
   lineb[i] = lineb[i].rstrip()
   if lineb[i] in files:
      seen[lineb[i]] = 1
   i = i + 1

for words in seen:
   print(words)
