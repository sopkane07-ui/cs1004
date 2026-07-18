from bank_v2_132 import Customer, Bank

def main():
   c1 = Customer('Alan Wren', 12434655, 100.00)
   c2 = Customer('John Squire', 54211677, 200.22)
   c3 = Customer('Ian Brown', 10145211, 1.50)

   b = Bank()
   b.add(c1)
   b.add(c2)
   b.add(c3)

   print(b)

if __name__ == '__main__':
   main()
