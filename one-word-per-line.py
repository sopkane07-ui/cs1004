#!/usr/bin/env python3

import sys
i = 0
s = sys.stdin.read()

word = ("\n".join(" ".join(s.split("\n")).split()))
print(word)
