class Score(object):
   def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points

   def __str__(self):
      return f"{self.goals} goal(s) and {self.points} point(s)"

#   def scoretopoints(self):
#      return self.goals * 3 + self.points

   def __add__(self, other):
      totalgoals = self.goals + other.goals
      totalpoints = self.points + other.points
      return Score(totalgoals, totalpoints)
   def __iadd__(self, other):
      self.goals += other.goals
      self.points += other.points
      return self
