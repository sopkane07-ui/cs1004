import sys

"""
highest = 0
student = []

with open(sys.argv[1]) as lines:
   lines = lines.readlines()
   for line in lines:
      line = line.strip()
      score = line[:2]
      if int(score) > int(highest):
         highest = score
         student = line[3:]
      elif int(score) == int(highest):
         student.append(name)

print(f"Best student(s): {', '.join(student)}")
print(f'Best mark: {highest}')
"""

highest = -1
students = []

with open(sys.argv[1]) as f:
   for line in f:
      line = line.strip()
      score = int(line[:2])
      name = line[2:].strip()

      if score > highest:
         highest = score
         students = [name]
      elif score == highest:
         students.append(name)

print(f"Best student(s): {', '.join(students)}")
print(f'Best mark: {highest}')
