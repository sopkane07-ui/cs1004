import sys

#!/usr/bin/env python3

import sys

def squash_line(line):
   result = []
   count = 1
   prev_char = line[0]

   for char in line[1:]:
      if char == prev_char:
         count += 1
      else:
         result.append(f"{count}{prev_char}")
         prev_char = char
         count = 1
      # Append the last sequence
   result.append(f"{count}{prev_char}")

   return "".join(result)


for line in sys.stdin:
   line = line.strip()
   print(squash_line(line))



'''
count = 0
i = 0
for lines in sys.stdin:
   lines = lines.strip().split()
   #print(lines)
   for letter in lines:
      #print(letter[0])
      while i < len(lines):
         if letter[i] == letter[i + 1]:
            print(letter[i])
         i = i + 1
print(count)
'''
