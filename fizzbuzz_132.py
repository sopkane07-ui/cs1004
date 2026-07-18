import sys

line = sys.stdin.readline().split()

f = int(line[0])
b = int(line[1])
if f == b:
   fb = f
else:
   fb = f * b
i = 1
while i < (int(line[2]) + 1):
   #f = int(line[0])
   #b = int(line[1])
   #if f == b:
   #   fb == f
   #else:
   #   fb = f * b
   if i % fb == 0:
      print('fizzbuzz')
   elif i % f == 0:
      print('fizz')
   elif i % b == 0:
      print('buzz')
   else:
      print(i)
   i = i + 1
