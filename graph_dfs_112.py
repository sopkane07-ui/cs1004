class Graph(object):
   def __init__(self, V):
      self.V = V
      self.adj = [[] for _ in range(V)]

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def adjacent(self, v):
      return self.adj[v]


class DFSPaths(object):

   def __init__(self, g, s):
      self.marked = [False] * g.V
      self.edgeTo = [None] * g.V
      self.s = s
      self.g = g

      self.dfs(s)

   def dfs(self, v):
      self.marked[v] = True

      for w in self.g.adjacent(v):
         if not self.marked[w]:
            self.edgeTo[w] = v
            self.dfs(w)

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
