import sys

lines = sys.stdin.readlines()
orders = {}
#print(lines)
for line in lines:
   line = line.strip()
   length = (len(line))
   orders[line] = length
sorted_order = sorted(orders.values())
N = (sorted_order[0])
final = ''
for i in orders:
   if orders[i] == N:
      final += i
      break

print(final)

















'''
names = [line.strip() for line in sys.stdin if line.strip()]

left = []
right = []

i = 0
while i < len(names):
   if i + 1 < len(names):
      left.append(names[i])
      right.append(names[i + 1])
      i += 2
   else:
      left.append(names[i])
      i += 1

result = left + right[::-1]
for name in result:
   print(name)
'''
