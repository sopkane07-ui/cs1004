#!/usr/bin/env python3


import sys

es = ["ch","sh","x","s","z"]
vowel = ["a","e","i","o","u"]

for line in sys.stdin:
   line = line.strip()
   if line[-2:] in es or line[-1:] in es:
      print(line + "es")
   elif line[-2:-1] not in vowel and line[-1:] == "y":
      print(line[:len(line) - 1] + "ies")
   elif line[-1:] == "o":
      print(line + "es")
   elif line[-2:] == "fe":
      print(line[:len(line) - 2] + "ves")
   elif line[-1:] == "f":
      print(line[:len(line) - 1] + "ves")
   elif line[-1:] == "o":
      print(line + "es")
   else:
      print(line + "s")


'''
import sys

es = ['ch', 'sh', 'x', 's', 'z', 'o']
f = ['fe', 'f']

for word in sys.stdin:
   word = word.strip()
   lastes = (word[len(word)-2:])
   for char in es:
      if lastes in char:
         wordes = (word + "es")
   for charf in f:
      if lastes in charf:
         wordes = (word + "ves")
   print(wordes)
   lastf = (word[len(word)-2:])
   #print(lastf)


for line in sys.stdin:
   word = ''
   line = line.strip()
   #lastes = (line[len(line)-2:])
   #print(lastes)
   for e in es:
      if line.endswith(e):
         word = (line + 'es')
   for char in f:
      if line.endswith(char):
         word = line.replace(char, 'ves', 1)
   print(word)
'''

#(str.endswith) = returns true if ends in multiple strings
# es_end = ('es', 's')
# if word.endswith(es_endings):
#    word = word + 'es'
