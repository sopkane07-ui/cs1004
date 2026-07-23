class Customer(object):
   def __init__(self, name, number, balance=0.0):
      self.name = name
      self.number = number
      self.balance = balance
   def lodge(self, amount):
      self.balance = self.balance + amount
   def withdraw(self, amount):
      if self.balance >= amount:
          self.balance = self.balance - amount
   def __str__(self):
      return f'Name: {self.name}\nNumber: {self.number}\nBalance: {self.balance:.2f}'
