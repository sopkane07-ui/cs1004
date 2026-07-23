import sys

file = sys.argv[1]
with open(file) as lines:
   lines = lines.readlines()
highest = 0
student = ''

for line in lines:
   line = line.strip()
   score = line[:2]
   if int(score) > highest:
      highest = int(score)
      student = line
print(f'Best student: {student[3:]}')
print(f'Best mark: {highest}')
