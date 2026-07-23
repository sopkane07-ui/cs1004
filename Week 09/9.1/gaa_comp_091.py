class Score(object):
   def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points
   def __str__(self):
      return f"{self.goals} goal(s) and {self.points} point(s)"
   def scoretopoints(self):
      return self.goals * 3 + self.points
   def __gt__(self, other):
      return self.scoretopoints() > other.scoretopoints()
   def __eq__(self, other):
      return self.scoretopoints() == other.scoretopoints()
   def __ge__(self, other):
      return self.scoretopoints() >= other.scoretopoints()
