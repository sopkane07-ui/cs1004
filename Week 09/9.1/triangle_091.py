import math
class Point(object):
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def midpoint(self, other):
      xpoint = (self.x + other.x) / 2
      ypoint = (self.y + other.y) / 2
      return Point(xpoint, ypoint)

   def distance(self, other):
      return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

   def __str__(self):
     return f"({self.x:.1f}, {self.y:.1f})"

class Triangle(object):
   def __init__(self, a, b, c):
     self.a = a
     self.b = b
     self.c = c

   def side_lengths(self):
     AB = self.a.distance(self.b)
     AC = self.a.distance(self.c)
     BC = self.b.distance(self.c)
     return [AB, AC, BC]

   def perimeter(self):
     return sum(self.side_lengths())

   def right_angle_triangle(self):
     sides = sorted(self.side_lengths())
     return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
'''

class Point(object):
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def midpoint(self, other):
      pointx = (other.x + self.x) / 2
      pointy = (other.y + self.y) / 2
      return Point(pointx, pointy)
   def distance(self, other):
      return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
   def __str__(self):
      return f'({self.x:.1f}, {self.y:.1f})'

class Triangle(object):
   def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
   def side_length(self):
      AC = self.a.distance(self.c)
      AB = self.a.distance(self.b)
      BC = self.b.distance(self.c)
      return
   def perimeter(self):
      return (AC + AB + BC)





'''










