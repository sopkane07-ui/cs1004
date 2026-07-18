import sys

file = sys.argv[1]
highest = 0
student = ''


with open(file) as lines:
   for line in lines:
      line = line.strip()
      score = line[:2]

      try:
         if int(score) > int(highest):
            highest = score
            student = line[3:]
      except(ValueError):
         print(f'Invalid mark {score} encountered. Skipping.')
         continue

print(f'Best student: {student}')
print(f'Best mark: {highest}')

