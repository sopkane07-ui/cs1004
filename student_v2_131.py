class Student(object):
   def __init__(self, name, cao, prefs=[]):
      self.name = name
      self.cao = cao
      self.prefs = prefs
      self.grades = {}
   def add_preference(self, mod):
      self.prefs.append(mod)
   def add_grade(self, subject, score):
      self.grades[subject] = score
   def get_grade(self, subject):
      for i in self.grades:
         if i == subject:
            return self.grades[i]
   def __str__(self):
      #return f'{self.grades}'
      prefs_str = ', '.join(self.prefs)
      return f'Name: {self.name}\nCAO: {self.cao}\nPreferences: {prefs_str}'
