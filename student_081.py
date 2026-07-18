class Student(object):
   def set_attributes(self, sid, name, modlist):
      self.sid = sid
      self.name = name
      self.modlist = modlist
   def print_attributes(self):
      print("ID: " + str(self.sid))
      print("Name: " + self.name)
      print("Modules: " + ", ".join(self.modlist))
   def add_module(self, added):
      self.modlist.append(added)
   def del_module(self, delete):
      self.modlist.remove(delete)
