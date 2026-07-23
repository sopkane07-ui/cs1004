'''
import sys

starting = 0
previous = 0
for num in sys.stdin:
   num = int(num.strip())
   check = (starting + num)
   if check < starting:
      starting = (check + previous)
   else:
      previous = num
   #print(check)
   #print(starting)
   #print(previous)
print(starting * -1)
'''
import sys

balance = 0
min_balance = 0

for line in sys.stdin:
   t = int(line.strip())
   balance += t
   if balance < min_balance:
      min_balance = balance
print(-min_balance)
