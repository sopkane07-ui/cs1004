import sys
sys.setrecursionlimit(100000)

def shore_131():
   grid = [list(line.strip()) for line in sys.stdin if line.strip()]
   if not grid:
      return

   M, N = len(grid), len(grid[0])
   visited = [[False] * N for _ in range(M)]

   directions = [(1,0), (-1,0), (0,1), (0,-1)]

   def dfs(i, j):
      visited[i][j] = True

      shoreline = 0

      for di, dj in directions:
         ni, nj = i + di, j + dj
         if ni < 0 or ni >= M or nj < 0 or nj >= N:
            shoreline += 1
         elif grid[ni][nj] == 'W':
            shoreline += 1
         elif grid[ni][nj] == 'L' and not visited[ni][nj]:
            shoreline += dfs(ni, nj)

      return shoreline

   max_shore = 0

   for i in range(M):
      for j in range(N):
         if grid[i][j] == 'L' and not visited[i][j]:
            max_shore = max(max_shore, dfs(i, j))

   print(max_shore)

if __name__ == "__main__":
   shore_131()
