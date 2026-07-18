#!/usr/bin/env python3


prev = input()

if prev == "end":
   curr = prev
   longest_length = 0

else:
   prev = int(prev)
   curr = input()

   curr_length = 1
   longest_length = 1

   while curr != "end":
      curr = int(curr)
      if prev <= curr:
         curr_length = curr_length + 1
      else:
         curr_length = 1
      if longest_length < curr_length:
         longest_length = curr_length
      prev = curr
      curr = input()
print(longest_length)
