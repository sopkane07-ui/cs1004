import sys

def largest_unique(numbers):
   counts = {}
   # Count occurrences
   for n in numbers:
      counts[n] = counts.get(n, 0) + 1

   # Collect numbers that appear exactly once
   uniques = [n for n in numbers if counts[n] == 1]

   if not uniques:
      return "none"

   return str(max(uniques))


for line in sys.stdin:
   line = line.strip()
   if not line:
      continue

   numbers = list(map(int, line.split()))
   print(largest_unique(numbers))



'''
numbers = {}
for line in sys.stdin:
   largest = ''
   line = line.strip()
   for num in line:
      if num.isdigit():
         if num not in numbers:
            numbers[num] = 1
         elif num in numbers:
            numbers[num] = numbers[num] + 1

   for n in numbers:
      if numbers[n] == 1:
         largest = largest + n
   largest = sorted(largest)
   if len(largest) == 0:
      print('none')
   #print(largest)
   print(largest[len(largest)-1])
#print(min(numbers, key=numbers.get))
'''
