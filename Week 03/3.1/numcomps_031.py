import sys

def multip(n):
   return [n for n in nums if n % 3 == 0]

def square(n):
   return [n ** 2 for n in multiple]

def doub(n):
   return [n * 2 for n in nums if n % 4 == 0]

def threeor(n):
   return [n for n in nums if n % 3 == 0 or n % 4 == 0]

def threeand(n):
   return [n for n in nums if n % 3 == 0 and n % 4 == 0]


for number in sys.stdin:
   number = int(number.strip())
   nums = list(range(1, number + 1))
   multiple = multip(nums)
   print('Multiples of 3:', multiple)
   print('Multiples of 3 squared:', square(multiple))
   print('Multiples of 4 doubled:', doub(nums))
   print('Multiples of 3 or 4:', threeor(nums))
   print('Multiples of 3 and 4:', threeand(nums))
