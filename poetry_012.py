#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

longest = 0
for long in lines:
   long = (long.strip())
   if len(long) >= longest:
      longest = len(long)

for line in lines:
   line = (line.strip())
   l = (len(line))
   print(f'{line:^{longest}.{l}}')
