#!/usr/bin/env python3

i = 0
j = 0
p = 0
a = []
s = input()

while s != "end":
  a.append(int(s))
  s = input()

while i < len(a):
  smallest = a[i]
  while j != len(a):
    if smallest < a[j]:
      j = j + 1
    else:
      smallest = a[j]
      p = j
      j = j + 1
  a[p] = a[i]
  a[i] = smallest
  i = i + 1
  p = i
  j = i

if len(a) % 2 == 0:
  b = len(a) // 2
  print(a[b])
else:
  b = len(a) // 2
  print(a[b])
