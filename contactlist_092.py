'''
class Contact(object):
   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email
   def __str__(self):
      return f"{self.name} {self.phone} {self.email}"

class Contactlist(object):
   def __init__(self):
      self.d = {}
   def add(self, e):
      self.d[e.name] = e

   def remove(self, name):
      if name in self.d:
         del self.d[name]

   def get(self, name):
      return self.d.get(name)

   def __str__(self):
      result = []
      result.append('Contact list')
      result.append('------------')
      sorted_names = sorted(self.d.keys())
      for name in sorted_names:
         result.append(str(self.d[name]))
      return '\n'.join(result)
'''

class Contact(object):
   def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email
   def __str__(self):
      return f"{self.name} {self.phone} {self.email}"


class Contactlist(object):
   def __init__(self):
      self.list = {}
   def add(self, contact):
      self.list[contact.name] = contact
   def get(self, name):
       return self.list.get(name)
   def remove(self, name):
      if name in self.list:
         del self.list[name]
   def __str__(self):
      list = []
      list.append('Contact list')
      list.append('------------')
      sorted_names = sorted(self.list.keys())
      for c in sorted_names:
         list.append(str(self.list[c]))
      return '\n'.join(list)

