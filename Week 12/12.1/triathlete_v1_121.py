class Triathlete:
   def __init__(self, name, tid):
      self.name = name
      self.tid = tid
   def __str__(self):
      return f'Name: {self.name}\nID: {self.tid}'
