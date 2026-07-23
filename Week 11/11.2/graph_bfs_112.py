class Graph(object):
   def __init__(self, V):
      self.V = V
      self.adj = [[] for _ in range(V)]

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def adjacent(self, v):
      return self.adj[v]

class BFSPaths(object):

   def __init__(self, g, s):
      self.marked = [False] * g.V
      self.edgeTo = [None] * g.V
      self.s = s
      self.g = g
      self.bfs(s)

   def bfs(self, s):
      queue = []

      self.marked[s] = True
      queue.append(s)

      while queue:
         v = queue.pop(0)

         for w in self.g.adjacent(v):
            if not self.marked[w]:
               self.marked[w] = True
               self.edgeTo[w] = v
               queue.append(w)

   def hasPathTo(self, v):
      return self.marked[v]

   def pathTo(self, v):
      if not self.hasPathTo(v):
         return []

      path = []
      x = v
      while x is not None:
         path.append(x)
         x = self.edgeTo[x]

      return path[::-1]
