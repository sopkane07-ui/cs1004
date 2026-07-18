#!/usr/bin/env python3

xone = int(input())
yone = int(input())
rone = int(input())
xtwo = int(input())
ytwo = int(input())
rtwo = int(input())
if (rone + rtwo) ** 2 > (xtwo - xone) ** 2 + (ytwo - yone) ** 2:
   print("yes")
else:
   print("no")
