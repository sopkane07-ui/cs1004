class Student(object):
   def __init__(self, name, id, module):
      self.name = name
      self.id = id
      self.module = [module[0][0], module[1][0]]
      self.score = round((module[0][1] + module[1][1]) / 2)
   def __str__(self):
      sorted_value = sorted(self.module)
      return f"Name: {self.name}\nID: {self.id}\nModules: {sorted_value[0]}, {sorted_value[1]}\nAverage mark: {self.score}" 
class Classlist(object):
   def __init__(self):
      self.d = {}
   def add(self, s):
      self.d[s.score] = s
#self.d[e.name] = e
   def __str__(self):
      result = []
      sorted_values = sorted(self.d.keys(), reverse=True)
      #print(sorted_values)
      for num in sorted_values:
         result.append(str(self.d[num]))
      return '\n'.join(result)
