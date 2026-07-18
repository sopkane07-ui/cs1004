"""
import sys
lines = sys.stdin.readlines()

for line in lines:
   print(line.strip().split(':')
   hours, mins = line.strip().split(':')
   hours, mins = int(hours), int(mins)
   total_mins = hours * 60 + mins
   print(total_mins)
   total_mins -= 47
   print(total_mins)
   if total_mins < 0:
      total_mins += 24 * 60
"""
import sys

for line in sys.stdin:
   line = line.strip()
   #if not line:
   #   continue
   hours, minutes = (map(int, line.split(":")))

   total_minutes = hours * 60 + minutes
   total_minutes = (total_minutes - 47) % (24 * 60)

   new_hours = total_minutes // 60
   new_minutes = total_minutes % 60

   print(f"{new_hours:02d}:{new_minutes:02d}")


