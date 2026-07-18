#!/usr/bin/env python3

i = 0
j = 0
p = 0
s = input()
a = []
n = []

while s != "end":
  a.append(s)
  n.append(int(s[6:8]))
  s = input()
print(a)

while i < len(a):
  smallest = a[i][6:8]
  while j != len(a):
    if smallest < a[]:
      j = j + 1
    else:
      smallest = n[j]
      p = j
      j = j + 1
  n[p] = n[i]
  n[i] = smallest
  i = i + 1
  p = i
  j = i

print(n)
print(smallest)






