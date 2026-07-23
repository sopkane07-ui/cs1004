import sys

#names = sys.stdin.readlines()
inputs = sys.argv[1]
contacts = {}

with open(inputs) as input:
   input = input.readlines()


for char in input:
   char = char.strip().split()
   contacts[char[0]] = char[1:]

for names in sys.stdin:
   names = names.strip()
   if names in contacts:
      print('Name:', names)
      print('Phone:', contacts[names][0])
      print('Email:', contacts[names][1])
   if names not in contacts:
      print('Name:', names)
      print('No such contact')
