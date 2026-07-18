# zigzag_052.py

import sys

# Read all lines from stdin and strip newline characters
grid = [line.rstrip('\n') for line in sys.stdin if line.strip()]

if not grid:
   print("")
   sys.exit()

R = len(grid)
C = len(grid[0])

result = []

        # Iterate over each column
for col in range(C):
   for row in range(R):
      if grid[row][col] != '.':
         result.append(grid[row][col])
         break  # Move to next column once letter is found

print("".join(result))
