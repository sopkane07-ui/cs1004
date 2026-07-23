import sys

line = sys.stdin.readline().strip()

parts = line.split()
min = int(parts[0])
current = int(parts[1])
max = int(parts[2])
#print(min, current, max)

new = current
for command in sys.stdin:
   command = command.strip()
   #print(new)
   if command == 'UP':
      #print(new)
      if new == max:
         new == max
      else:
         new = new + 1
   elif command == 'DOWN':
      if new == min:
         new = min
      else:
         new = new - 1
print(new)

