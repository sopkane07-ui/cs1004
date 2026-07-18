class BankAccount:
   def __init__(self, balance=0):
      self.balance = float(balance)
      self.transactions = []
      self.opening_balance = float(balance)

   def deposit(self, amount):
      self.balance += amount
      self.transactions.append((amount, "deposit", self.balance))

   def withdraw(self, amount):
      self.balance -= amount
      self.transactions.append((-amount, "withdrawal", self.balance))

   def __str__(self):
      if len(self.transactions) <= 3:
         opening = self.opening_balance
         shown = self.transactions
      else:
         shown = self.transactions[-3:]
         opening = shown[0][2] - shown[0][0]

      s = f"Opening balance: {opening:.2f} euros\n"

      for amount, typ, bal in shown:
         if typ == "deposit":
            s += f"{amount:.2f} deposit for a new balance of {bal:.2f}\n"
         else:
            s += f"{amount:.2f} withdrawal for a new balance of {bal:.2f}\n"
      s += f"Current balance: {self.balance:.2f} euros"
      return s
