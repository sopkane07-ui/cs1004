"""
class Student(object):
   def __init__(self, sid, name, modlist=[]):
      self.sid = sid
      self.name = name
      self.modlist = modlist
   def add_module(self, a):
      self.modlist.append(a)
   def del_module(self, a):
      self.modlist.remove(a)
   def __str__(self):
      return f"ID: {self.sid}"
      return f"Name: {self.name}"
      return f"Modules: {self.modlist}"
"""

class Student:
   def __init__(self, sid, name, modlist=None):
      self.sid = sid
      self.name = name
      if modlist is None:
         self.modlist = []
      else:
         self.modlist = modlist

   def add_module(self, module):
      if module not in self.modlist:
         self.modlist.append(module)

   def del_module(self, module):
      if module in self.modlist:
         self.modlist.remove(module)

   def __str__(self):
      mods = sorted(self.modlist)
      mod_string = ", ".join(mods)
      return f"ID: {self.sid}\nName: {self.name}\nModules: {mod_string}"
