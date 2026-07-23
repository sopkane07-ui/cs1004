import sys


for line in sys.stdin:
   i = ''
   line = line.strip().split()
   #print(line)
   for char in line:
      first = char[0]
      first = first.strip()
      if first.isupper():
         i = i + first
   print(i)

'''
   acro = []
   acro.append(line[0][0])
print(acro)


   for word in line:
      print(word)
      acro = []
      if word[0] >= 'A' and 'Z' >= word[0]:
         acro.append(word[0])
         print(acro)
'''
