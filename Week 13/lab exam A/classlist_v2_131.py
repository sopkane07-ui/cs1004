class Student(object):
   def __init__(self, name, cao, prefs=None):
      self.name = name
      self.cao = cao
      self.prefs = prefs if prefs is not None else []
      self.grades = {}
   def add_preference(self, mod):
      self.prefs.append(mod)
   def add_grade(self, subject, score):
      self.grades[subject] = score
   def get_grade(self, subject):
      for i in self.grades:
         if i == subject:
            return self.grades[i]
   def cao_points(self):
      points = 0
      result = []
      for i in self.grades:
         result.append(self.grades[i])
      result = sorted(result)
      #print(result)
      if len(result) > 0:
         i = 0
         for i in range(3):
            if result[i] == 'H1':
               points = points + 100
            elif result[i] == 'H2':
               points = points + 88
            elif result[i] == 'H3':
               points = points + 77
            elif result[i] == 'H4':
               points = points + 66
            elif result[i] == 'H5':
               points = points + 56
            elif result[i] == 'H6':
               points = points + 46
            elif result[i] == 'H7':
               points = points + 37
            elif result[i] == 'H8':
               points = points + 0
         #print(points)
      return points
   def __str__(self):
      return f'{self.grades}'
'''
       prefs_str = ', '.join(self.prefs)
       return f'Name: {self.name}\nCAO: {self.cao}\nPreferences: {prefs_str}'
'''

class Classlist(object):
   def __init__(self):
      self.students = {}
   def add(self, id):
      self.students[id.cao] = id
   def lookup(self, id):
      return self.students.get(id)
   def remove(self, id):
      if id in self.students:
         del self.students[id]
   def most_popular_degree(self):
      counts = {}
      for student in self.students.values():
         for degree in student.prefs:
            if degree in counts:
               counts[degree] += 1
            else:
               counts[degree] = 1
      most_popular = max(counts, key=counts.get)
      return most_popular
