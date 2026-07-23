#!/usr/bin/env python3

import math
import sys

places = sys.stdin.readlines()
for place in places:
   place = place.strip()
   print(f'{math.pi:.{place}f}')
