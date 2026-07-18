#!/usr/bin/env python3

import random

maximum = 999
secret = random.randint(0,maximum)

N = 10
guesses = N
correct = False
print("secret:", secret)
def guess(n):
   global guesses, correct
   guesses -= 1
   print("guess {} (guess {} of {}, {} remaining)".format(n, N - guesses, N, guesses))
   if guesses < 0:
      raise Exception("error: too many guesses")
   correct = (n == secret)
   if n < secret:
      return "too-low"
   elif secret < n:
      return "too-high"
   else:
      return "correct"
