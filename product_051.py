import sys

def multiply_non_zero_digits(n):
   product = 1
   for digit in str(n):
      if digit != '0':
         product *= int(digit)
   return product


line = sys.stdin.readline().strip()
n = int(line)
while n >= 10:  # Continue until n is a single digit (1–9)
   n = multiply_non_zero_digits(n)
print(n)


'''
line = sys.stdin.readline().strip()
parts = int(line.strip())

first = parts[0] * parts[-1]
print(first)

for num in sys.stdin:
   num = num.strip()
   if len(num) == 3:
      first = (int(num[0]) * int(num[2]))

print(first[0])

      if len(str(first)) == 2:
         second = (int(first[0]) * int(first[1]))
         print(second)
      else:
         print(first)
'''
