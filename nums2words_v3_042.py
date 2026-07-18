import sys

with open(sys.argv[1]) as lines:
   lines = lines.readlines()

english = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
irish = {}

#print(numbers)
for line in lines:
   line = line.strip().split()
   irish[line[0]] = line[1]
#print(irish)


for nums in sys.stdin:
   final = ''
   nums = nums.strip().split()
   for num in nums:
      translate = english[num]
      final = final + ' ' + irish[translate]
   print(final.strip())
