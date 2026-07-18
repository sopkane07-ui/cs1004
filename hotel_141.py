# first number is number of rooms
# list of rooms occupied(the room numbers not the amount)
import sys
line = sys.stdin.readline().strip().split()
rooms = line[0]
occupied = line[1:]
final = []

list_rooms = []
free_rooms = []
for i in range(1, int(rooms)):
   list_rooms.append(i)

for num in list_rooms:
   if str(num) not in occupied:
      free_rooms.append(str(num))

if len(free_rooms) == 0:
    print('no vacancies')
else:
    print(free_rooms[0])
    #print(' '.join(free_rooms[0]))
