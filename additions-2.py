#!/usr/bin/env python3

count = 0
j = 0
store = 0
s = input()

while j < len(s):
   while j < len(s) and s[j] != "+":
      j = j + 1
   num = s[store:j]
   count = count + int(num)
   j = j + 1
   store = j
print(count)
