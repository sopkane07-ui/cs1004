class Student(object):
   def __init__(self, name, id, module):
      self.name = name
      self.id = id
      self.module = [module[0][0], module[1][0]]
      self.score = round((module[0][1] + module[1][1]) / 2)
   #def change(self):
     # m = [(module[0][0]), (module[1][0])]
     # return Student(m)
   #   self.module = module[0][0]
   #   return self
   def __str__(self):
      sorted_value = sorted(self.module)
      return f"Name: {self.name}\nID: {self.id}\nModules: {sorted_value[0]}, {sorted_value[1]}\nAverage mark: {self.score}"
