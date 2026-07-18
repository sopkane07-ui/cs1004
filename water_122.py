import sys

def main():
   lines = sys.stdin.read().strip().splitlines()

   N = int(lines[0])

   graph = {}
   for line in lines[1:]:
      if not line.strip():
         continue
      p, q = map(int, line.split())

      if p not in graph:
         graph[p] = []
      if q not in graph:
         graph[q] = []
      graph[p].append(q)
      graph[q].append(p)
   visited = set([1])
   queue = [1]
   front = 0
   while front < len(queue):
      node = queue[front]
      front += 1
      for neigh in graph.get(node, []):
         if neigh not in visited:
            visited.add(neigh)
            queue.append(neigh)
   result = [i for i in range(1, N + 1) if i not in visited]
   print(result)
if __name__ == "__main__":
   main()
