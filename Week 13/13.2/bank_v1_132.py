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

class Bank(object):
   def __init__(self):
      self.customers = {}
   def add(self, customer):
      self.customers[customer.number] = customer
   def lookup(self, id):
      return self.customers.get(id)
   def remove(self, id):
      if id in self.customers:
         del self.customers[id]










