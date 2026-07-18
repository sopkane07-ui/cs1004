import sys

def main():
   lines = [line.strip() for line in sys.stdin if line.strip()]
   if not lines:
      print(-1)
      return

   grid = [list(map(int, line.split())) for line in lines]

   M = len(grid)
   N = len(grid[0])
   if M < 3 or N < 3:
      print(-1)
      return
   for i in range(1, M - 1):
      for j in range(1, N - 1):
         val = grid[i][j]
         if (val > grid[i][j - 1] and
            val > grid[i][j + 1] and
            val > grid[i - 1][j] and
            val > grid[i + 1][j]):
            print(val)
            return

if __name__ == "__main__":
   main()


"""
peak = 0
i = 1
lines = sys.stdin.readlines()

for line in lines:
   line = line.strip().split()
   length = len(line)
   line_count = sum(1 for _ in lines)
print(line - 1)
"""

#line_count = sum(1 for _ in lines)
#while i < line_count:
#   print(lines[i])
#   i = i + 1

#for line in lines:
#   line = line.strip()
#   line_count = sum(1 for _ in lines)
   #while i < line_count:
   #   print(lines[i])
   #   i = i + 1
