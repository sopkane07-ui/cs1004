'''
class Point(object):
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def midpoint(self, other):
      xpoint = (self.x + other.x) / 2
      ypoint = (self.y + other.y) / 2
      return Point(xpoint, ypoint)

   def __str__(self):
      return f"({self.x:.1f}, {self.y:.1f})"
'''

class Point(object):
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def midpoint(self, other):
      pointx = (other.x + self.x) / 2
      pointy = (other.y + self.y) / 2
      return Point(pointx, pointy)
   def __str__(self):
      return f'({self.x:.1f}, {self.y:.1f})'



















