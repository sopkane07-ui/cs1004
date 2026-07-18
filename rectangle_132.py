import sys
first = sys.stdin.readline().split()
second = sys.stdin.readline().split()
third = sys.stdin.readline().split()
x = []
y = []
new = []
x.append(first[0])
x.append(second[0])
x.append(third[0])
y.append(first[1])
y.append(second[1])
y.append(third[1])
for i in x:
   number = x.count(i)
   if number == 1:
      new.append(i)

for i in y:
   number = y.count(i)
   if number == 1:
      new.append(i)
print(' '.join(new))
