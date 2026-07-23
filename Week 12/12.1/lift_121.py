import sys

def main():
   f, s, g, u, d = map(int, sys.stdin.readline().split())
   visited = [False] * (f + 1)
   queue = [(s, 0)]
   front = 0
   visited[s] = True
   while front < len(queue):
      current, steps = queue[front]
      front += 1

      if current == g:
         print(steps)
         return

      up = current + u
      if u > 0 and up <= f and not visited[up]:
         visited[up] = True
         queue.append((up, steps + 1))
      down = current - d
      if d > 0 and down >= 1 and not visited[down]:
         visited[down] = True
         queue.append((down, steps + 1))
   print("Sorry Margo!")

if __name__ == "__main__":
   main()
