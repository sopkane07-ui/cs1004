#!/usr/env/bin python3

import sys

lines = sys.stdin.readlines()

for line in lines:
   line = line.rstrip()
   if line[0] >= "A" and line[0] <= "Z":
      first = line[0]
      middle = line[1:len(line) - 1]
      last = ord(line[len(line) - 1]) - 32
      print(first + middle + chr(last))
   else:
      first = ord(line[0]) - 32
      middle = line[1:len(line) - 1]
      last =  ord(line[len(line) - 1]) - 32
      print(chr(first) + middle + chr(last))

