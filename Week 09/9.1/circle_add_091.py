import math
class Point(object):
   def __init__(self, x=0, y=0):
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

class Circle(object):
   def __init__(self, centre=None, radius=1):
      if centre is None:
         self.centre = Point()
      else:
         self.centre = centre
      self.radius = radius
   def __add__(self, other):
      total_x = (self.centre.x + other.centre.x) / 2
      total_y = (self.centre.y + other.centre.y) / 2
      total_radius = self.radius + other.radius
      new_centre = Point(total_x, total_y)
      return Circle(new_centre, total_radius)
   def __str__(self):
      return f"Centre: {self.centre}\nRadius: {self.radius}"
