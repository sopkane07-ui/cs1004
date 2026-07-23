"""
class File(object):
   def __init__(self, file_name):
      self.d = {}
      self.l = []
      self.file_name = file_name

   def add_line(self, s):
      self.l.append(s)

   def add_permission(self, name, per):
      self.d[name] = per

   def del_permission(self, name, delete):
      def self.d[name]

   def __str__(self):
      return f"File: {self.file_name}\n{self.l}"
"""

class File(object):
   def __init__(self, name):
      self.name = name
      self.content = []
      self.permissions = {}

   def add_line(self, line):
      self.content.append(line)

   def add_permission(self, user, perm):
      if user not in self.permissions:
         self.permissions[user] = set()
      self.permissions[user].add(perm)

   def del_permission(self, user, perm):
      if user in self.permissions and perm in self.permissions[user]:
         self.permissions[user].remove(perm)
         if len(self.permissions[user]) == 0:
            del self.permissions[user]

   def can_read(self, user):
      return user in self.permissions and 'r' in self.permissions[user]

   def can_write(self, user):
      return user in self.permissions and 'w' in self.permissions[user]

   def __str__(self):
      result = f"File: {self.name}"
      if self.content:
         result += "\n" + "\n".join(self.content)
      if self.permissions:
         result += "\nPermissions:"
         for user in sorted(self.permissions):
            perms = sorted(self.permissions[user])
            result += f"\n{user}: {', '.join(perms)}"

      return result
