import sys
import math

def primes(n):
   return [n for n in ranges if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]


for number in sys.stdin:
   nums = int(number.strip())
   ranges = list(range(2, nums + 1))
   print('Primes:', primes(nums))
