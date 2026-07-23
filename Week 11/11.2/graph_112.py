class Graph(object):
   def __init__(self, V):
       self.V = V
       self.adj = {}
       for v in range(self.V):
          self.adj[v] = list()

   def addEdge(self, v, w):
      self.adj[v].append(w)
      self.adj[w].append(v)

   def degree(self, v):
      return len(self.adj[v])

   def maxDegree(self):
      ans = []
      for num in self.adj:
         ans.append(len(self.adj[num]))
      return max(ans)

   def avgDegree(self):
      av = []
      average = 0
      for num in self.adj:
         av.append(len(self.adj[num]))
      length = len(av)
      for letters in av:
         average = average + int(letters)
      return average / length
