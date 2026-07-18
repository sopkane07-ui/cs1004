#!/usr/bin/env python3

def get_divisors(n):
  ### 6
   divisors = []
   numbers = range(1, n + 1)
   for char in numbers: ### for i in range(1,n+1):
      if n % char == 0:
         divisors.append(char)
         #print(divisors)
   return divisors

def get_proper_divisors(n):
   divisors = []
   for i in range(1, n):
      if n % i == 0:
         divisors.append(i)
   return divisors ## Returning a variable

def is_perfect(n):
   a = get_proper_divisors(n)
   count = 0
   for char in a:
      count = count + char
   return count == n
   #return sum(get_proper_divisors(n)) == n
