import sys

def main():
   F, S, G, U, D = map(int, sys.stdin.read().split())
   visited = [False] * (F + 1)
   queue = [(S, 0)]
   visited[S] = True
   while queue:
      floor, steps = queue.pop(0)
      if floor == G:
         print(steps)
         return
      up = floor + U
      if up <= F and not visited[up]:
         visited[up] = True
         queue.append((up, steps + 1))
      down = floor - D
      if down >= 1 and not visited[down]:
         visited[down] = True
         queue.append((down, steps + 1))
   print("Sorry Margo!")


if __name__ == "__main__":
   main()
