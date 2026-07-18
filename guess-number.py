#!/usr/bin/env python3

import secret

s = secret.guess(500)

min = 0
max = 1000
guess = 500
while s != "correct":
   if s == "too-high":
      max = guess
   else:
      min = guess
   s = secret.guess((max + min) // 2)
   guess = (max + min) // 2
