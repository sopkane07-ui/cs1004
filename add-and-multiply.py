#!/usr/bin/env python3

s = input()
a = s.split("+")
sum = 0
i = 0

while i < len(a):
  p = a[i].split("*")
  j = 0
  product = 1
  while j < len(p):
    product = product * int(p[j])
    j = j + 1
  sum = sum + product
  i = i + 1
print(sum)
