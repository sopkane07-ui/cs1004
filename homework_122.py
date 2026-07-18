import sys

count = 0
line = sys.stdin.readline().strip().split(';')
#print(line)
for char in line:
   if char.isalnum():
      count = count + 1
   else:
      char = char.split('-')
      for i in range(int(char[0]), int(char[1]) + 1):
         count = count + 1
print(count)
