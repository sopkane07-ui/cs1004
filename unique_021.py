#!/usr/bin/env python3

import sys
from string import punctuation
text = sys.stdin.read()
keep = []

tokens = text.lower().strip().split()
#print(tokens)
for token in tokens:
   token = token.strip(punctuation) #strips all the punctuation in the words
   if token and token not in keep:
      keep.append(token) # adds it to

#print(keep)
print(len(keep))
