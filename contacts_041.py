import sys

input = sys.argv[1]
names = sys.stdin.readlines()
contacts = {}

def check(n):
   for char in n:
      char = char.strip()
      if char in contacts:
         print('Name:', char)
         print('Phone:', contacts[char])
      if char not in contacts:
         print('Name:', char)
         print('No such contact')

with open(input) as inputs:
   inputs = inputs.readlines()
for c in inputs:
   c = c.strip().split()
   contacts[c[0]] = c[1]

check(names)
