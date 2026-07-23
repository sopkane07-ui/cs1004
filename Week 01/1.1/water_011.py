#!/usr/bin/env python3

import sys


capacity = int(sys.stdin.readline().strip())
buckets = sys.stdin.readline().strip().split()

i = 0
number = 0

while i < len(buckets):
   bucket_size = int(buckets[i])
   if capacity - bucket_size >= 0:
      capacity = capacity - bucket_size
      number = number + 1
   else:
      break
   i = i + 1
print(number)
'''
check = int(capacity)

while i < len(bucket):
   if check - int(bucket[i]) > 0:
      check = check - int(bucket[i])
      number = number + 1
      #print('n', number)
      #print('c', check)
   elif check - int(bucket[i]) < 0:
      print(number)
   i = i + 1
#print(number)

'''


'''
litres = sys.stdin.readline().rstrip()
capacity = sys.stdin.readline().rstrip()
buckets = capacity.split()

total = 0
i = 0
while i < len(buckets):
  total = total + int(buckets[i])
  if total > int(litres):
     final = i
     i = len(buckets)
  elif total > len(buckets):
     final = len(buckets)
  i = i + 1

print(final)
'''
